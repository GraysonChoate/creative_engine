# After Effects skills (13) - what they cover and how we use them
Source: ae_get_skill on the local MCP (fnf-after-effects-mcp v0.1.3). Read Oct 9, 2026.
License: skills are not redistributable. These notes are our own words. Never copy or edit them. Our layer sits on top. Cached locally at ~/.ce-ae/skills-cache (not in repo).
Names: companions are prefixed "ae-" (ae-ui-mastery, not ui-mastery). Fetch ae-clean-rig first; it routes to the rest.

## Core flow (ae-clean-rig)
Inspect project > ae_catalog (never guess operation names) > ae_do. Backup before structural edits. Target = the reference's look and motion; method = clean, editable, native (text, shapes, precomps, null controls). No bitmap UI, no hundreds of traced fragments. Verify by rendering frames (start, peak, settle, seams) and one real content edit. A queued render is not proof.
No reference? It asks which route: generate a foundation (moodboard of 4 > storyboard sheet), supply a reference, or proceed from text and say what was invented.

## The 8 companions
- ae-design-first: lock the still design first (aspect, safe areas, grid, hierarchy), render one component, then animate. No HTML-to-AE converter locally. Lottie JSON is not importable.
- ae-ui-mastery: tokens first (spacing 4/8/12/16/24/32/48/64/96; type scale 12-64), component anatomy, one dominant message, test long label and alt image, judge at final size.
- ae-transition-kit: A and B as replaceable sources; progress/direction/softness controls; test 0%, mid, 100% and the frames around the seam; test other aspect ratios.
- ae-liquid-glass: glass = refraction + edge light + tint + shadow, not a white rectangle. Layer stack named by role. Test on bright, dark, busy backgrounds and small sizes. Sizes (blur 40, scale 110) are examples only.
- ae-animation-principles: timing at 30 fps: 2-4 frames snap, 4-6 anticipation, 8-12 quick transition, 18-30 slow entrance, 6-10 settle. Sparse keys. Stagger for reading order. Hidden state before reveals. Trim paths for drawn lines. Loops: check the seam and velocity.
- ae-depth-space: parallax by planes; far planes move less, lose contrast. Depth-strength control where 0 = exact baseline. Camera only when needed.
- ae-build-orchestration: small verified batches, one representative component first, dependency order, test controls at 0 / fractional / extreme.
- ae-mcp-realities: local route = stdio server > AppleScript > dispatcher; no panel. Batch is not transactional. After a timeout, inspect before replaying. eval is off.

## Group modules inside ae-clean-rig (most relevant to us)
- collage: editorial paper collage + animated prompt interface (typing, caret, submit). Timing guide: 0.25-0.6 s per entrance, 0.04-0.15 s stagger, 3-6% overshoot only if the material calls for it. THIS is the style of Zubair's intro and the "MAKE IT CINEMATIC" bar.
- boards: sticky-note boards, camera routes, easing. Zero-speed stops at pauses; flat board = animate wrapper position + scale, not a 3D camera.
- 07 sliders: gallery / Coverflow / cyclic slider.
- characters, rigging, 11, 12: character work.
- 13-16 localization: translations, fitting text, recut to a video. Matches Adil's different-language workflow.
- 17 visual foundation: moodboard > storyboard when no reference.

## Check against our library
ALREADY HAVE: lock-first, one-element-at-a-time, stagger, eased keys, seam/loop checks, verify by frame.
NEW: (1) Token-first UI build. (2) Static-first, then motion. (3) Transition kit test list. (4) Glass layer stack. (5) Frame-count timing guide. (6) Zero = baseline controls. (7) "No reference" 3-way route. (8) Paper collage and prompt-bar recipes already exist for AE.
OPTIONS / CONFLICTS (decide by use case, no hard rule):
- Idle drift: skill says none unless asked; Zubair adds idle drift to everything. Default off; ON for ambient dashboards/hero loops, and only on request.
- Zubair's cloud route builds from HTML; our local route builds native only. Fine for editability; slower for complex glass.
- Our "silent-first" / sound rules unaffected.

## Gaps we must design ourselves (app UI motion)
The skills have no app-screen motion vocabulary. Needed: tab/screen transitions, list stagger, skeleton loading, pull-to-refresh, button press and success states, onboarding sequences, device frame and touch indicators, a "too much on screen" simplicity check, brand token set per app, sound cues for UI.
Plan: pair video findings with our own outside research (Apple HIG motion, Material motion, spring settings, Rive/Lottie practice, top fitness/consumer apps).

## Not done
- Did not run any build. Nothing in AE changed.
- Skills for characters/rigging/boards read at index level only.
