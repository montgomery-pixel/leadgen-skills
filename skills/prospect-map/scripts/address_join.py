#!/usr/bin/env python3
"""Address-based licensee join.

Given (a) the entities you enumerated and (b) a bulk licence or permit file for the
same geography, list every licensee registered at an entity's street address whose
name and owner share no identifying word with the entity, its owner or its manager.
Those are OUTSIDER candidates: a separate party licensed inside the building, which
is usually the public-record footprint of the paying relationship you are mapping.

They are candidates only. Every one goes through the refute pass (Step 4) before it
reaches the map. Known false positives: mixed-use towers that share a street number,
suite collisions, and the entity's own venue-name licences that share no word with
the entity name (add those venue names with --ignore-words if you know them).

Standard library only. Export spreadsheets to CSV first (UTF-8).

Usage:
  python address_join.py \
      --entities market.csv --entity-name entity --entity-address address \
      --entity-owner owner --entity-manager manager --entity-city city --entity-region region \
      --licensees licences.csv --lic-name "DBA Name" --lic-address "Location Address" \
      [--lic-owner "Owner Name"] [--lic-type "License Type"] \
      [--ignore-words "tavern,collection"] [--ignore-file words.txt] \
      --out outsiders.json

Every column named by an --entity-* or --lic-* flag must exist in its file (blank
cells are fine; the script exits when a named column is missing). --entity-owner,
--entity-manager, --entity-city and --entity-region may be omitted when the file has
no such column. The address key is the street number plus the first street word, upper-cased, with
punctuation removed ("12 Quay Street, Suite 4" and "12 QUAY ST" both become "12 QUAY").
"""
import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict

DEFAULT_IGNORE = set("""
the of and a an at on by in for to
llc inc co corp corporation lp llp ltd limited company companies group holdings partners partnership enterprises
trust ventures management hospitality properties property owner operating operations services
hotel hotels inn inns resort resorts suites suite lodge lodging motel spa club conference center centre
downtown uptown midtown beach island harbor harbour bay historic district collection plaza tower towers
restaurant restaurants bar bars grill grille kitchen cafe lounge room dining bistro tavern pub eatery
""".split())


def load_csv(path):
    with open(path, encoding="utf-8-sig", errors="replace", newline="") as f:
        rd = csv.DictReader(f)
        rows = list(rd)
        return rd.fieldnames or [], rows


def need(fieldnames, col, what, path):
    if col and col not in fieldnames:
        sys.exit(f"{what}: column {col!r} not found in {path}. Columns available: {fieldnames}")


def tokens(s, ignore):
    return {t for t in re.findall(r"[a-z0-9]+", (s or "").lower()) if len(t) > 2 and t not in ignore}


def address_key(a):
    a = re.sub(r"\s+", " ", (a or "").upper().replace(".", " ").replace(",", " ").replace("#", " ")).strip()
    m = re.match(r"^(\d+[A-Z]?)\s+([A-Z0-9]+)", a)
    return f"{m.group(1)} {m.group(2)}" if m else None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--entities", required=True)
    ap.add_argument("--entity-name", required=True)
    ap.add_argument("--entity-address", required=True)
    ap.add_argument("--entity-owner")
    ap.add_argument("--entity-manager")
    ap.add_argument("--entity-city", help="city column; city words are ignored on both sides of the match")
    ap.add_argument("--entity-region", help="region column, copied through to the output")
    ap.add_argument("--licensees", required=True)
    ap.add_argument("--lic-name", required=True)
    ap.add_argument("--lic-address", required=True)
    ap.add_argument("--lic-owner")
    ap.add_argument("--lic-type")
    ap.add_argument("--ignore-words", help="comma-separated extra words to treat as non-identifying")
    ap.add_argument("--ignore-file", help="text file, one extra ignore word per line")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    ignore = set(DEFAULT_IGNORE)
    if args.ignore_words:
        ignore |= {w.strip().lower() for w in args.ignore_words.split(",") if w.strip()}
    if args.ignore_file:
        with open(args.ignore_file, encoding="utf-8") as f:
            ignore |= {line.strip().lower() for line in f if line.strip()}

    ent_fields, entities = load_csv(args.entities)
    lic_fields, licensees = load_csv(args.licensees)
    for col, what in ((args.entity_name, "entity name"), (args.entity_address, "entity address"), (args.entity_owner, "entity owner"),
                      (args.entity_manager, "entity manager"), (args.entity_city, "entity city"), (args.entity_region, "entity region")):
        need(ent_fields, col, what, args.entities)
    for col, what in ((args.lic_name, "licensee name"), (args.lic_address, "licensee address"), (args.lic_owner, "licensee owner"), (args.lic_type, "licence type")):
        need(lic_fields, col, what, args.licensees)

    by_addr = defaultdict(list)
    for r in licensees:
        k = address_key(r.get(args.lic_address))
        if k:
            by_addr[k].append(r)

    out = []
    for e in entities:
        name = e.get(args.entity_name, "") or ""
        addr = e.get(args.entity_address, "") or ""
        k = address_key(addr)
        base = {"entity": name, "address": addr, "addressKey": k}
        if args.entity_region:
            base["region"] = e.get(args.entity_region, "")
        if args.entity_city:
            base["city"] = e.get(args.entity_city, "")
        if not k:
            out.append({**base, "status": "NO_ADDRESS", "licensesAtAddress": 0, "outsiders": []})
            continue
        local_ignore = set(ignore)
        if args.entity_city:
            local_ignore |= tokens(e.get(args.entity_city, ""), set())
        insiders = tokens(name, local_ignore)
        for col in (args.entity_owner, args.entity_manager):
            if col:
                insiders |= tokens(e.get(col, ""), local_ignore)
        lic = by_addr.get(k, [])
        seen = set()
        outsiders = []
        for r in lic:
            lname = r.get(args.lic_name, "") or ""
            lowner = (r.get(args.lic_owner, "") or "") if args.lic_owner else ""
            if (lname, lowner) in seen:
                continue
            seen.add((lname, lowner))
            lt = tokens(lname, local_ignore) | tokens(lowner, local_ignore)
            if lt and not (lt & insiders):
                outsiders.append({
                    "licensee": lname,
                    "licenseeOwner": lowner,
                    "address": r.get(args.lic_address, ""),
                    "type": (r.get(args.lic_type, "") or "") if args.lic_type else "",
                })
        status = "OUTSIDER_AT_ADDRESS" if outsiders else ("SELF_ONLY" if lic else "NO_LICENCE_AT_ADDRESS")
        out.append({**base, "status": status, "licensesAtAddress": len(lic), "outsiders": outsiders})

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)

    print("STATUS:", dict(Counter(o["status"] for o in out)))
    for o in out:
        if o["status"] == "OUTSIDER_AT_ADDRESS":
            print(f"\n{o['entity']} | {o['address']}")
            for x in o["outsiders"][:5]:
                extra = f" [{x['licenseeOwner']}]" if x["licenseeOwner"] else ""
                typ = f" ({x['type']})" if x["type"] else ""
                print(f"   -> {x['licensee']}{extra}{typ}")
    print(f"\nwritten {args.out}")


if __name__ == "__main__":
    main()
