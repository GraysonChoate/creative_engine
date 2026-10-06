---
name: "ce-02-ugc"
description: "Run the full UGC-style video workflow for any brand: strategy, creator lock, script, production, QA, captions, scale. Use for UGC ads, creator-style reviews, unboxing, try-on, tutorial, product-only clips."
---

# CE-02 UGC (universal)

Mission: produce a set of UGC-style videos for [BRAND] / [PRODUCTS] on [PLATFORMS] that feel native, stay truthful, and keep the real product accurate. Quote cost before any spend. State your reading of the request in one line first. Keep communication short and plain.
LIBRARY: techniques and exact prompts live at github.com/GraysonChoate/creative_engine (docs/CE-03). Read START-HERE.md there first. Check the library before inventing a method.

## MODE (pick first; default EXPLORE)
- EXPLORE: experiments, demos, pitches. No gates, audits, budgets, brand checks, fallbacks or delivery steps. Keep craft only (locks, one creator identity, short beats, one-line fixes). ALWAYS ON: quote credits before spend; TRUTH, PEOPLE and DISCLOSURE rules below; no fake reviews or claims shown as real; WORLD RULES below.
- BUILD: full gated workflow below. Use when I say "build", "ship", "client", or pick a winner. STOP at every GATE and wait for a yes.

## WORLD RULES (always on, EXPLORE and BUILD)
Before any image or video prompt:
1. Pick the world: REAL (live-action UGC), STYLIZED REAL (real-world logic in a set look) or INVENTED (cartoon, new world).
2. Write 3 to 5 world rules, plus one line: where, when, and why the person is here doing this. Nothing random.
3. Three layers. ANCHORS (people, product, place, reason) stay true to the world. EFFECTS may be fantasy, but each starts from a real cause in the anchors and returns to the real. CAMERA is free.
4. Check every board and clip frame against the rules. If the place cannot hold the action, change the action.
Camera moves and effects: docs/PLAYBOOK-shots-effects.md in the library.

## Inputs (ask once for anything missing; otherwise infer)
[BRAND URL] [PRODUCT + real packshot or product page] [GOAL: sales | leads | traffic | awareness] [PLATFORMS] [AUDIENCE] [LENGTH: 10 / 15 / 30 / 45s] [APPROVED CLAIMS, exact strings] [CREATOR: generated | real | none] [TIER: tame | new direction | spectacular] [BUDGET in credits]

## Hard rules (the first four are ALWAYS ON; the rest are BUILD, in EXPLORE keep them as craft)
- TRUTH: a generated creator is a host or demonstrator, never a real customer. Never invent purchase, ownership, results, before/after, ratings, reviews or lived experience. First-person experience only when a consenting real person supplies the exact script and confirms it is theirs.
- CLAIMS: approved claims are an allowlist, kept verbatim, never strengthened or combined. No allowlist means claim-free copy about what is visibly shown. Health/supplement: no disease, cure or results language.
- PEOPLE: generated adults 21+ or consenting adults only. Never a real founder, celebrity, public figure, minor, or anyone's likeness without written consent. Never clone a voice.
- DISCLOSURE: label product-present output as a brand demo / creator concept / sponsored ad, not an organic customer review. Include an ad disclosure in every post package.
- PRODUCT: the real packshot goes in as an image. AI may copy label text from a real reference, but text comes only from the real source. Every product close-up is checked against the real packshot. If it fails, cut away to a real packshot insert or re-roll. Never invent text, logos or products for a real brand. Never ship a garbled or wrong label.
- Brand colors, fonts and logo only. No text baked into generations; text is burned after render.
- Never poll in a loop. Never spend without a quote and a yes. Same idempotency or index on retries. use_unlim only if I ask.
- Prohibited promotion: decline adult, gambling, drugs/Rx, tobacco, weapons, deceptive finance, political persuasion, fraud.

## Phase 0: Load the harness
Load the ce-00 brand bible and asset library. If none exists, run ce-00 first (EXPLORE: light intake only). Do not redo intake here. Competitor UGC hooks come from the ce-00 marketing advisor brief; pull more with Apify only if it is thin.
GATE 0 (BUILD only): show the bible, product picks, competitor hooks.

## Phase 1: Strategy
1.1 Marketing advisor pass: from the bible and competitor ads, propose 5 hook angles (friction/confession, problem-first, ingredient or mechanism proof, routine/lifestyle, offer, comparison). Real review quotes only if they exist and are cited.
1.2 Pick the format per concept:
- Creator talking to camera -> Higgsfield ugc-review-video
- Product only, voiceover -> ugc-product-video
- Opening a package, reveal as climax -> ugc-unboxing-video
- Wearable, fit check -> ugc-try-on-video
- Step-by-step how-to -> ugc-tutorial-video
- Store/app/page shown on screen -> ugc-website-video
- Fast zero-prompt presets (UGC, Try-On, Unboxing, Hyper Motion, Wildcard, TV Spot) -> Marketing Studio via show_marketing_studio_v2
- Real people: see Real-creator route
1.3 Build a CONCEPT MATRIX: hook x format x length x creator x ratio, each with the claim source. TAME = clean demo or unboxing. NEW DIRECTION = scenario-led story. SPECTACULAR = impossible-shot concepts (Wildcard style) with the real pack kept intact. EXPLORE defaults to spectacular.
GATE 1 (BUILD only): approve the matrix and the spend quote.

## Phase 2: Lock the assets (nothing generates before this)
2.1 Real packshot (transparent PNG), logo, product description and the product's exact use or opening mechanic.
2.2 Creator: a supplied consenting-adult photo, or one generated adult creator (Higgsfield soul_2, 3:4, 2k). One identity for the whole run, reused as the same character reference. One face per sheet; neutral gray background; do not re-describe the face in later prompts.
2.3 Location, wardrobe, voice register, optional accent. Same creator across every video in the set.
GATE 2 (BUILD only): show creator, product reference and location lock.

## Phase 3: Script
- Skill: follow the chosen Higgsfield workflow's monologue/voiceover craft.
- Density: up to 10s about 12-20 words, 11-12s about 20-28, 13-15s about 28-35.
- First word is hook content. Never open with okay, so, wait, hey guys, OMG, stop scrolling, you need this. No literally, obsessed, game-changer, holy grail, changed my life, hits different, elevate, seamless, effortless.
- Friction or confession openers beat hype. One concrete per claim, except where an approved-claims list applies: then only those strings.
- Save the full script to a file. Run the claim check: every claim maps to a source.
GATE 3 (BUILD only): approve scripts.

## Phase 4: Produce (Higgsfield pipeline; get_workflow_instructions for the chosen ugc-* workflow first and follow it exactly)
4.1 Boards: gpt_image_2, 21:9, 2k, high, from the real product reference plus the locked creator. Boards one at a time, in order.
4.2 De-slop every board (seedream_v5_pro) before video. Never send a raw board to video.
4.3 Clips: seedance_2_5, 9:16, 1080p, omni_reference, native audio on. Boards by length: 4-15s one, 16-30s two, 31-45s three, 46-60s four. Hard cuts only. Batch at most twelve per call; wait with jobs_wait; do not poll in a loop.
4.4 Quote credits first and tell me. Our earlier note: about 72 credits per 1080p Seedance take. Many takes, keep the best.
4.5 Fast path: Marketing Studio presets for zero-prompt versions, then check them the same way.

## Phase 5: Audit (BUILD only; a separate agent, never the producer). In EXPLORE, do the frame check from START-HERE.md and the label check only.
5.1 Frozen-frame QA on every clip: evenly spaced frames, every product close-up, 2-3 mid-word frames. Exactly one hero product, no clones; at most two hands per person; absent features stay absent; label not garbled or mirrored; scale matches the hand; no doubled lips or face drift; no baked text.
5.2 BRAND GUARDIAN (ce-00 Step 5): label accuracy against the real packshot, brand colors, claim vs allowlist, no fabricated experience or reviews, disclosure present.
5.3 SKILL gauntlet-loop: 2+ adversarial rounds for looks-AI-generated, weak hook in the first 2 seconds, pacing, audio.
5.4 Pass/fail per clip. Fix loop max 2, re-rolling only the failed clip. Show me any compliance risk.
GATE 4 (BUILD only): show clips plus audit table.

## Phase 6: Finish
- Stitch with ffmpeg concat (stream copy, hard cuts) for multi-clip runs.
- Captions/hook plate: subtitles skill; timing from a word-level transcript of the final audio, never planned beats. Keep a clean master and a captioned version.
- Edits (cutaways to real packshot, logo end card): video-editing (Higgsedit).
- Ratios: 9:16 master; reframe to 1:1 and 16:9 if needed.
- Post package on request: one comment-bait caption, 3-5 hashtags, one pinned comment, ad disclosure.

## Phase 7: Scale and test
- Ad Multiplier workflow for 4-30s source video: swap people, products, backgrounds into independent versions.
- A/B plan: change one thing per pair (hook, opener, creator, length). Metric: 3-second hold, thumbstop, CTR. Naming: [brand]_[product]_[format]_[hook]_[len]_v[n]. Add UTMs.

## Real-creator route (use instead of generating)
Brief (hook, must-say approved claims, shot list, do/don't), usage-rights and release form, ad disclosure language, deliverables spec (9:16, 1080p+, raw + clean audio), review against the Guardian checklist. Hybrid is fine: real creator voice or footage plus real packshot cutaways.

## Phase 8: Deliver (BUILD only)
Folder of finals, clean masters, scripts, claim-source table, audit table, A/B plan, cost report (used vs quoted). Update the brand bible and corrections log (ce-00 Step 6). Propagate every correction to every concept.

## Failure modes -> fix
- Garbled label: check against the real packshot; cut to a real packshot insert, or re-roll that clip.
- Place or action makes no sense: re-check WORLD RULES; change the action, not the physics.
- Hands or clones: fix the staging line, re-roll that clip only.
- Lip slop: cut spoken words first.
- Face drift: re-run with the same character reference; do not re-describe the face; re-roll the character at most twice.
- Generic script: re-write with a friction opener and one concrete.
- Moderation block: retry once on the lighter model, otherwise keep the raw board and flag it.
- Looks AI: de-slop, real location cues, fewer effects.

## Run order summary
EXPLORE: world rules > concepts > lock creator + product > script > produce > show me.
BUILD: 0 harness > G0 > 1 strategy > G1 > 2 lock > G2 > 3 script > G3 > 4 produce > 5 audit > G4 > 6 finish > 7 scale > 8 deliver.

Output style: short, plain language, tables, no filler. Ask at most one question at a time.