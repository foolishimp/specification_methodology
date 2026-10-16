"""Focused local artifact and integer-contract checks for the initial return."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys

from total_cents import candidate_q, partition_total, total_cents


ROOT = Path(__file__).resolve().parent
RESULTS = []


def check(name, operation):
    try:
        detail = operation()
    except Exception as error:
        RESULTS.append({"name": name, "passed": False, "error_type": type(error).__name__, "error": str(error)})
    else:
        RESULTS.append({"name": name, "passed": True, "detail": detail})


def require(value, message):
    if not value:
        raise AssertionError(message)


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def inventory_check():
    answers = load("answers.json")
    expected = {"T1": ["E1", "E2", "E3"], "T2": ["K1", "K2", "K3"], "T3": ["D1", "D2", "D3", "D4"], "T4": ["L1", "L2", "L3", "L4"], "T5": ["W1", "W2", "W3"], "T6": ["I1", "I2", "I3", "I4"]}
    require([task["task_id"] for task in answers["tasks"]] == list(expected), "Task inventory differs")
    for task in answers["tasks"]:
        require([case["case_id"] for case in task["cases"]] == expected[task["task_id"]], "Case inventory differs")
        for case in task["cases"]:
            require(bool(case["dependencies"]), "Missing dependencies")
            require("unresolved" in case, "Missing unresolved field")
            require(bool(case["fixture_sources"]) and bool(case["method_sources"]), "Missing citations")
            for source in case["fixture_sources"]:
                require(source in answers["fixture_source_registry"], f"Unknown fixture citation {source}")
            for source in case["method_sources"]:
                require(source in answers["method_source_registry"], f"Unknown method citation {source}")
        for name in task["artifacts"]:
            require((ROOT / name).is_file(), f"Missing artifact {name}")
            if name.endswith(".json"):
                load(name)
    return {"tasks": 6, "cases": 21, "citation_and_artifact_links": "resolved within result records"}


def supplied_sum_cases():
    rows = load("total-cents-output.json")
    expected = {"K1": {"p": 5, "q": 1, "r": 5}, "K2": {"p": 0, "q": 0, "r": 0}, "K3": {"p": 5, "q": 5, "r": 5}}
    for row in rows:
        actual = {"p": partition_total(row["input"], row["partition_record_ids"]), "q": candidate_q(row["input"], row["partition_record_ids"]), "r": total_cents(row["input"])}
        require(actual == expected[row["case_id"]], f"Unexpected computed totals for {row['case_id']}")
        require(row["outputs"] == actual, "Persisted output differs from execution")
    return expected


def mathematical_edges():
    records = [{"record_id": "one", "cents": 4}, {"record_id": "two", "cents": 4}]
    require(total_cents(records) == 8 and partition_total(records, [["one", "two"]]) == 8, "Equal amounts were collapsed")
    require(candidate_q(records, [["one", "two"]]) == 4, "Counterexample no longer reproduces supplied q")
    big = 2 ** 100
    huge = [{"record_id": "x", "cents": big}, {"record_id": "y", "cents": big}, {"record_id": "z", "cents": -1}]
    require(total_cents(huge) == 2 ** 101 - 1, "Exact arithmetic failed beyond fixed 64-bit range")
    require(partition_total(huge, [["z"], [], ["y", "x"]]) == 2 ** 101 - 1, "Partition order/empty conservation failed")
    require(total_cents([]) == 0 and partition_total([], []) == 0 and partition_total([], [[], []]) == 0, "Empty identity failed")
    require(total_cents([{"record_id": "n", "cents": -3}]) == -3, "Negative amount failed")
    return {"equal_amounts": "8 retained; q gives 4", "large_integer_expected": 2 ** 101 - 1, "empty": 0, "negative": -3}


def partition_refusals():
    records = [{"record_id": "x", "cents": 1}, {"record_id": "y", "cents": 1}]
    candidates = {"omitted": [["x"]], "duplicate_with_same_numerical_total": [["x", "x"]], "foreign": [["x", "y", "z"]]}
    for name, parts in candidates.items():
        try:
            partition_total(records, parts)
        except ValueError:
            continue
        raise AssertionError(f"Invalid partition accepted: {name}")
    return {name: "refused" for name in candidates}


def cli_check():
    records = [{"record_id": "r1", "cents": 4}, {"record_id": "r2", "cents": 4}, {"record_id": "r3", "cents": -3}]
    run = subprocess.run([sys.executable, "-B", str(ROOT / "total_cents.py")], input=json.dumps(records), text=True, capture_output=True)
    require(run.returncode == 0 and json.loads(run.stdout) == {"total_cents": 5}, "CLI result failed")
    invalid = subprocess.run([sys.executable, "-B", str(ROOT / "total_cents.py")], input='[{"record_id":"r1","cents":1.5}]', text=True, capture_output=True)
    require(invalid.returncode == 2 and not invalid.stdout, "Noninteger input was reported as a successful total")
    return {"valid_input_stdout": json.loads(run.stdout), "valid_exit": run.returncode, "noninteger_exit": invalid.returncode, "noninteger_error": json.loads(invalid.stderr)}


def artifact_integrity():
    index = load("current-index.json")
    require(index == {"dataset_revision": "data-2", "ids": ["a", "b", "c"], "complete": True}, "Current complete index differs")
    digest = hashlib.sha256((ROOT / "current-index.json").read_bytes()).hexdigest()
    for case_id in ("W1", "W2", "W3"):
        handoff = load(f"recovery-handoff-{case_id}.json")
        require(handoff["performed_local_construction"]["sha256"] == digest, "Index hash link differs")
        require(handoff["actual_external_effects"] == [], "External effect recorded as performed")
    require((ROOT / "label-I1.txt").read_text() == "Maximum 1000 records\n", "Label differs")
    require(load("worker-config-I3.json") == {"worker_count": 2}, "Worker config differs")
    return {"index": index, "index_sha256": digest, "label": "Maximum 1000 records", "worker_count": 2}


def ledger_evidence_scope():
    ledger = load("assessment-ledger.json")
    by_case = {case["case_id"]: case for case in ledger["cases"]}
    for case in ledger["cases"]:
        require([r["check"] for r in case["components"]] == ["checksum", "retention", "access"], "Required check missing")
    e1 = {row["check"]: row for row in by_case["E1"]["components"]}
    require(e1["checksum"]["supporting_records"][0]["evidence"] == "obs-41", "Adverse observation lost")
    require(e1["access"]["supporting_records"][0]["subject"] == "urn:fixture:bundle:16", "Wrong-subject observation overwritten")
    e3_evidence = [entry["evidence"] for row in by_case["E3"]["components"] for entry in row["supporting_records"]]
    require("obs-41" not in e3_evidence and "obs-45" in e3_evidence, "Independent case evidence leaked")
    return {"required_rows_per_case": 3, "E1_adverse_and_wrong_subject_records": "preserved", "E3_case_scope": e3_evidence}


if __name__ == "__main__":
    for name, operation in [
        ("six_tasks_and_21_cases_with_resolved_artifact_and_citation_links", inventory_check),
        ("all_nine_supplied_plan_outputs", supplied_sum_cases),
        ("multiplicity_negative_empty_and_large_integer_preservation", mathematical_edges),
        ("invalid_identity_partitions_refused", partition_refusals),
        ("usable_CLI_and_noninteger_refusal", cli_check),
        ("current_index_hashes_and_concrete_local_artifacts", artifact_integrity),
        ("component_ledger_preserves_case_scoped_observations", ledger_evidence_scope),
    ]:
        check(name, operation)
    report = {"checked_at_utc": datetime.now(timezone.utc).isoformat(), "checks": RESULTS, "passed": all(row["passed"] for row in RESULTS), "independence": "Constructor self-checks; no independent review or live Product qualification is claimed."}
    (ROOT / "artifact-checks.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report))
    raise SystemExit(0 if report["passed"] else 1)
