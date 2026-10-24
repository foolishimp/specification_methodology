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

COMMAND = [
    "/Users/jim/.local/bin/claude", "-p", "--safe-mode", "--restricted",
    "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
    "--setting-sources", "", "--tools", "Read,Glob,Grep",
    "--allowedTools", "Read,Glob,Grep", "--no-session-persistence",
    "--disable-slash-commands", "--no-chrome", "--permission-prompts", "none",
    "--model", "claude-opus-5-5", "--effort", "xhigh",
    "--max-budget-usd", "10", "--output-format", "stream-json", "--verbose",
]


class Interrupted(Exception):
    def __init__(self, signum):
        self.signum = signum


def group_exists(pid):
    try:
        os.killpg(pid, 0)
        return True
    except ProcessLookupError:
        return False


def cleanup(proc):
    """Bound cleanup by group absence, independently of the direct exit."""
    sent = []
    for sig in (signal.SIGTERM, signal.SIGKILL):
        proc.poll()  # reap the direct child before testing the whole group
        if not group_exists(proc.pid):
            return {"confirmed": True, "signals": sent}
        try:
            os.killpg(proc.pid, sig)
            sent.append(int(sig))
        except ProcessLookupError:
            pass
        deadline = time.monotonic() + 5
        while time.monotonic() < deadline:
            proc.poll()
            if not group_exists(proc.pid):
                return {"confirmed": True, "signals": sent}
            time.sleep(0.05)
    proc.poll()
    return {"confirmed": not group_exists(proc.pid), "signals": sent}


def supervise(cmd, root, prompt, out):
    start = time.monotonic()
    proc = None
    record = {"exit_code": None, "timed_out": False, "interrupted_signal": None,
              "exception_type": None, "process_group": {"confirmed": False, "signals": []}}
    previous = {}

    def interrupt(signum, frame):
        record["interrupted_signal"] = int(signum)
        # Do not lose a child in the small Popen-before-assignment window.
        if proc is not None:
            raise Interrupted(signum)

    for sig in (signal.SIGINT, signal.SIGTERM, signal.SIGHUP):
        previous[sig] = signal.signal(sig, interrupt)
    try:
        with (out / "events.jsonl").open("xb") as stdout, (out / "stderr.txt").open("xb") as stderr:
            if record["interrupted_signal"]:
                raise Interrupted(record["interrupted_signal"])
            proc = subprocess.Popen(cmd, cwd=root, stdin=subprocess.PIPE, stdout=stdout,
                                    stderr=stderr, start_new_session=True)
            if record["interrupted_signal"]:
                raise Interrupted(record["interrupted_signal"])
            print(json.dumps({"started_pid": proc.pid, "output": str(out)}), flush=True)
            try:
                proc.communicate(prompt, timeout=900)
            except subprocess.TimeoutExpired:
                record["timed_out"] = True
    except Interrupted as exc:
        record["interrupted_signal"] = int(exc.signum)
    except KeyboardInterrupt:
        record["interrupted_signal"] = int(signal.SIGINT)
    except Exception as exc:
        record["exception_type"] = type(exc).__name__
    finally:
        # One controlled interruption starts bounded cleanup; a second must not
        # abort the retained result. SIGKILL is inherently uncatchable.
        for sig in previous:
            signal.signal(sig, signal.SIG_IGN)
        try:
            if proc is not None:
                try:
                    record["process_group"] = cleanup(proc)
                except Exception as exc:
                    record["process_group"]["error_type"] = type(exc).__name__
                record["exit_code"] = proc.poll()
            record["elapsed_seconds"] = round(time.monotonic() - start, 3)
            (out / "completion.json").write_text(json.dumps(record, indent=2) + "\n")
        finally:
            for sig, handler in previous.items():
                signal.signal(sig, handler)
    print(json.dumps(record), flush=True)
    return 0 if (record["exit_code"] == 0 and record["process_group"]["confirmed"]
                 and not record["timed_out"] and not record["interrupted_signal"]
                 and not record["exception_type"]) else 1


def main():
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
    invocation = {
        "argv": COMMAND, "cwd": str(root), "prompt_sha256": a.prompt_sha256,
        "timeout_seconds": 900, "max_budget_usd": 10,
        "capability": "Read,Glob,Grep confined to installed cwd; no MCP or shell",
        "freshness": "safe mode, no persistence, no resume, no automatic CLAUDE.md",
    }
    (out / "invocation.json").write_text(json.dumps(invocation, indent=2) + "\n")
    return supervise(COMMAND, root, prompt, out)


if __name__ == "__main__":
    raise SystemExit(main())
