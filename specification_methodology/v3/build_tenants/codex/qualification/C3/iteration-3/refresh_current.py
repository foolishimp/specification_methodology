"""Refresh current derivatives without changing any historical qualification.

The historical helpers are reused as algorithms, with all output locations bound
to this iteration. Refreshing coordinates supplies no semantic acceptance.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[2]
PACKAGE = TENANT / "successor"
PREVIOUS = HERE.parent
COMMON_INPUT = "cae6fe366395148558efb84c85501b768f6593fc"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read(path):
    return json.loads(path.read_text())


def write(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def refresh_views():
    target = HERE / "FRAME_INPUTS.json"
    index = read(target if target.exists() else PREVIOUS / "FRAME_INPUTS.json")
    # Every existing frame keeps its domain-specific owners. The shared law
    # replaces those owners' repeated bodies and must be available to the reader.
    for frame in index["frames"]:
        route = {"owner": "standards/TRANSFORMATION_LIBRARY.md", "anchor": "contract-application"}
        if not any(r["owner"] == route["owner"] and r["anchor"] == route["anchor"] for r in frame["routes"]):
            frame["routes"].append(route)
    index["standing"] = "Current iteration 3 source-bound views; sufficiency requires task-specific evidence."
    index["input_commit"] = COMMON_INPUT
    write("FRAME_INPUTS.json", index)
    helper = load_module("i3_views", PREVIOUS / "refresh_views.py")
    helper.base, helper.root, helper.std = TENANT, PACKAGE, PACKAGE / "standards"
    helper.__file__ = str(HERE / "refresh_views.py")
    helper.refresh()


def inventory(source_commit=None):
    previous = read(PREVIOUS / "CANDIDATE.json")
    members = {row["path"]: row for row in previous["members"]}
    repo = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], cwd=TENANT, text=True).strip())
    if source_commit:
        source_commit = subprocess.check_output(["git", "rev-parse", source_commit + "^{commit}"], cwd=repo, text=True).strip()
    rows = []
    for path in sorted(PACKAGE.rglob("*")):
        if not path.is_file():
            continue
        if source_commit:
            frozen = subprocess.check_output(["git", "show", source_commit + ":" + str(path.relative_to(repo))], cwd=repo)
            if frozen != path.read_bytes():
                raise ValueError("Package differs from frozen source: " + str(path))
        relative = str(path.relative_to(PACKAGE))
        row = dict(members.get(relative, {"path": relative, "role": "Product member", "expected_installed_path": relative}))
        row.update(sha256=sha(path), bytes=path.stat().st_size)
        rows.append(row)
    previous.update(members=rows, source_input_commit=COMMON_INPUT,
                    candidate_body_input_commit=source_commit, inventory_input_commit=source_commit,
                    standing="Codex iteration 3 author candidate; independent member and owner acceptance remain open.",
                    snapshot_order="Source commit precedes inventory recording." if source_commit else "Working source; immutable inventory pending.")
    write("CANDIDATE.json", previous)
    mapping = read(PREVIOUS / "CONSERVATION.json")
    historical_fields = {k: mapping.pop(k) for k in list(mapping)
                         if any(part in k for part in ("confirmation", "synthesis", "applicability", "review_routes", "surface_repair"))}
    mapping["historical_qualification"] = {"path": "../CONSERVATION.json", "subject": "3ad1fca31dc93ba0847bbbbf308312a554daa1f6", "fields": historical_fields}
    mapping.update(input_commit=COMMON_INPUT, candidate_source_commit=source_commit,
                   standing="Author mapping; all predecessor obligations retained. Coordinates alone do not establish conservation or acceptance.")
    for name, pin in mapping["successor_member_pins"].items():
        path = PACKAGE / name
        pin.update(sha256=sha(path), bytes=path.stat().st_size)
    for row in mapping["rows"]:
        if row.get("successor_sha256"):
            row["successor_sha256"] = sha(PACKAGE / row["successor_locus"].split("#", 1)[0])
        row["acceptance"] = "current_independent_review_pending"
    mapping["contraction_evidence"] = ["METHOD_REDUCTION.md", "PROFILE_REDUCTION.md", "FRAME_CALCULUS_REDUCTION.md", "PARENT_REDUCTION.md"]
    write("CONSERVATION.json", mapping)
    write("FRONTIER.json", {"input_commit": COMMON_INPUT, "candidate_source_commit": source_commit,
          "row_count": len(mapping["rows"]), "rows": mapping["rows"]})
    print(json.dumps({"members": len(rows), "predecessor_rows": len(mapping["rows"]), "source_commit": source_commit}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-commit")
    parser.add_argument("--views", action="store_true")
    args = parser.parse_args()
    if args.views:
        refresh_views()
    inventory(args.source_commit)
