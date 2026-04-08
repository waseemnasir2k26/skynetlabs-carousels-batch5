"""
SkynetLabs Carousel Batch 5 — PDF Generator
Produces 30 carousel PDFs + individual PNG slides across 6 design families.
"""
import os
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

from content import CAROUSELS

# ================================================================
# CONSTANTS
# ================================================================
W, H = 1080, 1350  # 4:5 aspect — optimal for LinkedIn/IG/FB carousels
MARGIN_X = 80
MARGIN_TOP = 130
BRAND_BAR_H = 96
CONTENT_BOTTOM = H - BRAND_BAR_H - 30

OUT_DIR = Path(__file__).parent.parent
SLIDES_DIR = OUT_DIR / "slides"
PDFS_DIR = OUT_DIR / "pdfs"
OUTPUT_DIR = OUT_DIR / "output"
for d in (SLIDES_DIR, PDFS_DIR, OUTPUT_DIR):
    d.mkdir(parents=True, exist_ok=True)

FONT_DIR = Path("C:/Windows/Fonts")

# ================================================================
# FONT LOADER
# ================================================================
def font(name, size):
    mapping = {
        "arial": "arial.ttf",
        "arial_b": "arialbd.ttf",
        "consol": "consola.ttf",
        "consol_b": "consolab.ttf",
        "segoe": "segoeui.ttf",
        "segoe_b": "segoeuib.ttf",
        "georgia": "georgia.ttf",
        "georgia_b": "georgiab.ttf",
        "georgia_i": "georgiai.ttf",
        "courier": "cour.ttf",
        "courier_b": "courbd.ttf",
    }
    return ImageFont.truetype(str(FONT_DIR / mapping[name]), size)


# ================================================================
# TEXT UTILITIES
# ================================================================
def text_size(draw, text, fnt):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def wrap_text(draw, text, fnt, max_width):
    """Word-wrap text to fit within max_width pixels."""
    lines = []
    for paragraph in text.split("\n"):
        if not paragraph.strip():
            lines.append("")
            continue
        words = paragraph.split(" ")
        current = ""
        for word in words:
            test = (current + " " + word).strip()
            w, _ = text_size(draw, test, fnt)
            if w <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines


def draw_wrapped(draw, text, fnt, xy, max_width, fill, line_spacing=10, align="left"):
    x, y = xy
    lines = wrap_text(draw, text, fnt, max_width)
    for line in lines:
        if align == "center":
            lw, _ = text_size(draw, line, fnt)
            draw.text((x + (max_width - lw) // 2, y), line, font=fnt, fill=fill)
        elif align == "right":
            lw, _ = text_size(draw, line, fnt)
            draw.text((x + max_width - lw, y), line, font=fnt, fill=fill)
        else:
            draw.text((x, y), line, font=fnt, fill=fill)
        _, lh = text_size(draw, line or "Ag", fnt)
        y += lh + line_spacing
    return y


def draw_centered(draw, text, fnt, y, fill, x_center=W // 2):
    w, _ = text_size(draw, text, fnt)
    draw.text((x_center - w // 2, y), text, font=fnt, fill=fill)
    _, h = text_size(draw, text, fnt)
    return y + h


def rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def blurred_circle(img, center, radius, color, opacity=0.6):
    """Soft glow circle using Gaussian blur."""
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    cx, cy = center
    ld.ellipse((cx - radius, cy - radius, cx + radius, cy + radius),
               fill=(*color, int(255 * opacity)))
    layer = layer.filter(ImageFilter.GaussianBlur(radius // 2))
    img.alpha_composite(layer)


# ================================================================
# BASE RENDERER
# ================================================================
class BaseRenderer:
    # Default palette (overridden by subclasses)
    BG = (10, 10, 18)
    FG = (255, 255, 255)
    MUTED = (150, 155, 175)
    PRIMARY = (0, 132, 255)
    SECONDARY = (0, 224, 208)
    ACCENT = (255, 56, 100)
    DIM_BG = (18, 18, 30)

    HEADER_FONT = "arial_b"
    BODY_FONT = "arial"
    BODY_BOLD_FONT = "arial_b"
    KICKER_FONT = "arial_b"
    NUMBER_FONT = "arial_b"

    FAMILY_NAME = "BASE"

    def make_background(self):
        return Image.new("RGBA", (W, H), (*self.BG, 255))

    def decorate(self, img, slide_index, total):
        """Family-specific background decoration. Override per family."""
        pass

    def draw_brand_bar(self, img, slide_index, total):
        d = ImageDraw.Draw(img)
        # Subtle separator line
        d.line([(MARGIN_X, H - BRAND_BAR_H), (W - MARGIN_X, H - BRAND_BAR_H)],
               fill=(*self.PRIMARY, 180), width=2)

        # Brand text left
        bf = font(self.KICKER_FONT, 26)
        d.text((MARGIN_X, H - BRAND_BAR_H + 20), "SKYNET LABS", font=bf, fill=self.FG)
        muted_f = font(self.BODY_FONT, 22)
        d.text((MARGIN_X, H - BRAND_BAR_H + 52), "skynetjoe.com  ·  @skynetjoe",
               font=muted_f, fill=self.MUTED)

        # Slide counter right
        counter = f"{slide_index + 1:02d} / {total:02d}"
        cf = font(self.KICKER_FONT, 32)
        cw, _ = text_size(d, counter, cf)
        d.text((W - MARGIN_X - cw, H - BRAND_BAR_H + 30), counter,
               font=cf, fill=self.PRIMARY)

    def draw_kicker(self, img, text):
        """Top-of-slide kicker tag (family style)."""
        if not text:
            return
        d = ImageDraw.Draw(img)
        kf = font(self.KICKER_FONT, 24)
        tw, th = text_size(d, text, kf)
        pad_x = 18
        pad_y = 10
        x = MARGIN_X
        y = 70
        # Solid-fill pill for maximum legibility across all backgrounds
        rounded_rect(d, (x, y, x + tw + pad_x * 2, y + th + pad_y * 2),
                     radius=8, fill=self.PRIMARY)
        d.text((x + pad_x, y + pad_y), text, font=kf, fill=self.BG)

    # ----- slide type renderers (shared layout) -----

    def render_hook(self, slide):
        img = self.make_background()
        self.decorate(img, 0, 10)
        self.draw_kicker(img, slide.get("kicker"))
        d = ImageDraw.Draw(img)
        # Massive title
        title_font = font(self.HEADER_FONT, 110)
        sub_font = font(self.BODY_FONT, 38)
        # center vertically-ish
        title_lines = wrap_text(d, slide["title"], title_font, W - MARGIN_X * 2)
        sub_lines = wrap_text(d, slide.get("sub", ""), sub_font, W - MARGIN_X * 2)
        _, tlh = text_size(d, "Ag", title_font)
        _, slh = text_size(d, "Ag", sub_font)
        total_h = len(title_lines) * (tlh + 12) + 30 + len(sub_lines) * (slh + 8)
        y = (H - total_h) // 2 - 40
        for line in title_lines:
            lw, _ = text_size(d, line, title_font)
            d.text(((W - lw) // 2, y), line, font=title_font, fill=self.FG)
            y += tlh + 12
        y += 30
        for line in sub_lines:
            lw, _ = text_size(d, line, sub_font)
            d.text(((W - lw) // 2, y), line, font=sub_font, fill=self.PRIMARY)
            y += slh + 8
        # Swipe arrow
        self.draw_swipe_hint(img)
        return img

    def draw_swipe_hint(self, img):
        d = ImageDraw.Draw(img)
        hf = font(self.KICKER_FONT, 28)
        text = "SWIPE →"
        tw, _ = text_size(d, text, hf)
        d.text((W - MARGIN_X - tw, H - BRAND_BAR_H - 60), text,
               font=hf, fill=self.SECONDARY)

    def render_problem(self, slide):
        img = self.make_background()
        self.decorate(img, 1, 10)
        self.draw_kicker(img, slide.get("kicker"))
        d = ImageDraw.Draw(img)
        title_font = font(self.HEADER_FONT, 76)
        body_font = font(self.BODY_FONT, 38)

        title_lines = wrap_text(d, slide["title"], title_font, W - MARGIN_X * 2)
        body_lines = wrap_text(d, slide.get("body", ""), body_font, W - MARGIN_X * 2)
        _, tlh = text_size(d, "Ag", title_font)
        _, blh = text_size(d, "Ag", body_font)

        title_h = len(title_lines) * (tlh + 14)
        body_h = len(body_lines) * (blh + 14)
        total_h = title_h + 50 + body_h

        y_start = max(200, (H - BRAND_BAR_H - total_h) // 2 - 40)
        y = y_start

        # Title
        for line in title_lines:
            d.text((MARGIN_X, y), line, font=title_font, fill=self.FG)
            y += tlh + 14

        # Accent line between title and body
        y += 20
        d.line([(MARGIN_X, y), (MARGIN_X + 120, y)],
               fill=self.PRIMARY, width=5)
        y += 30

        for line in body_lines:
            d.text((MARGIN_X, y), line, font=body_font, fill=self.MUTED)
            y += blh + 14

        return img

    def render_point(self, slide):
        img = self.make_background()
        self.decorate(img, 3, 10)
        self.draw_kicker(img, slide.get("tag", "").upper() if slide.get("tag") else None)
        d = ImageDraw.Draw(img)

        num = slide.get("num", "01")
        title = slide.get("title", "")
        body = slide.get("body", "")

        title_font = font(self.HEADER_FONT, 76)
        body_font = font(self.BODY_FONT, 36)
        num_font = font(self.NUMBER_FONT, 200)

        # Pre-measure content to center vertically
        title_lines = wrap_text(d, title, title_font, W - MARGIN_X * 2)
        body_lines = wrap_text(d, body, body_font, W - MARGIN_X * 2)
        _, tlh = text_size(d, "Ag", title_font)
        _, blh = text_size(d, "Ag", body_font)
        _, nh = text_size(d, num, num_font)

        title_block_h = len(title_lines) * (tlh + 10)
        body_block_h = len(body_lines) * (blh + 12)
        total_h = nh + 40 + 55 + title_block_h + 25 + body_block_h

        # Center vertically (leaving room for kicker at top and brand bar at bottom)
        available_top = 180
        available_bottom = H - BRAND_BAR_H - 60
        y_start = max(available_top, (available_top + available_bottom - total_h) // 2)

        # Huge number (left-aligned)
        y = y_start
        d.text((MARGIN_X - 20, y), num, font=num_font, fill=self.PRIMARY)

        # Accent line under number (separator) — more breathing room
        line_y = y + nh + 40
        d.line([(MARGIN_X, line_y), (MARGIN_X + 180, line_y)],
               fill=self.SECONDARY, width=5)

        # Title below separator
        ty = line_y + 55
        for line in title_lines:
            d.text((MARGIN_X, ty), line, font=title_font, fill=self.FG)
            ty += tlh + 10

        # Body below title
        ty += 25
        for line in body_lines:
            d.text((MARGIN_X, ty), line, font=body_font, fill=self.MUTED)
            ty += blh + 12

        return img

    def render_stat(self, slide):
        img = self.make_background()
        self.decorate(img, 4, 10)
        d = ImageDraw.Draw(img)
        big = slide.get("big", "00")
        label = slide.get("label", "")
        big_font = font(self.NUMBER_FONT, 320)
        label_font = font(self.BODY_FONT, 40)
        bw, bh = text_size(d, big, big_font)
        # center the big number
        cy = H // 2 - 180
        d.text(((W - bw) // 2, cy), big, font=big_font, fill=self.ACCENT)
        # label below
        ly = cy + bh + 50
        label_lines = wrap_text(d, label, label_font, W - MARGIN_X * 2)
        for line in label_lines:
            lw, lh_ = text_size(d, line, label_font)
            d.text(((W - lw) // 2, ly), line, font=label_font, fill=self.FG)
            ly += lh_ + 14
        return img

    def render_quote(self, slide):
        img = self.make_background()
        self.decorate(img, 5, 10)
        d = ImageDraw.Draw(img)
        quote_font = font("georgia_i", 58)
        attr_font = font(self.BODY_FONT, 30)
        # Big opening quote mark
        qf = font("georgia_b", 240)
        d.text((MARGIN_X - 20, 160), '"', font=qf, fill=(*self.PRIMARY, 120))
        text = slide.get("text", "")
        lines = wrap_text(d, text, quote_font, W - MARGIN_X * 2 - 60)
        y = 380
        _, lh = text_size(d, "Ag", quote_font)
        for line in lines:
            d.text((MARGIN_X + 30, y), line, font=quote_font, fill=self.FG)
            y += lh + 14
        y += 40
        attr = slide.get("attr", "")
        d.text((MARGIN_X + 30, y), attr, font=attr_font, fill=self.SECONDARY)
        return img

    def render_recap(self, slide):
        img = self.make_background()
        self.decorate(img, 8, 10)
        self.draw_kicker(img, "RECAP")
        d = ImageDraw.Draw(img)
        title_font = font(self.HEADER_FONT, 78)
        point_font = font(self.BODY_BOLD_FONT, 34)
        title = slide.get("title", "RECAP")
        points = slide.get("points", [])

        # Pre-measure to center vertically
        title_lines = wrap_text(d, title, title_font, W - MARGIN_X * 2)
        _, tlh = text_size(d, "Ag", title_font)
        _, plh = text_size(d, "Ag", point_font)
        title_h = len(title_lines) * (tlh + 10)

        # Estimate total points height
        points_h = 0
        point_line_data = []
        for p in points:
            lines = wrap_text(d, p, point_font, W - MARGIN_X * 2 - 40)
            h = len(lines) * (plh + 6) + 20
            points_h += h
            point_line_data.append(lines)

        # Accent line separator
        total_h = title_h + 50 + points_h
        y_start = max(180, (H - BRAND_BAR_H - total_h) // 2 - 30)
        y = y_start
        for line in title_lines:
            d.text((MARGIN_X, y), line, font=title_font, fill=self.FG)
            y += tlh + 10
        # Gold/primary separator
        y += 15
        d.line([(MARGIN_X, y), (MARGIN_X + 150, y)], fill=self.PRIMARY, width=5)
        y += 40
        # Render points
        for lines in point_line_data:
            # Bullet marker
            d.ellipse((MARGIN_X, y + 14, MARGIN_X + 16, y + 30),
                      fill=self.PRIMARY)
            py = y
            for line in lines:
                d.text((MARGIN_X + 38, py), line, font=point_font, fill=self.FG)
                py += plh + 6
            y = py + 20
        return img

    def render_cta(self, slide):
        img = self.make_background()
        self.decorate(img, 9, 10)
        self.draw_kicker(img, slide.get("kicker"))
        d = ImageDraw.Draw(img)
        title_font = font(self.HEADER_FONT, 88)
        body_font = font(self.BODY_FONT, 36)
        title = slide.get("title", "")
        body = slide.get("body", "")
        # center vertically
        title_lines = wrap_text(d, title, title_font, W - MARGIN_X * 2)
        body_lines = wrap_text(d, body, body_font, W - MARGIN_X * 2)
        _, tlh = text_size(d, "Ag", title_font)
        _, blh = text_size(d, "Ag", body_font)
        total_h = len(title_lines) * (tlh + 12) + 50 + len(body_lines) * (blh + 10)
        y = (H - total_h) // 2 - 60
        for line in title_lines:
            lw, _ = text_size(d, line, title_font)
            d.text(((W - lw) // 2, y), line, font=title_font, fill=self.FG)
            y += tlh + 12
        y += 50
        for line in body_lines:
            lw, _ = text_size(d, line, body_font)
            d.text(((W - lw) // 2, y), line, font=body_font, fill=self.MUTED)
            y += blh + 10
        # Big CTA pill
        pill_text = "SAVE  ·  SHARE  ·  FOLLOW"
        pf = font(self.BODY_BOLD_FONT, 32)
        pw, ph = text_size(d, pill_text, pf)
        px, py = (W - pw - 80) // 2, y + 40
        rounded_rect(d, (px, py, px + pw + 80, py + ph + 36),
                     radius=40, fill=self.PRIMARY)
        d.text((px + 40, py + 18), pill_text, font=pf, fill=self.BG)
        return img

    def render_slide(self, slide, index, total):
        t = slide.get("type", "point")
        if t == "hook":
            img = self.render_hook(slide)
        elif t == "problem":
            img = self.render_problem(slide)
        elif t == "point":
            img = self.render_point(slide)
        elif t == "stat":
            img = self.render_stat(slide)
        elif t == "quote":
            img = self.render_quote(slide)
        elif t == "recap":
            img = self.render_recap(slide)
        elif t == "cta":
            img = self.render_cta(slide)
        else:
            img = self.render_point(slide)
        self.draw_brand_bar(img, index, total)
        return img.convert("RGB")


# ================================================================
# FAMILY 1 — NEON TERMINAL (Category A: AI Tools)
# ================================================================
class NeonTerminal(BaseRenderer):
    FAMILY_NAME = "NEON TERMINAL"
    BG = (0, 0, 0)
    FG = (230, 255, 230)
    MUTED = (100, 180, 120)
    PRIMARY = (0, 255, 65)
    SECONDARY = (255, 176, 0)
    ACCENT = (255, 80, 80)
    DIM_BG = (8, 15, 8)

    HEADER_FONT = "consol_b"
    BODY_FONT = "consol"
    BODY_BOLD_FONT = "consol_b"
    KICKER_FONT = "consol_b"
    NUMBER_FONT = "consol_b"

    def decorate(self, img, slide_index, total):
        d = ImageDraw.Draw(img)
        # Scan lines (every 4 px, very faint)
        for y in range(0, H, 4):
            d.line([(0, y), (W, y)], fill=(0, 40, 0, 40), width=1)
        # Top/bottom green phosphor glow
        blurred_circle(img, (W // 2, -100), 450, (0, 255, 65), 0.12)
        blurred_circle(img, (W // 2, H + 100), 500, (0, 255, 65), 0.08)
        # Corner brackets
        bl = 40
        bw = 5
        col = (0, 255, 65)
        # top-left
        d.line([(20, 20), (20 + bl, 20)], fill=col, width=bw)
        d.line([(20, 20), (20, 20 + bl)], fill=col, width=bw)
        # top-right
        d.line([(W - 20 - bl, 20), (W - 20, 20)], fill=col, width=bw)
        d.line([(W - 20, 20), (W - 20, 20 + bl)], fill=col, width=bw)


# ================================================================
# FAMILY 2 — CIRCUIT BOARD (Category B: Automation)
# ================================================================
class CircuitBoard(BaseRenderer):
    FAMILY_NAME = "CIRCUIT BOARD"
    BG = (6, 10, 25)
    FG = (235, 245, 255)
    MUTED = (130, 160, 200)
    PRIMARY = (0, 132, 255)
    SECONDARY = (0, 224, 208)
    ACCENT = (138, 43, 226)
    DIM_BG = (12, 20, 40)

    HEADER_FONT = "segoe_b"
    BODY_FONT = "segoe"
    BODY_BOLD_FONT = "segoe_b"
    KICKER_FONT = "consol_b"
    NUMBER_FONT = "segoe_b"

    def decorate(self, img, slide_index, total):
        d = ImageDraw.Draw(img)
        # Gradient overlay (top dark → slightly lighter)
        for y in range(H):
            v = int(25 * (y / H))
            d.line([(0, y), (W, y)], fill=(6 + v // 3, 10 + v // 2, 25 + v, 255))
        # Circuit trace pattern (random-ish)
        import random
        random.seed(slide_index * 7 + 13)
        for _ in range(12):
            x1 = random.randint(0, W)
            y1 = random.randint(0, H)
            length = random.randint(100, 300)
            horiz = random.random() > 0.5
            if horiz:
                d.line([(x1, y1), (x1 + length, y1)], fill=(0, 132, 255, 40), width=2)
                d.ellipse((x1 + length - 6, y1 - 6, x1 + length + 6, y1 + 6),
                          outline=(0, 224, 208, 120), width=2)
            else:
                d.line([(x1, y1), (x1, y1 + length)], fill=(0, 132, 255, 40), width=2)
                d.ellipse((x1 - 6, y1 + length - 6, x1 + 6, y1 + length + 6),
                          outline=(0, 224, 208, 120), width=2)
        # Soft glow
        blurred_circle(img, (200, 200), 500, (0, 132, 255), 0.10)
        blurred_circle(img, (W - 200, H - 300), 400, (0, 224, 208), 0.08)


# ================================================================
# FAMILY 3 — EXECUTIVE NAVY (Category C: Frameworks)
# ================================================================
class ExecutiveNavy(BaseRenderer):
    FAMILY_NAME = "EXECUTIVE NAVY"
    BG = (10, 20, 45)
    FG = (245, 240, 225)
    MUTED = (180, 180, 180)
    PRIMARY = (212, 175, 55)
    SECONDARY = (240, 220, 150)
    ACCENT = (200, 100, 50)
    DIM_BG = (15, 28, 55)

    HEADER_FONT = "georgia_b"
    BODY_FONT = "segoe"
    BODY_BOLD_FONT = "segoe_b"
    KICKER_FONT = "segoe_b"
    NUMBER_FONT = "georgia_b"

    def decorate(self, img, slide_index, total):
        d = ImageDraw.Draw(img)
        # Subtle navy gradient
        for y in range(H):
            v = int(15 * math.sin(y / H * math.pi))
            d.line([(0, y), (W, y)], fill=(10 + v // 2, 20 + v, 45 + v, 255))
        # Gold hairline top and bottom of content
        d.line([(MARGIN_X, 110), (W - MARGIN_X, 110)],
               fill=(*self.PRIMARY, 200), width=2)
        d.line([(MARGIN_X, H - BRAND_BAR_H - 20), (W - MARGIN_X, H - BRAND_BAR_H - 20)],
               fill=(*self.PRIMARY, 200), width=2)
        # Gold corner ornaments
        corner_size = 30
        pad = 50
        col = self.PRIMARY
        # Top-left
        d.line([(pad, pad), (pad + corner_size, pad)], fill=col, width=3)
        d.line([(pad, pad), (pad, pad + corner_size)], fill=col, width=3)
        # Top-right
        d.line([(W - pad - corner_size, pad), (W - pad, pad)], fill=col, width=3)
        d.line([(W - pad, pad), (W - pad, pad + corner_size)], fill=col, width=3)
        # Subtle gold glow
        blurred_circle(img, (W // 2, H // 2), 550, (212, 175, 55), 0.05)


# ================================================================
# FAMILY 4 — DATA LAB (Category D: Research)
# ================================================================
class DataLab(BaseRenderer):
    FAMILY_NAME = "DATA LAB"
    BG = (18, 10, 35)
    FG = (245, 240, 255)
    MUTED = (160, 150, 200)
    PRIMARY = (255, 56, 100)
    SECONDARY = (0, 230, 118)
    ACCENT = (255, 176, 0)
    DIM_BG = (25, 15, 50)

    HEADER_FONT = "arial_b"
    BODY_FONT = "arial"
    BODY_BOLD_FONT = "arial_b"
    KICKER_FONT = "consol_b"
    NUMBER_FONT = "arial_b"

    def decorate(self, img, slide_index, total):
        d = ImageDraw.Draw(img)
        # Deep purple gradient
        for y in range(H):
            factor = y / H
            r = int(18 + (5 * factor))
            g = int(10 - (5 * factor))
            b = int(35 + (10 * factor))
            d.line([(0, y), (W, y)], fill=(max(0, r), max(0, g), min(60, b), 255))
        # Grid lines
        for x in range(0, W, 90):
            d.line([(x, 0), (x, H)], fill=(60, 40, 90, 40), width=1)
        for y in range(0, H, 90):
            d.line([(0, y), (W, y)], fill=(60, 40, 90, 40), width=1)
        # Glow orbs
        blurred_circle(img, (150, H - 250), 400, (255, 56, 100), 0.10)
        blurred_circle(img, (W - 150, 250), 400, (0, 230, 118), 0.08)
        # Mini "chart" in corner
        bar_x = W - 180
        bar_y = 80
        for i in range(5):
            h_bar = 10 + i * 8
            d.rectangle((bar_x + i * 18, bar_y + 40 - h_bar,
                         bar_x + i * 18 + 12, bar_y + 40),
                        fill=(*self.PRIMARY, 180))


# ================================================================
# FAMILY 5 — CASE FILE (Category E: Case Studies)
# ================================================================
class CaseFile(BaseRenderer):
    FAMILY_NAME = "CASE FILE"
    BG = (232, 215, 175)  # kraft paper
    FG = (25, 20, 15)
    MUTED = (90, 75, 60)
    PRIMARY = (180, 35, 30)  # stamp red
    SECONDARY = (50, 60, 95)  # ink blue
    ACCENT = (150, 100, 30)
    DIM_BG = (220, 200, 160)

    HEADER_FONT = "courier_b"
    BODY_FONT = "georgia"
    BODY_BOLD_FONT = "georgia_b"
    KICKER_FONT = "courier_b"
    NUMBER_FONT = "courier_b"

    def decorate(self, img, slide_index, total):
        d = ImageDraw.Draw(img)
        import random
        random.seed(slide_index * 11 + 5)
        # Paper noise
        for _ in range(2500):
            x = random.randint(0, W - 1)
            y = random.randint(0, H - 1)
            shade = random.randint(-15, 15)
            r = max(0, min(255, 232 + shade))
            g = max(0, min(255, 215 + shade))
            b = max(0, min(255, 175 + shade))
            d.point((x, y), fill=(r, g, b))
        # Edge darkening (vignette effect)
        for i in range(40):
            opacity = int(30 * (1 - i / 40))
            d.rectangle((i, i, W - i, H - i),
                        outline=(180, 160, 120, opacity), width=1)
        # "CLASSIFIED" diagonal stamp top-right
        stamp_font = font("courier_b", 42)
        stamp_text = f"CASE #{slide_index + 1:03d}"
        stamp_img = Image.new("RGBA", (300, 80), (0, 0, 0, 0))
        sd = ImageDraw.Draw(stamp_img)
        sd.rectangle((4, 4, 296, 76), outline=(180, 35, 30, 230), width=4)
        sd.text((30, 18), stamp_text, font=stamp_font, fill=(180, 35, 30, 230))
        rotated = stamp_img.rotate(-12, expand=True, resample=Image.BICUBIC)
        img.alpha_composite(rotated, (W - 320, 30))

    def draw_brand_bar(self, img, slide_index, total):
        # Override: darker brand bar on kraft bg
        d = ImageDraw.Draw(img)
        d.line([(MARGIN_X, H - BRAND_BAR_H), (W - MARGIN_X, H - BRAND_BAR_H)],
               fill=(*self.PRIMARY, 200), width=3)
        bf = font(self.KICKER_FONT, 26)
        d.text((MARGIN_X, H - BRAND_BAR_H + 20), "SKYNET LABS", font=bf, fill=self.FG)
        muted_f = font("georgia", 22)
        d.text((MARGIN_X, H - BRAND_BAR_H + 52), "skynetjoe.com  ·  @skynetjoe",
               font=muted_f, fill=self.MUTED)
        counter = f"{slide_index + 1:02d} / {total:02d}"
        cf = font(self.KICKER_FONT, 32)
        cw, _ = text_size(d, counter, cf)
        d.text((W - MARGIN_X - cw, H - BRAND_BAR_H + 30), counter,
               font=cf, fill=self.PRIMARY)


# ================================================================
# FAMILY 6 — MINDSCAPE (Category F: Mental Models)
# ================================================================
class Mindscape(BaseRenderer):
    FAMILY_NAME = "MINDSCAPE"
    BG = (40, 20, 60)
    FG = (255, 248, 230)
    MUTED = (245, 225, 200)
    PRIMARY = (255, 210, 100)
    SECONDARY = (255, 255, 220)
    ACCENT = (255, 120, 150)
    DIM_BG = (60, 30, 80)

    HEADER_FONT = "georgia_b"
    BODY_FONT = "segoe"
    BODY_BOLD_FONT = "segoe_b"
    KICKER_FONT = "segoe_b"
    NUMBER_FONT = "georgia_b"

    def decorate(self, img, slide_index, total):
        d = ImageDraw.Draw(img)
        # Deep sunset gradient — top-warm, bottom-deep-purple
        for y in range(H):
            factor = y / H
            r = int(200 - factor * 170)  # 200 → 30
            g = int(90 - factor * 70)    # 90 → 20
            b = int(80 + factor * 70)    # 80 → 150
            d.line([(0, y), (W, y)], fill=(max(0, r), max(0, g), min(160, b), 255))
        # Warm top glow — smaller, positioned further off-screen to avoid banding
        blurred_circle(img, (W // 2, -200), 550, (255, 160, 60), 0.45)
        # Cool bottom glow
        blurred_circle(img, (W // 2, H + 200), 600, (80, 20, 120), 0.45)
        # Corner accent circles (OUTSIDE content area only)
        blurred_circle(img, (-100, H - 100), 300, (255, 100, 130), 0.30)
        blurred_circle(img, (W + 100, H - 300), 300, (160, 60, 200), 0.28)


# ================================================================
# FAMILY MAP
# ================================================================
FAMILY_MAP = {
    "A": NeonTerminal,
    "B": CircuitBoard,
    "C": ExecutiveNavy,
    "D": DataLab,
    "E": CaseFile,
    "F": Mindscape,
}


# ================================================================
# MAIN GENERATION
# ================================================================
def slug(text):
    return (text.lower()
            .replace(" ", "-")
            .replace("—", "-")
            .replace("/", "-")
            .replace(",", "")
            .replace("'", "")
            .replace(".", "")
            .replace("(", "")
            .replace(")", ""))[:60]


def generate_all():
    total = len(CAROUSELS)
    for c in CAROUSELS:
        cid = c["id"]
        cat = c["category"]
        title_slug = slug(c["title"])
        renderer_cls = FAMILY_MAP[cat]
        renderer = renderer_cls()
        slides = c["slides"]
        rendered = []
        slide_dir = SLIDES_DIR / f"{cid:02d}_{title_slug}"
        slide_dir.mkdir(parents=True, exist_ok=True)
        print(f"[{cid:02d}/{total}] {renderer.FAMILY_NAME} — {c['title']}")
        for idx, slide in enumerate(slides):
            img = renderer.render_slide(slide, idx, len(slides))
            png_path = slide_dir / f"slide_{idx + 1:02d}.png"
            img.save(png_path, "PNG", optimize=True)
            rendered.append(img)
        # Save combined PDF
        pdf_path = PDFS_DIR / f"{cid:02d}_{title_slug}.pdf"
        rendered[0].save(pdf_path, "PDF", save_all=True,
                         append_images=rendered[1:],
                         resolution=150)
    print(f"\nDone. {total} carousels generated.")
    print(f"  Slides -> {SLIDES_DIR}")
    print(f"  PDFs   -> {PDFS_DIR}")


if __name__ == "__main__":
    generate_all()
