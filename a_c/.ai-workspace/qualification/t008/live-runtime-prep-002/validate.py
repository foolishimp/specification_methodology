"""Read-only preparation inspection; no public operation, receipt or actor."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import stat
import sys

BASE = Path(__file__).resolve().parent
PRODUCT = BASE.parents[3]
TENANT = PRODUCT / "build_tenants/graphify"
sys.path.insert(0, str(TENANT / "code"))
sys.path.insert(0, str(TENANT / "examples/fd-support"))
import ac_support_core as core
import actor_cli


def read(name: str) -> dict:
    return json.loads((BASE / name).read_bytes())


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    config = read("CONFIGURATION.json")
    worker_path = BASE / config["worker_tool_policy"]["path"]
    root_path = BASE / config["executive_policy"]["path"]
    worker = core.Runtime.from_policy(worker_path, config["worker_tool_policy"]["sha256"], "claude-worker-001")
    root = core.Runtime.from_policy(root_path, config["executive_policy"]["sha256"], "/root")
    for key in ["product", "method_profile", "principals", "grants", "event_sinks", "evidence_root"]:
        assert worker.policy[key] == root.policy[key], key
    assert worker.policy["executors"] == {}
    assert "work.write" not in root.principal["operations"]
    assert not any(name.startswith("dispatch.") for name in worker.principal["operations"])
    request = read("context.assemble.request.json")
    core.validate_request(request)
    core.validate_content(read("worker-return-contract.json"), "ReturnContract")
    # This is the selected core's pure preparation verifier, not an actor path,
    # semantic admission or a substitute for the later public CLI operations.
    target, _ = core._validate_packet(root, request["arguments"]["packet"])
    assert target == "claude-worker-001"
    assert request["arguments"]["envelope"]["capacity_bytes"] is None
    assert request["arguments"]["envelope"]["host_context"] == {"state": "unknown", "bytes": None, "evidence": None}
    plan = actor_cli.load_plan(BASE / "worker-actor-plan.json", config["helper_plan"]["sha256"])
    assert plan.document["decoder"] == "claude-result-jsonl/1"
    native_argv = plan.document["argv"]
    assert native_argv[native_argv.index("--permission-mode") + 1] == "dontAsk"
    assert native_argv[native_argv.index("--permission-prompts") + 1] == "none"
    assert native_argv.count("--permission-mode") == native_argv.count("--permission-prompts") == 1
    assert "--tools=" in native_argv
    assert plan.document["argv"][-1] == (BASE / "system-instructions.txt").read_text()
    assert not any(name in plan.document["environment"] for name in ["HOME", "home", "CODEX_HOME"])
    for forbidden in ["--bare", "--restricted", "--safe-mode", "--json-schema", "--model", "--settings", "--dangerously-skip-permissions"]:
        assert forbidden not in plan.document["argv"], forbidden
    cwd = Path(plan.document["cwd"])
    assert cwd == cwd.resolve(strict=True) and not cwd.is_relative_to(PRODUCT.parent)
    assert not list(cwd.iterdir())
    executor = root.policy["executors"]["claude-worker-001"]
    assert executor["cwd"] == str(cwd) and executor["argv"][-1] == config["helper_plan"]["sha256"]
    for source in executor["dependencies"]:
        core.read_source(root, source)
    for scope in read("root-observation-scope.json")["scope"]:
        core.source_path(root, {"engine": "workspace-regular-file", "root": scope["root"], "path": scope["path"]})
    target_path = TENANT / "examples/fd-support/LIFECYCLE_QUICKSTART.md"
    assert not target_path.exists() and not target_path.is_symlink()
    marker = read("source-index.json")["target_absent"]
    assert core.source_path(worker, marker, write=True, allow_absent=True) == target_path
    mcp = read("worker.mcp.json")["mcpServers"]
    assert list(mcp) == ["ac"]
    assert mcp["ac"]["args"][mcp["ac"]["args"].index("--policy-sha256") + 1] == config["worker_tool_policy"]["sha256"]
    for name, value in read("ENVIRONMENT.selected.json")["protected_pass_through"].items():
        assert executor["environment"][name] == value
    for name in ["worker-tool-policy.json", "worker.mcp.json", "worker-actor-plan.json", "worker-call.json", "executive-policy.json", "worker-packet.json"]:
        assert stat.S_ISREG((BASE / name).lstat().st_mode)
    print(json.dumps({"state": "pure_preparation_checks_passed", "policies": 2, "same_exact_grant": True, "worker_executors": 0, "selected_executor": "claude-worker-001", "cwd_empty": True, "helper_dependencies_match": True, "target_absent": True, "future_ArtifactRefs": 0, "public_operations_executed": 0, "admissions_created": 0, "actor_model_calls": 0, "qualification": "Pure source/configuration inspection only; actual public initialization/preflight/native compatibility remain separate observations"}, indent=2))


if __name__ == "__main__":
    main()
