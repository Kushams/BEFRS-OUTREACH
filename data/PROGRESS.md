# BEFRS European Restaurant Outreach Database — Progress Tracker

## Status
- Project started: 2026-08-25.
- Batch 001: IN PROGRESS — 45/500 rows (UK wave 1 complete; France/Germany
  wave 1 runs were interrupted before producing output and need to be
  redone).
- Grand total: 45 unique restaurants, 45 unique emails.

## Scope
- This branch (`claude/europe-restaurant-email-database-xq7t80`) is a
  separate, independent lead-collection effort from the US database on
  `claude/us-restaurant-email-database-y8g2j2`. Do not cross-reference or
  merge data between the two branches — they are intentionally isolated
  so European and US leads never collide or get deduplicated against
  each other.
- Geographic scope: the entire European continent (not just EU), per
  operator instructions — UK, Ireland, France, Belgium, Netherlands,
  Luxembourg, Germany, Switzerland, Austria, Liechtenstein, Denmark,
  Sweden, Norway, Finland, Iceland, Estonia, Latvia, Lithuania, Spain,
  Portugal, Italy, Greece, Malta, Cyprus, Andorra, Monaco, San Marino,
  Vatican City, Poland, Czechia, Slovakia, Hungary, Slovenia, Croatia,
  Albania, Bosnia and Herzegovina, Serbia, Montenegro, Kosovo, North
  Macedonia, Bulgaria, Romania, Ukraine, Moldova, Belarus, Russia,
  Türkiye, Georgia, Armenia, Azerbaijan. Search whole countries (capitals
  + major/medium/small cities + towns), not just capitals, and use
  local-language search terms alongside English.

## Methodology
- Same verification bar as the US project: every restaurant must have a
  publicly verifiable business email found on an official website,
  contact/reservations page, official social media profile, or a
  corroborated third-party source (press release, tourism board listing,
  official press kit, news article) clearly tied to that specific
  restaurant. Never guess or pattern-construct an email address.
- Columns (note: `State` replaced with `Country` since this is an
  international dataset, plus a `Region/State` column added for the
  first-level administrative subdivision — e.g. England's regions,
  Scotland/Wales/Northern Ireland, German Bundesländer, French régions,
  Italian regioni, etc. — since Europe doesn't use "states" uniformly):
  `Restaurant Name,Business Email,City,Region/State,Country,Website,Source URL`
- Dedup key: restaurant name + city/country, AND email address (both must
  be unique across the whole database on this branch).
- Batch size: 500 rows per file, saved as
  `data/restaurant_leads_batch_NNN.csv`. Never stop at any milestone —
  keep going batch after batch until European sources are reasonably
  exhausted, matching the standing instruction on the US project.

## Process
1. Refresh this branch (`git fetch` + `git log HEAD..origin/... --oneline`,
   pull if needed) before every research pass and before every commit —
   this branch may be worked from multiple sessions over time.
2. Launch parallel research agents per wave (2-3 at a time), each targeting
   a country or region with a tool-call budget (~40-50 calls).
3. Before appending any new lead, grep the candidate email
   (case-insensitive) against ALL existing batch CSVs on this branch, and
   grep candidate restaurant names to catch same-business email-variant
   duplicates. Same-name restaurants in different cities/countries with
   different emails are kept as separate rows (they are different
   businesses).
4. If the same restaurant has multiple verified emails, keep ONE row and
   put all addresses in the Business Email cell, semicolon-separated
   (e.g. `reservations@example.com; events@example.com`) — do not create
   duplicate rows for the same restaurant.
5. Commit and push after each merge with a descriptive message stating the
   new batch total and grand total.
6. Deliver each completed batch (500 rows) to the user as a CSV file
   immediately upon completion, and give brief status updates after each
   merge (batch total + grand total).

## Batch Files
- restaurant_leads_batch_001.csv — IN PROGRESS, 45/500 rows so far.
  - Countries covered so far: United Kingdom (45) — London, Manchester,
    Edinburgh, Glasgow, Bristol, Cardiff, Leeds/Horsforth, Belfast,
    Brighton, Oxford/Cotswolds, Cambridge, York, Bath, Newcastle upon
    Tyne, Liverpool, Birmingham, Padstow, Ullapool, Norwich, Aberdeen,
    Machynlleth, Southampton, Portsmouth.

## Country Progress Tracker
- **United Kingdom**: wave 1 done (45 restaurants). Still needs deeper
  coverage of smaller towns/regions before considered exhausted.
- **France**: not yet started (wave 1 attempt was interrupted, no data
  collected — redo from scratch).
- **Germany**: not yet started (wave 1 attempt was interrupted, no data
  collected — redo from scratch).
- **Ireland, Belgium, Netherlands, Luxembourg, Switzerland, Austria,
  Liechtenstein, Denmark, Sweden, Norway, Finland, Iceland, Estonia,
  Latvia, Lithuania, Spain, Portugal, Italy, Greece, Malta, Cyprus,
  Andorra, Monaco, San Marino, Vatican City, Poland, Czechia, Slovakia,
  Hungary, Slovenia, Croatia, Albania, Bosnia and Herzegovina, Serbia,
  Montenegro, Kosovo, North Macedonia, Bulgaria, Romania, Ukraine,
  Moldova, Belarus, Russia, Türkiye, Georgia, Armenia, Azerbaijan**: not
  yet started.
- Next up: France and Germany (wave 2), then Italy/Spain/Netherlands
  (wave 3).
