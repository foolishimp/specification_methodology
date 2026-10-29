#!/usr/bin/env python3
"""Explicit-inventory source packaging; no installer, compiler or gate invocation.

Inputs and outputs must be quiescent while a command runs. Hashes establish
correspondence to the caller's trusted selection, not its authorship or approval.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import tarfile

MANIFEST = "SOURCE_PACKAGE.json"
MAX_FILES = 512
MAX_FILE = 64 * 1024 * 1024
MAX_TOTAL = 256 * 1024 * 1024
MAX_MANIFEST = 2 * 1024 * 1024
BANNED = {".cache", ".lake", ".toolchain", ".git", "__pycache__", ".DS_Store",
          "private", "entries", "temp", "tmp"}
BANNED_SUFFIX = (".pyc", ".pyo", ".olean", ".olean.private", ".olean.server",
                 ".ir", ".ir.sig", ".dylib", ".so", ".o", ".a", ".key", ".pem")
HASH = re.compile(r"[0-9a-f]{64}\Z")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2,
                       allow_nan=False) + "\n").encode()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode()


def decode(raw):
    def pairs(items):
        out = {}
        for key, value in items:
            require(key not in out, "duplicate JSON key: " + key)
            out[key] = value
        return out

    def bad_number(value):
        raise ValueError("non-finite JSON: " + value)

    return json.loads(raw.decode("utf-8"), object_pairs_hook=pairs,
                      parse_constant=bad_number)


def relative(value):
    require(isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9_.\-/]+", value),
            "path must be a simple POSIX relative path")
    pieces = value.split("/")
    require(all(p not in ("", ".", "..") for p in pieces), "noncanonical path")
    require(not PurePosixPath(value).is_absolute(), "absolute path")
    require(not (set(pieces) & BANNED), "excluded runtime/private path: " + value)
    require(not value.endswith(BANNED_SUFFIX), "excluded binary/key: " + value)
    require(not any("origin-selection" in p or p.startswith("origin-key") for p in pieces),
            "excluded private origin selection: " + value)
    return value


def paths_unique(names):
    seen = set()
    components = {}
    for name in names:
        relative(name)
        require(name not in seen, "duplicate inventory path: " + name)
        seen.add(name)
        for i in range(1, len(name.split("/")) + 1):
            prefix = "/".join(name.split("/")[:i])
            folded = prefix.casefold()
            require(folded not in components or components[folded] == prefix,
                    "case-colliding path: " + prefix)
            components[folded] = prefix
    for name in seen:
        require(not any(parent.as_posix() in seen for parent in PurePosixPath(name).parents
                        if parent.as_posix() != "."), "file/directory collision: " + name)


def regular(root, name):
    relative(name)
    path = root
    parts = name.split("/")
    for i, part in enumerate(parts):
        path = path / part
        mode = path.lstat().st_mode
        require(not stat.S_ISLNK(mode), "symlink is forbidden: " + str(path))
        require(stat.S_ISREG(mode) if i == len(parts) - 1 else stat.S_ISDIR(mode),
                "not a regular file/path: " + str(path))
    require(path.stat().st_size <= MAX_FILE, "member exceeds byte bound")
    return path


def root_path(value, exists=True):
    p = Path(value).absolute()
    # Reject symlinks in existing ancestors, including output parent chains.
    for q in (p, *p.parents):
        if q.exists() or q.is_symlink():
            require(not q.is_symlink(), "symlink ancestor: " + str(q))
    if exists:
        require(p.is_dir(), "root is not a directory: " + str(p))
    return p


def separate(a, b):
    require(not a.is_relative_to(b) and not b.is_relative_to(a),
            "overlapping source/bundle/output paths")


def fresh_file(path, raw):
    path = root_path(path, False)
    require(path.parent.is_dir(), "output parent does not exist")
    with path.open("xb") as stream:
        stream.write(raw)


def validate_freeze(value):
    require(isinstance(value, dict) and set(value) ==
            {"schema", "kind", "selection_ref", "runtime_identity"}, "bad freeze fields")
    require(value["schema"] == "a_c.lean.package-freeze/1", "unsupported freeze")
    require(value["kind"] in ("candidate", "synthetic"), "bad freeze kind")
    require(isinstance(value["selection_ref"], str) and value["selection_ref"],
            "exact external selection reference required")
    identity = value["runtime_identity"]
    require(isinstance(identity, dict) and set(identity) == {"sha256", "pins"},
            "bad runtime identity")
    require(isinstance(identity["pins"], dict), "bad runtime pins")
    require(identity["sha256"] == sha(canonical(identity["pins"])), "runtime identity mismatch")
    require(value["kind"] == "synthetic" or bool(identity["pins"]), "candidate pins absent")
    for name, digest in identity["pins"].items():
        relative(name)
        require(isinstance(digest, str) and HASH.fullmatch(digest), "bad runtime pin")


def validate_manifest(value):
    require(isinstance(value, dict) and set(value) ==
            {"schema", "freeze", "freeze_sha256", "files"}, "bad package manifest fields")
    require(value["schema"] == "a_c.lean.source-package/1", "unsupported package manifest")
    validate_freeze(value["freeze"])
    require(value["freeze_sha256"] == sha(canonical(value["freeze"])), "freeze identity mismatch")
    rows = value["files"]
    require(isinstance(rows, list) and 0 < len(rows) <= MAX_FILES, "inventory count bound")
    total = 0
    for row in rows:
        require(isinstance(row, dict) and set(row) == {"source", "path", "sha256", "bytes", "role"},
                "bad inventory row")
        relative(row["source"]); relative(row["path"])
        require(row["path"] != MANIFEST, "reserved manifest destination")
        require(isinstance(row["role"], str) and row["role"], "missing inventory role")
        require(isinstance(row["sha256"], str) and HASH.fullmatch(row["sha256"]), "bad member hash")
        require(type(row["bytes"]) is int and 0 <= row["bytes"] <= MAX_FILE, "member byte bound")
        total += row["bytes"]
    require(total <= MAX_TOTAL, "total byte bound")
    paths_unique([r["path"] for r in rows]); paths_unique([r["source"] for r in rows])
    by_source = {r["source"]: r for r in rows}
    for name, digest in value["freeze"]["runtime_identity"]["pins"].items():
        source = "a_c/build_tenants/lean/" + name
        require(source in by_source and by_source[source]["sha256"] == digest
                and by_source[source]["path"] == source,
                "runtime identity absent/changed/remapped in package: " + name)
    return value


def select(source_root, plan_file, freeze_file, output):
    root = root_path(source_root)
    plan = decode(Path(plan_file).read_bytes()); freeze = decode(Path(freeze_file).read_bytes())
    require(isinstance(plan, dict) and set(plan) == {"schema", "state", "entries", "closed_directories"},
            "bad explicit plan fields")
    require(plan["schema"] == "a_c.lean.package-plan/1" and plan["state"] == "proposed",
            "bad explicit plan")
    validate_freeze(freeze)
    rows = []
    for entry in plan["entries"]:
        require(isinstance(entry, dict) and set(entry) == {"source", "path", "role"}, "bad plan entry")
        raw = regular(root, entry["source"]).read_bytes()
        rows.append(entry | {"sha256": sha(raw), "bytes": len(raw)})
    # Enumeration detects omissions; it never adds an unselected member.
    selected_sources = {r["source"] for r in rows}
    for directory in plan["closed_directories"]:
        relative(directory)
        base = root / directory
        require(base.is_dir() and not base.is_symlink(), "closed directory missing/symlink")
        for current, dirs, files in os.walk(base, followlinks=False):
            for name in dirs:
                p = Path(current) / name
                require(not p.is_symlink(), "symlink in closed source namespace")
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for name in files:
                p = Path(current) / name
                require(p.relative_to(root).as_posix() in selected_sources,
                        "unselected source; revise explicit inventory: " + str(p))
    result = {"schema": "a_c.lean.source-package/1", "freeze": freeze,
              "freeze_sha256": sha(canonical(freeze)), "files": sorted(rows, key=lambda r: r["path"])}
    validate_manifest(result)
    raw = encode(result); require(len(raw) <= MAX_MANIFEST, "manifest byte bound")
    fresh_file(output, raw)
    return {"manifest_sha256": sha(raw), "files": len(rows), "bytes": sum(r["bytes"] for r in rows)}


def load_manifest(raw, expected):
    require(isinstance(expected, str) and HASH.fullmatch(expected), "trusted manifest SHA-256 required")
    require(len(raw) <= MAX_MANIFEST and sha(raw) == expected, "manifest byte/hash mismatch")
    return validate_manifest(decode(raw))


def checked_data(root, row, source=False):
    raw = regular(root, row["source"] if source else row["path"]).read_bytes()
    require(len(raw) == row["bytes"] and sha(raw) == row["sha256"], "member changed: " + row["path"])
    return raw


def tree_files(root):
    files = set(); directories = set()
    for current, dirs, names in os.walk(root, followlinks=False):
        for name in dirs:
            p = Path(current) / name
            require(not p.is_symlink(), "symlink directory in bundle")
            directories.add(p.relative_to(root).as_posix())
        for name in names:
            p = Path(current) / name
            relative(p.relative_to(root).as_posix())
            require(stat.S_ISREG(p.lstat().st_mode), "nonregular bundle member")
            files.add(p.relative_to(root).as_posix())
    return files, directories


def verify_tree(tree, expected):
    root = root_path(tree)
    raw = regular(root, MANIFEST).read_bytes(); manifest = load_manifest(raw, expected)
    expected_files = {MANIFEST, *(r["path"] for r in manifest["files"])}
    expected_dirs = {p.as_posix() for name in expected_files for p in PurePosixPath(name).parents
                     if p.as_posix() != "."}
    files, directories = tree_files(root)
    require(files == expected_files and directories == expected_dirs, "tree differs from exact inventory")
    for row in manifest["files"]:
        checked_data(root, row)
    return {"status": "source_bytes_verified", "manifest_sha256": expected, "files": len(files)}


def build(source_root, selection, expected, output):
    root = root_path(source_root); out = root_path(output, False)
    separate(root, out); require(not out.exists(), "bundle destination exists")
    require(out.parent.is_dir(), "bundle parent does not exist")
    raw = Path(selection).read_bytes(); manifest = load_manifest(raw, expected)
    payload = [(row, checked_data(root, row, True)) for row in manifest["files"]]
    out.mkdir()
    for row, data in payload:
        dest = out / row["path"]; dest.parent.mkdir(parents=True, exist_ok=True)
        fresh_file(dest, data)
    fresh_file(out / MANIFEST, raw)
    return verify_tree(out, expected)


def archive(tree, expected, output):
    root = root_path(tree); out = root_path(output, False)
    separate(root, out); require(not out.exists(), "archive destination exists")
    verify_tree(root, expected)
    # Inventory is closed and materialized before opening any output.
    names = sorted(tree_files(root)[0])
    payload = [(name, regular(root, name).read_bytes()) for name in names]
    with out.open("xb") as stream:
        with tarfile.open(fileobj=stream, mode="w", format=tarfile.PAX_FORMAT) as tar:
            for name, raw in payload:
                info = tarfile.TarInfo(name)
                info.size = len(raw); info.mode = 0o644; info.mtime = 0
                info.uid = info.gid = 0; info.uname = info.gname = ""
                tar.addfile(info, io.BytesIO(raw))
    inspect_archive(out, expected)
    return {"status": "source_archive_created", "manifest_sha256": expected,
            "archive_sha256": sha(out.read_bytes()), "bytes": out.stat().st_size}


def inspect_archive(path, expected):
    path = root_path(path, False)
    require(path.is_file() and path.stat().st_size <= MAX_TOTAL + 16 * 1024 * 1024,
            "archive unavailable/oversized")
    blobs = {}; total = 0; end_of_members = 0
    with tarfile.open(path, "r:") as tar:
        for member in tar:
            name = relative(member.name)
            require(member.type == tarfile.REGTYPE, "archive contains nonregular member")
            require(name not in blobs and len(blobs) <= MAX_FILES, "duplicate/excess archive member")
            require(0 <= member.size <= (MAX_MANIFEST if name == MANIFEST else MAX_FILE), "archive member bound")
            total += member.size; require(total <= MAX_TOTAL + MAX_MANIFEST, "archive total byte bound")
            stream = tar.extractfile(member); require(stream is not None, "unreadable archive member")
            raw = stream.read(member.size + 1)
            require(len(raw) == member.size, "truncated archive member")
            blobs[name] = raw
            end_of_members = member.offset_data + ((member.size + 511) // 512) * 512
    with path.open("rb") as stream:
        stream.seek(end_of_members); padding = stream.read()
    require(len(padding) >= 1024 and not any(padding), "noncanonical tar ending/trailing payload")
    paths_unique(blobs)
    require(MANIFEST in blobs, "archive manifest absent")
    manifest = load_manifest(blobs[MANIFEST], expected)
    require(set(blobs) == {MANIFEST, *(r["path"] for r in manifest["files"])}, "archive inventory mismatch")
    for row in manifest["files"]:
        raw = blobs[row["path"]]
        require(len(raw) == row["bytes"] and sha(raw) == row["sha256"], "archive member mismatch")
    return blobs


def extract(path, expected, output):
    archive_path = root_path(path, False); out = root_path(output, False)
    separate(archive_path, out); require(not out.exists(), "extraction destination exists")
    require(out.parent.is_dir(), "extraction parent does not exist")
    blobs = inspect_archive(archive_path, expected)  # Validate every member before writing.
    out.mkdir()
    for name, raw in blobs.items():
        dest = out / name; dest.parent.mkdir(parents=True, exist_ok=True)
        fresh_file(dest, raw)
    return verify_tree(out, expected)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("select")
    for name in ("source-root", "plan", "freeze", "output"):
        p.add_argument("--" + name, required=True)
    for name in ("build", "verify-tree", "archive", "verify-archive", "extract"):
        p = sub.add_parser(name); p.add_argument("--manifest-sha256", required=True)
        if name == "build":
            p.add_argument("--source-root", required=True); p.add_argument("--selection", required=True)
        else:
            p.add_argument("--tree" if name in ("verify-tree", "archive") else "--archive", required=True)
        if name in ("build", "archive", "extract"):
            p.add_argument("--output", required=True)
    a = parser.parse_args()
    try:
        if a.command == "select": result = select(a.source_root, a.plan, a.freeze, a.output)
        elif a.command == "build": result = build(a.source_root, a.selection, a.manifest_sha256, a.output)
        elif a.command == "verify-tree": result = verify_tree(a.tree, a.manifest_sha256)
        elif a.command == "archive": result = archive(a.tree, a.manifest_sha256, a.output)
        elif a.command == "extract": result = extract(a.archive, a.manifest_sha256, a.output)
        else:
            blobs = inspect_archive(a.archive, a.manifest_sha256)
            result = {"status": "source_archive_verified", "manifest_sha256": a.manifest_sha256,
                      "files": len(blobs)}
        print(json.dumps(result, sort_keys=True))
        return 0
    except (OSError, ValueError, KeyError, TypeError, tarfile.TarError) as exc:
        print(json.dumps({"status": "refused", "reason": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
