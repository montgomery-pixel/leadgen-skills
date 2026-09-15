# Step 3: owner of record and confidence

The person who signs for the deal is usually the owner of the asset or its asset manager, not the manager whose name is on the sign. Get the owner from the record, not the press. If you already have a tool with tested parcel endpoints for the counties in scope (a bulk parcel vendor, a GIS client, a skill of your own), use it and keep this file's confidence scale; everything below runs on WebSearch, WebFetch and `curl`.

## Four tiers, cheapest first

1. Bulk pull. Query each county's parcel layer filtered by land-use code (hotel, restaurant, medical office, apartment). One request returns every parcel of that use in the county with owner name, owner mailing address, parcel id and appraised value. Store it in `sources/`.
2. Deterministic join. Match parcels to `market.csv` by address key. Then cluster rows by owner mailing address: one firm's office suite appears across many differently named LLCs, which reveals portfolios for free.
3. Unmask, with agents only where needed. Deed holders are usually single-asset LLCs. Search the mailing address string; it resolves to a firm's office. A `C/O <firm>` line on the tax roll is primary evidence. Cross-check the state registry (officers, managers, registered agent), annual-report property schedules for public owners, and the owner's own portfolio page.
4. Contacts, last and outside this skill. Only once the firm is known. A contact database answers "an email for a named person at a named company"; it cannot tell you who owns a building.

## Discovering a county's parcel endpoint

1. Search `"<county>" ArcGIS rest services parcels` or `"<county>" GIS open data parcel`.
2. Fetch the server directory: `https://<host>/arcgis/rest/services?f=json`. Look for a Parcels, TaxAssessor, Property or Cadastral layer.
3. Fetch the layer's metadata (`.../MapServer/<n>?f=json` or `.../FeatureServer/<n>?f=json`) and read the field names. They differ per county (`Owner`, `OWNERNME`, `PROPERTY_OWNER`, `own1`).
4. Query: `.../query?where=<field>+LIKE+'<NUM STREET>%25'&outFields=*&returnGeometry=false&f=json`. For bulk mode use the land-use field: `where=<LandUseField>=<code>`.
5. If a county seems to lack an owner field, look for a second GIS host before giving up. Several states publish a statewide cadastral layer; try the state first.
6. Some counties expose the owner only behind a click-through portal. Queue those for a human (two minutes each) rather than accepting terms as an agent, and mark the row's confidence accordingly.

## Confidence scale (write it into every row)

- `high`: the current parcel record names the deed entity and the unmasking is corroborated by a second source (registry, annual report, the owner's own page, a C/O line).
- `medium`: a parcel record found but the unmasking rests on one source; or no parcel reachable but an annual-report schedule or registry filing names the owner directly.
- `low`: press only, or a parcel record older than two years with a reported sale since.
- `unknown`: no reachable record. The row says "unknown" in the owner field and why in the evidence field. Never fill an unknown with the manager's name or a guess.

`ownerEvidence` names the record and its date: "the county parcel record, 14 August 2026; the deed LLC mails to the firm's registered office".

## The two errors that ruin these lists

Owner versus manager. Management companies publish press releases; owners hide in LLCs. Web research surfaces the manager and calls it the owner. Keep `manager` as its own field in `rows.json` and never let it into the `owner` column. The map's counterparty column may mention the manager where it explains who runs the unit.

Stale owner. Assets trade constantly. A press release from two years ago is not evidence of ownership today. The parcel record is current by definition; note its sale-date field where the county exposes one, because a recent sale is also a watch-list trigger.

## Special title situations

- Bond-lease, PILOT or authority-held title: record title sits with a public development authority while a private leasehold controls the asset. Record both. The leaseholder is the decision maker. Assignments of the leasehold appear in the authority's published minutes and are triggers.
- Deed in lieu, foreclosure, receivership: the lender or its affiliate becomes the owner of record. Record it as the owner with the date; it is also a trigger.
- Equity sale of the owning company: the deed entity name does not change. Only the registry or press shows the change; confidence `medium` at best until a filing confirms it.

## People are not on the page

This map shows entities. A named principal only enters your working notes when a current-year source confirms the person still holds the role. Departed executives in outreach are a credibility failure, and personal names on a shared page are a privacy failure.

## Refresh, not a one-off

Ownership decays. Script the parcel and licence pulls so they can be re-run quarterly and diffed against `rows.json`. Every change the diff finds is both a data fix and a watch-list trigger.

## Fields written in this step

`owner`, `ownerConfidence`, `ownerEvidence` (rendered on the page); `manager`, `parcelId`, `ownerMailing`, `saleDate` (working fields in `rows.json`, never rendered and not checked by the renderer). Put the parcel number in `parcelId` only: `ownerEvidence` names the record and its date, and a hyphenated parcel number written there trips the renderer's phone-number guard.
