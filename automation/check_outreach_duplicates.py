#!/usr/bin/env python3
"""Check candidate restaurant leads against the shared BEFRS suppression sources.

Usage:
    python3 automation/check_outreach_duplicates.py candidates.csv

The candidate CSV must contain: restaurant_name, business_email, city, state.
The script prints eligible and suppressed rows as CSV to stdout and never
modifies repository data.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def norm(value: str) -> str:
    return " ".join((value or "").strip().casefold().split())


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} candidates.csv", file=sys.stderr)
        return 2

    candidate_path = Path(sys.argv[1])
    existing: list[dict[str, str]] = []
    for path in sorted(DATA.glob("restaurant_leads_batch_*.csv")):
        existing.extend(load_rows(path))
    audit = DATA / "outreach_scheduled.csv"
    if audit.exists():
        existing.extend(load_rows(audit))

    email_keys = {norm(row.get("Business Email", row.get("business_email", ""))) for row in existing}
    identity_keys = {
        (
            norm(row.get("Restaurant Name", row.get("restaurant_name", ""))),
            norm(row.get("City", row.get("city", ""))),
            norm(row.get("State", row.get("state", ""))),
        )
        for row in existing
    }

    with candidate_path.open(newline="", encoding="utf-8-sig") as handle:
        candidates = csv.DictReader(handle)
        fieldnames = list(candidates.fieldnames or [])
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames + ["suppression_reason"])
        writer.writeheader()
        for row in candidates:
            email = norm(row.get("business_email", row.get("Business Email", "")))
            identity = (
                norm(row.get("restaurant_name", row.get("Restaurant Name", ""))),
                norm(row.get("city", row.get("City", ""))),
                norm(row.get("state", row.get("State", ""))),
            )
            reasons: list[str] = []
            if email and email in email_keys:
                reasons.append("email_match")
            if identity != ("", "", "") and identity in identity_keys:
                reasons.append("restaurant_identity_match")
            row["suppression_reason"] = ";".join(reasons)
            writer.writerow(row)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
