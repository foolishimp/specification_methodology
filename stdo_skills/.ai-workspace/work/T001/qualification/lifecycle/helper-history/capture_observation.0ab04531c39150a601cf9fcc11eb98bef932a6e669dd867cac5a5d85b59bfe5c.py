"""Copy exact completed trial observations and compute a bounded source census.

No host dispatch, source repair, acceptance or generic model-success grader.
Semantic findings remain the named assessor's responsibility.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import shutil

HERE = Path(__file__).resolve().parent


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def artifact_refs(value):
    if isinstance(value, dict):
        if isinstance(value.get("id"), str) and value["id"].startswith("sha256:") and value.get("sha256") == value["id"][7:]:
            yield value["sha256"]
        for item in value.values():
            yield from artifact_refs(item)
    elif isinstance(value, list):
        for item in value:
            yield from artifact_refs(item)


def capture(prepared_path: Path, native_transcript: Path | None = None) -> dict:
    prepared = json.loads(prepared_path.read_text())
    control, workspace = Path(prepared["control"]), Path(prepared["workspace"])
    process = json.loads((control / "actor-output/process.json").read_text())
    if process["returncode"] is None:
        raise ValueError("The observed native parent is not closed")
    name = prepared["tenant"] + "-" + prepared["lane"]
    destination = HERE / "results" / name
    destination.mkdir(parents=True, exist_ok=False)
    (destination / "raw").mkdir()
    for source in sorted((control / "actor-output").iterdir()):
        if source.is_file():
            shutil.copyfile(source, destination / "raw" / source.name)
    for filename in ("PREPARED.json", "SELECTION.json", "INSTALL.json", "worker-policy.json", "executive-policy.json", "RETURN-CONTRACT.json", "OWNER.json", "TASK.md", "launch.json", "actor-plan.json", "mcp.json"):
        shutil.copyfile(prepared_path if filename == "PREPARED.json" else control / filename, destination / filename)
    if sha(prepared_path) != sha(control / "PREPARED.json"):
        shutil.copyfile(control / "PREPARED.json", destination / "PRELIMINARY-PREPARED.json")
    shutil.copytree(control / "install-checks", destination / "install-checks")
    objects = control / "evidence/objects"
    selected = {}
    operations = []
    for source in objects.glob("*.json"):
        value = json.loads(source.read_text())
        if value.get("kind") == "operation" and value.get("provenance", {}).get("requester_principal") == "host":
            selected[source.stem] = value
            payload = value["payload"]
            request, response = payload["request"], payload["response_without_evidence"]
            operations.append({"artifact": source.stem, "operation": request["operation"], "request_id": request["id"],
                               "arguments": request["arguments"], "status": response["status"],
                               "refusal": response["refusal"], "operation_outcome": response["operation_outcome"],
                               "started_ns": payload["interval"]["started_ns"]})
    queue = list(selected)
    missing = []
    while queue:
        for digest in artifact_refs(selected[queue.pop()]):
            if digest in selected:
                continue
            path = objects / (digest + ".json")
            if not path.is_file():
                missing.append(digest)
                continue
            selected[digest] = json.loads(path.read_text())
            queue.append(digest)
    (destination / "public-evidence").mkdir()
    mismatched = []
    for digest in sorted(selected):
        source = objects / (digest + ".json")
        if sha(source) != digest:
            mismatched.append(digest)
        shutil.copyfile(source, destination / "public-evidence" / source.name)
    operations.sort(key=lambda row: row["started_ns"])
    events = []
    parse_errors = []
    for line, raw in enumerate((destination / "raw/vendor.stdout").read_text().splitlines(), 1):
        try:
            events.append((line, json.loads(raw)))
        except json.JSONDecodeError:
            parse_errors.append(line)
    commands, failures, messages, usage, models, skill_reads = [], [], [], [], [], []
    installed = json.loads((control / "INSTALL.json").read_text())
    skill_paths = [row["path"] for row in installed["files"] if row["path"].endswith("SKILL.md")]
    skill_texts = {path: (workspace / path).read_text() for path in skill_paths}
    skill_bodies = {path: re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S).strip() for path, text in skill_texts.items()}
    native_calls = {}
    initialized = []
    for line, event in events:
        item = event.get("item", {})
        if event.get("type") == "item.completed" and item.get("type") == "command_execution":
            command = {"line": line, "id": item.get("id"), "command": item.get("command"), "exit_code": item.get("exit_code")}
            commands.append(command)
            for path, text in skill_texts.items():
                if path in str(item.get("command", "")):
                    skill_reads.append({**command, "installed_path": path, "installed_sha256": sha(workspace / path), "complete_selected_body_in_observed_output": text in str(item.get("aggregated_output", ""))})
        if event.get("type") == "item.completed" and item.get("type") == "mcp_tool_call":
            if item.get("error") is not None or item.get("status") not in (None, "completed"):
                failures.append({"line": line, "item": item})
        if event.get("type") == "item.completed" and item.get("type") == "agent_message":
            messages.append({"line": line, "text": item.get("text")})
        if event.get("usage") is not None:
            usage.append({"line": line, "event": event.get("type"), "reported_usage": event["usage"], "reported_cost_usd": event.get("total_cost_usd")})
        if event.get("type") in ("system", "result", "turn.started", "turn.completed") and event.get("model") is not None:
            models.append({"line": line, "event": event.get("type"), "model": event["model"]})
        if event.get("type") == "system" and event.get("subtype") == "init":
            initialized.append({"line": line, "session_id": event.get("session_id"), "tools": event.get("tools"), "skills": event.get("skills"), "model": event.get("model"), "host_version": event.get("claude_code_version")})
        if event.get("message", {}).get("model") is not None:
            models.append({"line": line, "event": event.get("type"), "model": event["message"]["model"]})
        if event.get("type") in ("assistant", "user"):
            content = event.get("message", {}).get("content", [])
            blocks = [{"type": "text", "text": content}] if isinstance(content, str) else content
            text = "\n".join(b.get("text", "") for b in blocks if isinstance(b, dict))
            if event.get("type") == "user":
                for path, body in skill_bodies.items():
                    if body and body in text:
                        skill_reads.append({"line": line, "mechanism": "native skill-body delivery", "installed_path": path, "installed_sha256": sha(workspace / path), "complete_selected_body_in_observed_output": True})
            for block in blocks:
                if not isinstance(block, dict):
                    continue
                if block.get("type") == "tool_use":
                    native_calls[block["id"]] = {"line": line, "id": block["id"], "name": block.get("name"), "input": block.get("input"), "result_line": None, "is_error": None}
                if block.get("type") == "tool_result":
                    call = native_calls.get(block.get("tool_use_id"))
                    if call:
                        call.update({"result_line": line, "is_error": block.get("is_error", False)})
                        if call["name"] == "Bash":
                            commands.append({"line": call["line"], "result_line": line, "id": call["id"], "command": call["input"].get("command"), "exit_code": None, "native_tool_is_error": block.get("is_error", False)})
                        if block.get("is_error"):
                            failures.append({"line": line, "call": dict(call), "native_result": block.get("content")})
        if event.get("type") == "result" and event.get("result") is not None:
            messages.append({"line": line, "text": event["result"]})
            if event.get("modelUsage"):
                models.append({"line": line, "event": "result.modelUsage", "models": event["modelUsage"]})
    if native_transcript is not None:
        session_ids = {x["session_id"] for x in initialized}
        if native_transcript.stem not in session_ids:
            raise ValueError("Native transcript does not match the observed host session")
        delivery = []
        for line, raw in enumerate(native_transcript.read_text().splitlines(), 1):
            event = json.loads(raw)
            if event.get("type") != "user":
                continue
            content = event.get("message", {}).get("content", [])
            text = content if isinstance(content, str) else "\n".join(b.get("text", "") for b in content if isinstance(b, dict))
            for path, body in skill_bodies.items():
                if body and body in text:
                    delivery.append({"line": line, "raw_record": event, "installed_path": path, "installed_sha256": sha(workspace / path)})
                    skill_reads.append({"native_transcript_line": line, "mechanism": "native slash-command expansion", "installed_path": path, "installed_sha256": sha(workspace / path), "complete_selected_body_in_observed_output": True})
        (destination / "raw/native-input-delivery.json").write_text(json.dumps({"source_path": str(native_transcript), "source_sha256": sha(native_transcript), "observed_session_ids": sorted(session_ids), "deliveries": delivery}, indent=2) + "\n")
    expected = {}
    if prepared.get("workspace_preimage"):
        baseline = Path(prepared["workspace_preimage"]["path"])
        if sha(baseline) != prepared["workspace_preimage"]["sha256"]:
            raise ValueError("Frozen pre-run workspace inventory changed")
        shutil.copyfile(baseline, destination / "WORKSPACE-BEFORE.json")
        expected.update({row["path"]: row["sha256"] for row in json.loads(baseline.read_text())["files"]})
    else:
        source_prefix = "unrelated/" if prepared["lane"] == "unrelated" else "governed/"
        for row in json.loads((HERE / "INPUTS-v3.json").read_text())["files"]:
            if row["path"].startswith(source_prefix):
                expected[row["path"][len(source_prefix):]] = row["sha256"]
    expected.update({row["path"]: row["sha256"] for row in installed["files"]})
    policy = json.loads((control / "executive-policy.json").read_text())
    if prepared["lane"] != "unrelated":
        expected[".qualification/OWNER.json"] = policy["product"]["authority_binding"]["owner_record"]["sha256"]
        context = json.loads((objects / (prepared["context"]["sha256"] + ".json")).read_text())["payload"]
        for ref in context["packet"]["subject_basis"]["dependencies"]:
            if ref.get("root") == "product" and ref["path"] == "TOOLING.md":
                expected["TOOLING.md"] = ref["sha256"]
    actual = {}
    symlinks = []
    for path in sorted(workspace.rglob("*")):
        if path.is_symlink():
            symlinks.append(str(path.relative_to(workspace)))
        elif path.is_file():
            actual[str(path.relative_to(workspace))] = sha(path)
    changed = sorted(path for path in set(expected) & set(actual) if expected[path] != actual[path])
    (destination / "postimages").mkdir()
    for path in set(changed) | {"unrelated/sentinel.txt"}:
        source = workspace / path
        if source.is_file():
            target = destination / "postimages" / path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
    report = {
        "schema": "stdo_skills.qualification-census/1", "tenant": prepared["tenant"], "lane": prepared["lane"],
        "original_workspace": str(workspace), "original_control": str(control),
        "custody": "Exact observations copied; absolute runtime policies are not rebased or advertised as portable executable grants",
        "native_process": process, "declared_settings": json.loads((control / "actor-plan.json").read_text())["settings"],
        "actual_model_observations": models, "model_limit": "Absent native model observations stay unknown; configured aliases are not treated as resolved backend identities",
        "usage_events": usage, "usage_limit": "Exact native usage observations, no inferred monetary cost or hidden retry estimate",
        "commands": commands, "completed_commands": len(commands), "tool_failures": failures, "skill_acquisitions": skill_reads,
        "final_messages": messages, "jsonl_parse_errors": parse_errors,
        "public_operation_counts": dict(Counter(row["operation"] for row in operations)), "public_operations": operations,
        "public_artifact_closure": {"copied": len(selected), "missing": sorted(set(missing)), "digest_mismatches": mismatched},
        "native_initialization": initialized,
        "native_tool_calls": list(native_calls.values()),
        "workspace": {"before": expected, "after": actual, "changed": changed, "added": sorted(set(actual)-set(expected)), "missing": sorted(set(expected)-set(actual)), "symlinks": symlinks},
        "assessment": "Finite source census; a named source-oracle assessor judges the observed path and outcomes separately",
    }
    (destination / "CENSUS.json").write_text(json.dumps(report, indent=2) + "\n")
    inventory = [{"path": str(path.relative_to(destination)), "sha256": sha(path), "bytes": path.stat().st_size} for path in sorted(destination.rglob("*")) if path.is_file()]
    (destination / "INVENTORY.json").write_text(json.dumps({"files": inventory}, indent=2) + "\n")
    return {"path": str(destination), "inventory_sha256": sha(destination / "INVENTORY.json"), "public_operations": report["public_operation_counts"], "commands": len(commands), "changes": report["workspace"]["changed"], "added": report["workspace"]["added"], "missing": report["workspace"]["missing"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepared", required=True, type=Path)
    parser.add_argument("--native-transcript", type=Path)
    args = parser.parse_args()
    print(json.dumps(capture(args.prepared, args.native_transcript), indent=2))
