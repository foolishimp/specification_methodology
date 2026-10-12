#!/usr/bin/env python3
"""Check documentary identity, source routes and recorded conservation coverage.

This checks artifacts. It deliberately does not infer semantic satisfaction,
independent assessment, owner acceptance or release from structural success.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def anchors(text):
    found = set(re.findall(r'<a\s+(?:id|name)=[\"\']([^\"\']+)', text))
    counts = {}
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
        if in_fence:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        heading = re.sub(r"<[^>]*>", "", match[1]).replace("`", "")
        slug = unicodedata.normalize("NFC", heading).lower()
        slug = re.sub(r"[^\w\-\s]", "", slug)
        slug = re.sub(r"\s", "-", slug)
        number = counts.get(slug, 0)
        counts[slug] = number + 1
        found.add(slug + (f"-{number}" if number else ""))
    return found


def check(root, partial=False):
    failures = []
    checks = {"relative_links": 0, "frontier_rows": 0, "json_files": 0}
    files = [p for p in root.rglob("*") if p.is_file() and p.suffix in {".md", ".json", ".yaml"}]
    for path in files:
        text = path.read_text()
        if any(line != line.rstrip() for line in text.splitlines()):
            failures.append(f"trailing whitespace: {path.relative_to(root)}")
        if path.suffix == ".json":
            checks["json_files"] += 1
            try:
                json.loads(text)
            except ValueError as error:
                failures.append(f"invalid JSON: {path.relative_to(root)}: {error}")
        if path.suffix != ".md":
            continue
        for match in re.finditer(r"(?<!!)\[[^\]]*\]\(([^\n]+?)\)", text):
            target = match[1].strip().strip("<>").split(' "')[0]
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            location, _, fragment = target.partition("#")
            destination = (path.parent / unquote(location)).resolve() if location else path
            checks["relative_links"] += 1
            if not destination.exists():
                if not partial:
                    failures.append(f"missing target: {path.relative_to(root)} -> {target}")
            elif fragment and destination.suffix == ".md" and unquote(fragment) not in anchors(destination.read_text()):
                failures.append(f"missing anchor: {path.relative_to(root)} -> {target}")
    conservation = root / "CONSERVATION.json"
    if conservation.exists():
        rows = json.loads(conservation.read_text())["rows"]
        checks["frontier_rows"] = len(rows)
        if len(rows) != 690 or len({row["id"] for row in rows}) != 690:
            failures.append("frontier must contain exactly 690 distinct selected rows")
        for row in rows:
            locus = row.get("successor_locus")
            if row["disposition"] == "unresolved":
                if not partial:
                    failures.append(f"unresolved author disposition: {row['id']}")
                continue
            if not locus:
                failures.append(f"missing successor locus: {row['id']}")
                continue
            name, _, fragment = locus.partition("#")
            destination = root / name
            if not destination.is_file():
                failures.append(f"missing conservation member: {row['id']} -> {locus}")
            elif fragment and fragment not in anchors(destination.read_text()):
                failures.append(f"missing conservation anchor: {row['id']} -> {locus}")
            elif row.get("successor_sha256") and digest(destination) != row["successor_sha256"]:
                failures.append(f"changed mapped member: {row['id']}")
    elif not partial:
        failures.append("missing conservation map")
    manifest = root / "CANDIDATE.json"
    if manifest.exists():
        for member in json.loads(manifest.read_text())["members"]:
            path = root / member["path"]
            if not path.is_file() or digest(path) != member["sha256"]:
                failures.append(f"candidate pin mismatch: {member['path']}")
    elif not partial:
        failures.append("missing candidate manifest")
    return {"kind": "documentary_artifact_check", "partial": partial, "checks": checks,
            "failures": failures, "valid": not failures,
            "limits": ["No semantic conservation inference", "No independent use inference",
                       "No checkpoint acceptance or release inference"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--partial", action="store_true")
    args = parser.parse_args()
    report = check(Path(__file__).resolve().parent, args.partial)
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["valid"] else 1)
