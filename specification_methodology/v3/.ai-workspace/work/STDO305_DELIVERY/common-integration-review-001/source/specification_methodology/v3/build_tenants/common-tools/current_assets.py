"""Exact, regular-file inputs shared by current native documentation builders."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import unicodedata


def require(value, reason):
    if not value:
        raise ValueError(reason)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


def canonical_sha(value):
    return sha(json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True,
                          separators=(",", ":")).encode())


def digest(value):
    require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value), "invalid SHA256")
    return value


def version(value):
    require(isinstance(value, str) and re.fullmatch(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)", value),
            "exact stable distribution version required")
    return value


def name(value):
    require(isinstance(value, str) and value and not value.startswith("/"), "relative member path required")
    require("\\" not in value and ":" not in value and not any(ord(c) < 32 for c in value), "unsafe member path")
    require(all(p not in ("", ".", "..") and not p.endswith((" ", ".")) for p in value.split("/")), "member traversal")
    require(str(PurePosixPath(value)) == value, "noncanonical member path")
    return value


def ordinary(path):
    path = Path(path).absolute()
    require(".." not in path.parts, "path traversal")
    for part in (path, *path.parents):
        require(not part.is_symlink(), "redirected path: " + str(part))
    return path


def regular(path):
    path = ordinary(path)
    require(stat.S_ISREG(path.stat().st_mode), "nonregular file: " + str(path))
    return path.read_bytes()


def pinned(root, ref, *, json_value=False):
    raw = regular(ordinary(root) / name(ref["path"]))
    require(sha(raw) == digest(ref["sha256"]), "selected input differs: " + ref["path"])
    if "bytes" in ref:
        require(len(raw) == ref["bytes"], "selected input length differs")
    return json.loads(raw) if json_value else raw


def selection(root, path, expected, kind):
    path = ordinary(path)
    raw = regular(path)
    require(sha(raw) == digest(expected), "selection digest differs")
    value = json.loads(raw)
    require(value.get("kind") == kind, "selection profile differs")
    version(value["version"])
    return value


def inventory(files):
    folded = set()
    for key in files:
        name(key)
        folded_key = unicodedata.normalize("NFC", key).casefold()
        require(folded_key not in folded, "case/Unicode member alias")
        folded.add(folded_key)
        require(not any(str(p) in files for p in PurePosixPath(key).parents), "file/directory member collision")
    return [{"path": p, "bytes": len(raw), "sha256": sha(raw)} for p, raw in sorted(files.items())]


def read_tree(root):
    root = ordinary(root)
    require(root.is_dir(), "missing payload directory")
    files = {}
    for path in root.rglob("*"):
        require(not path.is_symlink(), "redirected payload member")
        if path.is_dir():
            continue
        files[path.relative_to(root).as_posix()] = regular(path)
    inventory(files)
    return files


def disjoint(output, protected):
    output, protected = ordinary(output), ordinary(protected)
    require(not output.is_relative_to(protected) and not protected.is_relative_to(output), "output overlaps protected input")
    # Existing ancestors detect volume case aliases even when the new leaf does not exist.
    for a in (output, *output.parents):
        if a.exists() and protected.exists():
            require(not os.path.samefile(a, protected), "output aliases protected input")
    for a in (protected, *protected.parents):
        if a.exists() and output.exists():
            require(not os.path.samefile(a, output), "protected input aliases output")


def write_tree(output, files):
    output = ordinary(output)
    require(not output.exists(), "preserve existing output")
    inventory(files)
    output.mkdir(parents=True, exist_ok=False)
    for key, raw in sorted(files.items()):
        path = output / key
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as stream:
            stream.write(raw)


def source_freeze(raw, selected_version):
    value = json.loads(raw)
    require(value.get("kind") == "stdo.semantic-source-freeze/1" and value.get("version") == selected_version,
            "source freeze version/profile differs")
    identity = {k: value[k] for k in ("version", "basis_uri", "members", "native_contracts")}
    require(value["basis_uri"] == f"stdo://releases/v{selected_version}/" and
            sha(encoded(identity)) == value["source_identity_sha256"], "semantic source identity differs")
    members = value["members"] + value["native_contracts"]
    require(members and len({name(r["path"]) for r in members}) == len(members), "invalid semantic source closure")
    for row in members:
        digest(row["sha256"])
        require(type(row["bytes"]) is int and row["bytes"] >= 0, "invalid semantic member length")
    return value


def model_identity(raw):
    value = json.loads(raw)
    require(isinstance(value["id"], str) and isinstance(value["profile"], str), "model identity missing")
    return {"id": value["id"], "sha256": canonical_sha(value), "profile": value["profile"]}


def source_model(freeze, model, manifest, prefix):
    prefix = name(prefix)
    expected = sorted(({"path": prefix + "/" + r["path"], "bytes": r["bytes"], "sha256": r["sha256"]}
                       for r in freeze["members"] + freeze["native_contracts"]), key=lambda r: r["path"])
    require(manifest["files"] == expected, "source manifest is not the complete semantic input")
    require(model["basis"]["subject"]["sha256"] == canonical_sha(expected), "model source identity differs")
    return expected
