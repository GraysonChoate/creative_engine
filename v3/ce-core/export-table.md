# Export table (read at step 4, enforced at step 7)
Edit here only. Engines never restate these.

## Placements
| Placement | Ratio | Px | Length band | Safe zone (keep key content out of) | Notes |
|---|---|---|---|---|---|
| TikTok / Reels / Shorts | 9:16 | 1080×1920 | 15–30 s UGC; 30–60 s cinematic | top 14%, bottom 35%, 6% each side | burned captions inside the safe box |
| Meta feed ad | 4:5 | 1080×1350 | 6–15 s | bottom 10% | crop from 9:16 or 3:4 master |
| Meta / IG square | 1:1 | 1080×1080 | — | — | carousels, stills |
| YouTube | 16:9 | 1920×1080 | 30–90 s | bottom 12% (player UI) | master |
| Site hero (desktop) | 16:9 or 21:9 | 1920×1080 / 2560×1080 | 6–12 s loop | text column side kept clear (declared on ticket) | poster frame required |
| Site section loop | 16:9 | 1920×1080 | 3–8 s loop | — | 1–3 MB |
| Site mobile | 9:16 | 1080×1920 | same | top 10% (nav) | separate crop, not a squeeze |
| Carousel slide | 4:5 or 1:1 | 1080×1350 / 1080×1080 | — | 8% all sides | 10 slides max |
| Pitch deck | 16:9 | 1920×1080 | — | — | |

## Video specs
H.264 MP4, yuv420p, 30 fps (24 for film look; 60 for code-built motion graphics), 1080p minimum. Also WebM for site use (headless Chromium lacks H.264). Audio −14 LUFS, true peak under −1 dB. Site loops 1–3 MB with a poster frame.

## Still specs
PNG for cutouts and anything with text; WebP for site; 2× for retina on site tiles.

## Make once, cut many
Every supplier ticket delivers the master plus every crop the placements need. One generation, every size.

## Shopify / site
Relative paths, assets/ folder, no external calls, under 100 MB per deploy folder, 0 console errors on a full scroll.
