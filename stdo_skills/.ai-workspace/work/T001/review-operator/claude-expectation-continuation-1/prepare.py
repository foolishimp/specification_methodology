"""Resume the actual source-only Reviewer once; never dispatch a model."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent
OLD = REVIEW / "claude-setup2/expectation"
spec = importlib.util.spec_from_file_location("existing_review_preparation", REVIEW / "prepare_review.py")
base = importlib.util.module_from_spec(spec); sys.modules[spec.name] = base; spec.loader.exec_module(base)
save, sha, pin = base.save, base.sha, base.pin
SESSION = "628dfe7c-13d9-4c76-8146-64fd9787ee38"
PRIOR_ATTEMPT = "3f375c058e51d8ee3d775bd9be2959e00256bb9671892ea87f004301b6e06553"
ACQUISITION_OPERATION = "cdd9ae5b2b78e83285dd9ab22a0d09727bd24351a73c2bf1f0ca76f4f5e99157"


def ref(name):
    return base.source("review", "claude-expectation-continuation-1/" + name)


def replace_refs(value, replacements):
    if isinstance(value, dict):
        for before, after in replacements:
            if value == before:
                return copy.deepcopy(after)
        return {k: replace_refs(v, replacements) for k, v in value.items()}
    if isinstance(value, list):
        return [replace_refs(v, replacements) for v in value]
    return value


def prepare():
    prior_policy = json.loads((OLD / "executive-policy.json").read_text())
    prior_worker = json.loads((OLD / "reviewer-policy.json").read_text())
    prior_plan = json.loads((OLD / "actor-plan.json").read_text())
    selection = json.loads((REVIEW / "claude-setup2/SELECTION.json").read_text())
    process = json.loads((OLD / "actor-cli-output/process.json").read_text())
    closed = subprocess.run(["ps", "-p", str(process["pid"]), "-o", "pid=,comm="], capture_output=True, text=True)
    if closed.returncode == 0:
        raise RuntimeError("Prior direct Reviewer process remains present")
    sessions = set(); models = set()
    for line in (OLD / "actor-cli-output/vendor.stdout").read_text().splitlines():
        try:
            item = json.loads(line)
        except ValueError:
            continue
        if item.get("type") == "system" and item.get("subtype") == "init":
            sessions.add(item["session_id"]); models.add(item["model"])
    if sessions != {SESSION}:
        raise RuntimeError("Actual prior Reviewer session differs")
    for source in selection["governing_sources"] + selection["candidate_sources"] + selection["proof_sources"]:
        base.check_source(prior_policy, source)
    for dependency in next(iter(prior_policy["executors"].values()))["dependencies"]:
        base.check_source(prior_policy, dependency)
    operation = base.old.load_artifact(ACQUISITION_OPERATION)
    actor_id = prior_worker["principals"]["reviewer"]["actor_id"]
    if operation["provenance"]["actor"]["actor_id"] != actor_id:
        raise RuntimeError("Retained acquisition is not this actual Reviewer")
    acquired = []
    for artifact_ref in operation["payload"]["acquisitions"]:
        envelope = base.old.load_artifact(artifact_ref["sha256"])
        payload = envelope["payload"]
        if payload["source"] in selection["governing_sources"]:
            if payload["recipient"] != actor_id:
                raise RuntimeError("Source acquisition recipient differs")
            acquired.append({"artifact": artifact_ref, "source": payload["source"]})
    if len(acquired) != len(selection["governing_sources"]):
        raise RuntimeError("Incomplete actual governing acquisition population")
    source_inputs = [x["artifact"] for x in acquired]
    save(HERE / "RETAINED-ACQUISITIONS.json", {"operation": base.old.artifact(ACQUISITION_OPERATION), "actual_recipient": actor_id, "acquired": acquired, "standing": "Actual prior source delivery, unchanged parent hashes; not a new acquisition or candidate assessment"})
    save(HERE / "RECONCILIATION.json", {"prior_attempt": base.old.artifact(PRIOR_ATTEMPT), "process": process, "session": SESSION, "reported_model": sorted(models), "current_direct_pid": {"argv": ["ps", "-p", str(process["pid"]), "-o", "pid=,comm="], "returncode": closed.returncode, "stdout": closed.stdout}, "known_result": "Governing acquisition and decoded source retained; no expectation artifact or closed return completed", "limits": ["No universal descendant/external effect absence claim", "No candidate assessment or qualification inferred", "No model override selected; actual resumed backend remains an observation"]})
    save(HERE / "DECISIONS.md", """# One source-only expectation continuation

Root selected one 600-second continuation of actual review session 628dfe7c-13d9-4c76-8146-64fd9787ee38 after its300-second source-only phase timed out. Same declared Reviewer, same36-file claim, exact released methodology, tool implementation and inherited model/effort settings. No candidate bytes may be acquired before recording actual source-derived expectations. Prior source acquisitions remain attributed to their original operation and actor; no earlier review judgment is substituted.

The actual operation cdd9ae5b2b78e83285dd9ab22a0d09727bd24351a73c2bf1f0ca76f4f5e99157 already delivered the9 governing slices. This continuation should use that retained source knowledge and those exact AcquisitionRefs, derive compact falsifiable expectations and record them through review.prepare. No schema/inventory research, scratch files, or on-disk decoding loops. If selected text is genuinely missing, source.read with encoding=utf8 or decode base64 in memory only.

The same Product owner and protected evidence surface apply. This is a new activation, not replay of the timed-out dispatch. Direct process closure is observed; unknown external effects remain explicit. --resume selects the exact session and --system-prompt-snapshot off makes the new bounded instruction effective. No global, source, candidate or model override is made. Root will select later900-second candidate assessment only after actual expectation evidence exists.
""")
    claim = base.source("review", "claude-setup2/CLAIM.json")
    recording_shape = {"schema": "a_c.fd-support.request/1", "id": "claude-expectation-continuation-record-1", "operation": "review.prepare", "arguments": {"phase": "expectation", "claim": claim, "sources": [], "candidate": selection["candidate"], "proof": [], "comparison": None, "expectations": None, "expectation_body": {"text": "REPLACE WITH YOUR OWN COMPACT SOURCE-DERIVED EXPECTATIONS", "source_inputs": source_inputs}}}
    task = """# Record the actual expectations now

Resume your SAME source-only review session. The prior activation timed out after it acquired and decoded governing sources. No expected-artifact or final review exists. This new activation has600seconds and one narrow outcome: derive compact falsifiable expectations from your retained governing-source knowledge and RECORD them with review.prepare. Do not inspect candidate files or prior verdicts. Do not research schemas, inventories or routing again. No scratchfile writes or disk decoding. The actual Context's sources carry base64; use already retained text, source.read(encoding=utf8) only if needed, or in-memory base64 decoding without files.

The exact prior acquisition OperationEvidence is cdd9ae5b2b78e83285dd9ab22a0d09727bd24351a73c2bf1f0ca76f4f5e99157. The following template already supplies its9 ACTUAL governing AcquisitionRefs delivered to your unchanged Reviewer identity. These are source_inputs, not OperationEvidence references. Replace only the expectation text with your own assessment expectations and select a fresh request id if necessary. sources=[] avoids redundantly acquiring the same governing bytes; the native checker verifies the supplied original source_inputs. The claim and candidate here are coordinates, not candidate-content acquisition.

""" + json.dumps(recording_shape, indent=2) + """

Use the current policy/CLI from startup, sending a complete JSON request on stdin to call --request -. A single in-memory Python subprocess may compose and send it; no file request or decoded-source file is needed. Do not send the placeholder text. Keep expectations concise, concrete and falsifiable for common WHAT, the native301/auth tool increment and Codex static package merits. Distinguish actual supported path, authority, semantic assessment and unperformed host Q01-Q12 qualification. Do not convert test totals or package presence into the expected answer.

On success, retain the returned actual expectation ArtifactRef and source_first/exposure result. If the tool reports a provenance/exposure gap, return that exact gap, not a fabricated independent expectation. Output one original closed-return JSON. Copy THIS Context's frame, activation identity, subject, original basis, actor and consumer. work_result=null; perform expectation-recording only using RETURN-CONTRACT's exact PREDICATES SourceRef. Evaluation fields are id,predicate,domain_outcome,core_value,evidence,residuals,invalidators. Put the actual expectation ArtifactRef in evidence and domain_outcome. Top-level fields are schema,id,frame,activation,subject,basis,actor,consumer,evaluations,not_performed,work_result,residuals,invalidators. Schema is a_c.fd-support.closed-return/1; no fences. This is preparation only, not candidate review or acceptance. Root will bind the resulting artifact into the later candidate contract. Do not start that stage.
"""
    save(HERE / "TASK.md", task)
    task_ref = ref("TASK.md"); decision = ref("DECISIONS.md")
    old_task = prior_worker["principals"]["reviewer"]["role_binding"]
    additional = [{"path": "claude-expectation-continuation-1/" + name, "kind": "file"} for name in ["TASK.md", "DECISIONS.md", "RETAINED-ACQUISITIONS.json", "RECONCILIATION.json", "RETURN-CONTRACT.json", "STARTUP.txt", "reviewer-policy.json", "actor-plan.json"]]
    worker = replace_refs(copy.deepcopy(prior_worker), [(old_task, task_ref)])
    worker["id"] = "urn:stdo-skills:T001:claude:review:expectation-continuation1"
    worker["sources"]["review"]["read_scope"] += additional
    worker["authority_sources"].append(decision)
    save(HERE / "reviewer-policy.json", worker)
    cli_argv = [str(base.old.PYTHON), "-B", str(base.old.CLI), "--policy", str(HERE / "reviewer-policy.json"), "--policy-sha256", sha(HERE / "reviewer-policy.json"), "--principal", "reviewer", "call", "--request", "-"]
    startup = "Continue your actual source-only review session with this NEW exact activation. You already acquired/decoded the9 governors; now derive and RECORD compact expectations. No schema or inventory research, candidate reads, scratch files or on-disk decode. TASK contains exact original AcquisitionRefs and a complete review.prepare request template; replace only its expectation text with your own. Read TASK once as UTF8 if needed: " + json.dumps(task_ref) + ". Public CLI argv, JSON on stdin: " + json.dumps(cli_argv) + ". source.read arguments={source:TASKref,encoding:'utf8'}. Emit the original closed-return JSON with the actual expectation ref within600seconds; do not begin candidate review."
    save(HERE / "STARTUP.txt", startup + "\n")
    plan = copy.deepcopy(prior_plan)
    plan["id"] = worker["id"] + ":plan"
    plan["argv"] = plan["argv"][:-1] + [startup, "--resume", SESSION, "--system-prompt-snapshot", "off"]
    plan["limits"]["timeout_ms"] = 600000
    plan["evidence_directory"] = str(HERE / "actor-cli-output")
    plan["settings"]["session_continuity"] = {"session_id": SESSION, "prior_attempt": PRIOR_ATTEMPT, "new_activation": worker["id"], "source_knowledge": "Retained actual acquisition; expectation assertion still required"}
    plan["dependencies"] = [x for x in plan["dependencies"] if Path(x["path"]).is_relative_to(base.old.TOOL)] + [pin(HERE / "reviewer-policy.json"), pin(HERE / "STARTUP.txt")]
    save(HERE / "actor-plan.json", plan)
    contract = replace_refs(json.loads((OLD / "RETURN-CONTRACT.json").read_text()), [(old_task, task_ref)])
    contract["id"] = worker["id"] + ":return"
    save(HERE / "RETURN-CONTRACT.json", contract)
    executive = replace_refs(copy.deepcopy(prior_policy), [(old_task, task_ref)])
    executive["id"] = worker["id"] + ":executive"
    executive["sources"]["review"]["read_scope"] += additional
    executive["principals"]["executive"]["role_binding"] = decision
    executive["authority_sources"].append(decision)
    grant = copy.deepcopy(next(iter(executive["grants"].values())))
    grant_id = worker["id"] + ":grant"
    grant["id"] = grant_id; grant["authority_sources"].append(decision); grant["executors"] = ["claude-review-expectation-continuation1"]
    executive["grants"] = {grant_id: grant}
    executor = copy.deepcopy(next(iter(executive["executors"].values())))
    executor["id"] = "claude-review-expectation-continuation1"
    executor["argv"] = [str(base.old.PYTHON), "-B", str(base.old.ADAPTER), "--plan", str(HERE / "actor-plan.json"), "--plan-sha256", sha(HERE / "actor-plan.json")]
    executor["settings"]["timeout_ms"] = 610000
    executor["dependencies"] = [x for x in executor["dependencies"] if x["root"] != "review"] + [ref(n) for n in ["reviewer-policy.json", "STARTUP.txt", "actor-plan.json"]]
    executive["executors"] = {executor["id"]: executor}
    policy_path = HERE / "executive-policy.json"; save(policy_path, executive)
    adapter_spec = importlib.util.spec_from_file_location("source_only_continuation_adapter", base.old.ADAPTER)
    adapter = importlib.util.module_from_spec(adapter_spec); sys.modules[adapter_spec.name] = adapter; adapter_spec.loader.exec_module(adapter)
    adapter.load_plan(HERE / "actor-plan.json", sha(HERE / "actor-plan.json"))
    old_observe = json.loads((OLD / "requests/claude-review-expectation-observe.json").read_text())["arguments"]
    observed = base.public_call(HERE, policy_path, "claude-review-expectc1-observe", "workspace.observe", old_observe)
    observation = observed["result"]["artifact"]
    assembly = json.loads((OLD / "requests/claude-review-expectation-assemble.json").read_text())["arguments"]
    old_contract = base.source("review", "claude-setup2/expectation/RETURN-CONTRACT.json")
    assembly = replace_refs(assembly, [(old_task, task_ref), (old_contract, ref("RETURN-CONTRACT.json"))])
    assembly["packet"]["activation"] = {"id": worker["id"], "revision": "2", "configuration": task_ref}
    assembly["packet"]["frame"]["revision"] = "2"
    assembly["packet"]["subject_basis"]["observations"] = [observation]
    assembly["packet"]["stop_change"]["stop_conditions"] = ["600 seconds", "source-first/provenance premise unavailable"]
    assembly["packet"]["stop_change"]["reconfiguration"] = ["Explicit same-session source-only continuation of timed-out attempt " + PRIOR_ATTEMPT]
    assembled = base.public_call(HERE, policy_path, "claude-review-expectc1-assemble", "context.assemble", assembly)
    context = assembled["result"]["artifact"]
    preflight = base.public_call(HERE, policy_path, "claude-review-expectc1-preflight", "contract.preflight", {"context": context, "grant_id": grant_id, "executor_id": executor["id"], "result_key": "T001/review/claude/expectation-continuation1", "observations": [observation]})
    value = preflight["result"]["value"]
    if value["decision"] != "admitted" or value["contract_state"] != "admitted" or value["gaps"]:
        raise RuntimeError("Source-only continuation not admitted; retained response")
    ready = {"plan": pin(HERE / "actor-plan.json"), "policy": pin(policy_path), "context": context, "observation": observation, "preflight": preflight["result"]["artifact"], "preflight_evidence": preflight["evidence"], "contract_sha256": value["contract_sha256"], "decision": value["decision"], "gaps": value["gaps"], "fit": assembled["result"]["value"]["fit"], "adapter_validation": "passed", "session": SESSION, "actor_id": actor_id, "actual_source_inputs": source_inputs, "no_dispatch": True, "standing": "One600second source-only continuation; no candidate assessment or expected artifact invented"}
    save(HERE / "READINESS.json", ready)
    save(HERE / "root-dispatch.request.json", {"schema": "a_c.fd-support.request/1", "id": "root-T001-claude-review-expectc1-dispatch", "operation": "dispatch.start", "arguments": {"preflight": ready["preflight"]}})
    print(json.dumps({"readiness": str(HERE / "READINESS.json"), "sha256": sha(HERE / "READINESS.json"), "no_dispatch": True}))


if __name__ == "__main__":
    prepare()
