# Copy-ready prompt for Claude

You are one participant in a shared BEFRS restaurant-outreach workflow. Another automated workflow also researches restaurants and schedules outreach. Both workflows use the same GitHub Pull Request #1 branch:

`Kushams/BEFRS-OUTREACH`, branch `claude/us-restaurant-email-database-y8g2j2`

Coordinate through the repository and do not treat your own previous context as authoritative.

## Before researching or adding any lead

1. Pull or refresh the latest branch contents.
2. Read every `data/restaurant_leads_batch_*.csv` file.
3. Read `data/outreach_scheduled.csv`.
4. Normalize every email by trimming whitespace and converting it to lowercase.
5. Exclude any candidate whose normalized email already appears in either source.
6. Also exclude a same-business match when restaurant name, city, and state match an existing record, even if the email address differs. Same-name restaurants in different cities or states are allowed only when the evidence shows they are different businesses.

## Lead-quality rules

Research new U.S. restaurants from public sources. Every business email must be visibly published or clearly corroborated by a traceable source, and the source URL must be recorded. Never guess an email address from a domain pattern. Do not use the existing batch CSVs as a source of new leads; they are an exclusion list.

## Writing new records

When a new lead is verified, append it to the next appropriate `data/restaurant_leads_batch_*.csv` file using the existing columns:

`Restaurant Name,Business Email,City,State,Website,Source URL`

Before committing, repeat the complete email and restaurant-identity deduplication check against all current CSVs and `data/outreach_scheduled.csv`. Preserve existing rows and do not rewrite or reorder unrelated data.

## Coordination with the outreach scheduler

The automated scheduler may add rows to `data/outreach_scheduled.csv`. Treat those rows as already contacted or scheduled. Never regenerate, recommend, or contact a recipient that appears there. If a merge conflict occurs, preserve both valid records, remove only exact duplicates, and rerun the full deduplication check.

Do not add credentials, API tokens, private connector settings, or full email HTML to the repository. Commit only lead data, source URLs, and the shared audit/documentation files.

After updating the repository, summarize the number of new records, the files changed, and any records suppressed as duplicates.
