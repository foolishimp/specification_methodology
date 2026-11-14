#!/usr/bin/env python3
"""Export a portable current-release catalog while retaining source history."""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import subprocess
import sys

PRODUCT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRODUCT / "skills/stdo-context/scripts"))
import context_catalog as catalog
import context_core as core


def encoded(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def package(out: Path, version: str, source_pin: str) -> dict:
    access = catalog.public_bundle(source_pin)
    public = copy.deepcopy(access["public"])
    core.need(public.get("release", {}).get("version") == version, "source release version differs")
    ids = {"stdo-" + version + "-python-pure-refactor-v2", "stdo-" + version + "-sdlc-workflow-v1"}
    entries = [item["entry"] for item in access["entries"] if item["entry"]["id"] in ids]
    core.need({entry["id"] for entry in entries} == ids, "both exact release indexes are required")
    core.need(all(entry["method"] == public["release"]["native_method"] for entry in entries), "release index native binding differs")
    out = out.absolute()
    core.need(not out.exists() and not out.is_symlink() and not out.is_relative_to(PRODUCT), "select a fresh output outside the source Product")
    bodies = {}
    relations = []
    excluded = []
    for row in public["files"]:
        path = Path(row["path"])
        historical_index = path.parts[:3] == ("skills", "stdo-context", "indexes") and len(path.parts) > 4 and path.parts[3] not in ids
        source_only = row["path"] in {"scripts/port_ci02_index.py", "scripts/test_sdlc_index.py"}
        if historical_index or source_only:
            excluded.append(row)
            continue
        body = catalog.local_file(PRODUCT, row["path"]).read_bytes()
        if row["path"] == catalog.CATALOG:
            body = encoded({"profile": "purpose-context.index-catalog/1", "entries": entries})
        bodies[row["path"]] = body
        relations.append({"path": row["path"], "source_sha256": row["sha256"],
                          "distribution_sha256": core.raw_digest(body), "bytes_equal": core.raw_digest(body) == row["sha256"]})
    relation = {"kind": "purpose-context.release-distribution-relation/1", "version": version,
                "source_public_manifest_sha256": source_pin, "native_method": public["release"]["native_method"],
                "selected_index_ids": sorted(ids), "members": relations, "excluded_source_members": excluded,
                "transformations": ["The catalog includes only the two exact current-release indexes.",
                                    "This separate public manifest inventories the actual portable distribution."],
                "limits": ["Historical source assets and work-record links remain in the source project and prior packages.",
                           "Source authoring and reconstruction need the retained predecessor assets named by their provenance; they are not runtime dependencies.",
                           "No semantic assessment, native actor result or publication verdict is created by this export."]}
    bodies["SOURCE_RELATION.json"] = encoded(relation)
    public["distribution"] = {"kind": relation["kind"], "version": version,
                              "source_public_manifest_sha256": source_pin, "source_relation": "SOURCE_RELATION.json"}
    public["files"] = [{"path": name, "sha256": core.raw_digest(body), "bytes": len(body)}
                       for name, body in sorted(bodies.items())]
    bodies["PUBLIC_MANIFEST.json"] = encoded(public)
    out.mkdir(parents=True, exist_ok=False)
    for name, body in bodies.items():
        target = out / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(body)
    pin = core.raw_digest(bodies["PUBLIC_MANIFEST.json"])
    check = subprocess.run([sys.executable, "-B", str(out / public["entrypoint"]), "indexes",
                            "--public-manifest-sha256", pin], capture_output=True, text=True)
    core.need(check.returncode == 0, "exported public runtime refused: " + check.stderr)
    return {"status": "packaged", "path": str(out), "files": len(bodies),
            "source_public_manifest_sha256": source_pin, "public_manifest_sha256": pin,
            "index_ids": sorted(ids), "source_relation_sha256": core.raw_digest(bodies["SOURCE_RELATION.json"])}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--public-manifest-sha256", required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(package(args.out, args.version, args.public_manifest_sha256), indent=2))
        return 0
    except (core.Refusal, OSError, ValueError, KeyError) as error:
        print(json.dumps({"status": "refused", "reason": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
