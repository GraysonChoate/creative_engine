# Higgsfield After Effects plugin: does it work with Claude? (researched Oct 7 2026)

## Answer: YES. Higgsfield now officially supports Claude.
Sources: higgsfield.ai/mcp/use-after-effects?tab=claude, higgsfield.ai/plugins/after-effects, alphasignal.ai news.

Three pieces:
1. Higgsfield MCP  https://mcp.higgsfield.ai/mcp  (already connected in our Claude). Models + workflow skills.
2. AE bridge       https://bridge.higgsfield.ai/mcp (custom connector "Higgsfield Bridge"). Relays Claude's actions into AE.
3. Adobe plugin    Mac .dmg installer from higgsfield.ai/plugins/after-effects. Needs AE 2025+. Panel: Window > Extensions > Higgsfield.

Claude can: build comps, animate layers, write expressions, import generated assets, render, return an editable .aep.
Presets (slash skills): /use-after-effects, /saas-animation, /localization-motion, /presentation-animation, /paper-collage, /whiteboard-animation, /illustration-animation.
Page note: "running this workflow requires the desktop software to be connected."
Cost: normal Higgsfield credits. No extra agent fee.
Plugin panel tools: Reframe, Remove Background, Upscale, Draw to edit, Edit Video, plus Generate Video / Image.

## Limits (honest)
- Presets are not visible to us via apps_search (returned nothing). Need to test after bridge is added.
- Stated ceiling: complex character animation, intricate rigging, tightly art-directed performance.
- Confirm AE version is 2025+.
- Third-party option: github.com/LobzyJay/motion-design-with-claude (MIT). Skills: motion-design, aftereffects-motion, motion-design-critique. Uses TheLlamainator/after-effects-mcp (live JSX bridge). Ideas worth copying, not required.

## Our two routes
A. Higgsfield bridge: easiest, official, gives their motion skills.
B. Our own ExtendScript + osascript + aerender via the linked Mac: already proven (3 s comp in 8 s, rendered). Full control, free, no credits.
Plan: use B as the base for the spectacular recipes; add A for presets and generation. Test A with one small job first.

## What the user must do for A (2 min)
1. Download installer at higgsfield.ai/plugins/after-effects, run it with AE closed.
2. Claude settings > Connectors > add custom: name "Higgsfield Bridge", URL https://bridge.higgsfield.ai/mcp. Sign in.
3. Open AE > Window > Extensions > Higgsfield, sign in.
