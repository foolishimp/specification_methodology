"""Adapt only evidence projection to fresh checks and explicitly retained proof."""
from pathlib import Path

D = Path(__file__).resolve().parent
text = (D.parent / "integration-003/close_integration.py").read_text()
text = text.replace('code-review-repair-001/implementation-001"', 'code-review-repair-002/implementation-001"')
text = text.replace('PREV = D.parent / "integration-002"', 'PREV = D.parent / "integration-003"')
text = text.replace('for stage in ["suite", "typing", "upstream"]:', 'for stage in ["suite", "typing"]:')
start = text.index('upstream = json.loads(')
end = text.index('demo = json.loads(', start)
text = text[:start] + '''upstream = json.loads((D / "UPSTREAM_APPLICABILITY.after.json").read_bytes())
assert upstream["carried_actual_checks"] == 9 and upstream["fresh_standalone_upstream_checks"] == 0
assert upstream["actual_filesystem_tree"] == upstream["pinned_tree"] == "6e11ed7cda0437ff12a29a328ca785e8915ddbc0"
summary["upstream_carried"] = {"checks": 9, "fresh_standalone_checks": 0,
    "actual_prior_report": upstream["carried_actual_report"],
    "applicability_before": loc(D / "UPSTREAM_APPLICABILITY.before.json"),
    "applicability_after": loc(D / "UPSTREAM_APPLICABILITY.after.json"),
    "limits": "Retained integration003 actual upstream result; fresh suite includes its named legacy upstream controls, but standalone9 was not rerun"}
''' + text[end:]
text = text.replace('"original": 242, "integration002": 254', '"original": 242, "integration002": 254, "integration003": 273')
text = text.replace('"selected_author_tests_not_added_to_total": 38', '"selected_author_tests_not_added_to_total": 35')

start = text.index('control_map = json.loads(')
end = text.index('# Relate executed test names', start)
block = '''# Reacquire prior19 source-selected discriminators as historical oracles, then bind current execution.
A1 = P / ".ai-workspace/qualification/t008/code-review-repair-001/implementation-001"
control_map = json.loads((A1 / "CONTROL_MAP.json").read_bytes())
prior_author_log = (A1 / "runs/004-final-selected/stderr").read_text()
prior_author_ids = set(re.findall(r"^test_\\w+ \\(([^)]+)\\) \\.\\.\\.", prior_author_log, re.M))
assert len(prior_author_ids) == 38 and prior_author_ids <= executed
author_execution = json.loads((A / "runs/003-final-focused/execution.json").read_bytes())
author_log = (A / "runs/003-final-focused/stderr").read_text()
author_ids = set(re.findall(r"^test_\\w+ \\(([^)]+)\\) \\.\\.\\.", author_log, re.M))
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
old_executed = set(re.findall(r"^test_\\w+ \\(([^)]+)\\) \\.\\.\\.", (PREV / "suite-001/stderr").read_text(), re.M))
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

'''
text = text[:start] + block + text[end:]
text = text.replace('old_source["sources"] + old_source["governing_sources"]', 'old_source["sources"] + old_source.get("governing_sources", [])')
text = text.replace('"changes_from_integration002"', '"changes_from_integration003"')
text = text.replace('"historical_integration002_witness_count"', '"historical_integration003_witness_count"')
text = text.replace('"historical_integration002_tests": 254', '"historical_integration002_tests": 254, "historical_integration003_tests": 273')
text = text.replace('"a_c.T008.mechanical-integration-results/3"', '"a_c.T008.mechanical-integration-results/4"')
text = text.replace('"a_c.T008.operation-scenario-map/3"', '"a_c.T008.operation-scenario-map/4"')
text = text.replace('"a_c.T008.closed-successor-source-manifest/3"', '"a_c.T008.closed-successor-source-manifest/4"')
start = text.index('report = f"""')
end = text.index('with (D / "REPORT.md").open', start)
text = text[:start] + '''report = f"""Integration-004 closed on the Root-selected repaired cut.

The single fresh full tenant run passed {count} tests with no skips in {match[0][1]}s. Fresh strict normal-import typing passed all9 selected files and the ordinary read-only CLI/MCP demo passed10 checks. The author's35 focused tests are a subset, not35 additional unique tests. The new8 methods and8 source-selected control rows are indexed alongside all prior19 controls reexecuted on current sources.

The standalone9 Graphify checks were not rerun. Their actual integration003 proof is carried with exact checker/codec/fixture and full1,064-member upstream source tree applicability, commit/tree, five entrypoints and selected Python/package versions verified before and after. Actual current legacy upstream controls still ran as part of the single full suite; these do not relabel the carried standalone result as fresh.

The nested required-P fold controls explicitly isolate the qualification gate and do not qualify a public operator. Writer lost-claim/history controls include actual CLI/MCP calls with test-only loss/fault injections; private completed-lookup, lock-callback and controlled Core cases retain their own lower-layer scope. Existing public retry and concurrent Writer/local actor-side MCP controls remain indexed as actual deterministic process evidence. Current work.write uses null plan; no Product or precomputed-plan integration patch was made.

The author's initial wrong-subject test assertion failure and its correction are preserved. Owning canonical OperationEvidence, raw transport records and passed unit assertions remain distinct. {len(missing)} declared operations still lack current owning witnesses. No all23-operation/F_P/FDV, publicly qualified operator, semantic/full-calculus, benefit, install or RC claim follows.

All{len(guards)} guarded historical/current members remain unchanged. Old273/254/242-test cuts and review002 F remain historical; the current independent review is separately owned and no pending verdict is asserted. Worker timeout/missing return, phase1 partial/unconsumable check and phase2 timeout histories persist. Binding002 remains historical/stale; no policy renewal/native-call budget is selected. No source/metadata edits, provider/native F_P calls, installs, network, Git commands or global changes were performed by this integration Worker.
"""
''' + text[end:]
start = text.index('save("CLOSED_RETURN.json",')
text = text[:start] + '''save("CLOSED_RETURN.json", {"schema": "a_c.T008.integration-successor-return/4", "state": "Closed finite current mechanical integration",
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
'''
with (D / "close_integration.py").open("x", encoding="utf-8") as stream:
    stream.write(text)
