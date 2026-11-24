# Transfer of Property Act, 1882: Interactive Mind Map
by Madhi Lokanath

An interactive study guide for TPA s.5–55 (plus s.3 and s.56). Each section has a plain-language explanation, illustrations, a decision flowchart, "Don't confuse with", exam points, a quiz and the bare act behind a tap.

## Open it
Online: **https://mlokanath2007-sketch.github.io/tpa-mindmap/** (tap **Share** on the site for a QR code).

Offline: double-click `dist/index.html`. It works in any browser, on a phone or a laptop.

## Rebuild after editing
```
python build_all.py
```
Content lives in `src/g1.py` … `src/g10.py` and `src/extra1.py` / `src/extra2.py`. See `CLAUDE.md` for the full map of the project.

## Folder layout
```
dist/       index.html (final old-book edition), classic.html (plain edition)
src/        content, template, styles and build scripts
tools/      bare-act extractor, checker, screenshot smoke test
source/     bare-act source text
```
