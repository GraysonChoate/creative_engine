---
name: "gauntlet-loop"
description: "Use when producing client-facing visual output (websites, sales decks, landing pages, marketing/social assets) that must not look AI-generated — runs a multi-round adversarial critic loop before calling anything done."
---

# Gauntlet Loop (Design Critic Loop)

Source: Jack Roberts' "AI Automation Vault" — the most-repeated technique in his course. Core premise: **the model that built something cannot grade its own homework.** A fresh-context critic judging the *rendered output* (a screenshot/frame), not the underlying code, catches what the builder is blind to. This is the anti-AI-slop mechanism.

## When to run this
Use for high-value, reusable, or client-facing work: a sales deck, a client website, a landing page, a branded social template. **Skip it for throwaways** — internal drafts, one-off experiments, anything that won't be looked at twice. Running the full loop on low-stakes work burns tokens for no benefit.

## Before starting: ground it
Don't start from a bare prompt. Pull in:
- 1-3 real reference sites/decks that represent the quality bar (e.g. Apple, Linear, Duolingo, Mercury — or client-specific references)
- The existing design system if one exists (typography, color, spacing, component rules) — codify one once and reuse it, don't reinvent per project
- Real brand assets and real content, not lorem ipsum

## The loop

**1. Interview** — before building, ask the requester (or infer from the brief) what this needs to accomplish, who it's for, and what "good" looks like here. Don't skip straight to output.

**2. Pre-flight checklist** — confirm: reference(s) named, design system available or being created, target format/dimensions known, brand assets in hand.

**3. Build** — produce the first-pass output (site, deck, asset).

**4. Teardown** — before critiquing the new work, do a comparison pass: place the new output next to the reference and name concrete gaps — letter spacing, line height, white space, elevation/shadows, hero imagery choice, color palette discipline, visual hierarchy. Specifics, not "looks generic."

**5. Critic rounds** — run three independent critic passes, each in **fresh context** (no memory of how the piece was built), each judging a **rendered frame/screenshot**, not the code:
   - **Brief critic** — does this actually satisfy what was asked? Right audience, right message, right format?
   - **System critic** — does this obey the design system? Consistent type scale, color tokens, spacing rules, component reuse?
   - **Craft critic** — is this well-made on its own terms? Named anti-slop tells to watch for: violet/purple gradients, Inter-for-everything, three-or-six identical cards, frosted glass, default-rounded sections, generic "seamless/innovative/elevate" copy, bounce-on-every-hover.
   
   Each critic gives a pass/fail plus specific, actionable fixes — not vague praise or vague criticism.

**6. Revise** — address every fail from every critic. Don't cherry-pick.

**7. Repeat 5-6** until all three critics pass, or until diminishing returns are obvious (2-3 rounds is typical; more than that usually means the brief or reference was wrong, not that another round will fix it).

**8. Final gate check** — one last look at the whole piece against the original ask before shipping. Does it still solve the actual problem, not just pass the critics?

## Cost discipline
The critic rounds are the expensive part. For anything routine, delegate critic passes to a cheaper/faster model rather than running everything on the flagship model. Reserve full flagship-on-flagship critique for genuinely high-value, reusable templates.

## What this replaces
Don't just eyeball your own output and ship it. Don't ask for "feedback" from the same context that built the thing — it will defend its own choices. The value is entirely in the fresh-context, rendered-output, multiple-independent-judges structure.