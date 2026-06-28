"""逐页截图自检 + 2x4 联络表拼接。

用法：python3 screenshot.py
输出：shots/page_NN.png + shots/contact_sheet.png
"""

from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = Path(__file__).parent
HTML = ROOT / "课件" / "index.html"
SHOTS = ROOT / "shots"
SHOTS.mkdir(exist_ok=True)

TOTAL_PAGES = 12


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
        page = ctx.new_page()
        page.goto(HTML.as_uri())
        page.wait_for_load_state("networkidle")
        # 等打字机第一拍
        page.wait_for_timeout(500)

        for i in range(TOTAL_PAGES):
            page.evaluate(f"show({i})")
            # 等翻页动画 + 目录滚动
            page.wait_for_timeout(700)
            png = SHOTS / f"page_{i+1:02d}.png"
            page.screenshot(path=str(png), clip={"x": 0, "y": 0, "width": 1920, "height": 1080})
            print(f"shot · {png.name}")

        browser.close()

    # 联络表 2x4 网格（13 页要 2 张：8 + 5）
    cell_w, cell_h = 480, 270
    per_sheet = 8
    cols = 4
    for sheet_idx in range(0, TOTAL_PAGES, per_sheet):
        batch = list(range(sheet_idx, min(sheet_idx + per_sheet, TOTAL_PAGES)))
        rows = (len(batch) + cols - 1) // cols
        sheet = Image.new("RGB", (cell_w * cols, cell_h * rows), "white")
        for n, idx in enumerate(batch):
            img = Image.open(SHOTS / f"page_{idx+1:02d}.png").resize((cell_w, cell_h))
            r, c = divmod(n, cols)
            sheet.paste(img, (c * cell_w, r * cell_h))
        out = SHOTS / f"contact_sheet_{sheet_idx//per_sheet + 1}.png"
        sheet.save(out)
        print(f"sheet · {out.name}")


if __name__ == "__main__":
    main()
