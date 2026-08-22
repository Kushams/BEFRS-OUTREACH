# BEFRS Outreach Workflow

This document defines the shared rules for the automated restaurant outreach workflow. The Pull Request #1 branch is the shared coordination point for the restaurant database and outreach history. The existing restaurant batch CSVs remain unchanged.

When one restaurant has multiple publicly verified business email addresses, keep the restaurant as one row and store all verified addresses in the `Business Email` cell, separated by semicolons. Do not create duplicate restaurant rows solely because the restaurant has multiple email addresses. The scheduler may expand that cell into individual recipient addresses, but each address may be scheduled at most once.

## Data roles

The files under `data/restaurant_leads_batch_*.csv` are the live suppression list. They contain restaurants and business emails already collected by the research workflow. `data/outreach_scheduled.csv` records recipients that the outreach scheduler has scheduled or sent. New lead research must read both sources before proposing a recipient.

The restaurant batch CSVs are **not** the source of new outreach recipients for the scheduler. New candidates must come from separate public web research and must include a traceable source URL. Never guess an email address or generate one from a domain pattern.

## Required checks before scheduling

The scheduler must refresh this branch immediately before selecting recipients and again immediately before calling the Zoho scheduling operation. It must read every restaurant batch CSV and `outreach_scheduled.csv`, split semicolon-separated values in `Business Email`, normalize each address by trimming whitespace and converting to lowercase, and exclude exact normalized email matches.

The scheduler must treat a same-business match as the same restaurant even when a different email address is present. Multiple verified addresses belonging to that same restaurant are not new restaurant leads; they should be retained in the same `Business Email` cell and may each receive one outreach message if they have not already been scheduled. Same-name restaurants in different cities or states may remain eligible when the evidence shows they are separate businesses.

Only publicly visible business contact addresses with a traceable source URL may be used. Each source URL must be retained in the outreach audit record.

## Scheduling rules

Use the sender `Liz@befrs.us`. Use the approved HTML template and replace `{{Restaurant Name}}` with the recipient restaurant name. Use the subject `{{Restaurant Name}} Collaboration Opportunity: 2026 Q3 Dining Experience - BEST EVER FOOD REVIEW SHOW`.

Target 10 messages per day in Africa/Lagos time. Prefer starting at 2:00 PM and use 10-minute intervals. If necessary, continue beyond 5:00 PM; 5:00 PM is not a hard stop. If execution starts later, use the next available 10-minute slots and still schedule 10 whenever 10 eligible recipient addresses exist. Do not send duplicates, follow-ups, or messages without a traceable source URL. The messages should use Zoho Mail scheduled delivery so they remain visible in the account's scheduled outbox.

## Shared-state rules

After an individual address is successfully scheduled, append one row to `data/outreach_scheduled.csv` for that recipient address. Multiple rows may refer to one restaurant when that restaurant has multiple verified public addresses. The append should be atomic and should preserve the CSV header. If a run fails before Zoho confirms scheduling, do not record the recipient as scheduled; record the failure only in the run summary.

Never commit credentials, OAuth tokens, API keys, or private connector configuration to this repository. The HTML template itself is hosted separately; store only its URL and version or hash in audit records when needed.

## Guidance for the Claude research workflow

Before generating a new restaurant lead, read all restaurant batch CSVs and `outreach_scheduled.csv`. Do not regenerate any email address or restaurant identity that is already present in either source. When adding new restaurant data, preserve the existing columns and record the source URL for every email. If several public addresses belong to one restaurant, place them in one `Business Email` cell separated by semicolons, not in duplicate restaurant rows.
