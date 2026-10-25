"""Complete native preflight from already-created immutable prepared files.

Preparation stopped at a Python dataclass import issue before public calls.
This continuation does not regenerate Product, policies, plans or contracts.
"""
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("successor_prepare", HERE / "prepare.py")
p = importlib.util.module_from_spec(spec); sys.modules[spec.name] = p; spec.loader.exec_module(p)
spec = importlib.util.spec_from_file_location("selected_actor_cli", p.ADAPTER)
adapter = importlib.util.module_from_spec(spec); sys.modules[spec.name] = adapter; spec.loader.exec_module(adapter)

policy_path = HERE / "executive-policy.json"
policy = json.loads(policy_path.read_text())
definition = policy["product"]["definition"]
profile = policy["method_profile"]
checks = {}
for tenant in ["codex", "claude"]:
    path = HERE / tenant / "actor-plan.json"
    adapter.load_plan(path, p.sha(path))
    checks[tenant] = {"plan_sha256": p.sha(path), "actual_adapter_validation": "passed", "backend_invoked": False}
p.save(HERE / "ADAPTER-PLAN-CHECK.json", checks)

receipts = {}
for tenant in ["codex", "claude"]:
    task = p.ref("successor", tenant + "/TASK.md")
    contract = p.ref("successor", tenant + "/RETURN-CONTRACT.json")
    predicates = p.ref("successor", tenant + "/PREDICATES.md")
    route = p.ref("successor", tenant + "/SOURCE-ROUTES.json")
    history = p.ref("successor", tenant + "/HISTORY.json")
    host = p.ref("successor", tenant + "/HOST.md")
    routes = json.loads((HERE / tenant / "SOURCE-ROUTES.json").read_text())
    inputs = routes["required"][:6]
    proof_source, result_source = routes["deciding_method"]
    grant_id = "urn:stdo-skills:T001:" + tenant + ":construction:2"
    grant = policy["grants"][grant_id]
    territory = grant["territory"]
    p.call(policy_path, "executive", tenant + "-s1-describe", "tools.describe", {"operation": "context.assemble"})
    observation_result = p.call(policy_path, "executive", tenant + "-s1-observe", "workspace.observe", {"scope": [{"root": "product", "path": "stdo_skills.json", "kind": "file"}] + [{"root": x["root"], "path": x["path"], "kind": "file"} for x in inputs] + territory})
    observation = observation_result["result"]["artifact"]
    subject = {"id": "urn:stdo-skills:T001:" + tenant + ":candidate", "sha256": p.COMMON}
    selected_inputs = routes["required"] + routes["deciding_method"] + [routes["tool_profile"], route]
    if routes["proposal"] is not None:
        selected_inputs.append(routes["proposal"])
    packet = {
        "activation": {"id": grant_id, "revision": "2", "configuration": task},
        "frame": {"id": "skills.worker/1", "revision": "2", "declaration": inputs[4], "evaluation": predicates, "result_algebra": result_source},
        "subject_basis": {"subject": subject, "method_profile": {k: profile[k] for k in ["id", "sha256"]}, "product": {"id": policy["product"]["definition_id"], "definition": definition}, "observations": [observation], "dependencies": inputs, "time_basis": "exact current observation after prior closure, revised contract and directory provisioning"},
        "attention": {"material_relations": [route, history], "invariants": [inputs[2], proof_source], "semantic_sources": [inputs[0], inputs[5]], "exclusions": ["peer design/code/output", "Git/remote/global mutations"], "prohibited_assumptions": ["source existence proves fitness", "candidate ready proves acceptance", "prior process end proves all effects absent"]},
        "actor_authority": {"actor_id": policy["principals"][tenant]["actor_id"], "role": "Worker", "capability": host, "semantic": inputs[0], "evaluation": predicates, "operation": task, "decision": None, "acceptance": None, "publication": None, "territory": territory, "tools": grant["tools"]},
        "evidence_relations": {"admissible_evidence": [predicates, task], "acquisition": selected_inputs, "dependencies": [history], "conjunction": None, "translation": None, "consumer": "root-executive", "return_contract": contract},
        "stop_change": {"invalidators": ["material source/tool/authority drift", "unreconciled effect"], "stop_conditions": ["600 seconds", "genuine unsupported required operation"], "residuals": ["mandatory actual-host Q01-Q12 and independent review remain open"], "re_entry": ["return exact partial candidate and missing premise"], "reconfiguration": ["successor of known failed attempt " + p.ATTEMPTS[tenant] + "; see retained HISTORY"]},
        "profile_additions": {"worker": {"operation_grant_id": grant_id, "mutation_subject": subject, "territory": territory}}
    }
    late = [json.loads(k) for k in dict.fromkeys(json.dumps(x, sort_keys=True) for x in selected_inputs) if json.loads(k) != predicates]
    assembled = p.call(policy_path, "executive", tenant + "-s1-assemble", "context.assemble", {"packet": packet, "models": [], "sources": [task, contract, predicates], "late_acquisition": late, "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})
    context = assembled["result"]["artifact"]
    preflight = p.call(policy_path, "executive", tenant + "-s1-preflight", "contract.preflight", {"context": context, "grant_id": grant_id, "executor_id": tenant + "-cli-successor-1", "result_key": "T001/" + tenant + "/construction-2", "observations": [observation]})
    value = preflight["result"]["value"]
    if value["decision"] != "admitted" or value["contract_state"] != "admitted" or value["gaps"]:
        raise RuntimeError("Preflight unresolved: " + tenant)
    receipts[tenant] = {"context": context, "observation": observation, "preflight": preflight["result"]["artifact"], "preflight_evidence": preflight["evidence"], "decision": value["decision"], "contract_sha256": value.get("exact_contract", {}).get("sha256"), "fit": assembled["result"]["value"]["fit"], "plan": p.pin(HERE / tenant / "actor-plan.json"), "policy": p.pin(policy_path)}
    p.save(HERE / ("root-dispatch-" + tenant + ".request.json"), {"schema": "a_c.fd-support.request/1", "id": "root-T001-" + tenant + "-successor1-dispatch", "operation": "dispatch.start", "arguments": {"preflight": receipts[tenant]["preflight"]}})
p.save(HERE / "READINESS.json", {"receipts": receipts, "external_model_dispatches": 0, "boundary": "Preparation and native admission only; Root reviews before launch", "historical_attempts_preserved": p.ATTEMPTS, "tool_basis": p.pin(HERE / "TOOL-BASIS.json")})
print(json.dumps({"readiness": str(HERE / "READINESS.json"), "sha256": p.sha(HERE / "READINESS.json"), "external_model_dispatches": 0}))
