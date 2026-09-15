# Voice profile: how to build one, the template, the neutral default, and an example

Contents
1. Why the sample matters
2. What to collect (5 to 10 messages)
3. What to extract, and how
4. Profile template
5. Neutral default (no samples available)
6. Fictional example: Dana Reyes, Fensworth Advisory
7. Applying the profile

## 1. Why the sample matters

The email must read as the sender, not as an assistant. The only clean evidence is text the sender produced alone. Sent mail is often contaminated: if the sender uses an assistant to draft, their inbox is full of the assistant's voice, and modelling on it copies the assistant back to itself. Short replies fired off by hand, chat messages, and transcripts of the sender speaking are clean.

## 2. What to collect

- 5 to 10 messages the sender wrote alone: short email replies, chat messages, a voice-note transcript, a rough draft they typed before anyone tidied it.
- Prefer messages to people outside their team (a customer, a prospect, a supplier).
- Exclude anything long and polished if the sender uses an assistant, newsletters, ghost-written pieces, and templates.
- Ask the sender one question: "How do you always sign off?" Their answer overrides the sample.

## 3. What to extract, and how

Each claim in the profile carries a quote or a count from the sample. No quote, no claim.

1. Greeting: exact form and count ("Hi Sam," 7 of 8).
2. Sign-off: exact words and line order, with the count. If the sample shows two, ask; if you cannot ask, take the majority and note it.
3. Sentence length: count words in 20 sentences; record the median and the longest.
4. Contractions: yes or no, with a quote.
5. Layout: paragraphs or bullets, bold, headers, as the sample shows.
6. Joins: commas with "and" and "so", or short separate sentences. Note whether dashes appear in the sample; they still never appear in output.
7. Opening: straight in, or small talk first, with a quote.
8. Closing move: question, statement, or instruction, with counts.
9. Favoured words: up to 10, each with the quote it comes from.
10. Never-use words: check the sample for the corporate list in writing-rules.md section 8 and for "excited", "thrilled", "reach out". Every word with zero hits goes on the never-use list.
11. Habits: undersells, hedges forecasts, discloses risk, asks permission before a sensitive topic, makes scheduling easy. Quote each.
12. Register shifts by audience, if the sample shows any.
13. What was excluded from the sample and why.

For speech transcripts: extract values and structure, not fillers. "Kind of", "you know" and "I mean" never go into writing.

## 4. Profile template

```markdown
# Voice profile: <Sender name>, <firm>
Built <date> from <n> unassisted messages (<types and date range>). Every claim carries a quote or a count.

## Sender line
- Footer: <Sender name>, <firm>, <one email address or one phone number>. Fills the page footer verbatim.

## Mechanics
- Greeting: "<exact>" (<count> of <n>)
- Sign-off: "<line 1>" then "<line 2>" on the next line (<count> of <n>). Confirmed by sender: yes/no
- Sentence length: median <n> words, longest <n>
- Contractions: yes/no ("<quote>")
- Layout: <paragraphs / bullets / bold / headers, as the sample shows>
- Joins: <"so" and "and" / short separate sentences> ("<quote>")
- Opening: <straight in / small talk first> ("<quote>")
- Closing move: <question / statement> (<count> of <n>) ("<quote>")

## Words
- Favours: <word> ("<quote>"), <word> ("<quote>")
- Never uses (zero hits in sample): <list>

## Habits
- <habit>: "<quote>"

## Register
- <shifts by audience, or "same voice with everyone">

## Sample
- Included: <messages with dates>
- Excluded: <what and why>
```

## 5. Neutral default

Use only when there is no profile and no sample, and write "neutral default voice used" in the notes.

- Sender line: none in the default. Ask the user once for name, firm and one contact (email or phone) before filling the page. Never invent one.
- Greeting: "Hi <First name>,"
- Sign-off: "Best," then "<Sender first name>" on the next line
- Sentence length: median 14 words, longest 22
- Contractions: yes
- Layout: paragraphs, no bullets, no bold
- Opening: straight in
- Closing move: a question
- Favoured words: none
- Never-use words: the corporate list in writing-rules.md section 8

## 6. Fictional example: Dana Reyes, Fensworth Advisory

Dana Reyes, Fensworth Advisory and every message below are invented for this example.

```markdown
# Voice profile: Dana Reyes, Fensworth Advisory
Built 2026-08-12 from 8 unassisted messages: 6 short email replies to hotel clients and suppliers (2026-03 to 2026-08) and 2 voice-note transcripts to her bookkeeper. Every claim carries a quote or a count.

## Sender line
- Footer: Dana Reyes, Fensworth Advisory, dana@northwind-advisory.example

## Mechanics
- Greeting: "Hi <First name>," (8 of 8)
- Sign-off: "Best," then "Dana" on the next line (7 of 8; the eighth was a one-line reply with no sign-off). Confirmed by sender: yes ("it's always Best, Dana, I don't do regards")
- Sentence length: median 13 words, longest 24
- Contractions: yes, every message ("I'll send the numbers Thursday", "that's the whole fix")
- Layout: paragraphs of one or two sentences; no bold, no headers; one bullet list in 8 messages, and it was a list of dates
- Joins: "so" and "and" ("the feed was late, so I ran it again"); no semicolons, no dashes
- Opening: straight in, no small talk in email ("Quick one on the September rates.")
- Closing move: a question (6 of 8) ("Does Thursday work?", "Want me to send the numbers?")

## Words
- Favours: walk-through ("happy to do a walk-through"), the numbers ("I'll bring the numbers"), on one page ("I put it on one page"), useful ("if that's useful"), quick ("quick one"), small fix ("it's a small fix")
- Never uses (zero hits): excited, thrilled, reach out, circle back, leverage, synergy, hope this finds you well, just checking in, touching base, solution, journey

## Habits
- Undersells: "it's a small fix, but it's worth the twenty minutes"
- Hedges forecasts: "I can't promise the number, I can promise the check"
- Discloses risk: "if the rate rule is wrong it takes a day to put back"
- Makes scheduling easy: "any afternoon next week is fine, you pick"

## Register
- Same voice with clients, suppliers and her bookkeeper; slightly shorter with people she has met in person

## Sample
- Included: 6 replies (2026-03-04, 2026-04-19, 2026-05-02, 2026-06-15, 2026-07-08, 2026-08-01), 2 voice notes (2026-07-22, 2026-08-09)
- Excluded: her monthly newsletter (drafted by an assistant), 3 proposal emails (built from a template)
```

## 7. Applying the profile

- Greeting and sign-off verbatim, line breaks included. Never substitute a closing you think reads better.
- The Sender line fills the page footer verbatim. A profile without one is incomplete: ask the sender for it before filling the page.
- Longest sentence in the email never exceeds the sample's longest. Aim at the median.
- Use two or three favoured words at most, and only where they fit. Do not sprinkle.
- Zero never-use words. Append them to the banned-phrase grep before the self-review.
- Match the closing move: if the sender closes with questions, the ask is a question in their shape.
- Match habits: if the sender undersells, the effort line undersells ("a small fix, worth the twenty minutes"). If the sender discloses risk, the "what it would take" block names the reversal path.
- The profile shapes the email and the prose blocks of the page. The figure blocks and the footer stay neutral.
