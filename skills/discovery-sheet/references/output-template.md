# Output template: CALL NOTES and SKELETON

Contents
1. File naming and header
2. CALL NOTES, section by section
3. SKELETON, section by section
4. Placeholders, copy and fill

Both files are Markdown. Short lines. Bold only for the figure in a numbers bullet and
for the one or two questions the seller cannot leave without. No tables in the SKELETON;
the seller is glancing at it while someone talks.

---

## 1. File naming and header

`CALL-NOTES-<prospect-slug>-<YYYY-MM-DD>.md` where the date is the call date, taken from
the transcript or the file name. If neither has it, use today's date and write
`(date assumed)` in the header.

`SKELETON-<prospect-slug>-<YYYY-MM-DD>.md` where the date is the next call if it was
booked, otherwise `SKELETON-<prospect-slug>-next.md`.

The prospect slug is the first name, or the company if the first name is unknown, lower
case, hyphens.

CALL NOTES header (the first lines of the file):

```
# CALL NOTES: <Prospect full name>, <company>, <date>, <time and timezone> (<duration>)

Source: <path | pasted into chat>. Grade: VERBATIM | NOTES. Shown: <nothing | deck |
map | document>. Who talked: <one clause, e.g. the prospect volunteered most of it; the
seller asked eleven questions>. Flags: <none | no speaker labels; attribution inferred |
speaker labels doubtful from 14:20 | recording gap at 31:00>.
```

---

## 2. CALL NOTES, section by section

### OUTCOME
Four to eight bullets. What the prospect asked for, what was agreed, what was refused,
what each side will do before the next contact, and the next call if booked (day, date,
time, timezone, who sends the invite). Quotes where the prospect's wording matters
("send that over, I'll walk my partner through it").

### THE ONE NUMBER
One line naming the figure that decides the deal, then one of:
- `Captured:` the figure in bold and the verbatim quote.
- `Not captured:` who holds it, what was said instead, and the note that it is line one
  of the SKELETON.

### THE NUMBERS (verbatim where it matters)
One figure per bullet. The label, the figure in bold, the quote it came from. Ranges stay
ranges, hedges stay hedges ("hopefully", "usually", "tops"). End the section with any
sums you did, each on its own line and each starting `Arithmetic:`. Never fold a sum
into a prospect bullet.

### ICP, IN THEIR WORDS
Sub-bullets in this order, each carrying a quote: size (floor and ceiling), type or
brand, owner or buyer type, NOT the ICP (their own words for who to skip), scope (what
they would run or sell), geography (in, out, would add, conditions), adjacent segments
(anything they said "yes" or "interesting" to that they do not chase today). Where the
prospect gave a reason ("the board has to vote"), keep the reason; it is the pitch line
later.

### DEAL ECONOMICS
How the prospect gets paid on one closed deal, in their words: base, incentive, anything
up front, when billing starts, time from signing to first payment, onboarding time, best
deal vs typical deal, capacity per year, sales cycle by buyer type, conversion if given,
who on the buyer's side has to say yes. Then, labelled `Arithmetic:`, what one closed deal
is worth to them in year one, and, labelled `Read:`, what that implies for the seller's
fee. Both labelled, both on their own lines.

### WHO THEY ARE (from the call only)
Background the prospect gave: company age, size, history, key people and roles, models
they admire, tools they use, how past deals came in. Nothing from outside the file. If the
user later adds a research pass, it goes under its own heading with sources.

### WHAT THE SELLER SAID THAT NOW BINDS US
Every price, term, concession, promise or agreement the seller uttered, as a quote,
one per bullet. Include agreements by assent ("completely fine", "sure, we can do that").
Include useful lines worth keeping ("I do need a baseline to cover my costs"). End with
one bullet beginning `Did not:` listing what the seller did not quote, mention or promise.
That line stops the next call from inventing a promise that was never made. On a file
flagged `no speaker labels`, every bullet whose speaker was inferred starts
`Read: seller.` before the quote.

### WHAT THEY ASKED US
Each question the prospect asked, as a quote, and after it either `Answered:` with the
answer given, or `Owed:` if the seller deferred. Owed items go on the NEXT CALL list. On
a file flagged `no speaker labels`, a bullet whose speaker was inferred starts
`Read: prospect.` before the quote.

### OPEN QUESTIONS
What the call did not settle and the next call must. Each one becomes a bullet on the
SKELETON, so write them as questions to the prospect, not notes to self.

### CONFLICTS
Lines that disagree with each other or with the seller's earlier material. Both quotes,
timestamps if present, no reconciliation. If the section is empty, write `None found.`

### NEXT CALL: WHAT HAS TO HAPPEN
Numbered. What the next call or the next document must do to move the deal: answer the
prospect's ask exactly, deliver what was owed, get the one number, get the decision-maker
in the room, book the step after. Three to six items.

---

## 3. SKELETON, section by section

### Title
`# <FIRST NAME>, <day> <time>` on one line. If no next call is booked:
`# <FIRST NAME>, NEXT CALL (not booked)`. Nothing else.

### The minute-12 line
Immediately under the title, alone:
`Minute 12 without <the one number>: drop everything and ask it.` Add who holds it if
someone other than the prospect does. If the number was captured on the last call, this
line names the next most important unknown instead, or reads `The one number is in hand:
<figure>. Say it back to them early.`

### WALK OUT WITH
Three to five numbered items. The answers and commitments that make the call a success.
Each one is checkable at the end of the call.

### BRIEFED
One line per proper noun used anywhere below: people (name, role, what they control),
company (one fact), footprint (the places), documents (what the prospect holds), assets
(what will be shown). This block is what lets every question below stand alone.

### ORDER
Numbered running order, six to nine lines. The default: hellos with one line of real news
from the notes, where they landed with the other decision-maker, VERIFY, the show if any,
discovery, "what questions do you have for me", terms, book the next step. Each line is
short enough to glance at.

### VERIFY (before the pitch)
The four-part list from the SKILL: goal and alternate shapes, geography, who decides, ICP
edges. Each item is a full spoken question. Edge cases get an ASK line: "does that count
for you, or is it a dead end?"

### SHOW (only if there is an asset)
Fact bullets about the asset, in the order they will be said, ninety seconds total. One
number per bullet inside a full sentence. ASK lines inline where the seller stops for an
answer. The last line is what the prospect keeps whatever happens.

### DISCOVERY
A. Who to hunt. B. Economics, marked CANNOT LEAVE WITHOUT. C. Cash. D. What we book.
E. If time. Pick from `question-bank.md`; keep only what this call left open. Six to
fifteen questions across all five.

### TERMS (only if a price is on the table)
The number already in writing, said as settled. What discovery moves and which way. The
one trade card, timing not amount. The guarantee sentence if one is offered, and the
instruction to stop after it. The seller's figures come from BINDS; none from this skill.

### NEVER
Short list of lines the seller must not say, numbers not to quote, names not to use,
scope not to add, promises not to make. Each item one line.

---

## 4. Placeholders, copy and fill

```
# CALL NOTES: <Name>, <Company>, <date>, <time TZ> (<minutes> minutes)

Source: <path | pasted into chat>. Grade: <VERBATIM|NOTES>. Shown: <...>. Who talked: <...>. Flags: <...>.

## OUTCOME
- ...

## THE ONE NUMBER
<What it is.> Captured|Not captured: ...

## THE NUMBERS (verbatim where it matters)
- <Label>: **<figure>.** "<quote>"
- Arithmetic: ...

## ICP, IN THEIR WORDS
- **Size:** ...
- **Type:** ...
- **Buyer type:** ...
- **Not the ICP:** ...
- **Scope:** ...
- **Geography:** ...
- **Adjacent:** ...

## DEAL ECONOMICS
- ...
- Arithmetic: ...
- Read: ...

## WHO THEY ARE (from the call only)
- ...

## WHAT THE SELLER SAID THAT NOW BINDS US
- "<quote>"
- Did not: ...

## WHAT THEY ASKED US
- "<question>" Answered: ... | Owed: ...

## OPEN QUESTIONS
- ...

## CONFLICTS
None found. | - <quote A> vs <quote B>

## NEXT CALL: WHAT HAS TO HAPPEN
1. ...
```

```
# <FIRST NAME>, <DAY> <TIME>

Minute 12 without <the one number>: drop everything and ask it.

## WALK OUT WITH
1. ...

## BRIEFED
- ...

## ORDER
1. ...

## VERIFY (before the pitch)
- ...

## SHOW
- ...

## DISCOVERY
**A. Who to hunt**
- ...
**B. Economics. CANNOT LEAVE WITHOUT.**
- ...
**C. Cash**
- ...
**D. What we book**
- ...
**E. If time**
- ...

## TERMS
- ...

## NEVER
- ...
```
