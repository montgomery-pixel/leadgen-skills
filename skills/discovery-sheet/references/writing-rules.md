# Writing rules and the review checklist

Contents
1. The eight rules
2. The grep pass (run it, do not eyeball it)
3. Fixes for the common defects

Each rule prevents a defect that costs a call. They are not style preferences.

---

## 1. The eight rules

### Rule 1. Quote first, interpret second, label the interpretation
Every claim about what the prospect wants, earns, or will do traces to a quote in the
file. Interpretation is allowed only after the quote and only with a label:
`Arithmetic:` (a sum you did), `Read:` (what you think a line means), `Unverified:`
(the file does not settle it). An unlabelled interpretation reads as a finding and
gets repeated as one. When two lines disagree, both go in under CONFLICTS, neither is
picked, and the next call asks.

Cutting a quote: a quote may start or stop at a clause boundary. Close a cut quote with
a full stop inside the quotation marks, or mark the cut with three dots. The words inside
the quotation marks never change; a cut is not an alteration, a changed word is.

### Rule 2. Facts only, no invented rapport
Nothing about how the prospect felt unless they said it in words. No "seemed engaged",
"clearly excited", "loved the idea". No claims about their business the file does not
contain. If the seller wants a warm opener for the next call, it is a fact the prospect
stated or a public fact with a source, never a compliment.

### Rule 3. Numbers on their own line (THE NUMBERS section)
One figure per bullet, in bold, with the quote it came from. A range is one figure. Two
figures in one bullet is a defect because the second one gets lost when the bullet is
copied into a proposal. Hedges travel with the figure: "four, tops" is not "4".

### Rule 4. Speech is written as speech (SKELETON)
Every bullet that will be said aloud is a complete spoken sentence with a verb. A number
lives inside the sentence where the stress falls. A figure never trails after a comma as
an appositive and never stands alone after a full stop.

Wrong: "Clubs that already use an outside company. Thirty-one."
Wrong: "Corporate-owned clubs in Oregon, six. Idaho, one."
Right: "Thirty-one of them already pay somebody else to run the grounds."
Right: "Six of the corporate-owned clubs are in Oregon, and only one is in Idaho."

Contractions are fine. Don't narrate a table; say what the table means. Never write the
instruction "the number as the punch" anywhere; it produces exactly the wrong pattern.

### Rule 5. No em dashes
No em dashes and no en dashes used as dashes, in either file. Use a comma, a full stop, a
colon or parentheses. This applies to quotes too: people rarely speak in dashes;
recorders insert them. Replace with a comma inside the quote.

### Rule 6. No confession copy
Anything the prospect will see or hear presents the finished state and the method. It
never narrates how the work got there, what was wrong before, what is still being
checked, how big a number used to be, or that this is a first. Disclosing a risk to the
prospect is fine. Disclosing your own rework is not.

Applies to: SHOW bullets, TERMS lines, answers under WHAT THEY ASKED US that will be
said back, and anything copied from these files into a proposal or email.

Banned in those places: "we found", "turned out", "we corrected", "we got that wrong",
"still confirming", "the first count was", "we haven't done this before", "we missed",
"we're not sure", and "first" or "founding" as a claim about your own track record.

Wrong: "Nine of the owners came back different from what the club websites said."
Right: "Every owner on the list was checked against the state business registry and the
club's own filings."
Wrong: "Four we're still confirming."
Right: (cut the line.)

### Rule 7. No unbriefed proper nouns (SKELETON)
Every person, company, place, brand, product or document named in a question appears
in the BRIEFED block. The test: hand the SKELETON to someone who has read only BRIEFED.
If any question makes them ask "who is that?", the sheet fails. Fix by adding a BRIEFED
line or by rewriting the question without the noun.

### Rule 8. Notes never become verbatim
A file graded NOTES produces quotes without quotation marks, each ending `(notes)`. They
stay that way in every downstream document. The moment a paraphrase gains quotation
marks it becomes a claim the prospect can deny.

---

## 2. The grep pass

Run from the folder holding the two files, in bash or zsh (Git Bash on Windows works).
Name the two new files explicitly; a glob would also scan older files for the same
prospect. Every command should return nothing, except the proper-noun list, which you
check by hand against BRIEFED. The patterns use POSIX classes only, so they run the same
under GNU grep and the BSD grep on macOS.

```bash
N=CALL-NOTES-<slug>-<date>.md
S=SKELETON-<slug>-<date-or-next>.md

# Rule 5: dashes (em dash U+2014, en dash U+2013, given as bytes so this file stays clean).
# Want: no output.
grep -n $'\xe2\x80\x94' "$N" "$S"
grep -n $'\xe2\x80\x93' "$N" "$S"

# Rule 6: confession words on the sheet the seller reads aloud. Want: no output.
# A hit inside a prospect quotation or under NEVER is not a defect.
grep -niE "we found|turned out|we corrected|got (it|that) wrong|still confirming|first count|haven't done|we missed|not sure|founding|first time|our first|the first one" "$S"

# Rule 4: a figure trailing after a comma, or alone on a line. Digits, then number words.
# Want: no output from any of the four.
W="(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million)"
grep -nE ",[[:space:]]*[0-9][0-9,.]*%?[[:space:]]*\.?$" "$S"
grep -nE "^[[:space:]]*[-*]?[[:space:]]*[0-9][0-9,.]*%?[[:space:]]*\.?$" "$S"
grep -niE ",[[:space:]]*$W([[:space:]-]$W)*( percent)?[[:space:]]*\.?$" "$S"
grep -niE "^[[:space:]]*[-*]?[[:space:]]*$W([[:space:]-]$W)*( percent)?[[:space:]]*\.?$" "$S"

# Rule 7: proper-noun candidates, including all-caps (GM, CEO) and mixed-case (McAllister).
# Sentence-openers will appear too; check each real name against BRIEFED by hand.
grep -oE "[[:upper:]][[:alpha:]]+([[:space:]][[:upper:]][[:alpha:]]+)*" "$S" | sort -u

# Rule 2: rapport words. Want: no output in either file.
grep -niE "seemed|clearly (excited|keen|interested)|loved|enthusiastic|rapport" "$N" "$S"
```

Then two checks no grep can do:

- Rule 1: pick five quotes at random from CALL NOTES and find each in the source file. A
  quote cut at a clause boundary and closed with a full stop counts as found. If one is
  missing or has a changed word, check them all.
- Rule 3: scan THE NUMBERS. Any bullet holding two bold figures gets split.

---

## 3. Fixes for the common defects

| Defect | Fix |
|---|---|
| A bullet with two numbers | Split into two bullets, each with its own quote. |
| "About $10M" written as "$10M" | Restore the hedge: "about $10M". |
| A question naming a person not in BRIEFED | Add "<Name>, <role>, <what they control>" to BRIEFED. |
| A SHOW bullet that explains how the list was built by listing what was wrong before | Replace with the method: what was cross-referenced, what standard each row met. |
| "She was excited about the resort angle" | "Resorts: 'yes, actually that's interesting. We haven't gone after those.'" |
| A sum presented as the prospect's figure | Prefix `Arithmetic:` and move it to the end of the section. |
| Two quotes that disagree, one silently chosen | Both under CONFLICTS; a question on the SKELETON. |
| A stage direction on the SKELETON ("pause", "then pivot to") | Delete it. The sheet is bullets the seller reads, not blocking. |
| A price in TERMS the seller never said | Delete it. TERMS carries only what BINDS holds. |
