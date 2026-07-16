# BEFRS Restaurant Outreach Database — Progress Tracker

## Status
- Project started: 2026-07-15
- Current batch in progress: 001 (partial checkpoint saved, still filling toward 500)
- Total verified restaurants collected so far: 86
- Target milestone: 1,500 (no upper limit; continue until sources exhausted)
- Note: Region pass 1 was interrupted by a WebSearch/WebFetch tool session-usage
  limit (message: "You've hit your session limit, resets 1:30am UTC"). 6 of 10
  region agents completed fully; 4 (Mid-Atlantic, Midwest East, Southwest, West
  Coast) were cut off with zero verified results and must be re-run from scratch
  on resume. Direct curl fetches to specific known URLs still work; general web
  search via curl (DuckDuckGo) is blocked by a bot challenge, so real search
  requires the WebSearch tool to be available again.

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
- restaurant_leads_batch_001.csv — 86 restaurants saved (checkpoint, need ~414 more to complete batch 001)

## Next Steps On Resume
1. Re-run region agents for: Mid-Atlantic (NY/NJ/PA/DE/MD/DC), Midwest East (OH/MI/IN/IL/WI),
   Southwest (TX/OK/NM/AZ), West Coast (CA/OR/WA/AK/HI) — these have zero verified restaurants.
2. Run a "gap-fill" pass for the partially-covered regions listed above, targeting the
   specific cities/states noted as thin or missing.
3. Continue until batch 001 reaches ~500, then start batch 002 with a fresh set of
   cities/towns not yet covered (use this file's Coverage Log + the batch CSV's own
   restaurant list as the exclusion list — never re-search a city already exhausted
   without new candidates).

## Exclusion List
Full exclusion list (names + emails already collected) lives inside each
batch CSV. Before starting new research, the latest batch CSV(s) must be
loaded and treated as the exclusion list.
