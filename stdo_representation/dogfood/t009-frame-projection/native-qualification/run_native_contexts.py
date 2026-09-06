"""Run the finite fresh host contexts, retaining unmodified command and output evidence."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import os
import signal
import subprocess
import time


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_context(context, timeout):
    dest = Path(context["directory"])
    snapshot = Path(context["snapshot"])
    prompt = (dest / "prompt.txt").read_text()
    if (dest / "command.json").exists():
        raise RuntimeError(f"Refuse duplicate invocation: {dest}")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    environment_overrides = {"PYTHONDONTWRITEBYTECODE": "1"}
    if context["host"] == "codex":
        # The user wrapper injects a global sandbox bypass. Invoke the installed
        # CLI directly with the same intended native profile and explicit scope.
        executable = "/opt/homebrew/lib/node_modules/@openai/codex/bin/codex.js"
        env["CODEX_HOME"] = "/Users/jim/.codex"
        environment_overrides["CODEX_HOME"] = env["CODEX_HOME"]
        argv = [executable, "exec", "--ephemeral", "--sandbox",
                context.get("sandbox", "read-only"), "--json", "--color", "never",
                "--model", "gpt-6-astra", "-c", 'model_reasoning_effort="max"',
                "-C", context["cwd"], "-o", str(dest / "final.txt"), "-"]
        stdin = prompt
    else:
        executable = "claude"
        argv = ["claude", "--print", "--output-format", "stream-json", "--verbose",
                "--no-session-persistence", "--permission-mode", "dontAsk",
                "--allowedTools", "Read", "Glob", "Grep", "Skill",
                "Bash(python3 *)", "Bash(rg *)", "Bash(shasum *)", "Bash(ls *)",
                "Bash(cat *)", "Bash(sed *)", "Bash(pwd)"]
        if context.get("allow_fixture_edit"):
            argv += ["Edit", "Write"]
        argv += ["--", prompt]
        stdin = None
    version = subprocess.run([executable, "--version"], env=env, capture_output=True, text=True, check=False)
    command = {"argv": argv, "cwd": context["cwd"], "prompt_sha256": digest(dest / "prompt.txt"),
               "stdin": "prompt.txt" if stdin is not None else None,
               "host_version": version.stdout.strip(), "host_version_stderr": version.stderr,
               "started_at": now(), "timeout_seconds": timeout,
               "environment_overrides": environment_overrides,
               "model_selection": "Codex explicitly binds the wrapper's configured gpt-6-astra/max; Claude uses configured default recorded in raw metadata.",
               "runner_sha256": digest(Path(__file__))}
    (dest / "command.json").write_text(json.dumps(command, indent=2) + "\n")
    started = time.monotonic()
    timed_out = False
    with (dest / "stdout.jsonl").open("w") as stdout, (dest / "stderr.txt").open("w") as stderr:
        process = subprocess.Popen(argv, cwd=context["cwd"], env=env,
                                   stdin=subprocess.PIPE if stdin is not None else subprocess.DEVNULL,
                                   stdout=stdout, stderr=stderr, text=True, start_new_session=True)
        (dest / "process.json").write_text(json.dumps({"pid": process.pid, "started_at": now()}) + "\n")
        try:
            process.communicate(stdin, timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
    metadata = []
    final_messages = []
    for line in (dest / "stdout.jsonl").read_text().splitlines():
        try:
            row = json.loads(line)
        except ValueError:
            continue
        if row.get("type") == "system" or row.get("type") in ("thread.started", "turn.completed", "result"):
            metadata.append(row)
        if row.get("type") == "result" and isinstance(row.get("result"), str):
            final_messages.append(row["result"])
    if context["host"] == "claude" and final_messages:
        (dest / "final.txt").write_text("\n\n".join(final_messages) + "\n")
    (dest / "host-metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
    before = json.loads((dest / "snapshot-before.json").read_text())
    after = {str(p.relative_to(snapshot)): digest(p) for p in sorted(snapshot.rglob("*"))
             if p.is_file() and ".git" not in p.relative_to(snapshot).parts and not p.is_symlink()}
    (dest / "snapshot-after.json").write_text(json.dumps(after, indent=2) + "\n")
    changed = {key: {"before": before.get(key), "after": after.get(key)}
               for key in sorted(set(before) | set(after)) if before.get(key) != after.get(key)}
    result = {"context": context["name"], "finished_at": now(), "exit_code": process.returncode,
              "timed_out": timed_out, "duration_seconds": round(time.monotonic() - started, 3),
              "host_version": version.stdout.strip(), "snapshot_changes": changed,
              "files": {p.name: digest(p) for p in [dest / "command.json", dest / "stdout.jsonl",
                       dest / "stderr.txt", dest / "host-metadata.json", dest / "snapshot-before.json",
                       dest / "snapshot-after.json"] + ([dest / "final.txt"] if (dest / "final.txt").exists() else [])},
              "semantic_disposition": "Not computed by runner; assess actual response against frozen source oracles."}
    (dest / "execution-result.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("contexts", type=Path)
    parser.add_argument("--timeout", type=int, default=720)
    parser.add_argument("--parallel", type=int, default=4)
    args = parser.parse_args()
    data = json.loads(args.contexts.read_text())
    with ThreadPoolExecutor(max_workers=args.parallel) as pool:
        futures = [pool.submit(run_context, context, args.timeout) for context in data["contexts"]]
        for future in as_completed(futures):
            result = future.result()
            print(json.dumps({key: result[key] for key in ("context", "exit_code", "timed_out", "duration_seconds", "snapshot_changes")}), flush=True)


if __name__ == "__main__":
    main()
