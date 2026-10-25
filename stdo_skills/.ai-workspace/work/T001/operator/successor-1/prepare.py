"""Create-only successor preparation. Public preflight only; never dispatch.

This is operator configuration, not a replacement tool or admission interpreter.
Original plans, failed attempts and retained evidence remain in their old paths.
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
OLD = HERE.parent
REPO = HERE.parents[5]
PRODUCT = REPO / "stdo_skills"
TOOL = REPO / "a_c"
METHOD = Path("/Users/jim/Library/Application Support/STDO/releases/v3.0.1-rc.1")
EVIDENCE = OLD / "protected-evidence"
CORE = TOOL / "build_tenants/graphify/code/ac_support_core.py"
CLI = TOOL / "build_tenants/graphify/code/ac_support.py"
ADAPTER = TOOL / "build_tenants/graphify/examples/fd-support/actor_cli.py"
PROFILE = TOOL / "build_tenants/graphify/design/fd-method-stdo-3.0.1.json"
PYTHON = Path("/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python").resolve()
CODEX = Path("/opt/homebrew/lib/node_modules/@openai/codex/node_modules/@openai/codex-darwin-arm64/vendor/aarch64-apple-darwin/bin/codex").resolve()
CLAUDE = Path("/Users/jim/.local/share/claude/versions/2.1.306").resolve()
COMMON = "a6d348b8385ea453ce29362fb9d74559304b1b91743b3c9ea31a83a9f02b5f2d"
MANIFEST = "60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8"
AUTH_FREEZE_SHA = "9f30837e4ffad6c1be7dcad1067ff59856ef6c1b0f251dd6ae5eac4ccf50004b"
CORE_SHA = "bf72a28444e0497cd564066e41c7e5943810d5a2e0be5488c92fa5add5a67209"
READ = ["tools.describe", "workspace.observe", "source.read", "records.find", "records.read", "graph.project", "relations.query", "evidence.read", "work.project"]
ATTEMPTS = {"codex": "4b0aaf3769ae2bf8b2ce26828efed9394755c7433acaf3ebfad584965a5e9368", "claude": "8e519a7970d602e7d96f0732104e5c5801567739124641c3781aad3b75d9d1ef"}
REFUSAL = "2cc76eb6958566e5c357d26eac85e4a543e73ac44ce095a0014ffc3f10aefc4d"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    raw = value.encode() if isinstance(value, str) else (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != raw:
            raise RuntimeError("Preserve existing record; select successor: " + str(path))
        return
    with path.open("xb") as stream:
        stream.write(raw)


def ref(root, path, lines=None):
    roots = {"product": PRODUCT, "tool": TOOL, "method": METHOD, "operator": OLD, "successor": HERE}
    return {"engine": "workspace-regular-file", "root": root, "path": path, "object": None, "sha256": sha(roots[root] / path), "selector": None if lines is None else {"lines": lines}}


def pin(path):
    return {"path": str(path), "sha256": sha(path)}


def artifact(value):
    return {"id": "sha256:" + value, "sha256": value}


def load_artifact(value):
    path = EVIDENCE / "objects" / (value + ".json")
    data = json.loads(path.read_text())
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    if hashlib.sha256(canonical).hexdigest() != value:
        raise RuntimeError("Historical artifact identity mismatch: " + value)
    return data


def call(policy, principal, identity, operation, arguments):
    request = {"schema": "a_c.fd-support.request/1", "id": identity, "operation": operation, "arguments": arguments}
    reqpath = HERE / "requests" / (identity + ".json")
    save(reqpath, request)
    argv = [str(PYTHON), "-B", str(CLI), "--policy", str(policy), "--policy-sha256", sha(policy), "--principal", principal, "call", "--request", str(reqpath)]
    out = HERE / "responses" / identity
    if out.with_suffix(".stdout.json").exists():
        raise RuntimeError("Refuse repeated preparation invocation: " + identity)
    # Inherit the current environment. Never serialize credential values.
    done = subprocess.run(argv, cwd=PRODUCT, capture_output=True, timeout=60)
    save(out.with_suffix(".invocation.json"), {"argv": argv, "returncode": done.returncode})
    save(out.with_suffix(".stdout.json"), done.stdout.decode())
    save(out.with_suffix(".stderr.txt"), done.stderr.decode())
    result = json.loads(done.stdout)
    if done.returncode or result.get("status") != "ok":
        raise RuntimeError("Public operation refused; inspect retained response: " + identity)
    return result


def task(tenant):
    reuse = "Acquire PRIOR-PROPOSAL.md: exact text from your earlier refused write, not an adopted design or successful effect. Reuse or improve it, updating obsolete grant/tool assumptions before recording your actual design." if tenant == "codex" else "Your previous attempt failed authentication before model execution; it produced no design. Develop your own tenant without reading the other tenant."
    return f"""# {tenant.title()} tenant construction: successor 1

Build a useful, reviewable {tenant} skill package from the shared STDO Skills WHAT. Produce a concise design first, then working skill files, packaged references, installation/update/removal instructions, focused checks and an exact candidate inventory. Skill names, number and decomposition are yours. This is candidate construction; Product acceptance and actual-host Q01-Q12 qualification remain later obligations.

Use SOURCE-ROUTES.json to acquire deciding Product/requirements/scenarios, frame and source-owner material through public source.read. Those unchanged common hashes remain selected at inventory {COMMON}. The static installed method is stdo://releases/v3.0.1-rc.1/, manifest {MANIFEST}; no channel adoption. Historical acquisitions in HISTORY.json retain their original provenance; they do not become fresh Worker observations. Read only needed method sections. {reuse}

Your grant allows artifact construction only under build_tenants/{tenant}/ and .ai-workspace/work/T001/{tenant}/actor/successor-1/. Predictable design/, skills/ and tests/ roots are provisioned. Bash may mkdir further ordinary directories inside those two territories; reject symlinks or path escape. Host read/compute and read-only focused validation are allowed on permitted inputs and your candidate. Artifact file contents MUST use public a_c work.write, including design, skills, tests, inventories and retained test reports. No direct file-content writes, Git, remote/model calls, global config changes, peer material or shared-source edits. Host permission grants are cooperative scope, not OS confinement.

The public CLI is the normal transport; MCP is not required. Send a full envelope through `call --request -` on stdin, so no request file needs to be written. tools.describe gives exact schemas; source.read uses arguments {{source: SourceRef, encoding: "utf8"}}. work.write uses your grant, exact target preimage (sha256 null only for absent file), mode replace, record {{text, provenance: this TASK SourceRef}}, interpretation null and your own current workspace.observe. Before each write ensure its parent exists and observe the target's containing directory. Preserve the returned postimage and OperationEvidence. Read acquired tool responses; do not reload every schema or repeat verified acquisition for ceremony. After an uncertain effect, reconcile before retrying.

Prior attempts are closed and reconciled in HISTORY.json. This revised contract permits the missing mkdir/CLI capability and selects the repaired authentication transport; it is a new activation, not a reissued old dispatch. There are no automatic retries. No old success or qualification is invented. On any new genuine blocker, retain partial candidate/evidence and return the precise cause.

Keep instructions practical and progressive: normal task entry, automatic and explicit invocation, exact method/tool binding, proportional direct work, bounded worker/reviewer handoff where needed, continuation/recovery and scoped release/install. Link deciding method sources; do not reproduce the method. Native results.conjoin remains unsupported. Preserve existing authority without repeated permission ceremony. All SK-01 to SK-12 and Q01 to Q12 remain visible; construction does not silently waive them.

Perform the two assessments defined in PREDICATES.md using exact candidate and actual focused proof. Mechanical availability is separate from author semantic assessment; neither proves host compliance or independent acceptance. STDO ACTIVATION transition evidence requires the cheapest focused proof capable of falsifying the active relation, with expensive whole-candidate qualification at a declared boundary. A package verifier alone cannot establish instruction fitness. Do not spend the construction bound repeating full host trials.

Time bound 600 seconds; unknown total cost. Prioritize a coherent usable package. Run focused read-only package checks and manually reason through the named falsifiers; record what actually ran and what remains. Return one a_c.fd-support.closed-return/1 JSON object, without fences. Copy the actual Context frame, activation identity, subject, original method/observation basis, actor and consumer. Required evaluation IDs and exact predicates are in RETURN-CONTRACT.json. Use evidence refs for your actual assessment and tool observations; unperformed evaluation belongs in not_performed. candidate_ready means exact candidate and transition evidence exist, not fitness or acceptance. Keep independent review, automatic/explicit host behavior and unperformed Q cases open. Do not activate a next stage.
"""


PREDICATES = """# Bounded candidate assessments

These are Worker F_P assessment contracts, not registered deterministic checker predicates. Each assessment names exact candidate bytes, source clauses, actual observations, counterexamples and residuals. File existence/acquisition alone proves neither predicate. Operation output availability remains the tool's separate mechanical predicate.

## tenant-instruction-fitness

Predicate: the candidate contains usable host-specific instructions and resources which, on the selected common WHAT and supported tool contracts, specify a coherent path for all SK-01 to SK-12 without an identified contradiction or material missing action. Assess the actual skill bodies and linked resources, not its design's claims. Explain the required paths and cite exact locations. Exercise three source-derived discriminators by reasoning over the candidate: Q04 sufficient one-file authorization must avoid mandatory coordination/review; Q07 equal candidate bytes with a retained counterexample must change continuation; Q06/Q08 unsupported or uncertain effect must retain the failure and prevent dependent success/repeated effect. Identify actual tool invocations, discovery and install paths. A generic method summary or non-executable invented command falsifies the affected path. Additional source-derived counterexamples remain admissible.

Report satisfied only for this bounded author assessment if every required instruction path is present and no material counterexample remains after the performed assessment. Report falsified with the counterexample, indeterminate if performed evidence cannot decide, invalid_basis for a materially unusable basis, out_of_frame for a missing assessment capability. If not performed there is no assessment result. Evidence must include an actual assessment record tied to candidate inventory, inspected source references and any executed focused checks. This does not claim automatic discovery, runtime execution, independent review or actual-host Q01-Q12 qualification.

## tenant-package-integrity

Predicate: the exact package is present, internally resolvable and deployable by its stated scoped recipe, with an inventory matching its ordinary regular files and no dependency on omitted tenant-local resources or another tenant. Check SKILL.md metadata and resource paths; run a focused read-only verifier or equivalent finite checks against actual files. Check update/removal addresses the selected owned installation and preserves unrelated configuration. Verify that the design was retained before dependent implementation and successful work.write evidence binds candidate artifacts. Do not treat the presence of a verifier or test file as its execution.

Use satisfied only for the observed finite package checks on that exact inventory. False observed metadata/path/inventory or deployment-contract check is falsified; insufficient performed evidence is indeterminate; no executed assessment is not_performed. Distinguish finite package facts from host installation/discovery behavior, which requires later isolated host proof. Candidate availability is independently candidate_ready only when an exact candidate and transition evidence exist.
"""


def prepare():
    auth_path = PRODUCT / ".ai-workspace/work/T001/tooling/auth-repair-prep/source-freeze.json"
    predecessor = PRODUCT / ".ai-workspace/work/T001/tooling/repair-1/RETURN.json"
    if sha(auth_path) != AUTH_FREEZE_SHA or sha(CORE) != CORE_SHA:
        raise RuntimeError("Selected auth repair changed")
    rows = {x["path"]: {"path": x["path"], "sha256": x["sha256"]} for x in json.loads(predecessor.read_text())["source"]}
    rows.update({x["path"]: {"path": x["path"], "sha256": x["sha256"]} for x in json.loads(auth_path.read_text())["source"]})
    for row in rows.values():
        if sha(REPO / row["path"]) != row["sha256"]:
            raise RuntimeError("Tool source changed: " + row["path"])
    save(HERE / "TOOL-BASIS.json", {"scope": "Union of previous native binding and selected auth repair; source custody only", "predecessor": pin(predecessor), "auth_repair": pin(auth_path), "source": sorted(rows.values(), key=lambda x: x["path"])})
    common = PRODUCT / ".ai-workspace/work/T001/common/candidate-inventory.json"
    if json.loads(common.read_text())["inventory_sha256"] != COMMON:
        raise RuntimeError("Common inventory changed")
    for row in json.loads(common.read_text())["files"]:
        if sha(PRODUCT / row["path"]) != row["sha256"]:
            raise RuntimeError("Common source changed: " + row["path"])
    if sha(METHOD / "manifest.json") != MANIFEST:
        raise RuntimeError("Installed method manifest changed")

    historical = load_artifact(REFUSAL)
    save(HERE / "codex/PRIOR-PROPOSAL.md", historical["payload"]["request"]["arguments"]["record"]["text"])
    original_return = load_artifact("10b3f64a6bec2aa113d36173e444ff5cf913b27b414645a770e5fa2ba56a292b")["payload"]["original"]
    return_check = load_artifact("ebd2d91419d04c12701dcb3f3963512ad7e6cd074b50bfd173b30b380e69a25c")["payload"]["response_without_evidence"]["result"]["value"]
    observed_paths = []
    for tenant in ["codex", "claude"]:
        paths = [PRODUCT / "build_tenants" / tenant / x for x in ["design", "skills", "tests"]] + [PRODUCT / ".ai-workspace/work/T001" / tenant / "actor/successor-1"]
        for path in paths:
            existed = path.exists()
            for parent in [path] + list(path.parents):
                if parent == PRODUCT.parent:
                    break
                if parent.is_symlink():
                    raise RuntimeError("Symlink in provisioned territory")
            path.mkdir(parents=True, exist_ok=True)
            observed_paths.append({"path": str(path.relative_to(PRODUCT)), "existed": existed, "is_directory": path.is_dir(), "effect": "mkdir only; no candidate content"})
        process_path = OLD / tenant / "actor-cli-output/process.json"
        process = json.loads(process_path.read_text())
        pid = process["pid"]
        ps = subprocess.run(["ps", "-p", str(pid), "-o", "pid=,comm="], capture_output=True, text=True)
        if ps.returncode == 0:
            raise RuntimeError("Prior direct actor PID still exists; reconcile")
        observations = []
        for p in (EVIDENCE / "objects").glob("*.json"):
            data = json.loads(p.read_text())
            payload = data.get("payload", {})
            if data["kind"] != "operation" or payload.get("request", {}).get("operation") != "dispatch.observe":
                continue
            if payload["request"]["arguments"].get("attempt", {}).get("sha256") == ATTEMPTS[tenant]:
                value = payload["response_without_evidence"]["result"]["value"]
                observations.append({"evidence": artifact(p.stem), "process_end": value["process_end"], "effect": value["effect"], "output": value["output"]})
        history = {"prior_attempt": artifact(ATTEMPTS[tenant]), "original_process": pin(process_path), "direct_parent": process, "current_pid_observation": {"argv": ["ps", "-p", str(pid), "-o", "pid=,comm="], "returncode": ps.returncode, "stdout": ps.stdout, "meaning": "Recorded direct PID absent; no universal descendant/effect absence claim"}, "retained_observations": observations, "decision": "New contract after known parent closure and observed absence of candidate writes. No replay of old dispatch or automatic retry. Keep external/descendant effects unknown where not observed."}
        if tenant == "codex":
            history.update({"work_result": original_return["work_result"], "return_check": {"evidence": artifact("ebd2d91419d04c12701dcb3f3963512ad7e6cd074b50bfd173b30b380e69a25c"), "consumable": return_check["consumable"], "gaps": return_check["gaps"]}, "proposal_origin": {"evidence": artifact(REFUSAL), "pointer": "/payload/request/arguments/record/text", "recovered_sha256": sha(HERE / "codex/PRIOR-PROPOSAL.md"), "standing": "unwritten proposal only; old grant/prose is historical and must be updated"}})
            acquisitions = []
            roots = {"product": PRODUCT, "operator": OLD, "method": METHOD, "tool": TOOL}
            for p in (EVIDENCE / "objects").glob("*.json"):
                data = json.loads(p.read_text()); payload = data.get("payload", {})
                if data["kind"] == "operation" and data["provenance"]["requester_principal"] == "codex" and payload.get("request", {}).get("operation") == "source.read" and payload["response_without_evidence"]["status"] == "ok":
                    src = payload["request"]["arguments"]["source"]
                    path = roots[src["root"]] / src["path"]
                    acquisitions.append({"evidence": artifact(p.stem), "source": src, "same_bytes_at_preparation": path.exists() and sha(path) == src["sha256"], "standing": "historical acquisition; retain provenance, no fresh observation or fitness proof"})
            history["acquisitions"] = acquisitions
        else:
            history["failure"] = {"observed": "Not logged in; Please run /login", "reported_input_tokens": 0, "reported_output_tokens": 0, "reported_cost_usd": 0, "standing": "No model-produced candidate or assessment. Selected environment repair restores only credential routing; future authentication success unobserved."}
        save(HERE / tenant / "HISTORY.json", history)
    save(HERE / "DIRECTORY-PROVISION.json", observed_paths)

    save(HERE / "DECISIONS.md", f"""# Root successor construction selection

Root delegates a new pair of exact bounded construction contracts after both original parents closed. The user mandate remains the same two independent tenants. Common inventory {COMMON}, static STDO3.0.1 manifest {MANIFEST}, and auth-repaired native tool freeze {AUTH_FREEZE_SHA} are selected. Earlier admission gaps and incomplete attempts remain historical; no acceptance or retrospective admission is asserted.

The previous contracts lacked a usable directory/host transport grant. This revision provisions empty design/skills/tests roots, permits bounded mkdir within each tenant and its own evidence territory, and uses public CLI through Bash. Artifact contents still pass work.write. Claude's selected credential name passes privately through trusted executor and helper settings; values are not retained. Codex keeps the native workspace-write host; Claude uses Bash/Read with noninteractive allowedTools. These are cooperative scopes, not OS confinement.

Each actor receives 600 seconds, 4MiB vendor output, no automatic retries and unknown cost. Configured model/effort defaults remain unchanged. Exact retained acquisition can be reused on unchanged basis; authority, Product definition, tool pins and grant changes require current binding. Required source routes remain available by late acquisition. Full host context and backend hidden behavior remain unknown.

The candidate boundary requires useful artifacts, focused proof and two bounded author assessments. ACTIVATION transition evidence uses the cheapest proof capable of falsifying the active relation; whole-candidate host qualification is a later boundary. Presence, deterministic tool output availability, author fitness assessment, independent review and Product acceptance have separate claims. Q01-Q12 remain mandatory qualification obligations. Root will review these concrete plans and preflights before dispatch.
""")
    owner = {"mechanism": {"id": "product-policy-preflight/1", "source": ref("tool", str(CORE.relative_to(TOOL))), "implementation_sha256": CORE_SHA}, "result_surface": {"root": str(EVIDENCE), "namespace": "T001", "consumer": "root-executive"}, "scope": {"owner": "Jim", "executive": "/root", "product": "urn:stdo:product-definition:stdo-skills", "work": "T001 successor construction of two independent skill tenants", "common_inventory_sha256": COMMON, "method": "stdo://releases/v3.0.1-rc.1/", "manifest_sha256": MANIFEST, "no_publication": True, "no_global_configuration_changes": True}, "authority_sources": [ref("product", ".ai-workspace/tickets/active/T-001-skills-dogfood.md"), ref("successor", "DECISIONS.md")]}
    save(HERE / "OWNER.json", owner)
    definition_path = PRODUCT / "stdo_skills.json"
    definition = json.loads(definition_path.read_text()); before = copy.deepcopy(definition)
    uri = "./.ai-workspace/work/T001/operator/successor-1/OWNER.json"
    if uri in definition["how"]["common"]:
        raise RuntimeError("Successor already prepared; do not repeat effects")
    save(HERE / "definition-before.json", before)
    definition["how"]["common"].append(uri)
    definition_path.write_text(json.dumps(definition, indent=2) + "\n")
    check = copy.deepcopy(definition); check["how"]["common"].remove(uri)
    save(HERE / "definition-change-check.json", {"only_owner_uri_appended": check == before, "definition_sha256": sha(definition_path)})
    locator = "/how/common/" + str(definition["how"]["common"].index(uri))
    owner_ref = ref("successor", "OWNER.json"); definition_ref = ref("product", "stdo_skills.json")
    profile = {"id": "urn:a-c:fd-support:method:stdo-3.0.1-rc.1:executive:1", "sha256": sha(PROFILE), "source": ref("tool", str(PROFILE.relative_to(TOOL)))}
    inputs = [ref("product", p) for p in ["specification/PRODUCT.md", "specification/INTENT.md", "specification/requirements/README.md", "specification/requirements/SCENARIOS.md", "specification/REFERENCE_FRAME_BASIS.md", "specification/SOURCE_OWNERS.md"]]
    proof_source = ref("method", "standards/ACTIVATION.md", [1750, 1768])
    result_source = ref("method", "standards/ACTIVATION.md", [1004, 1055])
    common_scopes = [{"path": p, "kind": k} for p, k in [("stdo_skills.json", "file"), ("specification", "directory"), ("AGENTS.md", "file"), ("CLAUDE.md", "file"), (".ai-workspace/tickets/active/T-001-skills-dogfood.md", "file")]]
    sources = {"product": {"path": str(PRODUCT), "kind": "workspace", "writable": True, "read_scope": common_scopes}, "operator": {"path": str(OLD), "kind": "workspace", "writable": False, "read_scope": [{"path": p, "kind": k} for p, k in [("OWNER.json", "file"), ("DECISIONS.md", "file"), ("codex", "directory"), ("claude", "directory")]]}, "successor": {"path": str(HERE), "kind": "workspace", "writable": False, "read_scope": [{"path": p, "kind": k} for p, k in [("OWNER.json", "file"), ("DECISIONS.md", "file"), ("TOOL-BASIS.json", "file"), ("codex", "directory"), ("claude", "directory")]]}, "tool": {"path": str(TOOL), "kind": "workspace", "writable": False, "read_scope": [{"path": "build_tenants/graphify", "kind": "directory"}]}, "method": {"path": str(METHOD), "kind": "workspace", "writable": False, "read_scope": [{"path": "standards", "kind": "directory"}, {"path": "manifest.json", "kind": "file"}]}}
    host_refs = {}
    for name, path in [("python", PYTHON), ("codex", CODEX), ("claude", CLAUDE)]:
        alias = "host_" + name
        sources[alias] = {"path": str(path.parent), "kind": "workspace", "writable": False, "read_scope": [{"path": path.name, "kind": "file"}]}
        host_refs[name] = {"engine": "workspace-regular-file", "root": alias, "path": path.name, "object": None, "sha256": sha(path), "selector": None}
    base = {"schema": "a_c.fd-support.policy/1", "id": "urn:stdo-skills:T001:operator:successor-1", "product": {"definition_id": definition["product"]["definition_id"], "definition": definition_ref, "authority_binding": {"definition_locator": locator, "owner_record": owner_ref, **{k: owner[k] for k in ["mechanism", "result_surface", "scope"]}}}, "method_profile": profile, "sources": sources, "principals": {}, "grants": {}, "predicates": {}, "operators": {}, "executors": {}, "event_sinks": {}, "independence_policy": None, "evidence_root": str(EVIDENCE), "limits": {"max_message_bytes": 4*1024*1024, "max_files": 2048, "max_bytes": 64*1024*1024, "max_history_records": 50000, "max_wait_ms": 1000}, "authority_sources": owner["authority_sources"]}
    principals = {"executive": {"actor_id": "urn:stdo-skills:T001:root-executive", "role": "Executive", "family": "native-orchestrator", "authorship": "Root coordination; no candidate authorship in this role", "operations": READ + ["context.assemble", "contract.preflight", "dispatch.start", "dispatch.observe", "events.wait", "return.capture", "return.check"], "role_binding": ref("successor", "DECISIONS.md"), "role_transition": None}}
    environment = {k: os.environ[k] for k in ["PATH", "LANG", "LC_ALL", "TMPDIR"] if k in os.environ}
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    outer_environment = dict(environment)
    for name in ["HOME", "home", "CODEX_HOME"]:
        if name in os.environ:
            outer_environment[name] = os.environ[name]
    save(HERE / "environment-presence.json", {"selected_passthrough": [{"name": "CLAUDE_CODE_OAUTH_TOKEN", "present": "CLAUDE_CODE_OAUTH_TOKEN" in os.environ}], "values_retained": False, "authentication": "not yet attempted"})
    tool_files = sorted((TOOL / "build_tenants/graphify/code").glob("*.py")) + [ADAPTER, PROFILE]
    grants = {}; executors = {}; territories = {}; tasks = {}; contracts = {}; tenant_inputs = {}
    for tenant in ["codex", "claude"]:
        host_text = (OLD / tenant / "HOST.md").read_text()
        host_text = host_text.replace("Your construction host exposes only configured a_c MCP tools. Executable tests unavailable in this activation remain explicitly unperformed for Root's later proof.", "Your construction host exposes Bash and Read. Public CLI is the ordinary transport; no MCP approval is required. Scoped mkdir and read-only focused validation are authorized; file contents must use work.write.")
        save(HERE / tenant / "HOST.md", host_text)
        save(HERE / tenant / "TASK.md", task(tenant))
        save(HERE / tenant / "PREDICATES.md", PREDICATES)
        task_ref = ref("successor", tenant + "/TASK.md")
        predicates = ref("successor", tenant + "/PREDICATES.md")
        grant_id = "urn:stdo-skills:T001:" + tenant + ":construction:2"
        actor_id = "urn:stdo-skills:T001:" + tenant + ":worker:2"
        principals[tenant] = {"actor_id": actor_id, "role": "Worker", "family": "openai-codex" if tenant == "codex" else "anthropic-claude", "authorship": tenant + " tenant candidate author; successor activation", "operations": READ + ["work.write"], "role_binding": task_ref, "role_transition": None}
        territory = [{"root": "product", "path": p, "kind": "directory"} for p in ["build_tenants/" + tenant, ".ai-workspace/work/T001/" + tenant + "/actor/successor-1"]]
        territories[tenant] = territory
        grant = {"id": grant_id, "authority_sources": owner["authority_sources"] + [task_ref], "outcome": {"id": "urn:stdo-skills:T001:" + tenant + ":candidate", "source": task_ref}, "principals": ["executive", tenant], "targets": [tenant], "operations": ["contract.preflight", "dispatch.start", "work.write"], "tools": ["a_c.public-native301", "host.scoped-mkdir-read-compute-validation"], "executors": [tenant + "-cli-successor-1"], "territory": territory, "preconditions": inputs, "admission": {"mechanism_id": "product-policy-preflight/1", "mechanism_source": owner["mechanism"]["source"], "authority_source": owner_ref, "required_predicates": [], "allowed_override_sources": []}, "notification_sink": "root-events"}
        grants[grant_id] = grant
        wp = copy.deepcopy(base); wp["id"] += ":" + tenant
        for alias in ["operator", "successor"]:
            wp["sources"][alias]["read_scope"] = [s for s in wp["sources"][alias]["read_scope"] if s["path"] != ("claude" if tenant == "codex" else "codex")]
        wp["sources"]["product"]["read_scope"] += [{"path": x["path"], "kind": x["kind"]} for x in territory]
        wp["principals"] = {tenant: principals[tenant]}
        wg = copy.deepcopy(grant); wg.update({"principals": [tenant], "targets": [tenant], "operations": ["work.write"], "executors": [], "notification_sink": None})
        wp["grants"] = {grant_id: wg}
        wp_path = HERE / tenant / "worker-policy.json"; save(wp_path, wp)
        selected_inputs = inputs + [definition_ref, proof_source, result_source, profile["source"], ref("successor", tenant + "/HOST.md"), ref("successor", tenant + "/HISTORY.json"), predicates]
        if tenant == "codex":
            selected_inputs.append(ref("successor", "codex/PRIOR-PROPOSAL.md"))
        save(HERE / tenant / "SOURCE-ROUTES.json", {"required": inputs + [definition_ref, predicates, ref("successor", tenant + "/HOST.md"), ref("successor", tenant + "/HISTORY.json")], "deciding_method": [proof_source, result_source], "tool_profile": profile["source"], "proposal": None if tenant == "claude" else ref("successor", "codex/PRIOR-PROPOSAL.md"), "root_paths": {k: v["path"] for k, v in wp["sources"].items()}})
        cli_argv = [str(PYTHON), "-B", str(CLI), "--policy", str(wp_path), "--policy-sha256", sha(wp_path), "--principal", tenant, "call", "--request", "-"]
        startup = f"You are the {tenant} Worker under the attached exact Context. Build a useful tenant candidate within 600 seconds. First public source.read TASK {json.dumps(task_ref, separators=(',',':'))}; then SOURCE-ROUTES and deciding sources. Public CLI is the ordinary supported transport; MCP is not required. Execute this argv with JSON envelope on stdin: {json.dumps(cli_argv)}. Example request: {{\"schema\":\"a_c.fd-support.request/1\",\"id\":\"{tenant}-s1-task\",\"operation\":\"source.read\",\"arguments\":{{\"source\":{json.dumps(task_ref,separators=(',',':'))},\"encoding\":\"utf8\"}}}}. Bash/Python may compose the JSON in memory and subprocess.run it with input, preserving the inherited environment; no request file is needed. Use work.write for every artifact's content. Scoped mkdir, reads and read-only validation are authorized by TASK; parent directories already exist. No peer/global/Git/model effects. Emit one original closed-return JSON using Context identities and actual assessment evidence; no summary replacement."
        save(HERE / tenant / "STARTUP.txt", startup + "\n")
        if tenant == "codex":
            argv = [str(CODEX), "exec", "--json", "--color", "never", "--sandbox", "workspace-write", "--cd", str(PRODUCT), startup]
            backend = CODEX; decoder = "codex-final-jsonl/1"
        else:
            argv = [str(CLAUDE), "--print", "--output-format", "stream-json", "--verbose", "--permission-mode", "acceptEdits", "--permission-prompts", "none", "--tools", "Bash,Read", "--allowedTools", "Bash,Read", "--strict-mcp-config", "--append-system-prompt", startup]
            backend = CLAUDE; decoder = "claude-result-jsonl/1"
        settings = {"selected_host": "codex-cli 0.164.0" if tenant == "codex" else "Claude Code 2.1.306", "model_default": "gpt-6-astra" if tenant == "codex" else "fable", "effort_default": "max" if tenant == "codex" else "high", "model_override": False, "resolved_backend": "unobserved until actual run", "cost": "unknown", "host_context_bytes": "unknown", "retry_policy": "no automatic actor retry", "host_scope": "cooperative exact territory; scoped mkdir/read-compute/validation; artifact content through work.write"}
        if tenant == "claude":
            settings["environment_passthrough"] = ["CLAUDE_CODE_OAUTH_TOKEN"]
        plan = {"schema": "a_c.fd-support.actor-cli-plan/1", "id": "urn:stdo-skills:T001:" + tenant + ":actor-plan:successor-1", "backend": tenant, "executable": pin(backend), "argv": argv, "dependencies": [pin(p) for p in tool_files] + [pin(wp_path), pin(HERE / tenant / "STARTUP.txt")], "cwd": str(PRODUCT), "environment": environment, "settings": settings, "decoder": decoder, "evidence_directory": str(HERE / tenant / "actor-cli-output"), "limits": {"max_input_bytes": 4*1024*1024, "max_output_bytes": 4*1024*1024, "timeout_ms": 600000, "termination_grace_ms": 3000}}
        plan_path = HERE / tenant / "actor-plan.json"; save(plan_path, plan)
        executor_settings = {"timeout_ms": 610000, "termination_grace_ms": 5000, "max_output_bytes": 4*1024*1024, "model_default": settings["model_default"], "effort_default": settings["effort_default"]}
        if tenant == "claude":
            executor_settings["environment_passthrough"] = ["CLAUDE_CODE_OAUTH_TOKEN"]
        executors[tenant + "-cli-successor-1"] = {"id": tenant + "-cli-successor-1", "executable": pin(PYTHON), "argv": [str(PYTHON), "-B", str(ADAPTER), "--plan", str(plan_path), "--plan-sha256", sha(plan_path)], "dependencies": [ref("tool", str(p.relative_to(TOOL))) for p in tool_files] + [ref("successor", tenant + "/" + n) for n in ["worker-policy.json", "STARTUP.txt", "actor-plan.json"]] + [host_refs[tenant], host_refs["python"]], "cwd": str(PRODUCT), "environment": outer_environment, "actor_id": actor_id, "settings": executor_settings, "tools": grant["tools"], "effect_scope": {"declared_territory": territory, "host_operations": "mkdir inside territory, permitted reads and focused read-only validation; no artifact content bypass", "external_effects": "unknown until observed; no OS confinement claim", "no_remote_or_git_grant": True}, "stdin_mode": "context-utf8", "stdout_decoder": {"format": "json", "pointer": None, "decode_json_string": False}, "observers": [{"kind": "process-end"}]}
        contract = {"schema": "a_c.fd-support.return-contract/1", "id": "urn:stdo-skills:T001:" + tenant + ":return:successor-1", "authority_source": task_ref, "carrier": "a_c.fd-support.closed-return/1", "output_slot": "final_stdout_object", "required_evaluations": [{"id": "tenant-instruction-fitness", "predicate": predicates}, {"id": "tenant-package-integrity", "predicate": predicates}], "role": "Worker", "proof": {"transition_sources": [], "predicate_ids": []}}
        save(HERE / tenant / "RETURN-CONTRACT.json", contract)
        tasks[tenant] = task_ref; contracts[tenant] = ref("successor", tenant + "/RETURN-CONTRACT.json")
        tenant_inputs[tenant] = selected_inputs + [ref("successor", tenant + "/SOURCE-ROUTES.json")]
    executive = copy.deepcopy(base); executive.update({"principals": principals, "grants": grants, "executors": executors})
    executive["event_sinks"] = {"root-events": {"kind": "durable-file-events", "directory": "notifications", "consumer": "root-executive", "authority_source": owner_ref, "retention": "indefinite"}}
    for territory in territories.values():
        executive["sources"]["product"]["read_scope"] += [{"path": x["path"], "kind": x["kind"]} for x in territory]
    policy_path = HERE / "executive-policy.json"; save(policy_path, executive)
    save(HERE / "PREPARED.json", {"policy": pin(policy_path), "tool_basis": pin(HERE / "TOOL-BASIS.json"), "definition": pin(definition_path), "plans": {t: pin(HERE / t / "actor-plan.json") for t in tasks}, "external_model_dispatches": 0})
    # Exercise the actual adapter's plan validator without invoking a backend.
    spec = importlib.util.spec_from_file_location("prepared_actor_cli", ADAPTER)
    module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module; spec.loader.exec_module(module)
    checks = {}
    for tenant in tasks:
        planpath = HERE / tenant / "actor-plan.json"
        module.load_plan(planpath, sha(planpath))
        checks[tenant] = {"plan_sha256": sha(planpath), "actual_adapter_validation": "passed", "backend_invoked": False}
    save(HERE / "ADAPTER-PLAN-CHECK.json", checks)
    receipts = {}
    for tenant in tasks:
        call(policy_path, "executive", tenant + "-s1-describe", "tools.describe", {"operation": "context.assemble"})
        observation_result = call(policy_path, "executive", tenant + "-s1-observe", "workspace.observe", {"scope": [{"root": "product", "path": "stdo_skills.json", "kind": "file"}] + [{"root": x["root"], "path": x["path"], "kind": "file"} for x in inputs] + territories[tenant]})
        observation = observation_result["result"]["artifact"]
        subject = {"id": "urn:stdo-skills:T001:" + tenant + ":candidate", "sha256": COMMON}
        grant_id = "urn:stdo-skills:T001:" + tenant + ":construction:2"
        predicates = ref("successor", tenant + "/PREDICATES.md")
        packet = {"activation": {"id": grant_id, "revision": "2", "configuration": tasks[tenant]}, "frame": {"id": "skills.worker/1", "revision": "2", "declaration": inputs[4], "evaluation": predicates, "result_algebra": result_source}, "subject_basis": {"subject": subject, "method_profile": {k: profile[k] for k in ["id", "sha256"]}, "product": {"id": executive["product"]["definition_id"], "definition": definition_ref}, "observations": [observation], "dependencies": inputs, "time_basis": "exact current observation after prior closure, revised contract and directory provisioning"}, "attention": {"material_relations": [ref("successor", tenant + "/SOURCE-ROUTES.json"), ref("successor", tenant + "/HISTORY.json")], "invariants": [inputs[2], proof_source], "semantic_sources": [inputs[0], inputs[5]], "exclusions": ["peer design/code/output", "Git/remote/global mutations"], "prohibited_assumptions": ["source existence proves fitness", "candidate ready proves acceptance", "prior process end proves all effects absent"]}, "actor_authority": {"actor_id": principals[tenant]["actor_id"], "role": "Worker", "capability": ref("successor", tenant + "/HOST.md"), "semantic": inputs[0], "evaluation": predicates, "operation": tasks[tenant], "decision": None, "acceptance": None, "publication": None, "territory": territories[tenant], "tools": grants[grant_id]["tools"]}, "evidence_relations": {"admissible_evidence": [predicates, tasks[tenant]], "acquisition": tenant_inputs[tenant], "dependencies": [ref("successor", tenant + "/HISTORY.json")], "conjunction": None, "translation": None, "consumer": "root-executive", "return_contract": contracts[tenant]}, "stop_change": {"invalidators": ["material source/tool/authority drift", "unreconciled effect"], "stop_conditions": ["600 seconds", "genuine unsupported required operation"], "residuals": ["mandatory actual-host Q01-Q12 and independent review remain open"], "re_entry": ["return exact partial candidate and missing premise"], "reconfiguration": ["successor of known failed attempt " + ATTEMPTS[tenant] + "; see retained HISTORY"]}, "profile_additions": {"worker": {"operation_grant_id": grant_id, "mutation_subject": subject, "territory": territories[tenant]}}}
        # Context has the concise deciding task and predicate. All other exact
        # material sources remain available through declared late acquisition.
        late = tenant_inputs[tenant] + [inputs[4], result_source]
        late = [json.loads(k) for k in dict.fromkeys(json.dumps(x, sort_keys=True) for x in late) if json.loads(k) != predicates]
        assembled = call(policy_path, "executive", tenant + "-s1-assemble", "context.assemble", {"packet": packet, "models": [], "sources": [tasks[tenant], contracts[tenant], predicates], "late_acquisition": late, "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})
        context = assembled["result"]["artifact"]
        preflight = call(policy_path, "executive", tenant + "-s1-preflight", "contract.preflight", {"context": context, "grant_id": grant_id, "executor_id": tenant + "-cli-successor-1", "result_key": "T001/" + tenant + "/construction-2", "observations": [observation]})
        value = preflight["result"]["value"]
        if value["decision"] != "admitted" or value["contract_state"] != "admitted" or value["gaps"]:
            raise RuntimeError("Preflight has unresolved admission: " + tenant)
        receipts[tenant] = {"context": context, "observation": observation, "preflight": preflight["result"]["artifact"], "preflight_evidence": preflight["evidence"], "decision": value["decision"], "contract_sha256": value.get("exact_contract", {}).get("sha256"), "fit": assembled["result"]["value"]["fit"], "plan": pin(HERE / tenant / "actor-plan.json"), "policy": pin(policy_path)}
        save(HERE / ("root-dispatch-" + tenant + ".request.json"), {"schema": "a_c.fd-support.request/1", "id": "root-T001-" + tenant + "-successor1-dispatch", "operation": "dispatch.start", "arguments": {"preflight": receipts[tenant]["preflight"]}})
    save(HERE / "READINESS.json", {"receipts": receipts, "external_model_dispatches": 0, "boundary": "Preparation and native admission only; Root reviews before launch", "historical_attempts_preserved": ATTEMPTS, "tool_basis": pin(HERE / "TOOL-BASIS.json")})
    return {"readiness": str(HERE / "READINESS.json"), "sha256": sha(HERE / "READINESS.json"), "external_model_dispatches": 0}


if __name__ == "__main__":
    print(json.dumps(prepare(), indent=2))
