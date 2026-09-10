#!/usr/bin/env python3
"""Build docs/rules.html from docs/rules.json and prompts/exploration-log.txt.

Sole writer of docs/rules.html. Stdlib only. Deterministic: a second run leaves
the file byte-identical. Exits non-zero on any validation failure:

  * a rule with other than three prompt tags, or a tag that is not in the log
  * a proof entry whose prompt is not the verbatim log line for its tag, or
    whose image is missing under docs/
  * an archive with other than 24 entries, or an entry whose prompt is not
    byte-identical to its source path:line, or whose file is missing

Tag ids are ``<round>#<ordinal>``: ``r30#14`` is the 14th tagged line of round
30 in docs/prompts/exploration-log.txt. Ordinals never change because the log is
append-only.

Usage:  python3 scripts/build_rules.py            # build
        python3 scripts/build_rules.py --tag r30#14   # print one prompt
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "docs" / "prompts" / "exploration-log.txt"
RULES = ROOT / "docs" / "rules.json"
OUT = ROOT / "docs" / "rules.html"
TAG_RE = re.compile(r"^\[(r\d+)[^\]]*\]\s*(.*\S)\s*$")


def load_tags() -> dict[str, str]:
    """Map tag id -> prompt text (tag prefix stripped)."""
    tags: dict[str, str] = {}
    counts: dict[str, int] = {}
    for line in LOG.read_text(encoding="utf-8").splitlines():
        m = TAG_RE.match(line)
        if not m:
            continue
        rnd, text = m.group(1), m.group(2)
        counts[rnd] = counts.get(rnd, 0) + 1
        tags[f"{rnd}#{counts[rnd]}"] = text
    return tags


def fail(msg: str) -> None:
    print(f"build_rules: {msg}", file=sys.stderr)
    sys.exit(1)


def validate(data: dict, tags: dict[str, str]) -> None:
    rules = data.get("rules", [])
    if len(rules) < 6:
        fail(f"need at least six rules, found {len(rules)}")
    seen: set[str] = set()
    for r in rules:
        for key in ("id", "title", "statement", "prompt_tags", "flags", "proof"):
            if key not in r:
                fail(f"rule {r.get('id', '?')} missing field {key}")
        if r["id"] in seen:
            fail(f"duplicate rule id {r['id']}")
        seen.add(r["id"])
        if len(r["prompt_tags"]) != 3:
            fail(f"rule {r['id']} must have exactly three prompt tags")
        for t in r["prompt_tags"]:
            if t not in tags:
                fail(f"rule {r['id']} references unknown tag {t}")
        for p in r["proof"]:
            for key in ("image", "prompt_tag", "prompt"):
                if key not in p:
                    fail(f"rule {r['id']} proof entry missing {key}")
            if p["prompt_tag"] not in tags:
                fail(f"rule {r['id']} proof references unknown tag {p['prompt_tag']}")
            if p["prompt"] != tags[p["prompt_tag"]]:
                fail(f"rule {r['id']} proof prompt is not verbatim for {p['prompt_tag']}")
            if not (ROOT / "docs" / p["image"]).is_file():
                fail(f"rule {r['id']} proof image missing: {p['image']}")
    archive = data.get("archive", [])
    if len(archive) != 24:
        fail(f"archive must have exactly 24 entries, found {len(archive)}")
    for a in archive:
        for key in ("file", "prompt", "source"):
            if key not in a:
                fail(f"archive entry missing {key}: {a}")
        if not (ROOT / "docs" / "v10-v11-mj-pulls" / a["file"]).is_file():
            fail(f"archive file missing: {a['file']}")
        path, _, line_no = a["source"].rpartition(":")
        src = (ROOT / path).read_text(encoding="utf-8").splitlines()
        try:
            actual = src[int(line_no) - 1]
        except (ValueError, IndexError):
            fail(f"archive source out of range: {a['source']}")
        if actual != a["prompt"]:
            fail(f"archive prompt not byte-identical to {a['source']}")


CSS = """
:root{--bg:#0b0f14;--ink:#f3efe4;--mute:#9aa3ad;--line:#232b34;--blue:#1e3a8a;--blue-2:#3b82f6;--red:#d62828;--cream:#f3efe4}
*{box-sizing:border-box}html{color-scheme:dark}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 ui-serif,Georgia,"Times New Roman",serif}
a{color:var(--blue-2)}
.nav{display:flex;flex-wrap:wrap;gap:1rem;align-items:center;padding:.9rem 1rem;border-bottom:1px solid var(--line);font:13px ui-monospace,Menlo,monospace;letter-spacing:.04em;text-transform:uppercase}
.nav b{color:var(--ink)}.nav a{text-decoration:none;color:var(--mute)}.nav a[aria-current]{color:var(--ink)}
.banner{background:var(--blue);color:var(--cream);font:13px ui-monospace,Menlo,monospace;padding:.6rem 1rem}
main{max-width:52rem;margin:0 auto;padding:1.5rem 1rem 4rem}
h1{font-size:2rem;line-height:1.15;margin:1.5rem 0 .5rem}
.lede{color:var(--mute);margin:0 0 2rem}
.rule{border-top:1px solid var(--line);padding:1.75rem 0}
.rule h2{font-size:1.35rem;margin:0 0 .35rem}.rule h2 a{color:inherit;text-decoration:none}.rule h2 span{color:var(--red);font:14px ui-monospace,Menlo,monospace;margin-right:.6rem}
.statement{font-size:1.1rem;margin:.25rem 0 1rem}
.flags{font:13px ui-monospace,Menlo,monospace;color:var(--mute);margin:0 0 1rem}
.prompt{position:relative;margin:0 0 .75rem}
pre{margin:0;padding:.85rem 5.5rem .85rem .9rem;background:#111821;border:1px solid var(--line);border-radius:6px;white-space:pre-wrap;overflow-wrap:anywhere;font:13px/1.5 ui-monospace,Menlo,monospace;color:var(--ink)}
.copy{position:absolute;top:.5rem;right:.5rem;font:12px ui-monospace,Menlo,monospace;background:var(--cream);color:#0b0f14;border:0;border-radius:4px;padding:.3rem .55rem;cursor:pointer}
.tag{font:11px ui-monospace,Menlo,monospace;color:var(--mute);margin:.15rem 0 0}
.proof{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:.75rem;margin-top:1rem}
.proof figure{margin:0}.proof img{width:100%;height:auto;display:block;border:1px solid var(--line)}
.proof figcaption{font:11px ui-monospace,Menlo,monospace;color:var(--mute);margin-top:.3rem}
.archive-head{border-top:1px solid var(--line);padding-top:1.75rem;margin-top:1rem}
.archive-head p{color:var(--mute)}
.arch{display:grid;grid-template-columns:1fr;gap:1.25rem}
.arch figure{margin:0;display:grid;grid-template-columns:minmax(120px,180px) 1fr;gap:.75rem;align-items:start}
.arch img{width:100%;height:auto;display:block;border:1px solid var(--line)}
.arch pre{padding-right:.9rem}
.src{font:11px ui-monospace,Menlo,monospace;color:var(--mute);margin:.3rem 0 0}
footer{border-top:1px solid var(--line);margin-top:3rem;padding-top:1rem;font:12px ui-monospace,Menlo,monospace;color:var(--mute)}
@media (max-width:480px){h1{font-size:1.6rem}.arch figure{grid-template-columns:1fr}pre{padding-right:.9rem;padding-bottom:2.4rem}.copy{top:auto;bottom:.5rem}}
"""

JS = """
document.addEventListener('click',function(e){var b=e.target.closest('.copy');if(!b)return;
var t=b.parentNode.querySelector('pre').textContent;
navigator.clipboard.writeText(t).then(function(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy'},1200)});});
"""

NAV = (
    '<nav class="nav"><b>NOUS INSPIRED</b> '
    '<a href="index.html">Overview</a> '
    '<a href="rules.html" aria-current="page">Rulebook</a> '
    '<a href="method.html">Method</a> '
    '<a href="kit/README.md">Kit</a> '
    '<a href="https://github.com/thedavidmurray/nous-inspired-design-system">GitHub</a></nav>'
)
BANNER = (
    '<div class="banner">Unofficial. A fan-made design system inspired by Nous Research, '
    'built by Edgeless Lab. Not affiliated with or endorsed by Nous Research.</div>'
)


def prompt_block(text: str, tag: str) -> str:
    return (
        '<div class="prompt"><pre>' + html.escape(text) + '</pre>'
        '<button class="copy" type="button">Copy</button>'
        '<p class="tag">' + html.escape(tag) + '</p></div>'
    )


def render(data: dict, tags: dict[str, str]) -> str:
    out = [
        "<!doctype html>", '<html lang="en">', "<head>", '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>Rulebook, Nous Inspired Design System</title>",
        '<meta name="description" content="Numbered rules for the Nous inspired aesthetic, each with three copyable Midjourney prompts and proof images as they are made.">',
        "<style>" + CSS.strip() + "</style>", "</head>", "<body>", NAV, BANNER, "<main>",
        "<h1>" + html.escape(data["title"]) + "</h1>",
        '<p class="lede">' + html.escape(data["lede"]) + "</p>",
    ]
    for r in data["rules"]:
        out.append('<section class="rule" id="' + html.escape(r["id"]) + '">')
        out.append('<h2><a href="#' + html.escape(r["id"]) + '"><span>' + html.escape(r["id"]) + "</span>"
                   + html.escape(r["title"]) + "</a></h2>")
        out.append('<p class="statement">' + html.escape(r["statement"]) + "</p>")
        if r["flags"]:
            out.append('<p class="flags">flags: ' + html.escape(r["flags"]) + "</p>")
        for t in r["prompt_tags"]:
            out.append(prompt_block(tags[t], t))
        if r["proof"]:
            out.append('<div class="proof">')
            for p in r["proof"]:
                out.append('<figure><img src="' + html.escape(p["image"]) + '" alt="" loading="lazy">'
                           '<figcaption>' + html.escape(p["prompt_tag"]) + "</figcaption></figure>")
            out.append("</div>")
        out.append("</section>")
    out.append('<section class="archive-head" id="archive">')
    out.append("<h2>Archive: v10/v11-era output, not the validated recipe</h2>")
    out.append("<p>" + html.escape(data["archive_note"]) + "</p>")
    out.append("</section>")
    out.append('<div class="arch">')
    for a in data["archive"]:
        out.append('<figure><img src="v10-v11-mj-pulls/' + html.escape(a["file"]) + '" alt="" loading="lazy">'
                   '<div><pre>' + html.escape(a["prompt"]) + '</pre>'
                   '<p class="src">' + html.escape(a["source"]) + "</p></div></figure>")
    out.append("</div>")
    out.append("<footer>Built from docs/rules.json and docs/prompts/exploration-log.txt by scripts/build_rules.py.</footer>")
    out += ["</main>", "<script>" + JS.strip() + "</script>", "</body>", "</html>", ""]
    return "\n".join(out)


def main(argv: list[str]) -> int:
    tags = load_tags()
    if len(argv) == 2 and argv[0] == "--tag":
        print(tags.get(argv[1], f"(unknown tag {argv[1]})"))
        return 0
    data = json.loads(RULES.read_text(encoding="utf-8"))
    validate(data, tags)
    OUT.write_text(render(data, tags), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(data['rules'])} rules, {len(data['archive'])} archive entries")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
