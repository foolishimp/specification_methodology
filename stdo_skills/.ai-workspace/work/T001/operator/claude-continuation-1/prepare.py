"""Bounded continuation setup over the existing native APIs. Never dispatch."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
OLD = HERE.parent / "successor-1"
spec = importlib.util.spec_from_file_location("previous_operator_preparation", OLD / "prepare.py")
p = importlib.util.module_from_spec(spec); sys.modules[spec.name] = p; spec.loader.exec_module(p)
save, sha, pin = p.save, p.sha, p.pin
BASE = json.loads((OLD / "executive-policy.json").read_text())
WORKER = json.loads((OLD / "claude/worker-policy.json").read_text())
SESSION = "9069a765-b3ee-4a03-8f71-6288ce3b57b6"
ATTEMPT = "a8f5dd10d123bcc8d5be3353eee07e954f8b837c37044dba83fab7acf1ec0997"


def ref(name):
    return {"engine": "workspace-regular-file", "root": "continuation", "path": name, "object": None, "sha256": sha(HERE / name), "selector": None}


def call(policy, name, operation, arguments):
    request = {"schema": "a_c.fd-support.request/1", "id": name, "operation": operation, "arguments": arguments}
    path = HERE / "requests" / (name + ".json"); save(path, request)
    argv = [str(p.PYTHON), "-B", str(p.CLI), "--policy", str(policy), "--policy-sha256", sha(policy), "--principal", "executive", "call", "--request", str(path)]
    completed = subprocess.run(argv, cwd=p.PRODUCT, capture_output=True, timeout=60)
    save(HERE / "responses" / (name + ".invocation.json"), {"argv": argv, "returncode": completed.returncode})
    save(HERE / "responses" / (name + ".stdout.json"), completed.stdout.decode())
    save(HERE / "responses" / (name + ".stderr.txt"), completed.stderr.decode())
    result = json.loads(completed.stdout)
    if completed.returncode or result.get("status") != "ok":
        raise RuntimeError("Public operation refused; retained response " + name)
    return result


def prepare():
    # Verify all originally selected production dependencies; no source change.
    for dep in BASE["executors"]["claude-cli-successor-1"]["dependencies"]:
        root = Path(BASE["sources"][dep["root"]]["path"])
        if sha(root / dep["path"]) != dep["sha256"]:
            raise RuntimeError("Selected dependency changed: " + dep["path"])
    actual_definition = Path(BASE["sources"]["product"]["path"]) / BASE["product"]["definition"]["path"]
    if sha(actual_definition) != BASE["product"]["definition"]["sha256"]:
        raise RuntimeError("Product definition changed")
    process = json.loads((OLD / "claude/actor-cli-output/process.json").read_text())
    sessions = set(); models = set()
    for line in (OLD / "claude/actor-cli-output/vendor.stdout").read_text().splitlines():
        try:
            value = json.loads(line)
        except ValueError:
            continue
        if value.get("type") == "system" and value.get("subtype") == "init":
            sessions.add(value["session_id"]); models.add(value["model"])
    if sessions != {SESSION}:
        raise RuntimeError("Exact retained Claude session differs")
    check = subprocess.run(["ps", "-p", str(process["pid"]), "-o", "pid=,comm="], capture_output=True, text=True)
    if check.returncode == 0:
        raise RuntimeError("Prior actor PID still present")
    observed_files = [str(x.relative_to(p.PRODUCT)) for x in (p.PRODUCT / "build_tenants/claude").rglob("*") if x.is_file()]
    if observed_files:
        raise RuntimeError("Expected empty Claude tenant changed; reconcile observed files")
    history = {"prior_attempt": p.artifact(ATTEMPT), "process": process, "session": SESSION, "reported_model": sorted(models), "current_direct_pid": {"argv": ["ps", "-p", str(process["pid"]), "-o", "pid=,comm="], "returncode": check.returncode, "stdout": check.stdout}, "tenant_files": observed_files, "root_observation": "Root reported no remaining successor-1/tenant commands", "limits": ["Timeout is not rollback; generic external/descendant effects remain unknown", "No closed Worker return or candidate assessment was produced", "Retained source acquisitions have original provenance, not current observations"], "continuation": "Root explicitly selects same actual Claude session with a new activation and existing fixed method/tool/model basis; no old dispatch is replayed"}
    acquisitions = []
    for path in (p.EVIDENCE / "objects").glob("*.json"):
        d = json.loads(path.read_text()); payload = d.get("payload", {})
        actor = d.get("provenance", {}).get("actor") or {}
        if d["kind"] == "operation" and actor.get("actor_id") == WORKER["principals"]["claude"]["actor_id"] and payload.get("request", {}).get("operation") == "source.read" and payload["response_without_evidence"]["status"] == "ok":
            src = payload["request"]["arguments"]["source"]
            root = Path(WORKER["sources"][src["root"]]["path"])
            acquisitions.append({"operation_evidence": p.artifact(path.stem), "source": src, "bytes_still_match": sha(root / src["path"]) == src["sha256"]})
    history["retained_acquisitions"] = acquisitions
    save(HERE / "HISTORY.json", history)
    help_run = subprocess.run([str(p.CLAUDE), "--help"], capture_output=True, text=True, timeout=20)
    if help_run.returncode or "--resume" not in help_run.stdout or "--system-prompt-snapshot" not in help_run.stdout:
        raise RuntimeError("Required actual Claude resume controls unavailable")
    save(HERE / "HOST-HELP.json", {"argv": [str(p.CLAUDE), "--help"], "returncode": help_run.returncode, "stdout": help_run.stdout, "stderr": help_run.stderr})
    save(HERE / "DECISIONS.md", """# Root bounded Claude continuation

Root selected continuation of actual Claude session 9069a765-b3ee-4a03-8f71-6288ce3b57b6 after the 600-second source-acquisition run timed out with no tenant files and no closed return. The recorded direct parent is closed and absent; unknown external effects stay explicit. No old dispatch is retried. This new activation resumes the same declared actor under a 1200-second bound.

The owner, Product definition, released method, common WHAT, tool implementation and configured model/effort remain unchanged. Existing T001 owner selects the same mechanism and result surface; this Root selection narrows delivery to actual Claude materialization and a compact closed return. Model init previously reported claude-fable-5-1; future resolution is observed, not imposed.

The supported --resume flag selects that session. --system-prompt-snapshot off ensures the explicit new activation/startup is used instead of silently retaining the old append-system-prompt. This is a per-invocation setting, no global configuration mutation. Artifact contents still use work.write; scoped mkdir/read-only validation remain permitted. The granted tenant and actor evidence territories remain the same; no peer acquisition or mutation is allowed.

Stable decision-input observation is the return Context basis. Target directories are observed separately only for launch/preimage safety; intended new files do not falsify the stable decision basis. Each Worker write acquires its own current target observation. No original return or earlier currentness result is rewritten. Root will review the exact native preflight before dispatch.
""")
    task = """# Claude continuation: construct the package now

This is a new explicitly admitted activation in your SAME retained Claude session. Your prior 600-second activation ended after acquisition with no tenant files or closed return. Root has reconciled the absent target and closed direct parent; generic external effects remain unknown. Read the new Context and use this activation's policy/grant/return contract, not a prior request ID or dispatch.

Use the exact shared WHAT and STDO3.0.1 sources you already acquired and retained. No source/method/model change occurred. Do not repeat broad contract research, tools catalogs or whole-method reading. Reacquire only a missing or changed deciding premise. SOURCE-ROUTES.json preserves exact pointers; HISTORY.json retains actual prior acquisition evidence with its provenance.

Deliver a concise design FIRST, then a coherent useful Claude skill package, scoped install/update/remove instructions, focused package checks, an exact inventory and a compact author assessment. Choose your own skill names and decomposition. Prioritize actual materialized artifacts over more planning. All shared SK-01 to SK-12 remain required; actual-host Q01-Q12 qualification and independent review stay open. Do not read the Codex tenant.

Territory remains build_tenants/claude/ and .ai-workspace/work/T001/claude/actor/successor-1/. Empty design/, skills/ and tests/ directories already exist. Bash may mkdir ordinary descendants inside those territories, inspect permitted sources and run read-only/in-memory focused checks. ALL artifact file contents must use a_c work.write. No Git, remote/model/subagent call, global/shared source edit or peer access. Public CLI on stdin is the normal transport; MCP is not required. Compose request JSON in memory and call --request -; no request file is needed.

Use this new registered grant, exact target preimage and your OWN current workspace.observe for each write. For a new file use sha256:null only after confirming absence and a present parent. Retain returned postimage/OperationEvidence. On uncertain completion reconcile before any repeat. The stable Context observation covers deciding inputs only; target-preimage observations are separate evidence.

The two return assessments are the same actual instruction-fitness and package-integrity predicates in PREDICATES.md. Check the exact files, run a focused useful read-only package check, and record a compact assessment tied to inventory; source existence or test count is not fitness. Candidate availability, author assessment, actual host trials, independence and acceptance remain separate. Stop construction in time to emit the closed return within 1200 seconds; no automatic retry. Unavailable or unperformed work stays explicit.

Return ONE original a_c.fd-support.closed-return/1 JSON object, no fences. Copy THIS Context's frame, activation identity, subject, original method/observation basis, actor and consumer. Use RETURN-CONTRACT's exact predicates, actual assessment/effect evidence and candidate SourceRef. candidate_ready means exact candidate plus transition evidence, not acceptance. If incomplete, return the real partial files and blocker. Do not start another stage.
"""
    save(HERE / "TASK.md", task)
    save(HERE / "PREDICATES.md", (OLD / "claude/PREDICATES.md").read_text())
    routes = json.loads((OLD / "claude/SOURCE-ROUTES.json").read_text())
    routes["required"] = [x for x in routes["required"] if not (x["root"] == "successor" and x["path"] in ("claude/HISTORY.json", "claude/PREDICATES.md"))] + [ref("PREDICATES.md"), ref("HISTORY.json")]
    save(HERE / "SOURCE-ROUTES.json", routes)
    task_ref = ref("TASK.md"); decision = ref("DECISIONS.md")
    grant_id = "urn:stdo-skills:T001:claude:construction:3"
    scope = {"path": str(HERE), "kind": "workspace", "writable": False, "read_scope": [{"path": n, "kind": "file"} for n in ["TASK.md", "DECISIONS.md", "HISTORY.json", "PREDICATES.md", "SOURCE-ROUTES.json", "RETURN-CONTRACT.json", "STARTUP.txt", "worker-policy.json", "actor-plan.json"]]}
    worker = copy.deepcopy(WORKER); worker["id"] = "urn:stdo-skills:T001:claude:continuation:1"
    worker["sources"]["continuation"] = scope
    worker["principals"]["claude"]["role_binding"] = task_ref
    grant = copy.deepcopy(next(iter(worker["grants"].values())))
    grant["id"] = grant_id; grant["authority_sources"] += [decision, task_ref]; grant["outcome"]["source"] = task_ref
    worker["grants"] = {grant_id: grant}
    save(HERE / "worker-policy.json", worker)
    cli_argv = [str(p.PYTHON), "-B", str(p.CLI), "--policy", str(HERE / "worker-policy.json"), "--policy-sha256", sha(HERE / "worker-policy.json"), "--principal", "claude", "call", "--request", "-"]
    startup = "Explicit Root successor activation in the same Claude session. Previous activation ended; use the new exact Context, policy and grant. Construct the package now using retained acquired sources; avoid repeating contract research. Read TASK at " + json.dumps(task_ref) + ". Public CLI argv with full JSON envelope on stdin: " + json.dumps(cli_argv) + ". New work.write grant " + grant_id + ". Preserve stable Context return basis; obtain separate current target observations. All artifacts through work.write, scoped mkdir/validation allowed, no peer/Git/model effects. Record design, materialize skills, inventory, compact assessment, then original closed-return JSON within1200seconds."
    save(HERE / "STARTUP.txt", startup + "\n")
    plan = json.loads((OLD / "claude/actor-plan.json").read_text())
    plan["id"] = worker["id"] + ":plan"
    plan["argv"] = plan["argv"][:-1] + [startup, "--resume", SESSION, "--system-prompt-snapshot", "off"]
    plan["dependencies"] = [x for x in plan["dependencies"] if Path(x["path"]).is_relative_to(p.TOOL)] + [pin(HERE / "worker-policy.json"), pin(HERE / "STARTUP.txt")]
    plan["limits"]["timeout_ms"] = 1200000
    plan["evidence_directory"] = str(HERE / "actor-cli-output")
    plan["settings"]["session_continuity"] = {"session_id": SESSION, "prior_attempt": ATTEMPT, "new_activation": grant_id, "new_system_prompt_snapshot": "off; actual updated activation"}
    save(HERE / "actor-plan.json", plan)
    old_contract = json.loads((OLD / "claude/RETURN-CONTRACT.json").read_text())
    old_contract["id"] = worker["id"] + ":return"; old_contract["authority_source"] = task_ref
    for evaluation in old_contract["required_evaluations"]:
        evaluation["predicate"] = ref("PREDICATES.md")
    save(HERE / "RETURN-CONTRACT.json", old_contract)
    executive = copy.deepcopy(BASE); executive["id"] = worker["id"] + ":executive"
    executive["sources"]["continuation"] = scope
    executive["principals"] = {"executive": BASE["principals"]["executive"], "claude": worker["principals"]["claude"]}
    executive["principals"]["executive"]["role_binding"] = decision
    granted = copy.deepcopy(BASE["grants"]["urn:stdo-skills:T001:claude:construction:2"])
    granted["id"] = grant_id; granted["authority_sources"] += [decision, task_ref]; granted["outcome"]["source"] = task_ref; granted["executors"] = ["claude-continuation-1"]
    executive["grants"] = {grant_id: granted}
    executor = copy.deepcopy(BASE["executors"]["claude-cli-successor-1"])
    executor["id"] = "claude-continuation-1"
    executor["argv"] = [str(p.PYTHON), "-B", str(p.ADAPTER), "--plan", str(HERE / "actor-plan.json"), "--plan-sha256", sha(HERE / "actor-plan.json")]
    executor["dependencies"] = [x for x in executor["dependencies"] if x["root"] != "successor"] + [ref(n) for n in ["worker-policy.json", "STARTUP.txt", "actor-plan.json"]]
    executor["settings"]["timeout_ms"] = 1210000
    executive["executors"] = {executor["id"]: executor}
    save(HERE / "executive-policy.json", executive)
    adapter_spec = importlib.util.spec_from_file_location("continuation_actor_cli", p.ADAPTER)
    adapter = importlib.util.module_from_spec(adapter_spec); sys.modules[adapter_spec.name] = adapter; adapter_spec.loader.exec_module(adapter)
    adapter.load_plan(HERE / "actor-plan.json", sha(HERE / "actor-plan.json"))
    save(HERE / "PLAN-CHECK.json", {"adapter_validation": "passed", "plan": pin(HERE / "actor-plan.json"), "session": SESSION, "host_or_model_invoked": False})
    inputs = BASE["grants"]["urn:stdo-skills:T001:claude:construction:2"]["preconditions"]
    stable_scopes = [{"root": x["root"], "path": x["path"], "kind": "file"} for x in [BASE["product"]["definition"], BASE["method_profile"]["source"]] + inputs]
    policy_path = HERE / "executive-policy.json"
    stable = call(policy_path, "claude-c1-stable-observe", "workspace.observe", {"scope": stable_scopes})["result"]["artifact"]
    targets = call(policy_path, "claude-c1-target-observe", "workspace.observe", {"scope": granted["territory"]})["result"]["artifact"]
    packet = json.loads((OLD / "requests/claude-s1-assemble.json").read_text())["arguments"]["packet"]
    packet["activation"] = {"id": grant_id, "revision": "3", "configuration": task_ref}
    packet["frame"]["revision"] = "3"; packet["frame"]["evaluation"] = ref("PREDICATES.md")
    packet["subject_basis"]["observations"] = [stable]
    packet["subject_basis"]["time_basis"] = "Stable deciding inputs only; intended target changes are separate transition evidence"
    packet["attention"]["material_relations"] = [ref("SOURCE-ROUTES.json"), ref("HISTORY.json")]
    packet["actor_authority"]["evaluation"] = ref("PREDICATES.md"); packet["actor_authority"]["operation"] = task_ref
    packet["evidence_relations"].update({"admissible_evidence": [ref("PREDICATES.md"), task_ref], "acquisition": routes["required"] + routes["deciding_method"], "dependencies": [ref("HISTORY.json")], "return_contract": ref("RETURN-CONTRACT.json")})
    packet["stop_change"]["stop_conditions"] = ["1200 seconds", "genuine unsupported required operation"]
    packet["stop_change"]["reconfiguration"] = ["Explicit resumed-session continuation of closed attempt " + ATTEMPT + "; no replay or assumed rollback"]
    packet["profile_additions"]["worker"]["operation_grant_id"] = grant_id
    # Everything already acquired can remain a late exact route; current TASK,
    # predicates and return contract alone are delivered as content again.
    late = inputs + routes["deciding_method"] + [BASE["product"]["definition"], ref("HISTORY.json"), ref("SOURCE-ROUTES.json"), packet["actor_authority"]["capability"], packet["frame"]["declaration"], packet["frame"]["result_algebra"]]
    late = list({json.dumps(x, sort_keys=True): x for x in late}.values())
    assembled = call(policy_path, "claude-c1-assemble", "context.assemble", {"packet": packet, "models": [], "sources": [], "late_acquisition": late, "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})
    context = assembled["result"]["artifact"]
    preflight = call(policy_path, "claude-c1-preflight", "contract.preflight", {"context": context, "grant_id": grant_id, "executor_id": executor["id"], "result_key": "T001/claude/construction-3", "observations": [stable, targets]})
    value = preflight["result"]["value"]
    if value["decision"] != "admitted" or value["contract_state"] != "admitted" or value["gaps"]:
        raise RuntimeError("Actual preflight not admitted")
    ready = {"plan": pin(HERE / "actor-plan.json"), "policy": pin(policy_path), "context": context, "basis_observations_for_return_check": [stable], "preflight_only_target_observation": targets, "preflight": preflight["result"]["artifact"], "contract_sha256": value["contract_sha256"], "decision": value["decision"], "gaps": value["gaps"], "fit": assembled["result"]["value"]["fit"], "session": SESSION, "actor_id": worker["principals"]["claude"]["actor_id"], "new_activation": grant_id, "no_dispatch": True, "method_source_model_unchanged": True}
    save(HERE / "READINESS.json", ready)
    save(HERE / "root-dispatch.request.json", {"schema": "a_c.fd-support.request/1", "id": "root-T001-claude-continuation1-dispatch", "operation": "dispatch.start", "arguments": {"preflight": ready["preflight"]}})
    print(json.dumps({"readiness": str(HERE / "READINESS.json"), "sha256": sha(HERE / "READINESS.json"), "no_dispatch": True}))


if __name__ == "__main__":
    prepare()
