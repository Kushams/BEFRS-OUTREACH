# BEFRS European Restaurant Outreach Database — Progress Tracker

## Status
- Project started: (fill in on first real session)
- Batch 001: starting now, target 500.
- Grand total: 0.

## Scope
- This branch (`claude/europe-restaurant-email-database`) is a separate,
  independent lead-collection effort from the US database on
  `claude/us-restaurant-email-database-y8g2j2`. Do not cross-reference or
  merge data between the two branches — they are intentionally isolated
  so European and US leads never collide or get deduplicated against
  each other.
- Countries/regions: TBD by the operator on first use — e.g. UK, Ireland,
  France, Italy, Spain, Germany, Netherlands, Portugal, Greece, etc.
  Update this section once scope is confirmed.

## Methodology
- Same verification bar as the US project: every restaurant must have a
  publicly verifiable business email found on an official website,
  contact/reservations page, official social media profile, or a
  corroborated third-party source (press release, tourism board listing,
  official press kit, news article) clearly tied to that specific
  restaurant. Never guess or pattern-construct an email address.
- Columns (note: `State` replaced with `Country` since this is a
  international dataset — adjust here and in existing batch CSVs together
  if the operator wants a different column set, e.g. adding a `Region`
  column for country subdivisions):
  `Restaurant Name,Business Email,City,Country,Website,Source URL`
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
- restaurant_leads_batch_001.csv — starting now, target 500.
