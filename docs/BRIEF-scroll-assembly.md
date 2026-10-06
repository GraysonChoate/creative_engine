# Brief: assemble finished scenes into a cinematic scroll ad (After Effects + web)

Paste this to the agent after every scene is made and approved.

---
All scenes are done and approved. Now assemble them into one cinematic scroll experience that works like a website. Read START-HERE.md, docs/AE-route.md and ce-04 (spectacular tier) first. Work in EXPLORE mode.

**What I have:** [folder path with the scene clips, locked element images, real logo and pack files, music if any]
**Goal:** the page scrolls like a film. Scroll down = the film plays forward. Scroll up = it plays back. Text and the product appear at the right moments.

**Step 1. Plan (show me, then stop).** One table, one row per scroll section: section | which scene clip | what the viewer reads (headline/line, in code) | how it hands off to the next (match cut, push through steam, whip). Include the order and total scroll length. Wait for my yes.

**Step 2. After Effects (the film).**
- Import the real clips, logo and pack files. Never redraw them.
- One comp at 1920x1080, 30 fps. Cut each scene to its best seconds. Trim half a second off both ends.
- Build the hand-offs between scenes as transitions through a real object in frame.
- One grade across all scenes. Fix mismatches.
- Add the real logo and pack shot at the end. Text comes from real fonts, set in AE or left to the page (tell me which).
- Render a frame from every scene and check each one against the real files before moving on.
- Export: (a) a frame sequence, WebP, 1280 wide for desktop and 720 wide for phone, about 24 frames per second of film; (b) one MP4 backup. Tell me file sizes.

**Step 3. The page (the scroll).**
- One HTML page. GSAP + ScrollTrigger + Lenis. The frame sequence plays on a canvas, scrubbed by scroll position. Preload the first frames first, load the rest in the background.
- Headlines and the call to action are real text on top, fading in at set scroll points. One main button.
- Phone: use the 720 sequence. Show a poster frame while loading. Respect reduced motion (show stills, no scrubbing).
- Pause everything when the page is off screen.

**Step 4. Show me.** Give me a local preview link and a phone-width screenshot of 5 moments (start, 3 middle, end). Say the total weight in MB and how long a first load takes. List anything that looks wrong and how you would fix it. Do not publish or touch any live site.

Rules: real logo, pack and fonts only. Quote nothing in AE (no credits), but say how long renders will take first. Keep every file in the project folder, and never overwrite my originals.
---

## Notes for the human
- AE builds the film. The scroll behavior is built in code (the page). AE does not make the website.
- Frame sequences are heavy. 24 fps x 60 s = about 1,400 frames. Keep the sequence to the most important scroll-driven moments, or use fewer fps (12) and let the page smooth between frames.
- Not yet tested here: real clip import, frame-sequence export from AE, tracking. The first run may need one fix round.
