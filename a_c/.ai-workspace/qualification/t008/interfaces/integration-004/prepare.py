"""Retain the exact externally admitted cut before deterministic integration."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import time

ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
PRIOR = HERE.parent / "integration-003"
AUTHOR = ROOT / "a_c/.ai-workspace/qualification/t008/code-review-repair-002/implementation-001"


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def save(name, value):
    with (HERE / name).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, sort_keys=True, indent=2)
        stream.write("\n")


def walk(directory):
    for parent, directories, names in os.walk(directory, followlinks=False):
        directories[:] = [name for name in directories if name not in {"__pycache__", ".mypy_cache", ".venv", ".git"}]
        for name in names:
            path = Path(parent) / name
            if path.suffix not in {".pyc", ".pyo"}:
                yield path
        for name in directories[:]:
            path = Path(parent) / name
            if path.is_symlink():
                yield path
                directories.remove(name)


updates = {
    "a_c/build_tenants/graphify/code/ac_support_core.py": "842f3f136478b6948196fdd431f207f236c8c3e6ebb5573503726061c5d7bcc5",
    "a_c/build_tenants/graphify/code/ac_support_effects.py": "23dfafb2d7177d64287fc22002ec039ecc451d03c864a647f3c2deade7b2145c",
    "a_c/build_tenants/graphify/code/ac_support.py": "4d41a2373def237136cefe8b186c196c2e4376137c221ae4675c274abed5ad31",
    "a_c/build_tenants/graphify/test_env/test_ac_support_core.py": "c2ff9be121ee7ccdf6974e257c0d3f0e86b6f92c84a7020d5f2b1f632cd0530f",
    "a_c/build_tenants/graphify/test_env/test_ac_support_effects.py": "d944ba73369d3c672ba1b830419260f239d8d1bbfdc6558461412ae1f8978dda",
    "a_c/build_tenants/graphify/test_env/test_ac_support_interfaces.py": "597f33aae147fdc0ecc7c85638bf77615a59b856f6ee4ffe65041d1e9b82ef9e",
    "a_c/build_tenants/graphify/design/fd-support.md": "e3c5e6e83d9be525a0ca44fc4e64c9077e33958337bc29807014715a50592939",
    "a_c/.ai-workspace/tickets/active/T-008-fd-tenant-implementation.md": "2f59468cbecac464589ee99d79f32e4a12f551cd308c8a3d3e9ac52df8d7278f",
}
assert sha(AUTHOR / "CLOSED_RETURN.json") == "0d1634816568b13986b8a5821d9136df163e9012a1a851e235a26f6560b301f4"
assert sha(PRIOR / "CLOSED_RETURN.json") == "dd738980b592ef7fb516df984fff9f5b679c53602f7c2cd504c88058fc174a0f"
prior_subject = json.loads((PRIOR / "CLOSED_SUBJECT.json").read_bytes())
required = {**prior_subject["required_sources"], **updates}
for relative, expected in required.items():
    path = ROOT / relative
    assert path.is_file() and not path.is_symlink() and sha(path) == expected, relative
invariance = json.loads((AUTHOR / "INVARIANCE.json").read_bytes())
for row in json.loads((AUTHOR / "CANDIDATE.json").read_bytes())["files"]:
    assert sha(AUTHOR / row["snapshot"]) == row["after_sha256"] == required[row["path"]]
for row in invariance["readonly_guards"]:
    assert sha(ROOT / row["path"]) == row["expected_sha256"], row["path"]
profile = json.loads((ROOT / "a_c/build_tenants/graphify/design/fd-method-claude-rc9.json").read_bytes())
method_root = ROOT / "a_c/.ai-workspace/qualification/t008/live-review-runtime-002/authority/method"
for row in profile["members"]:
    path = method_root / row["member"]
    assert sha(path) == row["sha256"] and path.stat().st_size == row["bytes"], row["member"]
save("CLOSED_SUBJECT.json", {
    "root_execution_go": True,
    "source_basis": "T008 integration004 closed code-review-repair002",
    "required_sources": required,
    "implementation_closed_return_sha256": sha(AUTHOR / "CLOSED_RETURN.json"),
    "previous_integration_closed_return_sha256": sha(PRIOR / "CLOSED_RETURN.json"),
    "actual_provider_calls_authorized": 0,
    "expected_tests": None,
    "limits": "Execution-only mechanical qualification; F1 isolation is not a publicly qualified operator; no semantic/FP/install/benefit/RC acceptance",
})
basis = HERE / "basis"
basis.mkdir()
for origin, name in [(PRIOR / "run_checks.py", "prior-run_checks.py"), (PRIOR / "run_demo.py", "prior-run_demo.py"),
                     (PRIOR / "close_integration.py", "prior-close_integration.py"),
                     (PRIOR / "CLOSED_RETURN.json", "prior-CLOSED_RETURN.json"),
                     (PRIOR / "SOURCE_MANIFEST.json", "prior-SOURCE_MANIFEST.json"),
                     (AUTHOR / "CONTROL_MAP.json", "author-CONTROL_MAP.json"),
                     (AUTHOR / "CLOSED_RETURN.json", "author-CLOSED_RETURN.json"),
                     (AUTHOR / "runs/003-final-focused/execution.json", "author-selected-execution.json")]:
    shutil.copyfile(origin, basis / name)

tenant = ROOT / "a_c/build_tenants/graphify"
source_paths = set(walk(tenant)) | set(walk(ROOT / "a_c/specification"))
source_paths |= {ROOT / x for x in required}
source_paths |= {ROOT / x["path"] for x in invariance["readonly_guards"]}
source_paths |= set(walk(method_root))
source_paths |= {ROOT / "AGENTS.md", ROOT / "a_c/AGENTS.md", ROOT / "a_c/README.md"}
sources = []
for path in sorted(source_paths):
    assert path.is_file() and not path.is_symlink(), path
    relative = str(path.relative_to(ROOT))
    snapshot = HERE / "source-snapshots" / relative
    snapshot.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(path, snapshot)
    sources.append({"path": relative, "sha256": sha(path), "bytes": path.stat().st_size,
                    "snapshot": str(snapshot.relative_to(HERE))})
save("SOURCE_BEFORE.json", {"sources": sources, "method_members": len(profile["members"]), "captured_ns": time.time_ns()})
guard_roots = [ROOT / "a_c/dogfood", HERE.parent / "integration-001", PRIOR,
    ROOT / "a_c/.ai-workspace/qualification/t008/code-review-repair-001",
    ROOT / "a_c/.ai-workspace/qualification/t008/code-review-repair-002",
    HERE.parent / "integration-002",
    ROOT / "a_c/.ai-workspace/qualification/t008/live-review-runtime-001",
    ROOT / "a_c/.ai-workspace/qualification/t008/live-review-runtime-002"]
guards = []
for path in sorted(set(source_paths) | {p for d in guard_roots for p in walk(d)}):
    relative = str(path.relative_to(ROOT))
    if path.is_symlink():
        guards.append({"path": relative, "kind": "symlink", "target": os.readlink(path), "target_not_followed": True})
    elif path.is_file():
        guards.append({"path": relative, "kind": "regular", "sha256": sha(path), "bytes": path.stat().st_size})
save("GUARDS_BEFORE.json", {"files": guards, "scope": "Exact current source/WHAT/PD/12 method owners and existing historical studies/integration/reproduction/live-trial evidence; opaque bytes hashed only, no hidden reasoning extracted"})

runner = (PRIOR / "run_checks.py").read_text()
runner = runner.replace('"T008 integration003 closed code-review-repair001"', '"T008 integration004 closed code-review-repair002"')
# Add exact source/authority guards to the existing tenant guard at every stage.
runner = runner.replace('    for relative, expected in value["required_sources"].items():', '    for row in json.loads((HERE / "SOURCE_BEFORE.json").read_bytes())["sources"]:\n        if digest(ROOT / row["path"]) != row["sha256"]:\n            raise ValueError("Frozen source/authority changed: " + row["path"])\n    for relative, expected in value["required_sources"].items():')
runner = runner.replace('        after = sources()\n', '        gate()\n        after = sources()\n')
(HERE / "run_checks.py").write_text(runner)
(HERE / "run_demo.py").write_text((PRIOR / "run_demo.py").read_text().replace('            after = sources()\n', '            gate()\n            after = sources()\n'))
save("PREPARATION.checks.json", {"exact_root_cut_verified": True, "five_author_snapshots_match": True,
    "readonly_author_guards_verified": len(invariance["readonly_guards"]), "method_members_exact": len(profile["members"]),
    "current_source_snapshots": len(sources), "historical_and_current_guard_members": len(guards),
    "no_source_edits": True, "actual_provider_calls": 0,
    "standalone_upstream_rerun_selected": False,
    "harness_only_adaptation": "New harness binds current admitted cut; ordinary demo has no Writer precomputed plan. Product sources/tests unchanged; closure must distinguish new null-plan seam from old lower-layer historical proof."})
print(json.dumps({"prepared_sources": len(sources), "guards": len(guards), "regular_guard_bytes": sum(x.get("bytes", 0) for x in guards), "subject_sha256": sha(HERE / "CLOSED_SUBJECT.json")}))
