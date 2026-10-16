# Tickets (the handoff spec)
A ticket is the order form for one piece. The engine that needs the piece writes it; the engine that makes the piece builds to it and nothing else. Both check against it.

## Fields
| Field | Example |
|---|---|
| ID | T3a (from board row R3) |
| What | Maya scoops creatine into the shaker |
| Made by | Realism (clip) |
| Mode | EXACT |
| Sizes | 9:16 master; 4:5 crop |
| Length | 3 s |
| Loops? | No |
| First frame | Back to camera, tub on counter |
| Last frame | Label sharp, facing camera |
| Text space | Bottom 35% clear (captions) |
| Sound | Scoop scrape, blender start; phone-mic quality |
| Must match | Cast lock MAYA-01, product lock CREAT-01, location lock KITCH-01 |
| Tool | tools/routing.md row "clip, person, no dialogue" |
| Credits | 10 |
| Takes max | 2 |

## Sheet
All tickets for a job on one sheet, in board order, with the total. Shown with the board at the step 4 gate.
```
TICKET SHEET: <job> · <mode> · <n> tickets · <credits> credits
| ID | What | Made by | Sizes | Length | Credits | Takes |
```

## Approval rules
- Paid tickets wait for a yes. One reply covers the sheet ("approved", "drop T6, T5 to 10 s, approved").
- Free tickets (code, layout, edits): EXPLORE logs and goes; EXACT waits with the rest.
- Not on an approved ticket → not built. New idea → new ticket, proposed.
- A ticket that fails its takes cap stops and shows; it does not spend more.

## Checks
- Maker: before handing back, tick every field. First/last frame, text space and locks are the usual misses.
- Taker: on receipt, tick again. A miss goes back with the ticket ID and the failing field, not "feels off".

## Derived fields
Sizes, text space, file limits and codec come from export-table.md by placement. The engine fills them; the user is never asked.
