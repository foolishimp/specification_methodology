"""Independent bounded checks of frozen actor artifacts; no actor checker is run.

Run with python3 -B run_artifact_probe.py --snapshot PATH --output REPORT.
The snapshot contains verified git-show copies; executable sources live beside
this script under probe_sources. All CLI work executes in /private/tmp.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    inputs = json.loads((here / "PROBE_INPUTS.json").read_bytes())
    started = datetime.now(timezone.utc)
    report = {
        "kind": "independent-required-artifact-proof",
        "basis": inputs["source_commit"],
        "task_packet_sha256": inputs["actor_packet_sha256"],
        "probe_script_sha256": digest(Path(__file__)),
        "probe_inputs_sha256": digest(here / "PROBE_INPUTS.json"),
        "started_utc": started.isoformat(),
        "arms": [],
        "limits": [
            "Semantic assertion grades are separate; actor self-check totals are unused.",
            "Supplemental arithmetic checks exercise the same admitted exact-integer contract; they are not extra acceptance criteria.",
            "No requirement to reject duplicate input identities is added: unique identities are an explicit Product input precondition.",
            "No categorical, universal capacity, general method or external-effect qualification follows from these finite probes.",
        ],
    }
    with tempfile.TemporaryDirectory(prefix="i3r2-code-probe-", dir="/private/tmp") as scratch:
        for arm in "ABC":
            result = args.snapshot / "arms" / arm / "result"
            executable = here / "probe_sources" / arm / "total_cents.py"
            assert executable.read_bytes() == (result / "total_cents.py").read_bytes()
            module_spec = importlib.util.spec_from_file_location("probe_" + arm, executable)
            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)
            p = getattr(module, {"A": "partition_total", "B": "partitioned_total", "C": "plan_p"}[arm])
            q = getattr(module, {"A": "candidate_q", "B": "candidate_q", "C": "plan_q"}[arm])
            r = module.total_cents
            record = {"arm": arm, "source_sha256": digest(executable), "required_cases": [], "supplemental": {}, "concrete_artifacts": []}
            for fixture, expected in zip(inputs["task2_cases"], inputs["task2_expected"]):
                values = {"p": p(fixture["input"], fixture["partition_record_ids"]),
                          "q": q(fixture["input"], fixture["partition_record_ids"]),
                          "r": r(fixture["input"])}
                cli = subprocess.run([sys.executable, "-B", str(executable)],
                                     input=json.dumps(fixture["input"]), text=True,
                                     capture_output=True, cwd=scratch, timeout=10)
                parsed = json.loads(cli.stdout) if cli.stdout else None
                match = values == {k: expected[k] for k in "pqr"}
                cli_match = cli.returncode == 0 and parsed["total_cents"] == expected["r"]
                record["required_cases"].append({
                    "case_id": fixture["case_id"], "observed": values,
                    "expected": {k: expected[k] for k in "pqr"}, "matches": match,
                    "cli": {"exit_code": cli.returncode, "stdout": cli.stdout,
                            "stderr": cli.stderr, "matches": cli_match},
                })
            failures = []
            dataset_count = 0
            partition_count = 0
            for n in range(5):
                for amounts in itertools.product((-2, 0, 2), repeat=n):
                    dataset_count += 1
                    data = [{"record_id": f"r{i}", "cents": v} for i, v in enumerate(amounts)]
                    expected = sum(amounts)
                    if r(data) != expected:
                        failures.append({"kind": "r", "input": data, "expected": expected})
                    ids = [row["record_id"] for row in data]
                    partitions = [[ids], [[], list(reversed(ids)), []], [[x] for x in reversed(ids)]]
                    partitions += [[ids[:cut], ids[cut:]] for cut in range(n + 1)]
                    for partition in partitions:
                        partition_count += 1
                        if p(data, partition) != expected:
                            failures.append({"kind": "p", "input": data, "partition": partition, "expected": expected})
            large = [{"record_id": "a", "cents": 10**80},
                     {"record_id": "b", "cents": 10**80},
                     {"record_id": "c", "cents": -(10**80)},
                     {"record_id": "d", "cents": -7}]
            large_observed = r(large)
            record["supplemental"] = {
                "admitted_datasets": dataset_count, "valid_partitions": partition_count,
                "failures": failures, "large_signed_multiplicity": {
                    "observed": large_observed, "expected": 10**80 - 7,
                    "matches": large_observed == 10**80 - 7},
            }
            # These are file-content observations, never a replay of result-writing scripts.
            index_names = ["current-index.json"] if arm != "C" else [f"current-index-W{i}.json" for i in (1, 2, 3)]
            for name in index_names:
                obj = json.loads((result / name).read_bytes())
                match = obj["dataset_revision"] == "data-2" and obj["ids"] == ["a", "b", "c"]
                record["concrete_artifacts"].append({"file": name, "sha256": digest(result / name), "value": obj, "matches": match})
            label_name = {"A": "label-I1.txt", "B": "I1-label.json", "C": "I1-label.txt"}[arm]
            label_path = result / label_name
            label_value = json.loads(label_path.read_bytes())["displayed_label"] if arm == "B" else label_path.read_text().strip()
            record["concrete_artifacts"].append({"file": label_name, "sha256": digest(label_path), "observed": label_value, "matches": label_value == "Maximum 1000 records"})
            config_name = "worker-config-I3.json" if arm == "A" else "I3-config.json"
            config = json.loads((result / config_name).read_bytes())
            record["concrete_artifacts"].append({"file": config_name, "sha256": digest(result / config_name), "value": config, "matches": config["worker_count"] == 2})
            record["required_artifact_observations_match"] = (
                all(x["matches"] and x["cli"]["matches"] for x in record["required_cases"])
                and all(x["matches"] for x in record["concrete_artifacts"]))
            report["arms"].append(record)
    report["finished_utc"] = datetime.now(timezone.utc).isoformat()
    report["elapsed_seconds"] = (datetime.now(timezone.utc) - started).total_seconds()
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"report": str(args.output), "arms": [
        {"arm": a["arm"], "required_artifact_observations_match": a["required_artifact_observations_match"],
         "supplemental_datasets": a["supplemental"]["admitted_datasets"],
         "supplemental_partitions": a["supplemental"]["valid_partitions"],
         "supplemental_failures": len(a["supplemental"]["failures"])} for a in report["arms"]]}))


if __name__ == "__main__":
    main()
