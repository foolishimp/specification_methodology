"""Custody/supervision only. No semantic grading; no implicit provider start."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import os
import shutil
import signal
import subprocess
import threading
import time

from prepare_native import HERE, sha, snapshot, write

CODEX = "/opt/homebrew/lib/node_modules/@openai/codex/bin/codex.js"
CLAUDE = "/Users/jim/.local/bin/claude"
PYTHON = "/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python"


def now():
    return datetime.now(timezone.utc).isoformat()


def environment(context):
    runtime, work = Path(context["runtime"]), Path(context["worksite"])
    native = json.loads((work / "native-context.json").read_text())
    # Existing HOME and CODEX_HOME are inherited unchanged. Never retain full env.
    overrides = {"PYTHONDONTWRITEBYTECODE": "1", "STDO_STORE": native["source_store"],
                 "ZDOTDIR": str(runtime / "zsh"), "TMPDIR": str(runtime / "tmp") + "/",
                 "TMPPREFIX": str(runtime / "tmp/zsh"),
                 "PATH": "/Users/jim/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"}
    for relative in ("tmp", "sqlite", "logs", "claude/projects"):
        (runtime / relative).mkdir(parents=True, exist_ok=True)
    if context["host"] == "claude":
        overrides.update(CLAUDE_CONFIG_DIR=str(runtime / "claude"), CLAUDE_CODE_TMPDIR=str(runtime / "tmp"),
                         CLAUDE_TMPDIR=str(runtime / "tmp"), CLAUDE_CODE_DISABLE_AUTO_MEMORY="1",
                         CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC="1")
        if not os.environ.get("CLAUDE_CODE_OAUTH_TOKEN"):
            raise RuntimeError("Claude OAuth transport unavailable")
    return dict(os.environ, **overrides), overrides


def prefix(context):
    return ["/usr/bin/sandbox-exec", "-f", context["outer_profile"]]


def transport_state(context):
    rows = []
    for expected in context.get("nonsemantic_transport", []):
        path = Path(expected["path"])
        info = path.stat()
        rows.append({"path": str(path), "sha256": sha(path), "device": info.st_dev,
                     "inode": info.st_ino, "mode": info.st_mode & 0o777, "size": info.st_size})
    return rows


def preflight(context, selection_path):
    selection_path = Path(selection_path).resolve()
    evidence, work, runtime = (Path(context[key]) for key in ("directory", "worksite", "runtime"))
    result_path = evidence / "confinement-preflight.json"
    if result_path.exists():
        raise RuntimeError("Refuse overwriting a preflight observation")
    before = json.loads((evidence / "snapshot-before.json").read_text())
    if snapshot(work) != before:
        raise RuntimeError("Worksite drift before preflight")
    transport_before = transport_state(context)
    if transport_before != context.get("nonsemantic_transport", []):
        raise RuntimeError("Nonsemantic transport preimage changed")
    env, env_overrides = environment(context)
    native = json.loads((work / "native-context.json").read_text())
    source = Path(native["source_store"]) / "releases/v2.5.1-rc.1/standards/SPEC_METHOD.md"
    controls = {"read_allowed": [str(work / "task.md"), str(source)],
                "read_denied": [str(HERE / "oracle.md"), str(HERE / "oracle-binding.json"), str(selection_path.parent / "withheld.txt")],
                "runtime_write": str(runtime / "preflight-probe"), "write_denied": str(work / "task.md"),
                "transport_open": [row["path"] for row in transport_before]}
    probe = """import json,os,sys
x=json.loads(sys.argv[1]);rows=[]
for p in x['read_allowed']:
 try:
  with open(p,'rb') as f:f.read(1)
  rows.append({'operation':'allowed_read','path':p,'pass':True})
 except OSError as e:rows.append({'operation':'allowed_read','path':p,'pass':False,'error':str(e)})
for p in x['read_denied']:
 try:
  with open(p,'rb') as f:f.read(1)
  rows.append({'operation':'denied_read','path':p,'pass':False})
 except PermissionError:rows.append({'operation':'denied_read','path':p,'pass':True})
 except OSError as e:rows.append({'operation':'denied_read','path':p,'pass':False,'error':str(e)})
for p in x['transport_open']:
 try:
  fd=os.open(p,os.O_RDWR);os.close(fd);rows.append({'operation':'existing_transport_open','path':p,'pass':True})
 except OSError as e:rows.append({'operation':'existing_transport_open','path':p,'pass':False,'error':str(e)})
try:
 with open(x['runtime_write'],'w') as f:f.write('transport probe')
 os.unlink(x['runtime_write']);rows.append({'operation':'runtime_write','pass':True})
except OSError as e:rows.append({'operation':'runtime_write','pass':False,'error':str(e)})
try:
 fd=os.open(x['write_denied'],os.O_WRONLY);os.close(fd);rows.append({'operation':'denied_write','pass':False})
except PermissionError:rows.append({'operation':'denied_write','pass':True})
except OSError as e:rows.append({'operation':'denied_write','pass':False,'error':str(e)})
print(json.dumps(rows));sys.exit(0 if all(r['pass'] for r in rows) else 2)
"""
    operations = [
        ("confinement", [PYTHON, "-B", "-c", probe, json.dumps(controls)], None),
        ("host_version", [CODEX if context["host"] == "codex" else CLAUDE, "--version"], None),
        ("fixture", [PYTHON, "-B", str(work / "fixture.py")], None),
        ("join", [PYTHON, "-B", str(Path(native["axiom_root"]) / "build_tenants/core/code/ac.py"), "join", "--input", "/dev/stdin"], '[{"label":"PROBE","text":"read-only join"}]'),
    ]
    if native.get("representation_root"):
        artifact = Path(native["representation_root"]) / "build_tenants/axiom_indexer/representation/stdo-v2.5.1-rc.1"
        operations.append(("bound_frame_projection", [PYTHON, "-B", str(Path(native["axiom_root"]) / "build_tenants/core/code/ac.py"),
            "project", "--program", str(artifact / "axiomatic-program.json"), "--map", str(artifact / "logical-constraint-map.json"),
            "--bindings", str(work / native["bindings"]), "--frame-index", "urn:stdo-representation:frame-index:end-to-end-interface-integration",
            "--frame-index", "urn:stdo-representation:frame-index:computational-whole-path-evaluation", "--mode", "reference-only"], None))
    results = []
    for name, command, stdin in operations:
        result = subprocess.run(prefix(context) + command, cwd=work, env=env, input=stdin, capture_output=True, text=True, timeout=45)
        row = {"operation": name, "argv": prefix(context) + command, "exit_code": result.returncode,
               "stdout": result.stdout, "stderr": result.stderr, "pass": result.returncode == 0}
        if name == "join":
            row["pass"] = row["pass"] and result.stdout == "PROBE\nread-only join"
        if name == "fixture" and row["pass"]:
            observed = json.loads(result.stdout)
            row["pass"] = observed["importer"][1]["meter"]["item_visits"] == 2000
        if name == "bound_frame_projection" and row["pass"]:
            row["pass"] = isinstance(json.loads(result.stdout), dict)
        results.append(row)
    unchanged = snapshot(work) == before
    transport_after = transport_state(context)
    transport_unchanged = transport_after == transport_before
    value = {"at": now(), "context": context["name"], "selection_sha256": sha(selection_path),
             "runner_sha256": sha(Path(__file__)), "profile_sha256": sha(context["outer_profile"]),
             "environment_overrides": env_overrides, "checks": results, "worksite_unchanged": unchanged,
             "nonsemantic_transport_before": transport_before, "nonsemantic_transport_after": transport_after,
             "nonsemantic_transport_unchanged": transport_unchanged,
             "status": "pass" if unchanged and transport_unchanged and all(r["pass"] for r in results) else "harness_not_ready",
             "provider_calls": 0, "scope": "OS custody, local runtime/version and pure fixture/join commands only; full authenticated host turn remains unobserved"}
    write(result_path, value)
    return value


def native_command(context):
    work, runtime = Path(context["worksite"]), Path(context["runtime"])
    model = context["models"][context["host"]]
    if context["host"] == "codex":
        args = [CODEX, "exec", "--ignore-user-config", "--ignore-rules", "--ephemeral", "--skip-git-repo-check",
                "--sandbox", "danger-full-access", "--json", "--color", "never", "--model", model["model"],
                "-c", "model_reasoning_effort=" + json.dumps(model["effort"]),
                "-c", 'approval_policy="never"', "-c", "sqlite_home=" + json.dumps(str(runtime / "sqlite")),
                "-c", "log_dir=" + json.dumps(str(runtime / "logs")), "-c", 'history.persistence="none"',
                "-c", 'check_for_update_on_startup=false', "-c", 'project_root_markers=["stdo_task.json"]']
        for feature in ("memories", "hooks", "shell_snapshot", "multi_agent", "apps"):
            args += ["--disable", feature]
        args += ["-C", str(work), "-o", str(runtime / "final.txt"), "-"]
    else:
        allowed = "Read,Glob,Grep,Skill,Bash"
        args = [CLAUDE, "--print", "--output-format", "stream-json", "--verbose", "--no-session-persistence",
                "--restricted", "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
                "--setting-sources", "", "--settings", '{"autoMemoryEnabled":false}', "--no-chrome",
                "--permission-mode", "dontAsk", "--model", model["model"], "--effort", model["effort"],
                "--tools", allowed, "--allowedTools", allowed, "--add-dir", str(runtime / "claude/projects"),
                "--", (Path(context["directory"]) / "prompt.txt").read_text()]
    return prefix(context) + args


def run(context, selection_path, authority_path, timeout):
    selection_path, authority_path = Path(selection_path).resolve(), Path(authority_path).resolve()
    evidence, work, runtime = (Path(context[key]) for key in ("directory", "worksite", "runtime"))
    if (evidence / "command.json").exists():
        raise RuntimeError("Context already exposed; no retry: " + context["name"])
    preflight_path = evidence / "confinement-preflight.json"
    pre = json.loads(preflight_path.read_text())
    authority = json.loads(authority_path.read_text())
    if pre["status"] != "pass" or pre["selection_sha256"] != sha(selection_path):
        raise RuntimeError("Mechanical preflight not current")
    if pre["runner_sha256"] != sha(Path(__file__)) or pre["profile_sha256"] != sha(context["outer_profile"]):
        raise RuntimeError("Runner or confinement profile changed after preflight")
    if authority["selection_sha256"] != sha(selection_path) or authority["preflight_sha256"].get(context["name"]) != sha(preflight_path) or authority["status"] != "execution_authorized":
        raise RuntimeError("No exact parent execution trigger for context")
    before = json.loads((evidence / "snapshot-before.json").read_text())
    if snapshot(work) != before:
        raise RuntimeError("Worksite drift before exposure")
    transport_before = transport_state(context)
    if transport_before != context.get("nonsemantic_transport", []):
        raise RuntimeError("Nonsemantic transport preimage changed before exposure")
    env, env_overrides = environment(context)
    argv = native_command(context)
    prompt = (evidence / "prompt.txt").read_text()
    write(evidence / "command.json", {"argv": argv, "cwd": str(work), "prompt_sha256": sha(evidence / "prompt.txt"),
          "started_at": now(), "timeout_seconds": timeout, "runner_sha256": sha(Path(__file__)),
          "execution_authority_sha256": sha(authority_path), "environment_overrides": env_overrides,
          "HOME_and_CODEX_HOME": "inherited unchanged; no credentials copied", "limit_is_not_product_criterion": True})
    started = time.monotonic()
    process = subprocess.Popen(argv, cwd=work, env=env, stdin=subprocess.PIPE if context["host"] == "codex" else subprocess.DEVNULL,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors="replace", start_new_session=True)
    write(evidence / "process.json", {"pid": process.pid, "started_at": now()})
    def collect(stream, path):
        with path.open("w") as out:
            for line in stream:
                out.write(line)
                out.flush()
    threads = [threading.Thread(target=collect, args=(process.stdout, evidence / "stdout.jsonl")),
               threading.Thread(target=collect, args=(process.stderr, evidence / "stderr.txt"))]
    for thread in threads:
        thread.start()
    if context["host"] == "codex":
        try:
            process.stdin.write(prompt)
            process.stdin.close()
        except BrokenPipeError:
            pass
    timed_out = False
    try:
        process.wait(timeout=timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        os.killpg(process.pid, signal.SIGTERM)
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait()
    for thread in threads:
        thread.join()
    metadata, finals = [], []
    for line in (evidence / "stdout.jsonl").read_text().splitlines():
        try:
            row = json.loads(line)
        except ValueError:
            continue
        if row.get("type") in ("system", "thread.started", "turn.completed", "result"):
            metadata.append(row)
        if row.get("type") == "result" and isinstance(row.get("result"), str):
            finals.append(row["result"])
    if context["host"] == "codex" and (runtime / "final.txt").exists():
        shutil.copy2(runtime / "final.txt", evidence / "final.txt")
    elif finals:
        write(evidence / "final.txt", "\n\n".join(finals) + "\n")
    write(evidence / "host-metadata.json", metadata)
    # Retain explicit stdout/stderr/metadata only. Never archive host state,
    # runtime credentials, configuration caches or private auth transport.
    after = snapshot(work)
    transport_after = transport_state(context)
    write(evidence / "snapshot-after.json", after)
    changes = {p: {"before": before.get(p), "after": after.get(p)} for p in sorted(set(before) | set(after)) if before.get(p) != after.get(p)}
    result = {"context": context["name"], "finished_at": now(), "exit_code": process.returncode, "timed_out": timed_out,
              "duration_seconds": round(time.monotonic() - started, 3), "snapshot_changes": changes,
              "nonsemantic_transport_before": transport_before, "nonsemantic_transport_after": transport_after,
              "nonsemantic_transport_unchanged": transport_after == transport_before,
              "files": {p.name: sha(p) for p in evidence.iterdir() if p.is_file() and p.name != "execution-result.json"},
              "semantic_disposition": "not computed; independent source-oracle assessment required"}
    write(evidence / "execution-result.json", result)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--contexts", type=Path, required=True)
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--execution-authority", type=Path)
    parser.add_argument("--timeout", type=int, default=1200)
    parser.add_argument("--parallel", type=int, default=2)
    parser.add_argument("--only", nargs="*")
    args = parser.parse_args()
    selection = json.loads(args.contexts.read_text())
    if selection["oracle_sha256"] != sha(HERE / "oracle.md") or selection["oracle_binding_sha256"] != sha(HERE / "oracle-binding.json") or selection["packet"] != snapshot(HERE / "packet"):
        raise SystemExit("Packet or withheld oracle changed")
    if not args.preflight_only and args.execution_authority is None:
        raise SystemExit("Provider execution requires an exact parent trigger")
    contexts = [c for c in selection["contexts"] if not args.only or c["name"] in args.only]
    with ThreadPoolExecutor(max_workers=args.parallel) as pool:
        futures = {pool.submit(preflight, c, args.contexts) if args.preflight_only else pool.submit(run, c, args.contexts, args.execution_authority, args.timeout): c for c in contexts}
        for future in as_completed(futures):
            context = futures[future]
            try:
                result = future.result()
                print(json.dumps({"context": context["name"], "status": result.get("status"), "exit_code": result.get("exit_code"), "timed_out": result.get("timed_out")}), flush=True)
            except Exception as error:
                path = Path(context["directory"]) / "harness-exception.json"
                if not path.exists():
                    write(path, {"at": now(), "error": repr(error), "runner_sha256": sha(Path(__file__))})
                print(json.dumps({"context": context["name"], "harness_exception": repr(error)}), flush=True)


if __name__ == "__main__":
    main()
