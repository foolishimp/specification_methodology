"""Preserve first rejected setup; use native grant preconditions for targets."""
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("claude_continuation_preparation", HERE / "prepare.py")
p = importlib.util.module_from_spec(spec); sys.modules[spec.name] = p; spec.loader.exec_module(p)

stable = json.loads((HERE / "responses/claude-c1-stable-observe.stdout.json").read_text())["result"]["artifact"]
targets = json.loads((HERE / "responses/claude-c1-target-observe.stdout.json").read_text())["result"]["artifact"]
policy = json.loads((HERE / "executive-policy.json").read_text())
grant_id = "urn:stdo-skills:T001:claude:construction:3"
policy["id"] += ":target-preconditions"
policy["grants"][grant_id]["preconditions"].append(targets)
policy_path = HERE / "executive-policy-2.json"
p.save(policy_path, policy)
request = json.loads((HERE / "requests/claude-c1-assemble.json").read_text())
assembled = p.call(policy_path, "claude-c1-assemble-2", "context.assemble", request["arguments"])
context = assembled["result"]["artifact"]
preflight = p.call(policy_path, "claude-c1-preflight-2", "contract.preflight", {"context": context, "grant_id": grant_id, "executor_id": "claude-continuation-1", "result_key": "T001/claude/construction-3", "observations": [stable]})
value = preflight["result"]["value"]
if value["decision"] != "admitted" or value["contract_state"] != "admitted" or value["gaps"]:
    raise RuntimeError("Continuation still not admitted; retained second response")
ready = {"plan": p.pin(HERE / "actor-plan.json"), "policy": p.pin(policy_path), "context": context, "basis_observations_for_return_check": [stable], "grant_precondition_target_observation": targets, "preflight": preflight["result"]["artifact"], "preflight_evidence": preflight["evidence"], "contract_sha256": value["contract_sha256"], "decision": value["decision"], "contract_state": value["contract_state"], "gaps": value["gaps"], "fit": assembled["result"]["value"]["fit"], "session": p.SESSION, "actor_id": policy["principals"]["claude"]["actor_id"], "new_activation": grant_id, "no_dispatch": True, "method_source_model_unchanged": True, "first_rejected_setup": "claude-c1-preflight; Context observation list must equal preflight argument list; target observation now enters through existing grant.preconditions"}
p.save(HERE / "READINESS.json", ready)
p.save(HERE / "root-dispatch.request.json", {"schema": "a_c.fd-support.request/1", "id": "root-T001-claude-continuation1-dispatch", "operation": "dispatch.start", "arguments": {"preflight": ready["preflight"]}})
print(json.dumps({"readiness": str(HERE / "READINESS.json"), "sha256": p.sha(HERE / "READINESS.json"), "no_dispatch": True}))
