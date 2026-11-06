#!/usr/bin/env python3
"""Construct and check the selected source-only installed tooling payload."""
from __future__ import annotations
import argparse
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = "standards/tooling/"
LEGACY_MATERIALIZER = HERE / "fixtures/tooling_materialize-v3.0.4.py"


def current():
    if str(HERE) not in sys.path:
        sys.path.insert(0, str(HERE))
    import tooling_current
    return tooling_current


def materializer():
    try:
        spec = importlib.util.spec_from_file_location("stdo_tool_sources", HERE / "tooling_materialize.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except (OSError, ImportError) as exc:
        raise ValueError("required source materializer unavailable: " + str(exc)) from exc


def selection():
    return json.loads((HERE / "tooling-selection.json").read_bytes())


def check_payload(payload):
    tool = materializer()
    files = {p[len(ROOT):]: raw for p, raw in payload.items() if p.startswith(ROOT)}
    if json.loads(files["TOOLING.json"]).get("kind") == "stdo.installed-tooling/2":
        return current().check_files(files)
    meta, sources = tool.source_bytes(files)
    selected = selection()
    tool.require(meta["sources"] == selected["sources"] and meta["source_commit"] == selected["source_commit"],
                 "installed source inventory differs from release selection")
    tool.require(files["materialize.py"] == LEGACY_MATERIALIZER.read_bytes(), "installed materializer differs")
    tool.require(files["README.md"] == (HERE / "tooling-guide.md").read_bytes(), "installed tooling guide differs")
    return {"status": "checked", "source_files": len(sources), "source_commit": meta["source_commit"],
            "archive_sha256": tool.sha(files["sources.zip"])}


def build(repository, destination):
    tool = materializer()
    repository, destination = tool.ordinary_path(repository), tool.ordinary_path(destination)
    tool.require(not destination.exists(), "preserve existing tooling payload")
    selected = selection()
    tool.require(selected["source_commit"] == tool.SOURCE_COMMIT, "source cut differs")
    archive = io.BytesIO()
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipped:
        for row in selected["sources"]:
            name = tool.safe_path(row["archive_path"])
            raw = subprocess.check_output(["git", "--no-optional-locks", "-C", str(repository),
                                           "show", selected["source_commit"] + ":" + name])
            tool.require(tool.sha(raw) == row["sha256"] and len(raw) == row["bytes"], "source selection changed: " + name)
            tool.require(tool.ordinary_path(repository / name).read_bytes() == raw, "working source differs: " + name)
            entry = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            entry.create_system = 3; entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = int(row["git_mode"], 8) << 16
            zipped.writestr(entry, raw, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    files = {"sources.zip": archive.getvalue(), "materialize.py": LEGACY_MATERIALIZER.read_bytes(),
             "README.md": (HERE / "tooling-guide.md").read_bytes()}
    meta = {"kind": "stdo.installed-tooling/1", "distribution_version": tool.VERSION,
            "source_commit": selected["source_commit"], "sources": selected["sources"],
            "scope": "Existing a_c Graphify/Lean and Codex/Claude Skills source snapshot; external execution dependencies are selected separately.",
            "distribution_members": {p: {"bytes": len(raw), "sha256": tool.sha(raw)} for p, raw in sorted(files.items())}}
    files["TOOLING.json"] = tool.encoded(meta)
    result = check_payload({ROOT + p: raw for p, raw in files.items()})
    destination.mkdir(parents=True, exist_ok=False)
    for p, raw in files.items():
        with (destination / p).open("xb") as stream:
            stream.write(raw)
    return dict(result, status="bundled", archive_bytes=len(files["sources.zip"]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    build_parser = commands.add_parser("build")
    build_parser.add_argument("--repository", type=Path, required=True)
    build_parser.add_argument("--destination", type=Path, required=True)
    build_parser.add_argument("--selection", type=Path)
    build_parser.add_argument("--selection-sha256")
    commands.add_parser("check").add_argument("root", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "build":
            result = (current().build(args.repository, args.destination, args.selection, args.selection_sha256)
                      if args.selection else build(args.repository, args.destination))
        else:
            tool = materializer(); root = tool.ordinary_path(args.root)
            result = check_payload({ROOT + p: b for p, b in tool.read_bundle(root / ROOT).items()})
        print(json.dumps(result, indent=2))
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        print(json.dumps({"status": "refused", "reason": str(exc)}), file=sys.stderr)
        raise SystemExit(2)


if __name__ == "__main__":
    main()
