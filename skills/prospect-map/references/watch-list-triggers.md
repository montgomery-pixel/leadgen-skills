# Step 5: watch-list triggers

The table answers "who already buys this deal shape". The watch list answers "where is a decision about to be made". A trigger is a dated public fact about an entity in the count that makes a conversation timely: a sale, a change of operator, a renovation, a new build. Triggers attach to any row, including `aside` rows (an in-house hotel that just changed hands is a conversation), and each renders as one line on the page.

## Trigger types and where they show up

| Type | What it looks like | Typical source |
| --- | --- | --- |
| Sale or deed transfer | New deed entity, sale date and price on the parcel record | County parcel record (sale-date field), county recorder index, press |
| Ownership change at the parent | Take-private, merger, portfolio sale, REIT disposition | Filings (current reports, annual reports), the parent's own release, press |
| Operator or manager change | New management company, new lease tenant, licence transfer | The new operator's portfolio page, licence-file diff, press |
| Renovation, closure, rebrand | Permit issued, "closed for renovation" notice, new name | Building permit index, the entity's own site, press |
| New build or opening | Permit, development authority approval, "opening 2027" | Permit index, authority minutes, the developer's project page |
| Authority-held title or bond lease | Parcel names a public authority; assignment approved in minutes | Parcel record, authority minutes |
| Default, foreclosure, deed in lieu, receivership | Notice recorded, lender affiliate on the deed | County recorder index, loan servicer commentary, press |
| Contract or lease expiry | Rarely public; sometimes in minutes or filings | Authority minutes, filings |
| Principal departure | Team page changes, resignation in a filing | Working notes only; never on the page |

## Rules for every trigger

- Dated: month and year at minimum; the exact day when a deed or filing gives it. Put the date in `trigger.when` as prose and in `trigger.sortDate` as `YYYY`, `YYYY-MM` or `YYYY-MM-DD` so the list sorts; the renderer refuses a trigger without `sortDate`.
- Sourced: `trigger.source` names the record or outlet ("county parcel record; regional business press, 12 June 2026"). No URLs on the page; keep them in the working fields.
- Windowed: decide the window in the journal (36 months is a sensible default) and say it in `watchNote`.
- Most recent first; capped (`watchCap`, default 40); the renderer prints how many more exist.
- Fact, not forecast. "Sale approved by the authority on 21 May 2026; closing not publicly confirmed" is a fact. "Expected to close soon" is not.
- Never state a closing, a buyer or a price that only one paywalled headline reports. Name what the public record shows and stop.
- Never volunteer more than the row says. If the deal detail belongs to a paid engagement, the page carries the fact and the date, not the analysis.

## Refresh cadence

Re-run the parcel and licence pulls quarterly. Diff owner, licensee and manager against `rows.json`. Every difference becomes a trigger with the extract date as its date, and a data fix at the same time. Log each refresh in `journal.md`.

## Fields written in this step

`trigger.what`, `trigger.when`, `trigger.source`, `trigger.sortDate` on any row. A `transition` status on a table row requires the sale or assignment trigger on that same row; the renderer refuses a `transition` row without one.
