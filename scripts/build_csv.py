"""
build_csv.py — SkynetLabs Carousel Batch 5

Reads content.py (30 carousels, each with 10-12 slides) and captions.py
(captions, hashtags, interactive first comments) and emits:

  1. output/ghl-batch5-carousels.csv
       Advanced 39-column GHL bulk-upload CSV with:
       - LinkedIn postAsPdf=TRUE (all slides stitched into PDF document post)
       - Facebook + Instagram type=post (native swipe carousel)
       - Pinterest title + link (each slide becomes a pin)
       - followUpComment = interactive first comment from captions.py
       - Schedule: 30 weekdays starting Fri 2026-04-10

  2. output/captions.json
       Structured JSON with all 30 carousels' captions, hashtags,
       first comments, and slide counts. For review + manual backup.

Images are served from the public GitHub repo:
    REPO_RAW_URL/slides/<folder>/slide_01.png, slide_02.png, ...

Edit REPO_RAW_URL if you fork.
"""

import csv
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).parent.parent
SCRIPTS = Path(__file__).parent
SLIDES_DIR = ROOT / "slides"
OUTPUT_DIR = ROOT / "output"

# Import sibling data modules
sys.path.insert(0, str(SCRIPTS))
import content as content_mod   # noqa: E402
import captions as captions_mod  # noqa: E402

# ---------- CONFIG ----------
REPO_RAW_URL = (
    "https://raw.githubusercontent.com/"
    "waseemnasir2k26/skynetlabs-carousels-batch5/main"
)
START_DATE = "2026-04-10"   # Friday
POST_TIME = "10:00:00"      # 10:00 AM EST
SKIP_WEEKENDS = True

CATEGORY_LABELS = {
    "A": "AI Tools",
    "B": "Automation",
    "C": "Frameworks",
    "D": "Research",
    "E": "Case Studies",
    "F": "Mental Models",
}

CATEGORY_TAGS = {
    "A": "ai,tools,claude,cursor,skynetjoe",
    "B": "automation,n8n,aiagents,skynetjoe",
    "C": "agency,frameworks,solopreneur,skynetjoe",
    "D": "data,research,airesearch,skynetjoe",
    "E": "casestudy,agency,aiwork,skynetjoe",
    "F": "mentalmodels,founder,mindset,skynetjoe",
}

PINTEREST_LINKS = [
    "https://www.skynetjoe.com",
    "https://skynetlabs-toolkit.vercel.app",
    "https://www.waseemnasir.com",
    "https://github.com/waseemnasir2k26",
]


# ---------- Advanced 39-col headers (exact GHL format) ----------
HEADER_ROW_1 = [
    "All Social"] * 11 + [
    "Facebook",
    "Instagram",
    "LinkedIn", "LinkedIn",
    "Google (GBP)"] * 1 + ["Google (GBP)"] * 9 + [
    "YouTube", "YouTube", "YouTube",
    "TikTok"] * 7 + [
    "Community", "Community",
    "Pinterest", "Pinterest",
]

# Rebuild cleanly to avoid list-multiply bugs
HEADER_ROW_1 = (
    ["All Social"] * 11
    + ["Facebook"]
    + ["Instagram"]
    + ["LinkedIn", "LinkedIn"]
    + ["Google (GBP)"] * 10
    + ["YouTube", "YouTube", "YouTube"]
    + ["TikTok"] * 7
    + ["Community", "Community"]
    + ["Pinterest", "Pinterest"]
)

HEADER_ROW_2 = [
    "postAtSpecificTime (YYYY-MM-DD HH:mm:ss)",
    "content",
    "OGmetaUrl (url)",
    "imageUrls (comma-separated)",
    "gifUrl",
    "videoUrls (comma-separated)",
    "mediaOptimization (true/false)",
    "applyWatermark (true/false)",
    "tags (comma-separated)",
    "category",
    "followUpComment",
    "type (post/story/reel)",        # Facebook
    "type (post/story/reel)",        # Instagram
    "pdfTitle",                      # LinkedIn
    "postAsPdf (true/false)",        # LinkedIn
    "eventType (call_to_action/event/offer)",
    "actionType (none/order/book/shop/learn_more/call/sign_up)",
    "title",
    "offerTitle",
    "startDate (YYYY-MM-DD HH:mm:ss)",
    "endDate (YYYY-MM-DD HH:mm:ss)",
    "termsConditions",
    "couponCode",
    "redeemOnlineUrl",
    "actionUrl",
    "title",                          # YouTube
    "privacyLevel (private/public/unlisted)",
    "type (video/short)",
    "privacyLevel (everyone/friends/only_me)",  # TikTok
    "promoteOtherBrand (true/false)",
    "enableComment (true/false)",
    "enableDuet (true/false)",
    "enableStitch (true/false)",
    "videoDisclosure (true/false)",
    "promoteYourBrand (true/false)",
    "title",                          # Community
    "notifyAllGroupMembers (true/false)",
    "title",                          # Pinterest
    "link",                           # Pinterest
]

assert len(HEADER_ROW_1) == 39, f"Row1 has {len(HEADER_ROW_1)} cols, need 39"
assert len(HEADER_ROW_2) == 39, f"Row2 has {len(HEADER_ROW_2)} cols, need 39"


def title_slug(title: str) -> str:
    """Must match generator.py slug() exactly."""
    return (title.lower()
            .replace(" ", "-")
            .replace("\u2014", "-")   # em dash
            .replace("/", "-")
            .replace(",", "")
            .replace("'", "")
            .replace("\u2019", "")    # right single quote
            .replace(".", "")
            .replace("(", "")
            .replace(")", ""))[:60]


def slide_urls_for(carousel_id: int, title: str, num_slides: int) -> list:
    from urllib.parse import quote
    folder = f"{carousel_id:02d}_{title_slug(title)}"
    # URL-encode folder name so chars like % become %25 (GitHub raw requires it)
    safe_folder = quote(folder, safe="-_.$")
    return [
        f"{REPO_RAW_URL}/slides/{safe_folder}/slide_{i:02d}.png"
        for i in range(1, num_slides + 1)
    ]


def next_weekday(date: datetime) -> datetime:
    """If date falls on Sat/Sun, push to Mon."""
    while date.weekday() >= 5:  # 5 = Sat, 6 = Sun
        date += timedelta(days=1)
    return date


def schedule_dates(n: int) -> list:
    """30 weekdays, 10:00 AM EST, starting Friday 2026-04-10."""
    start = datetime.strptime(f"{START_DATE} {POST_TIME}", "%Y-%m-%d %H:%M:%S")
    dates = []
    d = start
    while len(dates) < n:
        if SKIP_WEEKENDS:
            d = next_weekday(d)
        dates.append(d)
        d = d + timedelta(days=1)
    return dates


def build_row(carousel: dict, caption: dict, when: datetime) -> list:
    cid = carousel["id"]
    cat = carousel["category"]
    title = carousel["title"]
    subtitle = carousel.get("subtitle", "")
    num_slides = len(carousel["slides"])

    # content body = caption + hashtags + subtle brand line
    hashtags_line = " ".join(caption["hashtags"])
    body = f"{caption['caption']}\n\n{hashtags_line}"

    # Image URL: hook slide only (GHL CSV parser breaks on multiple
    # comma-separated URLs inside a quoted field — treats internal commas
    # as column separators, shifting all columns right and losing media)
    urls = slide_urls_for(cid, title, num_slides)
    image_urls_csv = urls[0]  # slide_01 = hook slide

    # LinkedIn PDF title — what shows in the document post header
    pdf_title = f"{title} — {subtitle}" if subtitle else title
    # GHL maxes pdfTitle around 100 chars
    pdf_title = pdf_title[:95]

    # Pinterest + YouTube fallback title
    short_title = title[:90]

    # Rotating Pinterest destination
    pin_link = PINTEREST_LINKS[(cid - 1) % len(PINTEREST_LINKS)]

    # Interactive first comment
    first_comment = caption["first_comment"]

    row = [
        when.strftime("%Y-%m-%d %H:%M:%S"),    # 1  postAtSpecificTime
        body,                                   # 2  content
        "",                                     # 3  OGmetaUrl
        image_urls_csv,                         # 4  imageUrls (hook slide)
        "",                                     # 5  gifUrl
        "",                                     # 6  videoUrls
        "TRUE",                                 # 7  mediaOptimization
        "FALSE",                                # 8  applyWatermark
        CATEGORY_TAGS[cat],                     # 9  tags
        CATEGORY_LABELS[cat],                   # 10 category
        first_comment,                          # 11 followUpComment (interactive)
        "",                                     # 12 FB type (skip — already in prev CSV)
        "post",                                 # 13 IG type
        "",                                     # 14 LinkedIn pdfTitle (skip — already in prev CSV)
        "FALSE",                                # 15 LinkedIn postAsPdf (skip)
        "",                                     # 16 GBP eventType
        "",                                     # 17 GBP actionType
        "",                                     # 18 GBP title
        "",                                     # 19 GBP offerTitle
        "",                                     # 20 GBP startDate
        "",                                     # 21 GBP endDate
        "",                                     # 22 GBP termsConditions
        "",                                     # 23 GBP couponCode
        "",                                     # 24 GBP redeemOnlineUrl
        "",                                     # 25 GBP actionUrl
        short_title,                            # 26 YouTube title (unused, kept for row shape)
        "public",                               # 27 YouTube privacy
        "short",                                # 28 YouTube type
        "everyone",                             # 29 TikTok privacy
        "FALSE",                                # 30 promoteOtherBrand
        "TRUE",                                 # 31 enableComment
        "TRUE",                                 # 32 enableDuet
        "TRUE",                                 # 33 enableStitch
        "FALSE",                                # 34 videoDisclosure
        "FALSE",                                # 35 promoteYourBrand
        short_title,                            # 36 Community title
        "FALSE",                                # 37 notifyAllGroupMembers
        short_title,                            # 38 Pinterest title
        pin_link,                               # 39 Pinterest link
    ]
    assert len(row) == 39, f"Row has {len(row)} cols, need 39"
    return row


def write_csv(rows: list, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        w.writerow(HEADER_ROW_1)
        w.writerow(HEADER_ROW_2)
        for r in rows:
            w.writerow(r)


def write_captions_json(dates: list, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    data = []
    for c, cap, when in zip(content_mod.CAROUSELS, captions_mod.CAPTIONS, dates):
        num_slides = len(c["slides"])
        urls = slide_urls_for(c["id"], c["title"], num_slides)
        data.append({
            "id": c["id"],
            "category": c["category"],
            "category_label": CATEGORY_LABELS[c["category"]],
            "title": c["title"],
            "subtitle": c.get("subtitle", ""),
            "scheduled_at": when.strftime("%Y-%m-%d %H:%M:%S"),
            "num_slides": num_slides,
            "caption": cap["caption"],
            "hashtags": cap["hashtags"],
            "first_comment_style": cap["first_comment_style"],
            "first_comment": cap["first_comment"],
            "slide_urls": urls,
        })
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    carousels = content_mod.CAROUSELS
    caps_by_id = {c["id"]: c for c in captions_mod.CAPTIONS}

    missing = [c["id"] for c in carousels if c["id"] not in caps_by_id]
    if missing:
        raise SystemExit(f"Missing captions for carousels: {missing}")

    n = len(carousels)
    dates = schedule_dates(n)

    # build CSV rows in carousel order
    rows = []
    for carousel, when in zip(carousels, dates):
        cap = caps_by_id[carousel["id"]]
        rows.append(build_row(carousel, cap, when))

    csv_path = OUTPUT_DIR / "ghl-batch5-ig-pinterest.csv"
    write_csv(rows, csv_path)

    json_path = OUTPUT_DIR / "captions.json"
    write_captions_json(dates, json_path)

    print(f"CSV written:      {csv_path}")
    print(f"Captions JSON:    {json_path}")
    print(f"Total rows:       {n}")
    print(f"Schedule window:  {dates[0]:%Y-%m-%d} -> {dates[-1]:%Y-%m-%d}")
    print()
    print("Import via GHL > Marketing > Social Planner > Bulk Upload > Advanced.")
    print("Images must be publicly accessible before upload.")


if __name__ == "__main__":
    main()
