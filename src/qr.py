"""Tiny dependency-free QR code generator (byte mode, error correction M, versions 1-6).

    import qr; svg = qr.svg("https://example.com/")

Used by make.py to bake the share QR code into the page as an inline SVG.
Follows ISO/IEC 18004 (same structure as Nayuki's reference implementation).
"""

# version: (ec codewords per block, [data codewords per block, ...]) for level M
_M = {1: (10, [16]), 2: (16, [28]), 3: (26, [44]), 4: (18, [32, 32]),
      5: (24, [43, 43]), 6: (16, [27, 27, 27, 27])}
_ALIGN = {1: [], 2: [6, 18], 3: [6, 22], 4: [6, 26], 5: [6, 30], 6: [6, 34]}


def _gmul(x, y):
    z = 0
    for i in range(7, -1, -1):
        z = (z << 1) ^ ((z >> 7) * 0x11D)
        z ^= ((y >> i) & 1) * x
    return z


def _rs_divisor(deg):
    res = [0] * (deg - 1) + [1]
    root = 1
    for _ in range(deg):
        for j in range(deg):
            res[j] = _gmul(res[j], root)
            if j + 1 < deg:
                res[j] ^= res[j + 1]
        root = _gmul(root, 2)
    return res


def _rs_remainder(data, div):
    res = [0] * len(div)
    for b in data:
        f = b ^ res.pop(0)
        res.append(0)
        for i, c in enumerate(div):
            res[i] ^= _gmul(c, f)
    return res


def _codewords(text):
    raw = text.encode("utf-8")
    for ver in range(1, 7):
        ec, blocks = _M[ver]
        cap = sum(blocks)
        if 4 + 8 + 8 * len(raw) <= cap * 8:
            break
    else:
        raise ValueError("text too long for this small QR encoder")
    bits = [0, 1, 0, 0] + [(len(raw) >> i) & 1 for i in range(7, -1, -1)]
    for b in raw:
        bits += [(b >> i) & 1 for i in range(7, -1, -1)]
    bits += [0] * min(4, cap * 8 - len(bits))
    bits += [0] * (-len(bits) % 8)
    data = [int("".join(map(str, bits[i:i + 8])), 2) for i in range(0, len(bits), 8)]
    pad = 0xEC
    while len(data) < cap:
        data.append(pad)
        pad ^= 0xEC ^ 0x11
    div = _rs_divisor(ec)
    dblocks, eblocks, k = [], [], 0
    for n in blocks:
        d = data[k:k + n]
        k += n
        dblocks.append(d)
        eblocks.append(_rs_remainder(d, div))
    out = []
    for i in range(max(blocks)):
        out += [d[i] for d in dblocks if i < len(d)]
    for i in range(ec):
        out += [e[i] for e in eblocks]
    return ver, out


def _matrix(text):
    ver, cw = _codewords(text)
    n = ver * 4 + 17
    mod = [[False] * n for _ in range(n)]
    fn = [[False] * n for _ in range(n)]

    def put(x, y, dark):
        mod[y][x] = dark
        fn[y][x] = True

    for i in range(n):  # timing patterns
        put(6, i, i % 2 == 0)
        put(i, 6, i % 2 == 0)
    for cx, cy in ((3, 3), (n - 4, 3), (3, n - 4)):  # finders + separators
        for dy in range(-4, 5):
            for dx in range(-4, 5):
                x, y = cx + dx, cy + dy
                if 0 <= x < n and 0 <= y < n:
                    put(x, y, max(abs(dx), abs(dy)) not in (2, 4))
    al = _ALIGN[ver]
    for i, ax in enumerate(al):
        for j, ay in enumerate(al):
            if (i == 0 and j == 0) or (i == 0 and j == len(al) - 1) or (i == len(al) - 1 and j == 0):
                continue
            for dy in range(-2, 3):
                for dx in range(-2, 3):
                    put(ax + dx, ay + dy, max(abs(dx), abs(dy)) != 1)

    def fmt(mask):
        d = (0 << 3) | mask  # level M = 00
        r = d
        for _ in range(10):
            r = (r << 1) ^ ((r >> 9) * 0x537)
        b = ((d << 10) | r) ^ 0x5412
        bit = lambda i: (b >> i) & 1 == 1
        for i in range(6):
            put(8, i, bit(i))
        put(8, 7, bit(6))
        put(8, 8, bit(7))
        put(7, 8, bit(8))
        for i in range(9, 15):
            put(14 - i, 8, bit(i))
        for i in range(8):
            put(n - 1 - i, 8, bit(i))
        for i in range(8, 15):
            put(8, n - 15 + i, bit(i))
        put(8, n - 8, True)

    fmt(0)  # reserve format areas
    i, right = 0, n - 1
    while right >= 1:
        if right == 6:
            right = 5
        for vert in range(n):
            for j in range(2):
                x = right - j
                y = n - 1 - vert if ((right + 1) & 2) == 0 else vert
                if not fn[y][x] and i < len(cw) * 8:
                    mod[y][x] = (cw[i >> 3] >> (7 - (i & 7))) & 1 == 1
                    i += 1
        right -= 2

    masks = [lambda x, y: (x + y) % 2 == 0, lambda x, y: y % 2 == 0, lambda x, y: x % 3 == 0,
             lambda x, y: (x + y) % 3 == 0, lambda x, y: (x // 3 + y // 2) % 2 == 0,
             lambda x, y: x * y % 2 + x * y % 3 == 0, lambda x, y: (x * y % 2 + x * y % 3) % 2 == 0,
             lambda x, y: ((x + y) % 2 + x * y % 3) % 2 == 0]

    def masked(m):
        g = [row[:] for row in mod]
        for y in range(n):
            for x in range(n):
                if not fn[y][x] and masks[m](x, y):
                    g[y][x] = not g[y][x]
        return g

    def penalty(g):
        p = 0
        for lines in (g, list(map(list, zip(*g)))):  # rule 1: runs of 5+
            for row in lines:
                run = 1
                for a, b in zip(row, row[1:]):
                    run = run + 1 if a == b else 1
                    if run == 5:
                        p += 3
                    elif run > 5:
                        p += 1
        for y in range(n - 1):  # rule 2: 2x2 blocks
            for x in range(n - 1):
                if g[y][x] == g[y][x + 1] == g[y + 1][x] == g[y + 1][x + 1]:
                    p += 3
        dark = sum(map(sum, g))  # rule 4: balance
        p += abs(dark * 20 - n * n * 10) // (n * n) * 10
        return p

    best = None
    for m in range(8):
        fmt(m)
        g = masked(m)
        s = penalty(g)
        if best is None or s < best[0]:
            best = (s, m)
    fmt(best[1])
    return masked(best[1])


def svg(text, dark="#2a1c0a", light="#fbf4e2", quiet=4):
    g = _matrix(text)
    n = len(g) + 2 * quiet
    path = "".join(f"M{x + quiet} {y + quiet}h1v1h-1z"
                   for y, row in enumerate(g) for x, v in enumerate(row) if v)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {n} {n}" shape-rendering="crispEdges" '
            f'role="img" aria-label="QR code for {text}"><rect width="{n}" height="{n}" fill="{light}"/>'
            f'<path d="{path}" fill="{dark}"/></svg>')


if __name__ == "__main__":
    import sys
    for row in _matrix(sys.argv[1] if len(sys.argv) > 1 else "HELLO"):
        print("".join("██" if v else "  " for v in row))
