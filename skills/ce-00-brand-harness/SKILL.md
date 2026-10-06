---
name: "ce-00-brand-harness"
description: "Run first, once per brand, before any ce-01 to ce-06 workflow: brand intake, brand bible, asset library, marketing advisor, Brand Guardian checks, corrections memory."
---

# CE-00 BRAND HARNESS (shared layer)

Run once per brand. Every other workflow (ce-01 image ads, ce-02 UGC, ce-03 animated ads, ce-04 homepage, ce-05 website rebuild, ce-06 cinematic ad) loads this output instead of redoing intake.
If a brand bible already exists: load it, check it is current (see REFRESH), skip intake.
Brand-agnostic. Variables: [BRAND], [PRODUCT], [AUDIENCE].

## MODE (pick first; default EXPLORE)
- EXPLORE: experiments, demos, pitches. Light intake only: real packshots and logo, plus a 5-line brand look. Skip Steps 2 to 5. ALWAYS ON: credit quote; no real person's likeness without consent; no fake reviews or claims shown as real; WORLD RULES below.
- BUILD: full harness below. Use when I say "build", "ship", "client", or pick a winner.

## WHERE THINGS LIVE
One home per brand (a claude.ai Project named [BRAND], or a folder). Four files:
1. `brand-bible.md`: identity, voice, palette, fonts, claims, legal, audience, competitors.
2. `asset-library.md`: list of every approved asset with file path/link, type, status (APPROVED / DRAFT / BANNED).
3. `corrections-log.md`: every correction the client or user made, dated, plus where it was applied.
4. `outputs-log.md`: every finished output (workflow, date, file, tier, credits, result).
The workflow skills live in the Creative Engine project. Brand facts live in the brand's home. Never mix.

## HARD RULES (BUILD; in EXPLORE only the ALWAYS ON items apply)
1. Real packs, logos and photos go in as images. AI may copy label text from a real reference, but text comes only from the real source and every result is checked against the real image; if it fails, put the real label back or re-run. Never invent text, logos or products for a real brand. Never redraw real people's faces. No fake testimonials or before/after proof. Prefer real images as references for new renders over flat cutouts; keep the cutout as backup when the label must be exact.
2. No invented claims, reviews, customers, numbers, endorsements. A claim is allowed only if it is on the APPROVED CLAIMS list with a source.
3. Health, supplement, finance and kids' categories: flag regulated claims. Mark them REVIEW BY CLIENT. Never guess.
4. Real people (founder, ambassador, creators): written consent and likeness scope recorded in the bible before use.
5. Public scraping only. Never enter passwords or use accounts the user did not provide. Respect robots/terms; use the official feed or ask the client for files.
6. Mark unknowns as UNKNOWN. Do not fill gaps with guesses.
7. Quote before any paid step. Never poll.

## WORLD RULES (always on, EXPLORE and BUILD)
Before any image or video prompt:
1. Pick the world: REAL (live-action brand ad), STYLIZED REAL (painted, anime: real-world logic in a set look) or INVENTED (cartoon, new world).
2. Write 3 to 5 world rules, plus one line: where, when, and why the person is here doing this. Nothing random.
3. Three layers. ANCHORS (people, product, place, reason) stay true to the world. EFFECTS may be fantasy, but each starts from a real cause in the anchors (she opens the bottle, the liquid swirls) and returns to the real. CAMERA is free (macro zoom, sky drop, thread-level close-up).
4. Check every storyboard frame against the rules. If the place cannot hold the action, change the action.

## STEP 1: INTAKE (ask once: URL, socials, any files)
| What | How |
|---|---|
| Site pages, copy, structure | Firecrawl map + scrape (markdown) |
| Logo, colors, fonts | Firecrawl scrape with `branding` format; confirm against the real logo file |
| Products, prices, variants, images | Public feed (`/products.json` on Shopify), or scrape collection + product pages |
| Instagram / TikTok: posts, top performers, comments | Apify actors (search-actors, call-actor) |
| Reviews | Scrape review pages / Apify; copy real reviews verbatim with source and date |
| Competitors | Firecrawl search + scrape 3-5; Meta Ad Library via browser (Claude in Chrome) |
| Screenshots (desktop + phone) | Claude in Chrome |
| Analytics, ad performance | Only if the client shares exports. Else UNKNOWN. |
Save raw pulls in a `raw/` folder. Never edit raw.

## STEP 2: BRAND BIBLE (fill every field, UNKNOWN where missing)
1. IDENTITY: name, one-line positioning, mission, what they sell, price tier, where they sell.
2. AUDIENCE: primary, secondary, pains, desires, words they use.
3. VOICE: 3 voice words, do / don't list, 5 sample lines lifted from the real site, banned words.
4. VISUAL: palette (hex, role), banned colors, fonts (name, weight, role, license/source), logo versions + clear space + min size, photo style, motion words (3).
5. PRODUCTS: per product: name, variants, benefit line, ingredients/specs, real image files (front, 3/4, back).
6. APPROVED CLAIMS: each claim + source + any required disclaimer. Plus BANNED CLAIMS.
7. LEGAL + PLATFORM: disclaimers, FDA/FTC-type rules for the category, AI-disclosure needs, age limits, music/talent rights.
8. PEOPLE: founder/ambassadors/creators, consent status, usage scope, expiry. Generated creators allowed? (pitch: yes; live: per client.)
9. COMPETITORS: 3-5, what they do well, where this brand can beat them.
10. PROOF: real reviews, press, numbers (each with source).
11. GOALS + CONSTRAINTS: goal, budget, deadline, must-keep items, no-go items.
12. WORLD: world type (real / stylized real / invented) and 3 to 5 world rules. Every workflow reads these.
Output: brand-bible.md. Show the user a 10-line summary and the UNKNOWN list.
GATE A: user confirms the bible. Fill or accept UNKNOWNs.

## STEP 3: ASSET LIBRARY
- Download/collect: logo (SVG/PNG, light + dark), packshots (front, 3/4, back), lifestyle, video, fonts.
- Clean: remove_background for packs if needed; keep originals untouched.
- Name: `[brand]_[type]_[subject]_[variant]_v[n]`.
- Status each: APPROVED / DRAFT / BANNED. Note resolution, rights, source.
- Packshot completeness check: every flagship has front + 3/4. If missing, ask the client. Do not generate a pack from nothing.
- Higgsfield: create brand + products (ads_studio_create_brand, add_product) and Elements (manage_reference_elements) for locked packs, people, locations.
GATE B: asset list reviewed. Gaps sent to client as a checklist.

## STEP 4: MARKETING ADVISOR (recommend what to make first)
- Read: competitors' ads and sites, the brand's best social posts, reviews (what customers praise), any performance data.
- Output a one-page brief: top 3 angles, top 3 formats, what competitors overuse, 5 recommended outputs ranked (workflow + why + cost), what to test first.
- Map to workflows: static angles > ce-01; creator proof > ce-02; motion > ce-03; site fixes > ce-04/05; brand film > ce-06.
GATE C: user picks what to run.

## STEP 5: BRAND GUARDIAN (checklist every workflow's audit step runs)
A separate pass, not the maker. Each item pass/fail:
- Palette: only bible hex values (sampled from output).
- Fonts: only bible fonts.
- Logo: correct file, clear space, min size, no distortion/recolor.
- Pack/label: matches the real image exactly; no warped or invented text.
- Claims: every claim on APPROVED list; disclaimers present.
- People: consented, scoped; generated people not presented as real customers; disclosure on.
- Voice: matches do/don't, no banned words.
- Proof: nothing fabricated; reviews verbatim with source.
- Legal/platform: category rules, AI label, music rights.
- Corrections log: no past correction repeated.
Result: PASS / FAIL with a line per failure and the fix. Max 2 fix loops, then escalate to the user. Pair with the gauntlet-loop skill for visual quality.

## STEP 6: MEMORY + CORRECTIONS
- Corrections log format: DATE | WHO | WHAT WAS WRONG | RULE (one line) | APPLIED TO (files/outputs).
- When anything is corrected: (1) log it, (2) update the bible/asset library if it is a standing rule, (3) re-check every open output and every workflow doc for the same issue, (4) say what was changed.
- Outputs log: add one line per delivered output.
- Decisions (approved tier, angle, hook, headline) go in the bible under DECISIONS with date.

## REFRESH
Re-run intake for changed items when: new products or prices, rebrand, a new campaign, more than 90 days old, or the user says so. Update the bible, log the change.

## WHAT THE SIX WORKFLOWS READ
| Workflow | Needs from harness |
|---|---|
| ce-01 image ads | palette, fonts, logo, packshots, claims, voice, competitors |
| ce-02 UGC | claims, people/consent, voice, packshots, audience words, disclosure rules |
| ce-03 animated ads | palette, logo, motion words, packshots, voice |
| ce-04 homepage | full bible, asset library, analytics, competitors |
| ce-05 website rebuild | full bible, asset library, site crawl, analytics, redirects |
| ce-06 cinematic ad | bible, packshots, people/consent, voice, legal/music rights |
If a needed field is UNKNOWN, the workflow stops and asks. It does not guess.

## DONE WHEN
Bible confirmed (Gate A), asset library reviewed (Gate B), advisor brief delivered (Gate C), logs created. Then hand off: "Harness ready. Which workflow first?"