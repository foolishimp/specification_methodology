#!/usr/bin/env python3
"""Run one fresh read-only task against an exact installed release.

Root supplies the pinned, task-specific activation through stdin. This launcher
records transport and usage, not an assessment or acceptance of the answer.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import time

p = argparse.ArgumentParser()
p.add_argument("--prompt", required=True, type=Path)
p.add_argument("--prompt-sha256", required=True)
p.add_argument("--release-root", required=True, type=Path)
p.add_argument("--output", required=True, type=Path)
a = p.parse_args()
prompt = a.prompt.read_bytes()
if hashlib.sha256(prompt).hexdigest() != a.prompt_sha256:
    raise SystemExit("activation bytes changed")
root = a.release_root.resolve(strict=True)
if not (root / "standards/README.md").is_file():
    raise SystemExit("installed entry missing")
out = a.output.resolve()
out.mkdir(parents=True, exist_ok=False)
cmd = [
    "/Users/jim/.local/bin/claude", "-p", "--safe-mode", "--restricted",
    "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
    "--setting-sources", "", "--tools", "Read,Glob,Grep",
    "--allowedTools", "Read,Glob,Grep", "--no-session-persistence",
    "--disable-slash-commands", "--no-chrome", "--permission-prompts", "none",
    "--model", "claude-opus-5-5", "--effort", "xhigh",
    "--max-budget-usd", "10", "--output-format", "stream-json", "--verbose",
]
invocation = {
    "argv": cmd, "cwd": str(root), "prompt_sha256": a.prompt_sha256,
    "timeout_seconds": 900, "max_budget_usd": 10,
    "capability": "Read,Glob,Grep confined to installed cwd; no MCP or shell",
    "freshness": "safe mode, no persistence, no resume, no automatic CLAUDE.md",
}
(out / "invocation.json").write_text(json.dumps(invocation, indent=2) + "\n")
start = time.monotonic()
timed_out = False
with (out / "events.jsonl").open("xb") as stdout, (out / "stderr.txt").open("xb") as stderr:
    proc = subprocess.Popen(cmd, cwd=root, stdin=subprocess.PIPE, stdout=stdout,
                            stderr=stderr, start_new_session=True)
    print(json.dumps({"started_pid": proc.pid, "output": str(out)}), flush=True)
    try:
        proc.communicate(prompt, timeout=900)
    except subprocess.TimeoutExpired:
        timed_out = True
        os.killpg(proc.pid, signal.SIGTERM)
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            proc.wait(timeout=10)
completion = {"exit_code": proc.returncode, "timed_out": timed_out,
              "elapsed_seconds": round(time.monotonic() - start, 3)}
(out / "completion.json").write_text(json.dumps(completion, indent=2) + "\n")
print(json.dumps(completion), flush=True)
raise SystemExit(proc.returncode if proc.returncode >= 0 else 1)
