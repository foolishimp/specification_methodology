#!/usr/bin/env python3
"""List the C3 re-proof span of the Claude tenant frontier, and check loci.

The span rule is PLAN.md, "Re-proof span": every frontier row whose text a
later step changes, plus every row that depends on a section whose content
or ownership changes. This script makes the rule mechanical. A row is in
the span for one or more of these reasons:

  T  a delta table with a Disposition column changes the row's text, or
     the row's disposition or locus differs from the frontier at the base
     commit (shown as T(frontier));
  D  a delta lists the row as re-proof span (a section or paragraph whose
     heading or first words contain "re-proof span");
  S  a section the row's locus names has changed text since the base
     commit (leaf section: heading to the next heading of any level,
     whitespace collapsed; a section absent at the base counts as changed;
     a locus with no anchor compares the whole file);
  R  a section the row's locus names refers to an owner whose content or
     ownership changed (PLAN.md: results and conjunction, measurement;
     deltas/A3.md: REFERENCE_FRAME §5 and §6).

Usage (run with python3 -I from anywhere):

  list_span.py [--ref REF | --worktree] [--base COMMIT] [--format text|markdown]
  list_span.py --check-loci [--ref REF | --worktree]

--ref reads every input (frontier, deltas, members) from a git ref through
`git show` (default HEAD); --worktree reads the files on disk. The base is
read with `git show` (default 31f28f9, the base in LEDGER.md). The script
runs no git command that changes state.

--check-loci checks that every `conserved` or `superseded` row names at
least one locus and that each locus file exists and each anchor is a
heading of that file, and prints each failure.

Rows are keyed by member and anchor, never by line number, because rows are
inserted into the frontier (I2 inserted five child rows). The base is
compared row by row under that key. A delta cites rows by the line numbers
of the frontier it was written against; every delta so far numbers the
862-line frontier that the base also numbers. A cited line is read through
the base frontier. Where the delta also cites an anchor for it, the row is
kept only if its anchor agrees (a cited path may omit a leading
directory); otherwise the current frontier's row at that line is tried,
and then, for a cell that cites one line, the one row carrying the cited
anchor (a child row cited as "after 516"). A cited anchor that none of
these resolves is reported as a warning. Output lines show each row's
current line number.
"""

import argparse
import os
import re
import subprocess
import sys

BASE_DEFAULT = "31f28f9"
HERE = os.path.dirname(os.path.abspath(__file__))
TENANT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
FRONTIER = "frontier/PREDECESSOR_CLAIMS.md"
DELTAS = "qualification/C3-SYNTHESIS/deltas"

# Owners whose content or ownership changed (PLAN.md "Sections whose
# ownership or content others depend on"; deltas/A3.md for RF §5 and §6).
# Each entry: owning member, in-member pattern, cross-member pattern.
OWNERS = [
    ("FOUNDATIONS.md", r"§4\b|\(#results\)|\(#conjunction-of-results\)",
     r"FOUNDATIONS §4|FOUNDATIONS\.md#results|FOUNDATIONS\.md#conjunction-of-results"),
    ("ACTIVATION.md",
     r"§[236]\b|\(#[236]-|\(#(admission-and-activation|construction-availability|disposition|ambiguity-outcome|effects)\)",
     r"ACTIVATION §[236]\b|ACTIVATION\.md#[236]-|ACTIVATION\.md#(admission-and-activation|construction-availability|disposition|ambiguity-outcome|effects)\b"),
    ("REFERENCE_FRAME.md",
     r"RF-002|§[56]\b|\(#(5-method-functions|6-frames-in-conjunction|result-conjunction|rf-002-finite-attention)\)",
     r"RF-002|REFERENCE_FRAME §[56]\b|REFERENCE_FRAME\.md#(5-method-functions|6-frames-in-conjunction|result-conjunction|rf-002-finite-attention)"),
]


def git(*args):
    return subprocess.run(["git", "-C", TENANT] + list(args), check=True,
                          capture_output=True, text=True).stdout


REPO_PREFIX = git("rev-parse", "--show-prefix").strip()


class Source:
    """Reads tenant-relative paths from a ref or from the working tree."""

    def __init__(self, ref=None):
        self.ref = ref
        self.cache = {}

    def read(self, rel):
        rel = os.path.normpath(rel)
        if rel in self.cache:
            return self.cache[rel]
        text = None
        if self.ref is None:
            path = os.path.join(TENANT, rel)
            if os.path.isfile(path):
                with open(path, encoding="utf-8") as fh:
                    text = fh.read()
        else:
            r = subprocess.run(["git", "-C", TENANT, "show",
                                f"{self.ref}:{REPO_PREFIX}{rel}"],
                               capture_output=True, text=True)
            if r.returncode == 0:
                text = r.stdout
        self.cache[rel] = text
        return text

    def listdir(self, rel):
        if self.ref is None:
            return sorted(os.listdir(os.path.join(TENANT, rel)))
        out = git("ls-tree", "--name-only", "--full-tree", f"{self.ref}:{REPO_PREFIX}{rel}")
        return sorted(out.split())


def slug(heading):
    h = heading.strip().lower()
    h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", h)
    h = h.replace("`", "")
    h = "".join(ch for ch in h if ch.isalnum() or ch in "-_ ")
    return h.replace(" ", "-")


def sections(text):
    """Map slug -> leaf section text; fence-aware; GitHub duplicate suffixes."""
    out, seen = {}, {}
    lines = text.split("\n")
    heads = []
    fence = False
    for i, line in enumerate(lines):
        if re.match(r"^\s*(```|~~~)", line):
            fence = not fence
            continue
        m = None if fence else re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if m:
            s = slug(m.group(2))
            n = seen.get(s, 0)
            seen[s] = n + 1
            heads.append((s if n == 0 else f"{s}-{n}", i))
    for k, (s, start) in enumerate(heads):
        end = heads[k + 1][1] if k + 1 < len(heads) else len(lines)
        out[s] = " ".join("\n".join(lines[start:end]).split())
    return out


def cells(line):
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")):
        return None
    s, out, cur, i = s[1:-1], [], "", 0
    while i < len(s):
        if s[i] == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur += "\\|"
            i += 2
            continue
        if s[i] == "|":
            out.append(cur.strip())
            cur = ""
        else:
            cur += s[i]
        i += 1
    out.append(cur.strip())
    return out


def frontier_rows(text):
    """Rows with a disposition: (member, anchor) -> dict(line, member, anchor, disp, locus)."""
    rows, member, started = {}, None, False
    for n, line in enumerate(text.split("\n"), 1):
        if line.startswith("## "):
            member = line[3:].strip()
            started = member not in ("Granularity and rules", "Members")
            continue
        c = cells(line)
        if not started or c is None or len(c) < 5:
            continue
        if c[0] in ("Section", "Member") or set("".join(c)) <= set("-: "):
            continue
        anchor = c[1].strip("`") if len(c) == 6 else c[0].strip("`")
        key = (member, anchor)
        if key in rows:
            sys.exit(f"duplicate frontier row {key} at lines {rows[key]['line']} and {n}")
        rows[key] = dict(line=n, member=member, anchor=anchor, disp=c[-2], locus=c[-1])
    return rows


def by_line(rows):
    return {r["line"]: k for k, r in rows.items()}


class Resolver:
    """Resolves a delta's cited line, with the anchors it cites, to a row key."""

    def __init__(self, rows, base_rows):
        self.rows = rows
        self.base_line = by_line(base_rows)
        self.cur_line = by_line(rows)

    def cited(self, x):
        return x in self.base_line or x in self.cur_line

    def resolve(self, x, anchors, single):
        """Return (key or None, warning or None).

        Without a cited anchor the line is read through the base frontier
        only. With one, the base row is kept if its anchor agrees; then the
        current row at that line; then, for a cell citing one line, the one
        row that carries the anchor."""
        base_k = self.base_line.get(x)
        base_k = base_k if base_k in self.rows else None
        if not anchors:
            return base_k, None
        cur_k = self.cur_line.get(x)
        for k in (base_k, cur_k):
            if k is not None and anchor_matches(self.rows[k]["anchor"], anchors):
                return k, None
        if single:
            hits = [k for k, r in self.rows.items() if anchor_matches(r["anchor"], anchors)]
            if len(hits) > 1 and base_k is not None:
                hits = [k for k in hits if k[0] == base_k[0]]
            if len(hits) == 1:
                return hits[0], None
        shown = self.rows[base_k]["anchor"] if base_k else "no row"
        return base_k, f"line {x} reads as {shown}, not in {sorted(anchors)}"


def anchor_matches(anchor, cited):
    """A row anchor matches a cited anchor, or a cited path that ends it."""
    return anchor in cited or any(
        not a.startswith("#") and anchor.endswith("/" + a) for a in cited)


def cited_anchors(header, c):
    """Backticked anchors or member paths in the delta row's anchor cells."""
    cols = [i for i, h in enumerate(header) if "anchor" in h.lower() or h.strip().lower() == "member"]
    if not cols and len(c) > 1:
        cols = [1]
    found = set()
    for i in cols:
        if i < len(c):
            found.update(re.findall(r"`([^`]+)`", c[i]))
    return found


def disposition_value(disp):
    d = disp.lower()
    for v in ("conserved", "superseded", "intentionally removed",
              "not applicable", "unresolved"):
        if d.startswith(v):
            return v
    return "other"


def locus_refs(locus):
    """(path, anchor or None) for each path-like reference in the locus."""
    refs, last = [], None
    for span in re.findall(r"`([^`]+)`", locus):
        for part in span.split(";"):
            part = part.strip()
            if re.match(r"^#[\w.%-]+$", part) and last:
                refs.append((last, part[1:]))
                continue
            m = re.match(r"^([\w./-]+\.(?:md|json|yaml|yml|py|txt)|LICENSE|[\w./-]+/LICENSE)(?:#([\w.%-]+))?$", part)
            if m:
                last = m.group(1)
                refs.append((m.group(1), m.group(2)))
    return refs


def resolve_path(src, path):
    """Body loci are relative to standards/, other loci to the tenant root."""
    for rel in (os.path.join("standards", path), path):
        rel = os.path.normpath(rel)
        if src.read(rel) is not None:
            return rel
    return None


def numbers(text):
    text = re.sub(r"`[^`]*`", " ", text)
    found = []
    for m in re.finditer(r"(?<![§:#\w.–-])(\d{2,3})(?:\s+to\s+(\d{2,3}))?(?![\w.%–])", text):
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else a
        found.extend(range(a, b + 1))
    return found


def delta_lists(src, rows, resolver):
    """T and D rows (keyed by member and anchor) from every delta file, with their delta names."""
    t_rows, d_rows, warnings = {}, {}, []
    for name in src.listdir(DELTAS):
        if not name.endswith(".md"):
            continue
        text = src.read(f"{DELTAS}/{name}") or ""
        tag = name[:-3]
        span_sec, header, para_span = False, None, False
        for line in text.split("\n"):
            if line.startswith("#"):
                span_sec = "re-proof span" in line.lower()
                header, para_span = None, False
                continue
            c = cells(line)
            if c is not None:
                if header is None:
                    header = c
                    continue
                if set("".join(c)) <= set("-: "):
                    continue
                nums = [x for x in numbers(c[0]) if resolver.cited(x)]
                is_t = any("isposition" in h for h in header) and header[0].lower().startswith("line")
                if is_t or span_sec:
                    anchors = cited_anchors(header, c)
                    target = t_rows if is_t else d_rows
                    for x in nums:
                        key, warn = resolver.resolve(x, anchors, len(nums) == 1)
                        if warn:
                            warnings.append(f"{tag}: {warn}")
                        if key is not None:
                            target.setdefault(key, set()).add(tag)
                continue
            header = None
            if line.strip() == "":
                para_span = False
                continue
            if line.lower().startswith("re-proof span"):
                para_span = True
            if (span_sec and line.startswith("- ")) or para_span:
                kept = re.sub(r"`([^`]*)`",
                              lambda s: s.group(0) if s.group(1).startswith("#") else " ", line)
                for m in re.finditer(r"(?<![§:#\w.–-])(\d{2,3})(?:\s+to\s+(\d{2,3}))?\s*(`#[^`]+`)?",
                                     kept):
                    a = int(m.group(1))
                    b = int(m.group(2)) if m.group(2) else a
                    anchors = {m.group(3).strip("`")} if m.group(3) and a == b else set()
                    for x in range(a, b + 1):
                        if not resolver.cited(x):
                            continue
                        key, warn = resolver.resolve(x, anchors, a == b)
                        if warn:
                            warnings.append(f"{tag}: {warn}")
                        if key is not None:
                            d_rows.setdefault(key, set()).add(tag)
    return t_rows, d_rows, warnings


def owner_refs(member_file, text):
    hits = []
    for owner, inside, outside in OWNERS:
        pat = inside + "|" + outside if member_file == owner else outside
        if re.search(pat, text):
            hits.append(owner)
    return hits


def compute_span(src, base):
    rows = frontier_rows(src.read(FRONTIER))
    base_rows = frontier_rows(base.read(FRONTIER) or "")
    t_rows, d_rows, warnings = delta_lists(src, rows, Resolver(rows, base_rows))
    for n, row in rows.items():
        old = base_rows.get(n)
        if old is None or (old["disp"], old["locus"]) != (row["disp"], row["locus"]):
            t_rows.setdefault(n, set()).add("frontier")
    base_secs, cand_secs = {}, {}
    span = {}
    for n, row in rows.items():
        reasons = []
        if n in t_rows:
            reasons.append("T(" + ",".join(sorted(t_rows[n])) + ")")
        if n in d_rows:
            reasons.append("D(" + ",".join(sorted(d_rows[n])) + ")")
        s_hits, r_hits = [], []
        for path, anchor in locus_refs(row["locus"]):
            rel = resolve_path(src, path)
            if rel is None:
                continue
            cand = src.read(rel)
            b = base.read(rel)
            if anchor is None:
                if b is None or " ".join(b.split()) != " ".join(cand.split()):
                    s_hits.append(path)
                text = cand
            else:
                cs = cand_secs.setdefault(rel, sections(cand) if rel.endswith(".md") else {})
                bs = base_secs.setdefault(rel, sections(b) if b and rel.endswith(".md") else {})
                if anchor not in cs:
                    continue
                if bs.get(anchor) != cs[anchor]:
                    s_hits.append(f"{path}#{anchor}")
                text = cs[anchor]
            for owner in owner_refs(os.path.basename(rel), text):
                r_hits.append(f"{path}{'#' + anchor if anchor else ''}->{owner[:-3]}")
        if s_hits:
            reasons.append("S")
        if r_hits:
            reasons.append("R")
        if reasons:
            span[n] = dict(row, reasons=reasons, s=s_hits, r=r_hits)
    return rows, span, warnings


def check_loci(src):
    rows = frontier_rows(src.read(FRONTIER))
    cache, failures, checked = {}, [], 0
    for row in rows.values():
        n = row["line"]
        if disposition_value(row["disp"]) not in ("conserved", "superseded"):
            continue
        checked += 1
        refs = locus_refs(row["locus"])
        if not refs:
            failures.append(f"{n}: no locus reference: {row['locus'][:80]}")
        for path, anchor in refs:
            rel = resolve_path(src, path)
            if rel is None:
                failures.append(f"{n}: file not found: {path}")
                continue
            if anchor is None:
                continue
            secs = cache.setdefault(rel, sections(src.read(rel)) if rel.endswith(".md") else {})
            if anchor not in secs:
                failures.append(f"{n}: anchor not found: {path}#{anchor}")
    return checked, failures


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--ref", default="HEAD")
    g.add_argument("--worktree", action="store_true")
    ap.add_argument("--base", default=BASE_DEFAULT)
    ap.add_argument("--format", choices=("text", "markdown"), default="text")
    ap.add_argument("--check-loci", action="store_true")
    a = ap.parse_args()
    src = Source(None if a.worktree else a.ref)
    if a.check_loci:
        checked, failures = check_loci(src)
        print(f"conserved or superseded rows checked: {checked}; failures: {len(failures)}")
        for f in failures:
            print(f)
        return 1 if failures else 0
    rows, span, warnings = compute_span(src, Source(a.base))
    for w in warnings:
        print("warning:", w, file=sys.stderr)
    if a.format == "markdown":
        print("| Line | Member | Anchor | Reasons | Changed locus sections (S) | Owner references (R) |")
        print("|---|---|---|---|---|---|")
        for r in sorted(span.values(), key=lambda r: r["line"]):
            print(f"| {r['line']} | {r['member']} | `{r['anchor']}` | {' '.join(r['reasons'])} | "
                  f"{'; '.join(r['s']) or '-'} | {'; '.join(r['r']) or '-'} |")
    else:
        for r in sorted(span.values(), key=lambda r: r["line"]):
            print(r["line"], r["member"], r["anchor"], " ".join(r["reasons"]))
    counts = {k: sum(1 for r in span.values() if any(x.startswith(k) for x in r["reasons"]))
              for k in "TDSR"}
    print(f"\nspan rows: {len(span)} of {len(rows)} rows with a disposition; "
          + ", ".join(f"{k} {v}" for k, v in counts.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
