"""
SkynetLabs Carousel Batch 5 — Captions + Hashtags + First Comments
30 carousels, each with:
  - caption        (main post body — hook, value, soft CTA)
  - hashtags       (10 targeted tags)
  - first_comment  (interactive engagement trigger, rotated across 6 styles)

First comment rotation (30 / 6 = 5 of each):
  POLL        — "which of these are you using?"
  CHALLENGE   — "pick one and do it this week"
  OPINION     — "controversial take... change my mind"
  FILL_BLANK  — "my X is ___ — what's yours?"
  TRADE       — "I'll trade X for your Y"
  RESOURCE    — "reply KEYWORD and I'll DM the template"
"""

# Shared hashtag pools by category so we get variety without losing relevance
TAGS_AI      = ["#AI","#ArtificialIntelligence","#AITools","#LLM","#ClaudeAI","#ChatGPT","#AIAgency","#AI2026","#TechTools","#FutureOfWork"]
TAGS_AUTO    = ["#n8n","#Automation","#NoCode","#AIAgents","#WorkflowAutomation","#AIAutomation","#BusinessAutomation","#SmallBiz","#TechStack","#AI"]
TAGS_AGENCY  = ["#AgencyLife","#AIAgency","#DigitalAgency","#Freelance","#Solopreneur","#ClientWork","#AgencyGrowth","#BusinessFrameworks","#Consulting","#Entrepreneurship"]
TAGS_DATA    = ["#AIResearch","#AITrends","#AI2026","#TechData","#MarketResearch","#FutureOfAI","#AIIndustry","#StartupData","#BusinessIntelligence","#DataDriven"]
TAGS_CASE    = ["#CaseStudy","#AIProjects","#AgencyWork","#ClientResults","#AIImplementation","#BusinessGrowth","#SmallBusiness","#DigitalTransformation","#Freelance","#Consulting"]
TAGS_MIND    = ["#MentalModels","#Founder","#Entrepreneurship","#DeepWork","#Mindset","#BusinessPhilosophy","#Solopreneur","#FounderLife","#ProductivityHacks","#SelfImprovement"]


CAPTIONS = [

# =============================================================
# CATEGORY A — NEON TERMINAL
# =============================================================

{
  "id": 1,
  "caption": (
    "Claude vs Cursor vs Windsurf — the honest 2026 comparison.\n\n"
    "I ran the same feature through all three.\n"
    "Same task. Same repo. Same prompt.\n\n"
    "The results weren't what I expected.\n\n"
    "Swipe to see who wins at what →\n\n"
    "TL;DR: stop picking one. Stack all three.\n"
    "Here's how I actually use them daily."
  ),
  "hashtags": TAGS_AI,
  "first_comment_style": "POLL",
  "first_comment": "Which one are you using most right now? Drop 1 for Claude, 2 for Cursor, 3 for Windsurf 👇",
},

{
  "id": 2,
  "caption": (
    "You don't need a $2K/month AI stack.\n\n"
    "You need to know where to look.\n\n"
    "Here are 15 free AI tools most agencies have no idea exist.\n"
    "Zero signup tricks. Zero BS.\n\n"
    "I use at least 8 of these every single day.\n\n"
    "Save this post — you'll come back to it."
  ),
  "hashtags": TAGS_AI,
  "first_comment_style": "RESOURCE",
  "first_comment": "Want the full 15 in one shareable Notion doc? Reply 'STACK' and I'll DM it to you.",
},

{
  "id": 3,
  "caption": (
    "Picking ONE AI model in 2026 is the mistake.\n\n"
    "Each top model has a superpower.\n"
    "Smart founders route tasks between them.\n\n"
    "Here's the routing table I use every day:\n"
    "• Writing → Claude\n"
    "• Research → Gemini\n"
    "• Brainstorm → ChatGPT\n"
    "• Code → Claude\n"
    "• Vision → Gemini\n\n"
    "Swipe for the full breakdown."
  ),
  "hashtags": TAGS_AI,
  "first_comment_style": "FILL_BLANK",
  "first_comment": "My most-used AI model for writing is ______. What's yours? 👇",
},

{
  "id": 4,
  "caption": (
    "The 2026 AI tool reality check.\n\n"
    "Winners, losers, and the overhyped stuff nobody wants to admit is underdelivering.\n\n"
    "I'm not here to please any founder.\n"
    "I'm here to save you money on bad tool choices.\n\n"
    "Some of these will surprise you.\n"
    "A few will make AI bros angry.\n\n"
    "Good."
  ),
  "hashtags": TAGS_AI,
  "first_comment_style": "OPINION",
  "first_comment": "Controversial take: slide 5 is wrong. Prove me otherwise in the replies 👇",
},

{
  "id": 5,
  "caption": (
    "The $0 AI Stack.\n\n"
    "Run your entire business on free AI tiers.\n"
    "Yes, really.\n\n"
    "I built this after watching too many founders burn $500/mo on tools they never opened.\n\n"
    "Free tier > paid plan you don't use.\n"
    "Stack 3 free tools = 1 paid tool.\n\n"
    "Save this. Audit your stack this weekend."
  ),
  "hashtags": TAGS_AI,
  "first_comment_style": "CHALLENGE",
  "first_comment": "Pick ONE paid tool from your stack and try replacing it with a free alternative this week. Reply 'DONE' when you do 👇",
},


# =============================================================
# CATEGORY B — CIRCUIT BOARD
# =============================================================

{
  "id": 6,
  "caption": (
    "10 n8n workflows that replace entire job roles.\n\n"
    "Not 'cool side-projects'.\n"
    "Actual workflows that replaced 5-figure annual salaries in my agency this year.\n\n"
    "• Lead Enricher\n"
    "• Content Recycler\n"
    "• Invoice Autopilot\n"
    "• Inbox Triage\n"
    "• Client Reporter\n\n"
    "+5 more inside. Swipe →"
  ),
  "hashtags": TAGS_AUTO,
  "first_comment_style": "RESOURCE",
  "first_comment": "Want my actual n8n templates for 3 of these? Reply 'N8N' and I'll send the JSON files.",
},

{
  "id": 7,
  "caption": (
    "The n8n beginner's visual cheat sheet.\n\n"
    "If you've been putting off learning n8n because 'it looks complicated'...\n"
    "Read this carousel once and you're past the learning curve.\n\n"
    "Nodes, triggers, variables, HTTP calls — all visualized.\n\n"
    "Save this. You'll never need another n8n tutorial."
  ),
  "hashtags": TAGS_AUTO,
  "first_comment_style": "POLL",
  "first_comment": "Where are you on your n8n journey? Drop a number: 1 = never heard of it | 2 = dabbled | 3 = active builder | 4 = making money with it 👇",
},

{
  "id": 8,
  "caption": (
    "Every business I audit has 7 hidden automation opportunities.\n\n"
    "They just don't see them — because the bottlenecks feel like 'the job'.\n\n"
    "Here's how to find the 7 in any business.\n"
    "Your own. A client's. Anyone's.\n\n"
    "This is the first thing I do on every discovery call."
  ),
  "hashtags": TAGS_AUTO,
  "first_comment_style": "FILL_BLANK",
  "first_comment": "The task I waste the most time on every week is ______. What's yours? 👇",
},

{
  "id": 9,
  "caption": (
    "How to audit any business for automation opportunities.\n\n"
    "I charge $2K for this audit.\n"
    "Here's the entire framework, free.\n\n"
    "4 steps. 90 minutes.\n"
    "You'll walk out with a list of 10+ automations every business has been paying humans to do manually.\n\n"
    "Use it on your own business first."
  ),
  "hashtags": TAGS_AUTO,
  "first_comment_style": "CHALLENGE",
  "first_comment": "Challenge: run this audit on YOUR business this weekend. Reply with the #1 opportunity you find 👇",
},

{
  "id": 10,
  "caption": (
    "20 AI agent prompts that actually work in production.\n\n"
    "Not 'cool demo' prompts.\n"
    "Not 'look what ChatGPT can do' prompts.\n\n"
    "These are the system prompts I'm using right now in live agents for real clients.\n\n"
    "Steal them. Adapt them. Ship them.\n\n"
    "Save this."
  ),
  "hashtags": TAGS_AUTO,
  "first_comment_style": "TRADE",
  "first_comment": "I'll trade one of my full production prompts for YOUR best one. Drop yours below — I'll DM mine.",
},


# =============================================================
# CATEGORY C — EXECUTIVE NAVY
# =============================================================

{
  "id": 11,
  "caption": (
    "The $10K/mo Agency Operating System.\n\n"
    "I lost 7 years + six figures figuring this out so you don't have to.\n\n"
    "It's not about more clients.\n"
    "It's not about more hours.\n"
    "It's about removing yourself from the bottleneck.\n\n"
    "This carousel is the whole operating system on one screen."
  ),
  "hashtags": TAGS_AGENCY,
  "first_comment_style": "OPINION",
  "first_comment": "Unpopular opinion: most agencies don't need more leads — they need better systems. Agree or disagree? 👇",
},

{
  "id": 12,
  "caption": (
    "10 pricing models for AI agencies (with real numbers).\n\n"
    "Stop guessing.\n"
    "Stop underpricing.\n"
    "Stop copying what the guru on TikTok told you to charge.\n\n"
    "Here are the 10 pricing models I've tested, with actual revenue numbers attached.\n\n"
    "One of these will double your rates. I promise."
  ),
  "hashtags": TAGS_AGENCY,
  "first_comment_style": "POLL",
  "first_comment": "Which pricing model are you on right now? Drop the number: 1=hourly, 2=project, 3=retainer, 4=value-based, 5=rev-share 👇",
},

{
  "id": 13,
  "caption": (
    "The 90-minute agency OS setup checklist.\n\n"
    "If you gave me 90 minutes and a fresh laptop, here's exactly how I'd set up a new agency from scratch.\n\n"
    "Tools. Systems. SOPs. Client onboarding.\n"
    "Everything.\n\n"
    "Save this and block out an afternoon this week."
  ),
  "hashtags": TAGS_AGENCY,
  "first_comment_style": "CHALLENGE",
  "first_comment": "Block 90 minutes this Sunday and run this setup on your agency. Reply 'DONE' when you finish 👇",
},

{
  "id": 14,
  "caption": (
    "The Solo Founder's Weekly Operating Rhythm.\n\n"
    "Stop reacting. Start directing.\n\n"
    "I used to work 70-hour weeks as a solo founder and still felt behind.\n"
    "This weekly rhythm fixed that in 3 weeks.\n\n"
    "Monday = strategy.\n"
    "Tue-Thu = execution.\n"
    "Fri = ops.\n"
    "Weekend = off. Actually off.\n\n"
    "The full breakdown is inside."
  ),
  "hashtags": TAGS_AGENCY,
  "first_comment_style": "FILL_BLANK",
  "first_comment": "The day of my week that always feels chaotic is ______. What's yours? 👇",
},

{
  "id": 15,
  "caption": (
    "10 copywriting frameworks — using AI.\n\n"
    "Not 'ChatGPT wrote this for me' slop.\n"
    "10 actual copywriting frameworks, each with a tested prompt you can steal.\n\n"
    "AIDA. PAS. BAB. 4Ps. And 6 more you've probably never heard of.\n\n"
    "Save this for your next landing page."
  ),
  "hashtags": TAGS_AGENCY,
  "first_comment_style": "TRADE",
  "first_comment": "I'll trade my #1 copywriting prompt for YOURS. Drop your favorite below and I'll reply with mine 👇",
},


# =============================================================
# CATEGORY D — DATA LAB
# =============================================================

{
  "id": 16,
  "caption": (
    "90% of AI agencies will die in 2026.\n\n"
    "Not a doom post. Data.\n\n"
    "I've been tracking AI agency launches + shutdowns since Q1 2024.\n"
    "The pattern is brutal and consistent.\n\n"
    "Here's why most will die — and what the 10% who survive are doing differently.\n\n"
    "If you run an agency, you need to see this."
  ),
  "hashtags": TAGS_DATA,
  "first_comment_style": "OPINION",
  "first_comment": "Hot take: the 90% aren't dying because of AI — they're dying because they never had a real business. Agree or fight me 👇",
},

{
  "id": 17,
  "caption": (
    "The truth about AI content performance.\n\n"
    "I audited 500+ AI-written posts vs. human-written posts across LinkedIn, IG, and blogs.\n\n"
    "The results will surprise the 'AI content is dead' crowd.\n"
    "And also the 'AI writes everything now' crowd.\n\n"
    "Nuance inside. Swipe for real metrics."
  ),
  "hashtags": TAGS_DATA,
  "first_comment_style": "POLL",
  "first_comment": "Be honest: how much of your content is AI-assisted? 1 = 0%, 2 = 25%, 3 = 50%, 4 = 75%, 5 = 100% 👇",
},

{
  "id": 18,
  "caption": (
    "AEO vs SEO — the rules changed in 2026.\n\n"
    "If you're still optimizing for Google's blue links, you're playing a dying game.\n\n"
    "AEO = Answer Engine Optimization.\n"
    "The new target: ChatGPT, Claude, Perplexity, Gemini — the engines people actually ask.\n\n"
    "Here's what changed, and what to do about it this quarter."
  ),
  "hashtags": TAGS_DATA,
  "first_comment_style": "RESOURCE",
  "first_comment": "Want my full AEO audit checklist? Reply 'AEO' and I'll DM it to you.",
},

{
  "id": 19,
  "caption": (
    "AI adoption by industry — what the data actually says.\n\n"
    "Forget the hype cycle.\n"
    "These are the real AI adoption numbers by industry, from Q1 2026.\n\n"
    "Some industries are way ahead.\n"
    "Some are decades behind.\n"
    "And one is ripe for a founder who moves now.\n\n"
    "Swipe to find your industry."
  ),
  "hashtags": TAGS_DATA,
  "first_comment_style": "FILL_BLANK",
  "first_comment": "The industry I work in is ______, and my honest AI-adoption grade for it is ______. What's yours? 👇",
},

{
  "id": 20,
  "caption": (
    "The honest cost of running an AI agency in 2026.\n\n"
    "Not 'I made $50K in 30 days' fluff.\n\n"
    "Real numbers.\n"
    "Real tools.\n"
    "Real margins.\n\n"
    "If you're thinking of starting an AI agency — read this BEFORE you register the LLC.\n\n"
    "Some of these line items nobody talks about."
  ),
  "hashtags": TAGS_DATA,
  "first_comment_style": "CHALLENGE",
  "first_comment": "Challenge: list every software bill your agency pays monthly. Reply with your total — let's see who has the leanest stack 👇",
},


# =============================================================
# CATEGORY E — CASE FILE
# =============================================================

{
  "id": 21,
  "caption": (
    "Anatomy of a $50K AI project.\n\n"
    "A real project. Real scope. Real invoice.\n\n"
    "Everything from discovery → proposal → build → delivery → retainer.\n\n"
    "I'm sharing this because 'AI agency' content online is 95% theater.\n"
    "You deserve to see what real work looks like.\n\n"
    "Names + industries anonymized. Numbers are real."
  ),
  "hashtags": TAGS_CASE,
  "first_comment_style": "RESOURCE",
  "first_comment": "Want my full proposal template (the one I used to close this one)? Reply 'PROPOSAL' and I'll DM it.",
},

{
  "id": 22,
  "caption": (
    "Before AI vs After AI — 10 real agency workflows.\n\n"
    "Side-by-side comparisons of exactly what changed when we added AI to existing workflows.\n\n"
    "Time saved.\n"
    "Errors reduced.\n"
    "Margins improved.\n\n"
    "Not 'AI will change everything' — actual receipts."
  ),
  "hashtags": TAGS_CASE,
  "first_comment_style": "POLL",
  "first_comment": "Which workflow in YOUR agency would you automate first? 1=lead gen 2=content 3=reporting 4=onboarding 5=admin 👇",
},

{
  "id": 23,
  "caption": (
    "How 3 workflows replaced a 5-person team.\n\n"
    "Yes — really.\n\n"
    "Not 'replaced jobs to save money' (we kept the team and promoted them).\n"
    "Replaced the MANUAL work so 5 people could do the work of 25.\n\n"
    "The 3 workflows, the stack, and the math — all inside."
  ),
  "hashtags": TAGS_CASE,
  "first_comment_style": "OPINION",
  "first_comment": "Controversial: AI should multiply your team, not replace it. Agree? 👇",
},

{
  "id": 24,
  "caption": (
    "10 lessons from building 100 websites.\n\n"
    "I'm not a designer. Never was.\n"
    "But I've shipped 100+ production websites for real clients.\n\n"
    "These 10 lessons are the ones I wish someone had given me on site #1.\n\n"
    "If you're building sites for clients — this will save you a year of pain."
  ),
  "hashtags": TAGS_CASE,
  "first_comment_style": "TRADE",
  "first_comment": "I'll trade my #1 lesson (slide 9) for YOUR hardest-earned one. Drop yours 👇",
},

{
  "id": 25,
  "caption": (
    "The $500 → $10K client transformation playbook.\n\n"
    "Your first real client probably paid $500.\n"
    "Here's how to turn that kind of client into $10K/month recurring revenue — without switching agencies.\n\n"
    "It's 3 moves.\n"
    "Most founders miss all three.\n\n"
    "Save this for your next renewal conversation."
  ),
  "hashtags": TAGS_CASE,
  "first_comment_style": "CHALLENGE",
  "first_comment": "Pick your smallest active client. Use the 3 moves on slide 4-6 this week. Reply 'DONE' when you pitch them 👇",
},


# =============================================================
# CATEGORY F — MINDSCAPE
# =============================================================

{
  "id": 26,
  "caption": (
    "10 mental models every AI founder should steal.\n\n"
    "AI moves too fast for tactics.\n"
    "You need thinking models that stay true when everything else changes.\n\n"
    "Here are 10 I reach for every single week — for pricing, hiring, shipping, positioning, and saying no.\n\n"
    "Save this. Revisit it every quarter."
  ),
  "hashtags": TAGS_MIND,
  "first_comment_style": "FILL_BLANK",
  "first_comment": "The one mental model I use most as a founder is ______. What's yours? 👇",
},

{
  "id": 27,
  "caption": (
    "The founder mental health playbook.\n\n"
    "No hustle BS. No 'grind harder'. No 5am cold plunge nonsense.\n\n"
    "Just the real playbook I wrote for myself after year 3 of running an agency — when the thing that almost broke me wasn't the work, it was the pressure.\n\n"
    "If you're a solo founder, please read this."
  ),
  "hashtags": TAGS_MIND,
  "first_comment_style": "OPINION",
  "first_comment": "Unpopular take: the 'hustle until you die' crowd is selling burnout as a lifestyle. Agree? 👇",
},

{
  "id": 28,
  "caption": (
    "7 books every AI agency owner should read.\n\n"
    "None of these are about AI.\n"
    "All of them will make you a better AI agency owner.\n\n"
    "Business. Pricing. Positioning. Mental models. Negotiation.\n\n"
    "The 7 books that changed how I run Skynet Labs — ranked."
  ),
  "hashtags": TAGS_MIND,
  "first_comment_style": "POLL",
  "first_comment": "How many of these 7 have you already read? Drop the number 0-7 👇",
},

{
  "id": 29,
  "caption": (
    "The art of saying no (with scripts).\n\n"
    "Every 'yes' to a bad client is a 'no' to the right one.\n\n"
    "Scope creep. Discounts. 'Quick favors'. Family friend projects.\n\n"
    "Here are the 7 scripts I use — verbatim — to say no without burning bridges.\n\n"
    "Save these. You'll need them this week."
  ),
  "hashtags": TAGS_MIND,
  "first_comment_style": "RESOURCE",
  "first_comment": "Want these 7 scripts in a one-page Notion doc you can copy-paste? Reply 'SCRIPTS' and I'll DM it.",
},

{
  "id": 30,
  "caption": (
    "The freelancer → agency transition roadmap.\n\n"
    "Most freelancers try to 'become an agency' by hiring people.\n"
    "That's how you go broke.\n\n"
    "The real transition is 4 stages. Each one has a specific revenue trigger.\n"
    "Skip a stage and you crash.\n\n"
    "Here's the roadmap I followed. Save it."
  ),
  "hashtags": TAGS_MIND,
  "first_comment_style": "TRADE",
  "first_comment": "I'll trade my biggest transition mistake for yours. Drop your freelancer→agency lesson below 👇",
},

]


def get(id_):
    for c in CAPTIONS:
        if c["id"] == id_:
            return c
    return None


if __name__ == "__main__":
    import sys
    print(f"Total caption entries: {len(CAPTIONS)}")
    styles = {}
    for c in CAPTIONS:
        styles[c["first_comment_style"]] = styles.get(c["first_comment_style"], 0) + 1
    print("First-comment style rotation:")
    for k, v in sorted(styles.items()):
        print(f"  {k:12s} {v}")
