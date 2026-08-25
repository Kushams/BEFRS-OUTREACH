# BEFRS European Restaurant Outreach Database — Progress Tracker

## Status
- Project started: 2026-08-25.
- Batch 001: IN PROGRESS — 421/500 rows (UK 45, Germany 38, Italy 74,
  Spain 29, Netherlands 33, Portugal 21, Switzerland 28, Austria 15,
  Ireland 20, Belgium 23, Denmark 12, Sweden 9, Norway 9, Finland 8,
  Poland 17, Czechia 8, Hungary 8, Greece 14, Croatia 10).
- Grand total: 421 unique restaurants, 421 unique emails (batch_001
  only — France operator-provided leads tracked separately, see below).

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
- restaurant_leads_batch_001.csv — IN PROGRESS, 326/500 rows so far.
  - United Kingdom (45) — London, Manchester, Edinburgh, Glasgow,
    Bristol, Cardiff, Leeds/Horsforth, Belfast, Brighton, Oxford/
    Cotswolds, Cambridge, York, Bath, Newcastle upon Tyne, Liverpool,
    Birmingham, Padstow, Ullapool, Norwich, Aberdeen, Machynlleth,
    Southampton, Portsmouth.
  - Germany (38) — Berlin, Munich, Hamburg, Cologne, Frankfurt,
    Stuttgart, Düsseldorf, Dresden, Leipzig, Nuremberg.
  - Italy (74) — Rome, Milan, Florence, Venice, Naples, Bologna, Turin,
    Genoa, Verona, Bari.
  - Spain (29) — Madrid, Barcelona, Valencia, Seville, Bilbao, San
    Sebastián, Málaga, Granada, Palma de Mallorca, Zaragoza.
  - Netherlands (33) — Amsterdam, Rotterdam, The Hague, Utrecht,
    Eindhoven, Groningen, Maastricht, Haarlem, Leiden, Delft.
  - Portugal (21) — Lisbon, Porto, Faro, Coimbra, Braga, Funchal,
    Cascais, Sintra, Évora, Albufeira.
  - Switzerland (28) — Zurich, Geneva, Basel, Bern, Lausanne, Lucerne,
    Zermatt, Interlaken.
  - Austria (15) — Vienna, Salzburg, Innsbruck, Graz.
  - Ireland (20) — Dublin, Cork, Galway, Limerick, Kilkenny, Killarney.
  - Belgium (23) — Brussels, Antwerp, Ghent, Bruges, Liège, Leuven.
  - Denmark (12) — Copenhagen, Aarhus, Odense.
  - Sweden (9) — Stockholm, Gothenburg, Malmö.
  - Norway (9) — Oslo, Bergen, Trondheim.
  - Finland (8) — Helsinki, Turku, Tampere.
  - Poland (17) — Warsaw, Kraków, Wrocław, Gdańsk.
  - Czechia (8) — Prague, Brno, Český Krumlov.
  - Hungary (8) — Budapest, Debrecen, Szeged.
  - Greece (14) — Athens, Thessaloniki, Santorini (Fira/Oia), Mykonos,
    Chania, Heraklion, Rhodes/Lindos.
  - Croatia (10) — Zagreb, Split, Dubrovnik, Rovinj.

## Country Progress Tracker
- **United Kingdom, Germany, Italy, Spain, Netherlands, Portugal,
  Switzerland, Austria, Ireland, Belgium, Denmark, Sweden, Norway,
  Finland, Poland, Czechia, Hungary, Greece, Croatia**: wave 1 done
  (major/mid cities covered per city lists above). All still need
  deeper coverage of smaller towns/regions before considered exhausted.
- **France**: SEPARATE TRACK per operator — see "France (operator-
  provided)" section below. Not part of the wave 1 research rotation.
- **Luxembourg, Liechtenstein, Iceland, Estonia, Latvia, Lithuania,
  Malta, Cyprus, Andorra, Monaco, San Marino, Vatican City, Slovakia,
  Slovenia, Albania, Bosnia and Herzegovina, Serbia, Montenegro, Kosovo,
  North Macedonia, Bulgaria, Romania, Ukraine, Moldova, Belarus, Russia,
  Türkiye, Georgia, Armenia, Azerbaijan**: not yet started.
- Next up: Balkans/Baltics (Slovakia/Slovenia, Albania/Serbia/Bosnia,
  Estonia/Latvia/Lithuania), then Eastern Europe (Ukraine, Romania,
  Bulgaria), then the remaining trans-continental countries. After wave
  1 finishes across all countries, start wave 2 passes on smaller
  cities/towns per country for deeper coverage.

## France (operator-provided)
- Operator already had 700+ France leads from another source and
  uploaded 3 files (Paris, general FR, small FR2 supplement — 782 rows
  combined after merge, 0 exact-duplicate emails across the 3 files).
- These live in `data/france_leads_operator_provided.csv` on this
  branch — counted in the grand total but NOT part of the sequential
  `restaurant_leads_batch_NNN.csv` deliverables (operator already has
  this data, no need to redeliver it).
- Validation pass: all 782 emails matched valid email syntax. DNS
  checked all 458 unique domains (A + MX records) — 37 domains have
  neither and are almost certainly dead; these rows are flagged
  `needs_verification=true` in the operator-provided file.
- Any row from the operator file where research finds the email was
  wrong and locates the real one: the CORRECTED row counts as newly
  extracted work and goes into the normal batch_NNN pipeline (not just
  the operator-provided file), per operator instruction.
- Research on the 37 flagged France restaurants is only run if/when
  time allows — France stays otherwise out of the wave rotation.
