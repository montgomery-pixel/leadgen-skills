# Worked example (entirely fictional)

Contents
1. The input: a transcript excerpt
2. Output 1: CALL NOTES
3. Output 2: SKELETON
4. What the review pass caught

Every name, company, figure and place below is invented for this example. Fairway and
Fern, Priya Lindqvist, Sam Ortega and Tom do not exist. Any resemblance to a real
business is accidental.

The setup: Sam sells an outbound service that books first conversations with buyers.
Fairway and Fern runs outsourced grounds maintenance for private golf clubs and wants
more club contracts. Sam sent a one-page proposal (monthly retainer plus a fee per
signed contract, fee left open) before this call. Priya is the CEO. Tom is her
co-founder.

---

## 1. The input: a transcript excerpt

File: `calls/fairway-fern-2026-03-10.txt` (speaker-labelled export, 24 minutes; the
excerpt is the first five).

```
Recording: 10 March 2026, 10:00 PT. Length 24:12.
Participants: Sam Ortega; Priya Lindqvist (CEO, Fairway and Fern).

[00:00] SAM: Priya, thanks for making the time. Did the one-pager come through?
[00:08] PRIYA: It did. I skimmed it on the way in. Nothing on there scared me.
[00:15] SAM: Good. Before I show you anything, where are you with Tom on this?
[00:22] PRIYA: Tom's seen it. He's cautious. He's cautious about everything, that's
his job. It's me and Tom, we started it together, Tom runs the money. I wouldn't sign
anything without him seeing it.
[00:41] SAM: Understood. So new maintenance contracts are what you're after?
[00:47] PRIYA: Yes. We've got eleven clubs now. Two more signing this quarter,
hopefully. Every one of those came through somebody we knew. That well is drying up.
[01:05] SAM: What does a club pay you?
[01:09] PRIYA: Flat monthly. Somewhere between twenty-two and twenty-eight thousand a
month depending on acreage and how many holes. And there's a bonus if the course hits the
member satisfaction target, usually another five percent on the year.
[01:31] SAM: Anything before you're actually on the property?
[01:35] PRIYA: Mobilization fee, one month up front. Then we bill from the day the
contract starts. Onboarding takes about ninety days before we're really running it,
but the clock starts at signing.
[01:52] SAM: And what's a club actually worth to you in year one, after the
superintendent and the crew?
[02:01] PRIYA: Depends on the property. I'd have to ask Tom for a real number. Some of
them are thin the first year.
[02:12] SAM: Fair. Let's come back to that. What's the club you'd most want to sign?
[02:20] PRIYA: Private, eighteen to thirty-six holes, grounds budget over three hundred
thousand a year. Below three hundred it doesn't work, we can't put a superintendent
on it.
[02:38] SAM: And the one you'd walk away from?
[02:42] PRIYA: Municipal. They bid everything, lowest price wins, and we're never the
lowest price. Also anywhere the board has to vote. Member-owned clubs take nine months
to a year, the board has to vote on everything. Corporate-owned, one person decides.
We've done a corporate one in six weeks.
[03:10] SAM: Geography?
[03:12] PRIYA: Oregon and Washington, obviously. Idaho, sure. Montana if the owner pays
travel. Not California. The water rules are a different business down there.
[03:30] SAM: Clubs only? Or would you do the same deal for a resort with a course?
[03:38] PRIYA: Resorts, yes, actually that's interesting. We haven't gone after those.
Same floor though, three hundred.
[03:50] SAM: How many new clubs could you take on in a year without breaking?
[03:55] PRIYA: Four, tops. After four we'd need a second regional super, and that's a
hire we'd only make with contracts in hand.
[04:10] PRIYA: Question for you. How do you get to the person who decides without
going through the GM? The GM is the person we'd be replacing, in their head.
[04:22] SAM: We go to the owner or the board president, never the GM. I'll put how in
writing.
[04:31] PRIYA: Okay. On the money side. I'd want a lower monthly and more on the win,
and a short first term, four months, until we've got a couple signed.
[04:48] SAM: I can do fifteen hundred a month on a four-month first term, and the fee
per signed contract goes up to cover it.
[04:58] PRIYA: That works for me. Send it over. Tom and I are together Wednesday.
[05:08] SAM: Thursday to go through it?
[05:11] PRIYA: Thursday afternoon works, after two.
[05:14] SAM: Thursday after two. I'll send the invite.
```

Invocation: `/discovery-sheet calls/fairway-fern-2026-03-10.txt "Priya Lindqvist"`

---

## 2. Output 1: CALL NOTES

File: `calls/CALL-NOTES-priya-2026-03-10.md`

```
# CALL NOTES: Priya Lindqvist, Fairway and Fern, 10 March 2026, 10:00 PT (24 minutes)

Source: calls/fairway-fern-2026-03-10.txt. Grade: VERBATIM. Shown: nothing. Who talked:
Priya volunteered most of it; Sam led with short questions. Flags: none.

## OUTCOME
- Priya has read the one-pager: "Nothing on there scared me."
- Her ask: lower monthly, more on the win, a four-month first term "until we've got a
  couple signed."
- Sam offered $1,500 a month on a four-month first term, with the fee per signed
  contract raised to cover it. Priya: "That works for me. Send it over."
- Tom has seen the one-pager and is "cautious." Priya and Tom are together Wednesday.
- Next call: Thursday 12 March, after 2:00 pm PT. Sam sends the invite: "I'll send the
  invite."
- Owed by Sam: how we reach the decision-maker without going through the GM, in writing.

## THE ONE NUMBER
What a typical club makes them in year one after the superintendent and crew.
Not captured. "Depends on the property. I'd have to ask Tom for a real number. Some of
them are thin the first year." Tom holds it. Line one of the SKELETON.

## THE NUMBERS (verbatim where it matters)
- Clubs today: **eleven.** "We've got eleven clubs now."
- Signing this quarter: **two,** "hopefully."
- Monthly fee per club: **$22,000 to $28,000.** "Somewhere between twenty-two and
  twenty-eight thousand a month depending on acreage and how many holes."
- Bonus: **usually another 5% on the year.** "there's a bonus if the course hits the
  member satisfaction target, usually another five percent on the year."
- Up front: **one month,** "Mobilization fee, one month up front."
- Billing starts: **the day the contract starts.** "the clock starts at signing."
- Onboarding: **about ninety days** "before we're really running it."
- Grounds-budget floor: **$300,000 a year.** "Below three hundred it doesn't work, we
  can't put a superintendent on it."
- Course size: **eighteen to thirty-six holes.** "Private, eighteen to thirty-six holes,
  grounds budget over three hundred thousand a year."
- Capacity: **four new clubs a year, tops.** "After four we'd need a second regional
  super, and that's a hire we'd only make with contracts in hand."
- Sales cycle, member-owned: **nine months to a year.** "the board has to vote on
  everything."
- Sales cycle, corporate-owned: **six weeks** in one case. "We've done a corporate one in
  six weeks."
- Her first-term ask: **four months.** "a short first term, four months, until we've got
  a couple signed."
- Arithmetic: one club is $264,000 to $336,000 gross a year on the monthly alone.
- Arithmetic: the bonus, when hit, adds roughly $13,000 to $17,000 on a year.

## ICP, IN THEIR WORDS
- **Size:** "eighteen to thirty-six holes, grounds budget over three hundred thousand a
  year." Floor is firm: "Below three hundred it doesn't work."
- **Type:** private clubs. Resorts with a course: "yes, actually that's interesting. We
  haven't gone after those. Same floor though, three hundred."
- **Buyer type:** corporate-owned preferred, "one person decides." Member-owned is slow:
  "nine months to a year, the board has to vote on everything."
- **Not the ICP:** municipal courses. "They bid everything, lowest price wins, and we're
  never the lowest price."
- **Scope:** the full grounds operation with their own superintendent on site (the floor
  exists because "we can't put a superintendent on it" below it).
- **Geography:** "Oregon and Washington, obviously. Idaho, sure. Montana if the owner
  pays travel. Not California. The water rules are a different business down there."
- **Adjacent:** resorts, unprompted "interesting." Not yet chased.

## DEAL ECONOMICS
- Paid a flat monthly per club, $22,000 to $28,000, plus a bonus of about 5% on the year
  when the satisfaction target is hit.
- One month's fee up front as mobilization; billing runs from the contract start date,
  about ninety days before they are fully operating.
- Capacity is four new clubs a year; a fifth needs a second regional superintendent, hired
  only with contracts in hand.
- Sales cycle: six weeks to a year depending on who decides on the club side.
- Every club to date came through a personal connection: "That well is drying up."
- Arithmetic: one signed club is worth $264,000 to $336,000 gross in year one before the
  bonus, and they are paid from day one plus a month ahead.
- Read: cash on a new club starts before the work does, so a fee at signing is not a
  cash problem for them on timing. Margin in year one is the unknown ("Some of them are
  thin the first year.") and sets what a signing is worth to them, which sets our fee.

## WHO THEY ARE (from the call only)
- Two founders. Priya, CEO, runs the operation. Tom "runs the money" and sees everything
  before it is signed.
- Eleven clubs under contract, two more expected this quarter, all from their own network.
- They put a superintendent on every property; that is the unit of capacity.

## WHAT THE SELLER SAID THAT NOW BINDS US
- "I can do fifteen hundred a month on a four-month first term, and the fee per signed
  contract goes up to cover it."
- "We go to the owner or the board president, never the GM."
- "I'll put how in writing." (Owed before Thursday.)
- "I'll send the invite."
- Did not: say by how much the fee per signed contract goes up; commit to a start date;
  mention a guarantee; say what counts as a booked meeting.

## WHAT THEY ASKED US
- "How do you get to the person who decides without going through the GM?" Answered:
  "We go to the owner or the board president, never the GM." Owed: the method in
  writing.

## OPEN QUESTIONS
- What does a typical club make you in year one, after the superintendent and the crew?
- If a club already has an outside grounds company on the property, prospect or dead end?
- Resorts with a course: on the list, or not this year?
- Would residential communities or universities with a course count?
- Does the mobilization month sit on top of the monthly, or is it the first month paid
  early?
- How many of the eleven hit the bonus target?
- Who takes the first calls, Priya or Tom?

## CONFLICTS
None found.

## NEXT CALL: WHAT HAS TO HAPPEN
1. Restate the offer exactly as made: $1,500 a month on a four-month first term, with
   the fee per signed contract raised to cover it.
2. Deliver the owed page: how we reach owners and board presidents without the GM.
3. Get the year-one margin on a typical club. Tom holds it; ask for Tom on the call.
4. Settle the ICP edges: existing outside company, resorts, communities, universities.
5. Set the fee per signed contract from her number, or put it on one page by Monday.
6. Book the step after Thursday with Tom in the room.
```

---

## 3. Output 2: SKELETON

File: `calls/SKELETON-priya-2026-03-12.md`

```
# PRIYA, THURSDAY AFTER 2:00 PM PT

Minute 12 without her year-one margin on a typical club: drop everything and ask it.
Tom holds the number.

## WALK OUT WITH
1. Year-one margin on a typical club, after the superintendent and the crew.
2. Her answer on clubs that already use an outside grounds company: prospect or dead end.
3. Her answer on resorts, communities and universities with a course: on the list or not.
4. Tom's yes, or the date Tom is in the room.

## BRIEFED
- Priya Lindqvist, CEO and co-founder. Runs the operation. Not the money person.
- Tom, co-founder, runs the money. No surname given on the call. Signs nothing she
  hasn't shown him. They met Wednesday.
- Fairway and Fern: eleven clubs today, two more signing this quarter, all from their
  own network.
- Footprint: Oregon and Washington. Idaho yes. Montana only if the owner pays travel.
  California no.
- The one-pager: monthly retainer plus a fee per signed contract. She has read it. Tom has
  seen it.
- GM: a club's general manager. In her words, "the person we'd be replacing, in their
  head."
- The GM page: the owed note on reaching owners and board presidents without the GM.
  Send before the call.

## ORDER
1. Hellos. Where did you and Tom land on Wednesday?
2. Verify. The list below, before anything else.
3. Discovery.
4. What questions do you have for me?
5. Terms, restated exactly as offered.
6. Book the next step with Tom on it.

## VERIFY (before the pitch)
- New maintenance contracts are the goal. Would you also take a consulting-only shape,
  where you advise and the club keeps its own crew, or is it the full contract or
  nothing?
- If a club already has an outside grounds company on the property, is that a prospect
  or a dead end?
- Oregon, Washington and Idaho, right? Montana only when the owner pays travel?
- Private clubs only, or the same deal on a different property? You said resorts with a
  course sounded interesting. Would a residential community with a course count? A
  university course?
  - Whatever she picks: then that's a second list, it goes on the next page.
- Is this your call, or does Tom need to be on it?

## DISCOVERY

**A. Who to hunt**
- Every club so far came through someone you knew. What happens when that runs dry?
- Which corporate club owners do you already know? Anyone mid-conversation now we must
  not touch?

**B. Economics. CANNOT LEAVE WITHOUT.**
- **What does a typical club make you in year one, after the superintendent and the
  crew?**
- Your best club and your typical club: what does each pay you in year one?
- The bonus, usually another five percent on the year: how many of the eleven hit it?
- The mobilization month: is that on top of the monthly, or the first month paid early?

**C. Cash**
- When a new club comes on, what does it cost you in the ninety days before you're
  running it?
- Does a fee at signing sit awkwardly against that, or does the timing work?

**D. What we book**
- Describe the first conversation you'd thank us for.
- Who has to be in the seat? The owner, the board president, someone else?
- What's an instant no?
- How many first calls a week can you take, and who takes them, you or Tom?

**E. If time**
- Whose name goes on the outreach, and whose calendar do the calls land on?
- A few real emails you've sent to club owners, so we can match your voice?

## TERMS
- Say it settled: fifteen hundred a month on a four-month first term, with the fee per
  signed contract raised to cover it. That was offered; it holds.
- The size of the fee per signed contract needs her year-one number. No number without
  her number. If she gives it, land it live. If not, it goes on one page by Monday.
- One trade card, timing not amount: the fee per signed contract paid over the first six
  months of the club contract.

## NEVER
- Quote the fee per signed contract before she gives the year-one number.
- Move the monthly below fifteen hundred; it was already offered.
- Say the GM is who she'd be replacing; that's her line, not ours.
- Promise a start date.
- Pitch consulting.
```

---

## 4. What the review pass catches

The three defects the checklist catches most often, shown against this example.

1. A THE NUMBERS bullet reading "Monthly fee **$22,000 to $28,000**, bonus **5%**." Two
   figures in one bullet. Split, each with its own quote, as above.
2. "Tom, cautious, on the money side" under ORDER before Tom is briefed. Tom goes in
   BRIEFED with his role and what he controls; ORDER can then name him freely.
3. A SHOW-style line reading "we haven't run this for golf clubs before, this is the
   first one." Cut under Rule 6. The answer, if asked, is what has been run and the
   numbers that can be defended, without "first."
