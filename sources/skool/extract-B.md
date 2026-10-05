# Extract B: S03 (motion graphics) + S04 (design teardown)
Format: Name | do | quote | tag | branches | lesson

## Techniques
1. **Real data into animated chart** | Give real numbers plus a style ask (colors, logos, gradients). Iterate until right. | "take real data, real numbers, and animate them" | S | ANIM, WEB | S03
2. **Codify approved style as reusable asset** | Once a chart looks right, save it as a rule for all future charts of that type. | "use this exact style for all future bar charts" | U | ANIM, IMG, WEB, APP | S03
3. **Font is the main slop tell: set it on purpose** | Name a specific font. Do not accept the default. | "drastically changes the perception" | U | all | S03
4. **Pull fonts from a live site (Firecrawl branding)** | Scrape a reference URL with the branding format to get fonts and logos. Tell Claude to build the design system from that font or a close one. | "drop in the URL and under format, come down and check on branding" | U | WEB, IMG, APP | S03
5. **Font match from a screenshot** | Find a font in a real-use gallery, screenshot it, ask Claude for the closest free font. Buy the font if the brand is long-term. | "find something as close as possible to this" | U | IMG, WEB, ANIM | S03
6. **One icon style per piece** | Download a full icon pack in one style and feed it to Claude. Do not mix styles. | "each presentation, you use one style" | S | ANIM, IMG, WEB | S03
7. **Lottie JSON library** | Download Lottie JSON files, put them in a library/repo, share with Claude. Check each license first. | "create a library, create a repository, and share it with Claude" | S | ANIM, WEB | S03
8. **Generated art dropped into motion** | Generate an image (16:9, 2K) with an image model, then hand it to Claude Design to insert. | "Hey, add this into the end" | S | ANIM, WEB, IMG | S03
9. **Word-level timestamp transcript** | Have Claude transcribe a video so every word maps to a time. Output as HTML plus a word file. | "every word that you say is mapped to a timestamp" | S | ANIM, UGC, CINE | S03
10. **Find motion-graphic moments in a script** | Ask the skill to pick spots in a transcript where an animation helps, then make clips for those exact moments. | "where a animation would be valuable" | S | ANIM, UGC | S03
11. **Research step before graphics** | Before making stat graphics, scrape real numbers with Firecrawl so the data is not invented. | "do some research with Firecrawl to find interesting insights and statistics" | U | ANIM, IMG, WEB | S03
12. **Build a skill per output type** | Make one skill each for Reels, YouTube, etc. that finds spots, researches, generates, inserts. | "build a Claude skill like this that does anything" | U | all | S03
13. **Show Claude what great looks like** | Slop comes from no good references. Feed real top-tier design systems (palette, type, tokens). | "never seen what good or great design looks like" | U | all | S04
14. **Check the five tells** | Audit output on typography, imagery, hierarchy, color, spacing. | "typography, imagery, hierarchy, color, spacing, some classic telltale signs" | U | all | S04
15. **Apply a reference design system to a new brief** | Paste a reference design system, then ask for the build. Expect a first draft; iterate. | "use this design architecture to go ahead and build for me" | S | WEB, APP, IMG | S04
16. **Ruthless teardown vs reference** | Give your page and a reference page. Ask for a harsh comparison with screenshots, output as concise HTML. | "I want you to be ruthless." | U | WEB, APP, IMG | S04
17. **Name the gaps in measurable values** | Teardown lists gaps (letter spacing, elevation ladder, hero art, radius, line height, shadows) side by side, with hex copy and a drag slider. | "letter spacing is too loose. There's no elevation ladder." | U | WEB, APP, IMG | S04
18. **Critic loop with 3 judges** | Give a benchmark. Three critics check: hits the brief, design quality, visual impact. Loop until the bar is met. | "goes around in a loop until it hits the desired mark" | U | all | S04
19. **Screenshot reference to HTML** | Screenshot a strong reference, run the loop, ask to match its light, vibe, energy. Adapt, do not copy. | "pay close attention to the luminosity, the vibe, the energy" | S | IMG, WEB | S04
20. **Test the output for real** | Send the HTML through an email connector and click the button to confirm it works. | "does the button work? Let's just see if it does." | S | WEB | S04
21. **Quote cost before generating** | Local tool shows model, ratio, resolution, count and credit cost before each run. | "shows you how many credits or how much it's actually costing you" | U | all | S04
22. **Searchable local asset library** | Index images/videos with a cheap vision model so Claude finds assets by content. | "I indexed it with like a really cheap model" | U | all | S04
23. **Style recipe** | Save a named recipe: description plus reference images. Reuse it for consistent output; change one element per run. | "replace the thing in the image with a giant protein shake" | S | IMG, ANIM, WEB | S04

(No F-only technique found. Nothing film-specific in either lesson.)

## (a) Tools / links named
- Claude Design: builds animation/design from a prompt, design system, data.
- Firecrawl: scrape with branding format (fonts, logos); web research; claimed 93% token saving, 22 cents for one scrape.
- fonts.inuse.com, Google Fonts, Fontshare, Open Foundry, Typewolf: font discovery.
- Flaticon (icon packs; ~$8 paid plan, free with attribution), Lordicon (Lottie animations; free ones are Creative Commons).
- Nano Banana Pro 2 / Nano Banana 2: image generation. Higgsfield, Kie AI, OpenRouter, OpenAI named as image/video platforms in the "Design OS".
- Zapier (called "Zapia" in transcript): connector layer to send generated HTML as an email.
- Design-reference site with 2,000+ designs (palette, type, Tailwind/CSS variables, tokens); not named in transcript.
- Email-campaign gallery (shared by George Harley): HTML emails from Apple, Figma, Anthropic.
- Design Loop / Gauntlet Loop: Notion guide https://app.notion.com/p/The-Design-Loop-Free-Guide-3b8e8d6bd13781ff8bf2fc06fd5d0aac
- RTFSkill.zip (NOT opened): per transcript, takes a video (file or YouTube), makes a word-level timestamped transcript, finds animation moments, researches stats with Firecrawl, generates and optionally inserts motion clips, saves to desktop.
- design-teardown-skill.zip (NOT opened): per transcript, compares your site to a reference design, finds gaps, outputs a concise HTML breakdown with slider and copyable hex.
- "Design OS" (community-only): local dashboard, generation with cost shown, searchable library, style recipes. Not available to us.

## (b) Numbers
- 5 levels (S03: data, fonts, icons, Lottie/images, video+skill); 3 levels (S04).
- 5 slop tells; 3 critic agents; 2,000+ designs in reference site.
- Image run: 16:9, 2K, 2 images = about 12 cents (S03 also says 4 credits).
- Firecrawl scrape: 22 cents, 93% fewer tokens.
- Skill suggested 6 clip placements in one video.
- Claim "99% of designs look generic": unsupported.
- No pass/score threshold or loop cap given for the critic loop.

## (c) Conflicts with our rules
- **Real packshots real**: S04 prompts Claude to "generate the images if you need to" for product bottles on a store page. Conflicts. Keep real packshots.
- **Prompts edited one line at a time**: S04 praises one-shot output ("on one simple shot") and one big prompt. Conflicts in spirit; keep our rule.
- **Text set in code**: no conflict. Fonts are set in code. Reinforces it.
- **Spectacular web tier / beats short**: not addressed. No conflict.
- Minor: Lottie/icon packs add third-party assets; license check needed (no rule yet).
