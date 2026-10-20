#!/usr/bin/env python3
"""Check this fixed source freeze; never replace files or select another cut.

Use --git-repository for an additional read-only replay of the exact Git blobs.
Only Python's standard library and read-only Git operations are used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys
from typing import Any


SOURCE_COMMIT = "35fb4824a064a84df5af214a0d0e2da597c18ac6"
PAYLOAD_COMMIT = "7d0516f37716298f038548c4152a1a697ce70f95"
PACKAGE_ROOT = "specification_methodology/v3/build_tenants/common"
PACKAGE_TREE = "7f2070b61c848b42b4dfb3af1e0ce53869de1aa1"
SUBJECT_ID = f"repo://stdo-v3-common/{SOURCE_COMMIT}"
EXPECTED_ALL = "740a3d1066a2b685c3985cf366f29dcb582c38e8ed98ddf5ee3a7576b993126d"
EXPECTED_PRIMARY = "7605efc789326de5f2d8568571a65113097cde54947743f622321193480af12f"
ROOT = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def safe_relative(path: str) -> str:
    value = PurePosixPath(path)
    require(bool(path) and not value.is_absolute() and value.as_posix() == path, "noncanonical source path")
    require(all(part not in ("", ".", "..") for part in value.parts), "unsafe source path")
    require("\\" not in path and "\x00" not in path, "unsafe source path characters")
    return path


def selection(path: str) -> str:
    if path.startswith("standards/frames/"):
        return "derived_frames"
    if path.startswith("standards/") or (path.startswith("plugins/") and path.endswith(".md")):
        return "primary_semantic"
    return "host_legal_release_metadata"


def inventory_rows(members: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [{key: row[key] for key in ("path", "bytes", "sha256")} for row in members]


def inventory_digest(members: list[dict[str, Any]]) -> str:
    return sha256(canonical(inventory_rows(members)))


def git(repository: Path, *arguments: str) -> bytes:
    return subprocess.check_output(["git", "--no-optional-locks", "-C", str(repository), *arguments])


def exact_git_members(repository: Path) -> list[tuple[dict[str, Any], bytes]]:
    tree = git(repository, "rev-parse", f"{SOURCE_COMMIT}:{PACKAGE_ROOT}").decode().strip()
    require(tree == PACKAGE_TREE, "exact source commit/package tree mismatch")
    payload_tree = git(repository, "rev-parse", f"{PAYLOAD_COMMIT}:{PACKAGE_ROOT}").decode().strip()
    require(payload_tree == PACKAGE_TREE, "payload commit/package tree mismatch")
    entries = git(repository, "ls-tree", "-rz", SOURCE_COMMIT, "--", PACKAGE_ROOT)
    result = []
    prefix = PACKAGE_ROOT + "/"
    for entry in entries.split(b"\x00"):
        if not entry:
            continue
        attributes, encoded_path = entry.split(b"\t", 1)
        mode, kind, blob = attributes.decode("ascii").split()
        source_path = encoded_path.decode("utf-8")
        require(source_path.startswith(prefix), "Git member escaped selected package")
        require(kind == "blob" and mode in ("100644", "100755"), "unsupported Git member type")
        path = safe_relative(source_path[len(prefix):])
        data = git(repository, "cat-file", "blob", blob)
        result.append(({"path": path, "bytes": len(data), "sha256": sha256(data),
                        "git_blob": blob, "git_mode": mode}, data))
    require(len(result) == 81 and sum(len(data) for _, data in result) == 3_298_515, "package extent mismatch")
    require(inventory_digest([row for row, _ in result]) == EXPECTED_ALL, "package inventory digest mismatch")
    return result


def frame_source_records(frame_inputs: dict[str, Any]) -> dict[str, Any]:
    return {
        "source_manifest_path": "standards/frames/FRAME_INPUTS.json",
        "standing": "Exact inherited owner routes; no fresh frame sufficiency or semantic judgment.",
        "frames": frame_inputs["frames"],
    }


def check(repository: Path | None = None) -> dict[str, Any]:
    custody = json.loads((ROOT / "package-custody.json").read_bytes())
    manifest = json.loads((ROOT / "source-manifest.json").read_bytes())
    classification = json.loads((ROOT / "source-classification.json").read_bytes())
    require(custody["subject_id"] == manifest["subject_id"] == classification["subject_id"] == SUBJECT_ID,
            "subject identity mismatch")
    source = custody["source"]
    require(source["commit"] == SOURCE_COMMIT and source["payload_commit"] == PAYLOAD_COMMIT
            and source["package_root"] == PACKAGE_ROOT and source["package_tree"] == PACKAGE_TREE,
            "source coordinates changed")
    require(manifest["source"] == source == classification["source"], "source-coordinate copies differ")
    members = custody["members"]
    paths = [safe_relative(row["path"]) for row in members]
    require(paths == sorted(paths) and len(paths) == len(set(paths)) == 81, "member order/uniqueness/count mismatch")
    require(custody["inventory_digest"] == EXPECTED_ALL == inventory_digest(members), "full inventory changed")
    require(custody["member_count"] == 81 and custody["bytes"] == 3_298_515, "custody totals changed")
    source_root = ROOT / "source"
    require(source_root.is_dir() and not source_root.is_symlink(), "missing or redirected frozen source root")
    discovered = []
    for path in source_root.rglob("*"):
        require(not path.is_symlink(), "symlink in frozen source")
        if path.is_file():
            discovered.append(path.relative_to(source_root).as_posix())
    require(sorted(discovered) == paths, "frozen source has missing or extra members")
    by_path = {}
    for member in members:
        path = member["path"]
        data = (source_root / path).read_bytes()
        require(len(data) == member["bytes"] and sha256(data) == member["sha256"], f"stale frozen bytes: {path}")
        blob = hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\x00" + data).hexdigest()
        require(blob == member["git_blob"], f"Git blob identity mismatch: {path}")
        require(member["git_mode"] in ("100644", "100755"), f"unsupported mode: {path}")
        if selection(path) == "primary_semantic":
            text = data.decode("utf-8")
            require("\r" not in text, f"ordinary generation requires LF source: {path}")
        by_path[path] = member
    primary = [row for row in members if selection(row["path"]) == "primary_semantic"]
    require(manifest["files"] == primary and len(primary) == 58, "semantic selection changed")
    require(manifest["member_count"] == 58 and manifest["bytes"] == 2_000_888, "semantic totals changed")
    require(manifest["inventory_digest"] == EXPECTED_PRIMARY == inventory_digest(primary), "semantic inventory changed")
    groups = {}
    for name, count, size in (("primary_semantic", 58, 2_000_888), ("derived_frames", 13, 1_270_927),
                              ("host_legal_release_metadata", 10, 26_700)):
        rows = [row for row in members if selection(row["path"]) == name]
        group = {"member_count": count, "bytes": size, "paths": [row["path"] for row in rows]}
        require(len(rows) == count and sum(row["bytes"] for row in rows) == size, f"classification totals differ: {name}")
        require(classification["classes"][name] == group, f"classification changed: {name}")
        groups[name] = {"member_count": count, "bytes": size}
    frame_inputs = json.loads((source_root / "standards/frames/FRAME_INPUTS.json").read_bytes())
    require(classification["derived_frame_sources"] == frame_source_records(frame_inputs), "frame owner routes changed")
    bindings = 0
    require(len(frame_inputs["frames"]) == 12, "frame population changed")
    for frame in frame_inputs["frames"]:
        frame_member = by_path[frame["path"]]
        require(frame["sha256"] == frame_member["sha256"] and frame["bytes"] == frame_member["bytes"], "frame bytes mismatch")
        for binding in frame.get("binds", []) + frame["routes"]:
            owner = binding["owner"]
            require(selection(owner) == "primary_semantic" and owner in by_path, "unavailable frame owner")
            require(binding["owner_sha256"] == by_path[owner]["sha256"], "stale frame owner identity")
            require(bool(binding["anchor"]) and len(binding["section_sha256"]) == 64, "incomplete inherited frame route")
            bindings += 1
    require(bindings == 223, "frame binding population changed")
    replayed = False
    if repository is not None:
        git_members = exact_git_members(repository)
        require([row for row, _ in git_members] == members, "Git custody rows changed")
        for row, data in git_members:
            require((source_root / row["path"]).read_bytes() == data, "exact Git replay bytes differ")
        replayed = True
    return {"kind": "a_c.application-source-freeze-check/1", "valid": True, "subject_id": SUBJECT_ID,
            "package_tree": PACKAGE_TREE, "member_count": 81, "bytes": 3_298_515,
            "inventory_digest": EXPECTED_ALL, "semantic_inventory_digest": EXPECTED_PRIMARY,
            "classes": groups, "preserved_frame_owner_bindings": bindings, "exact_git_replay": replayed,
            "claim": "Exact source custody and selection only; no interpretation fidelity, method acceptance or release qualification."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check local frozen bytes (the default; never writes)")
    parser.add_argument("--git-repository", type=Path, help="also compare with the fixed commit's immutable Git blobs")
    args = parser.parse_args()
    try:
        result = check(args.git_repository)
    except (OSError, ValueError, KeyError, TypeError, UnicodeError, subprocess.CalledProcessError) as error:
        print(json.dumps({"valid": False, "error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
