# Worked example: Harbor Lights Hotel

Everything here is invented: the hotel, the town of Port Ashby, Marisol Vance, Dana Reyes, Fensworth Advisory, the OTA, the survey, the numbers. The `.example` domains are reserved and resolve to nothing. The town and the hotel are the same invented ones the `/prospect-map` example uses, so the pack shares one world. The shape is what matters.

Contents
1. Input: the research file
2. Input: the voice profile
3. Output: the working notes
4. Output: the page
5. Output: the email
6. Why it is built this way

## 1. Input: the research file

`research/harbor-lights-hotel.md`

```markdown
# Harbor Lights Hotel, Port Ashby: research
Compiled 2026-08-18 by Dana Reyes. Source beside each fact.

- Contact: Marisol Vance, General Manager. Source: harborlightshotel.example/about, fetched 2026-08-18.
- 64 rooms and suites. Source: harborlightshotel.example home page, fetched 2026-08-18.
- Independent, family owned. No year given on the site. Source: /about, fetched 2026-08-18.
- Open year round, peak season June to September. Source: /faq, fetched 2026-08-18.
- Booking on the hotel's own site takes 4 steps and requires opening an account before payment. Source: test booking walkthrough 2026-08-18, screenshots in research/harbor-lights/booking-flow/.
- Rate scan: Standard King, 2 adults, 30 nights from 2026-08-20 to 2026-09-18, the hotel's own site against its largest OTA listing ("the OTA" below). Own site higher on 19 nights, equal on 8, lower on 3. Sum of the gaps on the 19 higher nights: $304. Source: research/harbor-lights/rate-scan.csv, collected 2026-08-18 14:00 local.
- Reviews: 3 of the 40 most recent reviews on the OTA say the guest booked on the OTA after giving up on the hotel's site. Quotes saved. Source: OTA listing review page, fetched 2026-08-18.
- The phone number on the hotel's Google Business Profile differs from the number on the hotel site. Source: both pages fetched 2026-08-18.
- OTA commission for independent hotels in the region: 15 to 18%. Source: Coastal Lodging Association, 2025 distribution survey, p.12. Benchmark, not prospect-specific.
- A local news item (Port Ashby Gazette, 2024) says the hotel added 12 rooms. Not confirmed on the hotel's site. Do not use.
- Dana and Marisol spoke for about five minutes about direct bookings at the Coastal Lodging Association regional meeting on 2026-06-11. Source: Dana's calendar and notes from that day.
```

## 2. Input: the voice profile

The Dana Reyes profile in `voice-profile.md`, section 6. Sender line: Dana Reyes, Fensworth Advisory, dana@northwind-advisory.example (this fills the page footer). Sign-off "Best," then "Dana". Median 13 words, longest 24. Favours "walk-through", "the numbers", "on one page", "useful", "quick", "small fix". Closes with a question.

## 3. Output: the working notes

`one-pager/harbor-lights-hotel-notes.md`

```markdown
# Working notes: Harbor Lights Hotel
Built 2026-08-18 from research/harbor-lights-hotel.md and the Dana Reyes voice profile.

## Claim ledger
| # | Claim | Source | Checked | Status |
|---|---|---|---|---|
| 1 | Marisol Vance is General Manager | harborlightshotel.example/about | 2026-08-18 | VERIFIED |
| 2 | 64 rooms and suites | home page | 2026-08-18 | VERIFIED |
| 3 | Independent, family owned; no year on the site | /about | 2026-08-18 | VERIFIED, never state a year |
| 4 | Open year round, peak June to September | /faq | 2026-08-18 | VERIFIED |
| 5 | Own-site booking is 4 steps, account required before payment | walkthrough + screenshots | 2026-08-18 | VERIFIED |
| 6 | Own site above the OTA on 19 of 30 nights, equal 8, below 3 (Standard King, 2 adults, 20 Aug to 18 Sep) | rate-scan.csv | 2026-08-18 | VERIFIED |
| 7 | Sum of gaps on the 19 higher nights is $304 | rate-scan.csv | 2026-08-18 | VERIFIED |
| 8 | 3 of the 40 most recent OTA reviews say the guest gave up on the hotel's site and booked on the OTA | OTA review page | 2026-08-18 | VERIFIED |
| 9 | Google Business Profile phone differs from the site phone | both pages | 2026-08-18 | VERIFIED |
| 10 | OTA commission for independents in the region is 15 to 18% | Coastal Lodging Association 2025 survey p.12 | 2026-08-18 | BENCHMARK |
| 11 | Hotel added 12 rooms in 2024 | Port Ashby Gazette, unconfirmed | | UNSOURCED |
| 12 | Dana and Marisol spoke about direct bookings at the CLA regional meeting, 2026-06-11 | Dana's calendar and notes | 2026-08-18 | VERIFIED, sender-side |
| 13 | Bookings that start on the site and end on the OTA cost the hotel commission it would not otherwise pay | reading of rows 6, 8, 10 | | INFERRED |

## Arithmetic
- Average gap on the 19 higher nights: $304 / 19 = $16.00 (rows 6, 7). Used in step 1.
- Figure blocks: 64 rooms (row 2); 19 of 30 nights (row 6); 3 of 40 reviews (row 8).

## The finding, and the runners-up
- Chosen: the hotel's own site sends guests to the OTA. Two sourced legs: rate above the OTA on 19 of 30 nights (row 6) and a booking flow that asks for an account first (row 5), with guests saying so in reviews (row 8).
- Runner-up: the 4-step booking flow on its own (row 5). Real, but hard to size on its own; folded into step 2.
- Runner-up: the phone number mismatch (row 9). True and an easy fix, too small to carry a page; raise it on the call.

## Paragraph to ledger map
- Situation: rows 2, 4, 6. Finding p1: rows 5, 6, 8. Finding p2: row 13 as a would, row 10 as the benchmark line. Steps: rows 5, 6, 7. Ask: sender-side.

## Voice profile applied
- Greeting "Hi Marisol," and sign-off "Best," / "Dana" verbatim. Longest email sentence 15 words (profile longest 24). Favoured words used: on one page, walk-through, useful. Never-use list appended to the grep; zero hits.

## Checks run
- Dash grep on all three files: no output. Banned-phrase grep on the page body (stylesheet stripped) and the email: no output. Hand-review grep: no output.
- Page prose: 308 words (whole page with title, figure labels and footer: 435). Email file: 62 words, body 53.
- Headless Chrome print with --no-pdf-header-footer: 1 page at Letter, 1 page at A4.

## Not on the page
- Row 9 (phone mismatch): for the call.
- Row 11 (12 rooms added in 2024): single secondary source, unconfirmed. Ask Marisol if it comes up.
- Row 13: appears only as "would" in finding p2 and in step 3's re-run.
```

## 4. Output: the page

`one-pager/harbor-lights-hotel-page.html`, body section only. The head and stylesheet are the template's, unchanged except `<title>`, which carries the same text as the `<h1>` below.

```html
<div class="wrap">
<h1>Harbor Lights Hotel: direct bookings over the next 30 nights</h1>
<div class="sub">Prepared for Marisol Vance, General Manager · 18 August 2026</div>

<div class="card">
<h2>Where Harbor Lights stands</h2>
<div class="figs">
<div class="fig"><span class="n">64</span><span class="l">rooms and suites, per the hotel's own site</span></div>
<div class="fig"><span class="n">19 of 30</span><span class="l">nights where the hotel's own site is priced above the OTA (Standard King, 2 adults, 20 Aug to 18 Sep)</span></div>
<div class="fig"><span class="n">3 of 40</span><span class="l">most recent OTA reviews where the guest says they gave up on the hotel's site and booked on the OTA</span></div>
</div>
<p>Harbor Lights takes bookings on its own site and is listed on the OTA. Peak season runs June to September, so the nights in the scan fall inside the busiest weeks of the year. The scan priced the same room for the same two adults on both channels, night by night, on 18 August.</p>
</div>

<div class="card">
<h2>One finding</h2>
<p>On most of the next 30 nights, a guest who prices a Standard King on harborlightshotel.example sees a higher rate than the same room on the OTA. A guest who stays on the site then has to open an account before paying. Recent OTA reviews include guests who say they gave up on the hotel's site and booked on the OTA instead.</p>
<p>A booking that starts on the hotel's site and ends on the OTA carries the OTA's commission. Matching the rate and shortening the booking flow would remove both reasons to leave.</p>
<p class="bench">Industry surveys put OTA commission for independent hotels in the region at 15 to 18% (Coastal Lodging Association, 2025 distribution survey).</p>
</div>

<div class="card">
<h2>What it would take</h2>
<ol class="steps">
<li>Set the own-site rate at or below the OTA on every night in the scan. The average gap on the 19 higher nights is $16, so the change is small.</li>
<li>Take account creation out of the booking flow on the hotel's site, so a guest can pay without opening an account.</li>
<li>Re-run the same scan two weeks after the change and compare, night by night. If the rate rule is wrong, it goes back in a day.</li>
</ol>
<p>About an hour from the hotel's side for the rate rule and the booking setting. I run both scans. It's a small fix, and worth the twenty minutes to walk through.</p>
</div>

<div class="card">
<h2>One ask</h2>
<div class="ask">Would a 20 minute walk-through of the scan, night by night, be useful this week or next? I'll bring the CSV and the screenshots, and they're yours to keep whatever you decide.</div>
</div>

<div class="foot">Dana Reyes, Fensworth Advisory · dana@northwind-advisory.example<br>Every figure on this page comes from Harbor Lights' own site, its OTA listing, and a rate scan run on 18 August 2026.<br>Sources: harborlightshotel.example, the OTA listing and its reviews, rate-scan.csv, Coastal Lodging Association 2025 distribution survey.</div>
</div>
```

## 5. Output: the email

`one-pager/harbor-lights-hotel-email.txt`

```text
Subject: Harbor Lights rate scan

Hi Marisol,

We spoke about direct bookings at the Coastal Lodging meeting in June. I ran a rate check on Harbor Lights and put it on one page, attached.

On 19 of the next 30 nights your own site is priced above the OTA.

Would a 20 minute walk-through be useful this week or next?

Best,
Dana
```

## 6. Why it is built this way

- Line 1 of the email carries the only rapport allowed: a sourced meeting (row 12), stated as the fact it is. Nothing about how nice the hotel looks.
- The email explains nothing about Dana or Fensworth. The page does that in one footer line, filled from the profile's Sender line.
- Line 2 of the email is one sentence and carries the page's one figure. The reviews point stays on the page; a second sentence in that line would bury the number.
- Three figure blocks, chosen from the ledger. The $16 average gap did not get a block; it defines step 1, and a step is its own line, so it sits there.
- The reviews stat is accurate to its source: guests gave up on the site. It is not presented as guests switching on price, which the research does not show.
- Row 13 is a reading of the facts, so it appears as "would" in the finding and as the re-run in step 3, never as a statement.
- The benchmark sits in one sentence of its own with its source name, outside the figure blocks.
- Step 3 names the reversal path. That is a risk in the prospect's decision, which is welcome; it is not the sender narrating her own rework, which is banned.
- The effort line undersells and the ask is a question, both taken from the profile's habits.
- Row 11 was a real-looking fact with one secondary source. It stayed off the page, and the page says nothing about it having been left off.
