"""Verify retained boundary evidence applicability using filesystem reads only."""
from pathlib import Path
import argparse
import hashlib
import importlib.metadata
import json
import os
import stat
import sys
import zlib

D = Path(__file__).resolve().parent
R = D.parents[5]
OLD = D.parent / "integration-003"
U = Path("/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-graphify-t008-upstream-w0b_fyxv/checkout")
COMMIT = "fe085cedddde3a18554f8749b230bfe47f3dcce7"
TREE = "6e11ed7cda0437ff12a29a328ca785e8915ddbc0"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_object(kind, data):
    return hashlib.sha1(kind.encode() + b" " + str(len(data)).encode() + b"\0" + data).digest()


def filesystem_tree(directory, rows):
    entries = []
    for path in directory.iterdir():
        if path.name in {".git", "__pycache__"} or path.suffix in {".pyc", ".pyo"}:
            continue
        name = os.fsencode(path.name)
        if path.is_symlink():
            mode = b"120000"
            digest = git_object("blob", os.fsencode(os.readlink(path)))
            key = name
            rows.append({"path": str(path.relative_to(U)), "kind": "symlink", "target": os.readlink(path), "target_not_followed": True})
        elif path.is_dir():
            mode = b"40000"
            digest = filesystem_tree(path, rows)
            key = name + b"/"
        elif path.is_file():
            mode = b"100755" if path.stat().st_mode & stat.S_IXUSR else b"100644"
            raw = path.read_bytes()
            digest = git_object("blob", raw)
            key = name
            rows.append({"path": str(path.relative_to(U)), "mode": mode.decode(), "sha256": hashlib.sha256(raw).hexdigest(), "blob_sha1": digest.hex(), "bytes": len(raw)})
        else:
            raise ValueError("Nonregular upstream member: " + str(path))
        entries.append((key, mode + b" " + name + b"\0" + digest))
    return git_object("tree", b"".join(row[1] for row in sorted(entries)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=["before", "after"])
    phase = parser.parse_args().phase
    report_path = OLD / "upstream-001/upstream-report.json"
    report = json.loads(report_path.read_bytes())
    assert report["status"] == "passed" and len(report["checks"]) == 9
    assert report["upstream"]["commit"] == COMMIT
    assert (U / ".git/HEAD").read_text().strip() == COMMIT
    commit_raw = zlib.decompress((U / ".git/objects" / COMMIT[:2] / COMMIT[2:]).read_bytes())
    assert hashlib.sha1(commit_raw).hexdigest() == COMMIT
    assert commit_raw.split(b"\0", 1)[1].splitlines()[0] == b"tree " + TREE.encode()
    upstream_rows = []
    actual_tree = filesystem_tree(U, upstream_rows).hex()
    assert actual_tree == TREE, "Upstream dependency tree changed"
    paths = {
        "qualification_script": (R / "a_c/build_tenants/graphify/test_env/check_upstream.py", report["qualification_script_sha256"]),
        "codec": (R / "a_c/build_tenants/graphify/code/ac_graph.py", report["codec_sha256"]),
        "fixture": (Path(report["fixture"]["path"]), report["fixture"]["sha256"]),
    }
    for relative, expected in report["upstream"]["entrypoint_sha256"].items():
        paths[relative] = (U / relative, expected)
    dependencies = []
    for label, (path, expected) in paths.items():
        assert path.is_file() and not path.is_symlink() and sha(path) == expected, label
        dependencies.append({"subject": label, "path": str(path), "sha256": expected, "unchanged": True})
    versions = {name: importlib.metadata.version(name) for name in report["upstream"]["packages"]}
    assert versions == report["upstream"]["packages"]
    old_python = json.loads((OLD / "EXECUTOR_ENVIRONMENT.json").read_bytes())["python"]
    python = Path(sys.executable).resolve()
    assert str(python) == old_python["path"] and sha(python) == old_python["sha256"] and sys.version == old_python["version"]
    value = {"schema": "a_c.T008.retained-upstream-applicability/1", "phase": phase,
        "carried_actual_report": {"path": str(report_path.relative_to(R)), "sha256": sha(report_path)},
        "carried_actual_checks": 9, "fresh_standalone_upstream_checks": 0,
        "commit": COMMIT, "pinned_tree": TREE, "actual_filesystem_tree": actual_tree,
        "upstream_source_rows": sorted(upstream_rows, key=lambda row: row["path"]),
        "dependencies": dependencies, "qualification_package_versions": versions, "python": old_python,
        "excluded_runtime_caches": [".git metadata", "__pycache__", "*.pyc", "*.pyo"],
        "scope": "Retained integration003 actual9-check result applies to unchanged checker/codec/fixture, exact complete upstream source tree and selected Python/package-version boundary. Fresh suite/strict/demo are separate. No new Git command, Graphify9 trial, install or network action."}
    if phase == "after":
        before = json.loads((D / "UPSTREAM_APPLICABILITY.before.json").read_bytes())
        assert {k: v for k, v in value.items() if k != "phase"} == {k: v for k, v in before.items() if k != "phase"}
    with (D / ("UPSTREAM_APPLICABILITY." + phase + ".json")).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({"phase": phase, "retained_actual_checks": 9, "fresh_standalone_upstream_checks": 0,
                      "dependency_tree_unchanged": True, "source_members": len(upstream_rows), "commit": COMMIT}))


if __name__ == "__main__":
    main()
