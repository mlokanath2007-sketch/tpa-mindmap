"""Smoke test: opens dist/index.html at laptop and phone size, clicks through,
saves screenshots to tools/shots/ and prints any JavaScript errors.

    pip install playwright && python -m playwright install chromium
    python tools/screenshot_test.py
"""
import asyncio, os, pathlib
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = (ROOT / "dist" / "index.html").as_uri()
OUT = ROOT / "tools" / "shots"
OUT.mkdir(parents=True, exist_ok=True)


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        errs = []
        for w, h, tag, cs in [(1280, 900, "d", "dark"), (390, 844, "p", "light")]:
            ctx = await b.new_context(viewport={"width": w, "height": h}, color_scheme=cs)
            pg = await ctx.new_page()
            pg.on("pageerror", lambda e: errs.append(str(e)))
            # Simulate the sandboxed artifact viewer, where replaceState throws
            await pg.add_init_script("history.replaceState=function(){throw new DOMException('x','SecurityError')}")
            await pg.goto(PAGE); await pg.wait_for_timeout(600)
            await pg.screenshot(path=str(OUT / f"{tag}_1cover.png"))
            await pg.click("#press"); await pg.wait_for_timeout(2300)
            await pg.screenshot(path=str(OUT / f"{tag}_2home.png"))
            await pg.evaluate("document.getElementById('stage').scrollIntoView()"); await pg.wait_for_timeout(500)
            await pg.screenshot(path=str(OUT / f"{tag}_3map.png"))
            await pg.click("#vDet"); await pg.wait_for_timeout(300)
            await pg.evaluate("document.getElementById('map').scrollIntoView()"); await pg.wait_for_timeout(300)
            await pg.screenshot(path=str(OUT / f"{tag}_4detailed.png"))
            await pg.click('.chip[data-s="13"]'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=str(OUT / f"{tag}_5section.png"))
            await ctx.close()
        print("errors:", errs or "none")
        await b.close()

asyncio.run(main())
