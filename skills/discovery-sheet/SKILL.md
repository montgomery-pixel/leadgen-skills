---
name: discovery-sheet
description: Turn a sales-call transcript or rough call notes into two files. CALL NOTES (facts with verbatim quotes, every number the prospect gave on its own line, the ICP in the prospect's own words, deal economics, what the seller promised, open questions) and a next-call SKELETON (standalone fact bullets the seller can read aloud, not a script). Use when the user says "discovery sheet", "call notes from this transcript", "debrief this call", "what did they actually say", "prep the next call", "skeleton for the follow-up", "ICP in their words", "what did I promise on the call", or drops a transcript, recording export or notes file after a sales, discovery or intro call.
argument-hint: <transcript-or-notes-file> [prospect name]
user-invocable: true
---

# Discovery Sheet

A sales call is only worth what you can prove it said. This skill turns one call into a
record you can act on and a sheet you can hold on the next call. It records, it does not
summarise, and it never invents.

Two outputs, written next to the input file unless the user names another folder. If the
transcript was pasted into chat and there is no input file, write both to the current
working directory and say so in the handover:

- `CALL-NOTES-<prospect-slug>-<call-date>.md` (the record)
- `SKELETON-<prospect-slug>-<next-call-or-next>.md` (what the seller holds mid-call)

Section order and contents for both: `references/output-template.md`.
Rules and the grep checklist: `references/writing-rules.md`.
Generic VERIFY list and discovery questions A to E: `references/question-bank.md`.
A fully fictional transcript and the two files it produces: `references/worked-example.md`.

## Inputs

- `$1` path to a transcript (.txt, .md, .vtt, .srt, .json from a recorder) or human notes.
  For .docx or .pdf, extract to text first (pandoc if installed, otherwise a document
  skill if one is available, otherwise ask the user for a text export). If the transcript
  was pasted into chat instead, the pasted text is the source and the header reads
  `Source: pasted into chat`.
- Everything after the path is the prospect name, optional. Quote a name with spaces
  (`"Priya Lindqvist"`); the positional split otherwise leaves only the first word in
  `$2`. If absent, infer it from the file and mark it `(inferred)` in the header.
- Nothing else. This skill does not web-search to fill gaps. Every fact in the notes traces
  to the file. Outside facts belong in a research skill and carry a source if they appear.

## Procedure

### 1. Read the whole file before writing a word

Note in the header: source type, call date and time, duration, who was on it, what was
shown (nothing, a deck, a map, a document), who did most of the talking.

Set the quote grade once for the whole file:

- **VERBATIM** for a transcript, with or without speaker labels. Quotes go in quotation
  marks. Without speaker labels (auto-captions, most .vtt and .srt exports): ask for a
  labelled export first. If the user says to use the file as is, the header Flags line
  reads `no speaker labels; attribution inferred`, and every bullet under WHAT THE SELLER
  SAID THAT NOW BINDS US and WHAT THEY ASKED US whose speaker you inferred starts with
  `Read: <who you think said it>.` before the quote.
- **NOTES** for human notes or paraphrase. Quotes carry no quotation marks and end with
  `(notes)`. Never promote a notes-grade line to quotation marks, in this file or later.
- **MIXED** for a curated extract or notes with pasted quotes: grade VERBATIM, keep
  quotation marks only on lines the file itself marks verbatim, carry every paraphrase
  without marks ending `(notes)`, and add `extract, not the full transcript; <timestamps>
  withheld` to Flags. The BINDS closing bullet then reads `Did not (in this file):`.

Check speaker labels. Auto-diarization swaps speakers. If a labelled line contradicts its
label (the "prospect" quoting the seller's own price back as an offer), flag it in the
header. Do not silently reassign.

### 2. Build the fact ledger (scratch, not output)

One line per fact: `[speaker] "verbatim" -> what it establishes`. Tag lines:

- **NUM** every figure, one per line. Ranges stay ranges. "About ten" stays "about ten".
- **BINDS** every price, term, deadline, concession or promise the seller uttered.
- **Q** every question the prospect asked, with the answer given or owed.
- **NEXT** every "I'll send", "I'll talk to", "Thursday works".
- **ICP** every line describing who they want, who they don't, where, what size, what shape.

No interpretation in the ledger. Quote first. Interpretation comes later, labelled.

### 3. Name the one number (the minute-12 rule)

Ask: which single figure decides whether this deal is worth doing and what to charge for it?
Usually it is what one closed deal makes the prospect in year one after costs. Sometimes it
is volume, budget or headcount. Name it in one line.

- Captured on the call: it goes under THE ONE NUMBER with its verbatim quote and repeats as the first bullet of THE NUMBERS.
- Not captured: it becomes line one of the SKELETON, above the running order:
  `Minute 12 without <the number>: drop everything and ask it.` If a named person holds
  that number ("I'd have to ask my partner"), say so on the same line.

### 4. Write CALL NOTES

Follow `references/output-template.md`. Sections, in order: header, OUTCOME, THE ONE
NUMBER, THE NUMBERS, ICP IN THEIR WORDS, DEAL ECONOMICS, WHO THEY ARE, WHAT THE SELLER SAID
THAT NOW BINDS US, WHAT THEY ASKED US, OPEN QUESTIONS, CONFLICTS, NEXT CALL: WHAT HAS TO
HAPPEN.

The rules that bite most:

- One figure per bullet, bold, followed by the quote it came from. Two numbers in one
  bullet is a defect.
- Interpretation is labelled every time: `Arithmetic:` for sums you did, `Read:` for what
  you think a line means, `Unverified:` for anything the file does not settle.
- What was NOT said is a fact. The BINDS section ends with a line listing what the seller
  did not quote, did not mention, did not promise.
- Nothing about mood, warmth, excitement or rapport unless the prospect said it in words.
  "She seemed keen" is fiction. "Nothing on there scared me" is a quote.
- Two lines that disagree both go in, under CONFLICTS, unreconciled.

### 5. Write the SKELETON

It is what the seller holds during the next call: fact bullets they can read aloud as
written. Not a script. No stage directions, no "then say", no "pause here".

Sections, in order: title (first name, time), the minute-12 line, WALK OUT WITH (three to
five items), BRIEFED, ORDER, VERIFY, SHOW (only if there is an asset to show), DISCOVERY A
to E, TERMS (only if a price is already on the table), NEVER.

**BRIEFED** is the contract that makes the standalone rule work. Every person, company,
place, product or document named anywhere below it gets one line here. A reader who has
seen only BRIEFED must understand every question on the sheet. If a proper noun in a
question is not in BRIEFED, either add the line or rewrite the question without the noun.

**VERIFY** always runs before any pitch, show or price, and always covers four things:

1. The goal. What shape of deal they actually want, and which other shapes they would take.
2. Geography. What is in, what is out, what they would add.
3. Who decides. "Is this your call, or does <briefed name> need to be in?"
4. ICP edges. The boundary cases: "does this count for you, or is it a dead end?"

Pull candidate questions from `references/question-bank.md` and keep only the ones this
call left open. A skeleton that pastes the whole bank is a defect.

**Speech rule** on every bullet that will be said aloud: a full sentence with a verb, a
number inside the sentence where the stress falls, never a figure trailing after a comma or
standing alone after a full stop. Read each line in your head. If it needs a breath in an
odd place, rewrite it.

**TERMS** carries structure, and the seller's own numbers from BINDS. The number already in
writing is said as settled. Discovery moves only the variable part, and only in the
prospect's favour. One trade card that changes timing, never amount. No number before
their number. If the seller offers a guarantee, it is one sentence and then silence;
mechanics live in the letter. This skill supplies no prices.

### 6. Review pass, mandatory

Run the checklist in `references/writing-rules.md` before you hand over. In short:

- Em dashes and en dashes used as dashes: zero in both files.
- Confession words in anything read aloud or shown: zero. The prospect hears the finished
  state and the method, never how you got there or what you are unsure of.
- Every quote in CALL NOTES is findable in the source. A quote cut at a clause boundary
  and closed with a full stop counts as found; a changed word does not. Delete or
  downgrade any that is not.
- Every proper noun on the SKELETON is in BRIEFED.
- Numbers: one bold figure per bullet under THE NUMBERS, quotes elsewhere carry what they carry; inside a spoken sentence on the SKELETON.
- No invented rapport, no claims about the prospect the file does not contain.

### 7. Hand over

Tell the user, in this order and nothing more: the two file paths (and that they went to
the working directory, if there was no input file), the one number and whether it was
captured, the WALK OUT WITH list, and any CONFLICTS or speaker-label flags.
Do not re-summarise the notes in chat. They will read the file.

## What this skill is not

- Not a summary. Summaries lose the numbers and the quotes, which are the only parts that
  matter a week later.
- Not research. Research lives in a separate skill and carries sources; in this pack that
  is one-pager and prospect-map. This records a call.
- Not a script. A script gets read in the wrong order the moment the prospect talks.

## Optional upgrades, never required

- A speaker-labelled export from your meeting recorder beats auto-captions; ask for it
  before accepting a captions file. If only captions exist, step 1 says how to grade and
  flag them.
- If a CRM connector is attached, offer to paste OUTCOME and NEXT into the deal record after
  the user approves the text. Never write to a CRM without approval.
