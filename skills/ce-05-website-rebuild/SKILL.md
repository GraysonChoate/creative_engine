---
name: "ce-05-website-rebuild"
description: "Universal master workflow for rebuilding a brand's full website: audit, sitemap, design system, page templates, build, migration, QA, launch and handoff. Brand-agnostic."
---

# CE-05 FULL WEBSITE REBUILD

Run this when the job is the WHOLE site (audit -> design -> code -> QA -> handoff). Homepage only? Use ce-04. This skill reuses ce-04 for the homepage step.
Brand-agnostic. Variables: [BRAND], [PRODUCT], [AUDIENCE], [GOAL].

## MODE (pick first; default EXPLORE)
- EXPLORE: experiments, demos, pitches. No gates, audits, weight budgets, brand checks, fallbacks or delivery steps. Keep craft only (locks, previews, loops, lighting, short beats, one-line fixes). ALWAYS ON: quote credits before spend; no real person's likeness without consent; no fake reviews or claims shown as real; no touching a live site or DNS; no credentials.
- BUILD: full gated workflow below. Use when I say "build", "ship", "client", or pick a winner.

## WORLD RULES (always on, EXPLORE and BUILD)
Before any image or video prompt:
1. Pick the world: REAL (live-action brand ad), STYLIZED REAL (painted, anime: real-world logic in a set look) or INVENTED (cartoon, new world).
2. Write 3 to 5 world rules, plus one line: where, when, and why the person is here doing this. Nothing random.
3. Three layers. ANCHORS (people, product, place, reason) stay true to the world. EFFECTS may be fantasy, but each starts from a real cause in the anchors (she opens the bottle, the liquid swirls) and returns to the real. CAMERA is free (macro zoom, sky drop, thread-level close-up).
4. Check every storyboard frame against the rules. If the place cannot hold the action, change the action.

## INPUTS (ask once, only what is missing)
- SITE: current URL (or none for a new site).
- GOAL: sales | leads | bookings | content | brand. One primary.
- PLATFORM: Shopify | WordPress | custom code | Higgsfield-hosted | undecided.
- SCOPE: page count, must-keep URLs, languages.
- TIER: tame | new-direction | spectacular. Set per page or per section, as the user chooses. Spectacular can run on any page, including the whole site, if the user wants it. Each page keeps its own weight budget (Phase 7).
- ACCESS: admin/theme access, analytics, Search Console, DNS owner. If none: prototype only.
- ASSETS: what exists (packshots, logo, photos, video, copy).

## HARD RULES (BUILD; in EXPLORE only the ALWAYS ON items apply)
1. Real packs, logos and photos go in as images. AI may copy label text from a real reference, but text comes only from the real source and every result is checked against the real image; if it fails, put the real label back or re-run. Never invent text, logos or products for a real brand. Prefer real images as references for new renders (light and shadow built in) over flat cutout composites; keep the cutout composite as backup when the label must be exact.
2. Text set in code. Brand palette and fonts only. Placeholders in dev only.
3. No invented claims, reviews, people, numbers. Claims from the approved list only.
4. NEVER break existing URLs. Every old URL gets a keep or a 301 redirect map. SEO traffic is protected first.
5. Never touch the live site or DNS without explicit approval. Build on staging/preview.
6. Prototype before production. One stage at a time, review each.
7. Quote before credit spend. Never poll jobs.
8. Do not claim a connector exists until a call succeeds. Fallback: screenshots, public feeds (products.json, sitemap.xml), file output.
9. No git/deploy jargon with the user.
10. Do not collect or enter credentials. User signs in; Claude never types passwords.

## PHASE 0: HARNESS + SITE AUDIT
- Brand bible: load the ce-00 bible. If none exists, run ce-00 first. Do not rebuild it here.
- Crawl the site: Firecrawl map + scrape (sitemap.xml, all URLs, titles, H1s, word counts, internal links, broken links).
- Screenshots desktop + phone (Claude in Chrome) of top pages.
- Pull analytics if given: top pages, traffic sources, conversion path, bounce, device split. If none, say so.
- Technical: page weight, LCP, mobile issues, accessibility, metadata, schema, redirects, forms, tracking pixels, apps/plugins.
- Output: AUDIT table (Page | Traffic | Purpose | Keep / Merge / Cut / New | Notes). Plus top 10 problems ranked by revenue impact.
- Marketing advisor: 3-5 competitor sites. What to match, what to beat.
GATE 0 (BUILD only): audit approved. Keep/merge/cut list agreed. Stop if SEO pages are not protected.

## PHASE 1: STRATEGY + SITEMAP
- Concept spine: one sentence.
- Sitemap: tree with page purpose, one primary CTA, and target keyword per page. Default: Home, Shop/Collections, Product template, About, Proof/Reviews (real only), Learn/Blog, Contact/FAQ, Legal.
- Nav: one sticky nav, 5 items max, one CTA. Footer carries the rest.
- User flows: top 2-3 journeys (e.g. land > product > cart). Count clicks. Fewer is better.
- Redirect map: old URL > new URL for every cut/merged page.
- Content plan: reuse existing copy where good; new copy marked DRAFT for client sign-off, claims checked.
GATE 1 (BUILD only): sitemap, flows, redirect map approved.

## PHASE 2: DESIGN SYSTEM
- Tokens: color, type scale, spacing, radius, shadow, motion (3 motion words, durations, easing).
- Components: nav, hero, product card, grid, accordion, review block, form, footer, buttons, badges.
- Boards: one per page TEMPLATE (not every page), desktop + phone. Tools: gpt_image_2_5 / nano_banana_pro / flux_3_image (Higgsfield) with real packs composited, or Canva generate-design.
- Three tiers from same inputs: TAME (clean, fast), NEW DIRECTION (new layout/imagery), SPECTACULAR (scroll film/3D/shaders; any page or section the user picks).
- Spectacular assets follow the core asset-request format: loop first frame = last frame; one timed world per scroll section; occlusion transitions between sections; frame-sequence or short video export; mobile weight limits stated up front.
GATE 2 (BUILD only): user picks tier, approves tokens + boards. Lock them.

## PHASE 3: HOMEPAGE
- Run ce-04-homepage Phases 1-5 using the locked system. Do not redo the audit or the brand intake.
GATE 3 (BUILD only): homepage approved on phone and desktop.

## PHASE 4: TEMPLATES + ASSET LOCK
- Build each template once: collection, product, article, about, contact. Pages are template + content.
- Asset lock: product sheets (front + 3/4, real label), lifestyle, OG/share images, icons. Optimize: WebP/AVIF, lazy-load, alt text written, local fonts.
- Optional per-page hero loops (Higgsfield, seamless, under 3 MB, poster frame). Quote first.
GATE 4 (BUILD only): every asset is a named file. Nothing generated shows a label or text.

## PHASE 5: BUILD (pick a route)
ROUTE A: Prototype (always first). Claude builds a clickable static site (HTML + Tailwind), mobile first. Shareable preview link.
ROUTE B: Shopify. Theme sections/templates, real variant IDs from products.json, quick-add, cart. Work in a duplicate/dev theme only. Never publish the theme without approval.
ROUTE C: Custom code. Framework of the client's choice. SSR-safe, no top-level window use. GSAP + ScrollTrigger + Lenis for scroll, Three.js for 3D, IntersectionObserver to pause heavy media, reduced-motion fallback.
ROUTE D: Higgsfield hosted. get_workflow_instructions("website-builder-flow"), create_website type "website", ask Animated vs Non-animated. Follow its phases. Publish only on request.
- Stage order: global (nav/footer/tokens) > homepage > templates > content pages > forms/tracking > SEO.
- SEO build: titles, meta, H1 per page, schema (Product, Organization, FAQ), sitemap.xml, robots.txt, canonical, OG/cover image, 301 map implemented.
- Integrations: analytics, pixels, email capture, reviews app. Re-use existing IDs. Do not enter keys; user adds them.

## PHASE 6: MIGRATION (BUILD only)
- Content move: products, collections, posts, images, metafields. Verify counts match (old vs new).
- Redirects live on staging. Test 100% of top-traffic URLs and a sample of the rest.
- Freeze window: tell client when edits stop on the old site.

## PHASE 7: AUDIT (BUILD only; separate agent, not the builder)
Brand Guardian pass/fail: colors, fonts, labels, claims, tone, no placeholders.
Critic loop (gauntlet-loop, 2+ rounds, max 2 fix loops):
- Phone 390px + 768px + desktop. No horizontal scroll. Tap targets 44px.
- Every link and form works. Cart/checkout path completes on staging.
- Redirects: no chains, no 404s on old top URLs.
- Performance: LCP under 2.5s on mid phone; weight budget per page: tame <1.5 MB, new direction <3 MB, spectacular <6 MB initial. Check every page against its own tier.
- Accessibility: contrast 4.5:1, alt text, keyboard focus, reduced motion.
- SEO: unique title/H1 per page, schema valid, sitemap submitted-ready, no noindex left on.
- Tracking fires once, not twice.
FAIL = fix and re-run. Never launch on a fail.

## PHASE 8: LAUNCH + HANDOFF (BUILD only)
- Launch checklist (user approves each): freeze > final migration > swap domain/theme > verify redirects > submit sitemap > watch 404s + analytics 48h.
- Rollback plan written before launch: how to restore the old site in minutes.
- Hand over: source/theme, design system doc, sitemap + redirect map, asset folder, copy marked DRAFT, how-to-edit guide (plain language), performance before/after, cost report.
- Save to memory: tier, tokens, decisions, corrections, open items.
- Next-step offer: ce-01 image ads and ce-03 animated ads using the new site's look.

## FAILURE MODES AND FIXES
| Problem | Fix |
|---|---|
| Traffic drop after launch | Check redirect map, titles/H1s kept, canonicals, noindex. |
| Scope creep | Templates first. New pages go to a Phase 2 backlog. |
| Label warps or text garbles | Check against the real image; put the real label back or re-run. |
| Off-brand drift between pages | Rebuild from tokens, re-run Guardian. |
| Slow pages | Compress, lazy-load, remove apps/scripts, drop that page's motion tier. |
| Missing access | Ship prototype + handoff pack, say what is blocked. |
| Connector missing | Use crawl, screenshots, public feeds. Say so. |
| Client keeps changing boards | Gate 2 lock. Changes after = new scope, logged. |

## RUN ORDER SUMMARY
EXPLORE: boards > prototype on spectacular tier > show me. No audit, sitemap, migration or budgets.
BUILD: 0 audit (ce-00 bible) > G0 > 1 sitemap > G1 > 2 design system > G2 > 3 homepage (ce-04) > G3 > 4 templates + assets > G4 > 5 build (prototype first) > 6 migrate > 7 audit > 8 launch + handoff.
Time: 1-2 weeks small site, 3-5 weeks 30+ pages. Credits: boards low, loops moderate. Always quote first.