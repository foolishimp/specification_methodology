#!/usr/bin/env python3
"""Freeze only an explicitly supplied native cut, or check its exact custody."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / "release_tools"))
import application_contract as c


def git(repository, *args):
    return subprocess.check_output(["git", "--no-optional-locks", "-C", str(repository), *args])


def members(repository, commit, package_path):
    c.require(c.hex_digest(commit, 40), "full nonzero Git commit required")
    c.relative(package_path)
    c.require(git(repository, "cat-file", "-t", commit).strip() == b"commit", "source must be a commit")
    rows = []
    raw_files = {}
    prefix = package_path + "/"
    for entry in git(repository, "ls-tree", "-rz", commit, "--", package_path).split(b"\0"):
        if not entry:
            continue
        attributes, raw_path = entry.split(b"\t", 1)
        mode, kind, blob = attributes.decode("ascii").split()
        path = raw_path.decode("utf-8")
        c.require(path.startswith(prefix) and kind == "blob" and mode in ("100644", "100755"), "unsupported source tree member")
        path = c.relative(path[len(prefix):])
        raw = git(repository, "cat-file", "blob", blob)
        raw_files[path] = raw
        rows.append({"path": path, "bytes": len(raw), "sha256": c.sha(raw), "git_blob": blob, "git_mode": mode})
    rows.sort(key=lambda row: row["path"])
    c.require(rows and len(rows) == len(raw_files), "empty or duplicate source inventory")
    return rows, raw_files


def verify_selection(repository, selection, expected_sha=None, raw=None):
    if expected_sha is not None:
        c.require(raw is not None and c.hex_digest(expected_sha) and c.sha(raw) == expected_sha, "Root-selected source-selection digest differs")
    c.require(selection["kind"] == "a_c.stdo301.native-source-selection/1", "unsupported native selection contract")
    native = selection["native"]
    c.require(native["cut"] == "v3.0.1-rc.1" and selection["standing"] == "test_candidate_not_accepted", "native cut/standing differs")
    c.require(re.fullmatch(r"[A-Za-z][A-Za-z0-9+.-]*:[^\s]+", selection["subject_uri"]) is not None, "absolute represented subject required")
    c.require(c.hex_digest(native["package_tree"], 40) and c.hex_digest(native["tag_object"], 40)
              and c.hex_digest(native["manifest_sha256"]), "exact native tree/tag/manifest coordinates required")
    ref = native["qualified_ref"]
    c.require(ref == "refs/tags/specification_methodology/v3.0.1-rc.1", "native qualified ref differs")
    c.require(git(repository, "rev-parse", "--verify", ref).decode().strip() == native["tag_object"], "native tag object differs")
    c.require(git(repository, "cat-file", "-t", native["tag_object"]).strip() == b"tag", "genuine annotated native tag required")
    c.require(git(repository, "rev-parse", ref + "^{commit}").decode().strip() == native["commit"], "native tag peeled commit differs")
    rows, raw_files = members(repository, native["commit"], native["package_path"])
    c.require(git(repository, "rev-parse", native["commit"] + ":" + native["package_path"]).decode().strip() == native["package_tree"], "native package tree differs")
    c.require(rows == selection["files"], "native Git files differ from selected manifest")
    c.require(selection["file_count"] == len(rows) and selection["total_bytes"] == sum(row["bytes"] for row in rows)
              and selection["inventory_sha256"] == c.digest(c.inventory_rows(rows)), "selected source extent differs")
    candidate = selection["source_candidate"]
    previous, _ = members(repository, candidate["commit"], candidate["package_path"])
    c.require(git(repository, "rev-parse", candidate["commit"] + ":" + candidate["package_path"]).decode().strip() == candidate["package_tree"], "source candidate tree differs")
    c.require(previous == rows, "source candidate and native payload bytes differ")
    manifest_verified = False
    if "manifest_path" in native:
        manifest = c.exact_file(repository, native["manifest_path"])
        c.require(c.sha(manifest.read_bytes()) == native["manifest_sha256"], "canonical native manifest bytes differ")
        manifest_verified = True
    return rows, raw_files, manifest_verified


def source_sections(root, primary, raw_files, subject, generation):
    sys.path.insert(0, str(root / "implementation/code"))
    import ac_generate as g
    sections = []
    for row in primary:
        text = raw_files[row["path"]].decode("utf-8")
        c.require("\r" not in text, "semantic source must be exact LF UTF-8: " + row["path"])
        sections.extend(g.sections(row["path"], text, subject))
    chunks = g.make_chunks(sections, generation["chunk_chars"])
    return [{key: segment[key] for key in ("id", "path", "start_line", "end_line", "sha256")}
            for chunk in chunks for segment in chunk["segments"]], len(chunks)


def readiness(app, selection, primary):
    native = selection["native"]
    return f'''# STDO 3.0.1 RC1 represented-source custody

This portable record binds one explicitly selected test candidate. It establishes
source custody only. Inherited common standing remains `not_ready` and unaccepted;
new representation assessment, semantic acceptance and publication remain open.
The selected predecessor is `{app['predecessor']}`. No immutable consumer changes
its operative method through this supplementary representation.

| Coordinate | Exact value |
|---|---|
| Subject | `{selection['subject_uri']}` |
| Native commit | `{native['commit']}` |
| Native package path | `{native['package_path']}` |
| Native package tree | `{native['package_tree']}` |
| Local native ref | `{native['qualified_ref']}` |
| Native annotated tag object | `{native['tag_object']}` |
| Canonical native manifest SHA256 | `{native['manifest_sha256']}` |
| Complete inventory SHA256 | `{selection['inventory_sha256']}` |
| Complete payload | {selection['file_count']} files, {selection['total_bytes']} bytes |
| Selected semantic source | {len(primary)} files, {sum(row['bytes'] for row in primary)} bytes |
| Builder | `{app['builder']['uri']}` |
| Builder manifest SHA256 | `{app['builder']['manifest_sha256']}` |

`source/` preserves every native payload member, including derived frames and
host/legal/release metadata. `source-manifest.json` selects semantic owners;
`source-classification.json` preserves frame routes and the complete partition.
Frame-owner byte checks do not establish frame semantic sufficiency. Templates,
optional profiles and host configuration retain their own applicability.

From an extracted final bundle, run `python3 -B release_tools/bundle_check.py .`.
That command requires only bundled inputs and Python standard library. The
originating Git checkout and private actor evidence are not distribution inputs.
`RELEASE.json` indexes any separately supplied actual construction/review receipts.
No construction, independent review, semantic acceptance or browser result is
manufactured by this source record. Local tag presence is not remote publication.
'''


def freeze(root, repository, selection_path, expected_sha):
    app = c.application(root)
    c.implementation(root)
    raw_selection = Path(selection_path).read_bytes()
    selection = c.load(selection_path)
    rows, raw_files, manifest_verified = verify_selection(repository, selection, expected_sha, raw_selection)
    native = selection["native"]
    source = {"commit": native["commit"], "payload_commit": selection["source_candidate"]["commit"],
              "package_root": native["package_path"], "package_tree": native["package_tree"],
              "qualified_ref": native["qualified_ref"], "tag_object": native["tag_object"], "native_manifest_sha256": native["manifest_sha256"]}
    primary = [row for row in rows if c.selection_class(row["path"]) == "primary_semantic"]
    c.require(primary, "semantic selection is empty")
    frame_data = json.loads(raw_files["standards/frames/FRAME_INPUTS.json"])
    c.check_frame_routes(rows, frame_data)
    common = {"subject_id": selection["subject_uri"], "source": source}
    custody = {"kind": "a_c.application-package-custody/1", **common, "members": rows,
               "member_count": len(rows), "bytes": sum(row["bytes"] for row in rows), "inventory_digest": c.digest(c.inventory_rows(rows))}
    semantic = {"kind": "a_c.application-semantic-source/1", **common, "files": primary,
                "member_count": len(primary), "bytes": sum(row["bytes"] for row in primary), "inventory_digest": c.digest(c.inventory_rows(primary))}
    groups = {}
    for group in ("primary_semantic", "derived_frames", "host_legal_release_metadata"):
        selected = [row for row in rows if c.selection_class(row["path"]) == group]
        groups[group] = {"member_count": len(selected), "bytes": sum(row["bytes"] for row in selected), "paths": [row["path"] for row in selected]}
    classification = {"kind": "a_c.application-source-classification/1", **common, "classes": groups, "derived_frame_sources": frame_data}
    sections, chunk_count = source_sections(root, primary, raw_files, selection["subject_uri"], app["generation"])
    objects = {"package-custody.json": custody, "source-manifest.json": semantic, "source-classification.json": classification,
               "release_tools/source-sections.json": {"kind": "a_c.stdo301.source-sections/1", "sections": sections}}
    names = list(objects) + ["source-selection.json", "SOURCE-READINESS.md", "source-contract.json", "source"]
    c.require(all(not (root / name).exists() and not (root / name).is_symlink() for name in names), "source freeze output exists; preserve its identity")
    # Exact inputs and generation partition are checked before creating any source output.
    for name, raw in raw_files.items():
        path = root / "source" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as stream:
            stream.write(raw)
    for name, value in objects.items():
        c.save(root / name, value)
    (root / "source-selection.json").write_bytes(raw_selection)
    (root / "SOURCE-READINESS.md").write_text(readiness(app, selection, primary), encoding="utf-8")
    names = list(objects) + ["source-selection.json", "SOURCE-READINESS.md"]
    contract = {"kind": "a_c.stdo301.frozen-source/1", "artifact": app["artifact"], "subject_id": selection["subject_uri"],
                "source": source, "builder": app["builder"], "generation": app["generation"],
                "application_sha256": c.sha((root / "application.json").read_bytes()),
                "implementation_manifest_sha256": c.sha((root / "implementation/manifest.json").read_bytes()),
                "metadata_sha256": {name: c.sha((root / name).read_bytes()) for name in names},
                "section_count": len(sections), "chunk_count": chunk_count,
                "canonical_native_manifest_bytes_checked": manifest_verified,
                "claim": "Exact selected native/source-candidate payload custody; no representation or semantic judgment."}
    c.save(root / "source-contract.json", contract)
    result = c.check_sources(root)
    return {"status": "source_frozen", "source_contract_sha256": c.sha((root / "source-contract.json").read_bytes()), **result}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    selected = commands.add_parser("freeze")
    selected.add_argument("--selection", type=Path, required=True)
    selected.add_argument("--selection-sha256", required=True)
    selected.add_argument("--git-repository", type=Path, required=True)
    check = commands.add_parser("check")
    check.add_argument("--source-contract-sha256")
    check.add_argument("--git-repository", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "freeze":
            result = freeze(ROOT, args.git_repository, args.selection, args.selection_sha256)
        else:
            result = c.check_sources(ROOT, args.source_contract_sha256)
            if args.git_repository:
                verify_selection(args.git_repository, c.load(ROOT / "source-selection.json"))
                result["exact_git_replay"] = True
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except (ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError) as error:
        print(json.dumps({"status": "refused", "reason": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
