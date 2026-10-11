#!/usr/bin/env python3
"""Measure or print one Markdown heading section by slug.

Usage:
  fragment.py --file PATH --slug SLUG --size   # bytes of the section, nothing read into context
  fragment.py --file PATH --slug SLUG --text   # the section text
  fragment.py --file PATH --list               # slugs with byte sizes

The slug rule is the Axiom Indexer rule at the pinned subject: lower-case the
heading, drop characters other than word characters, hyphens and spaces,
collapse runs of spaces and hyphens to one hyphen, strip hyphens; a repeated
slug gets -1, -2, ... in order of occurrence. A section runs from its heading
to the next heading of the same or higher level.
"""
import argparse
import re
import sys

HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")


def slug_of(title: str) -> str:
    base = title.strip().lower()
    base = re.sub(r"[^\w\- ]", "", base, flags=re.UNICODE)
    return re.sub(r"[\s\-]+", "-", base).strip("-")


def sections(text: str):
    lines = text.splitlines(keepends=True)
    heads = []
    occurrences = {}
    for i, line in enumerate(lines):
        m = HEADING.match(line)
        if not m:
            continue
        base = slug_of(m.group(2))
        n = occurrences.get(base, 0)
        occurrences[base] = n + 1
        heads.append((i, len(m.group(1)), base if n == 0 else f"{base}-{n}"))
    out = {}
    for k, (start, level, slug) in enumerate(heads):
        end = len(lines)
        for j in range(k + 1, len(heads)):
            if heads[j][1] <= level:
                end = heads[j][0]
                break
        out[slug] = "".join(lines[start:end])
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--slug")
    ap.add_argument("--size", action="store_true")
    ap.add_argument("--text", action="store_true")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    with open(a.file, encoding="utf-8") as fh:
        secs = sections(fh.read())
    if a.list:
        for slug, body in secs.items():
            print(f"{len(body.encode('utf-8')):8d}  {slug}")
        return 0
    if not a.slug or a.slug not in secs:
        print(f"unresolved_fragment: {a.slug}", file=sys.stderr)
        return 2
    body = secs[a.slug]
    if a.size:
        print(len(body.encode("utf-8")))
    if a.text:
        sys.stdout.write(body)
    return 0


if __name__ == "__main__":
    sys.exit(main())
