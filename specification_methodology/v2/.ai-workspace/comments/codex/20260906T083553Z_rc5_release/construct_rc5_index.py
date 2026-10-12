"""Bind the reviewed authored program to the exact RC5 Install and replay views."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[5]
PROOF = Path(__file__).resolve().parent
REP = ROOT / "stdo_representation"
INSTALL = Path("/Users/jim/Library/Application Support/STDO/releases/v2.5.0-rc.5")
TARGET = REP / "build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.5"
PREVIOUS = REP / "dogfood/t009-frame-projection/run-003/axiomatic-program.json"
OLD_PREFIX = "repo://stdo-t009-construction/86370472a9b7eabe52933d5bcd8093bb94435392420d38e8d145976317a4d2ca/"
NEW_PREFIX = "stdo://releases/v2.5.0-rc.5/"
MECHANIC = ROOT / "axiom_indexer/build_tenants/core/code/ac.py"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def put(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def rewrite(value, old, new):
    if isinstance(value, str):
        return value.replace(old, new)
    if isinstance(value, list):
        return [rewrite(v, old, new) for v in value]
    if isinstance(value, dict):
        return {k: rewrite(v, old, new) for k, v in value.items()}
    return value


assert sha(PREVIOUS) == "c39896e9c562bffe1f0632d3eb0dbefa71ab2aef5c92a5f576776408d6689a1d"
assert sha(MECHANIC) == "87c43389c619d9ca0e2d930a10e471a17545be9a0394d1c0f47db7e8e2c6d931"
assert sha(INSTALL / "manifest.json") == "3fb89aeb80c65403debf1eba1705fde614556520bf1ce1a08a39033b6d98a50f"
installed = json.loads((INSTALL / "manifest.json").read_text())
for row in installed["standards"]["members"]:
    assert sha(INSTALL / "standards" / row["path"]) == row["sha256"]
    assert sha(REP / "dogfood/t009-frame-projection/run-001/source/standards" / row["path"]) == row["sha256"]

old = json.loads(PREVIOUS.read_text())
program = rewrite(old, OLD_PREFIX, NEW_PREFIX)
program["uri"] = "urn:stdo-representation:program:a-c-text:stdo-v2.5.0-rc.5"
restored = rewrite(program, NEW_PREFIX, OLD_PREFIX)
restored["uri"] = old["uri"]
assert restored == old
put(TARGET / "axiomatic-program.json", program)
put(PROOF / "rc5-bindings.json", {"kind": "axiom-indexer.binding-set", "schema_version": 1,
    "bindings": [{"uri_prefix": NEW_PREFIX, "path": str(INSTALL)}]})

commands = []


def run(label, args):
    argv = [sys.executable, str(MECHANIC), *args]
    result = subprocess.run(argv, capture_output=True, text=True)
    commands.append({"label": label, "argv": argv, "exit_code": result.returncode})
    (PROOF / f"index-{label}.stdout.txt").write_text(result.stdout)
    (PROOF / f"index-{label}.stderr.txt").write_text(result.stderr)
    if result.returncode:
        raise RuntimeError(f"{label}: {result.stderr or result.stdout}")


common = ["--program", str(TARGET / "axiomatic-program.json"), "--bindings", str(PROOF / "rc5-bindings.json")]
run("validate", ["validate", *common, "--output", str(TARGET / "validation-report.json"), "--emit-map", str(TARGET / "logical-constraint-map.json")])
for name, frames in [("worker", ["worker"]), ("reviewer", ["reviewer"]), ("combined", ["worker", "reviewer"])]:
    for mode in ["reference-only", "materialized"]:
        path = PROOF / "projections" / f"{name}-{mode}.json"
        path.parent.mkdir(exist_ok=True)
        flags = [part for frame in frames for part in ["--frame-index", f"urn:stdo-representation:frame-index:t009:complete-update-{frame}"]]
        run(f"{name}-{mode}", ["project", *common, "--map", str(TARGET / "logical-constraint-map.json"), *flags, "--mode", mode, "--output", str(path)])

release = dict(installed["release"])
release.update({"uri": NEW_PREFIX, "installed_manifest_sha256": sha(INSTALL / "manifest.json"),
    "standards_member_count": installed["standards"]["member_count"],
    "standards_member_set_sha256": installed["standards"]["member_set_sha256"],
    "standards_members": installed["standards"]["members"]})
put(TARGET / "source-corpus.json", {"kind": "stdo-representation.source-corpus", "schema_version": 1,
    "representation_version": "2.5.0-rc.5", "source_release": release})
put(PROOF / "index-commands.json", commands)
put(PROOF / "index-conservation.json", {"kind": "stdo.rc5-index-conservation", "predecessor_program": str(PREVIOUS.relative_to(ROOT)), "predecessor_program_sha256": sha(PREVIOUS),
    "permitted_changes": {"source_uri_prefix": {"from": OLD_PREFIX, "to": NEW_PREFIX}, "program_identity": program["uri"]},
    "inverse_transform_equals_authored_predecessor": restored == old, "source_members_identical": 52,
    "axiom_executable_sha256": sha(MECHANIC), "generated_files": {str(p.relative_to(ROOT)): sha(p) for p in sorted(TARGET.iterdir()) if p.is_file()},
    "claim": "Exact source and mechanical identity rebinding only; prior semantic authoring/review remains applicable. Native package behavior is assessed separately."})
print(json.dumps({"program": sha(TARGET / "axiomatic-program.json"), "map": sha(TARGET / "logical-constraint-map.json"), "source_members": 52, "views": 6, "conservation": True}))
