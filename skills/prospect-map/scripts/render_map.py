#!/usr/bin/env python3
"""Render a prospect map page from rows.json and map.config.json.

Every number on the page (market total, region chips, status chips, watch-list
count, owner-confidence split) is computed from the rows, so the page cannot
disagree with its own table. Rows with status "aside" are counted in the market
total and never listed: they are the entities that do not buy this deal shape today.

Usage:
  python render_map.py --rows rows.json --config map.config.json --out map.html
  python render_map.py --rows rows.json --config map.config.json --check
  python render_map.py --rows rows.json --config map.config.json --out map.html --fragment
      (--fragment omits doctype/html/head/body for tools that wrap the page themselves)

Placeholders allowed in any config string: {total} {table} {ready} {licensed} {verify}
{transition} {aside} {watch} {watchShown} {confHigh} {confMedium} {confLow} {confUnknown}
{ownerKnown}.

Exit code 1 when validation fails. Validation refuses: unknown statuses, table rows
missing evidence or evidenceDate (YYYY-MM-DD), triggers without sortDate, transition
rows without a trigger, em or en dashes and anything that looks like an email address
or phone number in a rendered field (contacts never go on the page; working fields
such as sources, parcelId, manager and ownerMailing are not checked), and config copy
still equal to references/example-config.json (pass --allow-example only to render
the shipped example). Standard library only.
"""
import argparse
import html
import json
import os
import re
import sys
from collections import Counter

STATUS_ORDER = ["ready", "licensed", "verify", "transition"]
ALL_STATUSES = STATUS_ORDER + ["aside"]
STATUS_LABEL = {"ready": "Ready", "licensed": "Licensed", "verify": "Verify", "transition": "In transition"}
STATUS_CLASS = {"ready": "y", "licensed": "c", "verify": "g", "transition": "t"}
CONFIDENCE = ["high", "medium", "low", "unknown"]
REQUIRED_TABLE = ["region", "city", "entity", "unit", "counterparty", "owner", "ownerConfidence", "ownerEvidence", "statusEvidence"]
DASH = re.compile("[\\u2013\\u2014]")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE = re.compile(r"(?<!\d)\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}(?!\d)")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
RENDERED_ROW_FIELDS = ["region", "city", "entity", "unit", "counterparty", "owner", "ownerConfidence", "ownerEvidence", "statusEvidence", "note"]
RENDERED_TRIGGER_FIELDS = ["what", "when", "source"]
COPY_FIELDS = ["title", "meta", "subtitle", "marketNote", "tableTitle", "tableNote", "watchNote"]

DEFAULTS = {
    "title": "Prospect map",
    "meta": "",
    "subtitle": "",
    "marketLabel": "entities counted",
    "marketNote": "",
    "regions": {},
    "regionOrder": [],
    "columns": {
        "region": "Region", "city": "City", "entity": "Entity", "unit": "Unit",
        "counterparty": "Who runs it today", "owner": "Owner of record", "status": "Status",
    },
    "tableTitle": "Where the paying relationship already exists",
    "tableNote": "",
    "watchTitle": "Deals coming loose",
    "watchNote": "",
    "watchCap": 40,
    "method": [],
    "caveat": "",
    "footer": [],
    "statusLabels": {},
}

CSS = """
  :root {
    --paper: #FAFAF8; --card: #FFFFFF; --ink: #1A1F26; --ink-2: #4A545F; --ink-3: #7C8794;
    --rule: #E0E3E0; --yes: #1F6B4A; --yes-bg: #E3F0E9; --no: #9C3A32; --no-bg: #F8E7E5;
    --cite: #8A5A12; --cite-bg: #ECEDEA; --accent: #1F4E6B;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --paper: #0F1216; --card: #171C22; --ink: #EDEFF2; --ink-2: #B0B9C3; --ink-3: #808B97;
      --rule: #2A323A; --yes: #63C79A; --yes-bg: #14291F; --no: #E38A82; --no-bg: #2B1917;
      --cite: #E0B060; --cite-bg: #23272C; --accent: #7FB8D8;
    }
  }
  :root[data-theme="dark"] {
    --paper: #0F1216; --card: #171C22; --ink: #EDEFF2; --ink-2: #B0B9C3; --ink-3: #808B97;
    --rule: #2A323A; --yes: #63C79A; --yes-bg: #14291F; --no: #E38A82; --no-bg: #2B1917;
    --cite: #E0B060; --cite-bg: #23272C; --accent: #7FB8D8;
  }
  * { box-sizing: border-box; }
  body { background: var(--paper); color: var(--ink); font-family: "Source Sans 3", ui-sans-serif, system-ui, sans-serif; font-size: 18px; line-height: 1.55; margin: 0; }
  .wrap { max-width: 1000px; margin: 0 auto; padding: 0 26px 80px; }
  h1, h2 { font-family: "Source Serif 4", Georgia, serif; margin: 0; line-height: 1.15; }
  header { padding: 52px 0 26px; border-bottom: 3px solid var(--ink); display: flex; flex-direction: column; gap: 12px; }
  header h1 { font-size: clamp(32px, 5.5vw, 46px); font-weight: 700; }
  header .sub { font-size: 18.5px; color: var(--ink-2); max-width: 62ch; }
  header .meta, .mono { font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--ink-3); }
  section { margin-top: 46px; }
  .band { display: flex; align-items: baseline; gap: 14px; flex-wrap: wrap; margin-bottom: 6px; }
  .band h2 { font-size: 25px; font-weight: 600; }
  .band .score { font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 13px; font-weight: 600; letter-spacing: 0.06em; padding: 4px 11px; border-radius: 3px; }
  .score.good { background: var(--yes-bg); color: var(--yes); }
  .score.mixed { background: var(--rule); color: var(--ink-2); }
  .band-note { color: var(--ink-2); font-size: 17px; max-width: 68ch; margin: 0 0 18px; }
  .chips { display: flex; flex-wrap: wrap; gap: 10px; margin: 14px 0 6px; }
  .chip { background: var(--card); border: 1px solid var(--rule); border-radius: 5px; padding: 12px 18px; display: flex; align-items: baseline; gap: 10px; }
  .chip .n { font-family: "Source Serif 4", Georgia, serif; font-size: 30px; font-weight: 700; line-height: 1; color: var(--accent); }
  .chip .l { font-size: 15px; color: var(--ink-2); }
  .chip .l small { display: block; font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--ink-3); margin-top: 3px; }
  .grid-head, .row { display: grid; gap: 10px; align-items: start; }
  .grid-head.h7, .row.r7 { grid-template-columns: 44px minmax(90px, 0.8fr) minmax(180px, 1.7fr) minmax(140px, 1.3fr) minmax(160px, 1.5fr) minmax(160px, 1.5fr) minmax(112px, 0.8fr); }
  .grid-head.h5, .row.r5 { grid-template-columns: 44px minmax(100px, 0.8fr) minmax(180px, 1.5fr) minmax(260px, 2.6fr) minmax(180px, 1.5fr); }
  .grid-head { padding: 0 16px 8px; font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 11px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: var(--ink-3); }
  .grid-head.h7 span:last-child { text-align: center; }
  .row { background: var(--card); border: 1px solid var(--rule); border-radius: 5px; padding: 15px 16px; margin-bottom: 9px; font-size: 15.5px; line-height: 1.4; }
  .row .st { font-family: "IBM Plex Mono", ui-monospace, monospace; font-weight: 600; font-size: 13px; letter-spacing: 0.06em; color: var(--ink-3); }
  .row .hn { font-weight: 600; color: var(--ink); }
  .row .dim { color: var(--ink-2); }
  .cell { text-align: center; font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 11.5px; font-weight: 600; letter-spacing: 0.06em; padding: 7px 4px; border-radius: 3px; text-transform: uppercase; align-self: center; }
  .cell.y { background: var(--yes-bg); color: var(--yes); }
  .cell.c { background: var(--cite-bg); color: var(--cite); }
  .cell.g { background: var(--rule); color: var(--ink-2); }
  .cell.t { background: var(--cite-bg); color: var(--cite); }
  .row.trans { border-left: 4px solid var(--cite); }
  .row .note { grid-column: 1 / -1; font-size: 14.5px; color: var(--ink-2); border-top: 1px dashed var(--rule); padding-top: 8px; margin-top: 2px; }
  .row .note b { font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--ink-3); font-weight: 600; margin-right: 6px; }
  .more { color: var(--ink-3); font-size: 14.5px; margin: 4px 0 0; }
  .pull { background: var(--card); border: 1px solid var(--rule); border-left: 5px solid var(--accent); border-radius: 5px; padding: 24px 28px; margin-top: 46px; display: flex; flex-direction: column; gap: 12px; }
  .pull h2 { font-size: 22px; font-weight: 600; }
  .pull p { margin: 0; max-width: 68ch; color: var(--ink-2); font-size: 17.5px; }
  .pull p.lead { color: var(--ink); font-size: 19px; }
  .pull p.caveat { border-top: 1px solid var(--rule); padding-top: 12px; color: var(--ink); }
  footer { margin-top: 52px; padding-top: 20px; border-top: 1px solid var(--rule); font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 12px; color: var(--ink-3); display: flex; flex-wrap: wrap; gap: 6px 22px; }
  @media (max-width: 900px) {
    .grid-head { display: none; }
    .row.r7, .row.r5 { grid-template-columns: 1fr 1fr; }
    .row .hn, .row .note { grid-column: 1 / -1; }
    .row .m::before { content: attr(data-l); display: block; font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 10.5px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--ink-3); margin-bottom: 2px; }
    .row .cell { grid-column: 1 / -1; }
  }
"""

FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&family=Source+Sans+3:wght@400;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap">'


def esc(s):
    return html.escape(str(s if s is not None else ""), quote=True)


def walk_strings(obj, path, out):
    if isinstance(obj, dict):
        for k, v in obj.items():
            walk_strings(v, f"{path}.{k}", out)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            walk_strings(v, f"{path}[{i}]", out)
    elif isinstance(obj, str):
        out.append((path, obj))


def rendered_strings(rows, config):
    """Strings that reach the page: the rendered row fields, the trigger text and every config string."""
    out = []
    for i, r in enumerate(rows):
        if not isinstance(r, dict):
            continue
        for f in RENDERED_ROW_FIELDS:
            if isinstance(r.get(f), str):
                out.append((f"rows[{i}].{f}", r[f]))
        t = r.get("trigger")
        if isinstance(t, dict):
            for f in RENDERED_TRIGGER_FIELDS:
                if isinstance(t.get(f), str):
                    out.append((f"rows[{i}].trigger.{f}", t[f]))
    walk_strings(config, "config", out)
    return out


def copy_strings(config):
    """Config strings that describe one market and must be rewritten from the shipped example."""
    out = []
    for f in COPY_FIELDS:
        if isinstance(config.get(f), str):
            out.append((f"config.{f}", config[f]))
    for k, v in (config.get("regions") or {}).items():
        if isinstance(v, str):
            out.append((f"config.regions.{k}", v))
    for i, m in enumerate(config.get("method") or []):
        if isinstance(m, dict) and isinstance(m.get("text"), str):
            out.append((f"config.method[{i}].text", m["text"]))
    for i, s in enumerate(config.get("footer") or []):
        if isinstance(s, str):
            out.append((f"config.footer[{i}]", s))
    return [(p, s.strip()) for p, s in out if s.strip()]


def load_example_config():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "example-config.json")
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def validate(rows, config, example=None):
    problems = []
    if not isinstance(rows, list):
        return ["rows.json must be a JSON array of row objects"]
    seen = set()
    for i, r in enumerate(rows):
        where = f"rows[{i}] ({r.get('entity', '?') if isinstance(r, dict) else '?'})"
        if not isinstance(r, dict):
            problems.append(f"{where}: not an object")
            continue
        status = r.get("status")
        if status not in ALL_STATUSES:
            problems.append(f"{where}: status must be one of {ALL_STATUSES}, got {status!r}")
        for f in ("region", "entity"):
            if not str(r.get(f) or "").strip():
                problems.append(f"{where}: missing {f}")
        if status in STATUS_ORDER:
            for f in REQUIRED_TABLE:
                if not str(r.get(f) or "").strip():
                    problems.append(f"{where}: table rows need {f} (unknowns must say unknown, not stay blank)")
            if r.get("ownerConfidence") not in CONFIDENCE:
                problems.append(f"{where}: ownerConfidence must be one of {CONFIDENCE}")
            if not str(r.get("evidenceDate") or "").strip():
                problems.append(f"{where}: table rows need evidenceDate (YYYY-MM-DD, the newest source date behind the status)")
        elif r.get("ownerConfidence") not in (None, "") and r.get("ownerConfidence") not in CONFIDENCE:
            problems.append(f"{where}: ownerConfidence must be one of {CONFIDENCE}")
        ed = r.get("evidenceDate")
        if ed and not DATE.fullmatch(str(ed)):
            problems.append(f"{where}: evidenceDate must be YYYY-MM-DD, got {ed!r}")
        t = r.get("trigger")
        if status == "transition" and not t:
            problems.append(f"{where}: transition rows need a trigger (the sale or assignment that puts the owner in motion)")
        if t is not None:
            if not isinstance(t, dict):
                problems.append(f"{where}: trigger must be an object")
            else:
                for f in ("what", "when", "source"):
                    if not str(t.get(f) or "").strip():
                        problems.append(f"{where}: trigger needs {f}")
                sd = t.get("sortDate")
                if not str(sd or "").strip():
                    problems.append(f"{where}: trigger needs sortDate (YYYY, YYYY-MM or YYYY-MM-DD) so the watch list sorts")
                elif not re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", str(sd)):
                    problems.append(f"{where}: trigger.sortDate must be YYYY, YYYY-MM or YYYY-MM-DD")
        key = (str(r.get("region")), str(r.get("city")), str(r.get("entity")).lower())
        if key in seen:
            problems.append(f"{where}: duplicate entity in the same region and city")
        seen.add(key)
    for path, s in rendered_strings(rows, config):
        if DASH.search(s):
            problems.append(f"{path}: contains an em or en dash; use a comma, colon or period")
        if EMAIL.search(s):
            problems.append(f"{path}: looks like an email address; contacts never go on the page")
        if PHONE.search(s):
            problems.append(f"{path}: looks like a phone number; contacts never go on the page")
    if example is not None:
        shipped = {s for _, s in copy_strings(example)}
        for path, s in copy_strings(config):
            if s in shipped:
                problems.append(f"{path}: still the shipped example text; rewrite it for this market (--allow-example is only for rendering the example itself)")
    return problems


def compute_counts(rows, config):
    by_status = Counter(r.get("status") for r in rows)
    conf = Counter((r.get("ownerConfidence") or "unknown") for r in rows)
    watch = [r for r in rows if r.get("trigger")]
    cap = int(config.get("watchCap") or 40)
    c = {
        "total": len(rows),
        "table": sum(by_status[s] for s in STATUS_ORDER),
        "aside": by_status["aside"],
        "watch": len(watch),
        "watchShown": min(len(watch), cap),
        "confHigh": conf["high"], "confMedium": conf["medium"], "confLow": conf["low"], "confUnknown": conf["unknown"],
    }
    for s in STATUS_ORDER:
        c[s] = by_status[s]
    c["ownerKnown"] = c["total"] - c["confUnknown"]
    return c


def fill(s, counts):
    return re.sub(r"\{(\w+)\}", lambda m: str(counts[m.group(1)]) if m.group(1) in counts else m.group(0), s or "")


def region_order(rows, config):
    order = list(config.get("regionOrder") or [])
    for r in rows:
        if r.get("region") not in order:
            order.append(r.get("region"))
    return order


def render(rows, config, counts, fragment=False):
    cols = dict(DEFAULTS["columns"])
    cols.update(config.get("columns") or {})
    labels = dict(STATUS_LABEL)
    labels.update(config.get("statusLabels") or {})
    regions = region_order(rows, config)
    region_names = config.get("regions") or {}
    rindex = {r: i for i, r in enumerate(regions)}
    out = []
    w = out.append

    title = fill(config.get("title") or DEFAULTS["title"], counts)
    if fragment:
        w(f"<title>{esc(title)}</title>")
        w(FONTS)
        w(f"<style>{CSS}</style>")
    else:
        w("<!doctype html>")
        w('<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">')
        w(f"<title>{esc(title)}</title>")
        w(FONTS)
        w(f"<style>{CSS}</style></head><body>")

    w('<div class="wrap">')
    w("<header>")
    if config.get("meta"):
        w(f'  <div class="meta">{esc(fill(config["meta"], counts))}</div>')
    w(f"  <h1>{esc(title)}</h1>")
    if config.get("subtitle"):
        w(f'  <p class="sub">{esc(fill(config["subtitle"], counts))}</p>')
    w("</header>")

    # Band 1: the market, counted
    w("<section>")
    w(f'  <div class="band"><h2>The market, counted</h2><span class="score good">{counts["total"]} {esc(fill(config.get("marketLabel") or DEFAULTS["marketLabel"], counts))}</span></div>')
    w('  <div class="chips">')
    per_region = Counter(r.get("region") for r in rows)
    for reg in regions:
        name = region_names.get(reg)
        if name:
            w(f'    <div class="chip"><span class="n">{per_region[reg]}</span><span class="l">{esc(name)}<small>{esc(reg)}</small></span></div>')
        else:
            w(f'    <div class="chip"><span class="n">{per_region[reg]}</span><span class="l">{esc(reg)}</span></div>')
    w("  </div>")
    conf_line = (f"Confidence in the owner name: {counts['confHigh']} high, {counts['confMedium']} medium, "
                 f"{counts['confLow']} low, {counts['confUnknown']} unknown.")
    note = fill(config.get("marketNote") or "", counts)
    w(f'  <p class="band-note">{esc((note + " " if note else "") + conf_line)}</p>')
    w("</section>")

    # Band 2: the table
    table_rows = [r for r in rows if r.get("status") in STATUS_ORDER]
    table_rows.sort(key=lambda r: (STATUS_ORDER.index(r["status"]), rindex.get(r.get("region"), 999), str(r.get("city") or ""), str(r.get("entity") or "")))
    w("<section>")
    chips = "".join(
        f'<span class="score {"good" if s == "ready" else "mixed"}">{counts[s]} {esc(labels[s].lower())}</span>'
        for s in STATUS_ORDER if counts[s]
    )
    w(f'  <div class="band"><h2>{esc(fill(config.get("tableTitle") or DEFAULTS["tableTitle"], counts))}</h2>{chips}</div>')
    if config.get("tableNote"):
        w(f'  <p class="band-note">{esc(fill(config["tableNote"], counts))}</p>')
    w(f'  <div class="grid-head h7"><span>{esc(cols["region"])}</span><span>{esc(cols["city"])}</span><span>{esc(cols["entity"])}</span><span>{esc(cols["unit"])}</span><span>{esc(cols["counterparty"])}</span><span>{esc(cols["owner"])}</span><span>{esc(cols["status"])}</span></div>')
    for r in table_rows:
        s = r["status"]
        w(f'  <div class="row r7{" trans" if s == "transition" else ""}">')
        w(f'    <span class="st">{esc(r.get("region"))}</span>')
        w(f'    <span class="m dim" data-l="{esc(cols["city"])}">{esc(r.get("city"))}</span>')
        w(f'    <span class="hn">{esc(r.get("entity"))}</span>')
        w(f'    <span class="m" data-l="{esc(cols["unit"])}">{esc(r.get("unit"))}</span>')
        w(f'    <span class="m dim" data-l="{esc(cols["counterparty"])}">{esc(r.get("counterparty"))}</span>')
        w(f'    <span class="m dim" data-l="{esc(cols["owner"])}">{esc(r.get("owner"))}</span>')
        w(f'    <span class="cell {STATUS_CLASS[s]}">{esc(labels[s])}</span>')
        ev = f'{r.get("statusEvidence")} Owner from {r.get("ownerEvidence")} (confidence {r.get("ownerConfidence")}).'
        w(f'    <span class="note"><b>Evidence</b>{esc(ev)}</span>')
        if r.get("note"):
            w(f'    <span class="note"><b>Note</b>{esc(r["note"])}</span>')
        w("  </div>")
    w("</section>")

    # Band 3: the watch list
    watch = [r for r in rows if r.get("trigger")]
    watch.sort(key=lambda r: str(r["trigger"].get("sortDate") or ""), reverse=True)
    cap = int(config.get("watchCap") or 40)
    shown = watch[:cap]
    w("<section>")
    w(f'  <div class="band"><h2>{esc(fill(config.get("watchTitle") or DEFAULTS["watchTitle"], counts))}</h2><span class="score mixed">{len(shown)} shown</span></div>')
    if config.get("watchNote"):
        w(f'  <p class="band-note">{esc(fill(config["watchNote"], counts))}</p>')
    w(f'  <div class="grid-head h5"><span>{esc(cols["region"])}</span><span>{esc(cols["city"])}</span><span>{esc(cols["entity"])}</span><span>What moved</span><span>When / source</span></div>')
    for r in shown:
        t = r["trigger"]
        w('  <div class="row r5">')
        w(f'    <span class="st">{esc(r.get("region"))}</span>')
        w(f'    <span class="m dim" data-l="{esc(cols["city"])}">{esc(r.get("city"))}</span>')
        w(f'    <span class="hn">{esc(r.get("entity"))}</span>')
        w(f'    <span class="m" data-l="What moved">{esc(t.get("what"))}</span>')
        w(f'    <span class="m dim" data-l="When / source">{esc(t.get("when"))}; {esc(t.get("source"))}</span>')
        w("  </div>")
    if len(watch) > cap:
        w(f'  <p class="more">{len(watch) - cap} more recorded and available on request.</p>')
    w("</section>")

    # Method block
    if config.get("method") or config.get("caveat"):
        w('<div class="pull">')
        w("  <h2>How this was built</h2>")
        for i, m in enumerate(config.get("method") or []):
            lead = esc(fill(m.get("lead") or "", counts))
            text = esc(fill(m.get("text") or "", counts))
            cls = ' class="lead"' if i == 0 else ""
            w(f"  <p{cls}><strong>{lead}</strong> {text}</p>")
        if config.get("caveat"):
            w(f'  <p class="caveat">{esc(fill(config["caveat"], counts))}</p>')
        w("</div>")

    if config.get("footer"):
        w("<footer>")
        for f in config["footer"]:
            w(f"  <span>{esc(fill(f, counts))}</span>")
        w("</footer>")
    w("</div>")
    if not fragment:
        w("</body></html>")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rows", required=True, help="rows.json (array of row objects)")
    ap.add_argument("--config", required=True, help="map.config.json (page copy and labels)")
    ap.add_argument("--out", help="output HTML path")
    ap.add_argument("--check", action="store_true", help="validate and print counts, write nothing")
    ap.add_argument("--fragment", action="store_true", help="omit doctype/html/head/body")
    ap.add_argument("--allow-example", action="store_true",
                    help="skip the check that config copy differs from references/example-config.json (only for rendering the shipped example)")
    args = ap.parse_args()
    if not args.out and not args.check:
        ap.error("give --out or --check")

    with open(args.rows, encoding="utf-8") as f:
        rows = json.load(f)
    with open(args.config, encoding="utf-8") as f:
        config = json.load(f)

    example = None if args.allow_example else load_example_config()
    problems = validate(rows, config, example)
    if problems:
        print("VALIDATION FAILED")
        for p in problems:
            print(" -", p)
        sys.exit(1)

    counts = compute_counts(rows, config)
    by_region = Counter(r.get("region") for r in rows)
    print("COUNTS")
    print(f"  total {counts['total']} | table {counts['table']} (ready {counts['ready']}, licensed {counts['licensed']}, "
          f"verify {counts['verify']}, in transition {counts['transition']}) | aside {counts['aside']} | watch {counts['watch']}")
    print("  by region: " + ", ".join(f"{k} {v}" for k, v in by_region.items()))
    print(f"  owner confidence: high {counts['confHigh']}, medium {counts['confMedium']}, low {counts['confLow']}, unknown {counts['confUnknown']}")
    if args.check:
        print("OK (validation passed, nothing written)")
        return
    page = render(rows, config, counts, fragment=args.fragment)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"written {args.out} ({len(page)} bytes)")


if __name__ == "__main__":
    main()
