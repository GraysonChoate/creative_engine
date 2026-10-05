# Extract D: S07 (Claude + NotebookLM) and S08 (AI websites)

Tags: U = any visual output, S = shared, adapt per branch, F = film-only.

## Techniques

**1. Substance before style** (S08, U, WEB/APP)
Answer the audience questions before any design work. Ask: who is the visitor, the one action, their objections, the vibe, existing brand assets.
Quote: "Remember, it's substance first, then style."

**2. Five-question brief** (S08, S, WEB/APP/IMG)
Write five short bullets: visitor, one action, objections, vibe, brand assets. Feed them to every later step.
Quote: "Who is the website for, not the business, the visitor."

**3. Competitor research via Firecrawl** (S08, S, WEB/IMG/CORE-RESEARCH)
Ask Claude (with the Firecrawl tool) to find 5 top sites in the niche and region, ranked by reviews and SEO. Have it answer the five questions from them, then output a build prompt.
Quote: "find me five of the top performing driveway cleaning websites in Ontario"

**4. Simple ranking rule for "top"** (S08, S, CORE-RESEARCH)
Define "top performer" with a stated score (reviews, search rank) and have Claude show it.
Quote: "based on things like Google reviews or SEO rankings"

**5. Ask Claude the page count** (S08, S, WEB)
After research, ask how many pages the site should realistically have. Do not default to one page.
Quote: "how many pages should this website be realistically"

**6. Sitemap, then wireframe, then style guide** (S08, S, WEB/APP)
Plan in this order: sitemap (section list per page, movable), wireframe, then style guide. Review and reorder sections before any code.
Quote: "site map, wireframe, and then the style guide at the bottom"

**7. One prompt per page** (S08, S, WEB)
Give each page its own prompt, taken from the sitemap step.
Quote: "Each page has its own prompt which is cool"

**8. Palette by asking Claude** (S08, S, WEB/IMG/APP)
Ask Claude for colors that fit the niche, then lock them in the style guide.
Quote: "Blue and teal signals trust."

**9. Export as React, then wire to sitemap** (S08, S, WEB)
Export the wireframe as React. Have Claude bring it into the project, install packages, open on localhost, and link all pages as the sitemap says.
Quote: "wire the website together in line with its sitemap"

**10. Design-skill pass** (S08, S, WEB/APP)
After the wireframe build, run a second pass: install Anthropic's design skill from GitHub and ask Claude to restyle the existing structure.
Quote: "use the below GitHub repo to get anthropics design skill"

**11. Generated assets after layout** (S08, S, WEB/IMG)
Generate site images only once the layout exists. Placeholder images first, real assets second.
Quote: "generate images that are going to be appropriate for the website"

**12. White-background hero assets** (S08, S, WEB/ANIM)
Make hero assets on a plain white background so they embed cleanly.
Quote: "a dirty driveway with a white background like this"

**13. Reference-chained image pair** (S08, S, WEB/ANIM/IMG)
Make image A. Then generate image B using A as a reference so both match exactly (before/after pair).
Quote: "you're basically giving a prompt with this image in mind"

**14. Start/end-frame video transition** (S08, S, WEB/ANIM)
Upload image A as start frame and image B as end frame, then generate a short transition clip.
Quote: "I upload the messy image."

**15. Video as scroll animation** (S08, S, WEB/ANIM)
Have Claude turn the clip into frames that play as the visitor scrolls. Ask Claude to pick where it goes.
Quote: "turn that video into a scroll animation"

**16. Placement without hijacking the page** (S08, S, WEB)
Ask Claude to place the animation near the top, with text on one side. Keep the page's message in front, not the effect.
Quote: "find a great place to insert this in the homepage"

**17. Review loop on links and architecture** (S08, S, WEB)
After the build, go back and forth with Claude until every link, page, and design standard checks out.
Quote: "making sure that everything's connected that all the page links"

**18. Delivery path** (S08, S, WEB)
Ship via a GitHub repo, then Vercel with multiple pages. Claude installs the CLIs.
Quote: "create a GitHub repo for this"

**19. Drop skill files into the project** (S08, U, all)
Put a skill's files in the project folder and tell Claude to use that skill by name.
Quote: "drop those files on the left hand side for the skill"

**20. Prompt-pack skill for asset steps** (S08, S, WEB/ANIM)
One skill file holds three ready prompts: image A, image B, video transition.
Quote: "dirty driveway, pristine driveway, and then the video transition"

**21. Prototype UI in Lovable first** (S07, S, APP/WEB)
Build the look in Lovable, sync to GitHub, clone to Claude Code, run on localhost. Two-way sync lets you edit in either.
Quote: "quickest way to get something that's gorgeous and then it's easy to refine"

**22. Reference image for UI** (S07, S, APP/WEB)
Drop a Dribbble screenshot (or another project) in as the visual reference.
Quote: "I like to get dashboard inspiration from dribble."

**23. Look first, wiring later** (S07, S, APP)
Tell the builder to make the front end only, no integrations. Add data later.
Quote: "Just build the application out plain as it is"

**24. Claude Code drives NotebookLM** (S07, U, CORE-RESEARCH)
Install the NotebookLM CLI skill, sign in once in the browser, and let Claude create notebooks and add sources by command.
Quote: "one command in does what it used to take 15 clicks"

**25. Give Claude the goal, let it choose sources** (S07, U, CORE-RESEARCH)
State the end goal, then let Claude pick and add sources (own work, experts, extra resources).
Quote: "always make sure you give it your end goal"

**26. Bulk-add video sources** (S07, U, CORE-RESEARCH)
Use the YouTube-to-NotebookLM Chrome extension to add a channel or video. Good for reference-ad or creator research.
Quote: "we're going to bulk add videos via Chrome extension"

**27. Words plus numbers** (S07, U, CORE-RESEARCH)
NotebookLM holds text knowledge. Add real metrics (API data) in Claude, then ask one question across both.
Quote: "words plus data equals the full picture"

**28. Export "trapped" notebook text** (S07, U, CORE-RESEARCH)
Ask Claude to save every source's full text into a local folder. Say "full transcript" and use the full-content flag, or you get a fraction.
Quote: "be sure just to be explicit on getting the full transcript"

**29. Check the export** (S07, U, CORE-RESEARCH)
Open a few saved files and confirm the whole text is there.
Quote: "make sure that the entire transcript is there"

**30. Prune sources** (S07, U, CORE-RESEARCH)
Bulk-add freely, then ask Claude to remove the noise.
Quote: "remove the veritassin videos"

**31. Turn research into a skill** (S07, U, CORE-RESEARCH)
End a research session by asking Claude to save it as a reusable skill (sources plus numbers).
Quote: "turn all of this into a skill so that in the future"

**32. Persistent knowledge base** (S07, S, APP/CORE-RESEARCH)
Numbers go in Supabase, text vectors in Pinecone (via Pipedream connector), so a shared app can answer without your laptop.
Quote: "this website you're creating has access to all of that knowledge"

**33. Restart after adding a connector** (S07, U, all)
If a new connector is not seen, quit and reopen Claude, then retry.
Quote: "shut down Claude and open it back up again"

**34. Per-system API key with budget** (S07, U, APP)
Give each system its own key, with a spend cap and one-year expiry. Fall back to a cheaper model at high usage.
Quote: "never have infinite expiry. One year is what you always go for."

**35. Second-brain notebook** (S07 skill file, U, CORE-RESEARCH)
Keep one permanent notebook. Append a summary after each session. Add a project rule: consult it first.
Quote: "always consult my NotebookLM AI Brain notebook first" (skill file)

**36. Ask against chosen sources** (S07 skill file, U, CORE-RESEARCH)
Query specific sources, and use JSON output to get references.
Quote: "notebooklm ask "question" -s src_id1 -s src_id2" (skill file)

**37. Wait for READY** (S07 skill file, U, CORE-RESEARCH)
Do not generate until every source status is ready.
Quote: "until all status=READY" (skill file)

## (a) Tools, skills, links
- Firecrawl (web research MCP), Reloom (sitemap + wireframe + style guide, exports React/Figma/Webflow/HTML), Anthropic design skill (GitHub anthropics/skills), Kie API (cheaper Nano Banana 2), Higgsfield (image and video; Kling 3.0), Vercel + GitHub CLI (deploy), Google Antigravity (editor running Claude Code), "asset generator" and "3D website builder / scroll" skills (course downloads, not available to us).
- NotebookLM (research; free; 1M tokens), notebooklm-py CLI + skill (github.com/jgravelle/notebooklm-py; skyremote skill repo), YouTube-to-NotebookLM Chrome extension, Lovable (UI builder), Supabase (numbers), Pinecone (vectors), Pipedream MCP (connector), OpenRouter (model keys), YouTube Data API v3, Dribbble (UI inspiration), Cloudflare Tunnel + FastMCP (only to use NotebookLM in Cowork).
- NotebookLM output types: podcast, video (styles: classic, whiteboard, kawaii, anime, watercolor, retro-print, heritage, paper-craft), slide deck (PDF/PPTX), infographic (landscape/portrait/square), report, mind map, data table, quiz, flashcards.

## (b) Numbers
- S08: 5 questions; 5 competitors; 5-10 pages (Claude advised 5-7); Nano Banana 2, 2K, 16:9, 4 images per run (2 ok); Kling 3.0, 5 s, 1080p; Kie ~50% of normal Nano Banana price; Reloom export beyond one page needs paid plan.
- S07: 1M-token context; example notebook 91 sources (2 private failed); 385 before pruning; last 10 videos, 12 months, 20 extra resources; 126 videos in Supabase; 80,000 vectors; localhost 8080; Sonnet about 1/5 the cost of Opus; key expiry 1 year; Python 3.10+ for CLI; generation times: audio 10-20 min, video 15-45 min, quiz 5-15 min; rate limit wait 5-10 min.

## (c) Conflicts with our rules
- Edit prompts one line at a time first: CONFLICT. S08 sends large multi-part prompts (restyle whole site, generate images, install skill in one go) and praises "one shot". S07 Lovable flow is iterative and agrees with us.
- Spectacular tier on any page: no conflict. S08 adds spectacular effects to the homepage only; ours is wider.
- Keep beats short: no conflict (5 s clip).
- Real packshots/logos real: CONFLICT. S08 generates all site images, including generated before/after "proof" for a service business. Placeholders are fine; generated results must not stand in for real work or products.
- Text in code: no conflict (React export keeps text in code).
- Gap: S08 has no QA gate before deploy beyond "spar back and forth". We keep our audit gate.
