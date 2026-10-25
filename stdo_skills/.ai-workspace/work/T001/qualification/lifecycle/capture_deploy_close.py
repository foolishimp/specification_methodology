"""Capture only the selected read-only close; no dispatch or workspace effect.

The control Product owns control/OWNER.json. The previous workspace owner stays
an unchanged historical file, so this bounded collector does not apply the
general collector's product-owner replacement assumption.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil

Q = Path(__file__).resolve().parent.parent
NAME = "claude-release-deploy-repair-2-close"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as stream:
        json.dump(value, stream, indent=2, sort_keys=True)
        stream.write("\n")


def main():
    prepared = json.loads((Q / "prepared" / (NAME + ".json")).read_text())
    control, workspace = Path(prepared["control"]), Path(prepared["workspace"])
    process = json.loads((control / "actor-output/process.json").read_text())
    if process["returncode"] is None:
        raise ValueError("Native parent not closed; do not capture or retry")
    dest = Q / "results" / NAME
    dest.mkdir(exist_ok=False)
    shutil.copytree(control / "actor-output", dest / "raw")
    for name in ("PREPARED.json", "SELECTION.json", "INSTALL.json", "worker-policy.json", "executive-policy.json", "RETURN-CONTRACT.json", "OWNER.json", "CONTROLLER.json", "TASK.md", "INTENT.md", "PRODUCT.md", "GOALS.md", "launch.json", "actor-plan.json", "mcp.json", "RECONCILIATION.json", "WORKSPACE-BEFORE.json"):
        shutil.copyfile(control / name, dest / name)
    if sha(Q / "prepared" / (NAME + ".json")) != sha(control / "PREPARED.json"):
        shutil.copyfile(Q / "prepared" / (NAME + ".json"), dest / "EXECUTIVE-PREPARED.json")
    for pin in (prepared["workspace_preimage"], prepared["installed"], prepared["policy"]):
        if sha(Path(pin["path"])) != pin["sha256"]:
            raise ValueError("Frozen input changed; retained partial capture")
    before = {r["path"]: r["sha256"] for r in json.loads((control / "WORKSPACE-BEFORE.json").read_text())["files"]}
    after, links = {}, []
    for path in sorted(workspace.rglob("*")):
        if path.is_symlink(): links.append(str(path.relative_to(workspace)))
        elif path.is_file(): after[str(path.relative_to(workspace))] = sha(path)
    policy = json.loads((control / "executive-policy.json").read_text())
    owner = policy["product"]["authority_binding"]["owner_record"]
    if owner["root"] != "control" or owner["path"] != "OWNER.json":
        raise ValueError("This collector is specific to the selected control Product")
    files, calls, final, usage, initialized, parse_errors = [], {}, [], [], [], []
    for number, line in enumerate((dest / "raw/vendor.stdout").read_text().splitlines(), 1):
        try: event = json.loads(line)
        except ValueError:
            parse_errors.append(number)
            continue
        if event.get("type") == "system" and event.get("subtype") == "init":
            initialized.append({"line": number, "session_id": event.get("session_id"), "model": event.get("model"), "tools": event.get("tools"), "claude_code_version": event.get("claude_code_version")})
        if event.get("type") == "result":
            final.append({"line": number, "text": event.get("result"), "subtype": event.get("subtype"), "is_error": event.get("is_error")})
            usage.append({"line": number, "usage": event.get("usage"), "modelUsage": event.get("modelUsage"), "reported_cost_usd": event.get("total_cost_usd")})
        content = event.get("message", {}).get("content", [])
        for block in content if isinstance(content, list) else []:
            if not isinstance(block, dict): continue
            if block.get("type") == "tool_use":
                calls[block["id"]] = {"line": number, "id": block["id"], "name": block.get("name"), "input": block.get("input"), "result_line": None}
            elif block.get("type") == "tool_result" and block.get("tool_use_id") in calls:
                calls[block["tool_use_id"]].update({"result_line": number, "is_error": block.get("is_error", False)})
    (dest / "public-evidence").mkdir()
    host_operations, mismatches = [], []
    for source in sorted((control / "evidence/objects").glob("*.json")):
        if sha(source) != source.stem: mismatches.append(source.stem)
        shutil.copyfile(source, dest / "public-evidence" / source.name)
        data = json.loads(source.read_text())
        if data.get("kind") == "operation" and data.get("provenance", {}).get("requester_principal") == "host":
            payload = data["payload"]
            host_operations.append({"evidence": source.stem, "request": payload["request"], "response_without_evidence": payload["response_without_evidence"]})
    for name in ("deploy-test/payload.txt", "deploy-test/manifest.json", "outputs/deployment.md", "retained/SOURCE.json"):
        target = dest / "current-artifacts" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(workspace / name, target)
    census = {"schema": "stdo_skills.readonly-close-census/1", "custody": "Exact native capture and public control evidence; historical source roots remain explicit, no grant rebasing", "native_process": process, "native_initialization": initialized, "native_tool_calls": list(calls.values()), "unmatched_tool_calls": [r for r in calls.values() if r["result_line"] is None], "jsonl_parse_errors": parse_errors, "final_messages": final, "usage_events": usage, "host_operations": host_operations, "public_object_digest_mismatches": mismatches, "workspace": {"before": before, "after": after, "changed": sorted(p for p in set(before) & set(after) if before[p] != after[p]), "added": sorted(set(after)-set(before)), "missing": sorted(set(before)-set(after)), "symlinks": links}, "owner_attribution": {"current_controller": owner, "historical_workspace_owner_sha256": before[".qualification/OWNER.json"], "replacement_applied": False}, "install_checks": {"new_checks": "not performed; no reinstall/update selected", "prior_installation": prepared["installed"]}, "assessment": "Source-derived read-only continuation assessment remains separate; prior timeout is not rewritten"}
    save(dest / "CENSUS.json", census)
    for path in sorted(dest.rglob("*")):
        if path.is_file(): files.append({"path": str(path.relative_to(dest)), "sha256": sha(path)})
    save(dest / "INVENTORY.json", {"schema": "stdo_skills.readonly-close-inventory/1", "files": files})
    print(json.dumps({"result": str(dest), "inventory_sha256": sha(dest / "INVENTORY.json"), "returncode": process["returncode"], "final_results": len(final), "changed": census["workspace"]["changed"]}, indent=2))


if __name__ == "__main__":
    main()
