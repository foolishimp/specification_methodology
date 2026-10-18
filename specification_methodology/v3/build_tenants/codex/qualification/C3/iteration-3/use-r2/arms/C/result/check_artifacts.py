#!/usr/bin/env python3
"""Focused local checks for arm C's own synthetic artifacts.

This reads only artifacts constructed in the result directory. It does not
acquire method sources, other arms, hidden oracles or repository state.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
started = datetime.now(timezone.utc).isoformat()
checks = []
actual_outputs = []


def read_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def check(name, function):
    try:
        detail = function()
        checks.append({"name": name, "status": "passed", "detail": detail})
    except Exception as error:
        checks.append({"name": name, "status": "failed",
                       "error": type(error).__name__ + ": " + str(error)})


fixtures = read_json("fixtures.json")
answers = read_json("answers.json")
by_task = {task["task_id"]: task for task in fixtures["tasks"]}
answer_tasks = {task["task_id"]: task for task in answers["tasks"]}
spec = importlib.util.spec_from_file_location("arm_c_total_cents", ROOT / "total_cents.py")
realization = importlib.util.module_from_spec(spec)
spec.loader.exec_module(realization)


def source_integrity():
    verified = []
    for task in fixtures["tasks"]:
        for source in task["initial_fixture_state"]["sources"]:
            body = json.dumps(source["content"], sort_keys=True, separators=(",", ":"),
                              ensure_ascii=False).encode("utf-8")
            assert len(body) == source["content_bytes"], source["source_id"]
            assert hashlib.sha256(body).hexdigest() == source["content_sha256"], source["source_id"]
            verified.append(source["source_id"])
    return {"fixture_sources_verified": verified,
            "scope": "Canonical retained fixture payloads only; not semantic proof or installed-method verification."}


def case_and_citation_coverage():
    assert set(answer_tasks) == set(by_task) == {"T1", "T2", "T3", "T4", "T5", "T6"}
    method_ids = {m["id"] for m in answers["source_citations"]["method_sources"]}
    source_ids = {s["source_id"] for s in answers["source_citations"]["fixture_sources"]}
    coverage = {}
    for task_id, source in by_task.items():
        wanted = [case["case_id"] for case in source["initial_fixture_state"]["cases"]]
        actual = [case["case_id"] for case in answer_tasks[task_id]["cases"]]
        assert actual == wanted, (task_id, wanted, actual)
        for case in answer_tasks[task_id]["cases"]:
            assert case["fixture_citations"] and case["method_citations"]
            assert set(case["method_citations"]) <= method_ids, case["case_id"]
            assert any(citation in source_ids for citation in case["fixture_citations"]), case["case_id"]
            assert "dependencies" in case and "unresolved" in case, case["case_id"]
        coverage[task_id] = actual
    return coverage


def fixture_plan_outputs():
    expected = {"K1": {"p": 5, "q": 1, "r": 5},
                "K2": {"p": 0, "q": 0, "r": 0},
                "K3": {"p": 5, "q": 5, "r": 5}}
    for case in by_task["T2"]["initial_fixture_state"]["cases"]:
        records, partitions = case["input"], case["partition_record_ids"]
        output = {"p": realization.plan_p(records, partitions),
                  "q": realization.plan_q(records, partitions),
                  "r": realization.total_cents(records)}
        assert output == expected[case["case_id"]], (case["case_id"], output)
        row = next(row for row in answer_tasks["T2"]["cases"] if row["case_id"] == case["case_id"])
        assert row["outputs"] == output
        actual_outputs.append({"case_id": case["case_id"], "actual": output,
                               "required_total_cents": row["required_total_cents"]})
    return actual_outputs


def exact_integer_edges():
    huge = 2 ** 100
    records = [{"record_id": "h1", "cents": huge},
               {"record_id": "h2", "cents": huge},
               {"record_id": "h3", "cents": -1}]
    assert realization.total_cents(records) == 2 ** 101 - 1
    assert realization.total_cents([]) == 0
    assert realization.total_cents([{"record_id": "negative", "cents": -7}]) == -7
    return {"large_equal_amounts_total": 2 ** 101 - 1, "empty": 0, "negative": -7,
            "claim": "Exact tested integers exceed fixed 64-bit range; no floating-point conversion."}


def invalid_partitions():
    records = by_task["T2"]["initial_fixture_state"]["cases"][0]["input"]
    trials = {"duplicate": [["r1", "r1"], ["r2", "r3"]],
              "omitted": [["r1"], ["r2"]],
              "unknown": [["r1", "r2"], ["r3", "not-an-input-id"]]}
    results = {}
    for name, partitions in trials.items():
        try:
            realization.plan_p(records, partitions)
        except ValueError as error:
            results[name] = str(error)
        else:
            raise AssertionError("invalid partition accepted: " + name)
    return results


def cli_use():
    records = by_task["T2"]["initial_fixture_state"]["cases"][0]["input"]
    process = subprocess.run([sys.executable, "-B", str(ROOT / "total_cents.py")],
                             input=json.dumps(records), capture_output=True, text=True,
                             cwd=ROOT, check=False)
    assert process.returncode == 0, process.stderr
    output = json.loads(process.stdout)
    assert output == {"status": "successful", "total_cents": 5}, output
    return {"exit_code": process.returncode, "stdout": output}


def cli_rejects_inexact_input():
    process = subprocess.run([sys.executable, "-B", str(ROOT / "total_cents.py")],
                             input=json.dumps([{"record_id": "bad", "cents": 1.5}]),
                             capture_output=True, text=True, cwd=ROOT, check=False)
    output = json.loads(process.stdout)
    assert process.returncode == 2 and output["status"] == "refused", output
    assert "total_cents" not in output
    return {"exit_code": process.returncode, "stdout": output,
            "standing": "Expected refusal retained; no approximate successful total."}


def current_indices_and_retained_style():
    workspace = next(s["content"] for s in by_task["T5"]["initial_fixture_state"]["sources"]
                     if s["source_id"] == "W.workspace")
    expected = sorted(record["id"] for record in workspace["current_dataset"]["records"])
    results = []
    for case in answer_tasks["T5"]["cases"]:
        index = read_json(case["current_index_artifact"])
        handoff = read_json(case["artifact"])
        assert index["ids"] == expected == ["a", "b", "c"]
        assert index["dataset_revision"] == workspace["current_dataset"]["revision"] == "data-2"
        assert index["complete"] is True
        assert handoff["style_reuse"]["assessment"] == workspace["style_assessment"]
        assert handoff["external_effects_performed_by_actor"] == []
        results.append({"case_id": case["case_id"], "index": index["ids"],
                        "retained_style_evidence": handoff["style_reuse"]["assessment"]["evidence"]})
    return results


def local_intake_results():
    product = next(s["content"] for s in by_task["T6"]["initial_fixture_state"]["sources"]
                   if s["source_id"] == "I.product")
    label = (ROOT / "I1-label.txt").read_text(encoding="utf-8").strip()
    config = read_json("I3-config.json")
    assert label == "Maximum " + str(product["maximum_export_records"]) + " records"
    assert config["worker_count"] == 2
    assert product["worker_count_range"][0] <= config["worker_count"] <= product["worker_count_range"][1]
    assert read_json("I2-product-change-intake.json")["result"]["maximum_export_records"] == 1000
    assert read_json("I4-unresolved-intake.json")["result"]["concrete_configuration_change"] is None
    return {"label": label, "configuration": config,
            "unadmitted_cases": "I2 retains current Product maximum; I4 invents no configuration."}


def component_evidence_preservation():
    ledger = read_json("assessment-ledger.json")
    expected = {"E1": ["obs-41", "obs-42"], "E2": ["obs-41", "obs-43", "obs-44"],
                "E3": ["obs-45", "obs-43", "obs-44"]}
    for case in ledger["cases"]:
        assert len(case["components"]) == 3
        assert [o["id"] for o in case["observations"]] == expected[case["case_id"]]
    return {"component_rows": 9, "scope": "Independent-case observations retained without catalogue leakage."}


def result_pair_validation():
    verdicts = {"satisfied", "falsified", "indeterminate", "out_of_frame", "invalid_basis"}
    count = 0
    def visit(value):
        nonlocal count
        if isinstance(value, dict):
            if "verdict" in value and "performance" in value:
                assert value["verdict"] in verdicts, value["verdict"]
                assert value["performance"] in {"performed", "not_performed", "unconfirmed"}
                assert value["verdict"] != "satisfied" or value["performance"] == "performed"
                count += 1
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)
    visit(answers["tasks"])
    return {"result_pairs_checked": count, "scope": "Structural legal-pair check; not semantic proof."}


task_files = sorted({name for task in answers["tasks"] for name in task["artifacts"]})
support_files = ["answers.json", "fixtures.json", "source-citations.json",
                 "acquisition-records.json", "authoring-observations.json", "check_artifacts.py"]


def artifact_references():
    for name in task_files + support_files:
        assert "/" not in name and (ROOT / name).is_file(), name
        if name.endswith(".json"):
            read_json(name)
    return {"artifact_files_checked": len(task_files + support_files), "task_artifacts": task_files}


check("retained_fixture_source_hashes", source_integrity)
check("all_six_tasks_and_21_cases_with_sources", case_and_citation_coverage)
check("all_supplied_plan_outputs", fixture_plan_outputs)
check("exact_integer_and_identity_sensitive_edges", exact_integer_edges)
check("invalid_partition_preconditions_refused", invalid_partitions)
check("usable_cli_success", cli_use)
check("usable_cli_inexact_input_refusal", cli_rejects_inexact_input)
check("current_index_and_independent_style_reuse", current_indices_and_retained_style)
check("authorized_local_intake_artifacts", local_intake_results)
check("component_and_case_evidence_preservation", component_evidence_preservation)
check("core_result_legal_pairs", result_pair_validation)
check("artifact_references_and_json_parse", artifact_references)

hashes = []
for name in sorted(set(task_files + support_files)):
    path = ROOT / name
    if path.is_file():
        data = path.read_bytes()
        hashes.append({"path": name, "bytes": len(data),
                       "sha256": hashlib.sha256(data).hexdigest()})
report = {"schema": "arm-C.artifact-checks.v1",
          "started_at_utc": started,
          "ended_at_utc": datetime.now(timezone.utc).isoformat(),
          "status": "passed" if all(c["status"] == "passed" for c in checks) else "failed",
          "checks": checks, "plan_outputs": actual_outputs, "artifact_hashes": hashes,
          "measurement_class": "Administrative artifact checking and hashing, separate from ordinary acquisition.",
          "limits": ["Self-checks of this finite synthetic return; no independent review or acceptance.",
                     "Mathematical preservation arguments are in construction-derivation.json.",
                     "No categorical construction qualification, installed/native-host proof, spend, token, attention or universal capacity measurement."]}
(ROOT / "artifact-checks.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                                          encoding="utf-8")
print(json.dumps({"status": report["status"], "checks": len(checks),
                  "failed": [c for c in checks if c["status"] == "failed"],
                  "plan_outputs": actual_outputs}, indent=2))
raise SystemExit(0 if report["status"] == "passed" else 1)

