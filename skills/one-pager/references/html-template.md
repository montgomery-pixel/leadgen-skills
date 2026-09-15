# Page template

Copy the block in the last section into `<slug>-page.html`, replace every `{{PLACEHOLDER}}`, and delete any `.fig` div, `<li>`, or optional paragraph you do not use. Keep the section order and the footer. Do not add sections.

Contents
1. Placeholders
2. Print rules
3. Template

## 1. Placeholders

| Placeholder | Fill with |
|---|---|
| `{{PAGE_TITLE}}` | Prospect organisation, colon, what the page is about ("Harbor Lights Hotel: direct bookings over the next 30 nights") |
| `{{PROSPECT_PERSON}}` | Full name of the reader |
| `{{PROSPECT_ROLE}}` | Their role as their own site or the call gives it. If neither gives one, use the organisation name; never guess a title |
| `{{DATE}}` | Written out: "18 August 2026" |
| `{{PROSPECT_ORG_SHORT}}` | Short form used in headings ("Harbor Lights") |
| `{{FIG_1_NUMBER}}` to `{{FIG_3_NUMBER}}` | The figure as the prospect reads it: "64", "19 of 30", "$16" |
| `{{FIG_1_LABEL}}` to `{{FIG_3_LABEL}}` | What the figure is, with the unit, the scope and the source name in plain words |
| `{{SITUATION}}` | The paragraph under the figures, 90 words at most |
| `{{FINDING_P1}}`, `{{FINDING_P2}}` | The one finding, 120 words across both |
| `{{BENCHMARK_LINE}}` | Optional. One sentence with the industry figure and its source name. Delete the paragraph if unused |
| `{{STEP_1}}` to `{{STEP_3}}` | Concrete steps, 25 words each, in order |
| `{{EFFORT_LINE}}` | Time from their side and from the sender's side, 30 words |
| `{{ASK}}` | One question with a time unit, 40 words |
| `{{SENDER_NAME}}`, `{{SENDER_ORG}}`, `{{SENDER_CONTACT}}` | Footer line one, from the voice profile's Sender line or the user's answer (SKILL.md, Inputs). Contact is one email address or one phone number, nothing else |
| `{{STANDARD_LINE}}` | One sentence stating where every figure comes from and the date it was checked |
| `{{SOURCES_LINE}}` | Source names, comma separated, no URLs |

## 2. Print rules

- Print from any browser. The stylesheet switches to a compact single-sheet layout, drops the shadows, and keeps each card whole.
- `@page` size is `auto`, so the printer's default (A4 or Letter) applies.
- If the preview spills onto a second sheet, cut words before touching CSS. The budgets in writing-rules.md fit with room to spare.
- Headless PDF: `<browser binary> --headless --no-pdf-header-footer --print-to-pdf=<slug>.pdf "<absolute path>/<slug>-page.html"`. Edge accepts the same flags. Without `--no-pdf-header-footer` the browser adds a date and URL line that can push a full page onto a second sheet.
- The binary is rarely on PATH, so give its full path:
  - Windows: `"C:\Program Files\Google\Chrome\Application\chrome.exe"` or `"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"`. In PowerShell put `&` before the quoted path; in cmd or Git Bash the quoted path runs as is.
  - macOS: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"` or `"/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"`.
  - Linux: `google-chrome`, `chromium` or `chromium-browser`, whichever `which` finds; Edge installs as `microsoft-edge`.
- The PDF lands in the current directory unless `--print-to-pdf` is given an absolute path. Open it and count the pages: one is the target.
- Colours live in the `:root` variables. Change them there to match the sender's brand; nothing else needs touching.
- Figure blocks are `display:flex` and wrap on narrow screens. Three blocks sit in one row at print width.

## 3. Template

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{{PAGE_TITLE}}</title>
<style>
:root{--ink:#20242B;--head:#1E2761;--muted:#6B7280;--bg:#f4f6fb;--card:#ffffff;--line:#e2e7f2;--tint:#eef3fd}
*{box-sizing:border-box}
body{font-family:Georgia,"Times New Roman",serif;background:var(--bg);color:var(--ink);margin:0;padding:40px}
.wrap{max-width:820px;margin:0 auto}
h1{color:var(--head);font-size:26px;line-height:1.2;margin:0 0 4px}
.sub{color:var(--muted);font-size:15px;margin:0 0 28px}
.card{background:var(--card);border-radius:12px;padding:22px 30px;margin-bottom:18px;box-shadow:0 2px 10px rgba(30,39,97,.08)}
.card h2{color:var(--head);font-size:13px;letter-spacing:2px;text-transform:uppercase;margin:0 0 10px}
.card p{font-size:15px;line-height:1.6;margin:0 0 10px}
.card p:last-child{margin-bottom:0}
.bench{color:var(--muted);font-size:14px}
.figs{display:flex;flex-wrap:wrap;gap:14px;margin:6px 0 14px}
.fig{flex:1 1 140px;background:var(--tint);border-radius:8px;padding:12px 16px}
.fig .n{display:block;font-size:30px;font-weight:bold;color:var(--head);line-height:1.1}
.fig .l{display:block;font-size:13px;color:var(--muted);line-height:1.35;margin-top:4px}
.steps{font-size:15px;line-height:1.6;margin:0 0 10px;padding-left:22px}
.steps li{margin-bottom:6px}
.ask{background:var(--tint);border-radius:8px;padding:14px 20px;font-size:16px;line-height:1.55}
.foot{color:var(--muted);font-size:12.5px;line-height:1.6;margin-top:22px}
@page{size:auto;margin:11mm 13mm}
@media print{
body{padding:0;background:#fff}
.wrap{max-width:100%}
h1{font-size:20px}
.sub{font-size:12px;margin-bottom:12px}
.card{padding:10px 16px;margin-bottom:8px;box-shadow:none;border:1px solid var(--line);break-inside:avoid}
.card h2{font-size:11px;margin-bottom:5px}
.card p,.steps{font-size:12.5px;line-height:1.42}
.bench{font-size:11.5px}
.figs{gap:8px;margin:4px 0 8px}
.fig{padding:8px 12px}
.fig .n{font-size:22px}
.fig .l{font-size:11px}
.ask{padding:9px 14px;font-size:13px}
.foot{font-size:10px;margin-top:10px}
}
</style>
</head>
<body>
<div class="wrap">
<h1>{{PAGE_TITLE}}</h1>
<div class="sub">Prepared for {{PROSPECT_PERSON}}, {{PROSPECT_ROLE}} · {{DATE}}</div>

<div class="card">
<h2>Where {{PROSPECT_ORG_SHORT}} stands</h2>
<div class="figs">
<div class="fig"><span class="n">{{FIG_1_NUMBER}}</span><span class="l">{{FIG_1_LABEL}}</span></div>
<div class="fig"><span class="n">{{FIG_2_NUMBER}}</span><span class="l">{{FIG_2_LABEL}}</span></div>
<div class="fig"><span class="n">{{FIG_3_NUMBER}}</span><span class="l">{{FIG_3_LABEL}}</span></div>
</div>
<p>{{SITUATION}}</p>
</div>

<div class="card">
<h2>One finding</h2>
<p>{{FINDING_P1}}</p>
<p>{{FINDING_P2}}</p>
<p class="bench">{{BENCHMARK_LINE}}</p>
</div>

<div class="card">
<h2>What it would take</h2>
<ol class="steps">
<li>{{STEP_1}}</li>
<li>{{STEP_2}}</li>
<li>{{STEP_3}}</li>
</ol>
<p>{{EFFORT_LINE}}</p>
</div>

<div class="card">
<h2>One ask</h2>
<div class="ask">{{ASK}}</div>
</div>

<div class="foot">{{SENDER_NAME}}, {{SENDER_ORG}} · {{SENDER_CONTACT}}<br>{{STANDARD_LINE}}<br>Sources: {{SOURCES_LINE}}</div>
</div>
</body>
</html>
```
