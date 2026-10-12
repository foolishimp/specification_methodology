"""Append the factual execution return and freeze this generation after closure."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
from prepare_native import sha, snapshot, write
from run_native import transport_state


def read(path):
    return json.loads(Path(path).read_text())


def ref(path):
    return {"path": str(path), "sha256": sha(path)}


def member(path):
    relative = str(path.relative_to(HERE))
    if path.is_symlink():
        target = os.readlink(path)
        return {"path": relative, "type": "symlink", "sha256": hashlib.sha256(target.encode()).hexdigest(), "target": target}
    return {"path": relative, "type": "file", "sha256": sha(path), "bytes": path.stat().st_size}


outputs = [HERE / "runtime-ignore-check-attempt-05.json", HERE / "execution-summary-attempt-05.json", HERE / "README-attempt-05.md", HERE / "output-freeze-attempt-05.json"]
assert not any(path.exists() for path in outputs), "Refuse replacing appended return"
selection_path = HERE / "attempt-05/coverage-selection.json"
selection = read(selection_path)
binding = read(HERE / "candidate-binding-read-only-streams.json")
base_path = HERE / "output-freeze.json"
assert sha(base_path) == "b28e9bd37e1705ff410872e4119702d9369a41a0d2e3eba0899a15c66e217df4"
base = read(base_path)
for prior in base["members"]:
    assert member(HERE / prior["path"]) == prior, "Frozen member drift: " + prior["path"]

observations, comparisons = [], []
for context in selection["contexts"]:
    evidence, work = Path(context["directory"]), Path(context["worksite"])
    result = read(evidence / "execution-result.json")
    for name, digest in result["files"].items():
        assert sha(evidence / name) == digest, "Receipt drift: " + name
    assert snapshot(work) == read(evidence / "snapshot-after.json")
    assert transport_state(context) == context["nonsemantic_transport"], "Existing installation identity changed"
    comparison = HERE / ("evaluation-subject-read-only-streams-" + context["host"] + ".json")
    assert comparison.is_file(), "Closed comparison manifest missing"
    comparisons.append(ref(comparison))
    preflight = read(evidence / "confinement-preflight.json")
    metadata = read(evidence / "host-metadata.json")
    mechanics_path = evidence / "return-mechanics.json"
    mechanics = read(mechanics_path)
    identity = [{key: row[key] for key in ("type", "subtype", "model", "claude_code_version") if key in row} for row in metadata if "model" in row or "claude_code_version" in row]
    usage = [{key: row[key] for key in ("type", "usage", "total_cost_usd", "modelUsage", "num_turns", "duration_ms", "duration_api_ms") if key in row} for row in metadata if "usage" in row]
    observations.append({"attempt": "attempt-05", "context": context["name"], "host": context["host"], "presentation": context["arm"], "requested_model_configuration": context["models"][context["host"]], "host_version": next(row["stdout"].strip() for row in preflight["checks"] if row["operation"] == "host_version"), "host_reported_identity": identity, "exit_code": result["exit_code"], "timed_out": result["timed_out"], "duration_seconds": result["duration_seconds"], "worksite_changes": result["snapshot_changes"], "nonsemantic_transport_unchanged": result["nonsemantic_transport_unchanged"], "final_present": (evidence / "final.txt").is_file(), "reported_usage": usage, "execution_receipt": ref(evidence / "execution-result.json"), "host_metadata": ref(evidence / "host-metadata.json"), "mechanical_return_receipt": dict(ref(mechanics_path), status=mechanics["status"])})

repo = Path("/Users/jim/src/apps/specification_methodology")
relative_root = HERE.relative_to(repo)
runtime_dirs = sorted(path for path in HERE.glob("*/**/runtime") if path.is_dir())
runtime_relatives = [str(path.relative_to(repo)) + "/" for path in runtime_dirs]
command = ["git", "-C", str(repo), "check-ignore", "--verbose", "--stdin"]
ignored = subprocess.run(command, input="\n".join(runtime_relatives) + "\n", capture_output=True, text=True, check=False)
listed = subprocess.run(["git", "-C", str(repo), "ls-files", "-z", "--", str(relative_root)], capture_output=True, text=True, check=True)
tracked_private = [path for path in listed.stdout.split("\0") if path and "runtime" in Path(path).parts]
assert ignored.returncode == 0 and len(ignored.stdout.splitlines()) == len(runtime_relatives)
assert not tracked_private, "Private runtime entered the Git index"
ignore_receipt = {"scope": "Read-only Git ignore/index inspection; no staging or Git mutation", "command": command, "exit_code": ignored.returncode, "stdout": ignored.stdout, "stderr": ignored.stderr, "private_runtime_directory_count": len(runtime_dirs), "all_recognized_ignored": True, "tracked_private_runtime_paths": tracked_private, "ignore_file_sha256": sha(HERE / ".gitignore")}
write(outputs[0], ignore_receipt)

summary = {"kind": "stdo.native-appended-execution-observations", "recorded_at": datetime.now(timezone.utc).isoformat(), "status": "Both selected attempt-05 processes closed; factual Worker return only", "subject": {"source_manifest_sha256": binding["source_manifest_sha256"], "cohort_sha256": binding["cohort_sha256"], "skill_sha256": binding["comparison"]["changed_representation_members"][0]["after"]["sha256"]}, "prior_complete_observation_population": ref(HERE / "execution-summary.json"), "prior_generation_freeze": ref(base_path), "attempt_class": "Two fresh all-command read-only guidance map observations, with the fixed first source controls reused and every earlier result preserved", "pre_exposure_preparation_record": ref(HERE / "attempt-05/preparation-record.json"), "observations": observations, "frozen_input_subject": ref(HERE / "evaluation-subject-read-only-streams-inputs.json"), "fixed_source_controls": ref(HERE / "fixed-source-controls.json"), "closed_comparison_subjects": comparisons, "runtime_ignore_check": ref(outputs[0]), "custody": {"prior_1607_members_unchanged": True, "prior_freeze_manifest_unchanged": True, "all_selected_processes_closed": True, "installation_identity_unchanged": True, "credentials_copied": False, "HOME_or_CODEX_HOME_repurposed": False, "private_runtime_directories_ignored": len(runtime_dirs)}, "limits": ["Return structure and exact join replay are mechanical observations, not semantic acceptance or read-only-grant compliance judgments.", "Independent comparison assessment owns semantic disposition. No Product acceptance, general reliability claim or automatic plugin-trigger claim is made.", "Usage fields retain native host meanings and are not normalized across providers; cached Codex input is included within input_tokens.", "No further native observation is selected by this Worker return."]}
write(outputs[1], summary)

lines = ["# Native execution supplement — attempt-05", "", "This appended return preserves the frozen generation through attempt-04. Both newly selected map observations are closed. The first task-emitting source observations remain the fixed controls: Claude attempt-02 and Codex attempt-03. No source control was rerun.", "", "The selected Representation skill is `" + summary["subject"]["skill_sha256"] + "`; the exact cohort is `" + summary["subject"]["cohort_sha256"] + "`. Source, task, fixture, oracle, program, map and all seven Axiom Product members remain unchanged. The Representation release record and cohort disclose the changed skill.", "", "| Host | Version | Requested model / effort | Exit | Seconds | Reported output tokens | Return mechanics |", "| --- | --- | --- | ---: | ---: | ---: | --- |"]
for row in observations:
    tokens = [item["usage"].get("output_tokens") for item in row["reported_usage"] if "usage" in item]
    config = row["requested_model_configuration"]
    lines.append("| " + " | ".join([row["host"], row["host_version"], config["model"] + " / " + config["effort"], str(row["exit_code"]), str(row["duration_seconds"]), ", ".join(str(value) for value in tokens) or "unreported", row["mechanical_return_receipt"]["status"]]) + " |")
lines += ["", "Full native usage, observed model identity where reported, exact durations, receipts and hashes are retained in [execution-summary-attempt-05.json](execution-summary-attempt-05.json). Codex's cached-input count is part of its input count; Claude reports separate input and cache categories. These fields are not a normalized cross-host cost measure.", "", "The unchanged runner and both exact preflights are bound by [attempt-05/execution-authority.json](attempt-05/execution-authority.json). [attempt-05/input-equivalence.json](attempt-05/input-equivalence.json) records equal task, source, Axiom, model, host version, effect grant and command/environment capabilities after fresh-path normalization. Full worksite equality across presentations is not claimed.", "", "A pre-exposure record-helper assertion failed because that helper counted the sandbox prefix twice. The original helper and diagnostic remain in the appended generation; a separately named copy corrected only that comparison. No native context, task, preflight or provider observation was changed. This preparation correction is recorded in [attempt-05/preparation-record.json](attempt-05/preparation-record.json).", "", "The earlier no-provider preflight failures, two zero-output Codex startup failures, original source/map returns and attempt-04 returns remain immutable. Their complete population is retained in [execution-summary.json](execution-summary.json). The original-cohort locator supplement continues to identify frozen context copies of that earlier cohort.", "", "Both attempt-05 worksite snapshots are retained before and after execution. The existing Codex installation file retains its digest and filesystem identity. No credentials were copied, and HOME/CODEX_HOME were inherited unchanged. All " + str(len(runtime_dirs)) + " private runtime directories remain ignored and absent from the Git index; [runtime-ignore-check-attempt-05.json](runtime-ignore-check-attempt-05.json) records the read-only check.", "", "Closed factual comparison subjects are [Claude](evaluation-subject-read-only-streams-claude.json) and [Codex](evaluation-subject-read-only-streams-codex.json), each against its fixed first source control. They expose no withheld oracle or expected verdict. The independent assessor owns semantic and grant-compliance disposition; exit status and join replay do not establish those claims.", "", "[output-freeze-attempt-05.json](output-freeze-attempt-05.json) freezes the appended retained generation and binds the conserved earlier freeze. Private runtime state and Python caches are excluded. No further observations are selected. This record makes no Product-acceptance, general-reliability or automatic-plugin-trigger claim.", ""]
write(outputs[2], "\n".join(lines))

base_names = {row["path"] for row in base["members"]}
appended = []
for path in sorted(HERE.rglob("*")):
    relative = path.relative_to(HERE)
    if path == outputs[3] or "runtime" in relative.parts or "__pycache__" in relative.parts:
        continue
    if not (path.is_file() or path.is_symlink()) or str(relative) in base_names:
        continue
    appended.append(member(path))
aggregate = hashlib.sha256("".join(row["sha256"] + "  " + row["type"] + "  " + row["path"] + "\n" for row in appended).encode()).hexdigest()
freeze = {"kind": "stdo.native-worker-appended-output-freeze", "recorded_at": datetime.now(timezone.utc).isoformat(), "status": "Selected appended Worker generation frozen for commit B; independent semantic disposition separately owned", "write_territory": str(HERE), "base_generation": ref(base_path), "base_member_count": base["member_count"], "base_member_set_sha256": base["member_set_sha256"], "base_members_and_manifest_unchanged": True, "scope": "All new retained native artifacts since the through-attempt-04 freeze, including the conserved base freeze itself. Base members are bound by that immutable manifest and not repeated here. Private ignored runtime state, Python caches and this manifest itself are excluded.", "member_count": len(appended), "member_set_sha256": aggregate, "aggregate_rule": "Sorted SHA-256, two spaces, type, two spaces, relative path, newline; symlink SHA covers UTF-8 target without newline.", "members": appended}
write(outputs[3], freeze)
print(json.dumps({"status": "frozen", "base_members_unchanged": base["member_count"], "appended_member_count": len(appended), "appended_member_set_sha256": aggregate, "records": [ref(path) for path in outputs]}, indent=2))
