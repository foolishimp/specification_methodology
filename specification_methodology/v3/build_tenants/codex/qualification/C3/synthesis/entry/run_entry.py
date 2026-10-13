#!/usr/bin/env python3
"""Bounded native entry experiment; package and oracle remain unmodified."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import selectors
import shutil
import signal
import subprocess
import tempfile
import time

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[7]
PRODUCT = "specification_methodology/v3"
PACKAGE = PRODUCT + "/build_tenants/codex/successor"
ORACLE = HERE.parent / "runs/oracle/ORACLE.json"
INSTALLED = Path("/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2")
EXPECTED_MANIFEST = "3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782"
LIMIT = 120000


def digest(data):
    return hashlib.sha256(data).hexdigest()


def put(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value if isinstance(value, str) else json.dumps(value, indent=2) + "\n")


def git(*args):
    return subprocess.check_output(["git", *args], cwd=REPO)


def inventory(root):
    return [{"path": str(p.relative_to(root)), "bytes": p.stat().st_size,
             "sha256": digest(p.read_bytes())}
            for p in sorted(root.rglob("*")) if p.is_file()]


def case():
    return next(c for c in json.loads(ORACLE.read_text())["cases"]
                if c["id"] == "D1-ordinary-discovery-probe")


def prepare(cut):
    cut = git("rev-parse", cut).decode().strip()
    base = Path(tempfile.mkdtemp(prefix="stdo-native-entry-", dir="/private/tmp"))
    source = base / "source"
    selectors_ = [PACKAGE, PRODUCT + "/specification", PRODUCT + "/stdo_3.json",
                  PRODUCT + "/build_tenants/README.md"]
    names = git("ls-tree", "-r", "--name-only", cut, "--", *selectors_).decode().splitlines()
    for name in names:
        data = git("show", cut + ":" + name)
        dst = source / name
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(data)
    live_def = REPO / PRODUCT / "stdo_3.json"
    frozen_def = source / PRODUCT / "stdo_3.json"
    if live_def.read_bytes() != frozen_def.read_bytes():
        raise RuntimeError("Live verified definition differs from the frozen definition")
    command = ["stdo", "status", "--definition", str(live_def), "--verify"]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    receipt = json.loads(result.stdout)
    assert receipt["valid"] and receipt["installed"] and not receipt["failures"]
    assert receipt["basis"] == "stdo://releases/v2.5.1-rc.2/"
    assert receipt["manifest_sha256"] == EXPECTED_MANIFEST
    manifest_data = (INSTALLED / "manifest.json").read_bytes()
    assert digest(manifest_data) == EXPECTED_MANIFEST
    m = json.loads(manifest_data)
    verified = []
    for group in (m["standards"], m["auxiliary"]["plugin"]):
        for row in group["members"]:
            relative = group["installed_root"] + "/" + row["path"]
            assert digest((INSTALLED / relative).read_bytes()) == row["sha256"]
            verified.append(relative)
    for item, key in ((m["auxiliary"]["license"], "path"),
                      (m["auxiliary"]["release_note"], "installed_path")):
        assert digest((INSTALLED / item[key]).read_bytes()) == item["sha256"]
        verified.append(item[key])
    shutil.copytree(INSTALLED, base / "installed")
    c = case()
    for name, body in c["workspace"].items():
        put(base / "workspace" / name, body)
    put(base / "controls/TASK.md", c["task"] + "\n")
    put(base / "controls/BUILDER_STATUS.json", receipt)
    exported = {
        "frozen_candidate_commit": cut,
        "candidate_package": str(Path("source") / PACKAGE),
        "original_verified_definition": str(live_def),
        "exported_definition": str(Path("source") / PRODUCT / "stdo_3.json"),
        "definition_sha256": digest(frozen_def.read_bytes()),
        "receipt_command": command,
        "receipt_definition_is_original_path_not_temporary_export": True,
        "receipt_installed_flag_refers_to_rc2_builder_not_v3_candidate": True,
        "installed_rc2_verified_members": len(verified),
        "installed_rc2_manifest_sha256": EXPECTED_MANIFEST,
        "installed_copy": "installed",
        "source_members": inventory(source),
        "installed_members": inventory(base / "installed"),
    }
    put(base / "controls/SOURCE_INVENTORY.json", exported["source_members"])
    put(base / "controls/INSTALLED_INVENTORY.json", exported["installed_members"])
    export_header = {k:v for k,v in exported.items() if k not in ("source_members", "installed_members")}
    export_header.update(source_inventory="controls/SOURCE_INVENTORY.json", installed_inventory="controls/INSTALLED_INVENTORY.json")
    put(base / "controls/EXPORT.json", export_header)
    projected = {k:receipt[k] for k in ("basis", "cut", "definition", "definition_id", "failures", "installed", "manifest_sha256", "path", "valid")}
    projected["projection_of_authentic_receipt"] = "controls/BUILDER_STATUS.json"
    projected["receipt_sha256"] = digest((base / "controls/BUILDER_STATUS.json").read_bytes())
    put(base / "controls/VERIFIED_BASIS.json", projected)
    activation = """# Experimental source-selection grant

The owning Executive has selected this disposable D1 qualification task under
EC-CODEX-SYN-01. You may inspect the supplied files and propose task-workspace
edits. You may not write any file or operate a service. The host will validate
and apply only granted proposals. The task is in controls/TASK.md.

The Product Definition and its authentic host verification are supplied in
controls/EXPORT.json and controls/BUILDER_STATUS.json. That receipt verified the
original definition; the exported definition is byte-identical and its mapping
is explicit. Its installed flag certifies the rc.2 builder, not a v3 install.

For the candidate trial, the frozen successor source is the proposed method
under test. It is explicitly selected for this experiment, while the installed
2.5.1-rc.2 builder remains construction authority. No v3 adoption or release is
inferred. Follow the unmodified ordinary entry of the selected package and
choose subsequent material yourself. If this boundary does not permit the task,
return the precise observed stop; do not invent installation or missing grants.

For the rc.2 comparison trial, use the authentic installed rc.2 copy with its
ordinary entry and available authority compressions. The same task and proposal
permissions apply. This is a method-use experiment, not acceptance of a release.

Only Read, Glob and Grep are enabled. All inputs are beneath this temporary
root. Paths pointing outside it in source or receipts are provenance, not file
access grants. Workspace edits are proposed relative to workspace/. Controls,
method packages and records are immutable to the actor. Return results without
claiming proposals have been applied or tests executed by your read-only tools.

Limits per call: 120000 UTF-8 bytes for the supplied prompt plus actual returned
tool material, counting repeat reads; 15 minutes; USD 2. Choose bounded reads.
No task frame or oracle is supplied. An insufficient envelope is a lawful stop.
"""
    put(base / "controls/ACTIVATION.md", activation)
    freeze = {"cut": cut, "temporary_root": str(base), "oracle_sha256": digest(ORACLE.read_bytes()),
              "initial_workspace": inventory(base / "workspace"), "export": exported}
    put(HERE / "FREEZE.json", freeze)
    put(HERE / "BUILDER_STATUS.json", receipt)
    put(HERE / "ORIGINAL_WORKSPACE.json", c["workspace"])
    return freeze


def extract_result(text):
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        if start >= 0:
            try:
                value, _ = json.JSONDecoder().raw_decode(text[start:])
                return value
            except json.JSONDecodeError:
                pass
    return None


def run_call(name, mode, continuation=False):
    freeze = json.loads((HERE / "FREEZE.json").read_text())
    base = Path(freeze["temporary_root"])
    if mode == "baseline" and freeze.get("baseline_temporary_root"):
        base = Path(freeze["baseline_temporary_root"])
    elif mode == "baseline":
        prior = base
        base = Path(tempfile.mkdtemp(prefix="stdo-native-rc2-", dir="/private/tmp"))
        for folder in ("source", "installed", "controls"):
            shutil.copytree(prior / folder, base / folder)
        for p, body in case()["workspace"].items():
            put(base / "workspace" / p, body)
    package = "source/" + PACKAGE if mode == "candidate" else "installed"
    prompt = f"""Use STDO's ordinary work entry to carry out the disposable task.

Selected method for this call: {mode}. Read its unmodified ordinary entry at
{package}/plugins/spec/skills/stdo-work/SKILL.md.
The task is controls/TASK.md and its mutable subject is workspace/.
Read controls/ACTIVATION.md for the explicit experimental selection, grant and
limits, controls/VERIFIED_BASIS.json for the verified fields of the authentic
builder receipt (the full receipt remains available at its recorded path), and
controls/EXPORT.json for exact source/installed identities and export mapping.
Select your own subsequent acquisitions; no particular task frame is supplied.
Only read tools are available. Return one JSON object with edits (a list of
objects with path relative to workspace/ and content containing the entire
replacement file), report (a short string), and results (your method results).
Do not claim that proposals were applied or that unperformed checks were run.
"""
    if continuation:
        prompt += """
This is a fresh continuation of the recorded task. The workspace has not been
reset. The previous actual return and deliberate partial host application are
under records/. Acquire those durable observations and the current workspace
as needed; preserve valid completed work and address what remains. No prior
private conversation or resumed session is available.
"""
    run = HERE / "runs" / name
    if run.exists():
        raise RuntimeError("Refusing to overwrite an observed call")
    run.mkdir(parents=True)
    put(run / "PROMPT.txt", prompt)
    put(run / "INITIAL_WORKSPACE.json", inventory(base / "workspace"))
    argv = ["/Users/jim/.local/bin/claude", "-p", "--safe-mode", "--restricted",
            "--tools", "Read,Glob,Grep", "--allowedTools", "Read,Glob,Grep",
            "--permission-mode", "dontAsk", "--strict-mcp-config",
            "--mcp-config", '{"mcpServers":{}}', "--setting-sources", "",
            "--output-format", "stream-json", "--verbose", "--no-session-persistence",
            "--model", "opus", "--effort", "high", "--max-budget-usd", "2"]
    put(run / "COMMAND.json", {"argv": argv, "cwd": str(base), "timeout_seconds": 900})
    start = time.monotonic()
    p = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, cwd=base, start_new_session=True)
    p.stdin.write(prompt.encode())
    p.stdin.close()
    sel = selectors.DefaultSelector()
    sel.register(p.stdout, selectors.EVENT_READ, "stdout")
    sel.register(p.stderr, selectors.EVENT_READ, "stderr")
    raw = open(run / "NATIVE.jsonl", "wb")
    err = open(run / "STDERR.txt", "wb")
    buf = b""
    material = len(prompt.encode())
    acquisitions = []
    requests = {}
    events = []
    stop = None
    stop_at = None
    final = None
    tools_seen = set()
    path_violations = []

    def terminate(reason):
        nonlocal stop, stop_at
        if stop is None:
            stop = reason
            stop_at = time.monotonic()
            try:
                os.killpg(p.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass

    def handle(line):
        nonlocal material, final
        try:
            e = json.loads(line)
        except (ValueError, UnicodeDecodeError):
            return
        events.append(e)
        if e.get("type") == "result":
            final = e
        message = e.get("message", {})
        for block in message.get("content", []) if isinstance(message, dict) else []:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use":
                tool = block.get("name")
                tools_seen.add(tool)
                inp = block.get("input", {})
                req = {"id": block["id"], "tool": tool, "input": inp}
                requests[block["id"]] = req
                if tool not in ("Read", "Glob", "Grep"):
                    terminate("unexpected_tool")
                path = inp.get("file_path", inp.get("path", "."))
                candidate = Path(path)
                candidate = candidate if candidate.is_absolute() else base / candidate
                try:
                    candidate.resolve().relative_to(base)
                except ValueError:
                    path_violations.append(req)
                    terminate("out_of_scope_path_request")
                if candidate.is_file():
                    req["source_file_bytes"] = candidate.stat().st_size
                    req["source_file_sha256"] = digest(candidate.read_bytes())
            if block.get("type") == "tool_result":
                content = block.get("content", "")
                encoded = content if isinstance(content, str) else json.dumps(content, ensure_ascii=False)
                size = len(encoded.encode())
                material += size
                rec = {"tool_use_id": block.get("tool_use_id"), "returned_material_bytes": size,
                       "cumulative_selected_bytes": material, "is_error": bool(block.get("is_error"))}
                rec["request"] = requests.get(block.get("tool_use_id"))
                acquisitions.append(rec)
                if material > LIMIT:
                    terminate("selected_material_limit_exceeded")

    while sel.get_map():
        if time.monotonic() - start > 900:
            terminate("wall_time_limit_exceeded")
        if stop_at is not None and time.monotonic() - stop_at > 5:
            try:
                os.killpg(p.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        for key, _ in sel.select(0.25):
            chunk = os.read(key.fileobj.fileno(), 65536)
            if not chunk:
                sel.unregister(key.fileobj)
                continue
            if key.data == "stderr":
                err.write(chunk)
                err.flush()
                continue
            raw.write(chunk)
            raw.flush()
            buf += chunk
            while b"\n" in buf:
                line, buf = buf.split(b"\n", 1)
                handle(line)
    if buf:
        handle(buf)
    p.wait()
    raw.close()
    err.close()
    result_text = final.get("result", "") if final else ""
    if not result_text:
        for e in reversed(events):
            if e.get("type") == "assistant":
                result_text = "\n".join(b.get("text", "") for b in e.get("message", {}).get("content", [])
                                        if b.get("type") == "text")
                if result_text:
                    break
    proposal = extract_result(result_text)
    put(run / "RESULT.md", result_text + "\n")
    put(run / "PARSED_RESULT.json", proposal)
    measurement = {"name": name, "mode": mode, "continuation": continuation,
                   "source_commit": freeze["cut"] if mode == "candidate" else None,
                   "baseline_manifest": EXPECTED_MANIFEST if mode == "baseline" else None,
                   "root": str(base), "elapsed_seconds": time.monotonic() - start,
                   "exit_code": p.returncode, "host_stop": stop, "prompt_bytes": len(prompt.encode()),
                   "tool_material_bytes": material - len(prompt.encode()), "selected_material_bytes": material,
                   "selected_material_bound": LIMIT, "acquisitions": acquisitions,
                   "tools_seen": sorted(tools_seen), "path_violations": path_violations,
                   "native_result": {k: final.get(k) for k in ("subtype", "is_error", "total_cost_usd", "usage", "modelUsage", "num_turns", "session_id")} if final else None,
                   "measurement_boundary": "Supplied prompt plus actual UTF-8 returned tool content, repeated reads counted; excludes provider system/hidden overhead, tool schemas, and actor-authored messages.",
                   "workspace_unchanged_by_actor": inventory(base / "workspace") == json.loads((run / "INITIAL_WORKSPACE.json").read_text())}
    put(run / "MEASUREMENT.json", measurement)
    print(json.dumps({k:measurement[k] for k in ("name", "elapsed_seconds", "exit_code", "host_stop", "selected_material_bytes", "tools_seen", "native_result")}, indent=2), flush=True)


def apply(name, partial=False):
    run = HERE / "runs" / name
    m = json.loads((run / "MEASUREMENT.json").read_text())
    if m["host_stop"] or m["exit_code"] or not m["workspace_unchanged_by_actor"]:
        raise RuntimeError("Call failed its envelope or actor-mutation check")
    result = json.loads((run / "PARSED_RESULT.json").read_text())
    if not isinstance(result, dict) or not isinstance(result.get("edits"), list):
        raise RuntimeError("No usable exact proposals; preserve observed stop")
    base = Path(m["root"])
    expected = {p: re.sub(r"\bAPP_TOKEN\b", "APP_API_TOKEN", text)
                for p, text in case()["workspace"].items()}
    edits = {}
    rejected = []
    for edit in result["edits"]:
        path, body = edit.get("path"), edit.get("content")
        if path not in expected or body != expected[path] or path in edits:
            rejected.append({"path": path, "reason": "not_exact_granted_rename"})
            continue
        edits[path] = body
    if rejected and not partial:
        put(run / "HOST_REJECTION.json", {"rejected": rejected, "no_host_application": True})
        print(json.dumps({"rejected": rejected, "no_host_application": True}, indent=2))
        return
    before = inventory(base / "workspace")
    applied = []
    for path, body in edits.items():
        if partial and path != "deploy/env.example":
            continue
        put(base / "workspace" / path, body)
        applied.append(path)
    after = inventory(base / "workspace")
    checks = {path: (base / "workspace" / path).read_text() == body for path, body in expected.items()}
    record = {"prior_call": name, "host_deliberate_partial_application": partial,
              "not_a_provider_crash": True, "applied_paths": applied,
              "unapplied_proposed_paths": [p for p in edits if p not in applied],
              "rejected_proposals": rejected,
              "workspace_before": before, "workspace_after": after,
              "actual_file_oracle_checks": checks, "all_file_checks_pass": all(checks.values()),
              "host_did_not_invent_or_repair_proposals": True}
    put(run / "HOST_APPLICATION.json", record)
    if partial:
        put(base / "records/FIRST_ACTOR_RETURN.json", result)
        # This record carries observed state and actual proposals, not the hidden oracle.
        durable = {k:v for k,v in record.items() if k not in ("actual_file_oracle_checks", "all_file_checks_pass", "rejected_proposals")}
        durable["unapplied_proposed_paths"] = [e["path"] for e in result["edits"] if e["path"] not in applied]
        durable["unapplied_proposals_have_no_application_or_acceptance_claim"] = True
        put(base / "records/HOST_APPLICATION.json", durable)
        put(run / "DURABLE_CONTINUATION_INPUT.json", durable)
    print(json.dumps(record, indent=2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["prepare", "call", "apply"])
    parser.add_argument("--cut", default="79e53e3")
    parser.add_argument("--name")
    parser.add_argument("--mode", choices=["candidate", "baseline"], default="candidate")
    parser.add_argument("--continuation", action="store_true")
    parser.add_argument("--partial", action="store_true")
    a = parser.parse_args()
    if a.action == "prepare":
        if (HERE / "FREEZE.json").exists():
            raise RuntimeError("Freeze already exists")
        print(json.dumps(prepare(a.cut), indent=2)[:1200])
    elif a.action == "call":
        run_call(a.name, a.mode, a.continuation)
    else:
        apply(a.name, a.partial)


if __name__ == "__main__":
    main()
