"""Bounded RC1 source-note, local-link and package conformance observations."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote, urlsplit

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
PROJECT = ROOT / "specification_methodology"
inventory = json.loads((OUT / "source-inventory.json").read_text())
files = [ROOT / p for p in ("README.md", "STACK_RELEASE.md", "AGENTS.md", "CLAUDE.md")]
files += [PROJECT / p for p in (
    "README.md", "QUICKSTART.md", "specification/GOALS.md", "releases/v2.5.1.md",
    "plugins/spec/references/GETTING_STARTED.md",
)]
failures = []
links = []


def require(condition, message):
    if not condition:
        failures.append(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prose(path):
    return re.sub(r"```.*?```", "", path.read_text(), flags=re.S)


def anchors(path):
    headings = re.findall(r"^#{1,6}\s+(.+)$", prose(path), flags=re.M)
    return {re.sub(r"[^\w\s-]", "", h.lower()).replace(" ", "-") for h in headings}


for path in files:
    require(path.exists(), f"missing document: {path}")
    for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", prose(path)):
        parts = urlsplit(target)
        if parts.scheme or parts.netloc:
            continue  # Public verification is a later release phase.
        destination = (path.parent / unquote(parts.path)).resolve() if parts.path else path
        valid = destination.exists()
        if valid and parts.fragment:
            valid = destination.is_file() and unquote(parts.fragment) in anchors(destination)
        links.append({"source": str(path.relative_to(ROOT)), "target": target, "valid": valid})
        require(valid, f"invalid local link: {path.relative_to(ROOT)} -> {target}")

require((PROJECT / "releases/v2.5.1.md").read_bytes() ==
        (OUT / "release-note.candidate.md").read_bytes(), "release note differs from exact inventory output")
for prefix, rows in (("specification/standards", inventory["standards"]),
                     ("plugins/spec", inventory["plugin"]),
                     ("src/stdo_toolchain", inventory["manager"])):
    for row in rows:
        require(digest(PROJECT / prefix / row["path"]) == row["sha256"],
                f"inventory drift: {prefix}/{row['path']}")
for path, expected in inventory["conserved_source_bindings"].items():
    require(digest(PROJECT / path) == expected, f"source binding drift: {path}")
for relative in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
    require(json.loads((PROJECT / "plugins/spec" / relative).read_text())["version"] ==
            "2.5.1-rc.1", f"wrong plugin version: {relative}")
for relative in ("QUICKSTART.md", "plugins/spec/references/GETTING_STARTED.md"):
    text = (PROJECT / relative).read_text()
    require("specification_methodology/v2.5.1-rc.1" in text and "after publication" in text,
            f"missing exact post-publication installation route: {relative}")
require("v2.5.0-rc.4" in (PROJECT / "stdo_default.json").read_text(), "source basis changed")
report = {"kind": "stdo.251-rc1-source-conformance", "status": "satisfied" if not failures else "failed",
          "links": links, "link_count": len(links), "failures": failures,
          "release_note_sha256": digest(PROJECT / "releases/v2.5.1.md"),
          "limits": "Local source/link/inventory checks only; no native or public release qualification."}
(OUT / "source-checks.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({key: report[key] for key in ("status", "link_count", "failures")}))
raise SystemExit(bool(failures))
