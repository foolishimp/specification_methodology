#!/usr/bin/env python3
"""One fresh repair005 current-design assessment; work evidence, not a method engine."""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()

def verify() -> dict:
    plan = json.loads((ROOT / "LAUNCH_PLAN.json").read_text())
    pairs = [("review_prompt.txt", "stdin_sha256"),
             ("system_prompt.txt", "system_sha256"),
             ("SOURCE_MANIFEST.json", "source_manifest_sha256"),
             ("SOURCE_SELECTION.json", "source_selection_sha256"),
             ("DRAFT_ASSURANCE_WRITER_ACTIVATION.json", "contract_sha256"),
             ("EXTERNAL_BOOTSTRAP_ADMISSION.json", "external_admission_sha256"),
             ("CLI_FLAG_CHECK.json", "cli_flag_check_sha256"),
             ("ACTION_AND_EXTERNAL_BINDINGS.json", "action_binding_sha256"),
             ("EXTERNAL_WORK_AUTHORITY.md", "authority_excerpt_sha256"),
             ("VERIFIED_CUSTODY_OBSERVATIONS.json", "custody_observations_sha256"),
             ("CLAUDE_EXPECTATIONS_V1.txt", "expectations_v1_sha256"),
             ("CLAUDE_EXPECTATIONS_A1.txt", "expectations_A1_sha256"),
             ("REVIEW_ACTIVATION_DRAFT.json", "review_activation_sha256"),
             ("CANDIDATE_MANIFEST.json", "candidate_manifest_sha256"),
             ("COMMITTED_PREIMAGE_MANIFEST.json", "preimage_manifest_sha256"),
             ("GOVERNING_SOURCE_DATA.txt", "governing_source_data_sha256"),
             ("PROOF_MANIFEST.json", "proof_manifest_sha256"),
             ("REVIEW_PAYLOAD_MANIFEST.json", "review_payload_manifest_sha256"),
             ("PRIOR_PACKET_PRESERVATION_HASHES.json", "prior_packet_preservation_sha256"),
             ("PRESERVATION_INVENTORY_PROJECTION.json", "preservation_projection_sha256"),
             ("SOURCE_ADDITIONS_MANIFEST.json", "source_additions_manifest_sha256"),
             ("SOURCE_ADDITIONS.txt", "source_additions_sha256")]
    for filename, key in pairs:
        if sha(ROOT / filename) != plan[key]:
            raise ValueError("Frozen input mismatch: " + filename)
    manifest = json.loads((ROOT / "SOURCE_MANIFEST.json").read_text())
    for entry in manifest["entries"]:
        source = Path(plan["source_copy_root"]) / entry["packet_path"]
        if sha(source) != entry["sha256"] or source.stat().st_size != entry["bytes"]:
            raise ValueError("Source packet changed: " + entry["packet_path"])
    candidate = json.loads((ROOT / "CANDIDATE_MANIFEST.json").read_text())
    for entry in candidate["identity"]["files"]:
        path = ROOT / entry["packet_path"]
        if sha(path) != entry["sha256"] or path.stat().st_size != entry["bytes"]:
            raise ValueError("Frozen candidate changed: " + entry["source_path"])
    for entry in json.loads((ROOT / "COMMITTED_PREIMAGE_MANIFEST.json").read_text())["entries"]:
        if entry["state"] == "present" and sha(ROOT / entry["packet_path"]) != entry["sha256"]:
            raise ValueError("Committed preimage changed: " + entry["source_path"])
    proof = json.loads((ROOT / "PROOF_MANIFEST.json").read_text())
    for entry in proof["entries"]:
        path = ROOT / entry["packet_path"]
        if sha(path) != entry["sha256"] or path.stat().st_size != entry["bytes"]:
            raise ValueError("Frozen proof changed: " + entry["packet_path"])
    payload = json.loads((ROOT / "REVIEW_PAYLOAD_MANIFEST.json").read_text())
    for entry in payload["components"]:
        path = ROOT / entry["packet_path"]
        if sha(path) != entry["sha256"] or path.stat().st_size != entry["bytes"]:
            raise ValueError("Model DATA component changed: " + entry["packet_path"])
    protected = json.loads((ROOT / "PRIOR_PACKET_PRESERVATION_HASHES.json").read_text())
    for packet_path, expected_hash in protected.items():
        if sha(ROOT.parent / packet_path) != expected_hash:
            raise ValueError("Protected prior packet changed: " + packet_path)
    additions = json.loads((ROOT / "SOURCE_ADDITIONS_MANIFEST.json").read_text())
    for entry in additions["entries"]:
        path = Path(entry["packet_path"])
        if not path.is_absolute():
            path = ROOT / path
        if sha(path) != entry["sha256"] or path.stat().st_size != entry["bytes"]:
            raise ValueError("Source availability addition changed: " + entry["member"])
    exe = Path(plan["executable"])
    if str(exe.resolve(strict=True)) != plan["executable_realpath"] or sha(exe.resolve()) != plan["executable_sha256"]:
        raise ValueError("Claude executable changed")
    system = (ROOT / "system_prompt.txt").read_text()
    expected = [str(exe), "--print", "--safe-mode", "--restricted", "--tools", "",
                "--disable-slash-commands", "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
                "--no-session-persistence", "--no-chrome", "--permission-mode", "dontAsk",
                "--permission-prompts", "none", "--output-format", "stream-json", "--verbose",
                "--system-prompt", system]
    if plan["argv"] != expected:
        raise ValueError("Launch argv differs from fixed isolated configured-CLI contract")
    if plan["stdin_sha256"] != "0c6e23910d3cf31ecd58c1fb332063ad19847cb57441a74e7f7405ac26eb4e9d":
        raise ValueError("Final-design prompt differs from exact prepared input")
    if plan["calls"] != 1 or plan["automatic_retries"] != 0 or plan["process_wall_limit_seconds"] > 1200:
        raise ValueError("Unapproved call/resource bound")
    return plan

def run(plan: dict) -> int:
    approval_path = ROOT / plan["required_final_approval_file"]
    if not approval_path.is_file():
        raise ValueError("Final Executive prelaunch check is absent; no model call")
    approval = json.loads(approval_path.read_text())
    required = {"launcher_sha256": sha(Path(__file__)),
                "launch_plan_sha256": sha(ROOT / "LAUNCH_PLAN.json"),
                "system_sha256": plan["system_sha256"],
                "prompt_sha256": plan["stdin_sha256"],
                "contract_sha256": plan["contract_sha256"],
                "action_binding_sha256": plan["action_binding_sha256"],
                "review_activation_sha256": plan["review_activation_sha256"],
                "candidate_manifest_sha256": plan["candidate_manifest_sha256"],
                "proof_manifest_sha256": plan["proof_manifest_sha256"],
                "review_payload_manifest_sha256": plan["review_payload_manifest_sha256"]}
    if approval.get("producer") != "/root Executive" or approval.get("decision") != plan["required_approval_decision"]:
        raise ValueError("Final approval producer/decision mismatch")
    for key, value in required.items():
        if approval.get(key) != value:
            raise ValueError("Final approval mismatch: " + key)
    attempt = ROOT / plan["attempt_directory"]
    attempt.mkdir(parents=True, exist_ok=False)
    workdir = Path(tempfile.mkdtemp(prefix="ac_t008_repair005_review_"))
    initial_files = sorted(p.name for p in workdir.iterdir())
    if initial_files:
        raise ValueError("Review workspace is not empty")
    started = time.monotonic()
    record = {"kind": "raw-repair005-design-model-assessment-attempt", "started_utc": now(),
              "executable": plan["executable"], "executable_realpath": plan["executable_realpath"],
              "executable_sha256": plan["executable_sha256"], "version": plan["version"],
              "argv": plan["argv"], "prompt_sha256": plan["stdin_sha256"],
              "system_sha256": plan["system_sha256"], "launch_plan_sha256": required["launch_plan_sha256"],
              "launcher_sha256": required["launcher_sha256"], "approval_sha256": sha(approval_path),
              "working_directory": str(workdir), "initial_workspace_entries": initial_files,
              "candidate_exposure": plan["candidate_exposure"], "signals": [], "timeout": False,
              "model_identity": "unknown until actual events", "backend_usage": "unknown until actual result counters",
              "host_context": "not measured; full active-context fit unclaimed",
              "configured_model_override": False, "provider_or_auth_override": False,
              "inherited_relevant_environment_presence": {key: key in os.environ for key in
                ["ANTHROPIC_API_KEY", "CLAUDE_CODE_OAUTH_TOKEN", "CLAUDE_CODE_USE_BEDROCK", "CLAUDE_CODE_USE_VERTEX", "CLAUDE_CODE_USE_FOUNDRY", "ANTHROPIC_MODEL"]}}
    (attempt / "attempt-start.json").write_text(json.dumps(record, indent=2) + "\n")
    process = None
    failure = None
    try:
        with (ROOT / "review_prompt.txt").open("rb") as prompt, (attempt / "stdout.stream.jsonl").open("wb") as stdout, (attempt / "stderr.txt").open("wb") as stderr:
            process = subprocess.Popen(plan["argv"], stdin=prompt, stdout=stdout, stderr=stderr,
                                       cwd=workdir, start_new_session=True)
            record["pid"] = process.pid
            try:
                process.wait(timeout=max(0, plan["soft_stop_at_seconds"] - (time.monotonic() - started)))
            except subprocess.TimeoutExpired:
                record["timeout"] = True
                record["signals"].append({"signal": "SIGTERM", "requested_utc": now()})
                try:
                    os.killpg(process.pid, signal.SIGTERM)
                except ProcessLookupError:
                    record["signals"][-1]["process_group_already_absent"] = True
                try:
                    process.wait(timeout=plan["terminate_grace_seconds"])
                except subprocess.TimeoutExpired:
                    record["signals"].append({"signal": "SIGKILL", "requested_utc": now()})
                    try:
                        os.killpg(process.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        record["signals"][-1]["process_group_already_absent"] = True
                    process.wait(timeout=plan["kill_grace_seconds"])
    except BaseException as error:
        failure = {"type": type(error).__name__, "message": str(error)}
        if process is not None and process.poll() is None:
            record["signals"].append({"signal": "SIGKILL", "requested_utc": now(), "cause": "launcher exception"})
            try:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait(timeout=5)
            except (ProcessLookupError, subprocess.TimeoutExpired):
                pass
    finally:
        record["ended_utc"] = now()
        record["elapsed_wall_seconds"] = time.monotonic() - started
        record["return_code"] = None if process is None else process.poll()
        record["process_end_observed"] = process is not None and process.poll() is not None
        record["backend_cancellation_or_end"] = "unknown; local process end does not prove backend end"
        record["launcher_exception"] = failure
        record["final_workspace_entries"] = sorted(p.name for p in workdir.iterdir())
        if not record["final_workspace_entries"]:
            workdir.rmdir()
            record["empty_temp_workspace_removed"] = True
        else:
            record["empty_temp_workspace_removed"] = False
            record["temporary_workspace_preserved"] = str(workdir)
        (attempt / "attempt-final.json").write_text(json.dumps(record, indent=2) + "\n")
    events, parse_errors, results, identities, tools, mcp = [], [], [], [], [], []
    for index, line in enumerate((attempt / "stdout.stream.jsonl").read_text(errors="replace").splitlines(), 1):
        try:
            event = json.loads(line)
        except json.JSONDecodeError as error:
            parse_errors.append({"line": index, "error": str(error)})
            continue
        events.append(event)
        if event.get("type") == "system":
            identities.append({key: event.get(key) for key in ["type", "subtype", "model", "claude_code_version", "session_id", "cwd"] if key in event})
            if "tools" in event:
                tools.append(event["tools"])
            if "mcp_servers" in event:
                mcp.append(event["mcp_servers"])
        if event.get("type") == "result":
            results.append(event)
    result_text = "\n\n".join(str(event["result"]) for event in results if "result" in event)
    (attempt / "result.txt").write_text(result_text + ("\n" if result_text else ""))
    producer = {"initial_event_identity": identities,
                "terminal_result_count": len(results),
                "terminal_usage_records": [{key: event.get(key) for key in ["type", "subtype", "is_error", "session_id", "duration_ms", "duration_api_ms", "num_turns", "total_cost_usd", "usage", "modelUsage", "permission_denials"] if key in event} for event in results],
                "actual_model_ids": sorted({str(event["model"]) for event in identities if event.get("model")} | {str(model) for event in results for model in (event.get("modelUsage") or {})}),
                "tools_observed": tools, "mcp_servers_observed": mcp,
                "tools_empty_observed": bool(tools) and all(value == [] for value in tools),
                "mcp_empty_observed": bool(mcp) and all(value == [] for value in mcp),
                "event_parse_errors": parse_errors,
                "no_model_override": True,
                "unknowns": ["Hidden host context and full fit not measured", "Backend end/cancellation not established by local process end", "Absent backend usage counters remain unknown"],
                "standing": "Raw returned assessment and execution metadata only; no automatic acceptance, disposition, independence certification or continuation"}
    (attempt / "producer-usage.json").write_text(json.dumps(producer, indent=2) + "\n")
    hashes = {p.name: sha(p) for p in attempt.iterdir() if p.is_file()}
    (attempt / "EVIDENCE_HASHES.json").write_text(json.dumps(hashes, indent=2) + "\n")
    print(json.dumps({"attempt_directory": str(attempt), "return_code": record["return_code"],
                      "timeout": record["timeout"], "process_end_observed": record["process_end_observed"],
                      "actual_model_ids": producer["actual_model_ids"], "terminal_result_count": len(results),
                      "tools_empty_observed": producer["tools_empty_observed"], "mcp_empty_observed": producer["mcp_empty_observed"],
                      "result_sha256": sha(attempt / "result.txt"), "automatic_retries": 0}, indent=2))
    return 0 if record["return_code"] == 0 and not record["timeout"] and failure is None else 1

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true", help="Run exactly one fresh final-design assessment after exact Executive activation/approval")
    args = parser.parse_args()
    plan = verify()
    if not args.run:
        print(json.dumps({"mode": "preflight_only", "model_calls": 0,
                          "launcher_sha256": sha(Path(__file__)), "launch_plan_sha256": sha(ROOT / "LAUNCH_PLAN.json"),
                          "system_sha256": plan["system_sha256"], "prompt_sha256": plan["stdin_sha256"],
                          "contract_sha256": plan["contract_sha256"], "executable_sha256": plan["executable_sha256"],
                          "candidate_exposure": plan["candidate_exposure"], "source_members_rehashed": len(json.loads((ROOT / "SOURCE_MANIFEST.json").read_text())["entries"]),
                          "candidate_manifest_sha256": plan["candidate_manifest_sha256"],
                          "proof_manifest_sha256": plan["proof_manifest_sha256"],
                          "review_payload_manifest_sha256": plan["review_payload_manifest_sha256"],
                          "proof_files_rehashed": len(json.loads((ROOT / "PROOF_MANIFEST.json").read_text())["entries"]),
                          "protected_prior_files": plan["protected_prior_files"]}, indent=2))
        return 0
    return run(plan)

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(2)
