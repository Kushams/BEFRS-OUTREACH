# BEFRS European Restaurant Outreach Database — Progress Tracker

## Status
- Project started: 2026-08-25.
- Batch 001: COMPLETE (closed over the 500 target, per operator: don't
  bother trimming to exactly 500, just start the next batch fresh) —
  558/500 rows (UK 45, Germany 38, Italy 74, Spain 29, Netherlands 33,
  Portugal 21, Switzerland 28, Austria 15, Ireland 20, Belgium 23,
  Denmark 12, Sweden 9, Norway 9, Finland 8, Poland 17, Czechia 8,
  Hungary 8, Greece 14, Croatia 10, Estonia 8, Latvia 8, Lithuania 10,
  Slovakia 7, Slovenia 8, Serbia 7, Bosnia and Herzegovina 5, France 84
  [13 corrections + 71 deep-search wave 6, see below]).
- Batch 002: COMPLETE (closed over the 500 target, same convention as
  batch 001 — don't trim, just close and start fresh) — 522 rows
  (Luxembourg 5, Iceland 5, Malta 8, Cyprus 19, Romania 19, Bulgaria 10,
  Albania 10, Montenegro 11, Kosovo 6, North Macedonia 9, Türkiye 9,
  Georgia 4, Armenia 2, Azerbaijan 2, Ukraine 10, Moldova 3, Andorra 2,
  Monaco 3, San Marino 1, Germany [wave 1+2] 77, United Kingdom
  [wave 1+2] 71, Liechtenstein 7, Belarus 2, Russia 9, Italy [wave 2] 36,
  Netherlands [wave 2] 18, Portugal [wave 2] 10, Spain [wave 2] 30,
  Denmark [wave 2] 10, Sweden [wave 2] 8, Norway [wave 2] 13, Finland
  [wave 2] 8, Switzerland [wave 2] 25, Austria [wave 2] 7, Belgium
  [wave 2] 14, Ireland [wave 2] 13, Poland [wave 2] 18, Czechia
  [wave 2] 7, Hungary [wave 2] 9, Estonia [wave 2] 4, Latvia [wave 2] 4,
  Lithuania [wave 2] 3, Bosnia and Herzegovina [wave 2] 3, Serbia
  [wave 2] 3, Slovakia [wave 2] 3, Slovenia [wave 2] 5, Greece
  [wave 1+2] 25, Croatia [wave 1+2] 20, France [wave 7] 29).
- Batch 003: IN PROGRESS — 442 rows (Romania [wave 2] 9, Bulgaria
  [wave 2] 3, Türkiye [wave 2] 9, Georgia [wave 2] 4, Armenia
  [wave 2] 1, Italy [wave 3] 29, Malta [wave 2] 4, Cyprus [wave 2] 6,
  Iceland [wave 2] 5, France [wave 8] 32, United Kingdom [wave 3] 43,
  Spain [wave 3] 27, Netherlands [wave 3] 17, Portugal [wave 3] 11,
  Ukraine [wave 2] 9, Moldova [wave 2] 2, Albania [wave 2] 4, Kosovo
  [wave 2] 7, Montenegro [wave 2] 2, North Macedonia [wave 2] 3,
  Denmark [wave 3] 7, Sweden [wave 3] 7, Norway [wave 3] 4, Finland
  [wave 3] 7, Germany [wave 3] 65, Poland [wave 3] 16, Czechia
  [wave 3] 15, Hungary [wave 3] 11, Italy [wave 4] 43, France
  [wave 9] 33, Spain [wave 4] 30, Netherlands [wave 4] 12, Belgium
  [wave 3] 21). Batch 003 is now CLOSED (closed over the 500 target,
  same convention as batch 001/002 — don't trim, just close and start
  fresh) — 505/500 rows. Per-city breakdown for the final merge
  (Netherlands/Belgium wave 4): Mechelen 4, Groningen 3, Arnhem 3,
  Hasselt 3, Kortrijk 3, Leuven 3, Mons 3, Enschede 2, Haarlem 2,
  Tilburg 2, Breda 1, Maastricht 1, Malonne (Namur) 1, Namur 1,
  Nijmegen 1 (7 of the agent's 40 finds duplicated already-covered
  restaurants and were dropped).
- Batch 004: IN PROGRESS — 158 rows (United Kingdom [wave 4] 34,
  Austria [wave 3] 22, Switzerland [wave 3] 20, Greece [wave 3] 10,
  Croatia [wave 3] 8, Portugal [wave 4] 39, Romania [wave 3] 15,
  Bulgaria [wave 3] 10). Per-city breakdown for the most recent
  merge (Romania/Bulgaria wave 3): Stara Zagora 4, Brasov 3,
  Craiova 3, Oradea 3, Ruse 3, Constanta 2, Pleven 2, Sibiu 2,
  Targu Mures 2, Veliko Tarnovo 1 (4 of the agent's 30 finds were
  duplicates and dropped; one pair of same-operator sibling
  restaurants sharing one contact email — Tempo Restaurant and Laci
  Csarda in Târgu Mureș — was collapsed to a single row to avoid
  double-counting one inbox).
- Grand total across branch: 2,525 unique restaurants (558 batch_001 +
  522 batch_002 + 505 batch_003 + 158 batch_004 +
  782 france_leads_operator_provided.csv, tracked separately per
  operator instruction — see "France" section below).
- **All countries in the original scope now have at least a wave 1
  pass** (Vatican City confirmed to have none; everything else has
  data). Wave 2 (smaller towns) done so far for: UK, Germany, Italy,
  Netherlands, Portugal, Spain, Denmark, Sweden, Norway, Finland,
  Switzerland, Austria, Belgium, Ireland, Poland, Czechia, Hungary.
  Continuing wave 2 across remaining countries (France, Greece/
  Croatia, Balkans, Baltics, small states, Türkiye/Caucasus, Eastern
  Europe).

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

## Search method upgrade (per operator, applies to all waves going forward)
Operator asked for a much more intensive/deep search across every possible
public source, not just official restaurant websites. Every wave from this
point on should actively pull verified emails from ALL of these source types
(whichever finds a real published email fastest for each restaurant):
- Official restaurant websites (contact/mentions légales/Impressum pages)
- OpenTable and TheFork/other reservation platform listings (when they show
  the restaurant's own email or link to a site with one)
- TripAdvisor listings
- Official Facebook Pages (About/Contact section)
- Official Instagram Business profiles (bio/contact button)
- Official Twitter/X profiles (bio)
- Google Business Profile listings
- Local/national business directories (PagesJaunes, Impressum registries,
  government business registries, chamber-of-commerce listings)
- Tourism board / office de tourisme listings
- Local press/food publications ("best restaurants in X" articles)
The verification bar is unchanged: only an ACTUALLY DISPLAYED email counts
(never guessed/pattern-constructed), and social media only counts when it's
the restaurant's own official account, not a fan page or random post.

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
- **Wave 1 done** (major/mid cities covered, still need deeper
  small-town coverage before considered exhausted): United Kingdom,
  Germany, Italy, Spain, Netherlands, Portugal, Switzerland, Austria,
  Ireland, Belgium, Denmark, Sweden, Norway, Finland, Poland, Czechia,
  Hungary, Greece, Croatia, Estonia, Latvia, Lithuania, Slovakia,
  Slovenia, Serbia, Bosnia and Herzegovina, Luxembourg, Iceland, Malta,
  Cyprus, Romania, Bulgaria, Albania, Montenegro, Kosovo, North
  Macedonia, Türkiye, Georgia, Armenia, Azerbaijan, Ukraine, Moldova,
  Andorra, Monaco, San Marino.
- **France**: SEPARATE TRACK per operator — see "France (operator-
  provided + new research)" section below. Deep multi-source wave 1
  done on top of the operator's 782-row dataset; not exhausted.
- **Not yet started**: Liechtenstein, Vatican City, Belarus, Russia.
  - Liechtenstein and Vatican City are extremely small (Vatican City
    has essentially no independent restaurants — mostly Rome
    spillover); low priority but still worth one pass.
  - Belarus and Russia: in scope per the original brief (geographic
    Europe, not EU-only) — worth attempting, but expect low yield and
    verification difficulty (language, site accessibility, current
    operating status). Try when other countries are further along.
- Next up: a Liechtenstein/Vatican City pass, then start wave 2 (deeper
  small-town/regional coverage) on the countries above that only have a
  wave 1 pass so far — that's most of them. Belarus/Russia attempted
  opportunistically.

## France (operator-provided + new research)
- Operator already had 700+ France leads from another source and
  uploaded 3 files (Paris, general FR, small FR2 supplement — 782 rows
  combined after merge, 0 exact-duplicate emails across the 3 files).
- These live in `data/france_leads_operator_provided.csv` on this
  branch — counted in the grand total but NOT part of the sequential
  `restaurant_leads_batch_NNN.csv` deliverables (operator already has
  this data, no need to redeliver it).
- Validation pass: all 782 emails matched valid email syntax. DNS
  checked all 458 unique domains (A + MX records) — 37 domains had
  neither. Research pass on those 37: 13 corrected (real replacement
  email found, now in batch_001 as newly-extracted leads, and the
  operator file's `Needs Verification` column set to
  `corrected-see-batch` for those rows), 3 confirmed permanently closed
  (`Needs Verification=closed`: 14 Paradis, Le Pain et la Rose,
  L'Assiette Autour du Vin), 21 still unresolved (`Needs
  Verification=yes` — active businesses but no public email found, or
  genuinely unreachable).
- Operator has since said to RESUME general France research (not just
  corrections), excluding restaurants the operator's 782 rows already
  cover (dedup by exact email + name/city, verified programmatically
  before every merge). Operator's data covers heavily (row counts):
  Paris 177, Toulouse 109, Bordeaux 108, Strasbourg 97, Nice 86,
  Boulogne-Billancourt 65, Lyon 48, Marseille 33, plus small counts
  (1-8 rows) in ~30 other communes.
  - Wave 6 France (deep multi-source, 71 new restaurants, all unique
    vs. both batch_001 and the operator file): Nantes, Rezé, Lille,
    Montpellier, Saint-Clément-de-Rivière, Reims, Dijon, Grenoble,
    Nîmes, Le Havre, Sainte-Adresse, Angers, Clermont-Ferrand, Aubière,
    Metz, Nancy, Vandœuvre-lès-Nancy, Annecy, Veyrier-du-Lac, Avignon,
    Aix-en-Provence, Perpignan, Cannes, Toulon, Le Mans, La Rochelle,
    Biarritz, Chamonix-Mont-Blanc, Colmar, Tours, Besançon. Sourced
    almost entirely from official sites' "mentions légales" pages
    (French law requires a real contact email there) — fastest, most
    reliable source for France specifically.
  - France is NOT exhausted — continue further waves targeting more
    towns/regions plus deeper passes on OpenTable/TripAdvisor/social
    media per the search-method upgrade above.

## Operator clarification on batching
- Don't retroactively trim a batch file to exactly 500 rows once it
  goes over during a merge — just close it as-is and start the next
  batch fresh (header only) for future new leads. Batch 001 ended at
  558 rows for this reason.
