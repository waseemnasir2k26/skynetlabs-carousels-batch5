# SkynetLabs Carousel Batch 5 — 30 Multi-Platform Carousels

30 document-style carousels for **LinkedIn + Instagram + Facebook + Pinterest**, bulk-posted via GoHighLevel.

Built by [Waseem Nasir](https://www.waseemnasir.com) / [SkynetLabs](https://www.skynetjoe.com).

---

## What's Inside

| Path | Count | Purpose |
|------|-------|---------|
| `slides/01_*/slide_01.png` → `30_*/slide_12.png` | 339 PNGs | 1080×1350 individual slides |
| `pdfs/01_*.pdf` → `30_*.pdf` | 30 PDFs | LinkedIn document-post fallback |
| `output/ghl-batch5-carousels.csv` | 1 | Advanced 39-col GHL bulk upload |
| `output/captions.json` | 1 | Captions + hashtags + first comments |
| `STRATEGY-BRIEF.md` | 1 | Competitor research + design system |

## 6 Design Families (5 carousels each)

| Code | Name | Vibe | Category |
|------|------|------|----------|
| A | **Neon Terminal** | Retro CRT hacker, green phosphor | AI Tools |
| B | **Circuit Board** | PCB diagram, electric blue traces | Automation |
| C | **Executive Navy** | McKinsey-premium navy + gold | Frameworks |
| D | **Data Lab** | Bloomberg + research journal | Research / Data |
| E | **Case File** | Vintage kraft-paper investigator | Case Studies |
| F | **Mindscape** | Warm sunrise gradient | Mental Models |

## Content Philosophy

- 24 carousels = pure value (frameworks, research, tools, data)
- 4 = teachable case studies
- 2 = soft brand stories
- **0 hard sells**

## Interactive First Comments

Every carousel has an engagement-trigger first comment, rotating across 6 styles:
`POLL · CHALLENGE · OPINION · FILL_BLANK · TRADE · RESOURCE`

## Build Pipeline

```bash
cd scripts
python generator.py    # renders all PNGs + PDFs
python build_csv.py    # builds GHL CSV + captions.json
```

## How to Upload to GoHighLevel

1. GHL → **Marketing → Social Planner → Bulk Upload → Advanced**
2. Upload `output/ghl-batch5-carousels.csv`
3. Verify images load from raw.githubusercontent.com
4. Confirm schedule (Apr 10 → May 21, 2026, weekdays 10 AM EST)
5. Publish

LinkedIn posts use `postAsPdf=TRUE` so slides auto-stitch into a document.
Facebook and Instagram get a native swipeable carousel.
Pinterest publishes each slide as a pin.

---

Part of the SkynetLabs social-content system. Previous batches:

- **Batch 1** — image posts
- **Batch 2** — video reels
- **Batch 3** — LinkedIn text posts
- **Batch 4** — [AI Motivational Quote Cards](https://github.com/waseemnasir2k26/ai-motivational-posts)
- **Batch 5** — 30 Multi-Platform Carousels (this repo)
