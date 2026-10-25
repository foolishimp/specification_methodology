"""Prepare one frozen installed-package trial and its real public preflight.

The Executive supplies an exact selection JSON after candidate freeze. This
script never dispatches a host, selects a model or manufactures an assessment.
Later cases reuse ordinary fixture files/prompts and this same preparation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
TOOL = REPO / "a_c"
CODE = TOOL / "build_tenants/graphify/code"
CLI = CODE / "ac_support.py"
CORE = CODE / "ac_support_core.py"
TRANSPORT = TOOL / "build_tenants/graphify/examples/fd-support/actor_cli.py"
PROFILE = TOOL / "build_tenants/graphify/design/fd-method-stdo-3.0.1.json"
METHOD = Path("/Users/jim/Library/Application Support/STDO/releases/v3.0.1-rc.1")
PYTHON = Path("/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python").resolve()
PROFILE_ID = "urn:a-c:fd-support:method:stdo-3.0.1-rc.1:executive:1"
CORE_SHA = "bf72a28444e0497cd564066e41c7e5943810d5a2e0be5488c92fa5add5a67209"
READ = ["tools.describe", "workspace.observe", "source.read", "records.find", "records.read", "graph.project", "relations.query", "evidence.read", "work.project"]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin(path: Path) -> dict:
    return {"path": str(path), "sha256": sha(path)}


def acquire(value: dict) -> Path:
    path = Path(value["path"])
    if not path.is_absolute() or any(p.is_symlink() for p in (path, *path.parents)) or sha(path) != value["sha256"]:
        raise ValueError("Selected exact input unavailable: " + str(path))
    return path


def save(path: Path, value) -> None:
    raw = value if isinstance(value, bytes) else value.encode() if isinstance(value, str) else (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(raw)


def materialize_selected_package(selection: dict, workspace: Path, control: Path,
                                 package_root: Path, destination: Path,
                                 package_files: list[dict]) -> dict | None:
    """Consume a selected shipped installer, or verify an actual earlier update.

    The legacy copy path is unchanged. This is fixture preparation, never a host
    dispatcher or another installation implementation. Existing-install inputs
    retain the prior actual lifecycle custody record rather than minting one.
    """
    binding = selection.get("install_binding")
    if binding is None:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(package_root, destination)
        return None
    tenant_root = Path(selection["tenant_root"]).resolve(strict=True)
    kind = binding.get("kind")
    if kind == "codex-existing-package/1":
        if selection["tenant"] != "codex" or package_root != tenant_root / "skills/stdo-work":
            raise ValueError("Existing Codex install binding disagrees with selected package")
        checker = acquire(binding["verifier"])
        if checker.resolve() != tenant_root / "tests/verify_package.py":
            raise ValueError("Select the shipped Codex custody verifier")
        custody = pin(acquire(binding["custody"]))
        command = [str(PYTHON), "-B", str(checker), str(tenant_root), "--installed", str(destination)]
        result = subprocess.run(command, cwd=workspace, capture_output=True, timeout=60)
        save(control / "install-checks/selected-existing.json", {"argv": command, "verifier": binding["verifier"],
            "prior_lifecycle_custody": custody, "returncode": result.returncode,
            "stdout": result.stdout.decode(), "stderr": result.stderr.decode()})
        if result.returncode != 0:
            raise ValueError("Existing selected Codex installation failed shipped custody check")
        return {"kind": kind, "custody": custody, "candidate_inventory": selection["candidate_record"]}
    if kind != "claude-bundle-installer/1" or selection["tenant"] != "claude":
        raise ValueError("Unsupported exact installation binding")
    if package_root != tenant_root / "skills" or destination != workspace / ".claude/skills":
        raise ValueError("Claude install must select the complete declared project bundle")
    helper = acquire(binding["helper"])
    if helper.resolve() != tenant_root / "skills/stdo-release-install/scripts/manage_install.py":
        raise ValueError("Select the shipped Claude bundle installer")
    action = binding.get("action")
    receipt = workspace / ".claude/stdo-skills-claude.receipt.json"
    prior = None
    if action == "install":
        command = [str(PYTHON), "-I", "-B", str(helper), "install", "--package", str(tenant_root), "--workspace", str(workspace)]
        result = subprocess.run(command, cwd=workspace, capture_output=True, timeout=60)
        save(control / "install-checks/selected-installer.json", {"argv": command, "helper": binding["helper"],
            "returncode": result.returncode, "stdout": result.stdout.decode(), "stderr": result.stderr.decode()})
        if result.returncode != 0:
            raise ValueError("Selected shipped installer refused or had uncertain effects; retain fixture")
        response = json.loads(result.stdout)
        if response.get("status") != "ok" or response.get("receipt") != str(receipt):
            raise ValueError("Shipped installer did not return the selected receipt")
        selected_receipt_sha = response["receipt_sha256"]
    elif action == "verified-existing":
        prior = pin(acquire(binding["custody"]))
        selected_receipt_sha = binding["receipt_sha256"]
    else:
        raise ValueError("Claude install action must be install or verified-existing")
    if receipt.is_symlink() or not receipt.is_file() or sha(receipt) != selected_receipt_sha:
        raise ValueError("Selected Claude receipt missing or changed")
    record = json.loads(receipt.read_text())
    if (record.get("schema") != "stdo-skills.claude-installation/1"
            or record.get("source_inventory_sha256") != selection["candidate_record"]["sha256"]):
        raise ValueError("Receipt source identity differs from selected package")
    names = {Path(item["path"]).parts[0] for item in package_files}
    if set(record.get("skills", {})) != names:
        raise ValueError("Receipt does not contain selected complete roster")
    # Compare current physical bytes/directories with both the retained receipt
    # and selected source. This read-only check performs no install/delete effect.
    for name in sorted(names):
        expected_files = {str(Path(x["path"]).relative_to(name)): x["sha256"] for x in package_files if Path(x["path"]).parts[0] == name}
        installed_root = destination / name
        if any(p.is_symlink() for p in (installed_root, *installed_root.parents)):
            raise ValueError("Selected installed path contains a symlink")
        files = {}; dirs = ["."]
        for p in sorted(installed_root.rglob("*")):
            if p.is_symlink():
                raise ValueError("Selected installed resource contains a symlink")
            if p.is_dir(): dirs.append(str(p.relative_to(installed_root)))
            elif p.is_file(): files[str(p.relative_to(installed_root))] = sha(p)
            else: raise ValueError("Selected installed resource is not regular")
        population = {"directories": sorted(dirs), "files": dict(sorted(files.items()))}
        if files != expected_files or record["skills"][name] != population:
            raise ValueError("Actual Claude installation differs from selected receipt/package")
    return {"kind": kind, "helper": binding["helper"], "action": action,
            "receipt": pin(receipt), "prior_lifecycle_custody": prior}


def prepare(selection_path: Path, selected_sha: str) -> dict:
    selection = json.loads(acquire({"path": str(selection_path), "sha256": selected_sha}).read_text())
    if selection["schema"] != "stdo_skills.qualification-selection/1" or sha(CORE) != CORE_SHA:
        raise ValueError("Selection schema or frozen tool mechanism differs")
    fixtures = json.loads((HERE / "FIXTURES-v3.json").read_text())
    selected_fixtures = [json.loads(acquire(selection["fixture_record"]).read_text())] if "fixture_record" in selection else fixtures["lanes"]
    matches = [x for x in selected_fixtures if x["tenant"] == selection["tenant"] and x["lane"] == selection["lane"]]
    if len(matches) != 1:
        raise ValueError("Select exactly one prepared fixture")
    fixture = matches[0]
    tenant, lane = fixture["tenant"], fixture["lane"]
    artifact_paths = fixture.get("artifact_paths", [] if lane == "unrelated" else ["outputs/greeting.txt"])
    stable_paths = fixture.get("stable_input_paths", [] if lane == "unrelated" else ["specification/REQUIREMENT.md", "design/DESIGN.md", "inputs/name.txt"])
    if any(not isinstance(p, str) or Path(p).is_absolute() or ".." in Path(p).parts for p in artifact_paths + stable_paths):
        raise ValueError("Fixture paths must remain inside the selected workspace")
    workspace, control = Path(fixture["workspace"]), Path(fixture["control"])
    if (control / "PREPARED.json").exists() or (control / "OWNER.json").exists():
        raise ValueError("Preparation is create-only; retain prior attempt and select a fresh fixture")
    acquire(selection["candidate_record"])
    acquire(selection["install_documentation"])
    host_plan_path = acquire(selection["host_plan_source"])
    host_source = json.loads(host_plan_path.read_text())
    backend = acquire(host_source["executable"])
    if host_source["backend"] != tenant:
        raise ValueError("Host selection does not match tenant")
    package_root = Path(selection["package_root"]).resolve(strict=True)
    package_files = []
    for path in sorted(package_root.rglob("*")):
        if path.is_symlink():
            raise ValueError("Package symlink is outside this declared copy recipe")
        if path.is_file():
            package_files.append({"path": str(path.relative_to(package_root)), "sha256": sha(path)})
    if package_files != selection["package_files"] or not any(x["path"].endswith("SKILL.md") for x in package_files):
        raise ValueError("Complete selected package population changed or has no skill")
    relative = Path(selection["install_relative"])
    prefix = ".agents/skills" if tenant == "codex" else ".claude/skills"
    if relative.is_absolute() or ".." in relative.parts or not (str(relative) == prefix or str(relative).startswith(prefix + "/")):
        raise ValueError("Installation is outside this tenant's documented local discovery scope")
    destination = workspace / relative
    if destination.exists() and selection.get("install_binding") is None:
        raise ValueError("Selected package destination is not fresh")
    tenant_root = Path(selection["tenant_root"]).resolve(strict=True)
    shutil.copytree(tenant_root, control / "tenant-receipt")

    def install_checks(stage: str) -> None:
        for index, check in enumerate(selection["install_checks"][stage]):
            for dependency in check["dependencies"]:
                acquire(dependency)
            command = check["argv"]
            offset = 3 if command[:3] == [str(PYTHON), "-I", "-B"] else 2
            if (offset == 2 and command[:2] != [str(PYTHON), "-B"]) or command[offset] not in [x["path"] for x in check["dependencies"]]:
                raise ValueError("Installation check is not the selected pinned Python verifier")
            result = subprocess.run(command, capture_output=True, timeout=30)
            save(control / "install-checks" / (stage + "-" + str(index) + ".json"), {"argv": command, "returncode": result.returncode, "stdout": result.stdout.decode(), "stderr": result.stderr.decode()})
            if result.returncode != 0:
                raise ValueError("Documented installation check failed; retain fixture")

    install_checks("before")
    install_binding = materialize_selected_package(selection, workspace, control, package_root, destination, package_files)
    install_checks("after")
    installed = [{"path": str((destination / x["path"]).relative_to(workspace)), "sha256": sha(destination / x["path"])} for x in package_files]
    package = {"candidate_record": selection["candidate_record"], "documentation": selection["install_documentation"],
               "source_root": str(package_root), "install_relative": str(relative), "files": installed}
    if install_binding is not None:
        package["installation_binding"] = install_binding
    save(control / "INSTALL.json", package)
    save(control / "SELECTION.json", selection)
    ordinary = (control / "ordinary-prompt.base.txt").read_text()
    if lane == "explicit":
        prefix = selection["explicit_prefix"]
        if not isinstance(prefix, str) or not prefix.startswith("$" if tenant == "codex" else "/") or "\n" in prefix:
            raise ValueError("Explicit lane needs the actual documented native invocation prefix")
        ordinary = prefix + " " + ordinary
    save(control / "ordinary-prompt.txt", ordinary)
    evidence = control / "evidence"
    evidence.mkdir()
    roots = {"product": workspace, "control": control, "tool": TOOL, "method": METHOD, "host_python": PYTHON.parent, "host_vendor": backend.parent, "fixture_code": HERE}

    def ref(alias: str, name: str) -> dict:
        return {"engine": "workspace-regular-file", "root": alias, "path": name, "object": None, "sha256": sha(roots[alias] / name), "selector": None}

    core_ref = ref("tool", str(CORE.relative_to(TOOL)))
    mechanism = {"id": "product-policy-preflight/1", "source": core_ref, "implementation_sha256": CORE_SHA}
    outcome_id = "urn:stdo-skills:qualification:" + tenant + ":" + lane
    consumer = "qualification-executive"
    scope = {"selection_sha256": selected_sha, "case": lane, "purpose": "Owner-selected finite skill qualification; no host semantic result preaccepted", "host_artifact_writes": artifact_paths, "physical_executor_writes": ["control/actor-output"], "forbidden": ["Git mutations/publication", "remote publication", "global configuration", "oracle acquisition", "unrelated mutation"], "projection": "Pinned launcher forwards only the exact selected ordinary prompt; context bookkeeping remains with operator"}
    if fixture.get("fixture_premise_effects"):
        scope["fixture_premise_effects"] = fixture["fixture_premise_effects"]
    owner = {"mechanism": mechanism, "result_surface": {"root": str(evidence), "namespace": "results", "consumer": consumer}, "scope": scope,
             "authority": "Root selected HOST_EVIDENCE_PLAN a831a5cc21683aa517264029cb822db5baf2a2de2dedee83f20157c5675a08e6 and this bounded preparation; actual dispatch still requires Root selection"}
    save(control / "OWNER.json", owner)
    if lane == "unrelated":
        definition = json.loads((HERE / "inputs-v3/governed/fixture_product.json").read_text())
        definition["product"].update({"definition_id": outcome_id + ":controller", "name": "Qualification control", "bounded_context": {"id": outcome_id + ":control-boundary", "definition": "./PRODUCT.md#product-boundary"}})
        definition["constitution"]["additional_authorities"] = ["./INTENT.md", "./PRODUCT.md"]
        definition["constitution"]["agent_bootstrap"]["targets"] = ["./TASK.md"]
        definition["reference_frame_bases"] = [{"uri": "./TASK.md", "authority": ["./PRODUCT.md#construction-authority"], "applies_to": [definition["product"]["definition_id"]]}]
        definition["what"] = {"intent": "./INTENT.md", "product": "./PRODUCT.md", "specification": ["./TASK.md"]}
        definition["how"] = {"common": ["./OWNER.json"], "build_tenants": [{"id": outcome_id + ":fixed-launcher", "root": "./actor-output/", "design": ["./TASK.md"], "implementation": ["./launch.json"]}]}
        definition["ticketing"]["goals"] = "./GOALS.md"
        save(control / "INTENT.md", "# Intent\nObserve one selected ordinary native-host task without adopting its workspace into this control Product.\n")
        save(control / "PRODUCT.md", "# Qualification control\n\n## Product boundary\nFixed local projection, host launch and exact observation custody only. The unrelated actor workspace remains outside STDO adoption.\n\n## Construction authority\nRoot selected the bounded trial plan. Its exact grant and preparation are in OWNER.json; Root separately selects dispatch.\n")
        save(control / "GOALS.md", "# Selection\nRetain one exact trial's observations; semantic host assessment remains with Root and the selected source-first reviewer.\n")
        save(control / "CONTROLLER.json", definition)
        definition_ref = ref("control", "CONTROLLER.json")
        locator = "/how/common/0"
    else:
        owner_path = workspace / ".qualification/OWNER.json"
        save(owner_path, owner)
        definition_ref = ref("product", "fixture_product.json")
        locator = "/how/common/1"
    # Binding points at the exact owner URI selected by this Product Definition.
    owner_ref = ref("control", "OWNER.json") if lane == "unrelated" else ref("product", ".qualification/OWNER.json")
    definition = json.loads((roots[definition_ref["root"]] / definition_ref["path"]).read_text())
    save(control / "TASK.md", "# Qualification transport contract\n\nExecute the exact selected native host once with the predeclared ordinary prompt and normally installed package. The fixed launcher returns only retained local observations. Host task success, discovery, actual model resolution and method behavior remain for source-first assessment. Read/compute and scoped ordinary directory creation are permitted; host artifact content uses its separate work.write grant. No oracle is supplied. No retry, model override or next stage.\n")
    task = ref("control", "TASK.md")
    sources = {
        "product": {"path": str(workspace), "kind": "workspace", "writable": True, "read_scope": [{"path": p.name, "kind": "directory" if p.is_dir() else "file"} for p in sorted(workspace.iterdir())] + ([] if lane == "unrelated" else [{"path": "TOOLING.md", "kind": "file"}])},
        "control": {"path": str(control), "kind": "workspace", "writable": False, "read_scope": [{"path": name, "kind": "file"} for name in ("OWNER.json", "TASK.md", "worker-policy.json", "mcp.json", "actor-plan.json", "launch.json", "executive-policy.json", "RETURN-CONTRACT.json", "ordinary-prompt.txt", "ordinary-prompt.base.txt", "INSTALL.json", "SELECTION.json", "CONTROLLER.json", "INTENT.md", "PRODUCT.md", "GOALS.md")] + [{"path": "actor-output", "kind": "directory"}]},
        "tool": {"path": str(TOOL), "kind": "workspace", "writable": False, "read_scope": [{"path": "build_tenants/graphify", "kind": "directory"}]},
        "method": {"path": str(METHOD), "kind": "workspace", "writable": False, "read_scope": [{"path": "standards", "kind": "directory"}, {"path": "manifest.json", "kind": "file"}]},
        "host_python": {"path": str(PYTHON.parent), "kind": "workspace", "writable": False, "read_scope": [{"path": PYTHON.name, "kind": "file"}]},
        "host_vendor": {"path": str(backend.parent), "kind": "workspace", "writable": False, "read_scope": [{"path": backend.name, "kind": "file"}]},
        "fixture_code": {"path": str(HERE), "kind": "workspace", "writable": False, "read_scope": [{"path": "launch_fixture.py", "kind": "file"}]},
    }
    profile = {"id": PROFILE_ID, "sha256": sha(PROFILE), "source": ref("tool", str(PROFILE.relative_to(TOOL)))}
    actor = {"id": outcome_id + ":physical-launcher", "family": "fixed-local-qualification-executor", "authorship": "pinned projection/capture implementation; no semantic host assessment"}
    principals = {"executive": {"actor_id": consumer, "role": "Executive", "family": "orchestrator", "authorship": "Root qualification coordination", "operations": READ + ["context.assemble", "contract.preflight", "dispatch.start", "dispatch.observe", "return.capture", "return.check"], "role_binding": task, "role_transition": None},
                  "launcher": {"actor_id": actor["id"], "role": "Worker", "family": actor["family"], "authorship": actor["authorship"], "operations": READ, "role_binding": task, "role_transition": None},
                  "host": {"actor_id": outcome_id + ":host", "role": "Worker", "family": tenant, "authorship": "actual native host trial; model observations remain raw", "operations": READ + ([] if lane == "unrelated" else ["work.write"]), "role_binding": task, "role_transition": None}}
    territory = [{"root": "product", "path": path, "kind": "file"} for path in artifact_paths]
    tools = ["native-host", "a_c.public-native301", "host.read-compute", "host.directory-create"]
    grant_id = outcome_id + ":launch"
    admission = {"mechanism_id": mechanism["id"], "mechanism_source": core_ref, "authority_source": owner_ref, "required_predicates": [], "allowed_override_sources": []}
    grant = {"id": grant_id, "authority_sources": [owner_ref, task], "outcome": {"id": outcome_id, "source": task}, "principals": ["executive"], "targets": ["launcher"], "operations": ["contract.preflight", "dispatch.start"], "tools": tools, "executors": ["trial"], "territory": territory, "preconditions": [task], "admission": admission, "notification_sink": "events"}
    base = {"schema": "a_c.fd-support.policy/1", "id": outcome_id + ":policy", "product": {"definition_id": definition["product"]["definition_id"], "definition": definition_ref,
            "authority_binding": {"definition_locator": locator, "owner_record": owner_ref, "mechanism": mechanism, "result_surface": owner["result_surface"], "scope": scope}},
            "method_profile": profile, "sources": sources, "principals": principals, "grants": {}, "predicates": {}, "operators": {}, "executors": {}, "event_sinks": {}, "independence_policy": "Source-first oracle remains outside actor input; Root independently assesses exact native trial observations", "evidence_root": str(evidence), "limits": {"max_source_bytes": 16*1024*1024,"max_scan_entries": 20000,"max_context_bytes": 4*1024*1024}, "authority_sources": [owner_ref]}
    # Reuse the shipped policy's exact limit keys, without importing its authority.
    old_policy = json.loads((REPO / "stdo_skills/.ai-workspace/work/T001/operator/executive-policy.json").read_text())
    base["limits"] = old_policy["limits"]
    worker = json.loads(json.dumps(base)); worker["id"] += ":host"; worker["principals"] = {"host": principals["host"]}
    if lane != "unrelated":
        write_grant = json.loads(json.dumps(grant)); write_grant.update({"id": outcome_id + ":write", "principals": ["host"], "targets": ["host"], "operations": ["work.write"], "executors": [], "notification_sink": None})
        worker["grants"] = {write_grant["id"]: write_grant}
    save(control / "worker-policy.json", worker)
    worker_args = ["-B", str(CLI), "--policy", str(control / "worker-policy.json"), "--policy-sha256", sha(control / "worker-policy.json"), "--principal", "host"]
    save(control / "mcp.json", {"mcpServers": {"stdo_ac": {"command": str(PYTHON), "args": worker_args + ["mcp"]}}})
    if lane != "unrelated":
        save(workspace / "TOOLING.md", "# Local tool binding\n\nNative 3.0.1 a_c is available as configured stdo_ac MCP tools, or this exact CLI (full request envelope on stdin):\n\n```sh\n" + " ".join([str(PYTHON), *worker_args, "call", "--request", "-"]) + "\n```\n\nUse tools.describe for the exact contract. Scope grant: `" + outcome_id + ":write`. Input source alias is `product`. Observe the output parent separately immediately before work.write; preserve target preimages and actual responses. Directory creation is permitted only within outputs. Stable governing inputs belong to Context; intended output preimages are separate. No native results.conjoin operator is selected.\n")
    environment = dict(host_source["environment"])
    environment.update({"AC_PYTHON": str(PYTHON), "AC_ENTRY": str(CLI), "AC_POLICY": str(control / "worker-policy.json"), "AC_POLICY_SHA256": sha(control / "worker-policy.json"), "AC_PRINCIPAL": "host"})
    settings = dict(host_source["settings"])
    settings.update({"fixture_case": lane, "model_override": False, "host_context_bytes": "unknown", "actual_models": "Retain all raw vendor model identifiers, including helper/classifier events"})
    if tenant == "claude":
        settings["environment_passthrough"] = ["CLAUDE_CODE_OAUTH_TOKEN"]
        argv = [str(backend), "--print", "--output-format", "stream-json", "--verbose", "--permission-mode", "acceptEdits", "--permission-prompts", "none", "--strict-mcp-config", "--mcp-config", str(control / "mcp.json"), "--allowedTools", "Bash,Read,Glob,Grep,Skill,mcp__stdo_ac__*"]
        decoder = "claude-result-jsonl/1"
    else:
        argv = [str(backend), "exec", "--json", "--color", "never", "--sandbox", "workspace-write", "--skip-git-repo-check", "--cd", str(workspace), "--add-dir", str(evidence), "-c", 'mcp_servers.stdo_ac.command=' + json.dumps(str(PYTHON)), "-c", 'mcp_servers.stdo_ac.args=' + json.dumps(worker_args + ["mcp"]), "-"]
        decoder = "codex-final-jsonl/1"
    timeout = selection["timeout_ms"]
    if type(timeout) is not int or timeout < 1000:
        raise ValueError("Root must select an explicit positive bounded host duration")
    dependencies = [pin(CORE), pin(TRANSPORT), pin(control / "worker-policy.json"), pin(control / "mcp.json")] + [pin(workspace / x["path"]) for x in installed]
    if install_binding and install_binding.get("receipt"):
        dependencies.append(install_binding["receipt"])
    plan = {"schema": "a_c.fd-support.actor-cli-plan/1", "id": outcome_id + ":native-plan", "backend": tenant, "executable": pin(backend), "argv": argv, "dependencies": dependencies, "cwd": str(workspace), "environment": environment, "settings": settings, "decoder": decoder, "evidence_directory": str(control / "actor-output"), "limits": {"max_input_bytes": 4*1024*1024, "max_output_bytes": 4*1024*1024, "timeout_ms": timeout, "termination_grace_ms": 3000}}
    save(control / "actor-plan.json", plan)
    activation_id = outcome_id + ":activation:1"
    launcher_config = {"schema": "stdo_skills.qualification-launch/1", "case": {"tenant": tenant, "lane": lane}, "activation_id": activation_id, "return_actor": actor,
                       "transport": pin(TRANSPORT), "actor_plan": pin(control / "actor-plan.json"), "ordinary_prompt": pin(control / "ordinary-prompt.txt"), "package": package, "max_outer_bytes": 4*1024*1024}
    save(control / "launch.json", launcher_config)
    outer_environment = dict(environment)
    for name in ("HOME", "home", "CODEX_HOME"):
        if name in os.environ:
            outer_environment[name] = os.environ[name]
    executor_settings = {"timeout_ms": timeout + 10000, "termination_grace_ms": 5000}
    if tenant == "claude":
        executor_settings["environment_passthrough"] = ["CLAUDE_CODE_OAUTH_TOKEN"]
    executor = {"id": "trial", "executable": pin(PYTHON), "argv": [str(PYTHON), "-B", str(HERE / "launch_fixture.py"), "--config", str(control / "launch.json"), "--config-sha256", sha(control / "launch.json")],
                "dependencies": [ref("fixture_code", "launch_fixture.py"), core_ref, ref("tool", str(TRANSPORT.relative_to(TOOL))), ref("control", "launch.json"), ref("control", "actor-plan.json"), ref("control", "ordinary-prompt.txt"), ref("control", "worker-policy.json"), ref("control", "mcp.json"), ref("host_vendor", backend.name)] + [ref("product", x["path"]) for x in installed],
                "cwd": str(workspace), "environment": outer_environment, "actor_id": actor["id"], "settings": executor_settings, "tools": tools, "effect_scope": scope, "stdin_mode": "context-utf8", "stdout_decoder": {"format": "json", "pointer": None, "decode_json_string": False}, "observers": [{"kind": "process-end"}]}
    base["grants"] = {grant_id: grant}; base["executors"] = {"trial": executor}
    base["event_sinks"] = {"events": {"kind": "durable-file-events", "directory": "notifications", "consumer": consumer, "authority_source": owner_ref, "retention": "indefinite"}}
    save(control / "executive-policy.json", base)
    contract = {"schema": "a_c.fd-support.return-contract/1", "id": outcome_id + ":physical-return", "authority_source": task, "carrier": "a_c.fd-support.closed-return/1", "output_slot": "final_stdout_object", "required_evaluations": [], "role": "Worker", "proof": {"transition_sources": [], "predicate_ids": []}}
    save(control / "RETURN-CONTRACT.json", contract)

    def call(name: str, operation: str, arguments: dict) -> dict:
        request = {"schema": "a_c.fd-support.request/1", "id": outcome_id + ":" + name, "operation": operation, "arguments": arguments}
        save(control / "requests" / (name + ".json"), request)
        command = [str(PYTHON), "-B", str(CLI), "--policy", str(control / "executive-policy.json"), "--policy-sha256", sha(control / "executive-policy.json"), "--principal", "executive", "call", "--request", str(control / "requests" / (name + ".json"))]
        result = subprocess.run(command, cwd=workspace, capture_output=True, timeout=60)
        save(control / "responses" / (name + ".stdout.json"), result.stdout)
        save(control / "responses" / (name + ".stderr.txt"), result.stderr)
        save(control / "responses" / (name + ".invocation.json"), {"argv": command, "returncode": result.returncode})
        response = json.loads(result.stdout)
        if result.returncode != 0 or response.get("status") != "ok":
            raise ValueError("Public preparation refused; preserve partial fixture: " + name + ": " + json.dumps(response.get("refusal")))
        return response

    call("describe", "tools.describe", {})
    call("acquire-prompt", "source.read", {"source": ref("control", "ordinary-prompt.txt"), "encoding": "utf8"})
    stable = [definition_ref, owner_ref, task, ref("control", "ordinary-prompt.txt"), ref("control", "INSTALL.json")] + [ref("product", x["path"]) for x in installed]
    if install_binding and install_binding.get("receipt"):
        stable.append(ref("product", str(Path(install_binding["receipt"]["path"]).relative_to(workspace))))
    if lane != "unrelated":
        stable += [ref("product", x) for x in stable_paths + ["TOOLING.md"]]
    observation = call("observe-stable-inputs", "workspace.observe", {"scope": [{"root": x["root"], "path": x["path"], "kind": "file"} for x in stable]})["result"]["artifact"]
    effect_target_preimage = None
    if lane != "unrelated":
        effect_target_preimage = call("observe-effect-target", "workspace.observe", {"scope": [{"root": "product", "path": path, "kind": "file"} for path in artifact_paths]})["result"]["artifact"]
    subject = {"id": outcome_id + ":observed-trial", "sha256": selected_sha}
    packet = {"activation": {"id": activation_id, "revision": "1", "configuration": task}, "frame": {"id": "qualification.physical-executor/1", "revision": "1", "declaration": task, "evaluation": task, "result_algebra": ref("method", "standards/ACTIVATION.md")},
              "subject_basis": {"subject": subject, "method_profile": {"id": PROFILE_ID, "sha256": sha(PROFILE)}, "product": {"id": base["product"]["definition_id"], "definition": definition_ref}, "observations": [observation], "dependencies": stable, "time_basis": "Stable deciding inputs only; intended mutable target preimages are separate host observations"},
              "attention": {"material_relations": stable, "invariants": stable, "semantic_sources": [task], "exclusions": ["independent oracle", "peer candidates", "prior host sessions"], "prohibited_assumptions": ["transport success is semantic host success", "configuration alias identifies one actual backend"]},
              "actor_authority": {"actor_id": actor["id"], "role": "Worker", "capability": task, "semantic": None, "evaluation": None, "operation": owner_ref, "decision": None, "acceptance": None, "publication": None, "territory": territory, "tools": tools},
              "evidence_relations": {"admissible_evidence": stable, "acquisition": stable, "dependencies": [], "conjunction": None, "translation": None, "consumer": consumer, "return_contract": ref("control", "RETURN-CONTRACT.json")},
              "stop_change": {"invalidators": ["source, package, prompt or authority drift"], "stop_conditions": ["selected duration", "required capability unavailable"], "residuals": ["host semantic assessment and exact model resolution remain separate"], "re_entry": ["retain every attempt; Root selects any successor"], "reconfiguration": []},
              "profile_additions": {"worker": {"operation_grant_id": grant_id, "mutation_subject": subject, "territory": territory}}}
    context = call("assemble", "context.assemble", {"packet": packet, "models": [], "sources": stable, "late_acquisition": [], "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})["result"]["artifact"]
    preflight = call("preflight", "contract.preflight", {"context": context, "grant_id": grant_id, "executor_id": "trial", "result_key": outcome_id, "observations": [observation]})
    baseline = {"schema": "stdo_skills.workspace-preimage/1", "workspace": str(workspace), "files": [{"path": str(p.relative_to(workspace)), "sha256": sha(p)} for p in sorted(workspace.rglob("*")) if p.is_file()]}
    save(control / "WORKSPACE-BEFORE.json", baseline)
    prepared = {"schema": "stdo_skills.qualification-prepared/1", "tenant": tenant, "lane": lane, "workspace": str(workspace), "control": str(control), "selection": pin(selection_path), "installed": pin(control / "INSTALL.json"), "policy": pin(control / "executive-policy.json"), "context": context, "effect_target_preimage": effect_target_preimage, "preflight": preflight["result"]["artifact"], "root_dispatch_selected": False, "host_dispatches": 0,
                "workspace_preimage": pin(control / "WORKSPACE-BEFORE.json"),
                "next": "Root reads exact native plan, ordinary prompt, projection and grant; only then selects dispatch.start using this preflight. No interpretation of this record authorizes a host launch."}
    save(control / "PREPARED.json", prepared)
    save(HERE / "prepared" / (tenant + "-" + lane + ".json"), prepared)
    return prepared


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selection", type=Path, required=True)
    parser.add_argument("--selection-sha256", required=True)
    args = parser.parse_args()
    print(json.dumps(prepare(args.selection.resolve(strict=True), args.selection_sha256), indent=2))
