"""Append a factual closed comparison subject, preserving all native output."""
from pathlib import Path
import argparse
import json
import sys

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
from prepare_native import sha, snapshot, write
from check_returns import check


def read(path):
    return json.loads(Path(path).read_text())


def ref(path):
    return {"path": str(path), "sha256": sha(path)}


parser = argparse.ArgumentParser()
parser.add_argument("--host", choices=("codex", "claude"), required=True)
args = parser.parse_args()
selection = read(HERE / "attempt-06/coverage-selection.json")
context = next(row for row in selection["contexts"] if row["host"] == args.host)
evidence, work = Path(context["directory"]), Path(context["worksite"])
destination = HERE / ("evaluation-subject-role-transition-" + args.host + ".json")
assert not destination.exists(), "Refuse replacing closed comparison"
receipt = read(evidence / "execution-result.json")
for name, digest in receipt["files"].items():
    assert sha(evidence / name) == digest, "Execution record drift: " + name
assert snapshot(work) == read(evidence / "snapshot-after.json"), "Post-return worksite drift"
mechanics_path = evidence / "return-mechanics.json"
if mechanics_path.exists():
    raise RuntimeError("Return mechanics already recorded; inspect rather than overwrite")
mechanics = check(context)
original_path = HERE / ("evaluation-subject-" + args.host + ".json")
original = read(original_path)
source = next(row for row in original["contexts"] if row["presentation"] == "source")
for row in source["evidence"]:
    assert sha(row["path"]) == row["sha256"], "Fixed source evidence drift"
names = ["prompt.txt", "command.json", "confinement-preflight.json", "stdout.jsonl", "stderr.txt", "final.txt", "host-metadata.json", "execution-result.json", "snapshot-before.json", "snapshot-after.json", "return-mechanics.json"]
new = {"name": context["name"], "host": args.host, "presentation": "map-first", "model_configuration": context["models"][args.host], "worksite": str(work), "frozen_inputs": ref(evidence / "snapshot-before.json"), "evidence": [ref(evidence / name) for name in names if (evidence / name).is_file()]}
inputs_path = HERE / "evaluation-subject-role-transition-inputs.json"
inputs = read(inputs_path)
value = {"kind": "stdo.native-changed-guidance-comparison-subject", "scope": "Closed fresh explicit role-transition guidance map observation against the fixed first source observation; no expected verdict or semantic grade. Every earlier native return and transport record remains retained.", "host": args.host, "contexts": [source, new], "source_control_reused": True, "frozen_input_subject": ref(inputs_path), "fixed_source_controls": ref(HERE / "fixed-source-controls.json"), "original_pair": ref(original_path), "prior_pair_manifests": inputs["prior_pair_manifests"], "original_cohort_locators": ref(HERE / "original-cohort-locators.json"), "new_cohort": ref(work / "native/cohort.json"), "fixture_evidence": original["fixture_evidence"], "return_mechanics_checker": ref(HERE / "check_returns.py"), "source_basis": inputs["source_basis"]}
write(destination, value)
print(json.dumps({"manifest": ref(destination), "execution_receipt": ref(evidence / "execution-result.json"), "host": args.host, "exit_code": receipt["exit_code"], "timed_out": receipt["timed_out"], "duration_seconds": receipt["duration_seconds"], "worksite_changes": receipt["snapshot_changes"], "nonsemantic_transport_unchanged": receipt["nonsemantic_transport_unchanged"], "return_mechanics": mechanics["status"]}, indent=2))
