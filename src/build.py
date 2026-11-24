import json, re, html, importlib, sys
B = json.load(open('bare_raw.json'))

FIX = {
 '6': [('(d)All interest', '(d)An interest'), ('military naval', 'military, naval')],
 '10': [('a women', 'a woman')],
 '17': [('under the transferor;', 'under the transfer;')],
 '27': [('in his life-time, transfer to B', 'in his life-time, transfers to B')],
 '29': [('cannot, take effect', 'cannot take effect'), ('dies as minor', 'dies a minor')],
 '30': [('if she does not desert her husband to C', 'if she do not desert her husband, to C')],
 '37': [('Rs. 7.50', 'Rs. 7½'), ('a contract, to the contrary', 'a contract to the contrary')],
 '40': [('enjoymentin', 'enjoyment in'), ('orOr of obligation annexed to ownership but not amounting to interest or easement.—', 'or\n<i>Or of obligation annexed to ownership but not amounting to interest or easement.</i>—'), ('not against such property', 'nor against such property')],
 '46': [('for a quarter share of mauza. There', 'for a quarter share of mauza Lalpura. There'), ('share in the mauza', 'share in that mauza')],
 '51': [('and he subsequently evicted', 'and he is subsequently evicted'), ('to sell interest', 'to sell his interest')],
 '52': [('suit or proceedings which', 'suit or proceeding which')],
 '55': [('buye of', 'buyer of'), ('encumbrance', 'incumbrance'), ('encumbered', 'incumbered')],
 '56': [('mortgaged-debt', 'mortgage-debt')],
 '36': [('all rents annuities', 'all rents, annuities')],
 '44': [('necessary to give, effect', 'necessary to give effect')],
}
NOTES = {
 '6': 'Your Indian Kanoon copy reads "All interest" in clause (d); the government text reads "An interest".',
 '10': 'Your Indian Kanoon copy has a typo, "a women"; corrected to "a woman".',
 '17': 'Your Indian Kanoon copy reads "under the transferor" in sub-section (2)(i); the government text reads "under the transfer".',
 '27': 'Your Indian Kanoon copy reads "transfer to B" in illustration (b); the government text reads "transfers to B".',
 '29': 'Your Indian Kanoon copy has a stray comma ("cannot, take effect") and reads "dies as minor"; the government text reads "dies a minor".',
 '30': 'Your Indian Kanoon copy reads "if she does not desert her husband to C"; the government text reads "if she do not desert her husband, to C".',
 '40': 'Your Indian Kanoon copy reads "not against such property"; the correct text is "nor against such property".',
 '46': 'Your Indian Kanoon copy drops the word "Lalpura" from illustration (a); restored here.',
 '51': 'Your Indian Kanoon copy drops "is" and "his" in two places; restored here.',
 '53A': 'This is the current text. The 2001 amendment (Act 48 of 2001) removed the words "the contract, though required to be registered, has not been registered, or". Older printed copies still show them.',
 '55': 'Your Indian Kanoon copy has a typo, "buye"; corrected. The Act spells it "incumbrance".',
 '56': 'Your Indian Kanoon copy reads "mortgaged debt"; the Act reads "mortgage-debt".',
 '52': 'Both the Indian Kanoon and government copies show the words "excluding the State of Jammu and Kashmir". Check the current India Code text if your professor asks about it.',
}

def clean(sid):
    t = B[sid]['body']
    t = re.split(r'\s+4\. Enactments relating', t)[0]
    t = re.sub(r'\s*Chapter [IVX]+\s+Of .*$', '', t, flags=re.S | re.I)
    t = re.sub(r'\s*\(B\)\s*Transfer of Immoveable Property.*$', '', t, flags=re.S)
    t = t.replace('the law4 for', 'the law for')
    for a, b in FIX.get(sid, []):
        if a not in t:
            print('FIX MISSING', sid, a); continue
        t = t.replace(a, b)
    return t.strip()

def pat(phrase):
    ph = phrase.strip().replace('’', '\x01').replace("'", '\x01')
    ph = re.sub(r'[“”"]', '\x02', ph)
    p = re.escape(ph).replace('\\ ', r'\s*')
    p = p.replace('\x01', "['’]").replace('\x02', '[“”"]')
    return re.compile(p, re.I)

def fmt(t):
    t = re.sub(r'([.;:,])(?=[A-Z“"(])', r'\1 ', t)
    t = re.sub(r';(?=[a-z])', '; ', t)
    t = re.sub(r'([a-z])\(((?:[a-z]{1,2}|[ivx]{1,4}|\d{1,2}))\)', r'\1 (\2)', t)
    t = re.sub(r'\((?:[a-z]{1,2}|[ivx]{1,4}|\d{1,2})\)(?=[A-Za-z])', lambda m: m.group(0)+' ', t)
    t = re.sub(r'\s*(Illustrations?|Explanation\s*[IVX]*\s*\.?—|\(Exception\)—|Exception\.?—)', r'\n\n\1', t)
    for lb in [r'(?<=[—;:.,])', r'(?<= or)', r'(?<= and)']:
        t = re.sub(lb + r'\s*(\((?:[a-z]{1,2}|[ivx]{1,4}|\d{1,2})\))\s*', r'\n\1 ', t)
    t = re.sub(r'\s*(Provided that)', r'\n\n\1', t)
    t = re.sub(r';\s*“', ';\n\n“', t)
    t = re.sub(r'(?<=[.;])\s+([A-Z][A-Za-z ,]{3,60}\.)—', r'\n\n<i>\1</i>—', t)
    return t

def render_bare(sid, dissect):
    t = fmt(clean(sid))
    out = []
    marks = []
    for i, (ph, note) in enumerate(dissect, 1):
        m = pat(ph).search(t)
        if not m:
            print(f'PHRASE NOT FOUND s.{sid}: {ph[:70]}')
            continue
        marks.append((m.start(), m.end(), i))
    marks.sort()
    res, pos, last_end = '', 0, -1
    keep = []
    for s, e, i in marks:
        if s < last_end:
            print(f'OVERLAP s.{sid} #{i}'); continue
        keep.append((s, e, i)); last_end = e
    for s, e, i in keep:
        res += t[pos:s] + f'⟦{i}⟧' + t[s:e] + f'⟦/{i}⟧'
        pos = e
    res += t[pos:]
    res = html.escape(res, quote=False).replace('&lt;i&gt;', '<i>').replace('&lt;/i&gt;', '</i>')
    res = re.sub(r'⟦(\d+)⟧', r'<span class="mk" data-k="\1">', res)
    res = re.sub(r'⟦/(\d+)⟧', lambda m: f'<sup>{m.group(1)}</sup></span>', res)
    res = res.replace('\n', '<br>')
    return res

if __name__ == '__main__':
    data = {}
    for g in sys.argv[1:]:
        mod = importlib.import_module(g)
        for sid, s in mod.S.items():
            s['bare_html'] = render_bare(sid, s['dissect'])
            s['bare_head'] = B[sid]['head']
            s['note'] = NOTES.get(sid, '')
            data[sid] = s
    import extra1, extra2
    EX = {**extra1.E, **extra2.E}
    for sid in data:
        if sid not in EX: print('NO EXTRA', sid)
        else: data[sid].update(EX[sid])
    json.dump(data, open('content.json', 'w'), ensure_ascii=False)
    print('sections:', sorted(data, key=lambda x: (int(re.sub(r'\D', '', x)), x)))
