# Step 4: the verification bar (refute mode)

## Why refute mode

An agent told to confirm a row finds one source that agrees and stops. An agent told the row is probably wrong, and that it may only keep the row with evidence dated this year, finds the closed venue, the consultant read as an operator, the announcement mistaken for an opening, and the tenant next door. Expect a refute pass to remove a large share of first-pass rows. That is the pass working. Run it before the map is shown to anyone, and run it again on any row older than a month before that row is used.

## The four tests

A row is `ready` only when all four pass with dated evidence. Instantiate them for the niche in `journal.md` before fanning out.

1. Separate party. The counterparty is a different legal entity from the owner and from the manager, and holds its own licence, permit or registration for the unit. A brand licence held by the entity itself fails.
2. Employer of record. The counterparty employs the people who do the work in the unit. Chef-partner deals, consulting arrangements, "in collaboration with" and franchisor-only relationships fail. Job postings, the counterparty's own careers page and the licence holder's name are the usual proof.
3. Inside the premises. The unit is physically within the entity's own building or parcel: the entity's own page lists it, or the suite sits within the entity's footprint. Same street number is not enough; mixed-use towers need a floor or suite check.
4. Live today. Open and operating now, with at least one source dated this year: the counterparty's own site or social post, an active licence in the current extract, a listing update, a press item. Announcements, "coming soon", undated pages and anything about a venue that has since closed fail.

## Status from the tests

- All four pass: `ready`.
- Test 2 fails, the rest hold: `licensed` (the name is on the door, the entity runs the room). Shown on the map as a different deal shape, never as a set-aside.
- Test 1 or 3 unproven, test 4 holds: `verify`. The counterparty field names the specific unknown ("lease versus owner-affiliated venture not confirmed").
- The unit facts hold but the owner is changing hands (a Step 5 trigger of type sale or assignment with no confirmed closing): `transition`.
- Anything else: `aside`. Counted, never listed.

Two agents that disagree on a row put it in `verify`, not `ready`.

## Evidence rules

- Every source gets a date. A source older than the current year is context, not proof.
- Prefer primary sources: the counterparty's own site, the licence extract, the entity's own page, the authority's minutes, a filing. Aggregators and old press are pointers to primary sources, not proof.
- `ready` needs two independent sources, at least one of them primary and dated this year.
- Quote what the source says before interpreting it. If two sources conflict, record both verbatim in the working notes and set `verify`.
- Never accept terms, solve a CAPTCHA or create an account to reach a source. Queue it for a human.
- Never invent an owner, operator or date. A blank is a defect; "unknown" with a reason is a finding.

## The refute-mode agent prompt (fill the brackets)

```
You are checking one row of a market map and your job is to disprove it. Assume the row is wrong until evidence dated [current year] says otherwise.

Row (JSON): [row]

The relationship being mapped: [split question from Step 1].
The four tests, for this niche:
1. Separate party: [instantiated]
2. Employer of record: [instantiated]
3. Inside the premises: [instantiated]
4. Live today: [instantiated]

Do this, in order:
- Open the entity's own page for the unit. Does it name the counterparty, and how (operator, partner, "our restaurant")?
- Open the counterparty's own site and its most recent social post or job posting. Is this unit listed as a current location? Date it.
- Check the licence or permit record at the address: who holds it, is it active, what is the extract date?
- Search for closure, sale, rebrand or operator change involving the unit or the entity in [current year] and [previous year].
- For the owner: does any [current year] source contradict the owner in the row?

Rules: cite a URL and a date for every claim; never accept terms or bypass a CAPTCHA; never guess; if a fact cannot be reached, say UNKNOWN and why. Plain words, no em dashes, no superlatives.

Return JSON only:
{
  "entity": "...",
  "verdict": "HOLDS" | "REFUTED" | "UNPROVEN",
  "status": "ready" | "licensed" | "verify" | "transition" | "aside",
  "tests": {
    "separateParty": {"result": "pass|fail|unknown", "evidence": "...", "date": "YYYY-MM-DD"},
    "employerOfRecord": {"result": "...", "evidence": "...", "date": "..."},
    "inside": {"result": "...", "evidence": "...", "date": "..."},
    "liveToday": {"result": "...", "evidence": "...", "date": "..."}
  },
  "corrections": {"counterparty": "...", "unit": "...", "owner": "..."},
  "statusEvidence": "one or two sentences naming the sources and dates that decide the status",
  "trigger": {"what": "...", "when": "...", "source": "...", "sortDate": "YYYY-MM"} or null,
  "sources": ["url", "url"]
}
```

## Fan-out rules

- One agent per candidate row: the `OUTSIDER_AT_ADDRESS` rows and any row an earlier pass marked `ready`, `licensed`, `verify` or `transition`. Do not refute-verify `aside` rows one by one; a spot check of ten is enough.
- Ask for JSON only, parse defensively, and merge into `rows.json` yourself. Keep the agent's `sources` in a working field; the page shows `statusEvidence`, not raw URLs.
- Use the cheapest model that reads a page reliably for the fan-out, and a stronger model for the merge and the final numbers check.
- Record in `journal.md`: date of the pass, rows checked, rows moved between statuses, and any row where two sources conflicted.

## Failure modes seen in practice (check each row against this list)

- A chef's or brand's name on a room the entity staffs itself (name on the door).
- A venue cited from an old article that has since closed; a successor operator missed.
- An announcement date reported as an opening date; a signing date invented from a press-release date.
- A consultant, "culinary director" or "chef partner" read as an operator.
- A tenant at the same street number but in the office podium or the next parcel.
- A franchisor named as operator when a franchisee runs the unit.
- The management company named as owner.
- Press from two or more years ago used as current evidence.
- The entity's own venue with an outside-sounding name counted as an outsider.
- Two rows for one entity under two names (brand rename, "formerly").

## After the pass

Every table row has `status`, `statusEvidence` with dates, `evidenceDate` (YYYY-MM-DD, the newest source date behind the status), and `counterparty` text that names what is known and, for `verify`, exactly what is not. Rewrite the seeded candidate text in `unit` and `counterparty` with what the pass found. The renderer refuses blank evidence, a missing or malformed `evidenceDate`, and a `transition` row without a trigger. Agent text merged into a rendered field (`unit`, `counterparty`, `owner`, `ownerEvidence`, `statusEvidence`, `note`, the trigger) must be free of em and en dashes and contact details; `sources` and the other working fields are not checked, so URLs and raw notes go there.
