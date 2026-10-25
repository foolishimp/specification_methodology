"""Prepare Root-selected one-shot read-only reentry; never launch an actor.

This bounded fixture construction reuses the frozen launcher/runtime and the
existing deployment workspace. It does not modify the general preparer, install
skills, publish a report or mutate the previous attempt's control files.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import time

Q = Path(__file__).resolve().parent.parent
SESSION = "3f43aa78-a75d-4a83-a00a-f53a718022d2"
LANE = "release-deploy-repair-2-close"
OLD_ATTEMPT = "657e9666e081eacd8893db39ea3366eafd71659399e8e31243f2ce3de83afbcc"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def pin(path):
    return {"path": str(path), "sha256": sha(path)}


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = value if isinstance(value, bytes) else (value.encode() if isinstance(value, str) else (json.dumps(value, indent=2, sort_keys=True) + "\n").encode())
    with path.open("xb") as stream:
        stream.write(raw)


def main():
    old_prepared_path = Q / "prepared/claude-release-deploy-repair-2.json"
    old = json.loads(old_prepared_path.read_text())
    old_control, workspace = Path(old["control"]), Path(old["workspace"])
    control = old_control.parent / "close-control"
    control.mkdir(exist_ok=False)
    (control / "evidence").mkdir()
    policy = json.loads((old_control / "executive-policy.json").read_text())
    plan = json.loads((old_control / "actor-plan.json").read_text())
    launch = json.loads((old_control / "launch.json").read_text())
    old_context = json.loads((old_control / "evidence/objects" / (old["context"]["sha256"] + ".json")).read_text())["payload"]
    py = policy["executors"]["trial"]["executable"]["path"]
    cli = plan["environment"]["AC_ENTRY"]
    ident = "urn:stdo-skills:qualification:claude:" + LANE
    process = subprocess.run(["ps", "-axo", "pid=,ppid=,pgid=,lstart=,stat=,comm="], capture_output=True, text=True, check=True)
    matching = []
    for row in process.stdout.splitlines():
        fields = row.split(None, 3)
        if len(fields) == 4 and set(map(int, fields[:3])) & {8774, 8796, 8819}:
            matching.append(row)
    if matching:
        raise ValueError("Prior local process or group still observed; Root must reconcile")
    current = []
    source = json.loads((workspace / "retained/SOURCE.json").read_text())
    for name in ("original_payload", "original_manifest", "prior_prepared"):
        expected = source[name]
        found = pin(Path(expected["path"]))
        if found != expected:
            raise ValueError("Original source identity changed: " + name)
        current.append({"name": name, "expected": expected, "observed": found, "matched": True})
    targets = ["retained/SOURCE.json", "retained/release/payload.txt", "retained/release/manifest.json", "deploy-test/payload.txt", "deploy-test/manifest.json", "outputs/deployment.md"]
    effects = []
    for digest in ("995204894dc8c2ed8bda38608cd8dcd2075a8e50c478d932b5af57cfd7b1d5cc", "a4b809305881c243ff2da6fdfc33bf67e01615a2f5ade086a4f8fab82df928ba", "fce7dd942d0b28f3e0a02b4cef814803b558e84a928ebed98fdc60d68b60a512", "571095b9b62a64eecff7c62fb13c2564660ef92644c5d4b2e2da0aa80b6acdfb"):
        path = old_control / "evidence/objects" / (digest + ".json")
        if sha(path) != digest:
            raise ValueError("Prior acknowledged effect evidence changed")
        effects.append(pin(path))
    reconciliation = {"schema": "stdo_skills.readonly-close-reconciliation/1", "observed_ns": time.time_ns(), "prior_attempt": OLD_ATTEMPT, "native_session": SESSION, "prior_prepared": pin(old_prepared_path), "prior_process": pin(old_control / "actor-output/process.json"), "prior_capture": pin(Q / "results/claude-release-deploy-repair-2/INVENTORY.json"), "process_observation": {"argv": ["ps", "-axo", "pid=,ppid=,pgid=,lstart=,stat=,comm="], "returncode": process.returncode, "retained_pids": [8774, 8796, 8819], "matching_pid_ppid_pgid_rows": matching, "source_fact": "ac_support_effects starts supervisor and launcher in new sessions; actor_cli native child inherits launcher group 8796", "limit": "No matching current local process/group observed; detached descendants and external effects remain unknown. No kill or cleanup."}, "acknowledged_effects": effects, "current_targets": [pin(workspace / x) for x in targets], "fresh_source_identity_readback": current, "readback_owner": "Fixture Writer now; do not attribute this new source readback to the timed-out actor", "limits": ["Earlier timeout, returncode143, incomplete EOF and missing native usage totals remain retained", "All prior public tool calls have results; no unresolved target write was identified", "Only a final returned host observation remains; no deployment or report write is selected"]}
    save(control / "RECONCILIATION.json", reconciliation)
    selection = {"schema": "stdo_skills.readonly-close-selection/1", "tenant": "claude", "lane": LANE, "timeout_ms": 180000, "session": SESSION, "reconciliation": pin(control / "RECONCILIATION.json"), "old_attempt": OLD_ATTEMPT, "authority": "Root selected one same-session read-only close after process reconciliation, no host dispatch by this Writer", "writes": [], "no_further_loop": True}
    selection_path = Q / "selections" / ("claude-" + LANE + ".json")
    save(selection_path, selection)
    save(control / "SELECTION.json", selection)
    save(control / "INSTALL.json", (old_control / "INSTALL.json").read_bytes())
    prompt = "This is a read-only close of the same session. The earlier invocation timed out after its final report write was acknowledged. All previous deployment, publication, work.write, scratch, cleanup and report-edit authority is suspended for this turn. Do not repeat deployment or rewrite any file.\n\nReconcile the acknowledged completion with the current retained facts in " + str(control / "RECONCILIATION.json") + ". Read the existing deployed files and outputs/deployment.md only if needed. Return a compact truthful final status: what was deployed and verified, what remains limited by the earlier timeout, and any genuinely unresolved work. The fresh source-identity readback belongs to the fixture Writer, not your earlier invocation. You have 180 seconds; no continuation loop is selected.\n"
    save(control / "ordinary-prompt.txt", prompt)
    save(control / "ordinary-prompt.base.txt", prompt)
    task_text = "# One read-only same-session close\n\nRoot selected reentry to session " + SESSION + " only to return a truthful final observation of acknowledged deployment effects. No workspace or report writes, work.write, scratch, cleanup, publication, acceptance, redeployment or retries. Prior mutation grants are suspended for this turn. The new native policy has no mutation operation or grant; exposed built-in tools are Read, Glob and Grep. A distinct control Product owns only read observation, transport and evidence custody. Old Product files and their old authority records are historical inputs, not grants for this continuation. No tool or package update occurs. Root separately selects actual dispatch.\n"
    save(control / "TASK.md", task_text)
    save(control / "INTENT.md", "# Intent\nReturn one read-only observation after acknowledged deployment effects and a transport timeout.\n")
    save(control / "PRODUCT.md", "# Read-only close control\n\n## Product boundary\nExact read-only continuation, transport and observation custody. The earlier deployment's artifacts and authority remain separate.\n\n## Construction authority\nRoot selected this bounded preparation and separately selects dispatch; OWNER.json defines the read-only grant.\n")
    save(control / "GOALS.md", "# Selection\nReturn one truthful final observation without target effects; retain all earlier timeout and uncertainty evidence.\n")
    definition = json.loads((Q / "inputs-v3/governed/fixture_product.json").read_text())
    definition["product"].update({"definition_id": ident + ":controller", "name": "Read-only close control", "bounded_context": {"id": ident + ":boundary", "definition": "./PRODUCT.md#product-boundary"}})
    definition["constitution"]["additional_authorities"] = ["./INTENT.md", "./PRODUCT.md"]
    definition["constitution"]["agent_bootstrap"]["targets"] = ["./TASK.md"]
    definition["reference_frame_bases"] = [{"uri": "./TASK.md", "authority": ["./PRODUCT.md#construction-authority"], "applies_to": [definition["product"]["definition_id"]]}]
    definition["what"] = {"intent": "./INTENT.md", "product": "./PRODUCT.md", "specification": ["./TASK.md"]}
    definition["how"] = {"common": ["./OWNER.json"], "build_tenants": [{"id": ident + ":fixed-launcher", "root": "./actor-output/", "design": ["./TASK.md"], "implementation": ["./launch.json"]}]}
    definition["ticketing"]["goals"] = "./GOALS.md"
    save(control / "CONTROLLER.json", definition)
    policy["sources"]["control"]["path"] = str(control)
    policy["sources"]["control"]["read_scope"].append({"path": "RECONCILIATION.json", "kind": "file"})
    policy["sources"]["product"]["writable"] = False

    def ref(root, path):
        return {"engine": "workspace-regular-file", "root": root, "path": path, "object": None, "sha256": sha(Path(policy["sources"][root]["path"]) / path), "selector": None}

    scope = {"selection_sha256": sha(selection_path), "case": LANE, "purpose": "One read-only same-session returned observation after exact prior effects were reconciled", "host_artifact_writes": [], "physical_executor_writes": ["control/actor-output", "native host session persistence"], "forbidden": ["all workspace mutation", "old write grant reuse", "work.write", "publication", "scratch", "cleanup", "report rewrite", "deployment", "further retries"], "projection": "Exact ordinary prompt only; prior session is explicitly selected and retained"}
    owner = json.loads((old_control / "OWNER.json").read_text())
    owner["result_surface"]["root"] = str(control / "evidence")
    owner["scope"] = scope
    owner["authority"] = selection["authority"]
    save(control / "OWNER.json", owner)
    owner_ref, task, definition_ref = ref("control", "OWNER.json"), ref("control", "TASK.md"), ref("control", "CONTROLLER.json")
    policy["id"] = ident + ":policy"
    policy["evidence_root"] = str(control / "evidence")
    policy["product"] = {"definition_id": definition["product"]["definition_id"], "definition": definition_ref, "authority_binding": {"definition_locator": "/how/common/0", "owner_record": owner_ref, "mechanism": owner["mechanism"], "result_surface": owner["result_surface"], "scope": scope}}
    policy["authority_sources"] = [owner_ref]
    actor = copy.deepcopy(launch["return_actor"])
    actor["id"] = ident + ":physical-launcher"
    for name, principal in policy["principals"].items():
        principal["role_binding"] = task
        if name == "launcher": principal["actor_id"] = actor["id"]
        if name == "host":
            principal["actor_id"] = ident + ":host"
            principal["operations"] = ["tools.describe", "source.read", "workspace.observe", "evidence.read"]
    grant = copy.deepcopy(next(iter(policy["grants"].values())))
    grant_id = ident + ":launch"
    grant.update({"id": grant_id, "authority_sources": [owner_ref, task], "outcome": {"id": ident, "source": task}, "territory": [], "tools": ["native-host", "a_c.public-native301", "host.read-only"], "preconditions": [task]})
    grant["admission"]["authority_source"] = owner_ref
    worker = copy.deepcopy(policy)
    worker.update({"id": ident + ":host-policy", "principals": {"host": policy["principals"]["host"]}, "grants": {}, "executors": {}, "event_sinks": {}})
    save(control / "worker-policy.json", worker)
    worker_args = ["-B", cli, "--policy", str(control / "worker-policy.json"), "--policy-sha256", sha(control / "worker-policy.json"), "--principal", "host"]
    save(control / "mcp.json", {"mcpServers": {"stdo_ac": {"command": py, "args": worker_args + ["mcp"]}}})
    plan["id"] = ident + ":native-plan"
    plan["argv"] = [plan["executable"]["path"], "--resume", SESSION, "--print", "--output-format", "stream-json", "--verbose", "--permission-mode", "default", "--permission-prompts", "none", "--strict-mcp-config", "--mcp-config", str(control / "mcp.json"), "--tools", "Read,Glob,Grep", "--allowedTools", "Read,Glob,Grep,mcp__stdo_ac__source_read,mcp__stdo_ac__workspace_observe,mcp__stdo_ac__evidence_read,mcp__stdo_ac__tools_describe", "--disallowedTools", "Bash,Write,Edit,Skill,mcp__stdo_ac__work_write"]
    for dep in plan["dependencies"]:
        if Path(dep["path"]).parent == old_control:
            dep.update(pin(control / Path(dep["path"]).name))
    plan["dependencies"] += [pin(control / "RECONCILIATION.json")] + [pin(workspace / p) for p in targets]
    plan["environment"].update({"AC_POLICY": str(control / "worker-policy.json"), "AC_POLICY_SHA256": sha(control / "worker-policy.json")})
    plan["settings"].update({"fixture_case": LANE, "host_scope": "read-only continuation; no workspace mutations or prior write grant reuse", "resumed_native_session": SESSION})
    plan["evidence_directory"] = str(control / "actor-output")
    plan["limits"]["timeout_ms"] = 180000
    save(control / "actor-plan.json", plan)
    activation = ident + ":activation:1"
    launch.update({"case": {"tenant": "claude", "lane": LANE}, "activation_id": activation, "return_actor": actor, "actor_plan": pin(control / "actor-plan.json"), "ordinary_prompt": pin(control / "ordinary-prompt.txt")})
    save(control / "launch.json", launch)
    executor = policy["executors"]["trial"]
    executor["argv"] = [py, "-B", str(Q / "launch_fixture.py"), "--config", str(control / "launch.json"), "--config-sha256", sha(control / "launch.json")]
    executor["dependencies"] = [ref(d["root"], d["path"]) for d in executor["dependencies"]] + [ref("control", "RECONCILIATION.json")] + [ref("product", p) for p in targets]
    executor["environment"].update({"AC_POLICY": str(control / "worker-policy.json"), "AC_POLICY_SHA256": sha(control / "worker-policy.json")})
    executor.update({"actor_id": actor["id"], "effect_scope": scope, "tools": grant["tools"]})
    executor["settings"]["timeout_ms"] = 190000
    policy["grants"] = {grant_id: grant}
    policy["event_sinks"]["events"]["authority_source"] = owner_ref
    save(control / "executive-policy.json", policy)
    contract = json.loads((old_control / "RETURN-CONTRACT.json").read_text())
    contract.update({"id": ident + ":physical-return", "authority_source": task})
    save(control / "RETURN-CONTRACT.json", contract)

    def call(name, operation, arguments):
        request = {"schema": "a_c.fd-support.request/1", "id": ident + ":" + name, "operation": operation, "arguments": arguments}
        request_path = control / "requests" / (name + ".json")
        save(request_path, request)
        argv = [py, "-B", cli, "--policy", str(control / "executive-policy.json"), "--policy-sha256", sha(control / "executive-policy.json"), "--principal", "executive", "call", "--request", str(request_path)]
        result = subprocess.run(argv, cwd=workspace, capture_output=True, timeout=60)
        save(control / "responses" / (name + ".stdout.json"), result.stdout)
        save(control / "responses" / (name + ".stderr.txt"), result.stderr)
        save(control / "responses" / (name + ".invocation.json"), {"argv": argv, "returncode": result.returncode})
        response = json.loads(result.stdout)
        if result.returncode != 0 or response.get("status") != "ok":
            raise ValueError("Public preparation refused; preserve inputs: " + name + ": " + str(response.get("refusal")))
        return response

    call("describe", "tools.describe", {})
    call("acquire-prompt", "source.read", {"source": ref("control", "ordinary-prompt.txt"), "encoding": "utf8"})
    package = json.loads((control / "INSTALL.json").read_text())
    stable = [definition_ref, owner_ref, task, ref("control", "ordinary-prompt.txt"), ref("control", "INSTALL.json"), ref("control", "RECONCILIATION.json")] + [ref("product", p) for p in targets] + [ref("product", x["path"]) for x in package["files"]] + [ref("product", ".claude/stdo-skills-claude.receipt.json")]
    observation = call("observe-stable-inputs", "workspace.observe", {"scope": [{"root": x["root"], "path": x["path"], "kind": "file"} for x in stable]})["result"]["artifact"]
    packet = copy.deepcopy(old_context["packet"])
    subject = {"id": ident + ":read-only-observation", "sha256": sha(selection_path)}
    packet["activation"] = {"id": activation, "revision": "1", "configuration": task}
    packet["frame"].update({"declaration": task, "evaluation": task})
    packet["subject_basis"].update({"subject": subject, "product": {"id": definition["product"]["definition_id"], "definition": definition_ref}, "observations": [observation], "dependencies": stable, "time_basis": "Fresh readback plus exact historical timeout/effect evidence; target bytes are immutable inputs for this close"})
    packet["attention"].update({"material_relations": stable, "invariants": stable, "semantic_sources": [task], "exclusions": ["independent oracle", "unrelated prior sessions"], "prohibited_assumptions": ["prior timeout vanished", "prior write authority remains active", "same-session completion proves general termination", "fixture Writer readback was performed by the earlier actor"]})
    packet["actor_authority"].update({"actor_id": actor["id"], "capability": task, "operation": owner_ref, "territory": [], "tools": grant["tools"]})
    packet["evidence_relations"].update({"admissible_evidence": stable, "acquisition": stable, "return_contract": ref("control", "RETURN-CONTRACT.json")})
    packet["stop_change"].update({"stop_conditions": ["180-second native ceiling", "required capability unavailable", "target drift"], "residuals": ["Prior timeout, EOF and usage limits retained", "Detached descendants remain unknown"], "re_entry": ["No further loop selected"]})
    packet["profile_additions"]["worker"] = {"operation_grant_id": grant_id, "mutation_subject": subject, "territory": []}
    context = call("assemble", "context.assemble", {"packet": packet, "models": [], "sources": stable, "late_acquisition": [], "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})["result"]["artifact"]
    preflight = call("preflight", "contract.preflight", {"context": context, "grant_id": grant_id, "executor_id": "trial", "result_key": ident, "observations": [observation]})["result"]["artifact"]
    baseline = {"schema": "stdo_skills.workspace-preimage/1", "workspace": str(workspace), "files": [{"path": str(p.relative_to(workspace)), "sha256": sha(p)} for p in sorted(workspace.rglob("*")) if p.is_file()]}
    save(control / "WORKSPACE-BEFORE.json", baseline)
    prepared = {"schema": "stdo_skills.qualification-prepared/1", "tenant": "claude", "lane": LANE, "workspace": str(workspace), "control": str(control), "selection": pin(selection_path), "installed": pin(control / "INSTALL.json"), "policy": pin(control / "executive-policy.json"), "context": context, "preflight": preflight, "effect_target_preimage": None, "workspace_preimage": pin(control / "WORKSPACE-BEFORE.json"), "root_dispatch_selected": False, "host_dispatches": 0, "resumes": {"session": SESSION, "prior_attempt": OLD_ATTEMPT}, "next": "Root inspects exact read-only plan and selects one dispatch; no further loop"}
    save(control / "PREPARED.json", prepared)
    save(Q / "prepared" / ("claude-" + LANE + ".json"), prepared)
    print(json.dumps(prepared, indent=2))


if __name__ == "__main__":
    main()
