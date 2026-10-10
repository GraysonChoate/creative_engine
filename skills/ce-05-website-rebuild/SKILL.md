---
name: "ce-05-website-rebuild"
description: "Universal master workflow for rebuilding a brand's full website: audit, sitemap, design system, page templates, build, migration, QA, launch and handoff. Brand-agnostic."
---

> Load ce-core first. Always on: quote credits before spend (model, why, total; re-quote if anything changes); real label only (text from the real source, checked against the real image, small print included); real brand text (name, price, CTA, claims) is set in code or checked letter by letter against the source; real people and voices are fine when the user says the person or client approved (note it once in the brief, never re-ask); no fake reviews, claims or results shown as real; world rules before any prompt.

# CE-05 FULL WEBSITE REBUILD

Run this when the job is the WHOLE site (audit -> design -> code -> QA -> handoff). Homepage only? Use ce-04. This skill reuses ce-04 for the homepage step.
Brand-agnostic. Variables: [BRAND], [PRODUCT], [AUDIENCE], [GOAL].
Mode, always-on rules, world rules, gates, fix order, shared failures, contingencies, library: see ce-core. Which model: ce-core section 1. Roles and prices: ce-core/TOOLS.md.
Camera moves and effects: docs/PLAYBOOK-shots-effects.md. Page motion built in After Effects (loops, Lottie, frame sequences): the After Effects layer.

## INPUTS (ask once, only what is missing)
- SITE: current URL (or none for a new site).
- GOAL: sales | leads | bookings | content | brand. One primary.
- PLATFORM: Shopify | WordPress | custom code | Higgsfield-hosted | undecided.
- SCOPE: page count, must-keep URLs, languages.
- TIER: tame | new-direction | spectacular. EXPLORE defaults to spectacular. Set per page or per section, as the user chooses. Spectacular can run on any page, including the whole site, if the user wants it. In BUILD each page keeps its own weight budget (Phase 7).
- ACCESS: admin/theme access, analytics, Search Console, DNS owner. If none: prototype only.
- ASSETS: what exists (packshots, logo, photos, video, copy).

## SITE RULES
1. Brand palette and fonts only (BUILD). Placeholders in dev only.
2. NEVER break existing URLs. Every old URL gets a keep or a 301 redirect map. SEO traffic is protected first.
3. Never touch the live site or DNS without explicit approval. Build on staging/preview.
4. Prototype before production. One stage at a time, review each.
5. No git/deploy jargon with the user.
6. Do not collect or enter credentials. User signs in; Claude never types passwords.
7. Do not claim a connector exists until a call succeeds. Fallback: screenshots, public feeds (products.json, sitemap.xml), file output.

## PHASE 0: HARNESS + SITE AUDIT
- Brand bible: load the ce-00 bible. If none exists, run ce-00 first (EXPLORE: light intake only). Do not rebuild it here.
- Crawl the site: Firecrawl map + scrape (sitemap.xml, all URLs, titles, H1s, word counts, internal links, broken links).
- Screenshots desktop + phone (Claude in Chrome) of top pages.
- Pull analytics if given: top pages, traffic sources, conversion path, bounce, device split. If none, say so.
- Technical: page weight, LCP, mobile issues, accessibility, metadata, schema, redirects, forms, tracking pixels, apps/plugins.
- Output: AUDIT table (Page | Traffic | Purpose | Keep / Merge / Cut / New | Notes). Plus top 10 problems ranked by revenue impact.
- Marketing advisor: 3-5 competitor sites. What to match, what to beat.
PLAN gate (BUILD only): audit approved. Keep/merge/cut list agreed. Stop if SEO pages are not protected.

## PHASE 1: STRATEGY + SITEMAP
- Concept spine: one sentence.
- Sitemap: tree with page purpose, one primary CTA, and target keyword per page. Default: Home, Shop/Collections, Product template, About, Proof/Reviews (real only), Learn/Blog, Contact/FAQ, Legal.
- Nav: one sticky nav, 5 items max, one CTA. Footer carries the rest.
- User flows: top 2-3 journeys (e.g. land > product > cart). Count clicks. Fewer is better.
- Redirect map: old URL > new URL for every cut/merged page.
- Content plan: reuse existing copy where good; new copy marked DRAFT for client sign-off, claims checked.
PLAN gate (BUILD only): sitemap, flows, redirect map approved.

## PHASE 2: DESIGN SYSTEM
- Tokens: color, type scale, spacing, radius, shadow, motion (3 motion words, durations, easing; from bible section 13).
- Components: nav, hero, product card, grid, accordion, review block, form, footer, buttons, badges.
- Boards: one per page TEMPLATE (not every page), desktop + phone. Tools: board models (TOOLS.md) with real packs as references or composited, or Canva generate-design.
- Three tiers from same inputs: TAME (clean, fast), NEW DIRECTION (new layout/imagery), SPECTACULAR (scroll film/3D/shaders; any page or section the user picks).
- Spectacular assets follow the core asset-request format: loop first frame = last frame; one timed world per scroll section; occlusion transitions between sections; frame-sequence or short video export; in BUILD, mobile weight limits stated up front.
LOOK gate (BUILD only): user picks tier per page, approves tokens + boards. Lock them.

## PHASE 3: HOMEPAGE
- Run ce-04-homepage Phases 1-5 using the locked system. Do not redo the audit or the brand intake.
LOOK gate (BUILD only): homepage approved on phone and desktop.

## PHASE 4: TEMPLATES + ASSET LOCK
- Build each template once: collection, product, article, about, contact. Pages are template + content.
- Asset lock: product sheets (front + 3/4, real label), lifestyle, OG/share images, icons. Optimize: WebP/AVIF, lazy-load, alt text written, local fonts.
- Optional per-page hero loops (video model, seamless, under 3 MB, poster frame). Quote first.
ASSETS gate (BUILD only): every asset is a named file. Every label and text matches the real source.

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

## EXTRA FAILURE MODES (shared ones are in ce-core)
| Problem | Fix |
|---|---|
| Traffic drop after launch | Check redirect map, titles/H1s kept, canonicals, noindex. |
| Scope creep | Templates first. New pages go to a Phase 2 backlog. |
| Off-brand drift between pages | Rebuild from tokens, re-run Guardian. |
| Slow pages | Compress, lazy-load, remove apps/scripts, drop that page's motion tier. |
| Missing access | Ship prototype + handoff pack, say what is blocked. |
| Client keeps changing boards | LOOK gate lock. Changes after = new scope, logged. |

## RUN ORDER SUMMARY
EXPLORE: world rules > boards > prototype on spectacular tier > show me. No audit, sitemap, migration or budgets.
BUILD: 0 audit (ce-00 bible) > PLAN > 1 sitemap > PLAN > 2 design system > LOOK > 3 homepage (ce-04) > LOOK > 4 templates + assets > ASSETS > 5 build (prototype first) > 6 migrate > 7 audit > 8 launch + handoff.
Time: 1-2 weeks small site, 3-5 weeks 30+ pages. Credits: boards low, loops moderate. Always quote first.
