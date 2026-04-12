"""
build_pinterest_csv.py — SkynetLabs Carousel Batch 5
Pinterest-ONLY GHL CSV with full SEO optimization.

Key differences from the original IG+Pinterest CSV:
  1. Pinterest SEO titles (keyword-rich, search-optimized, 100 chars max)
  2. Pinterest-native descriptions (keyword paragraphs, NO hashtags)
  3. ALL links → skynetjoe.com with UTM tracking params
  4. Uses tall infographic pins (pinterest-pins/) instead of hook slides
  5. Pinterest boards mapped via tags column
  6. IG/FB/LinkedIn columns intentionally empty (Pinterest-only CSV)

Output: output/ghl-pinterest-seo.csv
"""

import csv
import sys
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent.parent
SCRIPTS = Path(__file__).parent
OUTPUT_DIR = ROOT / "output"

sys.path.insert(0, str(SCRIPTS))

# ---------- CONFIG ----------
REPO_RAW_URL = (
    "https://raw.githubusercontent.com/"
    "waseemnasir2k26/skynetlabs-carousels-batch5/main"
)
START_DATE = "2026-04-13"   # Monday — first unposted date (Apr 10 already posted)
POST_TIME = "14:00:00"      # 2 PM EST — Pinterest peak time (afternoon users)
SKIP_WEEKENDS = True

BASE_URL = "https://www.skynetjoe.com"


# ---------- PINTEREST SEO DATA ----------
# Each pin gets: seo_title, description (keyword-rich), landing_path, board, keywords
PINTEREST_DATA = [
    # ===== CATEGORY A — AI Tools (pins 1-5) =====
    {
        "id": 1,
        "seo_title": "Claude vs Cursor vs Windsurf: Best AI Coding Tools Compared (2026)",
        "description": (
            "Honest side-by-side comparison of the top 3 AI coding tools in 2026. "
            "Claude Code excels at deep reasoning and refactors. Cursor wins on speed and autocomplete. "
            "Windsurf is best for onboarding new developers. "
            "See real benchmarks, use cases, and which tool to use for each task. "
            "The smart move? Stack all three. Get the full breakdown at skynetjoe.com"
        ),
        "landing": "/",
        "board": "AI Tools & Software",
        "keywords": "ai coding tools,claude code,cursor ai,windsurf,ai comparison,best ai tools 2026",
    },
    {
        "id": 2,
        "seo_title": "15 Free AI Tools for Agencies & Freelancers You Need in 2026",
        "description": (
            "Discover 15 completely free AI tools most digital agencies don't know exist. "
            "From Perplexity for research to NotebookLM for document analysis, Gamma for pitch decks, "
            "and Ideogram for AI images with readable text. "
            "Build a $0/month AI stack that rivals $2K/month subscriptions. "
            "Full list with use cases and free tier details at skynetjoe.com"
        ),
        "landing": "/",
        "board": "AI Tools & Software",
        "keywords": "free ai tools,ai tools for business,free ai software,perplexity ai,notebooklm",
    },
    {
        "id": 3,
        "seo_title": "ChatGPT vs Claude vs Gemini: Which AI Model for Each Task (2026 Guide)",
        "description": (
            "Stop picking one AI model. Route tasks to the right one. "
            "Claude wins for writing and code. Gemini dominates research with real-time web access. "
            "ChatGPT is still the best brainstorming partner. "
            "This routing table shows exactly which model to use for writing, research, coding, vision, and agents. "
            "Save this comparison chart for your daily AI workflow."
        ),
        "landing": "/",
        "board": "AI Tools & Software",
        "keywords": "chatgpt vs claude,ai model comparison,best ai model,gemini vs chatgpt,ai for business",
    },
    {
        "id": 4,
        "seo_title": "2026 AI Tool Reality Check: Winners, Losers & Overhyped Tools",
        "description": (
            "The honest AI tool scoreboard for 2026. Winners: Claude, n8n, Gemini 2.5, Lovable. "
            "Losers: Jasper, Copy.ai, Writesonic, generic GPT wrappers. "
            "Overhyped: most 'AI agents' and $20/month ChatGPT clones. "
            "87% of AI tools you paid for in 2025 are replaceable by Claude + n8n alone. "
            "Audit your AI stack with this guide before you renew any subscription."
        ),
        "landing": "/",
        "board": "AI Tools & Software",
        "keywords": "ai tools review,best ai tools,ai tool comparison,ai software 2026,ai stack",
    },
    {
        "id": 5,
        "seo_title": "The $0 AI Stack: Run Your Entire Business on Free AI Tools",
        "description": (
            "Build and run a real business using only free AI tool tiers. "
            "Claude free for writing, n8n self-hosted for automation ($4/month), "
            "Vercel for websites, Notion for CRM, Brevo for email marketing. "
            "Total monthly cost: $4. Stop burning $500/month on tools you never open. "
            "Free tier beats paid plan you don't use. Get the full free stack list."
        ),
        "landing": "/",
        "board": "AI Tools & Software",
        "keywords": "free business tools,free ai stack,bootstrap business tools,free automation tools,zero cost ai",
    },

    # ===== CATEGORY B — Automation (pins 6-10) =====
    {
        "id": 6,
        "seo_title": "10 n8n Automation Workflows That Replace Full-Time Job Roles",
        "description": (
            "Real n8n workflow templates that replaced $9.3K/month in staff costs. "
            "Lead enricher, content recycler, invoice autopilot, inbox triage, and client reporter. "
            "Each workflow runs on a $10/month n8n server and handles tasks that used to require "
            "an SDR intern, junior copywriter, and bookkeeper. "
            "Get the JSON templates and start automating your agency today."
        ),
        "landing": "/",
        "board": "Business Automation & Workflows",
        "keywords": "n8n workflows,business automation,workflow automation,n8n templates,automate business",
    },
    {
        "id": 7,
        "seo_title": "n8n Beginner Cheat Sheet: Visual Guide to Workflow Automation",
        "description": (
            "Learn n8n in 10 minutes with this visual cheat sheet. "
            "The 6 concepts you need: Triggers, Nodes, Expressions, If/Switch, Loops, and Merge. "
            "Includes a starter workflow template: Cron trigger, HTTP request, OpenAI summary, Gmail send. "
            "4 nodes, real business value. No coding experience required. "
            "Perfect for beginners learning workflow automation and no-code tools."
        ),
        "landing": "/",
        "board": "Business Automation & Workflows",
        "keywords": "n8n tutorial,n8n beginner guide,workflow automation,no code automation,n8n cheat sheet",
    },
    {
        "id": 8,
        "seo_title": "7 Hidden Automation Opportunities in Every Business (Find Them in 20 Min)",
        "description": (
            "Every business has $5K/month of automation opportunities hiding in plain sight. "
            "The copy-paste job, the Excel ghost, the Slack DM loop, the report builder, "
            "the human router, the inbox filter, and the reminder nag. "
            "Ask 3 questions to find all 7: What do you hate doing weekly? "
            "What spreadsheet do 3 people touch? Where do you copy-paste? "
            "Start saving with these automation quick wins."
        ),
        "landing": "/",
        "board": "Business Automation & Workflows",
        "keywords": "business automation ideas,automation opportunities,workflow efficiency,process automation",
    },
    {
        "id": 9,
        "seo_title": "How to Audit Any Business for Automation: 5-Step Framework (Free Template)",
        "description": (
            "The exact 5-step automation audit framework used by our agency. "
            "Step 1: Map the top 5 repeated tasks. Step 2: Calculate time and dollar value. "
            "Step 3: Filter by rule-based logic. Step 4: Match to automation tools. "
            "Step 5: Ship the lowest-risk workflow first. "
            "Average savings from one audit: $8.2K/month across our last 12 clients. "
            "Download the free audit template at skynetjoe.com"
        ),
        "landing": "/",
        "board": "Business Automation & Workflows",
        "keywords": "automation audit,business process audit,automation consulting,workflow optimization",
    },
    {
        "id": 10,
        "seo_title": "20 AI Agent Prompts That Actually Work in Production (Tested & Proven)",
        "description": (
            "Production-tested AI agent prompts for real business use cases. "
            "Lead qualifier, email triager, meeting summarizer, content recycler, and support ticket tagger. "
            "The pattern: Role + Task + Output format + One-word constraint. "
            "94% classification accuracy using Claude with temperature 0. "
            "Stop using demo prompts. These are running in live client systems right now. "
            "Get the full prompt library at skynetjoe.com"
        ),
        "landing": "/",
        "board": "Business Automation & Workflows",
        "keywords": "ai prompts,prompt engineering,ai agent prompts,chatgpt prompts,production ai",
    },

    # ===== CATEGORY C — Agency Frameworks (pins 11-15) =====
    {
        "id": 11,
        "seo_title": "The $10K/Month Agency Operating System: 6 Pillars Framework",
        "description": (
            "The complete operating system to break through the $5K/month agency ceiling. "
            "6 pillars: Offer (one niche, one outcome), Pipeline (1 inbound + 1 outbound), "
            "Delivery (SOPs + automation), Pricing ($3K minimum), Weekly rhythm, and 3 key metrics. "
            "Went from $2,800 to $11,400 in the first month using this system. "
            "Built from 7 years of expensive agency mistakes. Save this framework."
        ),
        "landing": "/",
        "board": "Agency Growth & Business Strategy",
        "keywords": "agency operating system,agency growth,digital agency tips,agency business model,10k agency",
    },
    {
        "id": 12,
        "seo_title": "10 Pricing Models for AI & Digital Agencies (With Real Revenue Numbers)",
        "description": (
            "Stop underpricing your agency work. 10 pricing models tested with real revenue numbers. "
            "Hourly ($50-300/hr), project-based ($3-15K), retainers ($1-10K/month), "
            "value-based (% of savings), performance ($50/lead), productized ($4,997 fixed), "
            "subscription + usage, and equity models. "
            "Start with productized, scale to retainer, leverage with value-based pricing. "
            "Never charge hourly unless it is a one-off."
        ),
        "landing": "/",
        "board": "Agency Growth & Business Strategy",
        "keywords": "agency pricing,freelance pricing,consulting rates,how to price services,agency revenue",
    },
    {
        "id": 13,
        "seo_title": "90-Minute Agency Setup Checklist: Launch Your Agency This Afternoon",
        "description": (
            "Set up your entire agency in 90 minutes flat. No expensive tools needed. "
            "Minutes 0-15: Write your one-sentence offer. 15-30: Ship a Vercel landing page. "
            "30-45: Build a Notion CRM. 45-60: Create delivery templates. "
            "60-75: Pick one pipeline channel. 75-90: Send 10 DMs to dream clients. "
            "Stop overthinking. Ship ugly, iterate fast. "
            "Free checklist template at skynetjoe.com"
        ),
        "landing": "/",
        "board": "Agency Growth & Business Strategy",
        "keywords": "start an agency,agency checklist,agency setup guide,launch digital agency,freelance to agency",
    },
    {
        "id": 14,
        "seo_title": "Solo Founder Weekly Schedule: 32-Hour Work Week Operating Rhythm",
        "description": (
            "The weekly operating rhythm that replaced 80-hour burnout weeks with 32 focused hours. "
            "Monday: pipeline and outbound (2 hours). Tuesday: deep work on delivery. "
            "Wednesday: batched client calls. Thursday: internal systems and content. "
            "Friday: weekly review and planning. Saturday-Sunday: completely off. "
            "Rhythm beats hustle. Batch beats context-switching. Rest is strategy."
        ),
        "landing": "/",
        "board": "Agency Growth & Business Strategy",
        "keywords": "solopreneur schedule,founder routine,weekly planning,work life balance,productivity system",
    },
    {
        "id": 15,
        "seo_title": "10 Copywriting Frameworks with AI Prompts (AIDA, PAS, BAB & More)",
        "description": (
            "10 proven copywriting frameworks, each paired with a tested AI prompt you can steal. "
            "AIDA (Attention-Interest-Desire-Action), PAS (Problem-Agitate-Solve), "
            "BAB (Before-After-Bridge), 4Ps, and 6 more most people have never heard of. "
            "Not AI slop. Real frameworks with battle-tested prompts for landing pages, "
            "sales emails, and ad copy. Save this for your next conversion project."
        ),
        "landing": "/",
        "board": "Agency Growth & Business Strategy",
        "keywords": "copywriting frameworks,ai copywriting,aida framework,copywriting formulas,sales copy ai",
    },

    # ===== CATEGORY D — Research & Data (pins 16-20) =====
    {
        "id": 16,
        "seo_title": "Why 90% of AI Agencies Will Fail in 2026 (Data-Backed Analysis)",
        "description": (
            "Data-driven analysis of AI agency survival rates from Q1 2024 to Q1 2026. "
            "The pattern is brutal and consistent. Most agencies die not because of AI, "
            "but because they never had a real business model, real systems, or real differentiation. "
            "What the surviving 10% do differently: niche specialization, productized offers, "
            "and recurring revenue. If you run an agency, read this before it is too late."
        ),
        "landing": "/",
        "board": "AI Industry Research & Trends",
        "keywords": "ai agency,agency failure rate,ai business model,digital agency trends,ai industry 2026",
    },
    {
        "id": 17,
        "seo_title": "AI Content vs Human Content Performance: 500+ Post Analysis (2026 Data)",
        "description": (
            "Real performance data from auditing 500+ posts across LinkedIn, Instagram, and blogs. "
            "AI-written vs human-written content compared on engagement, reach, and conversion. "
            "The results surprise both the 'AI content is dead' crowd and the 'AI writes everything' crowd. "
            "The truth is nuanced: AI-assisted content with human editing outperforms pure AI and pure human. "
            "See the metrics and learn the optimal content workflow."
        ),
        "landing": "/",
        "board": "AI Industry Research & Trends",
        "keywords": "ai content marketing,ai writing performance,content marketing data,ai vs human writing",
    },
    {
        "id": 18,
        "seo_title": "AEO vs SEO: Answer Engine Optimization Guide for 2026 (New Rules)",
        "description": (
            "The rules of search changed in 2026. AEO (Answer Engine Optimization) targets "
            "ChatGPT, Claude, Perplexity, and Gemini instead of just Google blue links. "
            "Learn how to optimize your content for AI answer engines, what structured data matters, "
            "and why traditional SEO alone is a dying strategy. "
            "Includes an AEO audit checklist you can apply to your website this week. "
            "Full guide at skynetjoe.com"
        ),
        "landing": "/",
        "board": "AI Industry Research & Trends",
        "keywords": "aeo optimization,answer engine optimization,seo vs aeo,ai seo,seo 2026,search optimization",
    },
    {
        "id": 19,
        "seo_title": "AI Adoption by Industry: Real 2026 Data (Which Industries Lead & Lag)",
        "description": (
            "Forget the hype cycle. These are the real AI adoption numbers by industry from Q1 2026. "
            "Tech and finance lead. Healthcare and education are catching up fast. "
            "Construction and manufacturing are decades behind. "
            "One industry is ripe for disruption right now. "
            "Find your industry, assess your competition, and identify the AI opportunity gap. "
            "Data-driven analysis with actionable insights."
        ),
        "landing": "/",
        "board": "AI Industry Research & Trends",
        "keywords": "ai adoption,ai industry data,ai statistics 2026,ai business trends,ai transformation",
    },
    {
        "id": 20,
        "seo_title": "Real Cost of Running an AI Agency in 2026 (Honest Numbers & Margins)",
        "description": (
            "Not another 'I made $50K in 30 days' post. Real numbers from running an AI agency. "
            "Tool costs, API bills, hosting, contractor rates, insurance, and the hidden expenses "
            "nobody talks about. See actual monthly P&L, real margins, and which costs to cut first. "
            "If you are thinking of starting an AI agency, read this before you register the LLC. "
            "Transparent breakdown at skynetjoe.com"
        ),
        "landing": "/",
        "board": "AI Industry Research & Trends",
        "keywords": "ai agency costs,start ai agency,agency profit margins,ai business expenses,agency finances",
    },

    # ===== CATEGORY E — Case Studies (pins 21-25) =====
    {
        "id": 21,
        "seo_title": "Anatomy of a $50K AI Project: Full Scope, Process & Invoice Breakdown",
        "description": (
            "Complete breakdown of a real $50K AI consulting project. "
            "From discovery call to proposal, build, delivery, and ongoing retainer. "
            "See the actual scope, timeline, team structure, and invoice structure. "
            "Names and industries anonymized, but all numbers are real. "
            "Paid $50K once, saved $200K per year. Every year. Forever. "
            "Includes the proposal template used to close the deal."
        ),
        "landing": "/",
        "board": "AI Case Studies & Client Results",
        "keywords": "ai consulting project,ai project scope,agency case study,50k project breakdown,ai proposal",
    },
    {
        "id": 22,
        "seo_title": "Before AI vs After AI: 10 Real Agency Workflow Transformations",
        "description": (
            "Side-by-side comparisons of 10 agency workflows before and after adding AI. "
            "Real metrics: time saved, errors reduced, margins improved. "
            "Lead generation, content creation, reporting, client onboarding, and admin workflows. "
            "Not 'AI will change everything' hype. Actual receipts from real agency operations. "
            "See which workflows deliver the highest ROI when you add automation."
        ),
        "landing": "/",
        "board": "AI Case Studies & Client Results",
        "keywords": "ai workflow automation,before after ai,agency automation,ai roi,business transformation",
    },
    {
        "id": 23,
        "seo_title": "How 3 Automation Workflows Replaced a 5-Person Team (Case Study)",
        "description": (
            "Real case study: 3 n8n automation workflows that let a 5-person team do the work of 25. "
            "We kept the team and promoted them. The automation replaced the manual work, not the people. "
            "See the 3 workflows, the tech stack, the implementation timeline, and the math. "
            "AI should multiply your team, not replace it. "
            "Full technical breakdown with workflow architecture included."
        ),
        "landing": "/",
        "board": "AI Case Studies & Client Results",
        "keywords": "automation case study,n8n case study,team automation,workflow replacement,ai efficiency",
    },
    {
        "id": 24,
        "seo_title": "10 Lessons From Building 100+ Client Websites (Hard-Won Wisdom)",
        "description": (
            "After shipping 100+ production websites for real clients, these are the 10 lessons "
            "I wish someone had given me on site number 1. "
            "Covering client communication, scope management, design decisions, tech stack choices, "
            "pricing mistakes, and the single biggest time waster in web development. "
            "If you build websites for clients, this will save you a year of painful learning."
        ),
        "landing": "/",
        "board": "AI Case Studies & Client Results",
        "keywords": "web design tips,client website lessons,freelance web development,website business,web agency",
    },
    {
        "id": 25,
        "seo_title": "Turn $500 Clients Into $10K/Month Revenue: 3-Move Playbook",
        "description": (
            "Your first client probably paid $500. Here is how to transform that relationship "
            "into $10K/month recurring revenue without switching agencies or finding new clients. "
            "3 strategic moves most founders miss completely. "
            "Use this playbook for your next client renewal conversation. "
            "Includes scripts and templates for the upsell conversation. "
            "Full transformation playbook at skynetjoe.com"
        ),
        "landing": "/",
        "board": "AI Case Studies & Client Results",
        "keywords": "client upselling,increase client revenue,agency revenue growth,recurring revenue,client retention",
    },

    # ===== CATEGORY F — Mental Models (pins 26-30) =====
    {
        "id": 26,
        "seo_title": "10 Mental Models Every AI Founder & Entrepreneur Should Know",
        "description": (
            "AI moves too fast for tactics. You need thinking frameworks that stay true "
            "when everything else changes. These 10 mental models cover pricing, hiring, "
            "shipping, positioning, and knowing when to say no. "
            "Including Hanlon's Razor, Pareto Principle, and frameworks most founders never discover. "
            "Save this and revisit quarterly. Models compound. Skills decay."
        ),
        "landing": "/",
        "board": "Entrepreneurship & Founder Mindset",
        "keywords": "mental models,founder mindset,entrepreneurship tips,business frameworks,decision making",
    },
    {
        "id": 27,
        "seo_title": "Founder Mental Health Playbook: Real Strategies (Not Hustle Culture)",
        "description": (
            "No hustle culture BS. No 5am cold plunge nonsense. "
            "A real mental health playbook written after year 3 of running an agency, "
            "when the pressure almost broke me. "
            "Covers burnout prevention, boundary setting, therapy timing, exercise as strategy, "
            "and the conversation nobody in tech wants to have. "
            "If you are a solo founder, please read this. Your business needs you healthy."
        ),
        "landing": "/",
        "board": "Entrepreneurship & Founder Mindset",
        "keywords": "founder mental health,entrepreneur burnout,work life balance,startup stress,founder wellness",
    },
    {
        "id": 28,
        "seo_title": "7 Must-Read Books for AI Agency Owners (None About AI)",
        "description": (
            "The 7 books that changed how I run my AI agency, and none of them are about AI. "
            "Business strategy, pricing psychology, market positioning, mental models, "
            "and negotiation frameworks. Ranked by impact on actual revenue. "
            "These books will make you a better business operator, not just a better technologist. "
            "Save this reading list for your next growth phase."
        ),
        "landing": "/",
        "board": "Entrepreneurship & Founder Mindset",
        "keywords": "business books,entrepreneur reading list,agency books,best business books,founder books",
    },
    {
        "id": 29,
        "seo_title": "The Art of Saying No: 7 Scripts for Freelancers & Agency Owners",
        "description": (
            "Every yes to a bad client is a no to the right one. "
            "7 copy-paste scripts for the hardest conversations in agency life: "
            "scope creep, discount requests, quick favors, family friend projects, "
            "and the client who wants everything for nothing. "
            "Say no without burning bridges. Protect your margins and your sanity. "
            "Save these scripts. You will need them this week."
        ),
        "landing": "/",
        "board": "Entrepreneurship & Founder Mindset",
        "keywords": "saying no scripts,freelancer boundaries,client management,scope creep,agency boundaries",
    },
    {
        "id": 30,
        "seo_title": "Freelancer to Agency Transition: 4-Stage Roadmap with Revenue Triggers",
        "description": (
            "Most freelancers try to become an agency by hiring people. That is how you go broke. "
            "The real transition has 4 stages, each with a specific revenue trigger. "
            "Skip a stage and you crash. Follow the roadmap and you scale sustainably. "
            "Covers when to hire, what to systematize, pricing transitions, "
            "and the exact revenue milestones that signal readiness for the next stage."
        ),
        "landing": "/",
        "board": "Entrepreneurship & Founder Mindset",
        "keywords": "freelancer to agency,scale freelance business,agency growth roadmap,hire first employee",
    },
]


# ---------- GHL 39-col headers ----------
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


def schedule_dates(n: int) -> list:
    """Weekdays only, 2 PM EST, starting Monday Apr 13."""
    start = datetime.strptime(f"{START_DATE} {POST_TIME}", "%Y-%m-%d %H:%M:%S")
    dates = []
    d = start
    while len(dates) < n:
        if SKIP_WEEKENDS:
            while d.weekday() >= 5:
                d += timedelta(days=1)
        dates.append(d)
        d = d + timedelta(days=1)
    return dates


def pin_image_url(pin_id: int) -> str:
    """Public GitHub raw URL for the tall Pinterest pin."""
    return f"{REPO_RAW_URL}/pinterest-pins/pin_{pin_id:02d}.png"


def utm_link(landing: str, pin_id: int) -> str:
    """Build skynetjoe.com URL with UTM tracking."""
    base = BASE_URL.rstrip("/") + landing
    return (
        f"{base}?utm_source=pinterest&utm_medium=pin"
        f"&utm_campaign=batch5-carousels&utm_content=pin_{pin_id:02d}"
    )


def build_row(pin_data: dict, when: datetime) -> list:
    pid = pin_data["id"]

    # Pinterest description as the content field (keyword-rich, NO hashtags)
    body = pin_data["description"]

    # Image: tall Pinterest pin
    image_url = pin_image_url(pid)

    # Pinterest title (SEO-optimized, max 100 chars)
    pin_title = pin_data["seo_title"][:100]

    # Pinterest link with UTM tracking — ALL to skynetjoe.com
    pin_link = utm_link(pin_data["landing"], pid)

    # Tags for GHL organization (maps to board name concept)
    tags = pin_data["keywords"]

    # Board name as category
    category = pin_data["board"]

    row = [
        when.strftime("%Y-%m-%d %H:%M:%S"),    # 1  postAtSpecificTime
        body,                                   # 2  content (Pinterest description)
        "",                                     # 3  OGmetaUrl (empty)
        image_url,                              # 4  imageUrls (tall pin)
        "",                                     # 5  gifUrl
        "",                                     # 6  videoUrls
        "TRUE",                                 # 7  mediaOptimization
        "FALSE",                                # 8  applyWatermark
        tags,                                   # 9  tags
        category,                               # 10 category
        "",                                     # 11 followUpComment (not used on Pinterest)
        "",                                     # 12 FB type (EMPTY — Pinterest only)
        "",                                     # 13 IG type (EMPTY — Pinterest only)
        "",                                     # 14 LinkedIn pdfTitle
        "FALSE",                                # 15 LinkedIn postAsPdf
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
        "",                                     # 26 YouTube title
        "",                                     # 27 YouTube privacy
        "",                                     # 28 YouTube type
        "",                                     # 29 TikTok privacy
        "",                                     # 30 promoteOtherBrand
        "",                                     # 31 enableComment
        "",                                     # 32 enableDuet
        "",                                     # 33 enableStitch
        "",                                     # 34 videoDisclosure
        "",                                     # 35 promoteYourBrand
        "",                                     # 36 Community title
        "",                                     # 37 notifyAllGroupMembers
        pin_title,                              # 38 Pinterest title (SEO)
        pin_link,                               # 39 Pinterest link (UTM tracked)
    ]
    assert len(row) == 39, f"Row has {len(row)} cols, need 39"
    return row


def main():
    n = len(PINTEREST_DATA)
    dates = schedule_dates(n)

    rows = []
    for pin_data, when in zip(PINTEREST_DATA, dates):
        rows.append(build_row(pin_data, when))

    # Write CSV
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = OUTPUT_DIR / "ghl-pinterest-seo.csv"
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        w.writerow(HEADER_ROW_1)
        w.writerow(HEADER_ROW_2)
        for r in rows:
            w.writerow(r)

    print(f"Pinterest SEO CSV written: {csv_path}")
    print(f"Total pins:                {n}")
    print(f"Schedule:                  {dates[0]:%Y-%m-%d} -> {dates[-1]:%Y-%m-%d}")
    print(f"Post time:                 {POST_TIME} EST (Pinterest peak)")
    print(f"All links:                 {BASE_URL} (with UTM tracking)")
    print()

    # Print summary
    boards = {}
    for p in PINTEREST_DATA:
        b = p["board"]
        boards[b] = boards.get(b, 0) + 1
    print("Pinterest Board Distribution:")
    for board, count in boards.items():
        print(f"  {board}: {count} pins")

    print()
    print("Upload instructions:")
    print("  1. Open GHL > Marketing > Social Planner > Bulk Upload > Advanced")
    print(f"  2. Upload: {csv_path}")
    print("  3. Select ONLY Pinterest as the platform")
    print("  4. Confirm schedule and hit Publish")
    print()
    print("IMPORTANT: This is a SEPARATE CSV from the IG+Pinterest one.")
    print("Delete the Pinterest posts from the old CSV first, then upload this one.")


if __name__ == "__main__":
    main()
