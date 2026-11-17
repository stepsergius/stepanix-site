#!/usr/bin/env python3
"""Draws the link preview pictures (1200 × 630) into assets/og-uk.jpg and og-en.jpg from scripts/og.html.

    python3 scripts/og.py        (needs Playwright with Chromium and Pillow)
"""
import io
import pathlib

from PIL import Image
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
    for lang in ("uk", "en"):
        page.goto((HERE / "og.html").as_uri() + f"?lang={lang}")
        page.wait_for_load_state("networkidle")
        page.evaluate("document.fonts.ready")
        page.evaluate("Promise.all([...document.images].map(i => i.decode().catch(() => 0)))")
        shot = Image.open(io.BytesIO(page.screenshot(type="png"))).convert("RGB").resize((1200, 630), Image.LANCZOS)
        shot.save(HERE.parent / "assets" / f"og-{lang}.jpg", quality=88, optimize=True)
        print(f"assets/og-{lang}.jpg")
    browser.close()
