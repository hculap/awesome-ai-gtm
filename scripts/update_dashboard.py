#!/usr/bin/env python3
"""Regenerate DASHBOARD.md stats from README.md.

Keeps the curated reference tables intact and only refreshes the machine-derivable
parts: total tool count, a per-stage breakdown, and the "Last updated" footer.
We deliberately do NOT fabricate pricing/category percentages — the README has no
machine-readable tags, so those stay hand-curated (or absent) rather than guessed.

Run: python3 scripts/update_dashboard.py [--check]
  --check exits 1 if DASHBOARD.md would change (for CI), without writing.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")
DASHBOARD = os.path.join(ROOT, "DASHBOARD.md")

# A tool entry is a top-level list item whose link is an external URL.
# TOC/anchor links look like `- [Text](#anchor)` and are excluded.
ENTRY_RE = re.compile(r"^- \[[^\]]+\]\(https?://")
# `## ` stage headings (skip the Contents section and the title).
H2_RE = re.compile(r"^## (.+)$")

AUTOGEN_START = "<!-- AUTOGEN:STATS START -->"
AUTOGEN_END = "<!-- AUTOGEN:STATS END -->"


def parse_readme(text: str) -> tuple[int, list[tuple[str, int]]]:
    """Return (total_tools, [(stage_name, count), ...])."""
    total = 0
    per_stage: list[tuple[str, int]] = []
    current: str | None = None
    count = 0
    in_contents = False
    for line in text.splitlines():
        m = H2_RE.match(line)
        if m:
            name = m.group(1).strip()
            # flush previous
            if current is not None:
                per_stage.append((current, count))
            in_contents = name.lower().startswith("contents")
            # Don't track non-stage sections like Contributing/Contents.
            current = None if (in_contents or name.lower().startswith("contributing")) else name
            count = 0
            continue
        if current is not None and ENTRY_RE.match(line):
            total += 1
            count += 1
    if current is not None:
        per_stage.append((current, count))
    return total, [s for s in per_stage if s[1] > 0]


def build_block(total: int, per_stage: list[tuple[str, int]], today: str) -> str:
    lines = [
        AUTOGEN_START,
        "## Auto-generated Stats 🤖",
        "",
        "> Derived directly from `README.md` by `scripts/update_dashboard.py`. Do not edit by hand.",
        "",
        f"- **Total tools listed**: {total}",
        "",
        "| GTM Stage | Tools |",
        "|-----------|-------|",
    ]
    for name, cnt in per_stage:
        lines.append(f"| {name} | {cnt} |")
    lines += ["", f"*Last updated: {today}*", AUTOGEN_END]
    return "\n".join(lines)


def render(dashboard_text: str, block: str) -> str:
    if AUTOGEN_START in dashboard_text and AUTOGEN_END in dashboard_text:
        return re.sub(
            re.escape(AUTOGEN_START) + r".*?" + re.escape(AUTOGEN_END),
            block.replace("\\", "\\\\"),
            dashboard_text,
            flags=re.DOTALL,
        )
    # Append the block at the end on first run.
    sep = "" if dashboard_text.endswith("\n") else "\n"
    return f"{dashboard_text}{sep}\n---\n\n{block}\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if changes needed, don't write")
    ap.add_argument("--date", default=None, help="override date (YYYY-MM-DD), for tests")
    args = ap.parse_args()

    with open(README, encoding="utf-8") as f:
        readme = f.read()
    with open(DASHBOARD, encoding="utf-8") as f:
        dashboard = f.read()

    today = args.date or _dt.date.today().isoformat()
    total, per_stage = parse_readme(readme)
    block = build_block(total, per_stage, today)
    updated = render(dashboard, block)

    if updated == dashboard:
        print(f"DASHBOARD.md already current ({total} tools).")
        return 0

    if args.check:
        print("DASHBOARD.md is out of date — run scripts/update_dashboard.py", file=sys.stderr)
        return 1

    with open(DASHBOARD, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"DASHBOARD.md updated: {total} tools across {len(per_stage)} stages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
