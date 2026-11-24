# TPA 1882 interactive mind map: project notes for Claude

## What this is
An interactive single-file HTML study guide and mind map of the **Transfer of Property Act, 1882**, covering s.5 to s.55, plus s.3 (definitions) and s.56 (marshalling). It is by **Madhi Lokanath**, a BBA LL.B. student at KIIT School of Law, for the Property Law (LW 3019) assignment. Marks are 7 for the work and 3 for distributing it to classmates. Reply to the user in English, even if he writes in Hindi.

**Final deliverable:** `dist/index.html`, the "old statute book" edition. It is one self-contained file that works offline, with fonts loaded from Google Fonts and fallbacks when offline.

## Build
```
python build_all.py              # rebuilds dist/classic.html, then dist/index.html
python build_all.py --textures   # also regenerates the paper/wood/leather textures (numpy, pillow)
python tools/screenshot_test.py  # Playwright smoke test: screenshots + JS errors
```
Every file is UTF-8. build_all.py sets PYTHONUTF8=1, so it works on Windows.

## Pipeline (src/)
1. `bare_raw.json`: bare-act text per section, extracted from `source/` by `tools/extract.py`.
2. `g1.py` … `g10.py`: the hand-written content per section. The dict `S[sid]` holds:
   - `tag`: syllabus / linked / beyond;
   - `simple`, `deep`;
   - `dissect`: the elements, each with its own illustration;
   - `master`: the master illustration;
   - `ills`, `exam`, `quiz`, `links`, `next`.

   The files split the sections like this:
   - g1: s.3, 5–9
   - g2: s.10–12
   - g3: s.13–18, 20
   - g4: s.19, 21–24
   - g5: s.25–34
   - g6: s.35–37
   - g7: s.38–43
   - g8: s.44–51
   - g9: s.52, 53, 53A
   - g10: s.54–56
3. `extra1.py` / `extra2.py`: `why` ("Why the law says this"), `flow` (decision flowchart) and `conf` ("Don't confuse with") for every section.
4. `build.py`: merges the above and fixes typos in the bare act (`FIX`). It renders the bare act with the dissect phrases highlighted (`render_bare`) and adds `NOTES`. It writes `content.json`.
5. `crisp.py`: the 16 mind-map branches (`BRANCH`) and their section groupings (`C`).
6. `make.py`: injects the JSON into `template.html` and writes `dist/classic.html`.
7. `make_old.py`: builds the old-book edition from classic.html:
   - swaps in `old_style.css` and `oldfx.py` (CSS for the torn paper edges, textures and book cover);
   - adds the cover-opening animation;
   - writes `dist/index.html`.
8. `tex.py`: generates tileable JPEG textures into `tex.json`. oldfx.py inlines each one once, as a CSS variable.

To edit content, change the g*/extra* files, then rebuild. Never hand-edit dist/.

## Locked decisions (the user approved these; don't change them without asking)
- **Content:**
  - No case law.
  - Very detailed illustrations: a master illustration plus one per element.
  - Every section has Why / Flowchart / Don't-confuse-with.
  - The bare act stays hidden behind a tap.
  - Syllabus / linked / beyond tags.
- **Views:** the default is the drill-down bubble mind map. The "Detailed" view (branch cards with section chips) sits behind the switch near the title.
- **Title:**
  - "Transfer of Property Act, 1882", "by Madhi Lokanath".
  - The title font is IM Fell English SC, not blackletter.
- **Old-book look:**
  - light textured paper with torn edges on a wooden desk;
  - leather book cover with "Press here to open the book", which pulses;
  - the cover opens with a 3D page turn and respects prefers-reduced-motion.
- **Mind-map bubbles:** stadium-shaped pills so the text never overflows. Branches are numbered from 1 (no "§ 0").
- **Detailed-view connector lines:**
  - wide screens: a centre spine with curves;
  - 860px or narrower: a left trunk plus horizontal ticks.

  Lines must never cross the cards or labels.

## Performance rules (the user reported lag once; it was fixed)
- No `filter: drop-shadow` on large or masked elements.
- No `background-attachment: fixed`.
- No SVG feTurbulence backgrounds; use the raster textures from tex.json.
- The map re-renders only when the width changes. Connector redraws are throttled with requestAnimationFrame.

## Gotchas
- In the claude.ai artifact viewer, `history.replaceState` throws a SecurityError. Always go through `setHash()` (try/catch). The smoke test simulates this.
- Hash routes: `#s-<sid>` opens a section directly and skips the cover.

## Possible next steps
- Deploy as a small website: Netlify Drop (drag the dist/ folder), or GitHub Pages / Vercel from this folder.
- Add a share button or QR code for classmates.
