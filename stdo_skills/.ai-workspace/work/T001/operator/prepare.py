"""Trusted, create-only preparation of fixed real-host plans and public preflights.

No dispatch, model invocation, admission emulator or tool implementation lives here.
The only executable decisions after drafting are made by the existing public CLI.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess

REPO = Path(__file__).resolve().parents[5]
PRODUCT = REPO / "stdo_skills"
OPERATOR = Path(__file__).resolve().parent
TOOL = REPO / "a_c"
METHOD = Path("/Users/jim/Library/Application Support/STDO/releases/v3.0.1-rc.1")
PYTHON = Path("/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python").resolve()
CODEX = Path("/opt/homebrew/lib/node_modules/@openai/codex/node_modules/@openai/codex-darwin-arm64/vendor/aarch64-apple-darwin/bin/codex").resolve()
CLAUDE = Path("/Users/jim/.local/share/claude/versions/2.1.306").resolve()
CORE = TOOL / "build_tenants/graphify/code/ac_support_core.py"
CLI = TOOL / "build_tenants/graphify/code/ac_support.py"
ADAPTER = TOOL / "build_tenants/graphify/examples/fd-support/actor_cli.py"
PROFILE = TOOL / "build_tenants/graphify/design/fd-method-stdo-3.0.1.json"
EVIDENCE = OPERATOR / "protected-evidence"
MANIFEST = "60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8"
COMMON = "a6d348b8385ea453ce29362fb9d74559304b1b91743b3c9ea31a83a9f02b5f2d"
PROFILE_ID = "urn:a-c:fd-support:method:stdo-3.0.1-rc.1:executive:1"
READ = ["tools.describe", "workspace.observe", "source.read", "records.find", "records.read", "graph.project", "relations.query", "evidence.read", "work.project"]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path: Path, value: object) -> None:
    raw = value.encode() if isinstance(value, str) else (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != raw:
            raise RuntimeError("Existing preparation differs; retain it and select a successor: " + str(path))
        return
    with path.open("xb") as stream:
        stream.write(raw)


def ref(root: str, path: str, *, lines: list[int] | None = None) -> dict:
    roots = {"product": PRODUCT, "tool": TOOL, "method": METHOD, "operator": OPERATOR, "host": Path("/")}
    p = roots[root] / path
    return {"engine": "workspace-regular-file", "root": root, "path": path, "object": None, "sha256": sha(p), "selector": None if lines is None else {"lines": lines}}


def host_ref(path: Path) -> dict:
    return ref("host", str(path).lstrip("/"))


def pin(path: Path) -> dict:
    return {"path": str(path), "sha256": sha(path)}


def request(identity: str, operation: str, arguments: dict) -> dict:
    return {"schema": "a_c.fd-support.request/1", "id": identity, "operation": operation, "arguments": arguments}


def call(policy: Path, principal: str, identity: str, operation: str, arguments: dict) -> dict:
    req = OPERATOR / "requests" / (identity + ".json")
    save(req, request(identity, operation, arguments))
    argv = [str(PYTHON), "-B", str(CLI), "--policy", str(policy), "--policy-sha256", sha(policy), "--principal", principal, "call", "--request", str(req)]
    output = OPERATOR / "responses" / identity
    if output.with_suffix(".stdout.json").exists():
        raise RuntimeError("Retain previous public invocation; select a new invocation ID: " + identity)
    done = subprocess.run(argv, cwd=PRODUCT, capture_output=True, timeout=60)
    save(output.with_suffix(".invocation.json"), {"argv": argv, "returncode": done.returncode})
    save(output.with_suffix(".stdout.json"), done.stdout.decode())
    save(output.with_suffix(".stderr.txt"), done.stderr.decode())
    parsed = json.loads(done.stdout)
    if done.returncode != 0 or parsed.get("status") != "ok":
        raise RuntimeError("Public operation refused: " + identity + ": " + json.dumps(parsed.get("refusal")))
    return parsed


def task(tenant: str) -> str:
    return f"""# {tenant.title()} tenant construction, T001

Root's bounded work grant selects the common WHAT at inventory {COMMON} for this construction experiment under static STDO3.0.1 RC1. The exact common requirements and scenarios determine success. Build your own {tenant} tenant: record a concise design before writing its implementation, then construct usable skills and necessary supported installation/verification resources. Your skill count, names, descriptions, decomposition and host integration are design choices. Do not acquire the other tenant's design, implementation, output or review.

Read the exact Product, shared requirements, scenarios and reference-frame basis through the configured public source.read tool. Acquire HOST.md for the independently sourced host mechanics and support limits. Use the native profile and actual tools.describe schemas. Do not load the entire method; source.read deciding sections through supplied SourceRefs when needed. Existing immutable installed method owns semantics; no rewritten local method. Shared requirement and tool semantics remain outside the tenant.

Your exclusive effect territory is build_tenants/{tenant}/ plus .ai-workspace/work/T001/{tenant}/actor/. Author every deliverable artifact through work.write using your registered grant, current target SourceRef and your own workspace.observe; read the actual postimage and OperationEvidence afterwards. The protected operator/evidence directory, common source, Product Definition, a_c, Git, remote services and global host configuration are outside your mutation grant. Host facilities may compute or inspect permitted inputs; they may not bypass work.write for deliverables. No subagent or nested model invocation is selected. No retries of this actor activation. Unknown effect completion requires a residual and reconciliation, not a repeated write.

Design records map requirements to algorithms and algorithms to host mechanisms, including exact source pin, actual discovery/invocation, proportional direct and coordinated work, source-first review, recovery, install/update/remove, failure semantics and finite proof. The native tool has no supported results.conjoin operator: use only the granted F_P consumption/decision relation; do not claim deterministic native conjunction. Support automatic and explicit discovery; do not disable implicit invocation. No universal ticket/reviewer ceremony. Preserve authorization already given.

Use current host capabilities with inherited model/effort defaults. Material facts and uncertain settings must be distinguished. Scope is a candidate, no release/publication or general reliability/efficiency claim. Common Q01-Q12 are finite obligations; executable host trials and independent review remain for Root's later activations. If local checks cannot run through your available tools, retain that absence. Write a coherent initial candidate rather than simulate passing trials.

Provide a tenant-local README with real supported installation, explicit invocation, normal task behavior, tool policy prerequisites and scoped update/removal. Include a candidate inventory with file paths and observed SHA256s. Preserve all initial attempts. Stop by the 600-second bound, returning partial artifacts if needed.

Return exactly one JSON object matching a_c.fd-support.closed-return/1 as your final message, with no Markdown fences. Copy frame id/revision, activation identity, subject, basis and consumer from the actual Context. Actor identity/family/authorship are supplied in that Context. Keep the original Context basis in the return even when effect proof cites your independently acquired Worker observations. For each required evaluation provide the exact predicate SourceRef, actual domain_outcome, one lawful core_value, and evidence; list an unperformed evaluation in not_performed instead. work_result is candidate_ready only with a real candidate SourceRef and actual transition evidence; otherwise use incomplete/refused/re_entry_requested and preserve residuals. Output availability is not assessment or acceptance. You do not start the next stage.
"""


def prepare(expected_core: str, tool_candidate: Path, tool_candidate_sha: str) -> dict:
    if sha(CORE) != expected_core:
        raise RuntimeError("Mechanism does not match selected repaired freeze")
    tool_candidate = tool_candidate.resolve(strict=True)
    if sha(tool_candidate) != tool_candidate_sha:
        raise RuntimeError("Tool candidate selection changed")
    tool_selection = json.loads(tool_candidate.read_text())
    if not tool_selection.get("source"):
        raise RuntimeError("Selected tool candidate has no source inventory")
    for item in tool_selection["source"]:
        if sha(REPO / item["path"]) != item["sha256"]:
            raise RuntimeError("Tool source changed: " + item["path"])
    common_path = PRODUCT / ".ai-workspace/work/T001/common/candidate-inventory.json"
    common = json.loads(common_path.read_text())
    if common["inventory_sha256"] != COMMON:
        raise RuntimeError("Wrong common candidate inventory")
    for item in common["files"]:
        if sha(PRODUCT / item["path"]) != item["sha256"]:
            raise RuntimeError("Common input changed: " + item["path"])
    core_ref = ref("tool", str(CORE.relative_to(TOOL)))
    save(OPERATOR / "DECISIONS.md", f"""# Root construction selection and operator preparation

Root selected common candidate inventory {COMMON} for bounded construction after source-first appraisal found no common-WHAT blocker. This is a construction selection within Jim's recorded two-tenant build mandate, not Product acceptance. The initial authority/admission gap remains recorded; this preparation retrospectively admits nothing.

The actual owner instruction is in T-001, Owner instruction. Root delegates two independent real CLI Workers to construct their own tenant under the fixed source and grants below. The native product-policy-preflight/1 implementation is selected at {expected_core}; its checked tool candidate is {tool_candidate_sha}. Runtime admission will be the public preflight receipt for each exact Context, grant, executor and result key.

Each actual actor has 600 seconds, no retry, 4MiB combined vendor output and declared unknown monetary cost. Preserve the configured Codex gpt-6-astra/max and Claude fable/high defaults; record actual resolution where exposed. Full host context size, backend hidden retries and unreported usage remain unknown. No full-host-fit judgment is claimed; Context measures actual supplied UTF8. Tool/host qualification remains a separate actual-use obligation.

The Codex convenience wrapper injects danger-full-access/approval-never. Root selected the pinned native executable directly with workspace-write, preserving configuration/auth/model defaults and protected environment. No global configuration changes. Claude uses only the selected a_c MCP server, with no built-in shell or file tools. Codex confinement remains the native sandbox plus cooperative declared territory; it does not prove only-tool isolation.

Preparation may create these records and append the owner URI in how.common. External model dispatch is withheld until Root reviews the concrete plans and exact public admission receipts.
""")
    scope = {"owner": "Jim", "executive": "/root", "product": "urn:stdo:product-definition:stdo-skills", "work": "T001 two independent skill tenant candidates", "common_inventory_sha256": COMMON, "method": "stdo://releases/v3.0.1-rc.1/", "manifest_sha256": MANIFEST, "no_publication": True, "no_global_configuration_changes": True}
    owner = {"mechanism": {"id": "product-policy-preflight/1", "source": core_ref, "implementation_sha256": expected_core}, "result_surface": {"root": str(EVIDENCE), "namespace": "T001", "consumer": "root-executive"}, "scope": scope, "authority_sources": [ref("product", ".ai-workspace/tickets/active/T-001-skills-dogfood.md"), ref("operator", "DECISIONS.md")]}
    save(OPERATOR / "OWNER.json", owner)
    definition_path = PRODUCT / "stdo_skills.json"
    definition = json.loads(definition_path.read_text())
    uri = "./.ai-workspace/work/T001/operator/OWNER.json"
    if uri not in definition["how"]["common"]:
        save(OPERATOR / "definition-before.json", definition)
        definition["how"]["common"].append(uri)
        definition_path.write_text(json.dumps(definition, indent=2) + "\n")
    locator = "/how/common/" + str(definition["how"]["common"].index(uri))
    owner_ref = ref("operator", "OWNER.json")
    definition_ref = ref("product", "stdo_skills.json")
    profile = {"id": PROFILE_ID, "sha256": sha(PROFILE), "source": ref("tool", str(PROFILE.relative_to(TOOL)))}
    inputs = [ref("product", x) for x in ["specification/PRODUCT.md", "specification/INTENT.md", "specification/requirements/README.md", "specification/requirements/SCENARIOS.md", "specification/REFERENCE_FRAME_BASIS.md", "specification/SOURCE_OWNERS.md"]]
    method_inputs = [ref("method", "standards/REFERENCE_FRAME.md", lines=[960, 1000]), ref("method", "standards/ACTIVATION.md", lines=[402, 435]), ref("method", "standards/AXIOMATIC_CALCULUS.md", lines=[985, 1050])]
    environment = {k: os.environ[k] for k in ["PATH", "LANG", "LC_ALL", "TMPDIR"] if k in os.environ}
    outer_environment = dict(environment)
    for key in ["HOME", "home", "CODEX_HOME"]:
        if key in os.environ:
            outer_environment[key] = os.environ[key]
    tool_files = sorted((TOOL / "build_tenants/graphify/code").glob("*.py")) + [ADAPTER, PROFILE]
    all_sources = {"product": {"path": str(PRODUCT), "kind": "workspace", "writable": True, "read_scope": [{"path": p, "kind": k} for p, k in [("stdo_skills.json", "file"), ("specification", "directory"), ("AGENTS.md", "file"), ("CLAUDE.md", "file"), (".ai-workspace/tickets/active/T-001-skills-dogfood.md", "file")]]}, "operator": {"path": str(OPERATOR), "kind": "workspace", "writable": False, "read_scope": [{"path": p, "kind": k} for p, k in [("OWNER.json", "file"), ("DECISIONS.md", "file"), ("codex", "directory"), ("claude", "directory")]]}, "tool": {"path": str(TOOL), "kind": "workspace", "writable": False, "read_scope": [{"path": "build_tenants/graphify", "kind": "directory"}]}, "method": {"path": str(METHOD), "kind": "workspace", "writable": False, "read_scope": [{"path": "standards", "kind": "directory"}, {"path": "manifest.json", "kind": "file"}]}, "host": {"path": "/", "kind": "workspace", "writable": False, "read_scope": [{"path": str(p).lstrip("/"), "kind": "file"} for p in [PYTHON, CODEX, CLAUDE]]}}
    # A read-only filesystem root of '/' would overlap every Writer target.
    # Register executable dependency roots separately instead.
    del all_sources["host"]
    host_refs = {}
    for label, path in [("python", PYTHON), ("codex", CODEX), ("claude", CLAUDE)]:
        alias = "host_" + label
        all_sources[alias] = {"path": str(path.parent), "kind": "workspace", "writable": False, "read_scope": [{"path": path.name, "kind": "file"}]}
        host_refs[label] = {"engine": "workspace-regular-file", "root": alias, "path": path.name, "object": None, "sha256": sha(path), "selector": None}
    base = {"schema": "a_c.fd-support.policy/1", "id": "urn:stdo-skills:T001:operator:1", "product": {"definition_id": "urn:stdo:product-definition:stdo-skills", "definition": definition_ref, "authority_binding": {"definition_locator": locator, "owner_record": owner_ref, **{k: owner[k] for k in ["mechanism", "result_surface", "scope"]}}}, "method_profile": profile, "sources": all_sources, "principals": {}, "grants": {}, "predicates": {}, "operators": {}, "executors": {}, "event_sinks": {}, "independence_policy": None, "evidence_root": str(EVIDENCE), "limits": {"max_message_bytes": 4*1024*1024, "max_files": 2048, "max_bytes": 64*1024*1024, "max_history_records": 50000, "max_wait_ms": 1000}, "authority_sources": owner["authority_sources"]}
    principals = {"executive": {"actor_id": "urn:stdo-skills:T001:root-executive", "role": "Executive", "family": "native-orchestrator", "authorship": "Root coordination; no candidate authorship in this role", "operations": READ + ["context.assemble", "contract.preflight", "dispatch.start", "dispatch.observe", "events.wait", "return.capture", "return.check"], "role_binding": ref("operator", "DECISIONS.md"), "role_transition": None}}
    grants = {}; executors = {}; tasks = {}; contracts = {}; territories = {}
    for tenant in ["codex", "claude"]:
        host_text = ("# Codex host mechanics\n\nVerified local version: codex-cli 0.164.0. Configured gpt-6-astra/max remains inherited; actual resolution is recorded only from the run.\n\nOfficial documentation inspected 2026-10-25: [Build skills](https://learn.chatgpt.com/docs/build-skills). A skill folder contains SKILL.md with name and description; optional scripts, references and agents/openai.yaml support it. Codex normally discovers repository .agents/skills directories from the current directory through the repository root. Explicit CLI invocation uses $skill-name or the skills selector. Descriptions support automatic selection and should lead with the relevant task. Only selected skill bodies are loaded. Duplicate names are not merged. Updates are normally detected; restart if discovery is stale. Relative resources must survive installation. User-level and plugin distribution are distinct installation choices. This task selects a repository-local install first. None of these documented mechanisms guarantees model selection or task success; qualify the actual host.\n\nTenant algorithm and prompt design remain your own; this file is sourced host input, not a donor design.\n" if tenant == "codex" else "# Claude host mechanics\n\nVerified local version: Claude Code 2.1.306. Configured fable/high remains inherited; actual resolution is recorded only from the run.\n\nOfficial documentation inspected 2026-10-25: [Extend Claude with skills](https://code.claude.com/docs/en/skills). Repository skills live in .claude/skills/<name>/SKILL.md. Project skill search includes parents up to the worktree root. Description supplies automatic selection; /skill-name explicitly invokes the entry. Default invocation permits both user and model. disable-model-invocation:true removes automatic selection and is not selected here. Optional frontmatter and supporting files can specialize mechanics. Plugin skills use a namespace; names can collide across project/personal/plugin scopes, so verify the actual selected path. Some newer documented behavior requires versions after 2.1.306; do not assume it applies. This task selects a repository-local install first and requires actual discovery evidence.\n\nTenant algorithm and prompt design remain your own; this file is sourced host input, not a donor design. Your construction host exposes only configured a_c MCP tools. Executable tests unavailable in this activation remain explicitly unperformed for Root's later proof.\n")
        save(OPERATOR / tenant / "HOST.md", host_text)
        save(OPERATOR / tenant / "TASK.md", task(tenant))
        task_ref = ref("operator", tenant + "/TASK.md")
        grant_id = "urn:stdo-skills:T001:" + tenant + ":construction:1"
        actor_id = "urn:stdo-skills:T001:" + tenant + ":worker:1"
        principals[tenant] = {"actor_id": actor_id, "role": "Worker", "family": "openai-codex" if tenant == "codex" else "anthropic-claude", "authorship": tenant + " tenant candidate author", "operations": READ + ["work.write"], "role_binding": task_ref, "role_transition": None}
        territory = [{"root": "product", "path": p, "kind": "directory"} for p in ["build_tenants/" + tenant, ".ai-workspace/work/T001/" + tenant + "/actor"]]
        territories[tenant] = territory
        grant = {"id": grant_id, "authority_sources": owner["authority_sources"] + [task_ref], "outcome": {"id": "urn:stdo-skills:T001:" + tenant + ":candidate", "source": task_ref}, "principals": ["executive", tenant], "targets": [tenant], "operations": ["contract.preflight", "dispatch.start", "work.write"], "tools": ["a_c.public-native301"] + (["host.read-compute"] if tenant == "codex" else []), "executors": [tenant + "-cli"], "territory": territory, "preconditions": inputs, "admission": {"mechanism_id": "product-policy-preflight/1", "mechanism_source": core_ref, "authority_source": owner_ref, "required_predicates": [], "allowed_override_sources": []}, "notification_sink": "root-events"}
        grants[grant_id] = grant
        worker_policy = json.loads(json.dumps(base)); worker_policy["id"] += ":" + tenant
        worker_policy["sources"]["operator"]["read_scope"] = [{"path": p, "kind": k} for p, k in [("OWNER.json", "file"), ("DECISIONS.md", "file"), (tenant, "directory")]]
        worker_policy["sources"]["product"]["read_scope"] += [{"path": x["path"], "kind": x["kind"]} for x in territory]
        worker_policy["principals"] = {tenant: principals[tenant]}
        worker_grant = json.loads(json.dumps(grant)); worker_grant.update({"principals": [tenant], "targets": [tenant], "operations": ["work.write"], "executors": [], "notification_sink": None})
        worker_policy["grants"] = {grant_id: worker_grant}
        worker_policy_path = OPERATOR / tenant / "worker-policy.json"
        save(worker_policy_path, worker_policy)
        cli_args = ["-B", str(CLI), "--policy", str(worker_policy_path), "--policy-sha256", sha(worker_policy_path), "--principal", tenant, "mcp"]
        mcp = {"mcpServers": {"stdo_ac": {"command": str(PYTHON), "args": cli_args}}}
        mcp_path = OPERATOR / tenant / "mcp.json"; save(mcp_path, mcp)
        startup = f"You are the separately admitted {tenant} Worker for STDO Skills. The stdin Context is your exact activation, not a request to redesign the method. Use the configured stdo_ac MCP tools to source.read TASK at {json.dumps(task_ref, separators=(',',':'))}, then its required sources. Tool calls require the full JSON envelope with schema='a_c.fd-support.request/1', a unique id, the exact operation name, and an arguments object; use tools.describe for schemas. Public CLI alternative is {PYTHON} -B {CLI} --policy {worker_policy_path} --policy-sha256 {sha(worker_policy_path)} --principal {tenant} call --request <own-actor-evidence-request.json>. Write deliverables only through work.write under grant {grant_id}. Do not edit operator configuration, shared WHAT or peer tenant. No external model calls or Git. Emit original closed-return JSON as final output as TASK specifies. Do not summarize or repair a return after submission. Your time budget is 600 seconds; prioritize coherent usable artifacts and truthful partial results."
        save(OPERATOR / tenant / "STARTUP.txt", startup + "\n")
        if tenant == "codex":
            argv = [str(CODEX), "exec", "--json", "--color", "never", "--sandbox", "workspace-write", "--cd", str(PRODUCT), "-c", 'mcp_servers.stdo_ac.command=' + json.dumps(str(PYTHON)), "-c", 'mcp_servers.stdo_ac.args=' + json.dumps(cli_args), startup]
            backend_path = CODEX; decoder = "codex-final-jsonl/1"
        else:
            argv = [str(CLAUDE), "--print", "--output-format", "stream-json", "--verbose", "--permission-mode", "acceptEdits", "--permission-prompts", "none", "--tools", "", "--strict-mcp-config", "--mcp-config", str(mcp_path), "--allowedTools", "mcp__stdo_ac__*", "--append-system-prompt", startup]
            backend_path = CLAUDE; decoder = "claude-result-jsonl/1"
        dependencies = [pin(x) for x in tool_files] + [pin(worker_policy_path), pin(mcp_path), pin(OPERATOR / tenant / "STARTUP.txt")]
        plan = {"schema": "a_c.fd-support.actor-cli-plan/1", "id": "urn:stdo-skills:T001:" + tenant + ":actor-plan:1", "backend": tenant, "executable": pin(backend_path), "argv": argv, "dependencies": dependencies, "cwd": str(PRODUCT), "environment": environment, "settings": {"selected_host": "codex-cli 0.164.0" if tenant == "codex" else "Claude Code 2.1.306", "model_default": "gpt-6-astra" if tenant == "codex" else "fable", "effort_default": "max" if tenant == "codex" else "high", "model_override": False, "resolved_backend": "unobserved until actual run", "cost": "unknown", "host_context_bytes": "unknown", "retry_policy": "no actor retry", "host_scope": "workspace-write sandbox and cooperative scoped writes" if tenant == "codex" else "only explicitly configured a_c MCP tools; host context/settings remain inherited"}, "decoder": decoder, "evidence_directory": str(OPERATOR / tenant / "actor-cli-output"), "limits": {"max_input_bytes": 4*1024*1024, "max_output_bytes": 4*1024*1024, "timeout_ms": 600000, "termination_grace_ms": 3000}}
        plan_path = OPERATOR / tenant / "actor-plan.json"; save(plan_path, plan)
        dependency_refs = [ref("tool", str(x.relative_to(TOOL))) for x in tool_files] + [ref("operator", tenant + "/" + name) for name in ["worker-policy.json", "mcp.json", "STARTUP.txt", "actor-plan.json"]] + [host_refs[tenant], host_refs["python"]]
        executors[tenant + "-cli"] = {"id": tenant + "-cli", "executable": pin(PYTHON), "argv": [str(PYTHON), "-B", str(ADAPTER), "--plan", str(plan_path), "--plan-sha256", sha(plan_path)], "dependencies": dependency_refs, "cwd": str(PRODUCT), "environment": outer_environment, "actor_id": actor_id, "settings": {"timeout_ms": 610000, "termination_grace_ms": 5000, "max_output_bytes": 4*1024*1024, "model_default": plan["settings"]["model_default"], "effort_default": plan["settings"]["effort_default"]}, "tools": grant["tools"], "effect_scope": {"declared_territory": territory, "external_effects": "unknown until observed; no general OS confinement claim", "no_remote_or_git_grant": True}, "stdin_mode": "context-utf8", "stdout_decoder": {"format": "json", "pointer": None, "decode_json_string": False}, "observers": [{"kind": "process-end"}]}
        contract = {"schema": "a_c.fd-support.return-contract/1", "id": "urn:stdo-skills:T001:" + tenant + ":return:1", "authority_source": task_ref, "carrier": "a_c.fd-support.closed-return/1", "output_slot": "final_stdout_object", "required_evaluations": [{"id": "requirements-realization", "predicate": inputs[2]}, {"id": "tenant-artifact-integrity", "predicate": task_ref}], "role": "Worker", "proof": {"transition_sources": [], "predicate_ids": []}}
        save(OPERATOR / tenant / "RETURN-CONTRACT.json", contract)
        tasks[tenant] = task_ref; contracts[tenant] = ref("operator", tenant + "/RETURN-CONTRACT.json")
    executive = json.loads(json.dumps(base)); executive["principals"] = principals; executive["grants"] = grants; executive["executors"] = executors
    executive["event_sinks"] = {"root-events": {"kind": "durable-file-events", "directory": "notifications", "consumer": "root-executive", "authority_source": owner_ref, "retention": "indefinite"}}
    for territory in territories.values():
        executive["sources"]["product"]["read_scope"] += [{"path": x["path"], "kind": x["kind"]} for x in territory]
    policy_path = OPERATOR / "executive-policy.json"; save(policy_path, executive)
    save(OPERATOR / "PREPARED.json", {"policy": str(policy_path), "policy_sha256": sha(policy_path), "tool_candidate_sha256": tool_candidate_sha, "core_sha256": expected_core, "definition_sha256": sha(definition_path), "no_model_dispatch": True, "plans": {t: {"path": str(OPERATOR / t / "actor-plan.json"), "sha256": sha(OPERATOR / t / "actor-plan.json")} for t in tasks}})
    receipts = {}
    for tenant in ["codex", "claude"]:
        for operation in ["context.assemble", "contract.preflight", "work.write"]:
            call(policy_path, "executive", tenant + "-describe-" + operation.replace(".", "-"), "tools.describe", {"operation": operation})
        observed = call(policy_path, "executive", tenant + "-observe", "workspace.observe", {"scope": [{"root": "product", "path": "stdo_skills.json", "kind": "file"}] + [{"root": x["root"], "path": x["path"], "kind": "file"} for x in inputs]})
        observation = observed["result"]["artifact"]
        subject = {"id": "urn:stdo-skills:T001:" + tenant + ":candidate", "sha256": COMMON}
        actor = principals[tenant]
        packet = {"activation": {"id": "urn:stdo-skills:T001:" + tenant + ":construction:1", "revision": "1", "configuration": inputs[4]}, "frame": {"id": "skills.worker/1", "revision": "1", "declaration": inputs[4], "evaluation": tasks[tenant], "result_algebra": ref("method", "standards/ACTIVATION.md", lines=[968, 1055])}, "subject_basis": {"subject": subject, "method_profile": {k: profile[k] for k in ["id", "sha256"]}, "product": {"id": executive["product"]["definition_id"], "definition": definition_ref}, "observations": [observation], "dependencies": inputs, "time_basis": "exact pre-dispatch source observation; recheck at launch"}, "attention": {"material_relations": inputs, "invariants": inputs + method_inputs, "semantic_sources": inputs + method_inputs, "exclusions": ["peer tenant design/code", "global config", "Git and remote effects"], "prohibited_assumptions": ["tool success is semantic acceptance", "same bytes erase retained obligations", "unperformed qualification passed"]}, "actor_authority": {"actor_id": actor["actor_id"], "role": "Worker", "capability": ref("operator", tenant + "/HOST.md"), "semantic": inputs[0], "evaluation": tasks[tenant], "operation": tasks[tenant], "decision": None, "acceptance": None, "publication": None, "territory": territories[tenant], "tools": grants["urn:stdo-skills:T001:"+tenant+":construction:1"]["tools"]}, "evidence_relations": {"admissible_evidence": inputs + [tasks[tenant], owner_ref], "acquisition": inputs + method_inputs, "dependencies": [], "conjunction": None, "translation": None, "consumer": "root-executive", "return_contract": contracts[tenant]}, "stop_change": {"invalidators": ["material source/tool/authority drift", "unsupported operation", "uncertain prior effect"], "stop_conditions": ["600 seconds", "required authority unavailable"], "residuals": ["actual host scenario qualification and independent review remain separate"], "re_entry": ["return exact missing premise and partial evidence to Root"], "reconfiguration": []}, "profile_additions": {"worker": {"operation_grant_id": "urn:stdo-skills:T001:"+tenant+":construction:1", "mutation_subject": subject, "territory": territories[tenant]}}}
        assembled = call(policy_path, "executive", tenant + "-assemble", "context.assemble", {"packet": packet, "models": [], "sources": inputs + method_inputs + [tasks[tenant], contracts[tenant], ref("operator", tenant + "/STARTUP.txt"), ref("operator", tenant + "/HOST.md")], "late_acquisition": [], "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})
        context = assembled["result"]["artifact"]
        preflight = call(policy_path, "executive", tenant + "-preflight", "contract.preflight", {"context": context, "grant_id": "urn:stdo-skills:T001:"+tenant+":construction:1", "executor_id": tenant + "-cli", "result_key": "T001/" + tenant + "/construction-1", "observations": [observation]})
        receipts[tenant] = {"context": context, "observation": observation, "preflight": preflight}
    save(OPERATOR / "PREFLIGHTS.json", receipts)
    return {"prepared": str(OPERATOR / "PREPARED.json"), "preflights": str(OPERATOR / "PREFLIGHTS.json"), "external_model_dispatches": 0}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--core-sha256", required=True)
    parser.add_argument("--tool-candidate", required=True, type=Path)
    parser.add_argument("--tool-candidate-sha256", required=True)
    arguments = parser.parse_args()
    print(json.dumps(prepare(arguments.core_sha256, arguments.tool_candidate, arguments.tool_candidate_sha256), indent=2))
