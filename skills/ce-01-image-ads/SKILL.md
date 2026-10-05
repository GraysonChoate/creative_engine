---
name: "ce-01-image-ads"
description: "Run the full static image-ad workflow for any brand: intake, strategy, production with real packshots, finishing, audit, delivery. Use when asked for image ads, Meta or social ad creatives."
---

# CE-01 Image Ads (universal)

Mission: produce a tested, brand-safe set of static ads for [BRAND] / [PRODUCTS] across [PLATFORMS], using the real product images, never redrawn ones. Run each phase in order. STOP at every GATE and wait for a yes. Quote cost before any spend. State your reading of the request in one line first.
LIBRARY: techniques and exact prompts live at github.com/GraysonChoate/creative_engine (docs/CE-03). Check it before inventing a method.

## Inputs (ask once for anything missing; otherwise infer)
[BRAND URL] [FLAGSHIP PRODUCTS, 3 to 5] [GOAL: sales | leads | traffic | awareness] [PLATFORMS + RATIOS] [AUDIENCE] [OFFER] [APPROVED CLAIMS] [BUDGET in credits] [TIER: tame | new direction | spectacular]

## Hard rules
- Real packshots and logos go in as images. No model redraws labels, logos or text.
- All headline, price and CTA text is set deterministically (Canva or code), never rendered by an image model.
- Brand colors and fonts only. No invented people, testimonials, reviews, before/afters.
- Claims only from the label or the approved list. Health/supplement claims: no disease or cure language.
- Never poll. Never spend without a quote and a yes. Same idempotency key on retries.
- Keep communication short and plain.

## Phase 0: Load the harness
0.1 Load the ce-00 brand bible and asset library. If none exists, run ce-00 first. Do not redo intake here.
0.2 MANUAL/CODE: pick the 3 to 5 flagships from the asset library. Confirm real packshots (transparent PNG preferred) and the logo (vector or PNG) are APPROVED.
0.3 Competitor ads and winning angles come from the ce-00 marketing advisor brief. Pull more with Apify only if it is thin.
GATE 0: show the bible, flagship picks and angle shortlist. Wait.

## Phase 1: Strategy
1.1 Marketing advisor pass: from the bible and competitor ads, propose 5 angles (benefit, ingredient/proof, routine/lifestyle, offer, comparison, social proof from REAL reviews only).
1.2 Build a CONCEPT MATRIX: angle x product x ratio, each with hook, headline, subline, CTA and the exact claim source. Pair concepts by mood for A/B (e.g. clean/calm vs bold/performance).
1.3 Pick a tier. TAME = elevated clean packshot ads. NEW DIRECTION = lifestyle / editorial scenes. SPECTACULAR = dynamic, in-motion composites (still frames).
GATE 1: approve the matrix and the spend quote.

## Phase 2: Production (choose the path per concept)
PATH A: FAST (Higgsfield Ads Studio)
- A1 SKILL: get_workflow_instructions("ads-studio") and follow it exactly.
- A2 CONNECTOR: ads_studio_create_brand (website) + ads_studio_add_product (page URL + packshot images). Wait until ready. Do not poll.
- A3 ads_studio_quote, tell the credits, wait for yes, then ads_studio_generate. Ratios: 1:1, 9:16, 16:9, 3:4. 4:5 is not offered: crop or use Path B.
- A4 Read the run once when asked. Treat output as concepts to audit, not final.

PATH B: ACCURATE (locked-pack composite). Use when the label must be exact.
- B1 SKILL: get_workflow_instructions("product-photoshoot") for scene and lighting recipes.
- B2 MODEL: build the scene WITHOUT the pack (empty surface, props, lighting, depth) with nano_banana_pro or gpt_image_2_5 at 4:5 / 3:4 / 9:16 / 1:1; flux_3_image if multi-reference is needed.
- B3 CODE: composite the real transparent packshot onto a measured surface line (contact shadow, matching light direction). The product must sit on the surface exactly, never floating.
- B4 If a model was allowed to render the pack, CODE (OpenCV): align to the real packshot, overlay the true label back, verify.
- B5 MODEL optional: Marketing Studio Product Shot (marketing_studio_2_image) for template-led looks, only if the label check passes.

PATH C: TEMPLATED SCALE (Canva)
- C1 CONNECTOR Canva: build or pick a brand template; autofill-design with headline/price/CTA/packshot per concept; resize-design to every ratio; export-design (PNG/JPG).
- C2 Use C after A or B to set final text and resize.

## Phase 3: Finish
3.1 Set text, logo, price, CTA in Canva or code. Safe zones: keep key content inside the 80% center for 9:16; keep text under about 20% of the image.
3.2 Export every concept at every ratio. Naming: [brand]_[product]_[angle]_[tier]_[ratio]_v[n].
GATE 2: show a contact sheet (all concepts, all ratios).

## Phase 4: Audit (a separate agent, never the producer)
4.1 BRAND GUARDIAN (ce-00 Step 5) checks each image: hex colors sampled by pixel, fonts, logo clearspace, label accuracy against the real packshot, claim vs approved source, no fabricated people/reviews, price correct.
4.2 SKILL gauntlet-loop: 2+ adversarial critic rounds for "looks AI-generated", clutter, weak hook, contrast, platform rules.
4.3 Pass/fail table per image. Failures return to Phase 2 with a named fix. Max 2 fix loops.
4.4 Show me any compliance risk (supplements/health, pricing, "best/#1" claims).

## Phase 5: Deliver
5.1 Ad set folder + contact sheet + spec table (ratio, size, file) + A/B test plan (what each pair tests, success metric, runtime, sample size) + UTM naming.
5.2 Update the brand bible and corrections log (ce-00 Step 6). Propagate every correction to every concept.
5.3 Cost report (credits used vs quoted).

## Failure modes -> fix
- Label/text warped: Path B composite, text in Canva.
- Product floating: measure the surface line, add a contact shadow.
- Off-brand color: recolor in code, re-sample hex.
- 4:5 needed: gpt_image_2_5 or crop from 3:4.
- Generic copy: re-run add_product with the page and photos before generating.
- Looks AI: real photos, tighter crop, fewer effects.

Output style: short, plain language, tables, no filler. Ask at most one question at a time.