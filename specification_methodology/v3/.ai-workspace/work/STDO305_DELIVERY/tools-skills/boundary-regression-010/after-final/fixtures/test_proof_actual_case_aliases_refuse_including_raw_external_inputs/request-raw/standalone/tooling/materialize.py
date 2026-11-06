#!/usr/bin/env python3
"""Verify installed STDO tool sources and materialize an explicit writable copy."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import sys
import unicodedata
import zipfile

VERSION = "3.0.4"
SOURCE_COMMIT = "9c9626ffd20ea88a75ac8143802c13f4f828ec1c"
MEMBERS = {"README.md", "TOOLING.json", "sources.zip", "materialize.py"}
SOURCE_INVENTORY_SHA256 = "15b0dd94626158f282c7202413cfc580ca3451165fc4d62642ccf3fac9923c82"
MAX_BYTES = 64 * 1024 * 1024
MAX_FILES = 512


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(value):
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


def safe_path(name):
    require(isinstance(name, str) and name and not name.startswith("/"), "invalid source member path")
    require("\\" not in name and ":" not in name and not any(ord(c) < 32 for c in name), "unsafe source member path")
    require(all(part not in ("", ".", "..") and not part.endswith((" ", ".")) for part in name.split("/")), "source member traversal")
    require(str(PurePosixPath(name)) == name, "noncanonical source member")
    return name


def ordinary_path(path):
    path = Path(path).absolute()
    require(".." not in path.parts, "path traversal refused")
    for member in (path, *path.parents):
        require(not member.is_symlink(), "redirected path: " + str(member))
    return path


def source_bytes(files):
    """Validate every archive member before exposing bytes or writing a target."""
    require("TOOLING.json" in files, "required tooling member set differs")
    meta = json.loads(files["TOOLING.json"])
    current = meta.get("kind") == "stdo.installed-tooling/2"
    members = MEMBERS | {"SELECTION.json", "setup.py", "runtime.py", "payload_boundary.py"} if current else MEMBERS
    max_bytes, max_files = (512 * 1024 * 1024, 8192) if current else (MAX_BYTES, MAX_FILES)
    require(set(files) == members, "required tooling member set differs")
    if current:
        require(re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", meta.get("distribution_version", "")), "stable tooling version required")
        selected = json.loads(files["SELECTION.json"])
        require(selected.get("kind") == "stdo.current-tooling-selection/1" and
                selected.get("version") == meta["distribution_version"] and
                sha(files["SELECTION.json"]) == meta["selection_sha256"], "tooling selection differs")
        require(set(selected["owners"]) == {"a_c", "stdo_skills", "stdo_representation", "axiom_indexer"}, "required tool Product closure differs")
        expected = []
        for owner, unit in sorted(selected["owners"].items()):
            require(unit["version"] == meta["distribution_version"] and unit["members"], "tool Product version or inventory differs")
            for row in unit["members"]:
                require(row["path"].startswith(owner + "/"), "tool member crosses Product boundary")
                expected.append({"archive_path": row["path"], "bytes": row["bytes"], "sha256": row["sha256"], "git_mode": row["git_mode"]})
        expected.sort(key=lambda row: row["archive_path"])
        require(meta["sources"] == expected and meta["source_identity_sha256"] == selected["source_identity_sha256"], "tool source closure differs from selection")
        require(sha(encoded(expected)) == meta["source_inventory_sha256"], "tool inventory commitment differs")
    else:
        require(meta.get("kind") == "stdo.installed-tooling/1" and meta.get("distribution_version") == VERSION,
                "tooling distribution contract differs")
        require(meta.get("source_commit") == SOURCE_COMMIT, "tooling source selection differs")
        require(sha(encoded(meta["sources"])) == SOURCE_INVENTORY_SHA256, "source inventory commitment differs")
    require(set(meta["distribution_members"]) == members - {"TOOLING.json"}, "tool distribution inventory differs")
    for name in members - {"TOOLING.json"}:
        require(meta["distribution_members"][name] == {"bytes": len(files[name]), "sha256": sha(files[name])},
                "tooling distribution digest differs: " + name)
    rows = meta["sources"]
    require(isinstance(rows, list) and 0 < len(rows) <= max_files, "invalid source inventory size")
    expected, folded = {}, set()
    for row in rows:
        name = safe_path(row["archive_path"])
        key = unicodedata.normalize("NFC", name).casefold()
        require(name not in expected and key not in folded, "duplicate source inventory path")
        require(row["git_mode"] in ("100644", "100755") and re.fullmatch(r"[a-f0-9]{64}", row["sha256"]) is not None,
                "invalid source inventory identity")
        require(type(row["bytes"]) is int and 0 <= row["bytes"] <= max_bytes, "invalid source member size")
        expected[name] = row; folded.add(key)
    require(sum(row["bytes"] for row in rows) <= max_bytes, "source inventory exceeds bound")
    require(rows == sorted(rows, key=lambda row: row["archive_path"]), "source inventory order differs")
    for name in expected:
        require(not any(str(parent) in expected for parent in PurePosixPath(name).parents), "file/directory source collision")
    result = {}
    with zipfile.ZipFile(io.BytesIO(files["sources.zip"])) as archive:
        infos = archive.infolist()
        require(len(infos) == len(expected), "archive member count differs")
        for info in infos:
            name = safe_path(info.filename)
            require(name in expected and name not in result, "extra or duplicate archive member")
            row = expected[name]
            mode = info.external_attr >> 16
            require(info.create_system == 3 and stat.S_ISREG(mode) and stat.S_IMODE(mode) == int(row["git_mode"], 8) & 0o777,
                    "nonregular or mismatched archive mode")
            require(not info.flag_bits & 1 and info.compress_type == zipfile.ZIP_DEFLATED, "unsupported archive encoding")
            require(info.file_size == row["bytes"], "archive member size differs")
            raw = archive.read(info)
            require(sha(raw) == row["sha256"], "source member digest differs: " + name)
            result[name] = raw
    require(set(result) == set(expected), "archive member set differs")
    return meta, result


def read_bundle(root):
    root = ordinary_path(root)
    require(root.is_dir(), "missing installed tooling directory")
    paths = list(root.iterdir())
    require(all(not p.is_symlink() and p.is_file() and stat.S_ISREG(p.stat().st_mode) for p in paths),
            "nonregular installed tooling member")
    return {p.name: p.read_bytes() for p in paths}


def check(root):
    meta, sources = source_bytes(read_bundle(root))
    return {"status": "checked", "version": meta["distribution_version"],
            **({"source_commit": meta["source_commit"]} if "source_commit" in meta else {"source_identity_sha256": meta["source_identity_sha256"]}),
            "source_files": len(sources), "source_bytes": sum(map(len, sources.values())),
            "archive_sha256": meta["distribution_members"]["sources.zip"]["sha256"]}


def verify_tree(bundle, destination):
    meta, expected = source_bytes(read_bundle(bundle))
    destination = ordinary_path(destination)
    require(destination.is_dir(), "missing materialized tree")
    actual = {}
    expected_dirs = {str(parent) for name in expected for parent in PurePosixPath(name).parents if str(parent) != "."}
    actual_dirs = set()
    for path in destination.rglob("*"):
        require(not path.is_symlink(), "redirected materialized member")
        if path.is_dir():
            actual_dirs.add(path.relative_to(destination).as_posix())
            continue
        require(stat.S_ISREG(path.stat().st_mode), "nonregular materialized member")
        actual[path.relative_to(destination).as_posix()] = path.read_bytes()
    require(actual == expected and actual_dirs == expected_dirs, "materialized source bytes differ")
    for row in meta["sources"]:
        require(stat.S_IMODE((destination / row["archive_path"]).stat().st_mode) == int(row["git_mode"], 8) & 0o777,
                "materialized source mode differs")
    return {"status": "checked", "source_files": len(actual), "destination": str(destination)}


def materialize(bundle, destination):
    bundle, destination = ordinary_path(bundle), ordinary_path(destination)
    # A caller must choose an absent sibling/outside directory with an existing
    # nonredirected parent. Never write beneath the immutable installed release.
    require(not destination.exists(), "materialization destination already exists")
    require(destination.parent.is_dir(), "materialization parent must already exist")
    protected = bundle.parent.parent if bundle.parent.name.casefold() == "standards" else bundle
    require(not destination.is_relative_to(protected) and not protected.is_relative_to(destination),
            "materialization overlaps installed payload")
    # Spelling is not filesystem identity. Case/Unicode aliases on an installed
    # volume must not let a caller materialize beneath the protected release.
    # Symlink ancestors were already refused; compare every existing ancestor
    # before creating the absent output (also covers mount aliases).
    require(not any(parent.exists() and os.path.samefile(parent, protected)
                    for parent in destination.parents), "materialization overlaps installed payload by filesystem identity")
    meta, sources = source_bytes(read_bundle(bundle))
    modes = {row["archive_path"]: int(row["git_mode"], 8) & 0o777 for row in meta["sources"]}
    destination.mkdir(mode=0o700, exist_ok=False)
    try:
        for name, raw in sources.items():
            path = destination / name
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("xb") as stream:
                stream.write(raw)
            path.chmod(modes[name])
        result = verify_tree(bundle, destination)
    except BaseException:
        shutil.rmtree(destination)
        raise
    result.update(status="materialized", version=meta["distribution_version"],
                  **({"source_commit": meta["source_commit"]} if "source_commit" in meta else {"source_identity_sha256": meta["source_identity_sha256"]}),
                  notice="Source custody only; select dependencies, work and authority explicitly.")
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, default=Path(__file__).resolve().parent)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check")
    for verb in ("materialize", "verify-tree"):
        commands.add_parser(verb).add_argument("--destination", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "check":
            result = check(args.bundle)
        elif args.command == "materialize":
            result = materialize(args.bundle, args.destination)
        else:
            result = verify_tree(args.bundle, args.destination)
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile, RuntimeError) as exc:
        print(json.dumps({"status": "refused", "reason": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
