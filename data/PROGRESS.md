# BEFRS Restaurant Outreach Database — Progress Tracker

## Status
- Project started: 2026-07-15
- Current batch in progress: 001
- Total verified restaurants collected so far: 0
- Target milestone: 1,500 (no upper limit; continue until sources exhausted)

## Methodology
- Nationwide coverage via regional research passes (see Region Groups below).
- Each restaurant must have a publicly verifiable business email found on an
  official website, official contact/reservations page, or official social
  media profile. Source URL recorded for every email.
- No guessed/pattern-generated emails. No third-party-directory-only emails
  unless the directory is quoting the restaurant's own published address.
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
| 1. Northeast | not started | |
| 2. Mid-Atlantic | not started | |
| 3. Southeast | not started | |
| 4. Florida | not started | |
| 5. Deep South | not started | |
| 6. Midwest East | not started | |
| 7. Midwest West | not started | |
| 8. Southwest | not started | |
| 9. Mountain West | not started | |
| 10. West Coast | not started | |

## Batch Files
- restaurant_leads_batch_001.csv — in progress

## Exclusion List
Full exclusion list (names + emails already collected) lives inside each
batch CSV. Before starting new research, the latest batch CSV(s) must be
loaded and treated as the exclusion list.
