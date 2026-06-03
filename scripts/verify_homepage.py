import sys
from pathlib import Path

from playwright.sync_api import expect, sync_playwright


ROOT = Path(__file__).resolve().parents[1]
SCREENSHOT_DIR = ROOT / "test-results"


def verify_page(url: str) -> None:
    SCREENSHOT_DIR.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1200})
        errors: list[str] = []
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
        page.goto(url, wait_until="networkidle")

        for text in [
            "基于AI与智能硬件的",
            "服务载体",
            "智能腕表",
            "数字疗法内容",
            "三端协同数字化平台",
            "关于智医康",
        ]:
            expect(page.get_by_text(text).first).to_be_visible()

        loaded_images = page.evaluate(
            """() => Array.from(document.images).map((img) => ({
                src: img.getAttribute('src'),
                complete: img.complete,
                width: img.naturalWidth,
                height: img.naturalHeight
            }))"""
        )
        broken_images = [
            img for img in loaded_images if not img["complete"] or img["width"] == 0 or img["height"] == 0
        ]
        if broken_images:
            raise AssertionError(f"Broken images: {broken_images}")

        if errors:
            raise AssertionError(f"Console errors: {errors}")

        page.screenshot(path=str(SCREENSHOT_DIR / "homepage-desktop.png"), full_page=True)

        mobile = browser.new_page(viewport={"width": 390, "height": 900}, is_mobile=True)
        mobile.goto(url, wait_until="networkidle")
        expect(mobile.get_by_text("基于AI与智能硬件的").first).to_be_visible()
        mobile.get_by_role("button", name="打开导航菜单").click()
        expect(mobile.get_by_role("link", name="服务载体")).to_be_visible()
        mobile.screenshot(path=str(SCREENSHOT_DIR / "homepage-mobile.png"), full_page=True)

        browser.close()


if __name__ == "__main__":
    verify_page(sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:3000")
