"""
pinterest_pins.py — SkynetLabs Carousel Batch 5
Generate tall Pinterest-optimized infographic pins.

For each carousel:
  1. Hook slide (title — grabs attention)
  2. Stat slide (big number — curiosity driver)
  3. Recap slide (bullet summary — value proof)

Stitched vertically: 1080 x 2100 (ratio ~1:1.94 — Pinterest sweet spot).
Each slide resized to 1080x700 from 1080x1350 originals.

Output: pinterest-pins/pin_01.png ... pin_30.png
"""

import sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent.parent
SCRIPTS = Path(__file__).parent
SLIDES_DIR = ROOT / "slides"
OUTPUT_DIR = ROOT / "pinterest-pins"

# Import content data
sys.path.insert(0, str(SCRIPTS))
import content as content_mod

# Pinterest pin dimensions
PIN_WIDTH = 1080
SLIDE_HEIGHT = 700  # each of 3 slides resized to this
PIN_HEIGHT = SLIDE_HEIGHT * 3  # 2100


def title_slug(title: str) -> str:
    """Must match generator.py slug() exactly."""
    return (title.lower()
            .replace(" ", "-")
            .replace("\u2014", "-")
            .replace("/", "-")
            .replace(",", "")
            .replace("'", "")
            .replace("\u2019", "")
            .replace(".", "")
            .replace("(", "")
            .replace(")", ""))[:60]


def find_slide_indices(slides: list) -> dict:
    """Find the best slides to use for Pinterest pin.
    Returns dict with 'hook', 'stat', 'recap' indices (1-based slide numbers).
    Falls back to best alternatives if stat/recap not found.
    """
    hook_idx = 1  # always slide 1

    stat_idx = None
    recap_idx = None
    best_point_idx = None
    cta_idx = None

    for i, slide in enumerate(slides):
        slide_num = i + 1
        stype = slide.get("type", "")
        if stype == "stat" and stat_idx is None:
            stat_idx = slide_num
        elif stype == "recap" and recap_idx is None:
            recap_idx = slide_num
        elif stype == "cta":
            cta_idx = slide_num
        elif stype == "point" and best_point_idx is None:
            # Pick the first point slide as fallback
            best_point_idx = slide_num

    # Fallbacks
    if stat_idx is None:
        # Use a content slide near the middle
        mid = len(slides) // 2
        stat_idx = mid + 1 if mid > 0 else 2

    if recap_idx is None:
        # Use the second-to-last slide
        recap_idx = max(len(slides) - 1, 2)

    return {
        "hook": hook_idx,
        "stat": stat_idx,
        "recap": recap_idx,
    }


def resize_and_crop_center(img: Image.Image, target_w: int, target_h: int) -> Image.Image:
    """Resize image to fill target dimensions, then center-crop.
    Preserves aspect ratio during resize, crops overflow.
    """
    src_w, src_h = img.size
    # Scale to fill (cover)
    scale = max(target_w / src_w, target_h / src_h)
    new_w = int(src_w * scale)
    new_h = int(src_h * scale)
    img = img.resize((new_w, new_h), Image.LANCZOS)

    # Center crop
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    return img.crop((left, top, left + target_w, top + target_h))


def generate_pin(carousel: dict) -> Path:
    """Generate a tall Pinterest pin for one carousel."""
    cid = carousel["id"]
    title = carousel["title"]
    slides = carousel["slides"]
    folder = f"{cid:02d}_{title_slug(title)}"
    folder_path = SLIDES_DIR / folder

    if not folder_path.exists():
        print(f"  SKIP: folder not found: {folder}")
        return None

    indices = find_slide_indices(slides)

    # Load the 3 slides
    slide_images = []
    for key in ["hook", "stat", "recap"]:
        idx = indices[key]
        slide_path = folder_path / f"slide_{idx:02d}.png"
        if not slide_path.exists():
            print(f"  WARN: slide {idx} not found for {title}, using slide_01")
            slide_path = folder_path / "slide_01.png"
        img = Image.open(slide_path).convert("RGB")
        slide_images.append(img)

    # Resize each slide to 1080x700 (center-crop)
    resized = [resize_and_crop_center(img, PIN_WIDTH, SLIDE_HEIGHT) for img in slide_images]

    # Create the tall pin canvas
    pin = Image.new("RGB", (PIN_WIDTH, PIN_HEIGHT))

    # Paste slides vertically
    y_offset = 0
    for img in resized:
        pin.paste(img, (0, y_offset))
        y_offset += SLIDE_HEIGHT

    # Save
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / f"pin_{cid:02d}.png"
    pin.save(out_path, "PNG", optimize=True)
    return out_path


def main():
    carousels = content_mod.CAROUSELS
    print(f"Generating {len(carousels)} Pinterest pins...")
    print(f"Output: {OUTPUT_DIR}")
    print(f"Pin size: {PIN_WIDTH}x{PIN_HEIGHT} (ratio 1:{PIN_HEIGHT/PIN_WIDTH:.1f})")
    print()

    success = 0
    for carousel in carousels:
        cid = carousel["id"]
        title = carousel["title"]
        indices = find_slide_indices(carousel["slides"])
        print(f"  [{cid:02d}] {title}")
        print(f"       slides: hook={indices['hook']}, stat={indices['stat']}, recap={indices['recap']}")

        result = generate_pin(carousel)
        if result:
            print(f"       -> {result.name}")
            success += 1

    print(f"\nDone: {success}/{len(carousels)} pins generated.")
    print(f"Total size: {sum(f.stat().st_size for f in OUTPUT_DIR.glob('*.png')) / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    main()
