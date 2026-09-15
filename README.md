# leadgen-skills

Three Claude Code skills that do the first steps of B2B lead generation the way a research-first outreach shop does it. Map a whole market from public records. Turn a sales call into notes you can prove. Send one page per prospect built from their own numbers.

Free, MIT licensed, built by [Aaxelera](https://aaxelera.com).

## The three skills

| Skill | In | Out |
|---|---|---|
| `prospect-map` | A niche and a geography | `market.csv` (the count), `rows.json` (owner, status, evidence per entity), `map.html` (the page with a dated watch list) |
| `discovery-sheet` | A call transcript or your notes | `CALL-NOTES-<prospect>-<date>.md` (facts, quotes, every number on its own line, the ICP in their words) and `SKELETON-<prospect>-<next>.md` (what you hold on the next call) |
| `one-pager` | A research file with sourced facts, optionally your voice profile | `<prospect>-page.html` (print-ready), `<prospect>-email.txt` (three lines plus your sign-off), `<prospect>-notes.md` (a source per claim) |

They chain. `rows.json` from the map is a valid research file for `one-pager`. So is the `CALL-NOTES` file from `discovery-sheet`.

## Who it is for

Founders and small B2B teams who run their own outreach with Claude Code and want the research done properly before anyone gets an email. If you sell to a market you can count (hotels, clinics, buildings, licensed operators of any kind), the map skill is the one to start with. If you already have calls booked, start with the discovery sheet.

## Install

Inside Claude Code:

```
/plugin marketplace add montgomery-pixel/leadgen-skills
/plugin install leadgen-skills@aaxelera-leadgen-skills
```

Then `/prospect-map`, `/discovery-sheet` and `/one-pager` are available in any project.

## Quick start

### prospect-map, 30 seconds to launch

```
/prospect-map "restaurant operator for full-service hotels" "Colorado"
```

The first argument is what you sell and to whom. The second is where to count. The skill writes its working folder at `prospect-map/<niche>-<geography>/`, pulls the public licence and parcel files first, runs verification agents only on the rows that need them, and renders `map.html`. Expect the full run to take a while on a large market; the skill reports the count, the table split and the watch-list size when it finishes, and queues anything that needs a human in `manual-queue.md`.

### discovery-sheet, 30 seconds to launch

```
/discovery-sheet ./calls/2026-09-09-harbor-lights.txt "Priya Lindqvist"
```

Point it at a transcript (`.txt`, `.md`, `.vtt`, `.srt`, or a recorder's `.json`) or at your own notes. The prospect name is optional; quote it if it has spaces. Both files land beside the input. Nothing in them comes from outside the file: no web search, no invented mood, no rapport that was not said in words.

### one-pager, 30 seconds to launch

```
/one-pager ./research/harbor-lights-hotel.md ./voice/my-voice-profile.md
```

The research file needs at least three facts with sources (a URL, a document, a filing, or "call with <name>, <date>"). The voice profile is optional; the skill can build one from 5 to 10 of your own unassisted messages. Output goes to `one-pager/` beside the research file. The page is the personalisation; the email stays at three lines.

## Requirements

- Claude Code with plugin support.
- Built-in tools only: Read, Write, Bash, WebSearch, WebFetch and Agent. No API keys, no paid service.
- Python 3.8 or newer on PATH, for the three helper scripts in `prospect-map` (standard library only, nothing to install). The other two skills need no Python.

### Optional upgrades, never required

- Firecrawl, Bright Data, Apify or Scrapling: JavaScript-rendered portals and paginated directories during the map's enumeration step.
- A bulk parcel-data vendor or a commercial real-estate database, if you already pay for one: replaces county-by-county owner discovery.
- A speaker-labelled export from your meeting recorder: better attribution in the discovery sheet than auto-captions.
- pandoc: reads `.docx` and `.pdf` transcripts without a manual text export.
- Chrome or Edge: prints the one-pager to PDF from the command line.

## Writing rules baked in

Every file these skills produce is checked against the same rules before it is handed over:

- No em dashes or en dashes anywhere.
- No confession copy. Nothing you send narrates your own rework, misses or doubt. The reader sees the finished state and the method.
- Facts only. Every prospect-specific claim traces to a record, a document or a quote from the call. Nothing about a prospect is invented, rapport included.
- Numbers on their own line, one per line.
- Anything meant to be said aloud is written the way a person would say it.

## Layout

```
.claude-plugin/     plugin.json, marketplace.json
skills/
  prospect-map/     SKILL.md, references/, scripts/ (address_join.py, seed_rows.py, render_map.py)
  discovery-sheet/  SKILL.md, references/
  one-pager/        SKILL.md, references/
```

Every skill ships a fully fictional worked example in `references/` (Harbor Lights Hotel, Fensworth Clubs, Dana Reyes at Fensworth Advisory). None of it is a real client.

## Licence

MIT. See `LICENSE`.

Want us to run this for you? aaxelera.com
