#!/usr/bin/env python3
"""Seed rows.json from market.csv and outsiders.json (end of Step 2).

Writes one row per market.csv row in the schema render_map.py expects. Rows whose
address join returned OUTSIDER_AT_ADDRESS are candidates: they start as status
"verify" with candidate true, the outsider licensee names in unit and counterparty,
owner copied from market.csv when present, and blank ownerConfidence, ownerEvidence,
statusEvidence and evidenceDate, so render_map.py --check refuses the page until
Steps 3 and 4 have written them. Every other row starts as "aside"
(counted in the header, never listed).

market.csv header names are case-sensitive. Required: region, city, entity, address.
Copied when present: owner, manager, sourceFile, licenceId, licenceType.
outsiders.json is the file address_join.py wrote; rows are matched on entity and
address (whitespace and case normalised).

Usage:
  python seed_rows.py --market market.csv --outsiders outsiders.json --out rows.json [--force]

Refuses to overwrite an existing rows.json unless --force is given, because Steps 3
to 5 write into that file. Standard library only.
"""
import argparse
import csv
import json
import os
import sys
from collections import Counter

REQUIRED = ["region", "city", "entity", "address"]
COPIED = ["owner", "manager", "sourceFile", "licenceId", "licenceType"]


def norm(s):
    return " ".join((s or "").split()).lower()


def candidate_text(outsiders):
    names = []
    parts = []
    for o in outsiders:
        name = (o.get("licensee") or "").strip()
        if not name:
            continue
        names.append(name)
        owner = (o.get("licenseeOwner") or "").strip()
        typ = (o.get("type") or "").strip()
        detail = []
        if owner and norm(owner) != norm(name):
            detail.append(owner)
        if typ:
            detail.append(f"{typ} licence")
        parts.append(f"{name} ({'; '.join(detail)})" if detail else name)
    if not parts:
        return "", ""
    unit = "; ".join(names)
    verb = "is licensed" if len(parts) == 1 else "are licensed"
    counterparty = "; ".join(parts) + f" {verb} at the address; separate party and employer of record not yet confirmed"
    return unit, counterparty


def cell(row, col, fields):
    return (row.get(col) or "").strip() if col in fields else ""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--market", required=True, help="market.csv from Step 2")
    ap.add_argument("--outsiders", required=True, help="outsiders.json written by address_join.py")
    ap.add_argument("--out", required=True, help="rows.json to write")
    ap.add_argument("--force", action="store_true", help="overwrite an existing rows.json")
    args = ap.parse_args()

    if os.path.exists(args.out) and not args.force:
        sys.exit(f"{args.out} exists; Steps 3 to 5 write into it. Pass --force to start over.")

    with open(args.market, encoding="utf-8-sig", errors="replace", newline="") as f:
        rd = csv.DictReader(f)
        fields = rd.fieldnames or []
        market = list(rd)
    missing = [c for c in REQUIRED if c not in fields]
    if missing:
        sys.exit(f"{args.market}: missing column(s) {missing}. Columns available: {fields}")
    absent = [c for c in COPIED if c not in fields]

    with open(args.outsiders, encoding="utf-8") as f:
        joined = json.load(f)
    if not isinstance(joined, list):
        sys.exit(f"{args.outsiders}: expected a JSON array (the output of address_join.py)")
    by_key = {}
    for j in joined:
        if isinstance(j, dict):
            by_key[(norm(j.get("entity")), norm(j.get("address")))] = j

    rows = []
    unmatched = 0
    for m in market:
        j = by_key.get((norm(m.get("entity")), norm(m.get("address"))))
        if j is None:
            unmatched += 1
        outsiders = [o for o in ((j or {}).get("outsiders") or []) if isinstance(o, dict)]
        is_candidate = bool(j) and j.get("status") == "OUTSIDER_AT_ADDRESS" and bool(outsiders)
        unit, counterparty = candidate_text(outsiders) if is_candidate else ("", "")
        source = cell(m, "sourceFile", fields)
        rows.append({
            "region": cell(m, "region", fields),
            "city": cell(m, "city", fields),
            "entity": cell(m, "entity", fields),
            "address": cell(m, "address", fields),
            "unit": unit,
            "counterparty": counterparty,
            "owner": cell(m, "owner", fields),
            "ownerConfidence": "",
            "ownerEvidence": "",
            "status": "verify" if is_candidate else "aside",
            "statusEvidence": "",
            "evidenceDate": "",
            "candidate": is_candidate,
            "candidates": [
                {"licensee": o.get("licensee", ""), "licenseeOwner": o.get("licenseeOwner", ""), "type": o.get("type", "")}
                for o in outsiders
            ],
            "joinStatus": (j or {}).get("status", "NOT_JOINED"),
            "manager": cell(m, "manager", fields),
            "parcelId": "",
            "ownerMailing": "",
            "sources": [source] if source else [],
            "licenceId": cell(m, "licenceId", fields),
            "licenceType": cell(m, "licenceType", fields),
        })

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)

    counts = Counter(r["status"] for r in rows)
    print(f"written {args.out}: {len(rows)} rows, {counts['verify']} candidates (status verify, candidate true), {counts['aside']} aside")
    if unmatched:
        print(f"{unmatched} market rows had no match in {args.outsiders}; they start as aside with joinStatus NOT_JOINED")
    if absent:
        print(f"columns not in {args.market}, left blank: {absent}")
    print("next: Step 3 writes owner, ownerConfidence, ownerEvidence on every row; Step 4 writes status, statusEvidence, evidenceDate on every candidate")


if __name__ == "__main__":
    main()
