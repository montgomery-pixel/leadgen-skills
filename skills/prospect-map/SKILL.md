---
name: prospect-map
description: Enumerate an entire B2B market from public records (state licence files, registries, county parcel layers), verify every row in refute mode against current-year evidence, and render an HTML prospect map with the owner, who runs it today, a status per row and a dated watch list. Use when the user says "map the market", "prospect map", "find every <niche> in <geography>", "who owns every hotel/practice/building in", "enumerate the market", "build a target list from public records", "total addressable list", or runs /prospect-map.
argument-hint: '"<niche>" "<geography>"'
user-invocable: true
---

# Prospect Map

Count a whole market from public records, sort it by one question (who already pays a separate party for what the client sells), put an owner and a status on every row, and render a page that reads as a receipt: the market counted, the rows where the paying relationship already exists, and the deals coming loose. Public records first, agents last, every row carries its evidence and its date.

Deliverables: `market.csv` (the count), `rows.json` (every entity with owner, counterparty, status, evidence, trigger), `map.html` (the page). Companion skills in this pack: `discovery-sheet` (the call after the map) and `one-pager` (the document per prospect).

## Requirements

- Built-in tools only: Read, Write, Bash, WebSearch, WebFetch and the Agent tool. No paid service is required (see Optional upgrades).
- Python 3.8 or newer on PATH for the three scripts in `scripts/`; standard library only, nothing to install. The commands below say `python`; use `python3` where `python` is not present.
- `<skill-dir>` in every command is the directory this SKILL.md was loaded from: `scripts/` and `references/` sit beside it (on a plugin install, the plugin's `skills/prospect-map/` folder). Resolve it to an absolute path once, write it at the top of `journal.md`, and run every command from inside the working folder.

## Arguments

`$ARGUMENTS` carries `"<niche>" "<geography>"`. The niche is what the client sells and to whom (for example "restaurant operator for full-service hotels"); the geography is where to count (a state, a metro, a list of counties). If either is missing, ask for both in one line and stop.

## Working folder

```
prospect-map/<niche-slug>-<geo-slug>/
  journal.md        decisions, sources with dates, pass logs (working notes, not a deliverable)
  sources/          raw downloads, one journal line each: URL, extract date, row count
  market.csv        the enumeration (Step 2): region, city, entity, address, sourceFile, licenceId, licenceType, owner, manager
  outsiders.json    output of the address join (Step 2)
  rows.json         seeded from market.csv and outsiders.json at the end of Step 2; Steps 3 to 5 write into it
  map.config.json   page copy and column labels (Step 6)
  map.html          the deliverable
  manual-queue.md   sources that need a human (terms gates, CAPTCHAs), with the exact search to run
```

`owner` and `manager` are always present in `market.csv`, blank when the source file has no value. Skeletons for `journal.md` and `manual-queue.md` are in `references/working-files.md`.

## Row schema (`rows.json`)

```json
{
  "region": "NS", "city": "Port Ashby", "entity": "Harbor Lights Hotel", "address": "12 Quay Street",
  "unit": "The Lantern Room",
  "counterparty": "Fensworth Clubs under a lease, own licence at the address",
  "owner": "Quay Street Hospitality LLC (Ockendale Family Holdings)",
  "ownerConfidence": "high | medium | low | unknown",
  "ownerEvidence": "the county parcel record, 14 August 2026; the deed LLC mails to the firm's office",
  "status": "ready | licensed | verify | transition | aside",
  "statusEvidence": "the sources and dates that decide the status, one or two sentences",
  "evidenceDate": "2026-09-02",
  "note": "optional line shown under the row",
  "trigger": {"what": "...", "when": "Deed dated 3 June 2026", "source": "county parcel record", "sortDate": "2026-06-03"},
  "candidate": true, "candidates": [{"licensee": "...", "licenseeOwner": "...", "type": "..."}],
  "manager": "working field, never rendered", "parcelId": "working", "ownerMailing": "working", "sources": ["working"]
}
```

Every entity in the count is a row. `aside` rows (no paying relationship today) are counted in the header and never listed. Rendered fields (`region`, `city`, `entity`, `unit`, `counterparty`, `owner`, `ownerConfidence`, `ownerEvidence`, `statusEvidence`, `note`, the trigger text) are checked for dashes and contact details; working fields (`address`, `candidate`, `candidates`, `joinStatus`, `manager`, `parcelId`, `ownerMailing`, `sources`, `saleDate`, `licenceId`, `licenceType`) are never rendered and never checked, so parcel numbers go in `parcelId` and URLs in `sources`. Table rows need `evidenceDate` as YYYY-MM-DD; every trigger needs `sortDate`. `references/example-rows.json` is a complete fictional set.

## Procedure

Seven steps: 1 define the split question, 2 enumerate in bulk, 3 owner per entity, 4 refute-mode verification, 5 watch-list triggers, 6 render, 7 honesty pass. Track them in a todo list; each step ends with a `journal.md` entry.

### Step 1: the split question

Before touching a source, write into `journal.md`: payer, payee, the one-sentence question a public record can answer, the four tests instantiated for this niche, the inclusion rule for the count, and the region granularity. Read `references/who-pays-whom.md` (worked examples across niches and the two false positives: the name on the door, and adjacent-not-inside).

### Step 2: enumerate in bulk

Pull the state licence or permit files, county parcel layers and association lists for the geography before any agent runs. Filter to the inclusion rule, dedupe on an address key, write `market.csv`, and run a ten-entity coverage check. Then run the address join (every `--entity-*` column named must exist in `market.csv`; blank cells are fine):

```
python <skill-dir>/scripts/address_join.py --entities market.csv --entity-name entity --entity-address address \
  --entity-owner owner --entity-manager manager --entity-city city --entity-region region \
  --licensees sources/<file>.csv --lic-name "<col>" --lic-address "<col>" --lic-owner "<col>" --lic-type "<col>" \
  --out outsiders.json
```

`OUTSIDER_AT_ADDRESS` rows are candidates for the table; `SELF_ONLY` rows are in-house today. Agents only for the residue, five to ten entities per agent, JSON back; merge their rows into `market.csv` before seeding. Then seed the row file:

```
python <skill-dir>/scripts/seed_rows.py --market market.csv --outsiders outsiders.json --out rows.json
```

One row per `market.csv` row. Candidates (`OUTSIDER_AT_ADDRESS`) start as `verify` with `candidate: true`, the outsider licensee names in `unit` and `counterparty`, with owner copied from market.csv when the file has one, and blank ownerConfidence, ownerEvidence, statusEvidence and evidenceDate, so `render_map.py --check` refuses the page until Steps 3 and 4 have written them. Every other row starts as `aside`. Read `references/bulk-sources.md` (source ladder, search patterns, the join's known false positives, blocked sources).

### Step 3: owner of record

For every row: bulk parcel pull by land-use code, join by address, cluster by owner mailing address, unmask the LLC through the mailing address, the registry, filings and the owner's own page. Write `owner`, `ownerConfidence`, `ownerEvidence`; keep `manager` separate and never in the owner column; unknown says unknown with the reason. Read `references/owner-lookup.md`.

### Step 4: verify in refute mode

Fan out one Agent per candidate row with the prompt in `references/verification-bar.md`: the agent's job is to disprove the row, and it may keep it only with evidence dated this year. Four tests: separate party, employer of record, inside the premises, live today. All four pass: `ready`. Name on the door: `licensed`. Structure unproven: `verify`. Owner changing hands: `transition`. Otherwise `aside`. Two agents that disagree put the row in `verify`. Merge results into `rows.json` yourself; parse defensively, and keep merged text in rendered fields free of em and en dashes and contact details (URLs go in `sources`).

Cost: one agent is roughly 15,000 to 25,000 tokens, so 100 candidate rows is 1.5 to 2.5 million tokens of agent traffic. Count the candidates (`candidate: true`) and write the budget in `journal.md` before fanning out.

### Step 5: watch-list triggers

Attach a dated, sourced trigger to any row where the record shows a sale, a parent ownership change, an operator or manager change, a renovation or closure, a new build, an authority-held title, or a default. Fact, not forecast; never a closing or a buyer that only one paywalled headline reports. A `transition` row must carry its trigger. Read `references/watch-list-triggers.md`.

### Step 6: render

Copy `references/example-config.json` to `map.config.json` and rewrite every string for this market (title, subtitle, column labels, the three method paragraphs, the caveat, the footer sources with dates). Placeholders such as `{total}`, `{ready}` and `{watch}` are filled from the rows. Then:

```
python <skill-dir>/scripts/render_map.py --rows rows.json --config map.config.json --check
python <skill-dir>/scripts/render_map.py --rows rows.json --config map.config.json --out map.html
```

The renderer computes every number on the page from the rows and refuses: blank evidence on a table row, unknown statuses, a table row without `evidenceDate`, a trigger without `sortDate`, a `transition` row without a trigger, em or en dashes or anything that looks like an email address or phone number in a rendered field, and the market-describing config strings still equal to the shipped example: title, meta, subtitle, marketNote, tableTitle, tableNote, watchNote, region names, method text and footer lines (`--allow-example` exists only to re-render the example itself). Column labels, marketLabel, watchTitle and the caveat are not checked, so read them by eye in Step 7. Add `--fragment` when publishing through a tool that wraps the page itself (the Artifact tool does). `references/map-template.html` is the rendered fictional example: header counts, chips by region, the table with Ready / Licensed / Verify / In transition cells, the watch list, the method block, the footer.

### Step 7: honesty pass

Open `map.html` and check every one of these before it is shown to anyone:

- Every table row states its evidence and a date; every owner field states its record; unknowns say unknown.
- No set-aside list, no "we were wrong" section, no narration of re-audits or corrections. Aside rows are in the count and nowhere else.
- The header numbers equal the rows (the renderer guarantees it; re-run `--check` after any hand edit).
- No phone numbers, no email addresses, no pricing, no terms, and no personal names: not an LLC's managers, not the family behind a holding company, not the chef behind a brand. A venue's or brand's own trade name is a venue name and stays.
- The Ready count is described as what the public record proves, not as the whole market: leases inside buildings are not announced, so the count is a floor.
- Five table rows picked at random re-opened against their cited source; a miss sends the row back to Step 4.
- Prose reads as plain fact: no superlatives, no hype, no forecast.

## Writing rules for the page and anything sent with it

- No em dashes or en dashes anywhere; commas, colons and periods do the work.
- No confession copy: never narrate rework, misses, uncertainty about the method, or what an earlier pass got wrong. The page shows the finished state and how it was built.
- Facts only: never invent an owner, an operator, a date, a relationship or rapport.
- Numbers on their own line in the summary message that accompanies the map, one number per line.
- Anything meant to be spoken (a talk track for presenting the map) is written as speech, in whole sentences a person would say aloud.

## Done means

Report to the user in this order: the count, the table split, the watch-list size, each on its own line; then the path to `map.html`; then what is queued for a human in `manual-queue.md`. Do not call a row verified without the pass logged in `journal.md`.

## Optional upgrades

Firecrawl, Bright Data, Apify or Scrapling, if you have them, for JavaScript-rendered portals and paginated directories. A bulk parcel-data vendor or a commercial real-estate database, if the client already pays for one, replaces the county discovery in Step 3. Nothing here requires them.
