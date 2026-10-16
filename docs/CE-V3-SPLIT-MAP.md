# Creative Engine v3: the split
Date: 2026-10-16. Status: PLAN, nothing moved yet. Approve, then migrate in the order at the bottom.

## 1. Target structure (6 repos + client folders)

```
ce-core/            the brain. Every engine pulls this in. Brand-free.
ce-realism/         UGC, creator reels, fitness, vlogs, testimonials   (phone-real)
ce-cinematic/       brand films, commercials, cinematic reels, stylized CG, explainers
ce-motion/          carousels, image ads, animated ads, interactive ads (no footage)
ce-web/             homepages, sites, Shopify, 3D/immersive sites
ce-app/             app UI, flows, design systems
clients/<brand>/    brief, brand bible, client rules, asset library, decisions, outputs
```
Rule: engines never learn brand taste. Client folders never flow back into engines.
Rule: Web and Motion are *assemblers*; Realism, Cinematic and Core's Asset Studio are *suppliers*. A piece that can run on its own (reel, ad, clip) is made by a supplier; a piece that only exists inside the page or carousel is made by the assembler in code or layout.

## 2. The spine (ce-core; every engine runs it, adds only its own thinking)

| Step | Name | Gate | What Core owns |
|---|---|---|---|
| 1 | Prepare | — | Intake questions (5 universal), scrape/Drive/brand guide, Asset Studio (cutouts, 3D, cast, locations, register) |
| 2 | Research | — | Trend/format brief; feeds recommendations into intake |
| 3 | Ideate | **pick 1 of 3** | Three directions, safe→bold, one mood snapshot each |
| 4 | Map | **approve board + tickets** | Six-track storyboard, story check, ticket sheet with credit quote |
| 5 | Build pieces | per-ticket freeze | Locks first, retake cap, tool routing table, Explore/Exact |
| 6 | Assemble | freeze | Diff vs last freeze |
| 7 | Audit + deliver | **demo gate** | Independent audit vs tickets, export table, cost ledger line, WAKE-UP, deploy only here |

Modes: EXPLORE (fast, show-and-go) / EXACT (locked specs, every gate). Named at intake; never self-upgraded.

### Six-track storyboard (step 4)
Tracks: Beat · Visual · Dialogue · Graphics · Sound · Product. Timeline = seconds (video), slides (carousel), scroll positions (site).
Lead track by format: UGC → Dialogue · Cinematic → Visual · Carousel → Graphics · Site → Beat.
Story check before tickets: hook by 2 s (or slide 1 / section 1), one tension, one proof, one payoff, one CTA. Engine fixes the board if a beat is missing.

### Ticket (handoff spec)
What · Made by · Sizes · Length · Loops? · First frame · Last frame · Text space · Sound · Must match (locks) · Credits · Takes max.
Engine writes all tickets from the board; shows one sheet; paid pieces wait for approval; free/code pieces log and go in EXPLORE.

### Intake rules
Listen first (never re-ask what was said) → research → ask only gaps, max 5, each with a proposed answer and reason → never ask what can be derived (sizes, safe zones) → "go with your picks" always valid.

## 3. File map: where every current file goes

| Current file | Goes to | Action |
|---|---|---|
| skills/ce-core/SKILL.md | ce-core/SKILL.md | **Rewrite around the 7-step spine.** Keep: route, model-by-need, modes, world rules, gates, fix order, shared failures, contingencies, library index, stub, tools. Add: intake, six-track board, story check, tickets, retake cap, no-drift, freeze/diff, WAKE-UP, tool-failure rule. |
| skills/ce-core/TOOLS.md | ce-core/tools/routing.md | Expand into the tool-routing table (piece type → model/tool → credits). Engines append lessons here. |
| skills/ce-00-brand-harness/SKILL.md | ce-core/asset-studio/SKILL.md + clients/_template/ | **Split.** Steps 1–3 (intake, bible, asset library) = Asset Studio in Core. Steps 4–6 (advisor, guardian, memory) = client folder template. |
| skills/ce-09-research/SKILL.md | ce-core/research/SKILL.md | Move. Becomes spine step 2 for every engine. |
| skills/gauntlet-loop/SKILL.md | ce-core/audit/gauntlet.md | Move. Becomes the independent audit in step 7. Add "AI tells" checklist for realism. |
| library/web-motion.md 2h (self-audit standard) | ce-core/audit/self-audit.md | Move out of web; it's universal (groups A–I). Web keeps its own extras. |
| library/web-motion.md asset handoff + routing rule | ce-core/tickets.md | Move. This is the ticket spec. |
| docs/DIRECTOR-PASS.md | ce-core/director-pass.md | Move. Runs in step 4 for any video. |
| docs/PLAYBOOK-shots-effects.md | ce-cinematic/library/shots.md | Move. |
| scripts/check.py, sync_report.py, .github/workflows | ce-core/scripts/ | Move; each engine's CI calls Core's check. |
| skills/ce-02-ugc/SKILL.md | ce-realism/SKILL.md | **Rewrite** as Realism engine: intake questions, voice/cadence/sound rules, selfie vs multi-scene, environment constancy, AI-tells list. Carousel mode leaves (→ ce-motion). Hired-creator section stays. |
| library/social-motion.md | ce-realism/library/social-motion.md | Move. Strip the carousel/motion-graphic parts to ce-motion. |
| library/adil/social.md | ce-realism/library/adil-social.md | Move. |
| skills/ce-06-cinematic-ad/SKILL.md | ce-cinematic/SKILL.md | **Rewrite** onto the spine. Keep film rules, phases as step content. Add the "lock one shot, then re-angle by timestamp" method, sound design track, stylized/CG branch. |
| skills/ce-08-explainer/** | ce-cinematic/explainer/ | Move whole. It's a Cinematic sub-mode with a voiceover step. |
| library/adil/Fable-Higgsfield-notes.md | ce-cinematic/library/ | Move (prompt anatomy, hyper-motion, sound in prompts). |
| library/adil/Adil-prompts-all-7.md, Different-Language-notes.md, AE-plugin-research.md, zubair.md, ae-skills.md, docs/AE-route.md, scripts/ae/ | ce-core/finish-layer/after-effects/ | Move. After Effects is a finishing tool every video engine uses. |
| skills/ce-03-animated-ads/SKILL.md | ce-motion/SKILL.md (animated) | **Rewrite** onto the spine. Add UI/SFX sound track, interactive ads. |
| skills/ce-01-image-ads/SKILL.md | ce-motion/image-ads.md | Move; Motion lays out, never invents photos (orders stills from Realism/Cinematic/Asset Studio by ticket). |
| ce-02 carousel mode + library/jad-carousel.md | ce-motion/carousel.md | Merge. |
| skills/ce-07-pitch-deck/SKILL.md | ce-motion/pitch-deck.md | Move. |
| skills/ce-04-homepage/SKILL.md | ce-web/homepage.md | **Rewrite** onto the spine. Keep brand-material-first, world inventory, story line per section, layer contracts, routing table, craft gate. Add 3 mood wireframes at step 3, freeze/deploy procedure (Vercel root, commit email, deploy/ folder), responsive gate. |
| skills/ce-05-website-rebuild/SKILL.md | ce-web/site.md | Rewrite onto the spine. |
| library/web-motion.md (rest) | ce-web/library/web-motion.md | Keep: three layers, elevate, synergy 2b, craft 2c, real-scroll 2d, layer contract 2e, legibility 2f, interaction walk 2g, six code moves. |
| library/jack-roberts.md | ce-web/library/ | Move. |
| docs/BRIEF-scroll-assembly.md | ce-web/library/ | Move. |
| docs/CE-01..04 merge passes, CE-02 video links | ce-core/docs/history/ | Archive. |
| skills/ce-extract-video/SKILL.md | ce-core/learn/extract-video.md | Move. Feeds engine libraries. |
| CHANGELOG.md | each repo | Core keeps v1–2.15 history; engines start at 3.0. |
| (none) | ce-app/ | **New.** Start from ce-web's craft gate + a UI-clarity standard. Lowest priority. |

## 4. New files that don't exist yet (write these first)

| File | Why |
|---|---|
| ce-core/intake.md | The universal 5 questions + the 4 asking rules |
| ce-core/storyboard.md | Six-track board, lead-track table, story check |
| ce-core/tickets.md | Ticket fields, sheet format, approval rules |
| ce-core/export-table.md | Sizes, safe zones, platform limits, Shopify needs |
| ce-core/tools/routing.md | Piece type → tool, with retake cap and credit per take |
| ce-core/freeze.md | Numbered freezes, diff vs last, rollback, WAKE-UP template |
| ce-core/ledger.md | Cost line format; per-client rollup |
| ce-core/lessons.md | Engine-lessons memory format (process only, never brand taste) |
| ce-core/naming.md | File/folder convention across engines and clients |
| ce-realism/intake.md, ce-cinematic/intake.md, ce-motion/intake.md, ce-web/intake.md | Engine-specific gap questions |
| ce-realism/sound.md, ce-cinematic/sound.md, ce-motion/sound.md | Sound thinking per engine |
| ce-realism/ai-tells.md | Hands, label text, eye line, lip sync, room constancy, voice cadence |
| clients/_template/ | brief, brand-bible, client-rules (empty by default), assets/, decisions.md, ledger.md, outputs/ |

## 5. Migration order

1. Write the 9 new Core files from this doc (no code, one day).
2. Create ce-core repo; move Core-bound files; rewrite ce-core/SKILL.md onto the spine.
3. Create clients/_template and move LIV Body into clients/liv-body (brief, bible, rules, assets, decisions, V1/V2 outputs).
4. ce-web first (LIV Body is live work): move web files, rewrite homepage onto the spine, add freeze/deploy procedure. Test on the LIV Body site build.
5. ce-realism second (LIV Body UGC is next work). Test on a Sarah/creatine reel.
6. ce-cinematic third. Test on the Greens cinematic reel.
7. ce-motion fourth. Test on a LIV carousel.
8. ce-app last, when there's a job for it.
9. Archive the old creative_engine repo read-only.

## 6. Decisions (2026-10-16)
- Repo names as above.
- Core is a git submodule in each engine now; switch to tagged copies when handed to the team.
- Routing is by role; Higgsfield fills the roles today, ElevenLabs = voice, After Effects/code = finish. Swap = one row.

## 7. Status
Step 1 done: the 9 Core files are drafted in `v3/ce-core/` of this repo (README, intake, storyboard, tickets, export-table, tools/routing, freeze, ledger, lessons, naming). Step 2 done: github.com/GraysonChoate/ce-core is live (3.0.0, 35 files, commit babe8ec). SKILL.md rewritten on the spine. Step 3 done: ce-core/clients-template/ and `Liv Body/2026-10-16_v3-client-folder/` on the Mac (brief, bible, client-rules, decisions, ledger, assets pointers, homepage job). Step 4 done: github.com/GraysonChoate/ce-web is live (3.0.0, commit d5dabed) with ce-core as submodule `core/`. SKILL.md (homepage), site.md, intake.md, responsive.md, deploy.md, lessons.md, library/. Next: test ce-web on the LIV Body real build; then step 5, ce-realism.
