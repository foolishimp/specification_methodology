"""Close this finite executed proof without altering any Product source."""
from pathlib import Path
import ast
import collections
import hashlib
import importlib.metadata
import json
import os
import re
import sys
import time

sys.dont_write_bytecode = True
from run_checks import gate

D = Path(__file__).resolve().parent
R = D.parents[5]
P = R / "a_c"
T = P / "build_tenants/graphify"
A = P / ".ai-workspace/qualification/t008/code-review-repair-002/implementation-001"
PREV = D.parent / "integration-003"
sys.path.insert(0, str(T / "code"))
import ac_support_core as c


def h(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def save(name, value):
    raw = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    with (D / name).open("x", encoding="utf-8") as stream:
        stream.write(raw)


def loc(path):
    return {"path": str(path.relative_to(R)), "sha256": h(path), "bytes": path.stat().st_size}


subject = gate()
subject_ref = loc(D / "CLOSED_SUBJECT.json")
log = (D / "suite-001/stderr").read_text()
match = re.findall(r"^Ran (\d+) tests? in ([0-9.]+)s$", log, re.M)
assert len(match) == 1 and re.search(r"^OK$", log, re.M)
count = int(match[0][0])
executed = set(re.findall(r"^test_\w+ \(([^)]+)\) \.\.\.", log, re.M))
assert len(executed) == count
assert not re.search(r"^test_.*\.\.\. (?:skipped|FAIL|ERROR)", log, re.M)
module_counts = dict(collections.Counter(x.split(".")[0] for x in executed))
summary = {}
for stage in ["suite", "typing"]:
    path = D / (stage + "-001")
    command = json.loads((path / "command.json").read_bytes())
    assert command["returncode"] == 0 and command["sources_unchanged"] is True
    summary[stage] = {"command": loc(path / "command.json"), "stdout": loc(path / "stdout"),
        "stderr": loc(path / "stderr"), "returncode": 0, "sources_unchanged": True}
summary["suite"].update(tests=count, seconds=match[0][1], skipped=0, full_runs=1, modules=module_counts)
assert "Success: no issues found in 9 source files" in (D / "typing-001/stdout").read_text()
summary["typing"]["strict_normal_import_files"] = 9
upstream = json.loads((D / "UPSTREAM_APPLICABILITY.after.json").read_bytes())
assert upstream["carried_actual_checks"] == 9 and upstream["fresh_standalone_upstream_checks"] == 0
assert upstream["actual_filesystem_tree"] == upstream["pinned_tree"] == "6e11ed7cda0437ff12a29a328ca785e8915ddbc0"
summary["upstream_carried"] = {"checks": 9, "fresh_standalone_checks": 0,
    "actual_prior_report": upstream["carried_actual_report"],
    "applicability_before": loc(D / "UPSTREAM_APPLICABILITY.before.json"),
    "applicability_after": loc(D / "UPSTREAM_APPLICABILITY.after.json"),
    "limits": "Retained integration003 actual upstream result; fresh suite includes its named legacy upstream controls, but standalone9 was not rerun"}
demo = json.loads((D / "ordinary-demo-001/checks.json").read_bytes())
assert len(demo["checks"]) == 10 and all(demo["checks"].values())
assert (D / "ordinary-demo-001/sources-before.json").read_bytes() == (D / "ordinary-demo-001/sources-after.json").read_bytes()
summary["ordinary_demo"] = {"checks": 10, "all_passed": True, "proof": loc(D / "ordinary-demo-001/checks.json"), "sources_unchanged": True}
save("RESULTS.json", {"schema": "a_c.T008.mechanical-integration-results/4", "subject": subject_ref,
    "stages": summary, "historical_tests": {"original": 242, "integration002": 254, "integration003": 273},
    "current_unique_full_suite_tests": count, "selected_author_tests_not_added_to_total": 35,
    "actual_provider_or_native_F_P_calls": 0,
    "qualification": "Finite deterministic/local-process/upstream checks only. No all23-operation, F_P/FDV, semantic, operator, benefit, install or RC acceptance."})

# Only current run stage trees are examined. Snapshots/historical byte guards are not mined as proof.
stage_dirs = [D / "suite-001", D / "ordinary-demo-001"]
operations = collections.defaultdict(dict)
artifact_paths = {}
excluded_mutated = []
kind_counts = collections.Counter()
for stage in stage_dirs:
    for path in sorted(stage.rglob("*.json")):
        if path.is_symlink() or not path.is_file():
            continue
        try:
            value = json.loads(path.read_bytes())
        except (ValueError, UnicodeError):
            continue
        if not isinstance(value, dict) or value.get("schema") != c.ARTIFACT:
            continue
        if not re.fullmatch(r"[0-9a-f]{64}", path.stem):
            continue
        digest = h(path)
        if digest != path.stem or c.canonical(value) != path.read_bytes():
            excluded_mutated.append(loc(path))
            continue
        artifact_paths.setdefault(digest, path)
        kind_counts[value.get("kind")] += 1
        if value.get("kind") != "operation":
            continue
        payload = value["payload"]
        request = payload.get("request", {})
        operation = request.get("operation")
        response = payload.get("response_without_evidence", {})
        if operation in c._ARGUMENTS:
            route = "retained lower-layer/callback fixture evidence; no CLI/MCP invocation inferred"
            if "public-fixtures" in path.parts or "retained-demo" in path.parts:
                route = "retained public CLI/MCP fixture artifact; exact raw call linkage is indexed separately"
            if "PublicRetryTests" in str(path):
                route = "retained actual public CLI/local-process fixture artifact"
            operations[operation].setdefault(digest, {"artifact": {"id": "sha256:" + digest, "sha256": digest},
                "source": loc(path), "request_id": request.get("id"), "status": response.get("status"),
                "refusal": response.get("refusal"), "operation_outcome": response.get("operation_outcome"), "route": route,
                "limits": "Owning canonical envelope in its actual fixture scope; not an F_P or semantic acceptance witness"})


def operation_reference(response):
    reference = response.get("evidence") if isinstance(response, dict) else None
    if not reference:
        return {"ref": None, "retained": None, "gap": "No owning OperationEvidence in this response (including startup/protocol/fatal cuts); raw transport remains evidence"}
    path = artifact_paths.get(reference.get("sha256"))
    return {"ref": reference, "retained": loc(path) if path else None,
            "gap": None if path else "Response ref exists but canonical owning envelope is absent/corrupt in retained fixture state"}


def public_calls(fixture):
    rows = []
    directory = fixture / "calls"
    if not directory.exists():
        return rows
    for call in sorted(directory.iterdir()):
        request_path = call / "request.json"
        if not request_path.is_file():
            continue
        request = json.loads(request_path.read_bytes())
        effects = (call / "execution.json").exists()
        response_path = call / ("stdout.bin" if effects else "stdout")
        metadata_path = call / ("execution.json" if effects else "command.json")
        metadata = json.loads(metadata_path.read_bytes())
        transport = "cli" if effects else metadata["transport"]
        response = None
        if response_path.read_bytes():
            wire = json.loads(response_path.read_bytes()) if transport == "cli" else [json.loads(line) for line in response_path.read_bytes().splitlines()]
            response = wire if transport == "cli" else next((m.get("result", {}).get("structuredContent") for m in wire if m.get("id") == 2), None)
        raw = [loc(request_path), loc(response_path), loc(metadata_path)]
        for filename in ["stderr.bin", "stderr", "ended.json", "stdin", "barrier.py", "pre-supervisor-barrier.py", "barrier-reached.txt"]:
            if (call / filename).is_file():
                raw.append(loc(call / filename))
        rows.append({"fixture": fixture.name, "operation": request["operation"], "request_id": request["id"],
            "transport": transport, "test_hook": metadata.get("test_hook"), "raw": raw,
            "response_status": response.get("status") if response else None,
            "refusal": response.get("refusal") if response else None,
            "operation_outcome": response.get("operation_outcome") if response else None,
            "result_artifact": (response.get("result") or {}).get("artifact") if response else None,
            "operation_evidence": operation_reference(response),
            "returncode": metadata.get("returncode") if effects else json.loads((call / "ended.json").read_bytes())["returncode"],
            "limits": "Actual registered/local subprocess CLI/MCP boundary; barriers/faults explicitly test-only, no semantic actor"})
    return rows


effects_root = D / "suite-001/effects-fixtures"
public_root = D / "suite-001/public-fixtures"
calls_by_fixture = {}
for fixture in sorted(effects_root.iterdir()):
    if "PublicRetryTests_" in fixture.name:
        calls_by_fixture[fixture.name] = public_calls(fixture)
for fixture in sorted(public_root.iterdir()):
    if (fixture / "calls").is_dir():
        calls_by_fixture[fixture.name] = public_calls(fixture)
save("PUBLIC_REPAIR_CALLS_INDEX.json", {"subject": subject_ref, "rows": calls_by_fixture,
    "raw_call_count": sum(map(len, calls_by_fixture.values())),
    "scope": "Actual current public retry/Context currentness/Writer replay calls; ordinary interface protocol and demo raw proofs remain separately retained. No all-operation coverage."})

retry_rows = []
selected = {}
for name, calls in calls_by_fixture.items():
    if "PublicRetryTests_test_public_" not in name:
        continue
    if name.endswith("test_public_selected_retry"):
        deciding = []
        for operation in ["context.assemble", "checks.evaluate", "contract.preflight", "dispatch.start", "dispatch.observe"]:
            matches = [x for x in calls if x["operation"] == operation]
            if matches:
                deciding.append(matches[-1])
    else:
        deciding = [calls[-1]]
    for row in deciding:
        for reference in row["raw"]:
            selected[reference["path"]] = reference
        reference = row["operation_evidence"]["retained"]
        if reference:
            selected[reference["path"]] = reference
    retry_rows.append({"test_fixture": name, "actual_calls": calls, "selected_deciding_calls": deciding})
assert len(retry_rows) == 10
save("PUBLIC_RETRY_PROOF_INDEX.json", {"subject": subject_ref, "actual_fixture_tests": len(retry_rows),
    "rows": retry_rows, "selected_deciding_raw_files": list(selected.values()),
    "limits": "Actual composed public CLI checks/retry. Old manufactured-receipt lower-layer fixture is separately named, not this public proof. No production/FP/operator qualification."})

# Reacquire prior19 source-selected discriminators as historical oracles, then bind current execution.
A1 = P / ".ai-workspace/qualification/t008/code-review-repair-001/implementation-001"
control_map = json.loads((A1 / "CONTROL_MAP.json").read_bytes())
prior_author_log = (A1 / "runs/004-final-selected/stderr").read_text()
prior_author_ids = set(re.findall(r"^test_\w+ \(([^)]+)\) \.\.\.", prior_author_log, re.M))
assert len(prior_author_ids) == 38 and prior_author_ids <= executed
author_execution = json.loads((A / "runs/003-final-focused/execution.json").read_bytes())
author_log = (A / "runs/003-final-focused/stderr").read_text()
author_ids = set(re.findall(r"^test_\w+ \(([^)]+)\) \.\.\.", author_log, re.M))
assert len(author_ids) == 35 and author_execution["returncode"] == 0 and author_ids <= executed
assert author_execution["source_before"] == author_execution["source_after"]
for relative, digest in author_execution["source_before"].items():
    assert h(R / relative) == digest
method_index = {}
for source in (T / "test_env").glob("test_*.py"):
    for cls in [node for node in ast.parse(source.read_text()).body if isinstance(node, ast.ClassDef)]:
        for node in cls.body:
            if isinstance(node, ast.FunctionDef) and node.name.startswith("test_"):
                method_index[(source.name, node.name)] = (source.stem + "." + cls.name + "." + node.name, cls.name, node.lineno)


def method_proof(filename, method):
    identity, cls, line = method_index[(filename, method)]
    assert identity in executed
    source = T / "test_env" / filename
    fixture = None
    if cls == "PublicRetryTests":
        fixture = effects_root / identity.replace(".", "_")
        classification = "Actual public CLI with registered local process; selected pre-supervisor mutation barrier is test-only"
    elif cls == "PublicWriterReplayTests":
        fixture = public_root / method
        classification = "Actual public CLI/MCP; explicit fault/owner-loss/planning/request-lock barriers are test-only"
    elif filename == "test_ac_support_effects.py":
        fixture = effects_root / identity.replace(".", "_")
        classification = "Direct Effects fixture unless named ProcessTests actor-side MCP control; no blanket public-route inference"
        if cls == "ProcessTests":
            classification = "Actual registered local subprocess and actor-side public MCP Writer; no native/provider/F_P actor"
    else:
        classification = "Pure/controlled Core fixture; qualification gate isolated for fold controls, not a publicly qualified operator"
    raw_calls = calls_by_fixture.get(fixture.name, []) if fixture else []
    fixture_files = [loc(path) for path in sorted(fixture.rglob("*")) if path.is_file() and not path.is_symlink()] if fixture and fixture.exists() else []
    owning = [call["operation_evidence"]["retained"] for call in raw_calls if call["operation_evidence"]["retained"]]
    return {"current_test": identity, "current_test_source": loc(source), "current_line": line,
        "current_full_suite_passed": True, "classification": classification,
        "retained_fixture": str(fixture.relative_to(R)) if fixture and fixture.exists() else None,
        "actual_indexed_public_calls": len(raw_calls), "owning_operation_witnesses": owning,
        "retained_fixture_files": fixture_files,
        "gaps": [] if owning else ["Passed assertion and source/log retained; no indexed owning public OperationEvidence inferred for direct/isolated test. Named process scope may have retained artifacts below its own custody."],
        "limits": "No F_P/semantic/operator/public-all-variant qualification from a fixture pass"}


prior_controls = []
for row in control_map["controls"]:
    proof = method_proof(row["test"].split(":")[0], row["method"])
    assert proof["current_test"] in prior_author_ids
    prior_controls.append({"historical_source_selected_control": row, "historical_control_origin": loc(A1 / "CONTROL_MAP.json"),
        **proof, "historical_author38_not_relabelled_current": True})
assert len(prior_controls) == 19
new_map = json.loads((A / "CONTROL_MAP.json").read_bytes())
controls = []
for row in new_map["controls"]:
    methods = []
    for selected_method in row["methods"]:
        proof = method_proof(Path(selected_method["source"]["path"]).name, selected_method["method"])
        assert proof["current_test"] in author_ids
        methods.append({"author_control_method": selected_method, **proof})
    controls.append({"source_selected_control": row, "origin": loc(A / "CONTROL_MAP.json"), "current_methods": methods})
assert len(controls) == 8
old_executed = set(re.findall(r"^test_\w+ \(([^)]+)\) \.\.\.", (PREV / "suite-001/stderr").read_text(), re.M))
new_methods = sorted(executed - old_executed)
assert len(new_methods) == 8 and set(new_methods) <= author_ids
public_author = json.loads((A / "PUBLIC_EVIDENCE.json").read_bytes())
assert public_author["call_count"] == len(public_author["calls"]) == 52
assert public_author["source_cut"] == author_execution["source_after"]
save("REPAIR_CONTROL_EVIDENCE_MAP.json", {"subject": subject_ref,
    "new8_control_rows": controls, "prior19_currently_reexecuted_controls": prior_controls,
    "new_test_methods": new_methods,
    "author_selected35": {"closed_return": loc(A / "CLOSED_RETURN.json"), "execution": loc(A / "runs/003-final-focused/execution.json"),
        "stderr": loc(A / "runs/003-final-focused/stderr"), "tests": sorted(author_ids), "all_in_current_unique_suite": True,
        "strict5": loc(A / "runs/004-final-strict/execution.json"), "not_added_to_unique_full_count": True,
        "public52": loc(A / "PUBLIC_EVIDENCE.json"), "public_call_count": 52},
    "historical_author38": {"closed_return": loc(A1 / "CLOSED_RETURN.json"), "tests": sorted(prior_author_ids),
        "all_corresponding_methods_reexecuted_current": True, "old_source_cut_stays_historical": True},
    "retained_initial_assertion_failure": {"execution": loc(A / "runs/001-focused/execution.json"),
        "stderr": loc(A / "runs/001-focused/stderr"), "correction": loc(A / "FIXTURE_ASSERTION_CORRECTION.json"),
        "scope": "Author retained the initial wrong-subject fixture assertion failure and correction; no failure or source cut overwritten by integration"},
    "writer_harness_seam": "Current admitted work.write calls pass null plan. Integration runner/demo required no Product or precomputed-plan harness patch. Explicit injected-plan rejection stays a negative control.",
    "source_selected_not_semantic_answer_oracle": True})

# Relate executed test names, actual owning artifacts and historical scopes without equating them.
mentions = collections.defaultdict(list)
for path in sorted((T / "test_env").glob("test_*.py")):
    tree = ast.parse(path.read_text())
    for cls in [node for node in tree.body if isinstance(node, ast.ClassDef)]:
        for node in cls.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) or not node.name.startswith("test_"):
                continue
            identity = path.stem + "." + cls.name + "." + node.name
            if identity not in executed:
                continue
            literals = {item.value for item in ast.walk(node) if isinstance(item, ast.Constant) and isinstance(item.value, str)}
            for operation in set(c._ARGUMENTS) & literals:
                mentions[operation].append({"test": identity, "source": loc(path), "line": node.lineno,
                    "scope": "Executed test with operation literal only; not proof of an actual public call"})
historical = json.loads((PREV / "OPERATION_SCENARIO_MAP.json").read_bytes())
old_rows = {row["operation"]: row for row in historical["rows"]}
rows = []
for operation in sorted(c._ARGUMENTS):
    witnesses = list(operations[operation].values())
    old = old_rows[operation]
    public_rows = [call for calls in calls_by_fixture.values() for call in calls if call["operation"] == operation]
    rows.append({"operation": operation, "requirements": old["requirements"], "current_owning_witnesses": witnesses,
        "current_witness_count": len(witnesses), "current_status_counts": dict(collections.Counter(x["status"] for x in witnesses)),
        "actual_indexed_public_repair_calls": public_rows, "executed_test_literal_mentions": mentions[operation],
        "historical_integration003_witness_count": old["current_witness_count"],
        "unexecuted_variants": old["unexecuted_variants"],
        "limits": ["Owning artifacts, actual process calls and isolated/direct test assertions remain distinct",
            "Missing owning evidence remains an explicit gap; no public/FP/all23 qualification inferred",
            "No F1 publicly qualified operator proof; no semantic/full-calculus/benefit/install/RC acceptance"]})
missing = [row["operation"] for row in rows if not row["current_owning_witnesses"]]
save("OPERATION_SCENARIO_MAP.json", {"schema": "a_c.T008.operation-scenario-map/4", "subject": subject_ref,
    "current_unique_full_suite_tests": count, "historical_original_tests": 242, "historical_integration002_tests": 254, "historical_integration003_tests": 273,
    "historical_map": loc(PREV / "OPERATION_SCENARIO_MAP.json"), "rows": rows,
    "operations_without_current_owning_evidence": missing, "repair_controls": loc(D / "REPAIR_CONTROL_EVIDENCE_MAP.json"),
    "actual_public_repair_calls": loc(D / "PUBLIC_REPAIR_CALLS_INDEX.json"), "actual_public_retry": loc(D / "PUBLIC_RETRY_PROOF_INDEX.json"),
    "excluded_corrupt_or_noncanonical_artifact_copies": excluded_mutated,
    "scope": "Finite current versus historical evidence map; no semantic review of every generated fixture or 23-operation qualification"})

# Recheck every existing finite historical/source guard, without following negative-fixture symlinks.
guards = json.loads((D / "GUARDS_BEFORE.json").read_bytes())["files"]
after = []
mismatches = []
for row in guards:
    path = R / row["path"]
    if row["kind"] == "symlink":
        actual = {"path": row["path"], "kind": "symlink", "target": os.readlink(path) if path.is_symlink() else None, "target_not_followed": True}
    else:
        actual = {"path": row["path"], "kind": "regular", "sha256": h(path) if path.is_file() and not path.is_symlink() else None,
                  "bytes": path.stat().st_size if path.is_file() and not path.is_symlink() else None}
    after.append(actual)
    if row != actual:
        mismatches.append({"before": row, "after": actual})
save("GUARD_CHECK.json", {"before": loc(D / "GUARDS_BEFORE.json"), "checked_ns": time.time_ns(),
    "members": len(guards), "regular_files": sum(row["kind"] == "regular" for row in guards),
    "symlink_target_texts_only": sum(row["kind"] == "symlink" for row in guards),
    "before_values_sha256": hashlib.sha256(canonical(guards)).hexdigest(), "after_values_sha256": hashlib.sha256(canonical(after)).hexdigest(),
    "mismatches": mismatches, "unchanged": not mismatches,
    "scope": "All finite before-listed current source/WHAT/PD/12 method owners/historical studies/old integration/reproduction/live timeout evidence; unrelated newly appended owner evidence is not relabeled"})
assert not mismatches, "Frozen source or prior evidence changed"
before = json.loads((D / "SOURCE_BEFORE.json").read_bytes())
for row in before["sources"]:
    assert h(R / row["path"]) == h(D / row["snapshot"]) == row["sha256"]
old_source = json.loads((PREV / "SOURCE_MANIFEST.json").read_bytes())
old_hashes = {row["path"]: row["sha256"] for row in old_source["sources"] + old_source.get("governing_sources", [])}
save("SOURCE_MANIFEST.json", {"schema": "a_c.T008.closed-successor-source-manifest/4", "subject": subject_ref,
    "sources": before["sources"], "method_members": before["method_members"], "current_unique_tests": count,
    "current_guard_proof": loc(D / "GUARD_CHECK.json"),
    "changes_from_integration003": [{"path": row["path"], "old_sha256": old_hashes[row["path"]], "current_sha256": row["sha256"]}
        for row in before["sources"] if row["path"] in old_hashes and old_hashes[row["path"]] != row["sha256"]],
    "implementation_closed_return": loc(A / "CLOSED_RETURN.json"), "actual_provider_or_native_F_P_calls": 0})
save("EXECUTOR_ENVIRONMENT.json", {"python": {"path": str(Path(sys.executable).resolve()), "sha256": h(Path(sys.executable).resolve()), "version": sys.version},
    "mypy_version": importlib.metadata.version("mypy"), "package_installs": 0,
    "selected_per_run_environment": "Exact command.json files; isolated external TMPDIR/cache roots; no global config or HOME/home/CODEX_HOME replacement",
    "host_and_effect_scope": "Local deterministic/process fixtures only; no native provider invocation; no claim external/process-tree closure from parent end"})
report = f"""Integration-004 closed on the Root-selected repaired cut.

The single fresh full tenant run passed {count} tests with no skips in {match[0][1]}s. Fresh strict normal-import typing passed all 9 selected files and the ordinary read-only CLI/MCP demo passed 10 checks. The author's 35 focused tests are a subset, not 35 additional unique tests. The new 8 methods and 8 source-selected control rows are indexed alongside all prior 19 controls reexecuted on current sources.

The standalone 9 Graphify checks were not rerun. Their actual integration003 proof is carried with exact checker/codec/fixture and full 1,064-member upstream source tree applicability, commit/tree, five entrypoints and selected Python/package versions verified before and after. Actual current legacy upstream controls still ran as part of the single full suite; these do not relabel the carried standalone result as fresh.

The nested required-P fold controls explicitly isolate the qualification gate and do not qualify a public operator. Writer lost-claim/history controls include actual CLI/MCP calls with test-only loss/fault injections; private completed-lookup, lock-callback and controlled Core cases retain their own lower-layer scope. Existing public retry and concurrent Writer/local actor-side MCP controls remain indexed as actual deterministic process evidence. Current work.write uses null plan; no Product or precomputed-plan integration patch was made.

The author's initial wrong-subject test assertion failure and its correction are preserved. Owning canonical OperationEvidence, raw transport records and passed unit assertions remain distinct. {len(missing)} declared operations still lack current owning witnesses. No all23-operation/F_P/FDV, publicly qualified operator, semantic/full-calculus, benefit, install or RC claim follows.

All {len(guards)} guarded historical/current members remain unchanged. Old 273/254/242-test cuts and review002 F remain historical; the current independent review is separately owned and no pending verdict is asserted. Worker timeout/missing return, phase1 partial/unconsumable check and phase2 timeout histories persist. Binding002 remains historical/stale; no policy renewal/native-call budget is selected. No source/metadata edits, provider/native F_P calls, installs, network or global changes were performed by this integration Worker. There were no direct Git commands or repository mutations; the existing suite boundary controls retain their declared read-only upstream Git inspections.
"""
with (D / "REPORT.md").open("x", encoding="utf-8") as stream:
    stream.write(report)
gate()
files = [loc(path) for path in sorted(D.rglob("*")) if path.is_file() and not path.is_symlink()
         and path.name not in {"EVIDENCE_MANIFEST.json", "CLOSED_RETURN.json"}]
links = [{"path": str(path.relative_to(R)), "kind": "symlink", "target": os.readlink(path), "target_not_followed": True}
         for path in sorted(D.rglob("*")) if path.is_symlink()]
save("EVIDENCE_MANIFEST.json", {"files": files, "symlinks": links, "scope": "Custody only; no semantic review of every fixture or link target"})
save("CLOSED_RETURN.json", {"schema": "a_c.T008.integration-successor-return/4", "state": "Closed finite current mechanical integration",
    "source_manifest_sha256": h(D / "SOURCE_MANIFEST.json"), "evidence_manifest_sha256": h(D / "EVIDENCE_MANIFEST.json"),
    "subject_sha256": h(D / "CLOSED_SUBJECT.json"), "results_sha256": h(D / "RESULTS.json"),
    "repair_map_sha256": h(D / "REPAIR_CONTROL_EVIDENCE_MAP.json"), "operation_map_sha256": h(D / "OPERATION_SCENARIO_MAP.json"),
    "public_retry_index_sha256": h(D / "PUBLIC_RETRY_PROOF_INDEX.json"), "public_repair_calls_sha256": h(D / "PUBLIC_REPAIR_CALLS_INDEX.json"),
    "guard_check_sha256": h(D / "GUARD_CHECK.json"), "report_sha256": h(D / "REPORT.md"),
    "upstream_applicability_before_sha256": h(D / "UPSTREAM_APPLICABILITY.before.json"),
    "upstream_applicability_after_sha256": h(D / "UPSTREAM_APPLICABILITY.after.json"),
    "carried_actual_upstream_report": upstream["carried_actual_report"],
    "current_unique_full_suite_tests": count, "full_suite_runs": 1, "skipped": 0, "strict_normal_import_files": 9,
    "fresh_upstream_standalone_checks": 0, "carried_actual_upstream_checks": 9, "fresh_ordinary_public_demo_checks": 10,
    "new_control_rows": 8, "prior_control_rows_reexecuted_current": 19, "new_test_methods": 8,
    "author_selected35_in_current_suite": True, "author_public52_retained": True,
    "sources_and_historical_guards_unchanged": True, "operations_without_current_owning_witness": missing,
    "actual_provider_or_native_F_P_calls": 0, "product_or_metadata_edits": 0, "own_harness_writer_plan_adaptations": 0,
    "remaining": ["Current independent code review/dispositions are separately owned; no pending verdict asserted",
        "Old review002 F remains bound to its old source cut",
        "Actual public F_P trials remain partial/unconsumable/timeout histories",
        "F1/R1 controlled fold is not a publicly qualified operator proof",
        "Root runtime owner/policy binding002 remains historical/stale; no renewal or native calls",
        "No all23-operation/FDV/full-calculus/benefit/install/RC acceptance"]})
print(json.dumps({"closed_return": h(D / "CLOSED_RETURN.json"), "source_manifest": h(D / "SOURCE_MANIFEST.json"),
    "evidence_manifest": h(D / "EVIDENCE_MANIFEST.json"), "tests": count, "proof_files": len(files), "symlink_texts": len(links),
    "operation_witnesses": sum(map(len, operations.values())), "missing_owning_witnesses": missing,
    "new_controls": len(controls), "prior_controls_current": len(prior_controls),
    "indexed_public_repair_calls": sum(map(len, calls_by_fixture.values())), "public_retry_tests": len(retry_rows),
    "selected_retry_files": len(selected), "guard_members": len(guards), "fresh_upstream9_runs": 0,
    "carried_upstream_checks": 9}, indent=2))
