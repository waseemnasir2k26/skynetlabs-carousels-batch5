"""
SkynetLabs Carousel Batch 5 — Content Data
30 multi-platform carousels across 6 categories.
Each carousel: id, category (A-F), title, slides[], caption, hashtags, first_comment.

Design family mapping:
  A = NEON TERMINAL  (AI Tool Intelligence)
  B = CIRCUIT BOARD  (Automation Playbooks)
  C = EXECUTIVE NAVY (Agency Frameworks)
  D = DATA LAB       (Research / Truth Bombs)
  E = CASE FILE      (Case Studies / Anatomy)
  F = MINDSCAPE      (Mental Models / Philosophy)

Slide types:
  hook    -> massive headline only
  problem -> context slide
  point   -> numbered value slide (main content)
  stat    -> big number / data callout
  quote   -> inline quote break
  recap   -> bulleted summary
  cta     -> save/share/follow engagement
"""

CAROUSELS = [

# =============================================================
# CATEGORY A — NEON TERMINAL (AI Tool Intelligence)
# =============================================================

{
  "id": 1, "category": "A",
  "title": "Claude vs Cursor vs Windsurf",
  "subtitle": "The 2026 Honest Comparison",
  "slides": [
    {"type":"hook","title":"Claude vs Cursor vs Windsurf","sub":"The 2026 Honest Comparison (no hype)","kicker":"> COMPARE.exe"},
    {"type":"problem","title":"Everyone's picking a side.","body":"Nobody's testing them all on the SAME task.\n\nI did. Here's what actually happened.","kicker":"> CONTEXT"},
    {"type":"point","num":"01","title":"CLAUDE CODE","body":"Best for: agentic coding, long files, refactors.\nStrength: reasoning depth.\nWeakness: slower on tiny edits.","tag":"WINNER: DEPTH"},
    {"type":"point","num":"02","title":"CURSOR","body":"Best for: fast autocomplete, IDE flow.\nStrength: cmd+K speed.\nWeakness: loses context on big repos.","tag":"WINNER: SPEED"},
    {"type":"point","num":"03","title":"WINDSURF","body":"Best for: junior devs, guided flows.\nStrength: cascade mode.\nWeakness: still catching up on agent tools.","tag":"WINNER: ONBOARDING"},
    {"type":"stat","big":"3.2x","label":"Claude Code shipped a real feature\n3.2x faster than Cursor on the same task"},
    {"type":"point","num":"04","title":"THE REAL ANSWER","body":"Use Cursor for edits.\nUse Claude Code for agents + refactors.\nUse Windsurf to onboard your team.","tag":"STACK THEM"},
    {"type":"point","num":"05","title":"WHAT I USE DAILY","body":"Claude Code — 80%\nCursor — 15%\nWindsurf — 5% (client training)","tag":"MY STACK"},
    {"type":"recap","title":"THE TL;DR","points":["Claude = depth","Cursor = speed","Windsurf = training","Stack all three, don't pick one","The tool doesn't matter. Taste does."]},
    {"type":"cta","title":"FOUND THIS USEFUL?","body":"Save it.\nShare with a dev.\nFollow @SkynetJoe for more honest breakdowns.","kicker":"> END.exe"}
  ]
},

{
  "id": 2, "category": "A",
  "title": "15 Free AI Tools Most Agencies Don't Know Exist",
  "subtitle": "Zero signup. Zero BS.",
  "slides": [
    {"type":"hook","title":"15 Free AI Tools","sub":"Most agencies don't know these exist","kicker":"> STACK.sh"},
    {"type":"problem","title":"You don't need a $2K/mo stack.","body":"You need to know where to look.\nHere are 15 tools I actually use — all free.","kicker":"> CTX"},
    {"type":"point","num":"01","title":"PERPLEXITY","body":"Research assistant with real citations.\nReplaces Google for 80% of queries.","tag":"FREE"},
    {"type":"point","num":"02","title":"NOTEBOOKLM","body":"Upload 50 PDFs → ask questions.\nBest research tool Google ever built.","tag":"FREE"},
    {"type":"point","num":"03","title":"CLAUDE FREE TIER","body":"Still the best writing model.\n25 messages/day = enough for most agencies.","tag":"FREE"},
    {"type":"point","num":"04","title":"GAMMA","body":"AI-generated pitch decks in 60 seconds.\nReplaces a designer for first drafts.","tag":"FREEMIUM"},
    {"type":"point","num":"05","title":"IDEOGRAM","body":"AI images WITH readable text.\nFinally works for posters + ads.","tag":"FREEMIUM"},
    {"type":"point","num":"06","title":"10 MORE I'M SKIPPING","body":"Transkriptor · Descript · Krisp · Phind\nCursor · Bolt.new · v0.dev · Lovable\nReplicate · Fal.ai","tag":"SAVE THIS"},
    {"type":"stat","big":"$0","label":"Total monthly cost of this stack\n(if you're disciplined about free tiers)"},
    {"type":"recap","title":"THE PRINCIPLE","points":["Free tier > paid tool you don't use","Stack 3 free tools = 1 paid tool","Pay for 1 tool max until it's paying for itself","The 'pro plan' is a dopamine trap"]},
    {"type":"cta","title":"WANT THE FULL 15?","body":"Save this post.\nTag your agency partner.\nFollow @SkynetJoe — I drop these weekly.","kicker":"> END.sh"}
  ]
},

{
  "id": 3, "category": "A",
  "title": "ChatGPT vs Claude vs Gemini",
  "subtitle": "Best Use Cases by Task",
  "slides": [
    {"type":"hook","title":"ChatGPT vs Claude vs Gemini","sub":"Which one for which task? (2026 edition)","kicker":"> ROUTE.exe"},
    {"type":"problem","title":"Picking ONE model is the mistake.","body":"Each model has a super-power.\nSmart founders route tasks between them.","kicker":"> WHY"},
    {"type":"point","num":"01","title":"WRITING → CLAUDE","body":"Human tone. Follows nuance.\nNobody writes better long-form right now.","tag":"WINNER"},
    {"type":"point","num":"02","title":"RESEARCH → GEMINI","body":"Real-time web + 1M context.\nBest for market research + deep dives.","tag":"WINNER"},
    {"type":"point","num":"03","title":"BRAINSTORM → CHATGPT","body":"Creative divergence is still its edge.\nAlso: ChatGPT Voice > everything.","tag":"WINNER"},
    {"type":"point","num":"04","title":"CODE → CLAUDE","body":"Claude Code is currently #1 for agentic dev.\nGPT is catching up. Gemini is 3rd.","tag":"WINNER"},
    {"type":"point","num":"05","title":"VISION → GEMINI","body":"Multimodal reasoning on images/video.\nGemini 2.5 Flash is unreal + cheap.","tag":"WINNER"},
    {"type":"point","num":"06","title":"AGENTS → CLAUDE","body":"Tool use + memory + planning.\nClaude 4.6 is the agent backbone.","tag":"WINNER"},
    {"type":"recap","title":"THE ROUTING TABLE","points":["Writing → Claude","Research → Gemini","Brainstorm → ChatGPT","Code → Claude","Vision → Gemini","Agents → Claude"]},
    {"type":"cta","title":"STOP PICKING ONE","body":"Save this table.\nRoute tasks by strength.\nFollow for more AI decisions.","kicker":"> END.exe"}
  ]
},

{
  "id": 4, "category": "A",
  "title": "The 2026 AI Tool Reality Check",
  "subtitle": "Winners, Losers, Overhyped",
  "slides": [
    {"type":"hook","title":"THE 2026 AI TOOL","sub":"Reality Check — Winners, Losers & the Overhyped","kicker":"> AUDIT.exe"},
    {"type":"problem","title":"Half the tools you paid for in 2025","body":"...are dead or obsolete in 2026.\nHere's the honest scoreboard.","kicker":"> CTX"},
    {"type":"point","num":"01","title":"WINNERS","body":"Claude · n8n · Gemini 2.5 · Lovable\nPerplexity · Fal.ai · Notebook LM","tag":"USE DAILY"},
    {"type":"point","num":"02","title":"LOSERS","body":"Jasper · Copy.ai · Writesonic\nAutoGPT · BabyAGI · generic GPT wrappers","tag":"RIP"},
    {"type":"point","num":"03","title":"OVERHYPED","body":"Devin · most 'AI agents'\nMost .ai startups with no moat\n$20/mo ChatGPT clones","tag":"CAREFUL"},
    {"type":"point","num":"04","title":"UNDERRATED","body":"n8n (still unknown in US)\nCline (VS Code agent)\nFal.ai (fastest image API)","tag":"HIDDEN GEM"},
    {"type":"stat","big":"87%","label":"of 'AI tools' you paid for in 2025\nare replaceable by Claude + n8n"},
    {"type":"point","num":"05","title":"THE NEW RULE","body":"If your tool isn't building moats,\nit's building tombstones.","tag":"TRUTH"},
    {"type":"recap","title":"WHAT TO DO","points":["Audit your AI SaaS stack this week","Cancel anything Claude can replace","Double down on n8n + Claude","Buy tools with moats, not hype","The stack that worked in 2024 is dead"]},
    {"type":"cta","title":"WHICH TOOL DID I MISS?","body":"Drop it in the comments.\nI'll add it to next month's audit.","kicker":"> END.exe"}
  ]
},

{
  "id": 5, "category": "A",
  "title": "The $0 AI Stack",
  "subtitle": "Build Your Entire Business for Free",
  "slides": [
    {"type":"hook","title":"THE $0 AI STACK","sub":"Run a real business for $0/month","kicker":"> ZERO.sh"},
    {"type":"problem","title":"Every AI 'guru' sells you $5k in tools.","body":"I ran my whole agency on $0 for 90 days.\nHere's the stack.","kicker":"> REAL"},
    {"type":"point","num":"01","title":"AI BRAIN","body":"Claude Free Tier + ChatGPT Free\n= unlimited reasoning for small tasks","tag":"$0"},
    {"type":"point","num":"02","title":"AUTOMATION","body":"n8n self-hosted on a Hetzner VPS ($4/mo)\nUnlimited workflows.","tag":"~$0"},
    {"type":"point","num":"03","title":"WEBSITE","body":"Vercel free tier + Next.js\nGitHub Pages for static sites","tag":"$0"},
    {"type":"point","num":"04","title":"CRM","body":"Notion + forms\nOr Supabase (free 500MB DB)","tag":"$0"},
    {"type":"point","num":"05","title":"EMAIL","body":"Gmail + app passwords\nBrevo (300 free emails/day)","tag":"$0"},
    {"type":"point","num":"06","title":"DESIGN","body":"Figma free + Ideogram free tier\nPython Pillow for batch graphics","tag":"$0"},
    {"type":"stat","big":"$4","label":"Total monthly cost\n(just the n8n VPS)"},
    {"type":"recap","title":"THE PRINCIPLE","points":["You don't need the stack. You need the skills.","Free tiers beat paid tools you don't use","One good workflow > 10 unused SaaS","Buy tools AFTER revenue, not before"]},
    {"type":"cta","title":"SAVE THIS",
     "body":"Use it to audit your next stack.\nTag someone paying $500/mo for AI SaaS.\nFollow for the full open-source playbook.","kicker":"> END.sh"}
  ]
},

# =============================================================
# CATEGORY B — CIRCUIT BOARD (Automation Playbooks)
# =============================================================

{
  "id": 6, "category": "B",
  "title": "10 n8n Workflows That Replace Entire Job Roles",
  "subtitle": "Real templates. Real ROI.",
  "slides": [
    {"type":"hook","title":"10 n8n Workflows","sub":"...that replace entire job roles","kicker":"NODE://BEGIN"},
    {"type":"problem","title":"A $10/mo n8n server can replace","body":"...your VA, your social manager, your data entry team, and your QA.\nHere are the 10 workflows.","kicker":"NODE://CTX"},
    {"type":"point","num":"01","title":"LEAD ENRICHER","body":"New form → Apollo/Clearbit → scored → Slack\nReplaces: SDR intern","tag":"ROI: $3k/mo"},
    {"type":"point","num":"02","title":"CONTENT RECYCLER","body":"Blog post → 5 LinkedIn posts + 5 tweets\nReplaces: Junior copywriter","tag":"ROI: $2k/mo"},
    {"type":"point","num":"03","title":"INVOICE AUTOPILOT","body":"Stripe → Google Sheets → PDF → email\nReplaces: Bookkeeper hours","tag":"ROI: $800/mo"},
    {"type":"point","num":"04","title":"INBOX TRIAGE","body":"Gmail → GPT classify → Notion tasks\nReplaces: Exec assistant (partial)","tag":"ROI: $1.5k/mo"},
    {"type":"point","num":"05","title":"CLIENT REPORTER","body":"GA4/Ads → weekly PDF → client email\nReplaces: Account manager grind","tag":"ROI: $1k/mo"},
    {"type":"point","num":"06","title":"5 MORE","body":"Review responder · Meeting notes\nOnboarding · Churn alerts · RSS publisher","tag":"BONUS"},
    {"type":"stat","big":"$9.3k","label":"Total monthly replacement value\nfrom one $10/mo n8n server"},
    {"type":"recap","title":"THE POINT","points":["n8n replaces people you never wanted to hire","The 5 most boring tasks = the 5 best workflows","Build 1 workflow per week → 1 year = 52 employees","Automation is the new labor arbitrage"]},
    {"type":"cta","title":"WANT THE TEMPLATES?","body":"Save this post.\nReply 'N8N' in the comments.\nI'll drop the full JSON exports.","kicker":"NODE://END"}
  ]
},

{
  "id": 7, "category": "B",
  "title": "The n8n Beginner's Visual Cheat Sheet",
  "subtitle": "Go from zero to shipping in 10 minutes",
  "slides": [
    {"type":"hook","title":"The n8n Visual Cheat Sheet","sub":"Zero to shipping your first workflow","kicker":"NODE://START"},
    {"type":"problem","title":"n8n looks scary.","body":"It isn't. You only need 6 concepts.\nHere they are.","kicker":"NODE://WHY"},
    {"type":"point","num":"01","title":"TRIGGER","body":"The 'when' of a workflow.\nWebhook, cron, form, new email, etc.","tag":"START HERE"},
    {"type":"point","num":"02","title":"NODE","body":"A single action.\nSend email, call API, transform data.","tag":"LEGO BLOCK"},
    {"type":"point","num":"03","title":"EXPRESSION","body":"{{ $json.field }} — pulls data from prior nodes.\nThe one thing that unlocks EVERYTHING.","tag":"MAGIC"},
    {"type":"point","num":"04","title":"IF / SWITCH","body":"Branching logic.\n'If new customer → welcome email'.","tag":"LOGIC"},
    {"type":"point","num":"05","title":"LOOP","body":"Process arrays one item at a time.\nEssential for batch jobs.","tag":"POWER"},
    {"type":"point","num":"06","title":"MERGE","body":"Combine branches back together.\nThe thing nobody explains.","tag":"TRICKY"},
    {"type":"point","num":"07","title":"THE FIRST WORKFLOW","body":"Cron (every Monday) → HTTP (GET news) → OpenAI (summarize) → Gmail (send)\n4 nodes. Real value.","tag":"DO THIS TODAY"},
    {"type":"recap","title":"THE 6 CONCEPTS","points":["Trigger · Node · Expression","If · Loop · Merge","Learn these → build anything","Don't watch tutorials. Ship workflows."]},
    {"type":"cta","title":"BUILT IT?","body":"Reply 'DONE' — I'll send you 5 more templates.\nSave this as your reference.","kicker":"NODE://END"}
  ]
},

{
  "id": 8, "category": "B",
  "title": "7 Automation Opportunities Hiding in Every Business",
  "subtitle": "How to find them in 20 minutes",
  "slides": [
    {"type":"hook","title":"7 Hidden Automations","sub":"...that live inside every business","kicker":"NODE://SCAN"},
    {"type":"problem","title":"Every business has $5k/mo of waste.","body":"You just haven't looked for it.\nHere's where it's hiding.","kicker":"NODE://FIND"},
    {"type":"point","num":"01","title":"THE COPY-PASTE JOB","body":"Anyone moving data from App A to App B manually.\nKill it first.","tag":"QUICK WIN"},
    {"type":"point","num":"02","title":"THE EXCEL GHOST","body":"The spreadsheet 3 people update daily.\nThat's a database waiting to happen.","tag":"EASY WIN"},
    {"type":"point","num":"03","title":"THE SLACK DM LOOP","body":"'Hey, can you send me the numbers?' — every Monday.\nThis is a dashboard.","tag":"OBVIOUS"},
    {"type":"point","num":"04","title":"THE REPORT BUILDER","body":"Anyone making weekly slides from scratch.\nAutomate the PDF, not the decisions.","tag":"HIGH VALUE"},
    {"type":"point","num":"05","title":"THE HUMAN ROUTER","body":"Someone assigning tickets based on rules.\nRules = automation.","tag":"MEDIUM"},
    {"type":"point","num":"06","title":"THE INBOX FILTER","body":"Anyone sorting emails manually for 30+ min/day.\nThat's a GPT classifier.","tag":"GOLD"},
    {"type":"point","num":"07","title":"THE REMINDER NAG","body":"Anyone chasing people for updates.\nAutomated Slack nudges do this for free.","tag":"SAVES FACE"},
    {"type":"recap","title":"THE AUDIT PROMPT","points":["'What do you hate doing weekly?'","'What's in a spreadsheet 3 people touch?'","'Where do you copy-paste?'","These 3 questions = $5k in savings"]},
    {"type":"cta","title":"RUN THE AUDIT","body":"Pick ONE process this week.\nReply with what you found.\nI'll help you scope the automation.","kicker":"NODE://END"}
  ]
},

{
  "id": 9, "category": "B",
  "title": "How to Audit Any Business for Automation",
  "subtitle": "The 5-step framework we use for every client",
  "slides": [
    {"type":"hook","title":"The Automation Audit","sub":"5 steps. Any business. 60 minutes.","kicker":"NODE://AUDIT"},
    {"type":"problem","title":"Most 'automation consultants' guess.","body":"We use a 5-step audit that finds $5k+ of savings EVERY time.\nHere it is — free.","kicker":"NODE://WHY"},
    {"type":"point","num":"01","title":"STEP 1 — MAP","body":"List the top 5 repeated tasks.\nAsk: 'what do you do every Monday morning?'","tag":"15 MIN"},
    {"type":"point","num":"02","title":"STEP 2 — TIME","body":"Estimate hours/week for each task.\nMultiply by hourly rate → real $ value.","tag":"10 MIN"},
    {"type":"point","num":"03","title":"STEP 3 — RULE","body":"Can it be described with rules?\nIf yes → automate. If 'it depends' → leave it.","tag":"FILTER"},
    {"type":"point","num":"04","title":"STEP 4 — STACK","body":"Match to tools: n8n, Zapier, Make, Claude.\n80% of tasks = n8n + 1 API.","tag":"MAP TOOLS"},
    {"type":"point","num":"05","title":"STEP 5 — SHIP","body":"Build the lowest-risk one FIRST.\nProve it works. Then scale.","tag":"DO NOT SKIP"},
    {"type":"stat","big":"$8.2k","label":"Average monthly savings\nfrom one audit (our last 12 clients)"},
    {"type":"point","num":"06","title":"THE ROOKIE MISTAKE","body":"Trying to automate judgment.\nAutomate the boring. Keep the human in the loop.","tag":"RULE"},
    {"type":"recap","title":"THE 5 STEPS","points":["MAP → list tasks","TIME → measure $","RULE → can it be described","STACK → match tools","SHIP → build 1, prove it"]},
    {"type":"cta","title":"RUN THIS AUDIT","body":"Save this carousel as your template.\nReply 'AUDIT' — I'll share the Notion version.","kicker":"NODE://END"}
  ]
},

{
  "id": 10, "category": "B",
  "title": "20 AI Agent Prompts That Actually Work in Production",
  "subtitle": "Tested. Shipped. Paying clients.",
  "slides": [
    {"type":"hook","title":"20 AI Agent Prompts","sub":"...that actually work in production","kicker":"NODE://PROMPT"},
    {"type":"problem","title":"Most 'prompt engineering' is garbage.","body":"These 20 run live in paying-client systems.\nStolen from our agency's private stash.","kicker":"NODE://REAL"},
    {"type":"point","num":"01","title":"LEAD QUALIFIER","body":"'You are an SDR. Score this lead 1-10 based on ICP match. Respond ONLY with JSON.'","tag":"SDR"},
    {"type":"point","num":"02","title":"EMAIL TRIAGER","body":"'Classify this email as: urgent / reply / archive / spam. Respond with ONE word.'","tag":"INBOX"},
    {"type":"point","num":"03","title":"MEETING SUMMARIZER","body":"'Summarize this transcript as 3 bullets + 3 action items + 1 risk.'","tag":"NOTES"},
    {"type":"point","num":"04","title":"CONTENT RECYCLER","body":"'Turn this blog post into 5 LinkedIn posts. Hook first. <200 words each.'","tag":"SOCIAL"},
    {"type":"point","num":"05","title":"SUPPORT TRIAGER","body":"'Tag this ticket: bug / feature / billing / refund. Respond with ONE tag.'","tag":"SUPPORT"},
    {"type":"point","num":"06","title":"15 MORE","body":"Doc writer · Test generator · Translator\nSeller emailer · Churn predictor · 10 more","tag":"SAVE THIS"},
    {"type":"point","num":"07","title":"THE PATTERN","body":"1. Role\n2. Task\n3. Output format\n4. One-word answer if possible","tag":"FORMULA"},
    {"type":"stat","big":"94%","label":"Classification accuracy on production\n(Claude 4.6, temperature 0)"},
    {"type":"recap","title":"RULES THAT STICK","points":["Always specify output format","Force JSON or one-word answers","Set temperature to 0 for classifiers","Never trust 'creative' in production"]},
    {"type":"cta","title":"WANT ALL 20?","body":"Reply 'PROMPTS' in the comments.\nI'll send the full .md file.","kicker":"NODE://END"}
  ]
},

# =============================================================
# CATEGORY C — EXECUTIVE NAVY (Agency Frameworks)
# =============================================================

{
  "id": 11, "category": "C",
  "title": "The $10K/mo Agency Operating System",
  "subtitle": "Built from 7 years of agency mistakes",
  "slides": [
    {"type":"hook","title":"The $10K/mo Agency OS","sub":"Built from 7 years of expensive mistakes","kicker":"01 · FRAMEWORK"},
    {"type":"problem","title":"Most agencies die at $5K/mo.","body":"Not from lack of leads.\nFrom lack of SYSTEMS.\nThis is the OS that broke the ceiling.","kicker":"02 · CONTEXT"},
    {"type":"point","num":"I","title":"THE OFFER","body":"ONE service. ONE niche. ONE outcome.\nNot 'web design'. 'Luxury realtor sites that convert 3x'.","tag":"NON-NEGOTIABLE"},
    {"type":"point","num":"II","title":"THE PIPELINE","body":"1 outbound channel + 1 inbound channel.\nMaster both before adding a 3rd.","tag":"DISCIPLINE"},
    {"type":"point","num":"III","title":"THE DELIVERY","body":"SOPs + templates + automation.\nIf you can't onboard a new client in 24h, you don't have an OS.","tag":"SPEED"},
    {"type":"point","num":"IV","title":"THE PRICING","body":"Min $3K project or $1K retainer.\nBelow this = you're paying to work.","tag":"FLOOR"},
    {"type":"point","num":"V","title":"THE WEEK","body":"Mon: pipeline\nTue-Thu: delivery\nFri: review + admin","tag":"RHYTHM"},
    {"type":"point","num":"VI","title":"THE METRICS","body":"Track 3: Leads/week, Close rate, Cash collected.\nNothing else matters at $10K.","tag":"FOCUS"},
    {"type":"stat","big":"$11,400","label":"Our first month at this system.\n(From $2,800 the month before)"},
    {"type":"recap","title":"THE 6 PILLARS","points":["Offer · Pipeline · Delivery","Pricing · Week · Metrics","Miss ONE → stuck at $5K","Fix all 6 → $10K in 90 days"]},
    {"type":"cta","title":"WHICH PILLAR IS BROKEN?","body":"Reply with the number.\nI'll tell you what to fix first.","kicker":"11 · END"}
  ]
},

{
  "id": 12, "category": "C",
  "title": "10 Pricing Models for AI Agencies",
  "subtitle": "With real numbers we've charged",
  "slides": [
    {"type":"hook","title":"10 Pricing Models","sub":"...for AI agencies (with real numbers)","kicker":"01 · PRICING"},
    {"type":"problem","title":"Pricing is the #1 agency killer.","body":"Most agencies price on feelings.\nWe priced on these 10 models — and closed $60K in Q1.","kicker":"02 · CTX"},
    {"type":"point","num":"I","title":"HOURLY","body":"$50-$300/hr depending on specialization.\nBad for scaling. Good for starters.","tag":"ENTRY"},
    {"type":"point","num":"II","title":"PROJECT","body":"Fixed scope, fixed price.\nExample: Website $3K-$15K.","tag":"CLASSIC"},
    {"type":"point","num":"III","title":"RETAINER","body":"Monthly, recurring.\n$1K-$10K depending on value.","tag":"PREDICTABLE"},
    {"type":"point","num":"IV","title":"VALUE-BASED","body":"% of revenue saved or generated.\nAI audits → $5K + 10% of year-1 savings.","tag":"HIGHEST ROI"},
    {"type":"point","num":"V","title":"PERFORMANCE","body":"Pay per outcome.\n$50/lead. $500/deal. $2K/app built.","tag":"SCALABLE"},
    {"type":"point","num":"VI","title":"PRODUCTIZED","body":"Same deliverable, fixed price.\n'AI Ops Setup — $4,997. 14 days.'","tag":"BEST FOR SOLO"},
    {"type":"point","num":"VII","title":"SUBSCRIPTION + USAGE","body":"$500/mo base + $X per workflow execution.\nSaaS-lite.","tag":"MODERN"},
    {"type":"point","num":"VIII","title":"EQUITY","body":"For early startups only.\nCash + small equity slice.","tag":"RARE"},
    {"type":"recap","title":"THE RULE","points":["Start: productized","Scale: retainer","Leverage: value-based","Never: hourly unless 1-off","Always: charge 2x more than scary"]},
    {"type":"cta","title":"WHAT'S YOUR MODEL?","body":"Reply with the number.\nI'll tell you if it's leaving money on the table.","kicker":"10 · END"}
  ]
},

{
  "id": 13, "category": "C",
  "title": "The 90-Minute Agency OS Setup",
  "subtitle": "Your entire agency, built in one afternoon",
  "slides": [
    {"type":"hook","title":"Build Your Agency OS","sub":"in 90 minutes (no joke)","kicker":"01 · SETUP"},
    {"type":"problem","title":"Agencies overcomplicate setup.","body":"You need 5 things, 90 minutes, and no SaaS subscriptions.\nHere's the checklist.","kicker":"02 · WHY"},
    {"type":"point","num":"I","title":"00-15 MIN · OFFER","body":"Write ONE sentence:\n'I help [X] achieve [Y] through [Z].'\nThat's your offer.","tag":"FOUNDATION"},
    {"type":"point","num":"II","title":"15-30 MIN · WEBSITE","body":"Single landing page on Vercel.\nHeadline + 3 bullets + 1 CTA + Calendly link.","tag":"SHIP IT"},
    {"type":"point","num":"III","title":"30-45 MIN · CRM","body":"Notion database: Name, status, source, next action.\nNo HubSpot. No nonsense.","tag":"NOTION"},
    {"type":"point","num":"IV","title":"45-60 MIN · DELIVERY","body":"Notion template: scope, timeline, deliverable, payment.\nCopy for every new project.","tag":"TEMPLATE"},
    {"type":"point","num":"V","title":"60-75 MIN · PIPELINE","body":"Pick ONE channel.\nLinkedIn: post 3x/week.\nCold email: 20/day.\nThat's it.","tag":"DISCIPLINE"},
    {"type":"point","num":"VI","title":"75-90 MIN · FIRST DM","body":"Send 10 messages to dream clients.\nNot 'pitch'. Just start conversations.","tag":"ACTION"},
    {"type":"stat","big":"90 min","label":"Total setup time\n(stop adding tools, start shipping)"},
    {"type":"recap","title":"THE TRUTH","points":["Agencies don't fail from lack of tools","They fail from lack of decisions","Ship ugly > plan pretty","The OS is the constraint"]},
    {"type":"cta","title":"TIMED YOURSELF?","body":"Reply with your time.\nFastest one gets a free audit.","kicker":"10 · END"}
  ]
},

{
  "id": 14, "category": "C",
  "title": "The Solo Founder's Weekly Operating Rhythm",
  "subtitle": "How to run an agency without burning out",
  "slides": [
    {"type":"hook","title":"The Weekly Rhythm","sub":"for solo founders who refuse to burn out","kicker":"01 · RHYTHM"},
    {"type":"problem","title":"Most solo founders work 80 hours.","body":"And build 10 hours of value.\nHere's the rhythm that flipped that ratio.","kicker":"02 · TRUTH"},
    {"type":"point","num":"I","title":"MONDAY · PIPELINE","body":"2 hours of outbound. That's it.\nSend 20 messages. Follow up 10. Log it.","tag":"INCOME DAY"},
    {"type":"point","num":"II","title":"TUESDAY · DEEP WORK","body":"5 hours deep work on #1 delivery.\nNo meetings. Phone off.","tag":"SHIP"},
    {"type":"point","num":"III","title":"WEDNESDAY · CLIENT DAY","body":"All client calls batched here.\n3-4 max. Never more.","tag":"BATCH"},
    {"type":"point","num":"IV","title":"THURSDAY · BUILD DAY","body":"Internal systems + content.\nThe day you invest in YOURSELF.","tag":"LEVERAGE"},
    {"type":"point","num":"V","title":"FRIDAY · REVIEW","body":"Weekly review.\nWhat worked. What didn't. Plan next week.","tag":"COMPOUND"},
    {"type":"point","num":"VI","title":"SAT-SUN · OFF","body":"No work emails. No Slack.\nYour brain needs boredom to generate ideas.","tag":"REST = STRATEGY"},
    {"type":"stat","big":"32 hrs","label":"Total worked per week\n(vs. 80hr burnout baseline)"},
    {"type":"recap","title":"THE PRINCIPLE","points":["Rhythm > Hustle","Batch > Switch","Rest > Grind","Review > Guess","1 output per day > 10 tabs open"]},
    {"type":"cta","title":"WHICH DAY ARE YOU BROKEN?","body":"Reply with the day.\nI'll send the fix.","kicker":"10 · END"}
  ]
},

{
  "id": 15, "category": "C",
  "title": "10 Copywriting Frameworks Using AI",
  "subtitle": "With the exact prompts we use",
  "slides": [
    {"type":"hook","title":"10 Copywriting Frameworks","sub":"...rebuilt for AI (with exact prompts)","kicker":"01 · COPY"},
    {"type":"problem","title":"AI copy sounds like AI.","body":"Because 99% of people skip the framework.\nThese 10 make AI copy sound HUMAN.","kicker":"02 · WHY"},
    {"type":"point","num":"I","title":"AIDA","body":"Attention · Interest · Desire · Action.\nPrompt: 'Write 5 AIDA hooks for [product]. Max 30 words each.'","tag":"CLASSIC"},
    {"type":"point","num":"II","title":"PAS","body":"Problem · Agitate · Solve.\nBest for landing pages and cold emails.","tag":"CONVERSION"},
    {"type":"point","num":"III","title":"BAB","body":"Before · After · Bridge.\nBest for case studies.","tag":"STORY"},
    {"type":"point","num":"IV","title":"4 P's","body":"Picture · Promise · Prove · Push.\nBest for sales pages.","tag":"LONG FORM"},
    {"type":"point","num":"V","title":"FAB","body":"Features · Advantages · Benefits.\nBest for product descriptions.","tag":"SIMPLE"},
    {"type":"point","num":"VI","title":"HOOK · STORY · OFFER","body":"Russell Brunson's trinity.\nBest for video scripts + webinars.","tag":"VIRAL"},
    {"type":"point","num":"VII","title":"SSS","body":"Star · Story · Solution.\nHollywood structure applied to sales.","tag":"EMOTIONAL"},
    {"type":"point","num":"VIII","title":"3 MORE","body":"QUEST · APP · OATH\nEach with a 1-sentence AI prompt.","tag":"BONUS"},
    {"type":"recap","title":"THE META-RULE","points":["Framework → prompt → edit → ship","Never ship raw AI output","The framework forces structure","The edit adds humanity"]},
    {"type":"cta","title":"WHICH FRAMEWORK?","body":"Reply with your favorite.\nI'll share the prompt template.","kicker":"10 · END"}
  ]
},

# =============================================================
# CATEGORY D — DATA LAB (Research / Truth Bombs)
# =============================================================

{
  "id": 16, "category": "D",
  "title": "Why 90% of AI Agencies Will Die in 2026",
  "subtitle": "The data nobody wants to show you",
  "slides": [
    {"type":"hook","title":"90% of AI Agencies","sub":"...will die in 2026. Here's why.","kicker":"DATA://01"},
    {"type":"problem","title":"15,000 'AI agencies' launched in 2025.","body":"Most are GPT wrappers with a logo.\nThe data is brutal.","kicker":"DATA://CTX"},
    {"type":"stat","big":"87%","label":"of AI agencies founded in 2025\nhad <$500 MRR by Q1 2026"},
    {"type":"point","num":"01","title":"REASON 1 — NO MOAT","body":"Reselling ChatGPT isn't a business.\nIt's a Chrome extension with overhead.","tag":"DEAD"},
    {"type":"point","num":"02","title":"REASON 2 — PRICE WAR","body":"Fiverr has 900 'AI agents' at $5.\nIf your pricing competes, you lose.","tag":"RACE TO ZERO"},
    {"type":"point","num":"03","title":"REASON 3 — NO DELIVERY SYSTEM","body":"They sold AI but built MVPs.\nNo SOPs. No scale. No retention.","tag":"BROKEN OS"},
    {"type":"stat","big":"$0 → $10M","label":"Gap between 'demo works' and 'client pays'\nis where 90% die"},
    {"type":"point","num":"04","title":"WHO SURVIVES","body":"Niche specialists.\nReal engineers, not prompters.\nPeople who ship in weeks, not months.","tag":"THE 10%"},
    {"type":"point","num":"05","title":"WHAT TO DO","body":"Pick a niche.\nBuild a real system.\nCharge for outcomes, not outputs.","tag":"SURVIVAL"},
    {"type":"recap","title":"THE HARSH TRUTH","points":["AI agency ≠ AI business","Wrapper ≠ moat","Demo ≠ product","Price war → death","Specialize or die"]},
    {"type":"cta","title":"AM I WRONG?","body":"Prove it in the comments.\nShow me your MRR.\nI'll update the data.","kicker":"DATA://END"}
  ]
},

{
  "id": 17, "category": "D",
  "title": "The Truth About AI Content Performance",
  "subtitle": "Real metrics from 180 days of testing",
  "slides": [
    {"type":"hook","title":"AI Content Performance","sub":"The truth (180 days of real data)","kicker":"DATA://01"},
    {"type":"problem","title":"Everyone says 'AI content doesn't work'.","body":"I tested it on 2 accounts for 180 days.\nHere are the actual numbers.","kicker":"DATA://TEST"},
    {"type":"stat","big":"2.1x","label":"Engagement boost on hybrid posts\n(AI draft + human edit)"},
    {"type":"stat","big":"0.4x","label":"Engagement on raw AI posts\n(no human editing)"},
    {"type":"point","num":"01","title":"FINDING 1","body":"Raw AI = worst performer.\nAlgorithm detects it. Humans sense it.","tag":"RAW = DEAD"},
    {"type":"point","num":"02","title":"FINDING 2","body":"AI + human edit = best performer.\n30-60% edit rate was the sweet spot.","tag":"HYBRID WINS"},
    {"type":"point","num":"03","title":"FINDING 3","body":"Hooks written by AI underperformed by 40%.\nHumans write hooks. AI writes body.","tag":"HOOK = HUMAN"},
    {"type":"point","num":"04","title":"FINDING 4","body":"Consistency > quality.\n5 mediocre posts > 1 perfect post.","tag":"VOLUME LAW"},
    {"type":"point","num":"05","title":"FINDING 5","body":"AI-generated images tanked reach.\nReal photos + custom graphics won.","tag":"VISUALS = REAL"},
    {"type":"recap","title":"THE PLAYBOOK","points":["Human hooks · AI body · Human edit","Real photos > AI images","Consistency beats perfection","Test with DATA, not feelings","Edit rate > 30% = safe"]},
    {"type":"cta","title":"TESTED THIS YOURSELF?","body":"Drop your numbers.\nI'll build a bigger dataset.","kicker":"DATA://END"}
  ]
},

{
  "id": 18, "category": "D",
  "title": "AEO vs SEO — The Rules Changed",
  "subtitle": "2026 playbook for ranking in AI answers",
  "slides": [
    {"type":"hook","title":"AEO vs SEO","sub":"The rules changed. Your traffic is next.","kicker":"DATA://01"},
    {"type":"problem","title":"Google search is shrinking.","body":"AI answer engines are the new front door.\nYour SEO playbook is 6 months from obsolete.","kicker":"DATA://WAKE"},
    {"type":"stat","big":"-47%","label":"Drop in organic Google CTR\nsince AI overviews launched (2024-2026)"},
    {"type":"point","num":"01","title":"AEO = ANSWER ENGINE OPT","body":"Optimizing for ChatGPT, Perplexity, Gemini, Claude.\nThey're the new 'search engines'.","tag":"DEFINITION"},
    {"type":"point","num":"02","title":"RULE 1 — ANSWER FIRST","body":"Lead with the answer.\nAI engines cite the first 200 words.","tag":"STRUCTURE"},
    {"type":"point","num":"03","title":"RULE 2 — SCHEMA MATTERS","body":"FAQ schema, HowTo schema, Article schema.\nAI crawlers eat structured data.","tag":"CODE"},
    {"type":"point","num":"04","title":"RULE 3 — ENTITY SIGNALS","body":"Your brand needs Wikipedia, G2, Crunchbase.\nLLMs trust entities, not keywords.","tag":"PROOF"},
    {"type":"point","num":"05","title":"RULE 4 — BE QUOTABLE","body":"Write in pull-quote format.\nOne-sentence facts that can be copy-pasted.","tag":"VOICE"},
    {"type":"point","num":"06","title":"RULE 5 — FRESHNESS","body":"Update posts every 90 days.\nAI engines prefer recent sources.","tag":"MAINTAIN"},
    {"type":"recap","title":"THE MIGRATION","points":["SEO: keywords","AEO: answers","SEO: backlinks","AEO: citations in AI outputs","SEO: rank","AEO: be quoted"]},
    {"type":"cta","title":"IS YOUR SITE AEO-READY?","body":"Save this as your audit checklist.\nReply 'AEO' — I'll send the full 2026 guide.","kicker":"DATA://END"}
  ]
},

{
  "id": 19, "category": "D",
  "title": "AI Adoption by Industry",
  "subtitle": "What the 2026 data actually says",
  "slides": [
    {"type":"hook","title":"AI Adoption by Industry","sub":"The numbers nobody posts","kicker":"DATA://01"},
    {"type":"problem","title":"Everyone asks: 'is AI overhyped?'","body":"Depends on your industry.\nHere's the real 2026 adoption data.","kicker":"DATA://CTX"},
    {"type":"stat","big":"78%","label":"Software & tech\nTop adopter. Obviously."},
    {"type":"stat","big":"61%","label":"Finance & banking\nFraud detection + research"},
    {"type":"stat","big":"54%","label":"Marketing & media\nContent + automation"},
    {"type":"stat","big":"34%","label":"Healthcare\nSlow — regulation"},
    {"type":"stat","big":"22%","label":"Construction\nThe biggest OPPORTUNITY gap"},
    {"type":"point","num":"01","title":"THE PATTERN","body":"High-adoption industries = more competition.\nLow-adoption = untapped goldmines.","tag":"INSIGHT"},
    {"type":"point","num":"02","title":"WHERE TO BUILD","body":"Construction · Logistics · Legal ops · Real estate · Manufacturing.\n<30% adoption = easy wins.","tag":"OPPORTUNITY"},
    {"type":"recap","title":"THE CONTRARIAN PLAY","points":["Everyone builds for tech","Smart money goes where tech hasn't","Boring industry + AI = moat","Pick the industry nobody tweets about","That's where the money is"]},
    {"type":"cta","title":"WHICH INDUSTRY ARE YOU IN?","body":"Drop it in the comments.\nI'll tell you your AI opportunity score.","kicker":"DATA://END"}
  ]
},

{
  "id": 20, "category": "D",
  "title": "The Honest Cost of Running an AI Agency",
  "subtitle": "Every expense. Every month.",
  "slides": [
    {"type":"hook","title":"The Honest Cost","sub":"...of running an AI agency in 2026","kicker":"DATA://01"},
    {"type":"problem","title":"Gurus don't show you their P&L.","body":"I will.\nHere's what it actually costs to run a lean AI agency.","kicker":"DATA://REAL"},
    {"type":"stat","big":"$387","label":"Total fixed costs per month\n(everything, not just 'tools')"},
    {"type":"point","num":"01","title":"HOSTING","body":"Vercel · Hostinger · Hetzner VPS for n8n\nTotal: $47/mo","tag":"INFRA"},
    {"type":"point","num":"02","title":"AI APIs","body":"Claude API · OpenAI · Gemini Flash\nTotal: $120/mo (averaged)","tag":"VARIABLE"},
    {"type":"point","num":"03","title":"SAAS (ESSENTIAL ONLY)","body":"GitHub Pro · Notion · Calendly · 1Password\nTotal: $75/mo","tag":"LEAN"},
    {"type":"point","num":"04","title":"DOMAINS + EMAIL","body":"3 domains + Google Workspace\nTotal: $45/mo","tag":"BRAND"},
    {"type":"point","num":"05","title":"MARKETING","body":"Ads · Cold email tool\nTotal: $100/mo (fluctuates)","tag":"GROWTH"},
    {"type":"point","num":"06","title":"WHAT I DON'T PAY FOR","body":"Office. CRM. HR. Lawyers on retainer.\nSlack. Zoom. 90% of SaaS.","tag":"AVOIDED"},
    {"type":"stat","big":"$387 IN","label":"vs. $12K+ out\nThat's the agency margin game"},
    {"type":"recap","title":"THE LESSONS","points":["Costs scale with ego, not revenue","Every 'essential SaaS' can be replaced","Variable costs > fixed costs","Tools after revenue, not before","Your biggest cost is the one you waste"]},
    {"type":"cta","title":"WHAT'S YOUR P&L?","body":"Comment 'RUNWAY' for my full breakdown PDF.\nSave this as your audit.","kicker":"DATA://END"}
  ]
},

# =============================================================
# CATEGORY E — CASE FILE (Case Studies / Anatomy)
# =============================================================

{
  "id": 21, "category": "E",
  "title": "Anatomy of a $50K AI Project",
  "subtitle": "Full breakdown — nothing hidden",
  "slides": [
    {"type":"hook","title":"Anatomy of a $50K","sub":"AI Project. Full breakdown.","kicker":"CASE FILE · #021"},
    {"type":"problem","title":"'How do people charge $50K?'","body":"Here's the exact project.\nExact deliverables. Exact price justification.","kicker":"CASE · CTX"},
    {"type":"point","num":"01","title":"THE CLIENT","body":"Mid-size logistics company.\nDrowning in manual ops. 8-person back office.","tag":"CONTEXT"},
    {"type":"point","num":"02","title":"THE PROBLEM","body":"2,400 orders/month processed by hand.\n40% error rate. $200K/year in recovery costs.","tag":"PAIN = $"},
    {"type":"point","num":"03","title":"THE DELIVERABLE","body":"n8n workflow + Claude API + dashboard.\nAuto-classifies, routes, enters data.","tag":"BUILD"},
    {"type":"point","num":"04","title":"THE PRICE","body":"$50K one-time.\n$2K/mo maintenance retainer.\nClient saved $200K → easy yes.","tag":"VALUE-BASED"},
    {"type":"point","num":"05","title":"THE TIMELINE","body":"Week 1: audit + scope\nWeek 2-3: build\nWeek 4: train + handover","tag":"FAST"},
    {"type":"point","num":"06","title":"THE STACK","body":"n8n (self-hosted) · Claude API · Supabase · Retool dashboard · Slack alerts","tag":"REAL"},
    {"type":"point","num":"07","title":"THE RESULT","body":"97% accuracy.\n$180K/year saved in Q1.\nContract renewed 2x.","tag":"ROI 3.6x"},
    {"type":"stat","big":"$50K","label":"Paid once.\n$200K saved. Every year. Forever."},
    {"type":"recap","title":"THE MODEL","points":["Find a $ bleeding process","Price as % of the bleed","Ship in weeks, not months","Retain on maintenance","Reference → next $50K deal"]},
    {"type":"cta","title":"YOUR TURN","body":"Which process in YOUR business bleeds $?\nDrop it below. I'll help scope it.","kicker":"CASE · CLOSE"}
  ]
},

{
  "id": 22, "category": "E",
  "title": "Before AI vs After AI",
  "subtitle": "10 Real Agency Workflows Rebuilt",
  "slides": [
    {"type":"hook","title":"Before AI vs After AI","sub":"10 real agency workflows, rebuilt","kicker":"CASE FILE · #022"},
    {"type":"problem","title":"Every 'before/after' post is fake.","body":"These are OUR real workflows.\nTimed. Measured. Shipping.","kicker":"CASE · CTX"},
    {"type":"point","num":"01","title":"CLIENT ONBOARDING","body":"Before: 4 hrs of forms + emails\nAfter: 20 min (auto-provisioned)","tag":"12x FASTER"},
    {"type":"point","num":"02","title":"PROPOSAL WRITING","body":"Before: 3 hrs per proposal\nAfter: 15 min (Claude + template)","tag":"12x FASTER"},
    {"type":"point","num":"03","title":"WEEKLY REPORTING","body":"Before: 2 hrs per client\nAfter: Automated PDF at 8AM Monday","tag":"∞ FASTER"},
    {"type":"point","num":"04","title":"CONTENT CREATION","body":"Before: 6 hrs for 5 LinkedIn posts\nAfter: 45 min (hook + AI body + edit)","tag":"8x FASTER"},
    {"type":"point","num":"05","title":"LEAD RESEARCH","body":"Before: 15 min per lead\nAfter: 45 seconds (enrichment API)","tag":"20x FASTER"},
    {"type":"point","num":"06","title":"5 MORE","body":"Support · QA · Design variations\nOnboarding emails · Meeting notes","tag":"ALL 5x+"},
    {"type":"stat","big":"38 hrs","label":"Reclaimed per week\n(from these 10 workflows alone)"},
    {"type":"point","num":"07","title":"THE INSIGHT","body":"We didn't cut the work.\nWe cut the TIME spent on work.\nAI doesn't replace humans. It reprices them.","tag":"TRUTH"},
    {"type":"recap","title":"WHAT TO REBUILD FIRST","points":["Anything done weekly","Anything with a template","Anything you hate","Anything that bottlenecks","Start with ONE. This week."]},
    {"type":"cta","title":"WHICH ONE HITS HARDEST?","body":"Drop the number.\nI'll send the exact workflow.","kicker":"CASE · CLOSE"}
  ]
},

{
  "id": 23, "category": "E",
  "title": "How 3 Workflows Replaced a 5-Person Team",
  "subtitle": "Client case study — with numbers",
  "slides": [
    {"type":"hook","title":"3 Workflows.","sub":"Replaced a 5-person team.","kicker":"CASE FILE · #023"},
    {"type":"problem","title":"Client asked: 'can we automate ops?'","body":"We built 3 workflows.\nTheir 5-person back office = now 1 person + a dashboard.","kicker":"CASE · CTX"},
    {"type":"point","num":"01","title":"WORKFLOW 1 — DATA ENTRY","body":"PDFs + emails → Claude extract → CRM\nReplaced: 2 data entry roles","tag":"AUTO"},
    {"type":"point","num":"02","title":"WORKFLOW 2 — CUSTOMER ROUTING","body":"Inbound → GPT classify → auto-response OR escalate\nReplaced: 1.5 support roles","tag":"AUTO"},
    {"type":"point","num":"03","title":"WORKFLOW 3 — REPORTING","body":"Nightly cron → pulls 6 sources → branded PDF → email\nReplaced: 1 analyst","tag":"AUTO"},
    {"type":"stat","big":"$360K","label":"Annual payroll eliminated\n(4.5 of 5 roles, kept senior ops lead)"},
    {"type":"point","num":"04","title":"THE ETHICS","body":"Client retrained the remaining 4 people.\nMoved them into higher-value roles.\nNobody lost their job.","tag":"IMPORTANT"},
    {"type":"point","num":"05","title":"OUR FEE","body":"$75K build.\n$3K/mo maintenance retainer.\nPayback: under 3 months.","tag":"PRICING"},
    {"type":"point","num":"06","title":"WHAT NOBODY TALKS ABOUT","body":"The workflows aren't the hard part.\nChange management is.\nPeople > prompts.","tag":"LESSON"},
    {"type":"recap","title":"THE PLAYBOOK","points":["Identify 3 tasks taking the most hours","Automate → don't fire → retrain","Price as % of annual saving","Retain on maintenance","Ship ugly. Iterate fast."]},
    {"type":"cta","title":"BUILDING SOMETHING SIMILAR?","body":"DM me the use case.\nI'll tell you if it's a 3-workflow job.","kicker":"CASE · CLOSE"}
  ]
},

{
  "id": 24, "category": "E",
  "title": "10 Lessons From Building 100 Websites",
  "subtitle": "Mistakes, truths, and what actually works",
  "slides": [
    {"type":"hook","title":"100 websites built.","sub":"10 lessons I wish I knew at #1.","kicker":"CASE FILE · #024"},
    {"type":"problem","title":"I've built 100+ websites over 7 years.","body":"Here are the non-obvious lessons.\nNothing in here is on YouTube.","kicker":"CASE · CTX"},
    {"type":"point","num":"01","title":"LESSON 1","body":"The homepage is a lie.\nMost traffic lands on sub-pages. Design those first.","tag":"TRUTH"},
    {"type":"point","num":"02","title":"LESSON 2","body":"Clients hate 'design'.\nThey want trust signals + clarity.\nBeauty is 3rd.","tag":"REFRAME"},
    {"type":"point","num":"03","title":"LESSON 3","body":"Shipping ugly > perfecting pretty.\nA live website earns. A Figma file doesn't.","tag":"SPEED"},
    {"type":"point","num":"04","title":"LESSON 4","body":"Never let clients write copy.\nAsk questions. Transcribe answers. YOU write.","tag":"COPY"},
    {"type":"point","num":"05","title":"LESSON 5","body":"Stock photos = trust killer.\nUse real photos, even bad ones.","tag":"VISUALS"},
    {"type":"point","num":"06","title":"LESSON 6","body":"Mobile-first is dead.\nMobile-ONLY is alive.\n72% of visits. Design for it.","tag":"MOBILE"},
    {"type":"point","num":"07","title":"LESSON 7","body":"Page speed beats everything.\nA slow 'stunning' site loses to a fast ugly one.","tag":"PERF"},
    {"type":"point","num":"08","title":"LESSON 8","body":"Contact form = revenue leak.\nUse a calendar, WhatsApp, or direct DM.","tag":"CONVERT"},
    {"type":"recap","title":"THE META-LESSON","points":["Websites are sales assets, not art","Trust > beauty","Speed > features","Ship > polish","Every website = a revenue machine in disguise"]},
    {"type":"cta","title":"WHICH LESSON HIT HARDEST?","body":"Drop the number in the comments.\nI'll share the deep-dive.","kicker":"CASE · CLOSE"}
  ]
},

{
  "id": 25, "category": "E",
  "title": "The $500 to $10K Client Transformation Playbook",
  "subtitle": "Real moves. Real numbers.",
  "slides": [
    {"type":"hook","title":"$500 → $10K client","sub":"How to 20x your average deal size","kicker":"CASE FILE · #025"},
    {"type":"problem","title":"Most freelancers stay stuck at $500 projects.","body":"Not because of skill.\nBecause of POSITIONING.\nHere's the ladder.","kicker":"CASE · CTX"},
    {"type":"point","num":"01","title":"STEP 1 — NICHE","body":"Stop saying 'I do web design'.\nSay 'I build lead-gen sites for dental clinics'.","tag":"POSITION"},
    {"type":"point","num":"02","title":"STEP 2 — CASE","body":"Build 1 case study. Real numbers.\n'Clinic X → 47 new patients/month from site'","tag":"PROOF"},
    {"type":"point","num":"03","title":"STEP 3 — OUTCOMES","body":"Price the outcome, not the output.\nNot '20 pages' → '47 new patients/month'.","tag":"REFRAME"},
    {"type":"point","num":"04","title":"STEP 4 — PACKAGE","body":"Productize: 'Lead-Gen Site — $9,997'\nFixed scope. Fixed timeline. No hourly.","tag":"PRODUCTIZE"},
    {"type":"point","num":"05","title":"STEP 5 — FLOOR","body":"Set a MIN price. $5K or $10K.\nWalk away from smaller deals.","tag":"DISCIPLINE"},
    {"type":"point","num":"06","title":"STEP 6 — PROOF STACK","body":"Testimonials · metrics · named clients · logos\nYour proof stack = your pricing power","tag":"ARSENAL"},
    {"type":"stat","big":"19.4x","label":"Average deal size increase\nfor freelancers who follow this ladder"},
    {"type":"recap","title":"THE TRUTH","points":["You're not 20x better at $10K","You're 20x more positioned","Skill is a commodity. Positioning isn't.","Say no to $500. Say yes to $10K."]},
    {"type":"cta","title":"STUCK AT $500?","body":"Reply with your niche.\nI'll tell you your $10K offer.","kicker":"CASE · CLOSE"}
  ]
},

# =============================================================
# CATEGORY F — MINDSCAPE (Mental Models / Philosophy)
# =============================================================

{
  "id": 26, "category": "F",
  "title": "10 Mental Models Every AI Founder Should Steal",
  "subtitle": "Frameworks that change how you decide",
  "slides": [
    {"type":"hook","title":"10 Mental Models","sub":"Every AI founder should steal","kicker":"· MINDSCAPE ·"},
    {"type":"problem","title":"Skills make you productive.","body":"Mental models make you correct.\nHere are the 10 that shaped us.","kicker":"· WHY ·"},
    {"type":"point","num":"01","title":"INVERSION","body":"Don't ask 'how to succeed'.\nAsk 'how would I guarantee failure?' Then avoid those.","tag":"CHARLIE MUNGER"},
    {"type":"point","num":"02","title":"SECOND-ORDER THINKING","body":"Every decision has downstream effects.\nThink 3 moves ahead, not 1.","tag":"CHESS"},
    {"type":"point","num":"03","title":"OPPORTUNITY COST","body":"Saying YES to X = saying NO to everything else.\nEvery hour is a choice.","tag":"ECONOMICS"},
    {"type":"point","num":"04","title":"10x vs 10%","body":"Thinking 10x is EASIER than 10%.\n10% = compete. 10x = rebuild.","tag":"ASTRO TELLER"},
    {"type":"point","num":"05","title":"HANLON'S RAZOR","body":"Never attribute to malice what stupidity explains.\nKeeps you sane in business.","tag":"PSYCHOLOGY"},
    {"type":"point","num":"06","title":"THE MAP IS NOT THE TERRITORY","body":"Models are approximations.\nReality > plans. Always.","tag":"HUMILITY"},
    {"type":"point","num":"07","title":"PARETO (80/20)","body":"20% of inputs → 80% of outputs.\nFind the 20. Kill the 80.","tag":"FOCUS"},
    {"type":"point","num":"08","title":"CIRCLE OF COMPETENCE","body":"Know what you know.\nKnow what you don't.\nOperate inside the first.","tag":"BUFFETT"},
    {"type":"recap","title":"THE META-MODEL","points":["Models → better questions","Better questions → better decisions","Better decisions → compounded outcomes","Skills decay. Models compound."]},
    {"type":"cta","title":"WHICH ONE RESHAPED YOU?","body":"Drop the number.\nLet's discuss in the comments.","kicker":"· CLOSE ·"}
  ]
},

{
  "id": 27, "category": "F",
  "title": "The Founder Mental Health Playbook",
  "subtitle": "No hustle BS. Real systems.",
  "slides": [
    {"type":"hook","title":"The Founder Mental","sub":"Health Playbook (no hustle BS)","kicker":"· MINDSCAPE ·"},
    {"type":"problem","title":"'Grind 100 hours' is killing founders.","body":"Here's what actually keeps you sharp for 10 years.\nNot 10 months.","kicker":"· TRUTH ·"},
    {"type":"point","num":"01","title":"SLEEP IS STRATEGY","body":"7-8 hours non-negotiable.\nEvery hour below = 1 IQ point off your decisions.","tag":"NEUROSCIENCE"},
    {"type":"point","num":"02","title":"MORNING SUN","body":"10 min sunlight before screens.\nSets cortisol rhythm for the whole day.","tag":"FREE"},
    {"type":"point","num":"03","title":"NO PHONE MORNINGS","body":"First hour = yours.\nNot notifications. Not Slack. Not X.","tag":"DEFENSE"},
    {"type":"point","num":"04","title":"MOVE DAILY","body":"Walk · lift · swim · anything.\n20 min moves your brain out of loops.","tag":"BODY-MIND"},
    {"type":"point","num":"05","title":"ONE FRIEND","body":"One person who knows your real numbers.\nAnd your real fears.\nIsolation kills founders.","tag":"HUMAN"},
    {"type":"point","num":"06","title":"REST GUILT-FREE","body":"Rest isn't lazy.\nRest is how compounding works.\nFounders who rest outlast founders who grind.","tag":"REFRAME"},
    {"type":"point","num":"07","title":"TRACK 3 THINGS","body":"Sleep · mood · energy.\nIf all 3 drop → stop everything. Reset.","tag":"EARLY WARNING"},
    {"type":"quote","text":"The goal isn't to burn bright.\nIt's to burn long.","attr":"— Agency lesson, learned the hard way"},
    {"type":"recap","title":"THE PLAYBOOK","points":["Sleep 7-8h","Sun + movement daily","1 honest friend","No phone morning hour","Rest without guilt","Track sleep/mood/energy"]},
    {"type":"cta","title":"WHICH DO YOU SKIP?","body":"Reply with the one you need most.\nI'll share the system I use.","kicker":"· CLOSE ·"}
  ]
},

{
  "id": 28, "category": "F",
  "title": "7 Books Every AI Agency Owner Should Read",
  "subtitle": "Not the typical list",
  "slides": [
    {"type":"hook","title":"7 Books Every","sub":"AI agency owner should read (not the usual ones)","kicker":"· MINDSCAPE ·"},
    {"type":"problem","title":"Everyone recommends '$100M Offers'.","body":"Here are 7 books almost nobody reads.\nThey'll change how you build.","kicker":"· WHY ·"},
    {"type":"point","num":"01","title":"THE E-MYTH","body":"Michael Gerber.\nWhy most founders are technicians trapped in their own business.","tag":"SYSTEMS"},
    {"type":"point","num":"02","title":"OBVIOUSLY AWESOME","body":"April Dunford.\nThe book on positioning your AI agency.","tag":"POSITIONING"},
    {"type":"point","num":"03","title":"THE GREAT CEO WITHIN","body":"Matt Mochary.\nOperating manual for founders. Unreasonably tactical.","tag":"OPS"},
    {"type":"point","num":"04","title":"THE DIP","body":"Seth Godin.\nHow to know when to quit.\nMore valuable than 'never give up'.","tag":"DECISIONS"},
    {"type":"point","num":"05","title":"THE ALMANACK OF NAVAL","body":"Eric Jorgenson.\nLeverage, wealth, peace.\nBetter than any productivity book.","tag":"MENTAL"},
    {"type":"point","num":"06","title":"HIGH OUTPUT MANAGEMENT","body":"Andy Grove.\nThe only management book that aged well.","tag":"CLASSIC"},
    {"type":"point","num":"07","title":"COMPANY OF ONE","body":"Paul Jarvis.\nThe case for staying small and profitable.","tag":"PHILOSOPHY"},
    {"type":"quote","text":"Readers become leaders.\nBut only if they apply ONE idea.","attr":"— stolen from somewhere smart"},
    {"type":"recap","title":"THE RULE","points":["1 book per month, max","Apply 1 idea per book","Re-read the best ones","Books compound. Feeds don't.","The quiet founder out-reads the loud one"]},
    {"type":"cta","title":"WHICH IS YOUR #1?","body":"Drop it below.\nI'll add to the next reading list post.","kicker":"· CLOSE ·"}
  ]
},

{
  "id": 29, "category": "F",
  "title": "The Art of Saying No",
  "subtitle": "With scripts you can steal",
  "slides": [
    {"type":"hook","title":"The Art of Saying No","sub":"...with scripts you can steal","kicker":"· MINDSCAPE ·"},
    {"type":"problem","title":"Every YES is a NO to something else.","body":"Founders die from over-committing.\nHere's how to say no — with grace and scripts.","kicker":"· WHY ·"},
    {"type":"point","num":"01","title":"TO BAD-FIT CLIENTS","body":"'Thanks for thinking of us. This isn't the right fit. Here's someone better: [name].'","tag":"SCRIPT"},
    {"type":"point","num":"02","title":"TO SCOPE CREEP","body":"'Great idea — I'll add it to V2. Current scope stays as agreed.'","tag":"SCRIPT"},
    {"type":"point","num":"03","title":"TO LOW BUDGETS","body":"'Our floor is $X. If budget is a constraint, here's a free resource: [link].'","tag":"SCRIPT"},
    {"type":"point","num":"04","title":"TO 'CAN I PICK YOUR BRAIN'","body":"'Happy to help. My paid consult is $500/30min. If that's not it, here's my best content.'","tag":"SCRIPT"},
    {"type":"point","num":"05","title":"TO NEW OPPORTUNITIES","body":"'Interesting — let me sit with it for 48 hours. I don't make 'yes' decisions in 5 minutes.'","tag":"BUY TIME"},
    {"type":"point","num":"06","title":"TO BURNOUT REQUESTS","body":"'Not this week. Can we revisit Monday?'\nNobody died from delayed YES.","tag":"SCRIPT"},
    {"type":"quote","text":"Every NO to distraction\nis a YES to your real work.","attr":"— Derek Sivers, paraphrased"},
    {"type":"point","num":"07","title":"THE UPGRADE","body":"'Hell yes or no'.\nIf it's not a hell yes, it's a no.\nKills 80% of overcommitment instantly.","tag":"FRAMEWORK"},
    {"type":"recap","title":"THE REFRAME","points":["Saying no is kindness, not cruelty","Fast NO > slow MAYBE","Scripts remove guilt","Hell yes or no","Every no protects your best work"]},
    {"type":"cta","title":"WHICH NO ARE YOU AVOIDING?","body":"Drop the situation.\nI'll write you the script.","kicker":"· CLOSE ·"}
  ]
},

{
  "id": 30, "category": "F",
  "title": "The Freelancer to Agency Transition",
  "subtitle": "The roadmap nobody gives you",
  "slides": [
    {"type":"hook","title":"Freelancer → Agency","sub":"The transition roadmap","kicker":"· MINDSCAPE ·"},
    {"type":"problem","title":"Most freelancers stay freelancers.","body":"Not because of skill.\nBecause the transition is invisible.\nHere's the roadmap.","kicker":"· WHY ·"},
    {"type":"point","num":"01","title":"STAGE 1 · OPERATOR","body":"You do everything.\nYou ARE the product. Max ceiling: ~$15K/mo.","tag":"STUCK"},
    {"type":"point","num":"02","title":"STAGE 2 · SYSTEMATIZER","body":"You document + automate your own process.\nSOPs. Templates. Automations.","tag":"KEY PIVOT"},
    {"type":"point","num":"03","title":"STAGE 3 · DELEGATOR","body":"You hire 1 person.\nFor the SOP'd task. Not the creative part.\nThis is where 80% fail.","tag":"SCARY"},
    {"type":"point","num":"04","title":"STAGE 4 · MANAGER","body":"You stop being in deliverables.\nYou manage the people doing deliverables.","tag":"IDENTITY SHIFT"},
    {"type":"point","num":"05","title":"STAGE 5 · OWNER","body":"You set direction.\nThe agency runs without your daily input.","tag":"FREEDOM"},
    {"type":"point","num":"06","title":"THE KILLER STEP","body":"Stage 2 → 3.\nWriting the SOPs so someone else can do the work.\nMost never write them.","tag":"DO THIS"},
    {"type":"point","num":"07","title":"THE TRUTH","body":"Most freelancers don't want an agency.\nThey want the freedom an agency promises.\nYou can get freedom without the agency.","tag":"CONTROVERSIAL"},
    {"type":"quote","text":"You don't scale an agency.\nYou scale yourself out of it.","attr":"— the quiet part out loud"},
    {"type":"recap","title":"THE CHOICE","points":["Stay lean → keep more profit","Scale → trade profit for reach","Both are valid","Neither is 'right'","Decide WHAT you're building for"]},
    {"type":"cta","title":"WHICH STAGE ARE YOU IN?","body":"Reply with the number.\nI'll share what to focus on next.","kicker":"· CLOSE ·"}
  ]
},

]
