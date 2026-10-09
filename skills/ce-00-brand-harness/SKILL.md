---
name: "ce-00-brand-harness"
description: "Run first, once per brand, before any ce-01 to ce-06 workflow: brand intake, brand bible, asset library, marketing advisor, Brand Guardian checks, corrections memory."
---

> Load ce-core first. Always on: quote credits before spend; real label only (text from the real source, checked against the real image); real brand text (name, price, CTA, claims) is set in code or checked letter by letter against the source; no real faces or voices without consent; no fake reviews, claims or results shown as real; world rules before any prompt.

# CE-00 BRAND HARNESS (brand layer)

Run once per brand. Every other workflow (ce-01 to ce-07) loads this output instead of redoing intake.
If a brand bible exists: load it, check it is current (see REFRESH), skip intake.
Brand-agnostic. Variables: [BRAND], [PRODUCT], [AUDIENCE].
Mode, always-on rules, world rules, gates, contingencies, library index: see ce-core.
EXPLORE: light intake only (real packshots, logo, 5-line brand look, world rules). Skip Steps 2 to 5.
BUILD: full harness below.

## WHERE THINGS LIVE
One home per brand (a claude.ai Project named [BRAND], or a folder). Four files:
1. `brand-bible.md`: identity, voice, palette, fonts, motion, claims, legal, audience, competitors.
2. `asset-library.md`: every approved asset with file path/link, type, status (APPROVED / DRAFT / BANNED).
3. `corrections-log.md`: every correction, dated, plus where it was applied.
4. `outputs-log.md`: every finished output (workflow, date, file, tier, credits, result).
The workflow skills live in the Creative Engine project. Brand facts live in the brand's home. Never mix.

## BRAND-LAYER RULES (BUILD; the universal rules are in ce-core)
1. APPROVED CLAIMS only: each claim has a source on the list. Anything else is not allowed.
2. Health, supplement, finance and kids' categories: flag regulated claims. Mark them REVIEW BY CLIENT. Never guess.
3. Real people (founder, ambassador, creators): written consent and likeness scope recorded in the bible before use.
4. Public scraping only. Never enter passwords or use accounts the user did not provide. Respect robots/terms; use the official feed or ask the client for files.
5. Mark unknowns as UNKNOWN. Do not fill gaps with guesses.
6. Real photos beat flat cutouts as references; keep the cutout as backup when the label must be exact. No fake testimonials or before/after proof.

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
Save raw pulls in a `raw/` folder in the working project (not this repo). Never edit raw.

## STEP 2: BRAND BIBLE (fill every field, UNKNOWN where missing)
1. IDENTITY: name, one-line positioning, mission, what they sell, price tier, where they sell.
2. AUDIENCE: primary, secondary, pains, desires, words they use.
3. VOICE: 3 voice words, do / don't list, 5 sample lines lifted from the real site, banned words.
4. VISUAL: palette (hex, role), banned colors, fonts (name, weight, role, license/source), logo versions + clear space + min size, photo style. Motion: see section 13.
5. PRODUCTS: per product: name, variants, benefit line, ingredients/specs, real image files (front, 3/4, back).
6. APPROVED CLAIMS: each claim + source + any required disclaimer. Plus BANNED CLAIMS.
7. LEGAL + PLATFORM: disclaimers, FDA/FTC-type rules for the category, AI-disclosure needs, age limits, music/talent rights.
8. PEOPLE: founder/ambassadors/creators, consent status, usage scope, expiry. Generated creators allowed? (pitch: yes; live: per client.)
9. COMPETITORS: 3-5, what they do well, where this brand can beat them.
10. PROOF: real reviews, press, numbers (each with source).
11. GOALS + CONSTRAINTS: goal, budget, deadline, must-keep items, no-go items.
12. WORLD: world type (real / stylized real / invented) and 3 to 5 world rules. Every workflow reads these.
13. MOTION: 3 motion words (speed and feel), easing curves, durations, transition style, sound style, plus the MOTION LIBRARY (approved motion styles, reusable). ce-03 and the After Effects layer read and extend this section. Check it before building new motion.
Output: brand-bible.md. Show the user a 10-line summary and the UNKNOWN list.
PLAN gate (BUILD only): user confirms the bible. Fill or accept UNKNOWNs.

## STEP 3: ASSET LIBRARY
- Download/collect: logo (SVG/PNG, light + dark), packshots (front, 3/4, back), lifestyle, video, fonts.
- Clean: remove_background for packs if needed; keep originals untouched.
- Name: `[brand]_[type]_[subject]_[variant]_v[n]`.
- Status each: APPROVED / DRAFT / BANNED. Note resolution, rights, source.
- Packshot completeness check: every flagship has front + 3/4. If missing, ask the client. Do not generate a pack from nothing.
- Higgsfield: create brand + products (ads_studio_create_brand, add_product) and Elements (manage_reference_elements) for locked packs, people, locations.
ASSETS gate (BUILD only): asset list reviewed. Gaps sent to client as a checklist.

## STEP 4: MARKETING ADVISOR (recommend what to make first)
- Read: competitors' ads and sites, the brand's best social posts, reviews (what customers praise), any performance data.
- Output a one-page brief: top 3 angles, top 3 formats, what competitors overuse, 5 recommended outputs ranked (workflow + why + cost), what to test first.
- Map to workflows: static angles > ce-01; creator proof > ce-02; motion > ce-03; site fixes > ce-04/05; brand film > ce-06; pitch > ce-07.
PLAN gate (BUILD only): user picks what to run.

## STEP 5: BRAND GUARDIAN (BUILD; checklist every workflow's audit step runs)
A separate pass, not the maker. Each item pass/fail:
- Palette: only bible hex values (sampled from output).
- Fonts: only bible fonts.
- Logo: correct file, clear space, min size, no distortion/recolor.
- Pack/label: matches the real image exactly; no warped or invented text.
- Claims: every claim on APPROVED list; disclaimers present.
- People: consented, scoped; generated people not presented as real customers; disclosure on.
- Voice: matches do/don't, no banned words.
- Motion: matches section 13 motion words and approved styles.
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

## WHAT THE WORKFLOWS READ
| Workflow | Needs from harness |
|---|---|
| ce-01 image ads | palette, fonts, logo, packshots, claims, voice, competitors |
| ce-02 UGC | claims, people/consent, voice, packshots, audience words, disclosure rules |
| ce-03 animated ads | palette, logo, motion (section 13), packshots, voice |
| ce-04 homepage | full bible, asset library, analytics, competitors |
| ce-05 website rebuild | full bible, asset library, site crawl, analytics, redirects |
| ce-06 cinematic ad | bible, packshots, people/consent, voice, legal/music rights |
| ce-07 pitch deck | whatever exists; inferred items marked |
In BUILD, if a needed field is UNKNOWN, the workflow stops and asks. It does not guess. In EXPLORE, use the light intake and note what is UNKNOWN.

## DONE WHEN
EXPLORE: real packshots, logo and 5-line look in hand, world rules written. BUILD: bible confirmed (PLAN), asset library reviewed (ASSETS), advisor brief delivered and workflow picked (PLAN), logs created. Then hand off: "Harness ready. Which workflow first?"
