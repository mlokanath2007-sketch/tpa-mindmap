import random, urllib.parse, json
TX=json.load(open('tex.json'))
PAPER="var(--ptex)"; WOOD="var(--wtex)"; LEATH="var(--ltex)"
TEXVARS=f":root{{{{--ptex:url('{TX['paper']}');--wtex:url('{TX['wood']}');--ltex:url('{TX['leather']}')}}}}"
random.seed(7)
def uri(svg): return "url(\"data:image/svg+xml," + urllib.parse.quote(svg) + "\")"
# paper grain: fine noise + soft blotches
grain = """<svg xmlns='http://www.w3.org/2000/svg' width='320' height='320'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .35  0 0 0 0 .24  0 0 0 0 .1  0 0 0 .55 0'/></filter><rect width='100%' height='100%' filter='url(#n)' opacity='.38'/></svg>"""
blot = """<svg xmlns='http://www.w3.org/2000/svg' width='900' height='900'><filter id='b'><feTurbulence type='fractalNoise' baseFrequency='.012' numOctaves='4' seed='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .55  0 0 0 0 .38  0 0 0 0 .14  0 0 0 1.1 -.48'/></filter><rect width='100%' height='100%' filter='url(#b)' opacity='.55'/></svg>"""
fiber = """<svg xmlns='http://www.w3.org/2000/svg' width='600' height='600'><filter id='f'><feTurbulence type='turbulence' baseFrequency='.004 .09' numOctaves='2' seed='9' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .4  0 0 0 0 .3  0 0 0 0 .15  0 0 0 .9 -.35'/></filter><rect width='100%' height='100%' filter='url(#f)' opacity='.35'/></svg>"""
wood = """<svg xmlns='http://www.w3.org/2000/svg' width='1600' height='600'><filter id='w'><feTurbulence type='fractalNoise' baseFrequency='.0025 .35' numOctaves='3' seed='4' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .16  0 0 0 0 .09  0 0 0 0 .04  0 0 0 .9 0'/></filter><rect width='100%' height='100%' fill='#2a1a0e'/><rect width='100%' height='100%' filter='url(#w)'/></svg>"""
leather = """<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='l'><feTurbulence type='fractalNoise' baseFrequency='.55' numOctaves='3' seed='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .08  0 0 0 0 .03  0 0 0 0 .02  0 0 0 .65 0'/></filter><rect width='100%' height='100%' fill='#5a1712'/><rect width='100%' height='100%' filter='url(#l)'/></svg>"""
def edge(side, L=160, D=16):
    pts=[]; n=26
    xs=[random.uniform(1,D-5) for _ in range(n)]; xs[-1]=xs[0]
    for i,x in enumerate(xs):
        t=i*L/(n-1)
        if random.random()<.18: x=random.uniform(0,3)
        pts.append((x,t))
    if side=='L': poly=[(D,0)]+[(x,t) for x,t in pts]+[(D,L)]; w,h=D,L
    if side=='R': poly=[(0,0)]+[(D-x,t) for x,t in pts]+[(0,L)]; w,h=D,L
    if side=='T': poly=[(0,D)]+[(t,x) for x,t in pts]+[(L,D)]; w,h=L,D
    if side=='B': poly=[(0,0)]+[(t,D-x) for x,t in pts]+[(L,0)]; w,h=L,D
    p=" ".join(f"{a:.1f},{b:.1f}" for a,b in poly)
    return uri(f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}' preserveAspectRatio='none'><polygon points='{p}' fill='#000'/></svg>")
E={k:edge(k) for k in 'LRTB'}
paper_bg = PAPER
mask = (f"{E['L']} left top/16px 160px repeat-y, {E['R']} right top/16px 160px repeat-y, "
        f"{E['T']} left top/160px 16px repeat-x, {E['B']} left bottom/160px 16px repeat-x, "
        "linear-gradient(#000,#000) center/calc(100% - 30px) calc(100% - 30px) no-repeat")
CSS = TEXVARS.replace("{{","{").replace("}}","}") + f"""
/* ---- real paper, torn edges, desk ---- */
:root{{color-scheme:light}}
body{{background:#24170c;background-image:{WOOD};background-size:1024px 512px}}
.pagewrap{{max-width:1220px;margin:clamp(12px,3vw,36px) auto}}
.page{{position:relative;background-color:#f3ead3;background-image:{paper_bg};background-size:512px 512px;box-shadow:inset 0 0 40px rgba(120,80,30,.32);-webkit-mask:{mask};mask:{mask}}}
.wrap{{border:none;outline:none;background:transparent;margin:0 auto;padding:clamp(34px,4vw,60px) max(5vw,26px) 60px}}
.wrap::before{{content:"";position:absolute;inset:22px;border:1px solid rgba(110,80,40,.55);outline:1px solid rgba(110,80,40,.35);outline-offset:4px;pointer-events:none}}
.reader{{background:#24170c;background-image:{WOOD};background-size:1024px 512px}}
.rpage{{max-width:940px;margin:14px auto 40px}}
.rpage>.rwrap{{border:none;outline:none;margin:0;background-color:#f3ead3;background-image:{paper_bg};background-size:512px 512px;box-shadow:inset 0 0 40px rgba(120,80,30,.32);-webkit-mask:{mask};mask:{mask};padding:40px max(5vw,26px) 70px}}
.sticky,.card,.panel,.quiz .q,.bare,.kcard,.master,.exam,.whybox,.fq,.fy,.fx,.fend,.next,.search input,.crumbs button,.btn,.switch,.chip{{background-color:rgba(250,244,228,.6)}}
.branch{{background-color:#f6eedb}}
.bub,.centre{{background-color:#f6eedb}}
.btn.pri,.switch button[aria-pressed=true],.crumbs button[aria-current],.chip.match{{background-color:#33240f}}
.limb>.lt{{background:rgba(243,234,211,.96)}}
/* ---- cover ---- */
.cover-ov{{position:fixed;inset:0;z-index:20;display:flex;align-items:center;justify-content:center;background:#1b1109;background-image:{WOOD};background-size:1024px 512px;perspective:1800px;transition:opacity .6s ease}}
.cover-ov.gone{{opacity:0;pointer-events:none}}
.book{{position:relative;width:min(440px,84vw);aspect-ratio:3/4.2;transform-style:preserve-3d}}
.book .inner{{position:absolute;inset:0;background-color:#f3ead3;background-image:{paper_bg};background-size:512px 512px;border-radius:2px 8px 8px 2px;box-shadow:0 18px 40px rgba(0,0,0,.6);display:flex;align-items:center;justify-content:center;text-align:center;padding:30px;color:#33240f;font-family:"IM Fell English",serif;font-size:20px;font-style:italic}}
.lid{{position:absolute;inset:0;transform-origin:left center;transition:transform 1.5s cubic-bezier(.6,.05,.25,1);transform-style:preserve-3d;cursor:pointer;border:0;padding:0;background:none}}
.lid .front,.lid .back{{position:absolute;inset:0;backface-visibility:hidden;border-radius:3px 10px 10px 3px}}
.lid .front{{background-color:#5a1712;background-image:{LEATH};background-size:256px 256px;box-shadow:inset 10px 0 18px rgba(0,0,0,.55),inset -3px 0 6px rgba(255,220,160,.12),0 18px 40px rgba(0,0,0,.6);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:34px 30px;color:#e8c77a;text-align:center}}
.lid .front::before{{content:"";position:absolute;inset:16px;border:2px solid rgba(232,199,122,.75);outline:1px solid rgba(232,199,122,.5);outline-offset:6px;border-radius:4px}}
.lid .back{{transform:rotateY(180deg);background-color:#efe3c4;background-image:{PAPER};background-size:512px 512px;box-shadow:inset -12px 0 20px rgba(0,0,0,.25)}}
.lid .orn{{font-size:34px;line-height:1}}
.lid .ct{{font-family:"IM Fell English SC",serif;font-size:clamp(26px,6.5vw,38px);letter-spacing:.08em;line-height:1.15;text-shadow:0 1px 0 rgba(0,0,0,.6),0 -1px 0 rgba(255,230,170,.25)}}
.lid .cb{{font-family:"IM Fell English",serif;font-style:italic;font-size:20px;opacity:.95}}
.lid .rule{{width:60%;height:5px;border-top:1px solid rgba(232,199,122,.8);border-bottom:2px solid rgba(232,199,122,.8)}}
.press{{position:absolute;left:50%;bottom:-58px;transform:translateX(-50%);white-space:nowrap;color:#e8c77a;font-family:"IM Fell English SC",serif;font-size:20px;letter-spacing:.08em;background:none;border:0;cursor:pointer;min-height:44px}}
.cover-ov.open .lid{{transform:rotateY(-165deg)}}
.cover-ov.open .press{{opacity:0}}
@media(prefers-reduced-motion:no-preference){{.press{{animation:pulse 1.6s ease-in-out infinite}}@keyframes pulse{{0%,100%{{opacity:.35}}50%{{opacity:1}}}}}}
@media(prefers-reduced-motion:reduce){{.lid{{transition:none}}}}
"""
