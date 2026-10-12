"""Append exact-input and execution-trigger records; never launch a provider."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import shutil
import sys

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
from prepare_native import sha, snapshot, write
from run_native import native_command, prefix, transport_state


def read(path):
    return json.loads(Path(path).read_text())


def ref(path):
    return {"path": str(path), "sha256": sha(path)}


def normalize(value, work, runtime, evidence):
    return json.dumps(value, sort_keys=True).replace(str(work), "<worksite>").replace(str(runtime), "<runtime>").replace(str(evidence), "<evidence>")


attempt = HERE / "attempt-05"
selection_path = attempt / "coverage-selection.json"
selection = read(selection_path)
binding_path = HERE / "candidate-binding-read-only-streams.json"
binding = read(binding_path)
cohort_path = Path(binding["cohort_manifest"])
cohort = read(cohort_path)
controls_path = HERE / "fixed-source-controls.json"
controls = {row["host"]: row for row in read(controls_path)["controls"]}
outputs = [attempt / "input-equivalence.json", HERE / "evaluation-subject-read-only-streams-inputs.json", attempt / "execution-authority.json"]
assert not any(path.exists() for path in outputs), "Refuse replacing records"
assert not (attempt / "harness").exists(), "Refuse replacing harness copy"
assert sha(binding_path) == selection["binding_sha256"]
assert sha(cohort_path) == binding["cohort_sha256"] == selection["cohort_sha256"]
assert sha(binding["guidance_review"]["path"]) == binding["guidance_review"]["sha256"]
assert sha(binding["activation"]["path"]) == binding["activation"]["sha256"]
assert sha(controls_path) == binding["comparison"]["fixed_source_controls"]["sha256"]
assert snapshot(HERE / "packet") == selection["packet"]
assert sha(HERE / "oracle.md") == selection["oracle_sha256"]
assert sha(HERE / "oracle-binding.json") == selection["oracle_binding_sha256"]
source = Path(binding["source_release_root"])
assert sha(source / "manifest.json") == binding["source_manifest_sha256"]
for member in read(source / "manifest.json")["standards"]["members"]:
    assert sha(source / "standards" / member["path"]) == member["sha256"]
for product, item in binding["products"].items():
    root = Path(item["root"])
    for member in cohort["products"][product]["subject"]["members"] + item["support_members"]:
        path = root / member["path"]
        digest = hashlib.sha256(os.readlink(path).encode()).hexdigest() if path.is_symlink() else sha(path)
        assert digest == member["sha256"], str(path)

base_freeze = HERE / "output-freeze.json"
assert sha(base_freeze) == "b28e9bd37e1705ff410872e4119702d9369a41a0d2e3eba0899a15c66e217df4"
base = read(base_freeze)
for member in base["members"]:
    path = HERE / member["path"]
    digest = hashlib.sha256(os.readlink(path).encode()).hexdigest() if path.is_symlink() else sha(path)
    assert digest == member["sha256"], "Prior generation drift: " + str(path)

rows, contexts, preflights = [], [], {}
for context in selection["contexts"]:
    host = context["host"]
    control = controls[host]
    work, evidence = Path(context["worksite"]), Path(context["directory"])
    runtime = Path(context["runtime"])
    oldwork, oldevidence = Path(control["worksite"]), Path(control["context_directory"])
    oldruntime = oldevidence.parent / "runtime"
    native, oldnative = read(work / "native-context.json"), read(oldwork / "native-context.json")
    preflight_path = evidence / "confinement-preflight.json"
    preflight, oldpreflight = read(preflight_path), read(oldevidence / "confinement-preflight.json")
    oldcommand = read(oldevidence / "command.json")
    assert preflight["status"] == "pass" and preflight["provider_calls"] == 0
    assert preflight["selection_sha256"] == sha(selection_path)
    assert preflight["runner_sha256"] == sha(HERE / "run_native.py")
    assert preflight["profile_sha256"] == sha(context["outer_profile"])
    assert snapshot(work) == read(evidence / "snapshot-before.json")
    assert snapshot(oldwork) == read(oldevidence / "snapshot-before.json")
    assert transport_state(context) == context["nonsemantic_transport"]
    assert preflight["nonsemantic_transport_unchanged"]
    assert context["models"][host] == control["model_configuration"]
    assert sha(evidence / "prompt.txt") == control["prompt_sha256"]
    assert sha(work / "stdo_task.json") == control["definition_sha256"]
    assert sha(work / "qualification-basis.md") == control["qualification_basis_sha256"]
    for relative, member in selection["packet"].items():
        assert sha(work / relative) == sha(oldwork / relative) == member["sha256"]
    for key in ("source_revision", "source_manifest_sha256", "source_basis"):
        assert native[key] == oldnative[key]
    assert snapshot(Path(native["source_store"])) == snapshot(Path(oldnative["source_store"]))
    assert snapshot(Path(native["axiom_root"])) == snapshot(Path(oldnative["axiom_root"]))
    assert cohort["products"]["axiom_indexer"]["subject"] == control["axiom_subject"]
    version = lambda p: next(c["stdout"] for c in p["checks"] if c["operation"] == "host_version")
    assert version(preflight) == version(oldpreflight)
    assert normalize(preflight["environment_overrides"], work, runtime, evidence) == normalize(oldcommand["environment_overrides"], oldwork, oldruntime, oldevidence)
    assert normalize(native_command(context), work, runtime, evidence) == normalize(oldcommand["argv"], oldwork, oldruntime, oldevidence)
    assert context["allowed_writes"] == []
    assert sha(oldevidence / "execution-result.json") == control["execution_receipt_sha256"]
    assert sha(oldevidence / "final.txt") == control["final_sha256"]
    assert sha(work / "native/cohort.json") == binding["cohort_sha256"]
    preflights[context["name"]] = sha(preflight_path)
    rows.append({"host": host, "new_map_context": context["name"], "fixed_source_context": control["selected_context"], "fixed_source_attempt": control["attempt"], "task_prompt_definition_frame_contract_source_axiom_model_and_host_version_equal": True, "environment_and_command_capabilities_equal_after_fresh_path_normalization": True, "effect_grant": "same read-only task", "new_preflight_sha256": sha(preflight_path), "source_control_receipt_sha256": control["execution_receipt_sha256"]})
    contexts.append({"name": context["name"], "host": host, "presentation": context["arm"], "model_configuration": context["models"][host], "worksite": str(work), "frozen_inputs": ref(evidence / "snapshot-before.json"), "preflight": ref(preflight_path)})

equivalence = {"kind": "stdo.native-changed-guidance-input-equivalence", "contexts": rows, "changed_members_from_previous_map_generation": binding["comparison"]["changed_representation_members"], "intended_additional_record_changes": "Representation release record and cohort bind the changed skill; fresh worksite/runtime paths differ. No complete-worksite equality is claimed.", "through_attempt_04_members_unchanged": base["member_count"], "previous_generation_freeze": ref(base_freeze)}
write(outputs[0], equivalence)
inputs = {"kind": "stdo.native-comparison-input-subject", "scope": "Factual frozen inputs for two new map observations compared with fixed first source controls; no semantic grade or expected-answer material. Outputs are supplied only after each host process closes.", "contexts": contexts, "fixed_source_controls": ref(controls_path), "input_equivalence": ref(outputs[0]), "original_cohort_locators": ref(HERE / "original-cohort-locators.json"), "changed_members_from_previous_map_generation": binding["comparison"]["changed_representation_members"], "prior_pair_manifests": binding["comparison"]["prior_pair_manifests"], "previous_map_cohort": binding["comparison"]["previous_map_cohort"], "cohort": ref(Path(selection["contexts"][0]["worksite"]) / "native/cohort.json"), "source_basis": {"root": binding["source_release_root"], "manifest_sha256": binding["source_manifest_sha256"], "revision": binding["source_revision"]}}
write(outputs[1], inputs)
authority = {"status": "execution_authorized", "recorded_at": datetime.now(timezone.utc).isoformat(), "parent_instruction": "Exact all-command read-only skill independently reviewed and live; two fresh map contexts may run after current-binding, unchanged-input equivalence and custody checks pass, using fixed first source controls. Preserve the frozen through-attempt-04 generation and all failures. Maximum two concurrent, 1200 seconds each, no favorable-case retry.", "selection_sha256": sha(selection_path), "preflight_sha256": preflights, "runner_sha256": sha(HERE / "run_native.py"), "input_equivalence_sha256": sha(outputs[0]), "input_manifest_sha256": sha(outputs[1]), "zero_binding_input_drift": True, "concurrency_maximum": 2, "timeout_seconds": 1200, "reused_source_controls_sha256": sha(controls_path), "base_generation_freeze_sha256": sha(base_freeze)}
write(outputs[2], authority)
for name in ("prepare_native.py", "run_native.py", "check_returns.py", "check_fixture.py"):
    destination = attempt / "harness" / name
    destination.parent.mkdir(exist_ok=True)
    shutil.copy2(HERE / name, destination)
print(json.dumps({"status": "ready", "records": [ref(path) for path in outputs], "passing_contexts": len(contexts), "provider_calls": 0}, indent=2))
