---
name: one-pager
description: Turn a prospect research file (facts with sources) and an optional sender voice profile into one personalised, print-ready HTML page per prospect plus the three-line email that carries it. The page is the personalisation, built from the prospect's own numbers, one finding, what it would take, and one ask. Use when the user says "one-pager", "one pager for this prospect", "build the page for", "personalised document", "turn this research into a page", "write the doc and the email", or wants a per-prospect leave-behind for before or after a sales call.
argument-hint: <prospect-research-file> [voice-profile-file]
user-invocable: true
---

# One-pager

The document is the personalisation. One page built from the prospect's own numbers, carried by a three-line email, does more than any clever first line and costs minutes to generate. This skill produces the page (print-ready HTML), the email, and working notes that trace every prospect-specific claim to its source.

`$ARGUMENTS` holds the research file path and, optionally, the voice profile path. Without a research file path, stop and ask for one.

## What gets written (per prospect)

Beside the research file, in a folder named `one-pager/`, unless the user names another location:

| File | What it is |
|---|---|
| `<slug>-page.html` | The one-page document, print-ready, built from `references/html-template.md` |
| `<slug>-email.txt` | Subject line plus the three-line email that carries the page, ending in the sender's real sign-off |
| `<slug>-notes.md` | Working notes: claim ledger with a source per claim, arithmetic, the finding chosen and the runners-up, checks run, and what was left off the page |

`<slug>` is the prospect organisation in lowercase with hyphens (`harbor-lights-hotel`).

## Inputs

**Research file (required).** Any text format. Every prospect-specific fact needs a source: a URL, a document name, a filing reference, or "call with <name>, <date>". A fact without a source is unsourced and never reaches the page. If the file has fewer than three sourced facts, stop and report what is missing rather than building a page on guesses. A hand-written list of facts with links works. From the companion skills in this pack, hand over `rows.json` from `/prospect-map` (one JSON object per entity, evidence fields as the sources; name the entity so the right row is used) or `CALL-NOTES-<slug>-<date>.md` from `/discovery-sheet` (the file is the source; what the prospect said enters the ledger as `STATED` with the call date and who said it; what the sender said enters as `STATED`, sender-side; the author's readings, plans and proposed terms enter as `INFERRED` and stay off the page).

**Voice profile (optional).** A short file describing how the sender writes: greeting, exact sign-off, sentence length, words they use, words they never use. Build one from 5 to 10 of the sender's own unassisted messages using `references/voice-profile.md`. If the second path holds raw messages rather than a built profile, build the profile per that file's sections 2 to 4 before step 1 and save it beside the research file. With no profile and no samples, use the neutral default in that file and say so in the notes.

**Sender line (required for the footer).** Name, firm, and one contact: an email address or a phone number. Take it from the voice profile's Sender line when present; otherwise from a third argument "<name>, <firm>, <contact>" or a `sender.md` beside the research file; otherwise ask the user once, before step 6. A batch or agent run that cannot ask stops before step 6 and reports the missing sender line. Never invent a contact and never lift one from the research file, which is about the prospect.

## Procedure

Load `references/writing-rules.md` before drafting anything. It holds the rules in full, the banned phrase list, the length budgets, and the self-review checklist.

### 1. Read everything, then build the claim ledger

Read the research file in full and the voice profile if given. In the notes, list every prospect-specific fact as a ledger row: claim, source, date checked, status.

Status values:
- `VERIFIED`: public record, the prospect's own site or documents, or a scan or test you ran and saved
- `STATED`: the prospect said it, with the call date and who said it
- `BENCHMARK`: an industry figure, not about this prospect, with its source
- `INFERRED`: a reasonable reading of the facts, not itself a fact
- `UNSOURCED`: no source given

Only `VERIFIED` and `STATED` rows may appear on the page as statements. `BENCHMARK` appears once at most, labelled as an industry figure. `INFERRED` may appear only as a question in the ask or as an "if" in what it would take. `UNSOURCED` never appears and is never mentioned to the prospect. When WebFetch is available and a source is a URL, re-open it, confirm the page still says what the ledger says, and record the date.

Sender-side claims (track record, results, clients) follow the same rule: a source in the ledger or nothing.

### 2. Put the situation in their own numbers

Choose up to three figures that describe where the prospect stands, drawn from `VERIFIED` or `STATED` rows or computed from them. Show every computation in the notes with its inputs. Use the prospect's own units and wording ("64 rooms", "19 of 30 nights", "$16"). No benchmarks in this block.

### 3. Choose one finding

One, not a list. Pick the finding that is specific to this prospect, sourced, consequential in their own numbers, and something they can act on. Write the two runners-up in the notes with one line each on why they lost. State the finding as a fact and the door it opens, never as a verdict on the prospect.

### 4. Write what it would take

Three steps at most, each concrete enough to start on Monday, in the order they would happen. One effort line: time from their side and time from the sender's side. No pricing on the page unless the user supplies it in the research file with a source.

### 5. Write the ask

One ask, phrased as a question, with a concrete unit of time ("a 20 minute walk-through"). Never two options. Never urgency the facts do not support.

### 6. Fill the page

Open `references/html-template.md`, copy the template, replace every `{{PLACEHOLDER}}` (the `<title>` included), and delete any figure block, step, or optional line you did not use. The footer's first line is the sender line from the Inputs, in the template's shape: name, firm, middle dot, contact. Keep the footer's standard line: it states the sourcing standard in one sentence, which is how rigour is shown. Do not add sections. Stay inside the length budgets so the page prints on one sheet.

### 7. Write the email

Subject: plain and descriptive, six words or fewer. Greeting from the profile. Three body lines, each a short paragraph of one or two sentences:
1. What this is and why it exists, from one ledger fact
2. The finding in one sentence, carrying the page's single most important figure
3. The ask, as a question

Then the sender's sign-off exactly as the profile gives it, line breaks included. No preamble, no "I hope", no introduction of the sender or their firm, no postscript. The page does the explaining.

### 8. Self-review, fix, re-run

Run the checklist at the end of `references/writing-rules.md`, including the grep commands: dashes on all three files, banned phrases on the page body and the email only (the notes must name `INFERRED` and `UNSOURCED` rows, so they are exempt), word counts on the page and the email. Fix every hit and run again until clean. Paste the final command output into the notes. Open the HTML in a browser if one is available and confirm it prints on one sheet. With Chrome or Edge installed, `<browser binary> --headless --no-pdf-header-footer --print-to-pdf=<slug>.pdf "<absolute path to page>"` produces the PDF; the binary is rarely on PATH, so use the full path for your OS from `references/html-template.md` section 2.

### 9. Report

Give the user the three absolute paths, the finding in one sentence, and the `INFERRED` and `UNSOURCED` rows they may want to verify before sending. Nothing else.

## Rules that override everything else

- Facts only. Every prospect-specific statement on the page or in the email traces to a ledger row.
- Never invent rapport. No "loved your", "big fan", "congrats", "hope you're well". A sourced personal connection may appear in email line 1 only, stated as the fact it is.
- No em dashes anywhere. Rewrite the sentence with a comma, a colon, a full stop, or parentheses.
- No confession copy. Never narrate the sender's process, rework, misses, or doubt. Finished state and method only.
- No first/founding language. The prospect is never the first, a pilot, a beta, a founding or early client, and the sender is never new or "building".
- Numbers on their own line. Figures live in figure blocks on the page; in the email, the one figure sits in a line of its own.
- Speech is written as speech. Any line meant to be said aloud is written the way it would be said.
- The email stays short and ends with the sign-off the profile gives; with no profile, the neutral default's "Best," then first name, and the notes say so.

## Batch runs

Given a folder of research files, run the procedure once per file. Drafting (steps 1 to 7) may fan out to parallel `Agent` calls, one prospect each, with this skill's rules and reference files named in the prompt; run step 8 serially on every output. One prospect's text never carries into another's page.

## Optional upgrades

None are required. This skill needs only Read, Write, Bash, and optionally WebFetch to re-check a source URL. If you have Firecrawl, Bright Data, Apify or Scrapling, use them upstream to build a richer research file; the page rules do not change.

## Reference files

- `references/writing-rules.md`: rules in full, banned phrase list, length budgets, self-review checklist with grep commands. Load before drafting.
- `references/voice-profile.md`: how to build a voice profile from 5 to 10 unassisted messages, the profile template (with the Sender line the footer needs), the neutral default, and a fictional example (Dana Reyes, Fensworth Advisory).
- `references/html-template.md`: the print-ready page template with placeholders and the print rules.
- `references/worked-example.md`: a complete fictional run for Harbor Lights Hotel: research file in; ledger, page, email and notes out.
