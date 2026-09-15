# Working files: journal.md and manual-queue.md

Both are working notes, never deliverables. Keep the shape below so two runs of the same market read the same way and a refresh can be diffed against the last run.

## journal.md

```
# Prospect map: <niche> in <geography>
Skill dir: <absolute path to the folder holding SKILL.md>
Working folder: <absolute path>
Started: YYYY-MM-DD

## Step 1: the split question
Payer: <who signs>
Payee: <who is paid today>
Split question: <one sentence a public record can answer>
Tests for this niche: 1 separate party: ... 2 employer of record: ... 3 inside: ... 4 live today: ...
Inclusion rule: <what counts as an entity in the market>
Region granularity: <state | county | metro>

## Sources
YYYY-MM-DD | <URL> | extract dated <date> | <rows> rows | sources/<file>

## Step 2: the count
Count: <n>. Inclusion rule applied: <restated>.
Coverage check: 10 named, <n> found. Misses and reasons: <entity: reason> ...
Address join: OUTSIDER_AT_ADDRESS <n>, SELF_ONLY <n>, NO_LICENCE_AT_ADDRESS <n>, NO_ADDRESS <n>.
Seeded rows.json: <n> rows, <n> candidates.

## Step 3: owners
Counties and endpoints: <county: endpoint URL, field names, rows returned> ...
Joined by address: <n>. Confidence split: high <n>, medium <n>, low <n>, unknown <n>.

## Step 4: refute pass, YYYY-MM-DD
Budget: <n> candidates at 15,000 to 25,000 tokens each.
Rows checked: <n>. Moved: <entity: from -> to, reason> ... Conflicts: <entity: source A says, source B says> ...

## Step 5: triggers
Window: 36 months. Triggers attached: <n>.

## Steps 6 and 7
--check output: <pasted>
Random five re-opened: <entity: held | sent back> ...
```

## manual-queue.md

```
# Manual queue: sources that need a person

| Entity | What is needed | Where | Exact search to run | Why an agent stops here |
| --- | --- | --- | --- | --- |
| <entity> | owner of record | <county portal URL> | Parcel search: 12 Quay Street | click-through terms |
| <entity> | licence holder | <state portal URL> | Premises search: 400 Harbor Road, active only | CAPTCHA |
```

Each row is about two minutes of a person's time. When the answer comes back, write it into `rows.json` with the date and the record name, and log it under the matching step in `journal.md`.
