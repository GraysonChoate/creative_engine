---
name: "ce-04-homepage"
description: "Universal master workflow for building or rebuilding a brand's homepage: audit, section plan, design boards, asset lock, tiered build (tame, new direction, spectacular), audit and delivery. Brand-agnostic."
---

> Load ce-core first. Always on: quote credits before spend (model, why, total; re-quote if anything changes); real label only (text from the real source, checked against the real image, small print included); real brand text (name, price, CTA, claims) is set in code or checked letter by letter against the source; real people and voices are fine when the user says the person or client approved (note it once in the brief, never re-ask); no fake reviews, claims or results shown as real; world rules before any prompt; a connector (Apify, ElevenLabs, Firecrawl, Higgsfield, Chrome) is never "missing" until ToolSearch has looked for it (ce-core section 14 TOOL CHECK).

# CE-04 HOMEPAGE BUILD
Version 2.7 (2026-10-14).

Run this when the job is ONE page: the homepage (hero, motion, sections, conversion flow). For a whole site, use ce-05.
Brand-agnostic. Every brand detail is a variable: [BRAND], [PRODUCT], [AUDIENCE], [GOAL].
Mode, always-on rules, world rules, gates, fix order, shared failures, contingencies, library: see ce-core. Which model: ce-core section 1. Roles, prices, specs: ce-core section 14.
Camera moves and effects: docs/PLAYBOOK-shots-effects.md. Hero motion, type reveals, loops and frame sequences built in After Effects: ce-core FINISH LAYER, docs/AE-route.md.
Which layer makes each element (Higgsfield, After Effects, code), elevate defined, 3D product, scroll film, transitions: library/web-motion.md. READ IT on every run.
Mode note: in EXPLORE every phase below still runs; the gates are show-and-go (ce-core section 2). A prompt that pre-decides sections, copy or look is input to the phase, not a reason to skip it.

## INPUTS (ask once, in plain words, only what is missing)
- BRAND: URL or brand bible (from ce-00).
- GOAL: sales | leads | launch | story. Pick one primary.
- TIER: tame | new-direction | spectacular. EXPLORE defaults to spectacular. If unsure in BUILD, build all three boards, then ask. Spectacular can be used on any section or page the user chooses.
- STACK: Shopify | other | none (preview only).
- DELIVERY: prototype link | production build | both.
- ASSETS: what the client already has (packshots, logo, photos, video).

## PAGE RULES
1. Brand palette and fonts only (BUILD). Placeholders and off-palette colors exist in dev only, never in client-facing output.
2. One primary conversion path. One primary CTA per screen.
3. Slow, deliberate motion. No bobbing. Motion either shows the product or opens information.
4. Storyboard first: boards -> prototype -> production. Never jump to a finished page.
5. Never use git/deploy jargon with the user.

## PHASE 0: HARNESS
- Load the brand bible from ce-00. If none exists, run ce-00 first (EXPLORE: light intake only). Do not rebuild it here.
- AUDIT the existing homepage (Claude in Chrome or Firecrawl screenshot, desktop + phone): nav depth, hero clarity, product count, load weight, CTA count, mobile problems. Write a keep / fix / cut list. Keep what already works.
- BRAND MATERIAL FIRST: every real video, photo, label art and lifestyle image on the site is downloaded and listed BEFORE any world is imagined. A video that renders as a poster is still a video: fetch its source URL and frame it. Cutting real brand footage is a Phase 0 failure.
- WORLD INVENTORY: list every visual world the site already uses (each hero banner, each campaign image: subject, setting, ingredient, color, mood). These are the raw material for elevate. Save the screenshots. Nothing in the build may replace these worlds with a generic one.
- Marketing advisor step: look at 3-5 competitor or best-in-niche homepages (Refero, Mobbin, Awwwards, or the user's references). Note what to match and what to beat. One line each.
- Asset request: send the client a checklist of what is missing (hi-res packshots, label art, lifestyle shots, brand video, fonts).
PLAN gate (BUILD only): bible loaded, audit done, asset list agreed. Stop if the bible is missing claims or colors.

## PHASE 1: STRATEGY AND SECTION PLAN
- One-line concept spine: what the page says in one sentence.
- STORY LINE PER SECTION: one sentence each. Every element in the section (world, photo, product, price, copy, motion) must trace to that sentence (library/web-motion.md 2b). The world is built out from the brand's real element in that section, never chosen first.
- LAYER CONTRACTS: one per hand-off between film, 3D and type (library/web-motion.md 2e), written here, before any clip is quoted.
- SHOP FIRST: it is a store. A visitor sees a product, its price, its rating and a way to buy within the first two screens. Ratings, badges and compare-at prices that exist on the real site stay.
- Trim to 3-5 flagship products. Everything else lives one click deeper.
- Navigation: one sticky nav, 5 items max, one CTA.
- Section plan (default, adjust to GOAL): Hero > proof strip > flagship products > how it works / benefits > social proof (real only) > secondary offer > footer. One job per section.
- Optional dual-state toggle (e.g. two product pillars) only if the brand has two clear pillars. Toggle changes copy, color accent, product and price together.
- CTA inventory: list every button and where it goes.
- ELEMENT ROUTING TABLE (library/web-motion.md section 1): one row per element: element | section | visitor does (watch / scroll / touch / read) | layer (Higgsfield / After Effects / code) | source file. Default: one real-3D showcase where the visitor picks a product, film everywhere else, code for every transition and all text. No element is built without a row. Show the table at the PLAN gate.
- CONSOLIDATION: for each section of the old page say keep, merge, or cut, and where its content goes. The old page's worlds (Phase 0 inventory) are reassigned, not dropped: a banner world that loses its hero slot becomes a section backdrop or a tab world.
- Copy: headlines and body from the brand voice and approved claims. Mark any new line as DRAFT for client sign-off.
PLAN gate (BUILD only): user approves concept, section plan and CTA inventory.

## PHASE 2: DESIGN BOARDS
- One board image per section, desktop + phone, in the locked palette and type. Plus a NAV board and a COMPONENT SHEET (tabs, pills, cards, buttons, every state) (web-motion 2f).
- Tools: board models (ce-core section 14) for mood and layout; real pack images as references or composited in. Or Canva (generate-design, resize-design) for layout boards.
- Produce the tier(s) asked for. Same inputs, three looks:
  - TAME: clean, fast, static + light reveals. Safe default for BUILD.
  - NEW DIRECTION: new layout and imagery, moderate motion, same brand rules.
  - SPECTACULAR: scroll film, 3D, shader transitions. Use where the user wants it (any section or page); in BUILD keep the weight budget for that page.
- Contact sheet of boards to the user.
LOOK gate (BUILD only): user picks the tier and approves the boards. Lock palette, fonts, spacing, section order.

## PHASE 3: ASSET LOCK
- Product sheet per flagship: front + 3/4, real label. Remove backgrounds (remove_background) or use client cutouts.
- Hero media: atmosphere loop (video model, seamless with first frame = last frame, 1080p, 5-10s) or still. Product stays a real image or real label render.
- Scroll film tier: asset request = one timed world per scroll section, start/end frames per scene, occlusion transitions between sections, frame sequence on canvas (or short video export), per-frame product tracking so packs sit on surfaces. In BUILD, state mobile weight limits before generating.
- 3D tier: Three.js with real label renders unwrapped onto the real silhouette. Do not use AI-generated 3D for labels. No outside 3D artist needed.
- Optimize (BUILD): WebP/AVIF images, video under 3 MB loops, poster frame for each video, local fonts.
ASSETS gate (BUILD only): every asset is a file, named, and checked against the bible. No video prompt or build step before this.

## PHASE 4: BUILD (pick a route)
ROUTE A: Prototype (fast, always first)
- Claude writes one HTML + Tailwind file from the boards. Mobile first. Review on phone width.
ROUTE B: Production (code)
- Hand-built: HTML/CSS/JS or the client's framework. GSAP + ScrollTrigger + Lenis for scroll. Three.js for 3D. GLSL shaders for transitions (spectacular tier). IntersectionObserver pauses video/WebGL off-screen. Reduced-motion fallback. Pause control for autoplay video.
ROUTE C: Higgsfield website builder (when the client has no site stack and wants a hosted result)
- get_workflow_instructions("website-builder-flow"), create_website type "website", ask Animated vs Non-animated. Follow its phases: design brief, boards, asset kit, build, motion, mechanical check, deploy. Publish only when the user says so.
ROUTE D: Shopify
- Output sections as theme-ready code. Quick-add hooks use real variant IDs from products.json. Do not touch the live theme without explicit approval.
- Build in stages: nav + hero > sections > motion > commerce. Review each stage.

## PHASE 4b: CRAFT GATE (both modes, before any frame goes to the user)
Measure, do not eyeball: web-motion 2c (grid, nav, type, spacing, components, colour, images), 2e side-by-side sheets for every hand-off against the contracts, 2f legibility, occlusion, scroll-efficiency and nav reports, 2g interaction walk (every clickable state screenshotted, every seam scrolled), 2h SELF-AUDIT.md (the scored standard; a FAIL is fixed or explained before the freeze). Then the real-scroll recording with the dead-air report (2d). Only then show the user.

## PHASE 5: AUDIT (BUILD only; separate agent, not the builder)
Brand Guardian checks, pass/fail:
- Colors and fonts match the bible. Labels match real packs. Claims are on the approved list. Tone matches voice.
Critic loop (gauntlet-loop skill, 2+ rounds, max 2 fix loops):
- Phone check at 390px and 768px. No horizontal scroll. Tap targets 44px.
- Hero readable in 3 seconds. One CTA per screen.
- Performance: LCP under 2.5s on mid phone, total weight budget (tame < 1.5 MB, new direction < 3 MB, spectacular < 6 MB initial).
- Accessibility: contrast 4.5:1, alt text, keyboard focus, reduced motion, muted autoplay.
- Motion: no jank, no layout shift, nothing floats, scroll never traps.
- Links and forms work. Metadata and share image present.
FAIL = fix and re-run. Never ship on a fail.

## PHASE 6: DELIVERY (BUILD only)
- Preview link (artifact or hosted build) + screenshots desktop and phone.
- Hand over: files or repo, asset folder, section/CTA map, copy marked DRAFT, change list vs the old page, performance numbers.
- Cost report (credits spent by step). Next-step offer: A/B variants, or run ce-05 for the full site.
- Save to memory: approved tier, palette, fonts, copy decisions, corrections.

## EXTRA FAILURE MODES (shared ones are in ce-core)
| Problem | Fix |
|---|---|
| Heavy page, slow phone | Compress, lazy-load, pause video off-screen, drop to lower tier. |
| Too busy | Cut sections. One job each. |
| Motion feels gimmicky | Slow it down. Remove anything that does not show product or open info. |
| Drift between boards and build | Rebuild from the locked boards, not memory. |

## RUN ORDER SUMMARY
EXPLORE: 0 brand material + audit + world inventory + references > 1 story lines + plan + routing table (show) > 2 boards (show) > 3 asset lock (show, quote) > 4 build > 4b craft gate + real-scroll recording (show) > gauntlet. Gates are show-and-go. No separate audit agent, weight budget or delivery.
BUILD: 0 harness (ce-00) + audit > PLAN > 1 strategy > PLAN > 2 boards > LOOK > 3 assets > ASSETS > 4 build (prototype first) > 5 audit > 6 deliver.
Time: tame 1 day, new direction 2-3 days, spectacular 4-7 days. Credits: boards low, atmosphere loops moderate, scroll film high. Always quote first.
