# Web motion: the code layer (3D, scroll film, transitions, particles)
Version 1.4 (2026-10-14). For ce-04 and ce-05. Companion to jack-roberts.md (interactive components) and ../docs/BRIEF-scroll-assembly.md (AE frame sequence route).

The engine has three layers that make motion. This page is the third one. It is not a fallback: for a web page, code is a first-class medium, equal to Higgsfield and After Effects.

| Layer | Makes | Never makes |
|---|---|---|
| Higgsfield | Film: hero loops, ingredient bursts, hypermotion product shots, one world per scroll section | Exact text, exact labels, anything the visitor touches |
| After Effects | Exact label on a moving product, type animation on film, compositing, frame-sequence exports | Interaction |
| Code (GSAP, Three.js, WebGL, GLSL) | Everything the visitor scrolls, drags, hovers or clicks; 3D products; transitions between sections; particles; type | Photoreal people or places |

## 1. THE ROUTING RULE (one line per element, before anything is built)
Ask of every element on the page: what does the visitor DO with it?

| Visitor does | Layer | Pattern |
|---|---|---|
| Watches it | Higgsfield film, played by code | Hero loop, world behind a section, ingredient burst |
| Scrolls through it | Code scrubs film or frames | Section hand-off, product carried into the next section, a scene that plays forward and back with the scroll |
| Touches it (drag, hover, tab) | Real 3D in code | Product showcase: turn the tub, tabs swap it, hover lifts it |
| Reads it | Code | Headlines, prices, buttons, legal. Never in a model. |

Write it as a table in the section plan (ce-04 Phase 1): element | section | visitor does | layer | source file. No element may be built without a row. If two layers could do it, pick the cheaper one that still passes the real-label rule.

Default split for a product page: ONE real-3D showcase (where the visitor picks a product), film everywhere else, code for every transition and all text. Real 3D on every product is a modeling job per product and rarely worth it.

## 2. ELEVATE (what the word means here)
Elevate = the brand's own visual world, kept, made to move, given room. Not a different brand. Not a strip-down.
- Keep: their imagery subjects (ingredients, settings, hands, skies), their palette, their packs.
- Remove: clutter, boxed text overlays, cramped type, carousels nobody swipes, duplicate sections.
- Add: motion with a job (the ingredient bursts, the cloud drifts, the callout line draws itself), big clean type, one hero instead of five, transitions that carry something from one section into the next.
- Test: a fan of the brand should say "that's them, but better." If it could be any brand, it failed.
- A product alone on a plain backdrop is a downgrade unless the brand's own site is already that minimal.

## 2b. SYNERGY (one sentence per section; every element traces to it)
Each section says one sentence. Write it first. Then every element must be traceable to that sentence or it goes:
- World (background, light, time of day, surface) is built OUT FROM the brand's real element in that section, never chosen first and the element dropped on top. Paige's beach photo means the section's water is her water, her light, her product (Collagen). A cherry splash belongs to Relief, not to her.
- The thing that moves is the thing the copy is about. "Energy, focus, pump" = the burst. "Save 20%" = the stack grows and the number counts. "Everyday wellness" = the brand's real footage of a real day.
- Products, prices, ratings and badges are elements of the story, not UI dropped in afterwards: a price sits beside the product it prices, on the same surface, lit the same.
- Real brand material first: the brand's own video, photos and label art are mined before anything is generated. An agent that logs a real video as "a grey poster" and cuts it has failed Phase 0.
- Test per element: "why is this here, and what is it next to?" A generic answer ("background", "a nice photo") fails.

## 2c. CRAFT PASS (its own gate; measured, never eyeballed)
Before any screenshot goes to the user, measure and report:
- Grid: one left edge for every headline, body and button in a column; section gutters identical; content max-width identical across sections.
- Nav: logo size and clear space, item spacing, cart and icons on one baseline, announcement bar height, nav background behaves the same over every world (same blur or none, same contrast).
- Type: one scale (eyebrow, h1, h2, body, small, legal), same letter-spacing per step, same line-height per step, headline never kisses an image edge, measure under 70 characters.
- Spacing: eyebrow to headline, headline to body, body to button are the same three numbers in every section.
- Components: one button radius, one card radius, one shadow, one pill; the same hover on every button.
- Color: one accent per view; price and compare-at on one baseline; rating stars one size.
- Images: no element cut by the viewport by accident; product base and shadow inside the frame; no photo as a hard rectangle unless every photo is.
A mock-up is judged as the finished thing. "It's a demo" lowers nothing.

## 2d. REAL-SCROLL RECORDING (the only honest motion check)
Stills hide pacing. Every motion check records a real scroll: Playwright or headed Chromium at 1440x900, constant wheel input at about 2400 px/s for the WHOLE page (never a short burst, which hides holds), page video on, then frames at 2 fps as strips. Report: total px, seconds, and every stretch over 1.5 s where nothing on screen changes (dead air). Any such stretch is a fail unless it is the one reading hold per section. The user's own recording at that rate is the reference; a builder recording that disagrees with it is wrong, not the user's.

## 2e. LAYER CONTRACT (how film, 3D and type agree, frame by frame)
The layers are checked against each other, never alone. Every hand-off (film to 3D, 3D to film, film or 3D to type) is a contract written in Phase 1 before any clip is quoted, and measured in Phase 4b after the build.
| Axis | Must match | Measured by |
|---|---|---|
| Position | product centre and base x/y, within 1% of viewport | pixel measure on both frames at the hand-off px |
| Scale | product height as % of viewport, within 1% | same |
| Light | key direction and colour, rim, shadow angle and softness | sampled from the film frame, set on the 3D scene, compared side by side |
| Time | one scroll px where both layers are at their matching frame | the ScrollTrigger table, verified on the recording |
| Surface | contact shadow on the same plane in both layers | compared at the hand-off frame |
Type near a product declares its relationship (baseline on the product base, left edge on the grid, colour sampled from the scene) and that relationship holds through the whole motion, not only at rest.
SIDE-BY-SIDE SHEET (required output): for every hand-off, one image: film frame left, 3D or next frame right, same scroll px, the five numbers written on it. Any miss is a fail before the page is shown.

## 2f. LEGIBILITY, OCCLUSION, SCROLL EFFICIENCY, NAV (measured)
- Legibility: every text element's contrast against what is actually behind it at 0, 50 and 100% of its motion (not at rest). Body 4.5:1, headline 3:1, nothing under 14 px. Price and rating never smaller than the product name. Report the lowest value per element.
- Occlusion: on every recorded frame, bounding boxes of text, price, button, tab, product and face. Any text or control overlapping a product, a face or other text is listed; one overlap is a fail.
- Scroll efficiency: product, price and buy visible within two screens; whole page under 7 screens. Anything stacked vertically that reads better side by side (a product and its copy, three tubs and three prices, a quote and its author) goes horizontal. Every beat's scroll length is in the table with a one-line reason.
- Nav as a designed object: its own board in Phase 2. Logo lockup and clear space, item spacing, cart with count, one treatment that reads over every world (dark, sky, water, white) without per-section hacks, scroll behaviour (shrink, blur or colour), and it never covers a headline. Tabs, pills, cards and buttons get a component sheet with every state (rest, hover, active, added), measured once and reused.

## 2g. INTERACTION WALK (stills at scroll positions do not find these)
Before any build is shown, an agent clicks everything a visitor can click and screenshots each state: every tab, every card, every picker chip, every hover, every drag, the cart count. Then it scrolls every section seam at about 300 px/s and screenshots the seam at 0/25/50/75/100%. Report: a table of element | state | screenshot | pass or fail. Specific traps this catches: a sticky or pinned element from the next section opening over the current one; pre-selected state on load; products that render differently from each other (some 3D, some flat) with no stated reason; a swap or drop animation that only runs on one trigger; a 3D model whose silhouette does not match its real render (lid height, body ratio, label panel facing). Any product shown in 3D is compared side by side to its real render at 0/90/180/270; silhouette and wrap registration are measured, not assumed. Mixed treatments (3 products modelled, 14 flat) are a fail unless the brief chose it.

## 2h. SELF-AUDIT STANDARD (run after every build, before every freeze)
Write SELF-AUDIT.md: one row per check, PASS or FAIL with the measured number, a screenshot path for every FAIL. A FAIL is fixed before moving on, or the row says why. Never round a FAIL into a PASS.
A. MOTION (real-scroll recording, constant 2,400 px/s, whole page): A1 no stretch over 1.5 s with nothing changing except one reading hold per section. A2 no pops: every arrival eases out over 0.6-1.2 s with 40-80 ms stagger; every exit fades; list single-frame appearances. A3 at every seam the next section's first element is rising before this section's last has left; screenshot seams at 25/50/75%. A4 scroll up and back through every section: nothing changes that scroll did not drive. A5 no pin over 60 vh.
B. LAYERS: B1 every 3D product vs its real render at 0/90/180/270: silhouette within 1%, lid height within 2%, front panel facing at rest, label readable at 2x; side-by-side sheet per product. B2 every product (3D or flat) has a contact shadow sized to its base; zoom each base at 2x: no gap, no fringe, no jagged edge. B3 every film-to-3D hand-off: position and scale within 1%, light and shadow angle matched, five numbers written on a side-by-side. B4 nothing floats: list every object and its surface.
C. CRAFT (measured): C1 one grid left edge per column. C2 one type scale, max 6 sizes. C3 one radius, one shadow, one pill, one tile, one hover (4-6 px lift, 200 ms); count each. C4 the same three spacings (eyebrow-headline, headline-body, body-button) in every section. C5 nothing within 24 px of a viewport edge or another element; buttons 50% more padding than default. C6 nav: logo size and clear space, item spacing, cart on baseline, one treatment over every world, never covers a headline.
D. LEGIBILITY AND OCCLUSION: D1 every text element's contrast vs what is behind it at 0/50/100% of its motion; body 4.5:1, headline 3:1, nothing under 14 px. D2 bounding boxes on every frame: any text or control over a product, a face or other text is a FAIL.
E. SYNERGY: E1 one sentence per section; every element traced; anything "just there" removed. E2 each world built from the brand's real element in it. E3 what moves is what the copy is about.
F. STORE: F1 product, price and buy within two screens. F2 every price, rating and badge matches the live site today. F3 every button does something visible when clicked. F4 copy only from the live site, word for word.
G. INTERACTION WALK: G1 every tab, card, chip, hover and drag clicked and screenshotted; state table with a path per row. G2 cold load: nothing pre-selected, cart 0, picker 0 of N.
H. PREMIUM: H1 beside apple.com/airpods-pro and aesop.com, list every place ours looks cheaper; each is a FAIL until fixed. H2 would a visitor notice a product is 3D rather than photographed? FAIL if yes. H3 "that's them, but better": FAIL if a fan would not say it, and say why.
I. DEPLOY: I1 deploy/ loads from the folder alone (npx serve), hero screenshot attached. I2 relative paths, no localhost, video MP4+WebM, under 100 MB. I3 no console errors on load or during a full scroll.
Final line: total checks, PASS, FAIL, and the one thing to fix first with one more hour.

## 3. THE SIX CODE MOVES

### 3.1 Real 3D product with the real label (touchable)
- When: the one section where the visitor picks a product.
- Needs from the brand: flat front render per product (the real label), ideally the full label wrap; otherwise front + sides composited by AE into one wrap texture.
- Build: Three.js. Cylinder or lathe mesh matched to the real silhouette (measure from the render: height/diameter ratio, lid height, shoulder curve). Real label as the texture on the body; lid and base get plain PBR materials sampled from the render. HDRI or 3-point studio light; soft contact shadow on a surface plane. Do not generate 3D with AI for labels (ce-04 rule).
- Interaction: drag to rotate (damped), auto-rotate at rest (slow, under 10 deg/s), tabs or cards swap the texture and silhouette with a cross-fade and a small lift. Hover: light lift, no bob.
- Label check: screenshot the 3D view at 0, 90, 180, 270 degrees at full size and compare to the real render. Garbled or stretched text fails.
- Limits: textures 2048 max, one mesh visible at a time, pause the render loop off-screen (IntersectionObserver), reduced-motion = static front view.

### 3.2 Scroll-scrubbed film (the page plays the film)
- When: a section should play forward on scroll down and back on scroll up.
- Source: Higgsfield clip (one world per section), or an AE frame sequence (docs/BRIEF-scroll-assembly.md).
- Build: frame sequence on a canvas, drawn by scroll progress (GSAP ScrollTrigger scrub, Lenis for smoothing). 12 to 24 fps, WebP, 1280 wide desktop, 720 phone. Preload the first second, stream the rest. Poster frame until ready.
- Rule: the clip's first and last frames are the hand-off frames (section 3.4). Lock them before generating.
- Limits: keep each section's sequence under 300 frames; whole page under the tier weight budget (ce-04 Phase 5).

### 3.3 Hero loop in WebGL (watched)
- When: the hero background moves and must blend into the page with no edge.
- Build: video texture on a full-bleed plane, first frame = last frame (seamless). The page background color is set in code; the loop's set is generated to match or is masked with a gradient so no edge shows. Add a slow parallax shift (2 to 4 percent) on scroll so the loop feels placed, not pasted.
- Text sits on top in code, with a protected clean zone that the shot was framed to leave empty (write the clean zone into the shot card).

### 3.4 Shader transitions between sections (the hand-off)
- When: two sections should feel like one film, not stacked blocks.
- Moves, from cheapest: (a) mask wipe (GSAP clip-path, free); (b) an object carried across (the tub from the hero flies forward and lands as the 3D model, GSAP Flip or a shared Three.js scene); (c) GLSL displacement or dissolve between two textures (last frame of section A, first frame of section B), driven by scroll progress; (d) occlusion: a foreground element in the film covers the frame at the cut (powder, cloud, hand), so the next world is already there when it clears.
- Rule: the hand-off happens through something real in the frame (ce-core world rules). Nothing teleports.
- Lock the two hand-off frames before generating either clip.

### 3.5 Particles (watched, sometimes touched)
- When: the brand's ingredient or atmosphere can be a field (berries, powder, bubbles, dust, light motes).
- Build: Three.js Points or an instanced mesh, 500 to 5,000 particles, sprite texture cut from the real ingredient render (remove_background), slow drift, slight mouse parallax, spawn and settle on scroll into a section. Under 1 ms per frame on a mid phone or cut the count.
- Rule: particles start from a cause in the world (the burst behind the tub, the scoop) and settle. No endless confetti.

### 3.6 Mouse parallax and tilt (touched, light)
- Layered PNGs or planes (background, product, foreground ingredient) move at different rates with the cursor, 2 to 6 percent, damped. Product tilts under 5 degrees. On phone, use the gyro or nothing.
- Never on text. Never on a section the visitor scrolls through.

## 4. MOTION RULES (all six moves)
- Every moving bit has a job: shows the product, opens information, or carries the visitor to the next section.
- Weighted and slow: ease-out on arrival, 0.8 to 1.6 s for reveals, 60 to 120 ms stagger on type.
- Products sit on surfaces or in hands. Ingredients may fly. Nothing bobs.
- One render loop per section; pause it off-screen. Reduced motion: stills and fades only.
- Transitions carry something real across the cut.
- Phone gets the same story with lighter assets, never a different page.

## 5. WHAT TO HAND EACH LAYER (asset list per section)
| Element | From Higgsfield | From AE | Code needs |
|---|---|---|---|
| Hero loop | 16:9 loop, first = last frame, clean zone for text, set color named | - | MP4 + WebM, poster frame |
| Section world | one clip per section, hand-off frames locked | optional grade + frame export | frame sequence or MP4 |
| 3D showcase | - | label wrap texture if the brand has no flat wrap | silhouette measurements, texture PNG 2048 |
| Ingredient particles | one burst still or clip | cutouts | sprite PNGs with alpha |
| Type, prices, buttons, legal | - | - | brand fonts, copy list word for word |

## 6. CHECK (before showing the user)
- Section story lines listed; every element traced (2b). Craft pass measured (2c). Real-scroll recording with dead-air report (2d). Side-by-side sheets for every hand-off (2e). Legibility, occlusion, scroll-efficiency and nav reports (2f). Interaction walk table with screenshots (2g). SELF-AUDIT.md per the standard (2h).
- Screenshot every section at desktop; every transition at 0, 50, 100 percent scroll progress.
- 3D label at four angles against the real render.
- Weight and first-load time against the tier budget.
- Run the X-ray (jack-roberts.md): list what is Higgsfield, what is AE, what is code. If one layer is doing everything, the routing table was skipped.
