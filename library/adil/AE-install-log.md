# AE tool install log (Oct 7 2026)

CORRECTION to AE-plugin-research.md: the "Higgsfield Bridge" cloud connector is NOT needed for the Claude route.
Higgsfield ships a LOCAL tool: npm package `fnf-after-effects-mcp` (v0.1.3). No panel, no Higgsfield login, no cloud.
Chain: client -> local Node server -> osascript/ExtendScript -> After Effects. The panel is only for generating media inside AE.

Installed on Mac: global npm install, Node 26.5.0, npm 11.17.0, After Effects 2026.
doctor: all checks OK, 13 AE skills verified.
Live test: ae_project_info answered in 245 ms (empty untitled project). AE is controllable.

Tools: ae_get_skill, ae_get_skill_asset, ae_project_info, ae_comp_info, ae_layer_info, ae_render_frame, ae_save_project,
ae_project_export_json, ae_project_import_json, ae_version_info, ae_catalog, ae_do, ae_context.
Policy: write access ON; eval.run (free-form script) DISABLED by default -> our own osascript + .jsx route covers free-form scripts.

Skills (13, served by ae_get_skill): ae-clean-rig (entry point) + animation-principles, build-orchestration, depth-space, design-first,
liquid-glass, mcp-realities, transition-kit, ui-mastery; ae-cleanup, ae-figma-transfer, ae-matte-painting, use-after-effects.
License: code MIT; skills not redistributable. Personal use ok. Our library points to them; never edit them; our layer sits on top.

Probe script on Mac: ~/.ce-ae/probe.mjs (talks to the server over stdio).
Not yet done: registering the server with a Claude client so ae_* tools appear directly in chat.
