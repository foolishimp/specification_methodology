#!/usr/bin/env python3
"""Prepare or execute one fresh isolated CLI actor; never retries a run.

Default is preparation only. --execute performs the already-authorized run.
--smoke substitutes an infrastructure-only prompt with no evaluation tasks.
All configuration overrides are per invocation; global files are read only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import time
import tomllib
from typing import Any

HERE = Path(__file__).resolve().parent
STUDY = HERE.parent
AC_ROOT = STUDY.parents[1]
SETTING_KEYS = ("model", "model_provider", "model_reasoning_effort", "model_reasoning_summary", "model_verbosity", "service_tier")
COMMON_TOOLS = {"info", "list_sources", "search", "read_source", "list_records", "read_record"}
SMOKE_PROMPT = """Infrastructure smoke only. There are no evaluation questions.
Call ac_study.info exactly once to verify the frozen source reader is available.
Use no other tools. Return the required JSON schema with tasks=[] and
limitations=["Infrastructure-only smoke; no evaluation task answered."]
"""


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def write_json(path: Path, value: Any) -> None:
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, sort_keys=True, indent=2)
        stream.write("\n")


def toml_value(value: Any) -> str:
    # JSON literals for this small domain are also TOML basic literals. Passing
    # argv directly avoids shell interpolation entirely.
    if isinstance(value, (str, bool, int, float, list)):
        return json.dumps(value, ensure_ascii=False)
    raise ValueError("unsupported inline configuration value")


def validate(value: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    errors: list[str] = []
    kind = schema.get("type")
    matches = ((kind == "object" and isinstance(value, dict)) or (kind == "array" and isinstance(value, list))
               or (kind == "string" and isinstance(value, str)))
    if not matches:
        return [path + ": expected " + str(kind)]
    if kind == "object":
        properties = schema["properties"]
        if set(value) != set(properties):
            errors.append(path + ": missing or additional fields")
        for key in set(value) & set(properties):
            errors.extend(validate(value[key], properties[key], path + "/" + key))
    elif kind == "array":
        for ordinal, child in enumerate(value):
            errors.extend(validate(child, schema["items"], path + "/" + str(ordinal)))
    return errors


def prepare(args: argparse.Namespace) -> dict[str, Any]:
    config_path = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "config.toml"
    config_raw = config_path.read_bytes()
    config = tomllib.loads(config_raw.decode("utf-8"))
    settings = {key: config[key] for key in SETTING_KEYS if key in config}
    if settings.get("model") != "gpt-6-astra" or settings.get("model_reasoning_effort") != "max":
        raise ValueError("Study requires the existing gpt-6-astra/max settings; no model/settings substitution is permitted.")
    codex = shutil.which(args.codex)
    if codex is None:
        raise ValueError("Codex CLI executable is unavailable")
    version = subprocess.check_output([codex, "--version"], text=True).strip()
    if version.split()[-1] != "0.162.1":
        raise ValueError("Study pins Codex CLI 0.162.1")
    # Desktop-injected MCPs can exist outside config.toml. Discover the effective
    # inventory without starting a model turn, and never persist their env data.
    inventory = json.loads(subprocess.check_output([codex, "mcp", "list", "--json"]))
    mcp_names = set(config.get("mcp_servers", {})) | {row["name"] for row in inventory}
    if args.condition == "graphify" and args.upstream is None:
        raise ValueError("Assisted condition requires --upstream")
    if args.smoke and args.condition != "direct":
        raise ValueError("The authorized infrastructure smoke is direct-only")
    prompt = SMOKE_PROMPT if args.smoke else args.prompt.read_bytes().decode("utf-8")
    output = args.output_dir.absolute()
    output.mkdir(parents=True, exist_ok=False)
    work = output / "empty-workspace"
    work.mkdir()
    (output / "prompt.txt").write_text(prompt, encoding="utf-8")
    server_args = [str(HERE / "study_mcp.py"), "--tenant", args.tenant, "--condition", args.condition,
                   "--baseline", str(args.baseline.resolve(strict=True)), "--log", str(output / "tool-audit.jsonl")]
    if args.upstream:
        server_args += ["--upstream", str(args.upstream.resolve(strict=True))]
    overrides: dict[str, Any] = {**settings,
        "features.shell_tool": False, "features.apps": False, "features.multi_agent": False,
        "features.memories": False, "features.js_repl": False,
        "web_search": "disabled", "project_doc_max_bytes": 0,
        # Preserve the venv executable path: resolving its symlink to the base
        # interpreter would silently discard the qualification environment.
        "mcp_servers.ac_study.command": str(args.python.absolute()),
        "mcp_servers.ac_study.args": server_args,
        "mcp_servers.ac_study.cwd": str(work), "mcp_servers.ac_study.enabled": True,
        "mcp_servers.ac_study.required": True, "mcp_servers.ac_study.startup_timeout_sec": 120,
        "mcp_servers.ac_study.tool_timeout_sec": 180}
    for name in sorted(mcp_names):
        if name != "ac_study":
            # CLI 0.162.1 parses -c key paths itself, so literal quotes create a
            # different key with no transport. Existing names are bare-safe.
            if re.fullmatch(r"[A-Za-z0-9_-]+", name) is None:
                raise ValueError("An existing MCP name cannot be safely disabled with the pinned CLI's inline dotted-key parser.")
            if name not in config.get("mcp_servers", {}):
                # Injected server settings arrive after bootstrap validation.
                # Provide a valid inert transport so the disabling key parses.
                overrides["mcp_servers." + name + ".command"] = "/usr/bin/false"
            overrides["mcp_servers." + name + ".enabled"] = False
    command = [codex, "exec", "--json", "--ephemeral", "--sandbox", "read-only", "--skip-git-repo-check",
               "--color", "never", "--output-schema", str(args.schema.resolve(strict=True)),
               "--output-last-message", str(output / "answer.json"), "--cd", str(work)]
    for key, value in overrides.items():
        command += ["-c", key + "=" + toml_value(value)]
    command.append("-")
    preflight_command = [codex, "mcp", "list", "--json"]
    for key, value in overrides.items():
        preflight_command += ["-c", key + "=" + toml_value(value)]
    effective = json.loads(subprocess.check_output(preflight_command, cwd=work))
    isolation = [{"name": row["name"], "enabled": row["enabled"]} for row in effective]
    if {row["name"] for row in isolation if row["enabled"]} != {"ac_study"}:
        raise ValueError("Effective actor MCP inventory is not isolated to ac_study")
    write_json(output / "mcp-isolation.json", {"profile": "ac.eval.mcp-isolation/1", "effective_servers": isolation,
                                             "scope": "Non-model preflight with the exact inline actor overrides; no server tools/model turn invoked."})
    invocation = {"profile": "ac.eval.actor-invocation/1", "run_id": args.run_id, "tenant": args.tenant,
                  "condition": args.condition, "infrastructure_smoke": args.smoke,
                  "cli_version": version, "command": command, "cwd": str(work),
                  "settings": settings, "inline_overrides": overrides,
                  "effective_mcp_inventory": isolation,
                  "user_config_sha256": sha(config_raw), "user_config_path": str(config_path),
                  "prompt_sha256": sha(prompt.encode()), "schema_sha256": sha(args.schema.read_bytes()),
                  "baseline_manifest_sha256": sha((args.baseline / "manifest.json").read_bytes()),
                  "runner_sha256": sha(Path(__file__).read_bytes()), "server_sha256": sha((HERE / "study_mcp.py").read_bytes()),
                  "timeout_seconds": args.timeout, "executed": args.execute,
                  "documentation": ["https://learn.chatgpt.com/docs/extend/mcp?surface=cli",
                                    "https://learn.chatgpt.com/docs/config-file/config-reference"],
                  "local_help_basis": "codex exec --help (0.162.1); no global configuration mutation"}
    write_json(output / "invocation.json", invocation)
    return {"invocation": invocation, "prompt": prompt, "output": output, "config_path": config_path}


def execute(prepared: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    invocation, output = prepared["invocation"], prepared["output"]
    started = time.perf_counter()
    timeout = False
    with (output / "events.jsonl").open("xb") as stdout, (output / "stderr.txt").open("xb") as stderr:
        process = subprocess.Popen(invocation["command"], stdin=subprocess.PIPE, stdout=stdout, stderr=stderr,
                                   cwd=invocation["cwd"], start_new_session=True)
        try:
            process.communicate(prepared["prompt"].encode(), timeout=args.timeout)
        except subprocess.TimeoutExpired:
            timeout = True
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.communicate(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.communicate()
    elapsed = time.perf_counter() - started
    errors: list[str] = []
    if timeout:
        errors.append("process_timeout")
    if process.returncode != 0:
        errors.append("cli_nonzero_exit")
    events, invalid_json_lines = [], 0
    for line in (output / "events.jsonl").read_text(encoding="utf-8").splitlines():
        try:
            events.append(json.loads(line))
        except ValueError:
            invalid_json_lines += 1
    usage = [event["usage"] for event in events if event.get("type") == "turn.completed" and "usage" in event]
    if not usage and process.returncode == 0:
        errors.append("missing_backend_usage")
    write_json(output / "usage.json", {"profile": "ac.eval.backend-usage/1", "run_id": args.run_id,
                                       "usage_events": usage, "scope": "Exact CLI-reported usage fields; no inferred price or billing discount."})
    tools = [event["item"] for event in events if event.get("type") in ("item.started", "item.completed")
             and isinstance(event.get("item"), dict) and event["item"].get("type") == "mcp_tool_call"]
    disallowed = [item for item in tools if item.get("server") != "ac_study"
                  or item.get("tool") not in COMMON_TOOLS | ({"graph_query", "graph_select"} if args.condition == "graphify" else set())]
    nonstudy_items = [event["item"].get("type") for event in events if event.get("type") == "item.completed"
                      and isinstance(event.get("item"), dict) and event["item"].get("type") in ("command_execution", "web_search", "collab_tool_call")]
    if disallowed or nonstudy_items:
        errors.append("isolation_violation")
    schema_errors = []
    answer = None
    try:
        answer = json.loads((output / "answer.json").read_bytes())
        schema_errors = validate(answer, json.loads(args.schema.read_bytes()))
    except (OSError, ValueError):
        schema_errors = ["missing_or_invalid_json_answer"]
    if schema_errors:
        errors.append("output_schema_failure")
    audit = []
    if (output / "tool-audit.jsonl").exists():
        audit = [json.loads(line) for line in (output / "tool-audit.jsonl").read_text().splitlines()]
    calls = [row for row in audit if row["event"] == "tool_call"]
    content_bytes = sum(row["emitted_utf8_bytes"] for row in calls)
    if len(calls) > 24 or content_bytes > 160_000:
        errors.append("resource_envelope_violation")
    if not audit:
        errors.append("missing_mcp_audit")
    if args.smoke and (len(calls) != 1 or calls[0]["tool"] != "info" or answer is None or answer.get("tasks") != []):
        errors.append("smoke_contract_failure")
    config_unchanged = sha(prepared["config_path"].read_bytes()) == invocation["user_config_sha256"]
    if not config_unchanged:
        errors.append("user_config_changed_during_run")
    summary = {"profile": "ac.eval.actor-result/1", "run_id": args.run_id,
               "status": "completed" if not errors else "failed", "errors": errors,
               "cli_exit_code": process.returncode, "timed_out": timeout, "elapsed_seconds": elapsed,
               "cli_version": invocation["cli_version"], "settings": invocation["settings"],
               "user_config_unchanged": config_unchanged, "usage_events": usage,
               "schema_errors": schema_errors, "invalid_stdout_json_lines": invalid_json_lines,
               "tool_calls_attempted": len(calls), "content_utf8_bytes": content_bytes,
               "wire_utf8_bytes": sum(row.get("emitted_wire_utf8_bytes", 0) for row in audit if row["event"] == "protocol_output"),
               "graph_startup_seconds": sum(row["duration_seconds"] for row in audit if row["event"] == "graph_startup"),
               "source_text_utf8_bytes": sum(row.get("source_bytes_emitted", 0) for row in calls),
               "pending_read_refusals": sum(row.get("code") in ("narrow_read_required", "content_budget_exhausted") for row in calls),
               "graph_uptake": any(row["tool"] in ("graph_query", "graph_select") for row in calls),
               "isolation_violations": {"unexpected_mcp_items": disallowed, "unexpected_completed_item_types": nonstudy_items},
               "stdout_sha256": sha((output / "events.jsonl").read_bytes()),
               "stderr_sha256": sha((output / "stderr.txt").read_bytes()),
               "answer_sha256": sha((output / "answer.json").read_bytes()) if (output / "answer.json").exists() else None}
    write_json(output / "summary.json", summary)
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--tenant", choices=("codex", "claude"), required=True)
    parser.add_argument("--condition", choices=("direct", "graphify"), required=True)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--upstream", type=Path)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--prompt", type=Path)
    group.add_argument("--smoke", action="store_true")
    parser.add_argument("--python", type=Path, default=AC_ROOT / ".venv/bin/python")
    parser.add_argument("--codex", default="codex")
    parser.add_argument("--schema", type=Path, default=STUDY / "output.schema.json")
    parser.add_argument("--timeout", type=int, default=720)
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args(argv)
    if not 1 <= args.timeout <= 720:
        parser.error("--timeout must be from 1 to 720 seconds")
    prepared = prepare(args)
    summary = execute(prepared, args) if args.execute else {"status": "prepared_only", "run_id": args.run_id}
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True, indent=2))
    return 0 if summary["status"] in ("completed", "prepared_only") else 1


if __name__ == "__main__":
    raise SystemExit(main())
