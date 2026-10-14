"""Bounded, replayable artifact checks; this is self-check evidence, not review."""
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

from total_cents import total_cents, partitioned_total, candidate_q

BASE = Path(__file__).resolve().parent
FIXTURES = json.loads("[{\"case_id\":\"K1\",\"input\":[{\"record_id\":\"r1\",\"cents\":4},{\"record_id\":\"r2\",\"cents\":4},{\"record_id\":\"r3\",\"cents\":-3}],\"partition_record_ids\":[[\"r1\",\"r2\"],[\"r3\"]]},{\"case_id\":\"K2\",\"input\":[],\"partition_record_ids\":[[],[]]},{\"case_id\":\"K3\",\"input\":[{\"record_id\":\"r4\",\"cents\":8},{\"record_id\":\"r5\",\"cents\":-8},{\"record_id\":\"r6\",\"cents\":5}],\"partition_record_ids\":[[\"r4\"],[\"r5\",\"r6\"]]}]")
EXPECTED = {"K1": {"p": 5, "q": 1, "r": 5},
            "K2": {"p": 0, "q": 0, "r": 0},
            "K3": {"p": 5, "q": 5, "r": 5}}
checks = []
outputs = []


def check(name, condition, detail=None):
    checks.append({"name": name, "passed": bool(condition), "detail": detail})


def rejects(name, operation):
    try:
        value = operation()
        check(name, False, {"unexpected_return": value})
    except ValueError as error:
        check(name, True, {"rejection": str(error)})
    except Exception as error:
        check(name, False, {"wrong_exception": type(error).__name__, "message": str(error)})


for fixture in FIXTURES:
    actual = {
        "p": partitioned_total(fixture["input"], fixture["partition_record_ids"]),
        "q": candidate_q(fixture["input"], fixture["partition_record_ids"]),
        "r": total_cents(fixture["input"]),
    }
    expected = EXPECTED[fixture["case_id"]]
    check(fixture["case_id"] + " concrete p/q/r outputs", actual == expected,
          {"expected": expected, "actual": actual})
    outputs.append({"case_id": fixture["case_id"],
                    "expected_contract_total": expected["r"],
                    "actual_outputs": actual,
                    "q_contract_conformance": actual["q"] == expected["r"]})

check("K1 is a retained q counterexample",
      outputs[0]["actual_outputs"]["q"] != outputs[0]["expected_contract_total"],
      {"q": 1, "required": 5, "lost_occurrence": "r2 contributes a separate +4"})

large = 10 ** 100
large_records = [{"record_id": "a", "cents": large},
                 {"record_id": "b", "cents": large},
                 {"record_id": "c", "cents": -1}]
large_expected = 2 * large - 1
check("r preserves a total above fixed-width integer ranges",
      total_cents(large_records) == large_expected)
check("p preserves a total above fixed-width integer ranges",
      partitioned_total(large_records, [["a", "b"], ["c"]]) == large_expected)
check("negative-only total",
      total_cents([{"record_id": "n1", "cents": -4},
                   {"record_id": "n2", "cents": -7}]) == -11)

records = FIXTURES[0]["input"]
rejects("duplicate partition occurrence refused",
        lambda: partitioned_total(records, [["r1", "r1"], ["r3"]]))
rejects("omitted partition occurrence refused",
        lambda: partitioned_total(records, [["r1"], ["r3"]]))
rejects("foreign partition identity refused",
        lambda: partitioned_total(records, [["r1", "r2"], ["foreign"]]))
rejects("duplicate input identity refused",
        lambda: total_cents([{"record_id": "x", "cents": 1},
                            {"record_id": "x", "cents": 2}]))
rejects("float coercion refused",
        lambda: total_cents([{"record_id": "x", "cents": 1.5}]))
rejects("bool-as-int coercion refused",
        lambda: total_cents([{"record_id": "x", "cents": True}]))

command = [sys.executable, "-B", str(BASE / "total_cents.py")]
cli = subprocess.run(command, input=json.dumps(records), capture_output=True, text=True)
check("usable stdin CLI computes K1", cli.returncode == 0 and
      json.loads(cli.stdout) == {"total_cents": 5},
      {"command": command, "exit_code": cli.returncode, "stdout": cli.stdout.strip(),
       "stderr": cli.stderr})

bad_cli = subprocess.run(command, input='[{"record_id":"x","cents":1.5}]',
                         capture_output=True, text=True)
check("CLI refuses approximation input", bad_cli.returncode == 2 and
      json.loads(bad_cli.stdout)["outcome"] == "rejected",
      {"exit_code": bad_cli.returncode, "stdout": bad_cli.stdout.strip()})

(BASE / "computed-totals.json").write_text(json.dumps({
    "task_id": "T2", "kind": "actual local execution",
    "case_outputs": outputs, "selected_realization": "r",
    "counterexample_preserved": "K1 q outputs 1; contract requires 5."
}, indent=2) + "\n")

required = [
    "answers.json", "assessment-ledger.json", "construction-assessment.json",
    "domain-results.json", "release-adoption-memo.json", "current-index.json",
    "recovery-W1.json", "recovery-W2.json", "recovery-W3.json",
    "intake-records.json", "I1-label.json", "I3-config.json",
    "method-citations.json", "acquisition-record.json", "computed-totals.json",
]
parsed = {}
for name in required:
    try:
        parsed[name] = json.loads((BASE / name).read_text())
        check("JSON readable: " + name, True)
    except Exception as error:
        check("JSON readable: " + name, False, str(error))

answers = parsed["answers.json"]
expected_cases = {
    "T1": ["E1", "E2", "E3"], "T2": ["K1", "K2", "K3"],
    "T3": ["D1", "D2", "D3", "D4"], "T4": ["L1", "L2", "L3", "L4"],
    "T5": ["W1", "W2", "W3"], "T6": ["I1", "I2", "I3", "I4"],
}
actual_cases = {task["task_id"]: [case["case_id"] for case in task["cases"]]
                for task in answers["tasks"]}
check("all six tasks and all 21 named cases present", actual_cases == expected_cases,
      actual_cases)
fixture_ids = {item["source_id"] for item in answers["fixture_sources"]}
method_ids = set(answers["method_sources"])
all_case_citations_resolve = all(
    set(case["fixture_sources"]) <= fixture_ids and
    set(case["method_citations"]) <= method_ids
    for task in answers["tasks"] for case in task["cases"]
)
check("every answer case cites registered fixture and method sources",
      all_case_citations_resolve)

artifact_paths = [name for task in answers["tasks"] for name in task["artifacts"]]
check("every named usable artifact exists",
      all((BASE / name).is_file() for name in artifact_paths), artifact_paths)

pointer_failures = []
for task in answers["tasks"]:
    for case in task["cases"]:
        parts = case["artifact_pointer"].split("#", 1)
        try:
            node = json.loads((BASE / parts[0]).read_text())
            if len(parts) == 2:
                for part in parts[1].strip("/").split("/"):
                    node = node[int(part)] if isinstance(node, list) else node[part]
            if node["case_id"] != case["case_id"]:
                pointer_failures.append(case["case_id"] + ": identity mismatch")
        except Exception as error:
            pointer_failures.append(case["case_id"] + ": " + str(error))
check("all 21 detailed case pointers resolve", not pointer_failures, pointer_failures)

verdicts = {"satisfied", "falsified", "indeterminate", "out_of_frame", "invalid_basis"}
performances = {"performed", "not_performed", "unconfirmed"}
effect_values = {"not_requested", "not_started", "completed", "partial", "reverted", "unknown"}
core_failures = []
core_count = 0


def inspect(value, path):
    global core_count
    if isinstance(value, dict):
        if {"predicate", "subject", "basis", "verdict", "performance"} <= set(value):
            core_count += 1
            if value["verdict"] not in verdicts or value["performance"] not in performances:
                core_failures.append(path + ": unknown verdict/performance")
            if value["verdict"] == "satisfied" and value["performance"] != "performed":
                core_failures.append(path + ": satisfaction without performed evaluation")
            if value.get("effects", {}).get("observation") not in effect_values:
                core_failures.append(path + ": missing/invalid effect observation")
            if not {"original_domain_outcome", "evidence", "unresolved_obligations"} <= set(value):
                core_failures.append(path + ": missing semantic result fields")
        for key, child in value.items():
            inspect(child, path + "/" + key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            inspect(child, path + "/" + str(index))


for name, value in parsed.items():
    inspect(value, name)
check("native core result records retain required coordinates and legal pairs",
      not core_failures, {"records": core_count, "failures": core_failures})
check("current index is complete for data-2 and sorted",
      parsed["current-index.json"] == {
          "dataset_revision": "data-2", "ids": ["a", "b", "c"], "complete": True})
check("I1 concrete label", parsed["I1-label.json"] == {"displayed_label": "Maximum 1000 records"})
check("I3 concrete configuration", parsed["I3-config.json"] == {"worker_count": 2})

report = {
    "schema": "arm-B-local-artifact-checks.v1",
    "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    "authority": "Self-check of this initial bounded return; no oracle, other arm or independent review used.",
    "checks": checks,
    "summary": {"passed": sum(item["passed"] for item in checks),
                "failed": sum(not item["passed"] for item in checks),
                "total": len(checks)},
    "limits": ["Finite execution checks supplement the mathematical argument; they do not establish universal resource fit.",
               "Schema/reference checks do not independently establish semantic correctness.",
               "The q counterexample and all refusal observations are retained."]
}
(BASE / "artifact-checks.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report["summary"]))
raise SystemExit(0 if report["summary"]["failed"] == 0 else 1)
