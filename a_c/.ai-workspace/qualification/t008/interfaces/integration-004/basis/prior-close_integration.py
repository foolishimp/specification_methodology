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
A = P / ".ai-workspace/qualification/t008/code-review-repair-001/implementation-001"
PREV = D.parent / "integration-002"
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
for stage in ["suite", "typing", "upstream"]:
    path = D / (stage + "-001")
    command = json.loads((path / "command.json").read_bytes())
    assert command["returncode"] == 0 and command["sources_unchanged"] is True
    summary[stage] = {"command": loc(path / "command.json"), "stdout": loc(path / "stdout"),
        "stderr": loc(path / "stderr"), "returncode": 0, "sources_unchanged": True}
summary["suite"].update(tests=count, seconds=match[0][1], skipped=0, full_runs=1, modules=module_counts)
assert "Success: no issues found in 9 source files" in (D / "typing-001/stdout").read_text()
summary["typing"]["strict_normal_import_files"] = 9
upstream = json.loads((D / "upstream-001/upstream-report.json").read_bytes())
assert upstream["status"] == "passed" and len(upstream["checks"]) == 9
assert upstream["upstream"]["commit"] == "fe085cedddde3a18554f8749b230bfe47f3dcce7"
summary["upstream"].update(checks=9, commit=upstream["upstream"]["commit"])
demo = json.loads((D / "ordinary-demo-001/checks.json").read_bytes())
assert len(demo["checks"]) == 10 and all(demo["checks"].values())
assert (D / "ordinary-demo-001/sources-before.json").read_bytes() == (D / "ordinary-demo-001/sources-after.json").read_bytes()
summary["ordinary_demo"] = {"checks": 10, "all_passed": True, "proof": loc(D / "ordinary-demo-001/checks.json"), "sources_unchanged": True}
save("RESULTS.json", {"schema": "a_c.T008.mechanical-integration-results/3", "subject": subject_ref,
    "stages": summary, "historical_tests": {"original": 242, "integration002": 254},
    "current_unique_full_suite_tests": count, "selected_author_tests_not_added_to_total": 38,
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

control_map = json.loads((A / "CONTROL_MAP.json").read_bytes())
author_execution = json.loads((A / "runs/004-final-selected/execution.json").read_bytes())
author_log = (A / "runs/004-final-selected/stderr").read_text()
author_ids = set(re.findall(r"^test_\w+ \(([^)]+)\) \.\.\.", author_log, re.M))
assert len(author_ids) == 38 and author_execution["returncode"] == 0 and author_ids <= executed
assert author_execution["source_before"] == author_execution["source_after"]
for relative, digest in author_execution["source_before"].items():
    assert h(R / relative) == digest
controls = []
for row in control_map["controls"]:
    filename = row["test"].split(":")[0]
    identity = filename[:-3] + "." + row["class"] + "." + row["method"]
    assert identity in executed and identity in author_ids
    source = T / "test_env" / filename
    fixture = None
    if row["class"] == "PublicRetryTests":
        fixture = effects_root / identity.replace(".", "_")
        classification = "Actual public CLI with registered local process; test-only pre-supervisor mutation barrier where selected"
    elif row["class"] == "PublicWriterReplayTests":
        fixture = public_root / row["method"]
        classification = "Actual public CLI/MCP; explicit fault/planning/request-lock barriers for selected variants"
    elif row["class"] == "WriterTests":
        fixture = effects_root / identity.replace(".", "_")
        classification = "Direct Effects callback/lock/replay control; no public CLI invocation inferred"
    elif row["control"].startswith("F1"):
        classification = "Isolated fold with controlled protected producer and patched qualification seam; NOT public qualified-operator proof"
    else:
        classification = "Pure Core boundary/authority control; no durable public result inferred"
    raw_calls = calls_by_fixture.get(fixture.name, []) if fixture else []
    fixture_files = []
    if fixture and fixture.exists():
        fixture_files = [loc(path) for path in sorted(fixture.rglob("*")) if path.is_file() and not path.is_symlink()
                         and ("calls" in path.parts or path.name in {"CUSTODY.json", "contender-attempted", "contender-acquired", "plan-planning", "contender-planning", "release-planning"})]
    owning = [x["operation_evidence"]["retained"] for x in raw_calls if x["operation_evidence"]["retained"]]
    controls.append({**row, "source_selected_assertion_origin": loc(A / "CONTROL_MAP.json"),
        "current_test": identity, "current_test_source": loc(source), "current_full_suite_passed": True,
        "author_selected38_passed": True, "classification": classification,
        "retained_fixture": str(fixture.relative_to(R)) if fixture and fixture.exists() else None,
        "actual_public_calls": len(raw_calls), "owning_operation_witnesses": owning,
        "deciding_raw_routes_and_barriers": fixture_files,
        "gaps": ([] if owning else ["Passed executed assertion/source/log is retained; no owning public OperationEvidence for this isolated/direct control"]),
        "limits": "No F_P judgment, public operator qualification or all-variant acceptance from this mechanical control"})
assert len(controls) == 19
save("REPAIR_CONTROL_EVIDENCE_MAP.json", {"subject": subject_ref, "controls": controls,
    "author_selected38": {"closed_return": loc(A / "CLOSED_RETURN.json"), "execution": loc(A / "runs/004-final-selected/execution.json"),
        "stderr": loc(A / "runs/004-final-selected/stderr"), "tests": sorted(author_ids), "all_in_current_unique_suite": True,
        "strict6": loc(A / "runs/005-final-strict/execution.json"), "not_added_to_unique_full_count": True},
    "writer_harness_seam": "Current admitted work.write calls pass null plan. Integration runner/demo contains no precomputed Writer plan and required no Product adaptation. Source-author lower-layer tests were updated within their own source grant; explicit injected-plan negative is not an admitted alternate entry. Historical old-cut proofs stay historical.",
    "source_selected_not_expected_answer_oracle": True})

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
        "historical_integration002_witness_count": old["current_witness_count"],
        "unexecuted_variants": old["unexecuted_variants"],
        "limits": ["Owning artifacts, actual process calls and isolated/direct test assertions remain distinct",
            "Missing owning evidence remains an explicit gap; no public/FP/all23 qualification inferred",
            "No F1 publicly qualified operator proof; no semantic/full-calculus/benefit/install/RC acceptance"]})
missing = [row["operation"] for row in rows if not row["current_owning_witnesses"]]
save("OPERATION_SCENARIO_MAP.json", {"schema": "a_c.T008.operation-scenario-map/3", "subject": subject_ref,
    "current_unique_full_suite_tests": count, "historical_original_tests": 242, "historical_integration002_tests": 254,
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
old_hashes = {row["path"]: row["sha256"] for row in old_source["sources"] + old_source["governing_sources"]}
save("SOURCE_MANIFEST.json", {"schema": "a_c.T008.closed-successor-source-manifest/3", "subject": subject_ref,
    "sources": before["sources"], "method_members": before["method_members"], "current_unique_tests": count,
    "current_guard_proof": loc(D / "GUARD_CHECK.json"),
    "changes_from_integration002": [{"path": row["path"], "old_sha256": old_hashes[row["path"]], "current_sha256": row["sha256"]}
        for row in before["sources"] if row["path"] in old_hashes and old_hashes[row["path"]] != row["sha256"]],
    "implementation_closed_return": loc(A / "CLOSED_RETURN.json"), "actual_provider_or_native_F_P_calls": 0})
save("EXECUTOR_ENVIRONMENT.json", {"python": {"path": str(Path(sys.executable).resolve()), "sha256": h(Path(sys.executable).resolve()), "version": sys.version},
    "mypy_version": importlib.metadata.version("mypy"), "package_installs": 0,
    "selected_per_run_environment": "Exact command.json files; isolated external TMPDIR/cache roots; no global config or HOME/home/CODEX_HOME replacement",
    "host_and_effect_scope": "Local deterministic/process fixtures only; no native provider invocation; no claim external/process-tree closure from parent end"})
report = f"""Integration-003 closed on the Root-selected repaired cut.

The single full tenant run passed {count} tests with no skips in {match[0][1]}s. Strict normal-import typing passed all9 selected files. The exact pinned Graphify upstream passed9 checks and the ordinary read-only CLI/MCP example passed10. The author's38 selected tests are a subset of this full run, not38 additional unique tests.

All19 source-selected repair discriminators are indexed with their current executed methods, exact source cut, author evidence, raw public calls or lower-layer scope. Required-P counterexample controls use an isolated qualification seam and do not qualify a public conjunction operator. The Context extra-source/model/required-fit controls use actual public calls and local launch/barrier variants. Writer replay covers real CLI/MCP append/replace, request-lock contention, authority/policy changes and fatal/uncertain history; direct lock-callback controls remain direct controls. Current work.write enters with null plan; this integration required no Product or precomputed-plan harness patch.

Canonical owning operation witnesses and raw public process calls remain separate from unit assertions. The operation map leaves {len(missing)} declared operations without current owning OperationEvidence. Passed tests do not establish all23-operation public qualification, F_P usability, full calculus conformance, semantic acceptance, efficiency, installed qualification or RC readiness.

All{len(guards)} guarded existing members are unchanged. Earlier254/242-test proof, negative reproductions, the unconsumable Worker return and public Reviewer timeout/partial histories remain historical evidence. No provider/native F_P calls, Product source edits, installs, Git, global or network actions were performed. Root owns any runtime owner/policy renewal and subsequent decisions.

After this run, Root reported external independent static-review residuals E10 (inherited newly-required-P counterexample) and E11 (missing claim-marker conflicting replay). This integration did not reproduce or test those residuals and performs no further checks or repairs. The green mechanical result is not an acceptance verdict. Root's exact notice is retained separately.
"""
with (D / "REPORT.md").open("x", encoding="utf-8") as stream:
    stream.write(report)
gate()
files = [loc(path) for path in sorted(D.rglob("*")) if path.is_file() and not path.is_symlink()
         and path.name not in {"EVIDENCE_MANIFEST.json", "CLOSED_RETURN.json"}]
links = [{"path": str(path.relative_to(R)), "kind": "symlink", "target": os.readlink(path), "target_not_followed": True}
         for path in sorted(D.rglob("*")) if path.is_symlink()]
save("EVIDENCE_MANIFEST.json", {"files": files, "symlinks": links, "scope": "Custody only; no semantic review of every fixture or link target"})
save("CLOSED_RETURN.json", {"schema": "a_c.T008.integration-successor-return/3", "state": "Closed finite current mechanical integration",
    "source_manifest_sha256": h(D / "SOURCE_MANIFEST.json"), "evidence_manifest_sha256": h(D / "EVIDENCE_MANIFEST.json"),
    "subject_sha256": h(D / "CLOSED_SUBJECT.json"), "results_sha256": h(D / "RESULTS.json"),
    "repair_map_sha256": h(D / "REPAIR_CONTROL_EVIDENCE_MAP.json"), "operation_map_sha256": h(D / "OPERATION_SCENARIO_MAP.json"),
    "public_retry_index_sha256": h(D / "PUBLIC_RETRY_PROOF_INDEX.json"), "public_repair_calls_sha256": h(D / "PUBLIC_REPAIR_CALLS_INDEX.json"),
    "guard_check_sha256": h(D / "GUARD_CHECK.json"), "report_sha256": h(D / "REPORT.md"),
    "current_unique_full_suite_tests": count, "full_suite_runs": 1, "skipped": 0, "strict_normal_import_files": 9,
    "upstream_checks": 9, "ordinary_public_demo_checks": 10, "repair_discriminators": 19,
    "author_selected38_in_current_suite": True, "sources_and_historical_guards_unchanged": True,
    "operations_without_current_owning_witness": missing, "actual_provider_or_native_F_P_calls": 0,
    "product_source_edits": 0, "own_harness_writer_plan_adaptations": 0,
    "external_review_notice": loc(D / "ROOT_REVIEW_NOTICE.txt"),
    "remaining": ["Independent current code review/dispositions are separately owned",
        "Root reports external static E10/E11 findings; this integration did not reproduce/test them and makes no acceptance verdict",
        "Actual public F_P trials remain partial/unconsumable/timeout histories, no later technical check erases them",
        "F1 isolated fold is not public qualified-operator proof",
        "Root runtime owner/policy renewal remains separately owned",
        "No all23-operation/FDV/full-calculus/benefit/install/RC acceptance"]})
print(json.dumps({"closed_return": h(D / "CLOSED_RETURN.json"), "source_manifest": h(D / "SOURCE_MANIFEST.json"),
    "evidence_manifest": h(D / "EVIDENCE_MANIFEST.json"), "tests": count, "proof_files": len(files), "symlink_texts": len(links),
    "operation_witnesses": sum(map(len, operations.values())), "missing_owning_witnesses": missing,
    "repair_controls": len(controls), "indexed_public_repair_calls": sum(map(len, calls_by_fixture.values())),
    "public_retry_tests": len(retry_rows), "selected_retry_files": len(selected), "guard_members": len(guards)}, indent=2))
