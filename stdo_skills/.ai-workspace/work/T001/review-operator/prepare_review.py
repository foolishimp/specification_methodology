"""Bind an exact review selection using the existing native setup. No dispatch.

All writes are create-only below review-operator, except genuine tool evidence
appends to the existing Product-selected protected surface when --preflight.
"""
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
PRODUCT = HERE.parents[3]
REPO = PRODUCT.parent
PREVIOUS = HERE.parent / "operator/successor-1"
spec = importlib.util.spec_from_file_location("existing_operator_preparation", PREVIOUS / "prepare.py")
old = importlib.util.module_from_spec(spec); sys.modules[spec.name] = old; spec.loader.exec_module(old)
save, sha, pin, artifact = old.save, old.sha, old.pin, old.artifact
BASE = json.loads((PREVIOUS / "executive-policy.json").read_text())


def source(root, path, selector=None):
    roots = {k: Path(v["path"]) for k, v in BASE["sources"].items()}
    roots["review"] = HERE
    return {"engine": "workspace-regular-file", "root": root, "path": path, "object": None, "sha256": sha(roots[root] / path), "selector": selector}


def add_scope(policy, reference):
    if reference["engine"] != "workspace-regular-file":
        raise RuntimeError("This bounded preparation selects workspace regular-file sources only")
    root = policy["sources"][reference["root"]]
    row = {"path": reference["path"], "kind": "file"}
    if row not in root["read_scope"]:
        root["read_scope"].append(row)


def check_source(policy, reference):
    root = Path(policy["sources"][reference["root"]]["path"])
    path = root / reference["path"]
    if sha(path) != reference["sha256"]:
        raise RuntimeError("Selected source changed: " + str(path))


def public_call(folder, policy, identity, operation, arguments):
    request = {"schema": "a_c.fd-support.request/1", "id": identity, "operation": operation, "arguments": arguments}
    path = folder / "requests" / (identity + ".json"); save(path, request)
    argv = [str(old.PYTHON), "-B", str(old.CLI), "--policy", str(policy), "--policy-sha256", sha(policy), "--principal", "executive", "call", "--request", str(path)]
    result = subprocess.run(argv, cwd=PRODUCT, capture_output=True, timeout=60)
    save(folder / "responses" / (identity + ".invocation.json"), {"argv": argv, "returncode": result.returncode})
    save(folder / "responses" / (identity + ".stdout.json"), result.stdout.decode())
    save(folder / "responses" / (identity + ".stderr.txt"), result.stderr.decode())
    body = json.loads(result.stdout)
    if result.returncode or body.get("status") != "ok":
        raise RuntimeError("Public operation refused; retained: " + identity)
    return body


def prepare(selection_path, selection_sha256, phase, expectation, run_preflight, lane=None):
    if sha(selection_path) != selection_sha256:
        raise RuntimeError("Frozen review selection hash differs")
    selection = json.loads(selection_path.read_text())
    required = {"backend", "subject", "candidate", "candidate_sources", "governing_sources", "proof_sources", "component_claims", "authors"}
    if set(selection) != required or selection["backend"] not in ("codex", "claude"):
        raise RuntimeError("Selection must bind the exact documented fields")
    backend = selection["backend"]
    population = selection["candidate_sources"]
    if not population or selection["candidate"] not in population:
        raise RuntimeError("Exact primary candidate must belong to explicit population")
    if phase == "candidate" and expectation is None:
        raise RuntimeError("Candidate review needs the actual prior Reviewer expectation")
    if phase == "expectation" and expectation is not None:
        raise RuntimeError("No substituted expectation in actual expectation phase")
    for method_file in ["standards/EXECUTIVE_BASELINE.md", "standards/ACTIVATION.md", "standards/EVALUATION.md"]:
        if not any(x["root"] == "method" and x["path"] == method_file for x in selection["governing_sources"]):
            raise RuntimeError("Selection lacks deciding method owner: " + method_file)
    sys.path.insert(0, str(old.TOOL / "build_tenants/graphify/code"))
    import ac_support_core as core
    for governing in selection["governing_sources"]:
        if any(core._source_overlap(governing, candidate) for candidate in population):
            raise RuntimeError("Governing source intersects candidate population; resolve claim boundary: " + governing["path"])
    lane = backend if lane is None else lane
    if not lane.replace("-", "").isalnum():
        raise RuntimeError("Invalid setup lane")
    root = HERE / lane
    folder = root / phase
    if folder.exists():
        raise RuntimeError("Prepared phase already exists; preserve and select a successor")
    folder.mkdir(parents=True)
    save(root / "SELECTION.json", selection)
    claim_body = {"id": "urn:stdo-skills:T001:" + backend + ":cross-family-review:1", "candidate_sources": population}
    save(root / "CLAIM.json", claim_body)
    claim = source("review", lane + "/CLAIM.json")
    actor_id = "urn:stdo-skills:T001:" + backend + ":reviewer:1"
    expected_ref = None
    if expectation is not None:
        expected_ref = artifact(expectation)
        ep = old.load_artifact(expectation)["payload"]
        if ep["producer"]["actor_id"] != actor_id or ep["claim"] != claim or ep["exposure_check"].get("source_first_observed") is not True:
            raise RuntimeError("Actual expectation is not source-first for this actor and exact claim")
    policy = copy.deepcopy(BASE)
    policy["id"] = "urn:stdo-skills:T001:" + backend + ":review:" + phase
    policy["sources"]["review"] = {"path": str(HERE), "kind": "workspace", "writable": False, "read_scope": []}
    for value in policy["sources"].values():
        value["writable"] = False
        value["read_scope"] = []
    policy.update({"grants": {}, "executors": {}, "principals": {}, "predicates": {}, "operators": {}})
    decision = source("review", "DECISIONS.md")
    independence = {"id": claim_body["id"] + ":independence", "authority_source": decision, "claim_scope": claim_body["id"], "require_non_author": True, "allowed_family_pairs": [{"author": "anthropic-claude", "reviewer": "openai-codex"}] if backend == "codex" else [{"author": "openai-codex", "reviewer": "anthropic-claude"}], "source_first": True, "mechanical_sharing": "Exact source custody and factual trial evidence may be shared; judgments may not substitute", "predicates": []}
    save(root / "INDEPENDENCE.json", independence)
    policy["independence_policy"] = source("review", lane + "/INDEPENDENCE.json")
    predicate = source("review", "PREDICATES.md")
    duration = 300 if phase == "expectation" else 900
    if phase == "expectation":
        action = "Acquire the governing sources through review.prepare phase=expectation, expectation_body=null, proof=[] and the exact claim/candidate coordinates. Do not acquire any candidate population bytes. Read the operation evidence to obtain its actual acquisitions ArtifactRefs. Derive your own falsifiable expectations, then call review.prepare phase=expectation with expectation_body={text: your actual wording, source_inputs: those prior acquisition refs}; expectations=null. Return the actual expectation ArtifactRef, source-first/exposure facts and limitations. No candidate assessment is performed. This partial return cannot be consumed as final review because its frozen proof.expectations is null."
    else:
        action = "Acquire your actual retained expectation through evidence.read and identify continuity from the prior source-only activation. Reacquire deciding sources as needed. Call review.prepare phase=candidate with this exact claim/candidate, selected proof sources, expectations=the bound prior ArtifactRef and expectation_body=null. Evaluate the real candidate and factual evidence against your source-derived expectations. Trace ordinary paths and material falsifiers, not counts. Return separate conclusions for every selected component. Record any missing scope, independence issue, tool refusal or changed expectation."
    task = f"""# Actual {backend} Reviewer: {phase}

Root selects the frozen claim in SELECTION.json. Read-only assessment; no source/candidate edits, repair, package installation, Git, model/subagent call or acceptance. Public a_c CLI writes only its own protected evidence. Bash/Read may inspect permitted sources and perform bounded in-memory/read-only probes. Do not write request files: use call --request - with an in-memory JSON envelope.

{action}

The governing source route is SELECTION.governing_sources. Candidate coordinates are metadata, not permission to read them before expectations. Shared requirements may govern tenant assessment, but common-WHAT candidate clauses cannot simultaneously be a pre-exposure governing source for their own review. If the selection has that overlap, return the exact missing basis instead of inventing source-first standing. Prior review expectations/verdicts are not your oracle. Disclose bootstrap/external exposure; no fresh context or family label certifies independence.

Use the exact current native profile and tools.describe where needed. Native results.conjoin is unsupported. Source ownership and source-first law are the selected STDO3.0.1 release; no methodology duplication or stronger universal ceremony. Report S0-S4 findings with file:line, exact violated relation, reachable evidence and consequence; separate evidence from causal/repair inference. Record unperformed host qualification and efficiency claims as open, not pass/fail totals.

The public review.prepare request envelope is {{"schema":"a_c.fd-support.request/1","id":"unique-id","operation":"review.prepare","arguments":{{"phase":"expectation" or "candidate","claim":the CLAIM SourceRef,"sources":SELECTION.governing_sources,"candidate":SELECTION.candidate,"proof":[] for expectation or the selected proof SourceRefs,"comparison":null,"expectations":null for expectation or the bound ArtifactRef for candidate,"expectation_body":null for acquisition, then {{"text":your actual source-derived expectations,"source_inputs":[actual prior acquisition ArtifactRefs]}} when recording expectations}}}}. Source reads use arguments {{"source":SourceRef,"encoding":"utf8"}}. Evidence reads use {{"artifact":ArtifactRef}}. The first review.prepare response's evidence points to an OperationEvidence; evidence.read reveals envelope.payload.acquisitions, the actual source_inputs. Do not use OperationEvidence references where Acquisition references are required. Acquisition alone is not expectation recording: make the second expectation call with your own text.

Closed return has exactly schema, id, frame, activation, subject, basis, actor, consumer, evaluations, not_performed, work_result, residuals, invalidators. schema="a_c.fd-support.closed-return/1"; frame={{id,revision}}, activation={{id,sha256}}, subject={{id,sha256}}, basis={{method_profile:{{id,sha256}},observations:[ArtifactRef]}}, actor={{id,family,authorship}}, copied from actual Context. Each evaluation has exactly id, predicate (exact PREDICATES SourceRef), domain_outcome, core_value, evidence, residuals, invalidators. evidence contains actual SourceRefs/ArtifactRefs; residuals/invalidators are arrays. work_result=null. Use the return contract's evaluation id. A source-first expectation phase returns expectation-recording only, with the expectation artifact in evidence/domain_outcome; it does not assess the candidate.

This phase has {duration} seconds within a 1200-second aggregate Reviewer budget; no retry. Inherited configured model/effort defaults remain unchanged. Final output is one original closed-return JSON object, no fences. Perform only the return contract's named evaluation and cite actual evidence; put unperformed evaluation IDs in not_performed. Candidate phase findings and per-component conclusions belong in domain_outcome. Never repair or replace the final original. Root owns continuation.
"""
    save(folder / "TASK.md", task)
    task_ref = source("review", lane + "/" + phase + "/TASK.md")
    actor = {"actor_id": actor_id, "role": "Reviewer", "family": "openai-codex" if backend == "codex" else "anthropic-claude", "authorship": "Nonauthor cross-family Reviewer; continuous declared identity across source and candidate phases", "operations": old.READ + ["review.prepare"], "role_binding": task_ref, "role_transition": None}
    key = "reviewer"
    policy["principals"] = {key: actor}
    authority = policy["product"]["authority_binding"]
    authority_sources = BASE["authority_sources"] + [decision, task_ref]
    policy["authority_sources"] = authority_sources
    needed = [policy["product"]["definition"], authority["owner_record"], authority["mechanism"]["source"], policy["method_profile"]["source"], decision, claim, predicate, policy["independence_policy"], source("review", "INDEPENDENCE.md"), source("review", "SEVERITY.md"), source("review", lane + "/SELECTION.json"), task_ref] + authority_sources + selection["governing_sources"] + population + selection["proof_sources"]
    original_plan = json.loads((PREVIOUS / backend / "actor-plan.json").read_text())
    original_executor = BASE["executors"][backend + "-cli-successor-1"]
    dependencies = [x for x in original_executor["dependencies"] if x["root"] in ("tool", "host_python", "host_codex", "host_claude")]
    for reference in needed + dependencies:
        add_scope(policy, reference); check_source(policy, reference)
    worker_policy = folder / "reviewer-policy.json"; save(worker_policy, policy)
    cli_argv = [str(old.PYTHON), "-B", str(old.CLI), "--policy", str(worker_policy), "--policy-sha256", sha(worker_policy), "--principal", key, "call", "--request", "-"]
    source_request = {"schema": "a_c.fd-support.request/1", "id": backend + "-review-" + phase + "-task", "operation": "source.read", "arguments": {"source": task_ref, "encoding": "utf8"}}
    startup = "You are the actually bound cross-family Reviewer, phase " + phase + ". Use public CLI argv " + json.dumps(cli_argv) + " with this first request JSON on stdin: " + json.dumps(source_request) + ". Then acquire SELECTION and deciding sources as TASK directs. No artifact edits or model calls. Derive your own expectations before candidate exposure. Final output is the original closed-return JSON, no fences or replacement summary."
    save(folder / "STARTUP.txt", startup + "\n")
    plan = copy.deepcopy(original_plan)
    plan["id"] = policy["id"] + ":actor-plan"
    plan["evidence_directory"] = str(folder / "actor-cli-output")
    plan["cwd"] = str(REPO)
    if "--cd" in plan["argv"]:
        plan["argv"][plan["argv"].index("--cd") + 1] = str(REPO)
    plan["dependencies"] = [x for x in original_plan["dependencies"] if Path(x["path"]).is_relative_to(old.TOOL)] + [pin(worker_policy), pin(folder / "STARTUP.txt")]
    plan["settings"]["host_scope"] = "Read-only host inspection/in-memory probes plus public CLI evidence operations; no candidate mutation or OS confinement claim"
    plan["limits"]["timeout_ms"] = duration * 1000
    plan["argv"][-1] = startup
    save(folder / "actor-plan.json", plan)
    contract = {"schema": "a_c.fd-support.return-contract/1", "id": policy["id"] + ":return", "authority_source": task_ref, "carrier": "a_c.fd-support.closed-return/1", "output_slot": "final_stdout_object", "required_evaluations": [{"id": "expectation-recording" if phase == "expectation" else "candidate-assessment", "predicate": predicate}], "role": "Reviewer", "proof": {"claim": claim, "expectations": expected_ref, "proof_sources": [] if phase == "expectation" else selection["proof_sources"], "comparison": None, "independence_policy": policy["independence_policy"], "predicate_ids": []}}
    save(folder / "RETURN-CONTRACT.json", contract)
    contract_ref = source("review", lane + "/" + phase + "/RETURN-CONTRACT.json")
    grant_id = policy["id"] + ":grant"
    executor_id = backend + "-review-" + phase
    executive = copy.deepcopy(policy)
    executive["principals"]["executive"] = copy.deepcopy(BASE["principals"]["executive"])
    executive["principals"]["executive"]["role_binding"] = decision
    executive["principals"]["executive"]["operations"] += ["review.prepare"]
    executor = copy.deepcopy(original_executor)
    executor.update({"id": executor_id, "actor_id": actor_id, "cwd": str(REPO), "argv": [str(old.PYTHON), "-B", str(old.ADAPTER), "--plan", str(folder / "actor-plan.json"), "--plan-sha256", sha(folder / "actor-plan.json")], "dependencies": dependencies + [source("review", lane + "/" + phase + "/" + name) for name in ["reviewer-policy.json", "STARTUP.txt", "actor-plan.json"]], "tools": ["a_c.public-native301", "host.read-only-in-memory"], "effect_scope": {"candidate_mutation": False, "public_evidence": "Existing Product-selected protected store", "unknowns": "Host hidden effects; no OS confinement claim"}})
    executor["settings"]["timeout_ms"] = duration * 1000 + 10000
    executive["executors"] = {executor_id: executor}
    executive["grants"] = {grant_id: {"id": grant_id, "authority_sources": authority_sources, "outcome": {"id": claim_body["id"], "source": task_ref}, "principals": ["executive"], "targets": [key], "operations": ["contract.preflight", "dispatch.start"], "tools": executor["tools"], "executors": [executor_id], "territory": [], "preconditions": selection["governing_sources"] + population, "admission": {"mechanism_id": authority["mechanism"]["id"], "mechanism_source": authority["mechanism"]["source"], "authority_source": authority["owner_record"], "required_predicates": [], "allowed_override_sources": []}, "notification_sink": "root-events"}}
    for reference in executor["dependencies"] + [contract_ref]:
        add_scope(executive, reference)
    policy_path = folder / "executive-policy.json"; save(policy_path, executive)
    routes = {"claim": claim, "candidate": selection["candidate"], "sources": selection["governing_sources"], "proof": [] if phase == "expectation" else selection["proof_sources"], "comparison": None, "expectations": expected_ref, "expectation_body": None, "phase": "expectation" if phase == "expectation" else "candidate"}
    save(folder / "review-prepare-arguments.json", routes)
    result = {"selection": pin(selection_path), "phase": phase, "plan": pin(folder / "actor-plan.json"), "policy": pin(policy_path), "return_contract": contract_ref, "expectation": expected_ref, "no_dispatch": True}
    if not run_preflight:
        save(folder / "PREPARED.json", result)
        return result
    stable_refs = [policy["product"]["definition"], policy["method_profile"]["source"]] + selection["governing_sources"] + population + selection["proof_sources"]
    scopes = list({(x["root"], x["path"]): {"root": x["root"], "path": x["path"], "kind": "file"} for x in stable_refs}.values())
    observed = public_call(folder, policy_path, backend + "-review-" + phase + "-observe", "workspace.observe", {"scope": scopes})
    observation = observed["result"]["artifact"]
    frame = source("method", "standards/EXECUTIVE_BASELINE.md", {"lines": [957, 1009]})
    algebra = source("method", "standards/ACTIVATION.md", {"lines": [1004, 1055]})
    packet = {"activation": {"id": policy["id"], "revision": "1", "configuration": task_ref}, "frame": {"id": "skills.reviewer/1", "revision": "1", "declaration": frame, "evaluation": predicate, "result_algebra": algebra}, "subject_basis": {"subject": selection["subject"], "method_profile": {k: policy["method_profile"][k] for k in ["id", "sha256"]}, "product": {"id": policy["product"]["definition_id"], "definition": policy["product"]["definition"]}, "observations": [observation], "dependencies": selection["governing_sources"], "time_basis": "Frozen exact decision/candidate files; no mutable result directories"}, "attention": {"material_relations": [task_ref, claim], "invariants": [source("review", "INDEPENDENCE.md")], "semantic_sources": selection["governing_sources"], "exclusions": ["candidate repair", "acceptance", "Git/remote/model effects"], "prohibited_assumptions": ["counts establish semantics", "same family or fresh context proves independence"]}, "actor_authority": {"actor_id": actor_id, "role": "Reviewer", "capability": task_ref, "semantic": task_ref, "evaluation": predicate, "operation": task_ref, "decision": None, "acceptance": None, "publication": None, "territory": [], "tools": executor["tools"]}, "evidence_relations": {"admissible_evidence": [task_ref], "acquisition": selection["governing_sources"], "dependencies": [], "conjunction": None, "translation": None, "consumer": "root-executive", "return_contract": contract_ref}, "stop_change": {"invalidators": ["source/candidate/authority drift", "prior candidate exposure"], "stop_conditions": [str(duration) + " seconds", "required capability unavailable"], "residuals": ["First phase is preparation only" if phase == "expectation" else "Unperformed qualification remains open"], "re_entry": ["return exact missing premise and retained evidence"], "reconfiguration": []}, "profile_additions": {"reviewer": {"claim": claim, "composition": task_ref, "population": claim, "oracle": predicate, "ordinary_module_path": source("review", lane + "/SELECTION.json"), "falsification_condition": predicate, "independence": policy["independence_policy"], "assurance": source("review", "INDEPENDENCE.md"), "severity_scale": source("review", "SEVERITY.md")}}}
    # The packet's refs have to be registered before policies are frozen. A
    # supplied governing selection must include these two method owner files.
    for required_source in [frame, algebra]:
        if not any(x["root"] == required_source["root"] and x["path"] == required_source["path"] for x in needed):
            raise RuntimeError("Selection must include frame/result owner: " + required_source["path"])
    late = selection["governing_sources"] + population + selection["proof_sources"] + [frame, algebra, policy["product"]["definition"], source("review", lane + "/SELECTION.json")]
    assembled = public_call(folder, policy_path, backend + "-review-" + phase + "-assemble", "context.assemble", {"packet": packet, "models": [], "sources": [], "late_acquisition": late, "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})
    context = assembled["result"]["artifact"]
    preflight = public_call(folder, policy_path, backend + "-review-" + phase + "-preflight", "contract.preflight", {"context": context, "grant_id": grant_id, "executor_id": executor_id, "result_key": "T001/review/" + backend + "/" + phase, "observations": [observation]})
    value = preflight["result"]["value"]
    result.update({"observation": observation, "context": context, "preflight": preflight["result"]["artifact"], "decision": value["decision"], "contract_state": value["contract_state"], "contract_sha256": value["contract_sha256"], "gaps": value["gaps"], "fit": assembled["result"]["value"]["fit"]})
    save(folder / "READINESS.json", result)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--selection", required=True, type=Path)
    parser.add_argument("--selection-sha256", required=True)
    parser.add_argument("--phase", choices=["expectation", "candidate"], required=True)
    parser.add_argument("--expectation")
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--lane")
    args = parser.parse_args()
    print(json.dumps(prepare(args.selection.resolve(), args.selection_sha256, args.phase, args.expectation, args.preflight, args.lane), indent=2))
