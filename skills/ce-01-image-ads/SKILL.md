---
name: "ce-01-image-ads"
description: "Run the full static image-ad workflow for any brand: intake, strategy, production with real packshots, finishing, audit, delivery. Use when asked for image ads, Meta or social ad creatives."
---

> Load ce-core first. Always on: quote credits before spend; real label only (text from the real source, checked against the real image); real brand text (name, price, CTA, claims) is set in code or checked letter by letter against the source; no real faces or voices without consent; no fake reviews, claims or results shown as real; world rules before any prompt.

# CE-01 Image Ads

Mission: produce a tested, brand-safe set of static ads for [BRAND] / [PRODUCTS] across [PLATFORMS], using the real product images as references or layers, never invented ones. State your reading of the request in one line first.
Mode, always-on rules, world rules, gates, fix order, shared failures, contingencies, library: see ce-core. Models and prices: ce-core/TOOLS.md.
Camera moves and effects: docs/PLAYBOOK-shots-effects.md.

## Inputs (ask once for anything missing; otherwise infer)
[BRAND URL] [FLAGSHIP PRODUCTS, 3 to 5] [GOAL: sales | leads | traffic | awareness] [PLATFORMS + RATIOS] [AUDIENCE] [OFFER] [APPROVED CLAIMS] [BUDGET in credits] [TIER: tame | new direction | spectacular]

## Workflow-specific rules
- Headline, price and CTA text is set in Canva or code (see ce-core).
- Brand colors and fonts only. No invented people, testimonials, reviews, before/afters.
- Claims only from the label or the approved list.

## Phase 0: Load the harness
0.1 Load the ce-00 brand bible and asset library. If none exists, run ce-00 first (EXPLORE: light intake only). Do not redo intake here.
0.2 MANUAL/CODE: pick the 3 to 5 flagships from the asset library. Confirm real packshots (transparent PNG preferred) and the logo (vector or PNG) are APPROVED.
0.3 Competitor ads and winning angles come from the ce-00 marketing advisor brief. Pull more with Apify only if it is thin.
PLAN gate (BUILD only): show the bible, flagship picks and angle shortlist. Wait.

## Phase 1: Strategy
1.1 Marketing advisor pass: from the bible and competitor ads, propose 5 angles (benefit, ingredient/proof, routine/lifestyle, offer, comparison, social proof from REAL reviews only).
1.2 Build a CONCEPT MATRIX: angle x product x ratio, each with hook, headline, subline, CTA and the exact claim source. Pair concepts by mood for A/B (e.g. clean/calm vs bold/performance).
1.3 Pick a tier. TAME = elevated clean packshot ads. NEW DIRECTION = lifestyle / editorial scenes. SPECTACULAR = dynamic, in-motion composites (still frames). EXPLORE defaults to spectacular.
PLAN gate (BUILD only): approve the matrix and the spend quote.

## Phase 2: Production (choose the path per concept)
PATH A: FAST (Higgsfield Ads Studio)
- A1 SKILL: get_workflow_instructions("ads-studio") and follow it exactly.
- A2 CONNECTOR: ads_studio_create_brand (website) + ads_studio_add_product (page URL + packshot images). Wait until ready. Do not poll.
- A3 ads_studio_quote, tell the credits, wait for yes, then ads_studio_generate. Ratios per TOOLS.md (4:5 is not offered: crop or use Path B).
- A4 Read the run once when asked. Treat output as concepts to check, not final.

PATH B: ACCURATE (locked-pack composite). Use when the label must be exact, or as backup when a real-reference render fails the label check.
- B1 SKILL: get_workflow_instructions("product-photoshoot") for scene and lighting recipes.
- B2 MODEL: build the scene WITHOUT the pack (empty surface, props, lighting, depth) with the board model at 4:5 / 3:4 / 9:16 / 1:1; multi-reference model if needed (TOOLS.md).
- B3 CODE: composite the real transparent packshot onto a measured surface line (contact shadow, matching light direction). The product must sit on the surface exactly, never floating.
- B4 If a model rendered the pack, CODE (OpenCV): align to the real packshot, overlay the true label back, verify.
- B5 MODEL optional: Marketing Studio Product Shot for template-led looks, only if the label check passes.

PATH C: TEMPLATED SCALE (Canva)
- C1 CONNECTOR Canva: build or pick a brand template; autofill-design with headline/price/CTA/packshot per concept; resize-design to every ratio; export-design (PNG/JPG).
- C2 Use C after A or B to set final text and resize.

Motion variants of an approved static (subtle loop, parallax, animated type): hand off to the After Effects layer via ce-03.

## Phase 3: Finish
3.1 Set text, logo, price, CTA in Canva or code. Safe zones: keep key content inside the 80% center for 9:16; keep text under about 20% of the image.
3.2 Export every concept at every ratio. Naming: [brand]_[product]_[angle]_[tier]_[ratio]_v[n].
LOOK gate (BUILD only): show a contact sheet (all concepts, all ratios).

## Phase 4: Audit (BUILD only; a separate agent, never the producer)
4.1 BRAND GUARDIAN (ce-00 Step 5) checks each image: hex colors sampled by pixel, fonts, logo clearspace, label accuracy against the real packshot, claim vs approved source, no fabricated people/reviews, price correct.
4.2 SKILL gauntlet-loop: 2+ adversarial critic rounds for "looks AI-generated", clutter, weak hook, contrast, platform rules.
4.3 Pass/fail table per image. Failures return to Phase 2 with a named fix. Max 2 fix loops.
4.4 Show me any compliance risk (supplements/health, pricing, "best/#1" claims).

## Phase 5: Deliver (BUILD only)
5.1 Ad set folder + contact sheet + spec table (ratio, size, file) + A/B test plan (what each pair tests, success metric, runtime, sample size) + UTM naming.
5.2 Update the brand bible and corrections log (ce-00 Step 6). Propagate every correction to every concept.
5.3 Cost report (credits used vs quoted).

## Extra failure modes (shared ones are in ce-core)
- 4:5 needed: board model at 4:5 or crop from 3:4.
- Generic copy: re-run add_product with the page and photos before generating.

## Run order summary
EXPLORE: world rules > concepts > produce > show me. No gates, audit or delivery.
BUILD: 0 harness > PLAN > 1 strategy > PLAN > 2 produce > 3 finish > LOOK > 4 audit > 5 deliver.

Output style: short, plain language, tables, no filler.
