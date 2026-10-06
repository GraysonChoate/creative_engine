---
name: "ce-04-homepage"
description: "Universal master workflow for building or rebuilding a brand's homepage: audit, section plan, design boards, asset lock, tiered build (tame, new direction, spectacular), audit and delivery. Brand-agnostic."
---

# CE-04 HOMEPAGE BUILD

Run this when the job is ONE page: the homepage (hero, motion, sections, conversion flow). For a whole site, use ce-05.
Brand-agnostic. Every brand detail is a variable: [BRAND], [PRODUCT], [AUDIENCE], [GOAL].

## MODE (pick first; default EXPLORE)
- EXPLORE: experiments, demos, pitches. No gates, audits, weight budgets, brand checks, fallbacks or delivery steps. Keep craft only (locks, previews, loops, lighting, short beats, one-line fixes). ALWAYS ON: quote credits before spend; no real person's likeness without consent; no fake reviews or claims shown as real; no touching a live site or DNS; no credentials.
- BUILD: full gated workflow below. Use when I say "build", "ship", "client", or pick a winner.

## INPUTS (ask once, in plain words, only what is missing)
- BRAND: URL or brand bible (from ce-00).
- GOAL: sales | leads | launch | story. Pick one primary.
- TIER: tame | new-direction | spectacular. If unsure, build all three boards, then ask. Spectacular can be used on any section or page the user chooses.
- STACK: Shopify | other | none (preview only).
- DELIVERY: prototype link | production build | both.
- ASSETS: what the client already has (packshots, logo, photos, video).

## HARD RULES (BUILD; in EXPLORE only the ALWAYS ON items apply, plus rule 9 as craft)
1. Real packs, logos and photos go in as images. AI may copy label text from a real reference, but text comes only from the real source and every result is checked against the real image; if it fails, put the real label back or re-run. Never invent text, logos or products for a real brand. Prefer real images as references for new renders (light and shadow built in) over flat cutout composites; keep the cutout composite as backup when the label must be exact.
2. Text is set in code. Never baked into generated images.
3. Brand palette and fonts only. Placeholders and off-palette colors exist in dev only, never in client-facing output.
4. No invented claims, reviews, testimonials, people or numbers. Claims come only from the brand bible's approved list.
5. One primary conversion path. One primary CTA per screen.
6. Slow, deliberate motion. No bobbing. Motion either shows the product or opens information.
7. Storyboard first: boards -> prototype -> production. Never jump to a finished page.
8. Quote before any credit spend. Never poll; wait on jobs once.
9. Products sit exactly on surfaces (shadows, contact, scale). Floating = fail.
10. Do not claim a connector exists until a call succeeds. Figma, GitHub, Vercel and Shopify connectors may be missing; fall back (screenshots, public products.json, file output).
11. Never use git/deploy jargon with the user.

## PHASE 0: HARNESS
- Load the brand bible from ce-00. If none exists, run ce-00 first. Do not rebuild it here.
- AUDIT the existing homepage (Claude in Chrome or Firecrawl screenshot, desktop + phone): nav depth, hero clarity, product count, load weight, CTA count, mobile problems. Write a keep / fix / cut list. Keep what already works.
- Marketing advisor step: look at 3-5 competitor homepages. Note what to match and what to beat.
- Asset request: send the client a checklist of what is missing (hi-res packshots, label art, lifestyle shots, brand video, fonts).
GATE 0 (BUILD only): bible loaded, audit done, asset list agreed. Stop if the bible is missing claims or colors.

## PHASE 1: STRATEGY AND SECTION PLAN
- One-line concept spine: what the page says in one sentence.
- Trim to 3-5 flagship products. Everything else lives one click deeper.
- Navigation: one sticky nav, 5 items max, one CTA.
- Section plan (default, adjust to GOAL): Hero > proof strip > flagship products > how it works / benefits > social proof (real only) > secondary offer > footer. One job per section.
- Optional dual-state toggle (e.g. two product pillars) only if the brand has two clear pillars. Toggle changes copy, color accent, product and price together.
- CTA inventory: list every button and where it goes.
- Copy: headlines and body from the brand voice and approved claims. Mark any new line as DRAFT for client sign-off.
GATE 1 (BUILD only): user approves concept, section plan and CTA inventory.

## PHASE 2: DESIGN BOARDS
- One board image per section, desktop + phone, in the locked palette and type.
- Tools: gpt_image_2_5 / nano_banana_pro / flux_3_image (via Higgsfield) for mood and layout; real pack images composited in. Or Canva (generate-design, resize-design) for layout boards.
- Produce the tier(s) asked for. Same inputs, three looks:
  - TAME: clean, fast, static + light reveals. Safe default.
  - NEW DIRECTION: new layout and imagery, moderate motion, same brand rules.
  - SPECTACULAR: scroll film, 3D, shader transitions. Use where the user wants it (any section or page); keep the weight budget for that page.
- Contact sheet of boards to the user.
GATE 2 (BUILD only): user picks the tier and approves the boards. Lock palette, fonts, spacing, section order.

## PHASE 3: ASSET LOCK
- Product sheet per flagship: front + 3/4, real label. Remove backgrounds (remove_background) or use client cutouts.
- Hero media: atmosphere loop (Higgsfield video, seamless with first frame = last frame, 1080p, 5-10s) or still. Product stays a real image or real label render.
- Scroll film tier: asset request = one timed world per scroll section, start/end frames per scene, occlusion transitions between sections, frame sequence on canvas (or short video export), per-frame product tracking so packs sit on surfaces. State mobile weight limits before generating.
- 3D tier: Three.js with real label renders unwrapped onto the real silhouette. Do not use AI-generated 3D for labels. No outside 3D artist needed.
- Optimize: WebP/AVIF images, video under 3 MB loops, poster frame for each video, local fonts.
GATE 3 (BUILD only): every asset is a file, named, and checked against the bible. No video prompt or build step before this.

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

## FAILURE MODES AND FIXES
| Problem | Fix |
|---|---|
| Label warps or text garbles | Check against the real image; use the real label render or re-run. |
| Product floats | Add contact shadow, match perspective, per-frame tracking. |
| Off-brand color | Re-lock palette tokens. Re-run Guardian. |
| Heavy page, slow phone | Compress, lazy-load, pause video off-screen, drop to lower tier. |
| Too busy | Cut sections. One job each. |
| Motion feels gimmicky | Slow it down. Remove anything that does not show product or open info. |
| Connector missing | Use screenshots, products.json, file output. Say so. |
| Drift between boards and build | Rebuild from the locked boards, not memory. |

## RUN ORDER SUMMARY
EXPLORE: boards > prototype (spectacular by default) > show me. No audit, weight budget or delivery.
BUILD: 0 harness (ce-00) + audit > G0 > 1 strategy > G1 > 2 boards > G2 > 3 assets > G3 > 4 build (prototype first) > 5 audit > 6 deliver.
Time: tame 1 day, new direction 2-3 days, spectacular 4-7 days. Credits: boards low, atmosphere loops moderate, scroll film high. Always quote first.