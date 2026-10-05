# Extract C: S05 + S06 (Claude Design, anti-slop)

Format: **Name** [tag | branches | lesson] - what to do. Quote.

## Techniques

1. **Independent critics, not self-review** [U | IMG, UGC, ANIM, CINE, WEB, APP | S05] - Never let the maker grade its own output. Spin up fresh-context critics that only judge. "Claude judges its own homework"
2. **Three critic roles** [U | all | S05] - Critic 1: brief (did it do what was asked). Critic 2: system (matches the design system). Critic 3: craft (visual quality bar set from the prompt). "one critic can be the brief"
3. **Critics judge rendered frames** [U | IMG, ANIM, WEB, APP, CINE | S05] - Critics look at screenshots/frames of the output, never the code. "rendered frames, never the code"
4. **Loop until all pass** [U | all | S05] - Repeat build > critique > fix until all critics pass. A human can stop it; it ended naturally. "it kind of ended naturally at a great point"
5. **Taste as a checklist** [U | all | S05] - Turn taste into written pass/fail checks the critics run every round. "taste becomes a checklist"
6. **Loop stages** [S | all | S05] - Order: interview, pre-flight, teardown of the reference (set the bar), build, critic rounds, final gate check. "interview pre-flight tear down the bar build it"
7. **Several critic passes catch different things** [U | all | S05] - One pass misses issues; repeated passes find new ones. Example catches: missing logos, color breaking, monochrome, headline underscaled, mark too small, second accent color. "you will get five different actors"
8. **Spend loop only on big jobs** [U | all | S05] - Use it for reusable templates, carousels, high-stakes work. Skip for quick one-offs. "I would reserve this for your bigger things"
9. **Cheap critics, strong designer** [U | all | S05] - Run critic rounds on smaller models (Haiku, Sonnet, or other cheap model); keep the strongest model for design judgment. "it's got great design taste"
10. **Reference-led build** [S | IMG, WEB, ANIM | S05] - Give a reference (URL, screenshot, or just a concept) and have it recreate in own subject/style. "I can give it a reference image"
11. **Reference for inspiration, system for look** [S | WEB, APP | S06] - Screenshot or link a design you like for vibe; the design system still sets final look. "I love this kind of design and vibe"
12. **Convert an existing asset into a design system** [U | all | S05] - Upload a deck/brand guide; ask Claude to codify typography, colors, layout; export; inject into every build. "Turn it into a design system."
13. **Design system = memory** [U | all | S05] - Claude has no memory of your style; the system is the codified blueprint. "what is known as a terrible memory"
14. **Slop comes from shared defaults** [U | all | S06] - Generic output = same default prompts and no brand context. Fix: brand-specific system built once, reused. "every page that Claude is designing is from the same systems"
15. **Interview before system** [S | all | S06] - Ask product, name, vibe, hero products, things to avoid. Then write one build prompt covering palette, costs, assets. "we have Claude interviewing us"
16. **Name what to avoid** [U | all | S06] - State cliches to avoid in intake. "just avoid all the cliches"
17. **Generate missing brand assets, then load them** [S | IMG, WEB, ANIM | S06] - If brand has no assets, generate logos, hero images, textures, ingredients in one session, upload all into the system. "Hicksfield lets us design videos and images"
18. **Scrape or upload real assets** [S | WEB, IMG | S06] - If brand exists, scrape/upload real files instead. "scrape those using firecrawl or just upload them"
19. **Texture packs as brand material** [S | IMG, WEB, ANIM | S06] - Include texture/background packs in the system. "It's even got texture packs"
20. **Decide once, reuse** [U | all | S06] - Do upfront design-system work once. "we decide once and we can reuse that system"
21. **Share the system as a file** [U | all | S06] - Export project archive/standalone HTML; tell Claude "look at the last downloaded system"; also hand to editors. "Please look at that when you are creating designs for me"
22. **One system across formats** [U | all | S06] - Decks, sites, animations, app screens all pull from same system. "it's all pulling from the exact same design system"
23. **Iterate, one shot is not enough** [U | all | S06] - Plan feedback rounds in plain language. "one shot is not enough"
24. **Moving piece (showstopper)** [S | WEB, ANIM | S06] - Add one showstopping motion element (scroll animation, 3D). "Think of it as something showstopping"
25. **Design to code handover** [S | WEB, APP | S06] - Export project archive, open in Claude Code on localhost to add 3D, shaders, interaction. "claude code can do everything that claude design can do"
26. **3D/video embed format choice** [F/S | WEB, CINE | S06] - Pick: scroll-scrub hero, autoplay hero background, or own section. Loop type: first and last frame match. "Scroll scrub hero, autoplay hero background, its own section."
27. **UI sniping** [S | WEB, APP | S06] - Browse component libraries, copy code, tell Claude Code to install with brand images swapped in. "go and install this, but replace the images with burgers"
28. **Let Claude improve the prompt** [U | all | S06] - Ask Claude to rewrite the prompt before running. "improve this prompt such that the output would be better"
29. **Simplify for viewers** [S | ANIM, WEB, IMG | S06] - Cut tags and clutter; short explainer text; support voiceover. "Don't make the user think."
30. **Cut clutter on request** [S | ANIM, IMG | S06] - "I don't need loads of tags."

## (a) Tools / links named
- Gauntlet Loop / Design Loop (Matt Shumer idea): multi-critic loop; `/design_loop` skill (Three Critic Skill, Notion guide link in S05).
- Claude Design: design systems, project HTML/archive export, artifact publish.
- Claude Code: handover, localhost preview.
- Higgsfield (CLI skill): generates logos, images, video, 3D clips.
- Claude "Fable 5": recommended top model for system build.
- Firecrawl: scrape brand assets.
- 21st.dev, UI Aceternity, ReactBits.dev: copy-paste UI components, shaders.
- 3D website skill (Notion "Brand Asset Machine" link): asks questions then builds embed video.
- Deep Seek V4 Flash, Haiku, Sonnet: cheap critic models.

## (b) Numbers
- Loop cost 2-3M tokens per build (3M, ~2M, 730k Haiku + 1.9M Sonnet runs).
- Rounds seen: 10 and 6; 3 critics.
- HTML animation: 10-15 s. Site video clip: ~25 s. Design system build ~5 min.
- Attach file limit 50 MB.
- Reference example: 15,000 likes carousel.

## (c) Conflicts with existing rules
- "Prompts edited one line at a time first": S06 has Claude rewrite whole prompt at once ("improve this prompt").
- "Spectacular web tier on any page": S06 treats showstopper as a single special feature on a site; S05 says "one piece per project" (about loop use).
- "Keep beats short": S06 recommends ~25 s embed clip; S05 10-15 s animation.
- "Real packshots/logos always real": S06 generates logos and product images with AI when brand has none (invented brand/burgers). S05 critic flags missing logos (supports real logos).
- "Text set in code": no conflict; S06 animates text as HTML.
