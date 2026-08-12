# BEFRS Restaurant Outreach Database — Progress Tracker

## Status
- Project started: 2026-07-15
- **Batch 001: COMPLETE — 508 verified restaurants.**
- **Batch 002: COMPLETE — 500 verified restaurants, no dupes vs batch 001.**
- **Batch 003: COMPLETE — 500 verified restaurants.**
- **Batch 004: COMPLETE — 504 verified restaurants.**
- Batch 005: starting now, target 500.
- Grand total: 2,012 — past the 2,000 milestone.
- User instruction (2026-07-22): do NOT stop at 1,500 — keep collecting
  batch after batch until US sources are reasonably exhausted. This
  instruction stands indefinitely; there is no new upper target.
- Dedup process: for every new agent result, grep the candidate email
  (case-insensitive) against ALL existing batch CSVs before appending.
  Also check restaurant names — same restaurant sometimes reappears with a
  different email variant; keep only the first-collected entry. Same-name
  restaurants in DIFFERENT cities/states with different emails are kept
  (e.g. "Odd Duck" in Austin TX and Milwaukee WI are different businesses).

## Methodology
- Nationwide coverage via regional research passes (see Region Groups below).
- Each restaurant must have a publicly verifiable business email found on an
  official website, official contact/reservations page, official social
  media profile, OR (as of 2026-07-17, user-approved) a corroborated
  third-party source — e.g. a press release, chamber of commerce listing,
  franchise/press kit, or news article — as long as the email is clearly
  tied to that specific restaurant (matches its domain/name, not a generic
  aggregator placeholder). This was loosened from "official site only" to
  increase throughput, since most independent restaurants only publish a
  phone number or contact form and don't have a fetchable email on their
  own site. Source URL recorded for every email regardless of source type.
- Still never guess/pattern-generate an email (e.g. assuming info@domain.com
  without seeing it anywhere). Still drop anything that can't be tied to a
  specific, currently-operating restaurant.
- Dedup key: restaurant name + city/state, AND email address (both must be
  unique across the whole database).

## Region Groups (used to parallelize research across the whole US)
1. Northeast: ME, NH, VT, MA, RI, CT
2. Mid-Atlantic: NY, NJ, PA, DE, MD, DC
3. Southeast: VA, WV, NC, SC, GA
4. Florida: FL
5. Deep South: TN, KY, AL, MS, LA, AR
6. Midwest East: OH, MI, IN, IL, WI
7. Midwest West: MN, IA, MO, ND, SD, NE, KS
8. Southwest: TX, OK, NM, AZ
9. Mountain West: CO, UT, WY, MT, ID, NV
10. West Coast: CA, OR, WA, AK, HI

## Coverage Log (per region group, per pass)
| Region Group | Pass 1 status | Notes |
|---|---|---|
| 1. Northeast | partial (14) | No NH restaurant verified yet. ME/VT/MA/CT/RI covered lightly. |
| 2. Mid-Atlantic | not started (0) | Agent failed immediately on tool-limit, no results returned. |
| 3. Southeast | partial (19) | SC thin (1 only). WV/VA/NC/GA covered. Need Hilton Head, Myrtle Beach, Savannah, Tybee, Outer Banks. |
| 4. Florida | partial (13) | Miami, Orlando, Tampa, Keys not yet covered. |
| 5. Deep South | partial (14) | Need Nashville, Little Rock, Jackson MS, Shreveport, Tuscaloosa, Gulf Shores. |
| 6. Midwest East | not started (0) | Agent failed immediately on tool-limit, no results returned. |
| 7. Midwest West | partial (9) | SD has zero entries. Need Sturgis, Rapid City, Bismarck, Cedar Rapids, Wichita, Duluth, Iowa City. |
| 8. Southwest | not started (0) | Agent failed immediately on tool-limit, no results returned. |
| 9. Mountain West | partial (17) | Need Denver, Las Vegas, Cheyenne, Fort Collins, Grand Junction, Estes Park, Big Sky, Coeur d'Alene. |
| 10. West Coast | not started (0) | Agent failed immediately on tool-limit, no results returned. |

## Batch Files
- restaurant_leads_batch_001.csv — COMPLETE, 508 restaurants, all 50 states + DC.
- restaurant_leads_batch_002.csv — COMPLETE, 500 restaurants.
- restaurant_leads_batch_003.csv — COMPLETE, 500 restaurants.
- restaurant_leads_batch_004.csv — COMPLETE, 504 restaurants.
- restaurant_leads_batch_005.csv — starting now, target 500.

## Next Steps
1. Continue deepening coverage across all 50 states — most cities so far only
   have a handful of restaurants sampled, not an exhaustive list, so there is
   plenty of room to keep finding new independents in already-touched cities
   as well as reaching brand-new towns.
2. Verification policy (updated 2026-07-17, user-approved): accept an email
   found either (a) live on the restaurant's own official site, or (b)
   corroborated by a reputable third-party source (press release, chamber of
   commerce/tourism listing, official press kit, news article, Michelin guide,
   OpenTable page showing the restaurant's own domain) clearly tied to that
   specific restaurant. Never guess/pattern-construct an email.
3. Process: launch 2-3 parallel research agents per wave, each with a tool-call
   budget (~40-50 calls) and a target city list, merge+dedupe+commit after each
   wave lands. If an agent goes idle without reporting, use SendMessage to
   resume it and ask for immediate results rather than waiting indefinitely.
4. Dedup: always grep the candidate email against ALL existing batch CSVs
   before appending (agents don't know about each other's or prior waves'
   results).

## Exclusion List
Full exclusion list (names + emails already collected) lives inside each
batch CSV. Before starting new research, the latest batch CSV(s) must be
loaded and treated as the exclusion list.
