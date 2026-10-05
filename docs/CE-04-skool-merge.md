# Creative Engine: Merge Pass 3 (Skool "AI Automation Vault", 10 lessons)

Source: 10 lessons (descriptions + video transcripts + a few text files), saved in `sources/skool/` (S01 to S10) with per-lesson extracts (`extract-A` to `extract-E`).
Tags: **U** = Universal · **S** = Shared (adapt per branch) · **F** = Film-only. Branches: IMG, UGC, ANIM, CINE, WEB, APP, plus CORE-RESEARCH.
Numbering continues from CE-03 (#1 to #92). New entries are **#93 onward**.
NOT opened (outside files, per safety rule): `RTFSkill.zip`, `design-teardown-skill.zip`, `Claude Looping.skill`. What the transcripts say they do is noted below.
Sales pitch, income claims and course promos were dropped.

---

## 1. Rule conflicts (decide before using)

| # | Source says | Our rule | Verdict |
|---|---|---|---|
| C1 | S02, S04, S08, S09: paste or rewrite a whole prompt, "one shot" | ce-06 rule 7: one-line change first, rewrite last | **Keep ours.** Whole-prompt rewrite is the last resort. Exception: asking Claude to improve a prompt BEFORE the first run (S06) is fine. |
| C2 | S02, S06, S08, S09: AI makes the logo, product, mascot, "proof" images | Real packshots and logos are always real images | **Keep ours** for any real brand. Generated logos are OK only for an invented brand or a concept pitch, labelled as such. Generated before/after "proof" for a real business is banned (fake proof rule). |
| C3 | S02: AI logo may carry text inside the image | Text set in code | **Keep ours.** |
| C4 | S09: Higgsfield UI cannot do start+end frame with Seedance; Kling 3.0 can | ce-03 Route B and ce-04/05 loop assets assume start=end frame | **Verify in our own Higgsfield tools before relying on either.** Likely dated. |
| C5 | S06: ~25 s site video clip; S05: 10 to 15 s HTML animation | Short beats; loops under 3 MB | No real conflict. Treat as a clip length, still subject to weight budget. |
| C6 | S06: one "showstopper" per site | ce-04/05 now: spectacular on any page the user picks | **Keep ours.** Source is advice, not a rule. |

---

## 2. New entries

### CORE: Design system and anti-slop (the biggest new block)

| # | Technique | Tag | Branch | Src |
|---|---|---|---|---|
| 93 | **System, not prompt.** Give the model a design system plus references, not one generic prompt. Generic prompts give everyone the same fonts, gradients and cards. | U | WEB, APP, IMG | S01 |
| 94 | **Slop checklist (the five tells):** typography, imagery, hierarchy, color, spacing. Named defaults to ban: same typeface, indigo-to-violet gradient, three feature cards, uniform rounding, frosted glass, AI-sounding headline. | U | all | S01, S04 |
| 95 | **Slop comes from shared defaults and no brand context.** Fix is one brand-specific system, built once, reused everywhere ("decide once, reuse"). | U | all | S06 |
| 96 | **Show Claude what great looks like.** Feed real top-tier design systems (palette, type, tokens). Slop = the model never saw good. | U | all | S04 |
| 97 | **Design system = memory.** Claude does not remember your style; the codified system is the memory. | U | all | S05 |
| 98 | **Niche reference pick.** Pull a gallery of top sites, ask for the 3 closest to the brand's niche. One primary, one secondary. | S | WEB, APP | S01 |
| 99 | **Reference to design system.** Paste a reference link, say "be inspired by its whole system, adapt to my product". Ask for a design-system page: typography, buttons, colors, login, graphic rules, asset inventory. | S | WEB, APP, IMG, ANIM | S01, S04 |
| 100 | **Blend references.** Combine several designs into your own style. Do not copy one site. | U | all | S01 |
| 101 | **Reference for vibe, system for look.** Screenshot or link for vibe; the design system still sets the final look. | S | WEB, APP | S06 |
| 102 | **Convert an existing asset into a design system.** Upload a deck or brand guide, ask Claude to codify type, colors, layout, export, inject into every build. | U | all | S05 |
| 103 | **Export the finished project as a system file** and reuse the one file for decks, emails, pages, animation, app screens. Tell Claude "look at the last downloaded system". | U | all | S02, S06 |
| 104 | **Interview before system.** Claude asks: product, name, vibe, hero products, things to avoid. Then one build prompt covers palette, assets, costs. Name the cliches to avoid. | S | all | S06 |
| 105 | **Missing brand assets: generate, then load.** If the brand has none, generate logos, textures, hero images in one session and load all into the system. If the brand exists, scrape or upload real files instead. (See C2.) | S | IMG, WEB, ANIM | S06 |
| 106 | **Texture packs** are part of the brand material. | S | IMG, WEB, ANIM | S06 |
| 107 | **Own character and graphic style.** Study the reference's graphics and motion, then make a unique style and cast for the brand. Human picks the concept; AI does repetition. | S | IMG, ANIM, WEB | S01 |
| 108 | **Palette from proven palettes** (a generator, lock colors you like). Do not invent from scratch. Or ask Claude for niche-fit colors, then lock them. | U | all | S02, S08 |
| 109 | **Font is the main slop tell: set it on purpose.** Name a specific font; never accept the default. Use galleries that show fonts in real use. Check the commercial licence. | U | all | S01, S03 |
| 110 | **Fonts from a live site.** Scrape a reference with Firecrawl `branding` format; build the system from that font or the closest free one. Match a font from a screenshot. | U | WEB, IMG, APP | S03 |
| 111 | **One icon style per piece.** Feed a full icon pack in one style; do not mix. Check licences (Flaticon, Lordicon). | S | ANIM, IMG, WEB | S03 |

### CORE: Critic loop (extends gauntlet-loop)

| # | Technique | Tag | Branch | Src |
|---|---|---|---|---|
| 112 | **Independent critics, not self-review.** Fresh-context critics that only judge, never the maker. | U | all | S05 |
| 113 | **Three critic roles:** brief (did it do what was asked), system (matches the design system), craft (visual quality bar set from the prompt). | U | all | S04, S05 |
| 114 | **Critics judge rendered frames or screenshots, never the code.** | U | IMG, ANIM, WEB, APP, CINE | S05 |
| 115 | **Loop until all pass.** Build, critique, fix; a human can stop it. Gold-standard reference + yes/no judges stops endless "improvements". | U | all | S01, S05 |
| 116 | **Taste as a checklist:** written pass/fail checks run every round. | U | all | S05 |
| 117 | **Loop stages:** interview > pre-flight > teardown of the reference (sets the bar) > build > critic rounds > final gate check. | S | all | S05 |
| 118 | **Repeated passes catch different issues** (missing logos, color breaks, headline too small, a second accent color). | U | all | S05 |
| 119 | **Spend the loop on big jobs only** (reusable templates, carousels, high stakes). Skip for one-offs. | U | all | S05 |
| 120 | **Cheap critics, strong designer.** Run critic rounds on smaller models; keep the best model for design judgment. | U | all | S05 |
| 121 | **Ruthless teardown vs reference.** Give your page and a reference; ask for a harsh side-by-side with screenshots in measurable values (letter spacing, elevation ladder, radius, line height, shadows). Output as short HTML. (Skill zip not opened.) | U | WEB, APP, IMG | S04 |
| 122 | **Test the output for real** (click the button, send the email). | S | WEB | S04 |

### CORE: Process and prompting

| # | Technique | Tag | Branch | Src |
|---|---|---|---|---|
| 123 | **Pilot first.** Make a small pilot of new graphics or video, approve the look, then run the full build. | U | all | S01 |
| 124 | **Brief like a design director.** Specific brief plus screenshots from inspiration sites. Plan 5 to 10 rounds of concrete feedback (contrast, colors per screen, consistent block height). | U | WEB, APP, IMG | S02 |
| 125 | **Variants, pick a winner.** Ask for 5 designs (4 logo variants), choose one, save it. 2K is enough, 4K is overkill. | U | IMG, WEB | S02 |
| 126 | **Claude thinks, Higgsfield makes.** Claude writes the prompts; the generator renders. Give it the design system so assets match. | S | all | S02 |
| 127 | **Ask Claude to improve the prompt before running.** (Pre-run only. See C1.) | U | all | S06 |
| 128 | **Copy pass with a second model** (AI-tell remover, banned-word list). Benchmark top 5 competitors' copy. Principles: name the pain first, one ask per screen, one screen one point, concrete lines. | S | WEB, IMG, UGC, ANIM | S01 |
| 129 | **Quote cost before generating** (model, ratio, resolution, count, credits). Already our rule; confirmed good practice. | U | all | S04 |
| 130 | **Searchable local asset library.** Index images and video with a cheap vision model so Claude finds assets by content. | U | all | S04 |
| 131 | **Style recipe.** Save a named recipe (description + reference images); change one element per run. | S | IMG, ANIM, WEB | S04 |
| 132 | **Real data into animated charts, then codify the approved style** as a rule for all future charts. Research stats with Firecrawl first so numbers are not invented. | S | ANIM, WEB, IMG | S03 |
| 133 | **Word-level timestamp transcript**, then find the moments where an animation helps and make clips for them. (RTFSkill zip not opened.) | S | ANIM, UGC, CINE | S03 |
| 134 | **Build one skill per output type** (Reels, YouTube, etc.). Run "evals": a skill must beat what Claude does unaided. | U | all | S03, S10 |
| 135 | **Lottie JSON library** in a repo; check each licence. | S | ANIM, WEB | S03 |
| 136 | **HTML motion and 3D one-shots** in the chosen system (10 to 15 s animation, a sphere), dropped into a page or deck. | S | ANIM, WEB | S02 |

### BRANCH: Website (fills part of the WEB gap)

| # | Technique | Tag | Src |
|---|---|---|---|
| 137 | **Substance before style.** Five-question brief: visitor, one action, objections, vibe, brand assets. Feed it to every step. | U (WEB, APP) | S08 |
| 138 | **Competitor research with a stated "top" rule** (5 sites, ranked by reviews or search rank); have Claude answer the five questions from them. | S | S08 |
| 139 | **Ask Claude the realistic page count** (not default one page). | S | S08 |
| 140 | **Order: sitemap > wireframe > style guide.** Review and reorder sections before any code. One prompt per page. | S | S08 |
| 141 | **Export wireframe as React, wire to the sitemap,** then run a design-skill restyle pass on the same structure. | S | S08 |
| 142 | **Layout first, generated assets second.** Placeholders first. | S | S08 |
| 143 | **Reference-chained image pair, then start/end-frame transition clip** (image A, image B built from A, video between). Applies to product or concept visuals only (see C2). | S | S08 |
| 144 | **Video to scroll animation:** have Claude turn the clip into frames that play on scroll, and choose the placement (near top, text on one side, message stays in front). **Detail is thin.** S08 gives the idea, not the export steps. | S | S08 |
| 145 | **Embed format choice:** scroll-scrub hero, autoplay hero background, or its own section; loop clips have matching first and last frame. | F/S | S06 |
| 146 | **Design to code handover:** export project archive, open in Claude Code on localhost to add 3D, shaders, interaction. | S | S06 |
| 147 | **UI component sources** (21st.dev, Aceternity, ReactBits): copy a component, install, swap the images for brand images. | S | S06 |
| 148 | **Seamless 360 product loop:** same still as first and last frame; prompt a spin that ends where it began. ~7 s sweet spot; 16:9; 720p test. | S | S09 |
| 149 | **Hero video wiring:** first hero element, looping background, enough contrast with text; darken edges in code so the clip blends. | S | S09 |
| 150 | **Baseline first, video second.** Reskin a base site template, then add video. Pair the cinematic hero with a conversion structure. | S | S09 |
| 151 | **Blank page fix:** open inspect, copy the console error, paste to Claude. | U | S09 |
| 152 | **Download the original file** (right-click save is low quality). | U | S09 |
| 153 | **Delivery path:** GitHub repo then Vercel. Fine for prototypes; our ce-05 launch rules (staging, redirect map, approvals) still apply. | S | S02, S08, S09 |
| 154 | **Prototype UI in Lovable,** sync to GitHub, clone to Claude Code. Front end first, wiring later. Dribbble/other screenshot as the reference. | S (APP, WEB) | S07 |
| 155 | **App back end:** install Supabase agent skills; run the database advisor for security gaps (row-level security, password protection); disable email confirmation only while testing. | S (APP) | S02 |

### BRANCH: UGC / IMG / ANIM from marketing lessons

| # | Technique | Tag | Branch | Src |
|---|---|---|---|---|
| 156 | **Trend scoring matrix:** score each signal 1 to 5 on recency (7-day cap), authority, velocity, relevance (out of 20). Confirm the matrix before running. | S | IMG, UGC, ANIM, CINE, WEB | S10 |
| 157 | **Competitor scrape table** (Apify: last 5 posts per named account: likes, comments, shares, description). Give it named accounts; do not let it pick. | S | IMG, UGC | S10 |
| 158 | **Make the approved report a scheduled task** (e.g. every day 9:00). | U | all | S10 |
| 159 | **Batch branded designs from one master template** + list of headlines (7 words max, centered). | S | IMG | S10 |

### CORE: Research (new, not creative)

| # | Technique | Tag | Src |
|---|---|---|---|
| 160 | **Claude Code drives NotebookLM** (CLI skill, sign in once). State the end goal; let Claude choose sources; bulk-add videos with the extension; prune noise; export full text locally; check the export; turn the session into a skill. | U | S07 |
| 161 | **Words plus numbers:** text in NotebookLM, metrics in a database; ask across both. | U | S07 |
| 162 | **Wait for sources READY before generating.** Use a permanent "second brain" notebook; consult it first. | U | S07 |
| 163 | **Per-system API key** with a spend cap and 1-year expiry. | U (APP) | S07 |

---

## 3. Already covered or confirmed (not added)

- Gauntlet-loop / Design Loop: same idea as our `gauntlet-loop` skill. #112 to #120 extend it (three roles, frames not code, cheap critics).
- Quote cost first: already our rule (#129 confirms).
- Firecrawl branding scrape: already in ce-00.
- Sound off on site video, 2K stills, 16:9 hero stills: consistent with ce-04/05.

## 4. Branch readiness after this pass

| Branch | Status |
|---|---|
| WEB | Much stronger: design-system front end (#93 to #111), critic loop (#112 to #122), page planning (#137 to #141), loops and hero video (#148 to #150). **Still missing:** scroll-linked playback export steps, WebGL/GLB, mobile weight and poster fallbacks (S09 has none despite its title; S08 #144 is one line). Next: read the Notion guides linked in S05/S06 ("Brand Asset Machine"/3D website skill) and the Higgsfield website builder instructions. |
| APP | Slightly stronger: #154, #155, design-system reuse. |
| IMG | Design system, copy, templates, trend research. Still no packshot compositing recipe or ad-testing method from this source. |
| UGC | Scoring matrix, competitor table, timestamp transcripts. Still no hook/script playbook. |
| ANIM | Charts from real data, Lottie, HTML motion. |
| CINE | Nothing film-specific in these lessons. |

## 5. Next actions

1. Decide the skill edits (propose, you save): add #93 to #121 as a **design-system and critic** section to ce-00 or a new `ce-core-design-system` skill; add #137 to #150 to ce-04/05 (five-question brief, sitemap > wireframe > style guide, hero loop wiring); fold C2 into ce-00 hard rules.
2. Read the linked Notion guides (Design Loop, Brand Asset Machine) to fill the WEB gap.
3. If you want the zip/skill files, open them yourself and drop them in `sources/skool/` for me to read.
