"""Rebuild the whole site in one go.

    python build_all.py            # content -> classic.html -> index.html (old-book)
    python build_all.py --textures # also regenerate paper/wood/leather textures first

Outputs:
    dist/index.html    final old-book edition (the one to share)
    dist/classic.html  plain hand-drawn edition (also the base the old-book one is built from)
"""
import os, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
ENV = {**os.environ, "PYTHONUTF8": "1"}  # Windows-safe: all files are UTF-8


def run(*args):
    print(">", " ".join(args))
    subprocess.run([sys.executable, *args], cwd=SRC, env=ENV, check=True)


if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
    if "--textures" in sys.argv:
        run("tex.py")  # needs numpy + pillow
    run("build.py", *[f"g{i}" for i in range(1, 11)])
    run("make.py")
    run("make_old.py")
    print("Done -> dist/index.html")
