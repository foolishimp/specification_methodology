#!/usr/bin/env python3
"""Lossless public compiled-evidence transport; never executes proof artifacts."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile
import zlib

CHUNK = 1024 * 1024
MAX_RAW = 512 * 1024 * 1024
MAX_COMPRESSED = 95 * 1024 * 1024
MAX_MEMBERS = 128
MAX_TOTAL = 16 * 1024 * 1024 * 1024
HEX = re.compile(r"[0-9a-f]{64}\Z")
FORBIDDEN = {".cache", ".git", ".lake", ".toolchain", "private", "keys", "entries", "formal-origin-v1"}


def need(value, message):
    if not value:
        raise ValueError(message)


def encode(value):
    return (json.dumps(value, sort_keys=True, indent=2, allow_nan=False) + "\n").encode()


def decode(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            need(key not in result, "duplicate JSON key")
            result[key] = value
        return result
    def bad(value):
        raise ValueError("nonfinite JSON")
    return json.loads(raw.decode("utf-8"), object_pairs_hook=pairs, parse_constant=bad)


def raw_sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_identity(path):
    digest = hashlib.sha256(); size = 0
    with Path(path).open("rb") as stream:
        while block := stream.read(CHUNK):
            digest.update(block); size += len(block)
    return {"sha256": digest.hexdigest(), "bytes": size}


def rooted(value, must_exist=True):
    p = Path(value)
    need(".." not in p.parts, "noncanonical root")
    p = p.absolute()
    for parent in (p, *p.parents):
        need(not parent.is_symlink(), "symlink path ancestor")
    if must_exist:
        need(p.is_dir(), "root missing or not directory")
    return p


def relative(name, compiled=False):
    need(isinstance(name, str) and re.fullmatch(r"[A-Za-z0-9_.\-/]+", name), "invalid relative path")
    parts = name.split("/")
    need(all(x not in ("", ".", "..") for x in parts), "noncanonical member path")
    need(not ({x.casefold() for x in parts} & FORBIDDEN), "private/runtime path forbidden")
    if compiled:
        need(parts[0] in ("lean", "reuse") and name.endswith(".olean.private"),
             "only explicitly mapped public compiled proof members are supported")
    return name


def separate_roots(a, b):
    need(not a.is_relative_to(b) and not b.is_relative_to(a), "transport/restore roots overlap")
    for root, other in ((a, b), (b, a)):
        try: root.stat()
        except FileNotFoundError: continue
        for ancestor in (other, *other.parents):
            try: ancestor.stat()
            except FileNotFoundError: continue
            need(not root.samefile(ancestor), "transport/restore filesystem roots overlap")


def file_path(root, name, absent=False):
    relative(name)
    p = root
    for part in name.split("/"):
        p /= part
        need(not p.is_symlink(), "symlink member/ancestor")
    if p.exists():
        need(stat.S_ISREG(p.lstat().st_mode), "nonregular member")
    else:
        need(absent, "member missing: " + name)
    return p


def rows_valid(rows):
    need(isinstance(rows, list) and 0 < len(rows) <= MAX_MEMBERS, "member count bound")
    seen = set(); folded = {}
    for row in rows:
        need(isinstance(row, dict) and set(row) == {"path", "sha256", "bytes"}, "invalid member row")
        name = relative(row["path"], True)
        need(name not in seen, "duplicate member path"); seen.add(name)
        for count in range(1, len(name.split("/")) + 1):
            part = "/".join(name.split("/")[:count]); key = part.casefold()
            need(key not in folded or folded[key] == part, "case-colliding paths"); folded[key] = part
        need(isinstance(row["sha256"], str) and HEX.fullmatch(row["sha256"]), "invalid raw SHA-256")
        need(type(row["bytes"]) is int and 0 < row["bytes"] <= MAX_RAW, "raw member bound")
    need(sum(r["bytes"] for r in rows) <= MAX_TOTAL, "total restored byte bound")
    for name in seen:
        need(not any(parent.as_posix() in seen for parent in Path(name).parents), "file/directory path collision")


def load_selection(path, expected):
    raw = Path(path).read_bytes()
    need(raw_sha(raw) == expected, "selection digest mismatch")
    selection = decode(raw)
    need(isinstance(selection, dict) and set(selection) == {"schema", "files", "historical_pins"}, "invalid selection fields")
    need(selection["schema"] == "a_c.evidence-transport-selection/1", "unsupported selection")
    rows_valid(selection["files"])
    need(isinstance(selection["historical_pins"], list), "historical pins missing")
    return selection


def manifest_load(directory, expected):
    raw = file_path(directory, "MANIFEST.json").read_bytes()
    need(raw_sha(raw) == expected, "manifest digest mismatch")
    value = decode(raw)
    need(isinstance(value, dict) and set(value) ==
         {"schema", "selection_sha256", "files", "payloads", "encoding", "generator"}, "invalid manifest fields")
    need(value["schema"] == "a_c.evidence-transport/1", "unsupported manifest")
    need(value["encoding"] == "gzip-level9-mtime0-empty-filename", "unsupported encoding")
    rows_valid(value["files"])
    need(isinstance(value["selection_sha256"], str) and HEX.fullmatch(value["selection_sha256"]), "invalid selection pin")
    payloads = value["payloads"]; need(isinstance(payloads, list), "invalid payloads")
    selected = {r["sha256"]: r["bytes"] for r in value["files"]}
    need(all(selected[r["sha256"]] == r["bytes"] for r in value["files"]), "conflicting raw sizes")
    by_hash = {}
    for item in payloads:
        need(isinstance(item, dict) and set(item) == {"path", "raw_sha256", "raw_bytes", "sha256", "bytes"}, "invalid payload row")
        digest = item["raw_sha256"]
        need(digest in selected and digest not in by_hash, "unknown/duplicate payload")
        need(item["path"] == "members/" + digest + ".gz", "noncanonical compressed path")
        need(item["raw_bytes"] == selected[digest], "payload raw size differs")
        need(isinstance(item["sha256"], str) and HEX.fullmatch(item["sha256"]), "invalid compressed hash")
        need(type(item["bytes"]) is int and 0 < item["bytes"] < MAX_COMPRESSED, "compressed member exceeds safe remote bound")
        by_hash[digest] = item
    need(set(by_hash) == set(selected), "payload coverage differs from mapping")
    actual = set()
    members = directory / "members"
    need(members.is_dir() and not members.is_symlink(), "payload directory missing/symlink")
    for p in members.iterdir():
        need(p.is_file() and not p.is_symlink(), "unexpected compressed member")
        actual.add(p.relative_to(directory).as_posix())
    need(actual == {v["path"] for v in payloads}, "compressed population differs")
    return value, by_hash


def stream_payload(directory, item, target=None, compare=None):
    path = file_path(directory, item["path"])
    need(path.stat().st_size == item["bytes"], "compressed payload size changed")
    need(file_identity(path) == {"sha256": item["sha256"], "bytes": item["bytes"]}, "compressed payload changed")
    digest = hashlib.sha256(); size = 0
    with gzip.open(path, "rb") as stream:
        while block := stream.read(min(CHUNK, item["raw_bytes"] - size + 1)):
            size += len(block)
            need(size <= item["raw_bytes"] and size <= MAX_RAW, "decompressed output exceeds bound")
            digest.update(block)
            if compare is not None:
                need(compare.read(len(block)) == block, "decompressed bytes differ from original/target")
            if target is not None:
                target.write(block)
    if compare is not None:
        need(not compare.read(1), "original/target has extra bytes")
    need(size == item["raw_bytes"] and digest.hexdigest() == item["raw_sha256"], "decompressed identity mismatch")
    return size


def prepare(source_root, selection_path, selection_sha256, output):
    source = rooted(source_root); out = rooted(output, False)
    need(not out.exists() and out.parent.is_dir(), "transport destination must be fresh with existing parent")
    selection = load_selection(selection_path, selection_sha256)
    rows = selection["files"]; first = {}
    # All source identities are observed before creating compressed output.
    for row in rows:
        path = file_path(source, row["path"])
        need(file_identity(path) == {"sha256": row["sha256"], "bytes": row["bytes"]}, "selected source changed")
        first.setdefault(row["sha256"], row)
    out.mkdir(); (out / "members").mkdir(); payloads = []
    for digest, row in sorted(first.items()):
        name = "members/" + digest + ".gz"; dest = out / name
        with file_path(source, row["path"]).open("rb") as src, dest.open("xb") as sink:
            with gzip.GzipFile(filename="", fileobj=sink, mode="wb", compresslevel=9, mtime=0) as zipped:
                while block := src.read(CHUNK):
                    zipped.write(block)
                    need(sink.tell() < MAX_COMPRESSED, "compressed member exceeds safe remote bound; no splitting")
        identity = file_identity(dest)
        need(identity["bytes"] < MAX_COMPRESSED, "compressed member exceeds safe remote bound; no splitting")
        item = {"path": name, "raw_sha256": digest, "raw_bytes": row["bytes"], **identity}
        with file_path(source, row["path"]).open("rb") as src:
            stream_payload(out, item, compare=src)
        payloads.append(item)
    manifest = {"schema": "a_c.evidence-transport/1", "selection_sha256": selection_sha256,
                "files": rows, "payloads": payloads, "encoding": "gzip-level9-mtime0-empty-filename",
                "generator": {"python": sys.version.split()[0], "zlib": zlib.ZLIB_RUNTIME_VERSION,
                              "script_sha256": file_identity(Path(__file__))["sha256"]}}
    raw = encode(manifest)
    with (out / "MANIFEST.json").open("xb") as stream: stream.write(raw)
    return verify(out, raw_sha(raw), source)


def verify(directory, expected, originals=None):
    directory = rooted(directory); manifest, payloads = manifest_load(directory, expected)
    for item in payloads.values(): stream_payload(directory, item)
    compared = 0
    if originals is not None:
        source = rooted(originals)
        for row in manifest["files"]:
            with file_path(source, row["path"]).open("rb") as src:
                stream_payload(directory, payloads[row["sha256"]], compare=src)
            compared += 1
    return {"status": "bytes_verified", "manifest_sha256": expected, "files": len(manifest["files"]),
            "unique_payloads": len(payloads), "originals_compared_byte_for_byte": compared,
            "raw_mapped_bytes": sum(r["bytes"] for r in manifest["files"]),
            "compressed_unique_bytes": sum(r["bytes"] for r in payloads.values())}


def restore(directory, expected, destination):
    directory = rooted(directory); dest = rooted(destination, False)
    separate_roots(directory, dest)
    need(dest.is_dir() if dest.exists() else dest.parent.is_dir(), "restore parent/root unavailable")
    manifest, payloads = manifest_load(directory, expected)
    for item in payloads.values(): stream_payload(directory, item)
    existing = []; absent = []
    for row in manifest["files"]:
        path = file_path(dest, row["path"], True)
        if path.exists():
            with path.open("rb") as stream:
                stream_payload(directory, payloads[row["sha256"]], compare=stream)
            existing.append(row["path"])
        else:
            absent.append(row)
    dest.mkdir(exist_ok=True); restored = []
    for row in absent:
        path = file_path(dest, row["path"], True)
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(prefix=".evidence-restore-", dir=path.parent, delete=False) as stream:
                temporary = Path(stream.name)
                stream_payload(directory, payloads[row["sha256"]], target=stream)
                stream.flush(); os.fsync(stream.fileno()); os.fchmod(stream.fileno(), 0o644)
            # Hard-link publication is atomic and cannot replace an existing path.
            os.link(temporary, path)
            restored.append(row["path"])
        finally:
            if temporary is not None: temporary.unlink(missing_ok=True)
    return {"status": "restored_or_verified", "manifest_sha256": expected,
            "restored": restored, "already_present_identical": existing, "overwritten": []}


def main():
    parser = argparse.ArgumentParser(description=__doc__); sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("prepare")
    for name in ("source-root", "selection", "selection-sha256", "output"): create.add_argument("--" + name, required=True)
    for name in ("verify", "restore"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--transport", required=True); cmd.add_argument("--manifest-sha256", required=True)
        cmd.add_argument("--originals" if name == "verify" else "--destination", required=name == "restore")
    a = parser.parse_args()
    try:
        if a.command == "prepare": result = prepare(a.source_root, a.selection, a.selection_sha256, a.output)
        elif a.command == "verify": result = verify(a.transport, a.manifest_sha256, a.originals)
        else: result = restore(a.transport, a.manifest_sha256, a.destination)
        print(json.dumps(result, sort_keys=True)); return 0
    except (OSError, ValueError, KeyError, TypeError, EOFError, zlib.error) as exc:
        print(json.dumps({"status": "refused", "reason": str(exc)}, sort_keys=True), file=sys.stderr); return 2


if __name__ == "__main__":
    sys.exit(main())
