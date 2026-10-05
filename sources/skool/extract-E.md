# Extract E: S09 (Cinematic AI Website Builds) and S10 (Cowork marketing skills)

Tags: U = any visual output, S = shared (adapt per branch), F = film-only. Quotes are verbatim from the transcripts.

## Gap warning (S09)
The transcript does NOT cover: scroll-linked playback, frame extraction, ffmpeg or compression, mobile or page weight, poster fallbacks, formal QA. Only a hero background video that loops. Do not assume more.

## S09 techniques

1. **Start from a base site, then reskin** [S, WEB, S09]. Clone a ready GitHub site template, or generate a baseline page from a prompt builder (business type, style, sections, button text). Have Claude rework it for the brand.
   Quote: "the prompt builder is that we can enter whatever we want"

2. **Baseline first, video second** [S, WEB, S09]. Get a working page with real structure before adding video.
   Quote: "now we have a baseline of a website that we like"

3. **Blank page fix** [U, WEB, APP, S09]. If the page loads black, open browser inspect, copy the error, paste it to Claude, reload.
   Quote: "come down to inspect, and it'll tell you exactly what the issue is"

4. **Image prompt first, via a Seedance skill** [S, WEB, CINE, IMG, S09]. A skill writes the still-image prompt. It asks where the image will be used (website, placement) so the composition fits.
   Quote: "what's your vision? Is it going to be on your website?"

5. **Logo as reference image** [S, WEB, IMG, CINE, S09]. Paste the logo into the image tool as a reference and ask for it on the product. The demo used a fictitious logo; he says to use the brand's own.
   Quote: "I would like this logo to be visible on the bag, please."

6. **Image settings** [S, WEB, S09]. Nano Banana 2, 16:9, 2K, 4 variants. Pick the one that keeps the logo true. Use landscape for full-bleed heroes and square when text sits beside the product.
   Quote: "Nano Banana 2, 16 by 9, 2K, and do four out of four images"

7. **Download the original file** [U, S09]. Right-click saves a low-quality copy. Use the real download.
   Quote: "If you right click and save it, it won't be high quality."

8. **Seamless 360 product loop** [S, WEB, ANIM, S09]. Give the same still as first frame and last frame. Prompt for a spin on its axis that ends in the same place. The looping skill automates this.
   Quote: "spinning on its axis as it kind of rotates and ends in the same place"

9. **Use a tool that allows start and end frames** [S, WEB, ANIM, CINE, S09]. In his test the Higgsfield UI did not allow start+end frames with Seedance; Kling 3.0 did. He used Kie.ai instead (cheapest he found).
   Quote: "cannot actually use a start frame and an end frame when you're using Seedance"

10. **Clip settings** [S, WEB, ANIM, S09]. 720p, 16:9, about 7 seconds. Reference image, video and audio URLs are accepted.
    Quote: "Duration I found 7 seconds to be a nice little sweet spot"

11. **Hero video wiring** [S, WEB, S09]. Tell Claude the downloaded file name; make it the first hero element, looping background, with enough contrast against the text.
    Quote: "sufficient contrast between that and the text in front of it"

12. **Darken the video edges in code** [S, WEB, S09]. Darken the edges so the clip blends into the page.
    Quote: "you can darken the edges so it feels like it blends in"

13. **Chat to refine, then ship** [U, WEB, S09]. Iterate with Claude, push to GitHub (CLI connect if needed), import into Vercel, deploy with the standard preset.
    Quote: "create a new GitHub repo, please, and publish this website there."

14. **Flash is not enough** [S, WEB, S09]. Pair the cinematic hero with a conversion wireframe and structure.
    Quote: "we need a website that actually converts"

## S10 techniques

15. **Scoring matrix for trends** [S, IMG, UGC, ANIM, CINE, WEB, S10]. Score each signal 1 to 5 per factor (out of 20): recency (7-day cap), authority, velocity, relevance. Confirm the matrix with Claude before running.
    Quote: "Each factor scored 1 to 5 out of 20."

16. **Trend scan through Grok on X** [S, IMG, UGC, S10]. Claude opens X in Chrome (signed in), questions Grok, and pushes back until satisfied. Free alternative to paid listening tools.
    Quote: "Claude can open up X, have conversations with Gro"

17. **Make it a scheduled task** [U, S10]. Once the output is right, schedule it.
    Quote: "I want this to run every day for me at 9:00 a.m."

18. **Competitor scrape table** [S, IMG, UGC, S10]. Via Apify, pull the last 5 reels per account: likes, comments, shares, description. Put results in a table. Give it named competitors, do not let it pick.
    Quote: "we want to guide it all the way through."

19. **NotebookLM research notebook** [S, UGC, CINE, S10]. Build a notebook of 50+ sources from top creators; extract hook and storytelling frameworks. Result in his demo: 204 sources.
    Quote: "fill that with 50 plus resources"

20. **Batch branded designs from one template** [S, IMG, S10]. Brand kit once, master template, then a list of headlines. Short text, centered.
    Quote: "no more than seven words per slide, put it in the middle"

21. **One-prompt HTML dashboard** [S, WEB, APP, S10]. Feed connectors into a single HTML view.
    Quote: "This revenue dashboard is just something that I built in one prompt."

22. **Eval a new skill** [U, S10]. "Run evals" tests a skill against what Claude does unaided; if it does not beat that, it is not used.
    Quote: "test this skill to see if it beats what code could do automatically"

## (a) Tools, skills, links named
- Claude Code, Anti-gravity (IDE): run the build.
- GitHub + Vercel: host and deploy (free tier implied).
- Higgsfield: image generation; video with Kling 3.0 (start/end frame works).
- Kie.ai (/seedance-2-0): cheapest Seedance access, start/end frame plus reference URLs. He notes it was taken temporarily offline.
- Nano Banana 2: product still with logo. Midjourney: source for logo ideas.
- Seedance skill (free): writes image and animation prompts, asks the use context.
- **Claude Looping .skill (NOT opened):** per transcript, it generates videos that repeat seamlessly without looking "cranky"; used with Seedance 2.0.
- Prompt-builder web page and "gorgeous website" repo (his links, not given).
- Apify custom connector (OAuth, 20,000+ scrapers). Claude in Chrome for Grok/X.
- NotebookLM skill (notebooklm-py CLI; podcast, video, slides, quiz, infographic outputs; unofficial API). Canva connector. Notion. Contract review skill (skip).

## (b) Numbers
- Build a baseline site: about 5 min (his claim). Clip: 7 s; 720p; 16:9. Stills: 2K; 4 variants.
- Matrix: 1-5 per factor, total 20; recency 7 days. Schedule: 9:00 a.m. daily.
- Apify: 20,000+ scrapers. Canva batch: 10 slides, 7 words max. NotebookLM: 50+ sources, 204 achieved.
- NotebookLM generation times: audio 10-20 min, video 15-45 min. Social listening tool cost cited: $800/month (skip).
- Credits/prices for Seedance: not stated.

## (c) Conflicts with existing rules
- **Prompts edited one line at a time first:** CONFLICT. He pastes a whole generated prompt and says "redo the whole thing". Keep our rule.
- **Spectacular web tier on any page:** no conflict; supports the tier plus conversion structure (item 14).
- **Keep beats short:** no conflict (7 s clips, 1 loop).
- **Real packshots/logos always real images:** CONFLICT. The workflow generates the product and logo with AI, and he shows a fictitious logo. Generated logos can warp. Keep our rule: real packshot/logo as reference only and composite or verify the real file; never ship a generated logo.
- **Text set in code:** no conflict. Hero text sits over the video in the page. A logo baked into the video is the risk, see above.
- Also: tool limits (Higgsfield no start/end frame with Seedance) may be out of date. Verify in our own Higgsfield tools before relying on it.
