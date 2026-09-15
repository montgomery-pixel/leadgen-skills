# Step 2: enumerate from bulk public sources

## The rule

Never send an agent to look up entities one at a time until the bulk sources are exhausted. One agent per row costs roughly 15,000 to 25,000 tokens and returns whatever the web says. A licence file is one download and returns what the state has certified. Agents are for the residue: the entities the files missed and the joins that are ambiguous.

## Source ladder (pull in this order)

1. Licence and permit files from the state or province. Alcohol, food service, lodging, health facility, professional (dental, medical, veterinary), contractor, childcare, insurance producer, real-estate brokerage, pharmacy. Most licensing boards publish an extract (CSV or XLSX), weekly or monthly, with licensee name, owner or entity name, premises address and licence type. Search patterns:
   - `"<state>" "<licence type>" license "download"` and `"<state>" "<licence type>" licenses csv`
   - `site:<state open data host> <licence type>` (many states run a Socrata or ArcGIS open-data portal)
   - `"<state>" "<licence type>" "active licenses" xlsx`
   - If nothing is published, email the board a records request; extracts are usually free and arrive within days.
2. County parcel layers by land-use code, which return every hotel, restaurant, clinic or apartment parcel in a county with the owner name. See `owner-lookup.md`; this is an enumeration source as well as an owner source.
3. Corporate registries. Some states publish bulk business-entity data; all have a search. Use them to resolve entity names and registered agents, not to enumerate a market.
4. Membership, accreditation and franchise lists. Association member directories, accreditation registers, tourism and lodging directories, franchise disclosure documents (which list every franchisee with an address). Useful for coverage checks and for niches without a licence.
5. Activity records. Building permits (renovations, new builds), health inspection results (a recent inspection means open), procurement and vendor registers (who holds the contract), UCC filings (equipment financing), development authority minutes (assignments, bond-lease titles).
6. Rating and review lists. Only as a coverage cross-check. Never as the count.
7. Full-text search of securities filings and annual-report property schedules for assets owned by public companies.

## Make the count

1. Download every raw file into `sources/` and log in `journal.md`: URL, extract date, row count.
2. Filter to the geography and the licence types that match the inclusion rule from Step 1.
3. Normalise: upper-case, strip punctuation, build an address key (street number plus first street word). Dedupe on the key plus the entity name.
4. Write `market.csv` with one row per entity: `region, city, entity, address, sourceFile, licenceId, licenceType, owner, manager`. Always write the `owner` and `manager` columns; leave a cell blank when the file has no value. The join and the seed script read both columns by name and exit when a named column is missing.
5. Coverage check. Take ten entities you know exist in the geography (press, a directory, the client's own list). Find each in `market.csv`. Every miss has a reason (licensed under a different name, a different licence class, a parent entity's address) and the reason changes the filter, not the count. Record the ten and the result in the journal.
6. State the inclusion rule and the count in the journal. The count is the number that goes in the header chip.

## The address join: finding the paying relationship in bulk

The entity's own licence gives its premises address. Every other licensee at that same address is a separate party doing licensed activity inside the building. Remove the entity's own venue-name licences (they share words with the entity, its owner or its manager) and what remains is a list of outsider candidates: the public-record footprint of the relationship you are mapping.

Run the script (standard library only; export spreadsheets to CSV first). `<skill-dir>` is the folder holding SKILL.md, as an absolute path; run from inside the working folder:

```
python <skill-dir>/scripts/address_join.py \
  --entities market.csv --entity-name entity --entity-address address \
  --entity-owner owner --entity-manager manager --entity-city city --entity-region region \
  --licensees sources/<state>-licences.csv --lic-name "<licensee name column>" \
  --lic-address "<premises address column>" --lic-owner "<owner column>" --lic-type "<type column>" \
  --out outsiders.json
```

Per entity it returns one of:

- `OUTSIDER_AT_ADDRESS`: at least one licensee at the address shares no identifying word with the entity, its owner or its manager. Candidate for the table. Goes to Step 4.
- `SELF_ONLY`: only the entity's own licences at the address. In-house today. Status `aside` unless Step 4 finds otherwise.
- `NO_LICENCE_AT_ADDRESS`: no licensee matched the address key. Check the address (a different street name in the file, a parent entity's mailing address) before concluding anything.
- `NO_ADDRESS`: the market row has no usable street address. Fix the row.

## Seed rows.json

Once `market.csv` is final (agent residue merged in) and `outsiders.json` is written:

```
python <skill-dir>/scripts/seed_rows.py --market market.csv --outsiders outsiders.json --out rows.json
```

One row per `market.csv` row, matched to `outsiders.json` on entity and address. `OUTSIDER_AT_ADDRESS` rows become candidates: status `verify`, `candidate: true`, the licensee names in `unit` and `counterparty`, `candidates` holding the licensee, its owner and the licence type, and blank `ownerConfidence`, `ownerEvidence`, `statusEvidence` and `evidenceDate`. Every other row is `aside`. `owner`, `manager`, `sourceFile` (into `sources`), `licenceId` and `licenceType` are copied from the CSV. The script refuses to overwrite an existing `rows.json` without `--force`, because Steps 3 to 5 write into it. Log the seeded counts in `journal.md`.

Known false positives, all of which Step 4 catches: mixed-use towers where a restaurant shares the street number but sits in the office podium; suite collisions; the entity's own venues whose names share no word with the entity (add those names with `--ignore-words` when you know them); wholesalers and caterers registered at a hotel address; a franchisor holding the licence for a unit the hotel staffs.

Known false negatives: licences held by a parent entity at a different address; files that carry only mailing addresses; brands licensed under numbered LLCs. This is why Step 4 also checks the entity's own page and the counterparty's own site, and why the count of Ready rows is a floor, not a ceiling. Say so on the page.

## Portals without a bulk file

Some permit portals only answer one address at a time. Check whether the search form is a plain POST without a token or JavaScript requirement; if it is, WebFetch or `curl` can query it per address, and a search by county plus active status often returns a downloadable file, which is bulk again. If the portal needs JavaScript, see the optional upgrades below.

## Blocked sources: queue for a human

Click-through terms portals, CAPTCHA-gated registries and paid deed sites take a person about two minutes each. Write them to `manual-queue.md` with the exact search to run. Never accept terms, bypass a CAPTCHA or create an account as an agent, and never present a guess in place of the record.

## Optional upgrades (never required)

If you have Firecrawl, Bright Data, Apify or Scrapling, use them for JavaScript-rendered portals and long paginated directories. Everything above runs on WebSearch, WebFetch, Bash and Python.

## Agents come last

Fan out only on the residue: entities the files missed, `NO_LICENCE_AT_ADDRESS` rows, and ambiguous joins. Batch five to ten entities per agent by geography, ask for JSON only in a fixed shape, guard the parse, and write the merged result into `market.csv` yourself before `seed_rows.py` runs. Use the cheapest model that reads a web page reliably.
