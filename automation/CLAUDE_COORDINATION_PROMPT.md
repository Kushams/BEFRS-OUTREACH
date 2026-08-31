# Copy-ready prompt for Claude

You are part of a shared BEFRS restaurant-outreach workflow. Another automated workflow researches public restaurant leads and schedules outreach through Zoho Mail. Both workflows coordinate through the same GitHub repository and branch:

- Repository: `Kushams/BEFRS-OUTREACH`
- Branch: `claude/us-restaurant-email-database-y8g2j2`
- Pull Request: `https://github.com/Kushams/BEFRS-OUTREACH/pull/1`

The GitHub branch is the shared source of truth for lead history and outreach history. Always refresh the latest branch before doing research or writing records. Do not rely on an old local copy.

## Files you must read first

Read every file matching `data/restaurant_leads_batch_*.csv`. These files contain restaurants and public business emails already collected. Also read `data/outreach_scheduled.csv`, which records email addresses already scheduled or sent by the outreach workflow. The restaurant batch CSVs are a suppression list, not the source of new leads for the scheduler.

## Deduplication rules

Normalize all email addresses by trimming whitespace and converting them to lowercase. Treat semicolons, commas, and line breaks as separators when a cell contains multiple email addresses.

Before adding or recommending a lead, exclude any email address that already appears in any restaurant batch CSV or in `data/outreach_scheduled.csv`.

Treat `restaurant name + city + state` as the restaurant identity. If the same restaurant has several publicly verified business email addresses, keep **one restaurant row** and put all verified addresses in the same `Business Email` cell, separated by semicolons. Do not create duplicate restaurant rows just because the restaurant has another email address.

The automated scheduler may send one email to each verified address for the same restaurant, but each individual address may be contacted only once. A different email address for the same restaurant is not automatically a new restaurant lead; it is an additional contact address for the existing restaurant record.

Same-name restaurants in different cities or states may be separate records only when the evidence confirms that they are different businesses.

## Lead-quality requirements

Research new U.S. restaurants from public sources, including official restaurant websites, official contact pages, Google Maps listings, OpenTable pages, tourism or chamber listings, reputable restaurant guides, and other clearly attributable public sources.

Every email must be visibly published or clearly corroborated as belonging to that specific restaurant. Record the source URL for every email. Never guess an email address, generate one from a domain pattern, or use a generic unverified address.

## How to write new restaurant records

Use the existing CSV columns exactly:

`Restaurant Name,Business Email,City,State,Website,Source URL`

If a restaurant has multiple verified addresses, store them in one `Business Email` cell, for example:

`reservations@example.com; events@example.com; catering@example.com`

If different addresses were found on different pages, record the most relevant traceable URLs in the `Source URL` cell, separated by semicolons if necessary. Preserve existing rows and do not reorder or rewrite unrelated data.

Before committing any new data, refresh the branch and repeat the complete email-level and restaurant-identity deduplication check against all restaurant batch CSVs and `data/outreach_scheduled.csv`.

## Coordination with the automated scheduler

The automated workflow uses the same branch. It refreshes the branch before every daily run and again immediately before scheduling Zoho messages. It uses `data/outreach_scheduled.csv` as a record of recipients already scheduled or sent.

Treat every row in `data/outreach_scheduled.csv` as already contacted or scheduled for that specific email address. Do not regenerate, recommend, or contact those addresses. If another address for the same restaurant is not yet recorded, it may be used only if it is publicly verified and is added to the existing restaurant row rather than creating a duplicate restaurant record.

When the scheduler adds multiple addresses for one restaurant, it may add multiple audit rows—one row per recipient address—because each address has its own scheduled status and timestamp.

If a merge conflict occurs, preserve valid distinct addresses for the same restaurant, remove only exact duplicate addresses, and rerun the full deduplication check. Never overwrite newer outreach audit rows with an older branch copy.

## Repository safety

Do not commit passwords, OAuth tokens, API keys, private connector settings, or private credentials. Do not add the complete email HTML to the repository unless explicitly requested; the approved template is stored separately. Commit only verified lead data, source URLs, workflow documentation, and audit information.

After each update, report the number of new restaurant records, the number of additional email addresses added to existing restaurants, the number of suppressed duplicates, the files changed, and the commit or branch updated.
