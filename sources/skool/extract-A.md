# Extract A: S01 + S02 (Skool, Claude Design)

Tags: U = any visual output, S = shared (adapt per branch), F = film-only. None found are F.

## Techniques

1. **System, not prompt (S01, U; WEB, APP, IMG)**. Give the model a design system plus references, not one generic prompt. Generic prompts give the same fonts, gradients and cards for everyone.
   Quote: "give it a system, not a prompt"

2. **Slop checklist (S01, S; WEB, IMG)**. Ban the default tells: same typeface, indigo-to-violet gradient, three feature cards, uniform rounding, frosted glass, AI-sounding headline.
   Quote: "the classic indigo to violet fade"

3. **Niche reference pick (S01, S; WEB, APP)**. Give Claude a list of top gallery sites and ask for the 3 closest to the brand's niche. Pick one as primary, add a second as secondary.
   Quote: "find for me three examples that are most closely related to my desired business"

4. **Reference to design system (S01, S; WEB, APP, IMG, ANIM)**. Paste the reference link and say to be inspired by its whole system, adapted to your product. Ask for a design-system page: typography, buttons, colors, login, graphics rules, asset inventory.
   Quote: "you have a fully codified design system here"

5. **Blend references (S01, U)**. Do not copy one site. Combine several designs into your own style.
   Quote: "combine multiple different designs to create something unique"

6. **Gold-standard judge loop (S01, U)**. Name a gold-standard reference. Judges score the output pass/fail against it and loop until it passes. This stops endless "improvements".
   Quote: "various judges that are saying does this hit the mark yes or no"

7. **Pilot first (S01, U)**. Make a small pilot of the new graphics/video, approve the look, then run the full build.
   Quote: "a pilot strategy first to make sure that I like the design"

8. **Own character and graphic style (S01, S; IMG, ANIM, WEB)**. Study the reference's graphics and motion, then make a unique style and character cast for the brand. Human picks the concept (e.g. mascot); AI does the repetition.
   Quote: "create a unique graphic style with unique characters"

9. **Higgsfield CLI inside Claude Code (S01+S02, S; WEB, APP, IMG, ANIM, CINE)**. Connect the CLI once (sign-in opens in browser). Then tell Claude to generate graphics and videos with it for the page.
   Quote: "connect to the Higsfield via the CLI"

10. **Name the video model; loop clips (S01, S; WEB, ANIM, CINE)**. State the video model in the prompt. Make most page graphics short loops with personality. Keep video silent.
    Quote: "using Seed to Dance 2.5 for the best video generations"; "volume of sound, which I don't recommend"

11. **Claude thinks, Higgsfield makes (S02, S)**. Claude writes the prompts; the generator renders. Upload the design system so assets match.
    Quote: "using claude as the kind of design intelligence engine"

12. **Variants, pick winner (S02, U; IMG, WEB)**. Ask for 5 designs (or 4 logo variants), choose one, save it. Use 2K, not 4K.
    Quote: "build me five different designs"

13. **Font curation (S01, U)**. Choose fonts from libraries that show real in-use samples. Match brand personality, trust, readability, kerning. Do this before building.
    Quote: "it actually shows you what fonts look like in real life situations"

14. **Font licence check (S01, U)**. Confirm commercial licence before using a font.
    Quote: "some are free for personal use but commercial will not"

15. **Copy pass with a second model (S01, S; WEB, IMG, UGC, ANIM)**. Run copy through an AI-tell remover (banned words list) using a non-Claude model. Benchmark the top 5 competitors' copy. Rewrite to be specific.
    Quote: "GPT 5.6 just makes it sound a little more human"

16. **Copy principles (S01, S; WEB, IMG, ANIM)**. Don't make me think; name the pain first; one ask per screen; one screen, one point. Use concrete lines ("five minutes on the train counts"; "Start free" over "Get started").
    Quote: "one page, one thought"

17. **Brief like a design director (S02, S; WEB, APP, IMG)**. Give a specific brief plus screenshots from inspiration sites. Never one-shot.
    Quote: "design inspiration that's going to be specific for our project"

18. **Iterate with concrete feedback (S02, U)**. Plan 5-10 rounds. Give specifics: contrast, colors per screen, consistent block height, no more than two sentences per slide, something visual on each slide.
    Quote: "five to 10 different back and forths"

19. **Export project to design system (S02, U)**. Export the finished project as an archive. Use "create a design system", upload it plus logos/fonts/notes, and generate. Re-use the one file everywhere.
    Quote: "click on create a design system at the bottom"

20. **Reuse system across assets (S02, U; IMG, WEB, ANIM)**. Apply the same system to decks, emails, pages. Ask it to explore color/type pairings.
    Quote: "one file that you can use everywhere"

21. **Palette from existing palettes (S02, U)**. Start from proven existing palettes; use a generator and lock colors you like. Do not invent from scratch.
    Quote: "finding existing color palettes that already exist"

22. **HTML motion and 3D one-shots (S02, S; ANIM, WEB)**. Ask Claude Design for an HTML animation or a 3D object (sphere) in the chosen system. Drop it into a page or deck.
    Quote: "create for me a beautiful HTML animation explaining the power of habits"

23. **Share for review (S02, U)**. Publish the design as an artifact to get a public review URL.
    Quote: "I can publish this as an artifact"

24. **App back end (S02, S; APP)**. Install Supabase agent skills so Claude stops guessing. Disable email confirmation while testing. Run the database advisor for security gaps (row-level security, leaked-password protection).
    Quote: "run the superbase database advisor"

## (a) Tools / links named
- Gallery of top sites (Linear, Mercury, Stripe-like; "Willy Wonka's chocolate factory"; filters: popular, newest, search). Name not given.
- Pinterest, Awwwards, Godly, Mobbin, Land-book: reference galleries.
- Coolors (transcribed "cool.co"): palette generator, lock colors.
- Font preview sites (transcribed "fontest.com", "Fonts in Use"): fonts shown in real use.
- Design Loop / Gauntlet Loop skill (Notion guide link): judge loop. Install as a skill, call with /loop.
- Higgsfield CLI/MCP: image, video, character generation.
- Nano Banana Pro, GPT Image 2: image models. "Seed to Dance 2.5" (Seedance): video model.
- GPT 5.6: copy humanizer. Claude Design: design system create/export, publish artifact.
- Supabase + agent skills + database advisor. Book "Don't Make Me Think"; "Daniel Priest" marketing system (pain first).

## (b) Numbers
- 3 reference sites; 1 secondary reference.
- Pilot before full run; loop build took under 5 min.
- 5-10 feedback rounds; 5 variants; 4 logo variants; 2K resolution (4K "overkill").
- Copy pass found 28 changes. Top 5 competitors benchmarked.
- Slides: max 2 sentences. One screen, one point per section.
- Model setting: top Claude model; "extra" vs "high" effort "doesn't make too much difference".

## (c) Conflicts with existing rules
- **One line at a time**: S02 sends several changes in one message (confetti + screens + colors). S01 sends one long prompt. Conflicts.
- **Spectacular tier on any page**: no direct conflict. S01 "one screen, one point" favors restraint, not spectacle.
- **Keep beats short**: consistent (two sentences max per slide).
- **Real packshots/logos always real**: S02 generates a logo and mascot with AI (invented brand). S01 invents characters. Conflicts if used on a real brand.
- **Text set in code**: not stated. S02's AI-generated logo may contain text in the image; treat as conflict for any text beyond a real logo.
