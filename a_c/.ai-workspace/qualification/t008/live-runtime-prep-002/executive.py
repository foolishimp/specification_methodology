"""One explicit public T008 operation per invocation; no automatic next action.

Default output is a request/argv preview. --execute is operator action, never
authority minted by this helper. Dispatch additionally requires Root's separate
exact call approval in the governing session. No actor bypass/imports exist.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
PRODUCT = BASE.parents[3]
ENTRY = PRODUCT / "build_tenants/graphify/code/ac_support.py"


def read(path: Path) -> dict:
    with path.open("rb") as source:
        value = json.load(source)
    if not isinstance(value, dict):
        raise ValueError("Expected a complete JSON object")
    return value


def artifact(value: object) -> dict:
    if not isinstance(value, dict) or set(value) != {"id", "sha256"}:
        raise ValueError("An actual public ArtifactRef is required")
    digest = value["sha256"]
    if not isinstance(digest, str) or len(digest) != 64 or value["id"] != "sha256:" + digest:
        raise ValueError("Actual artifact identity/hash disagree")
    return value


def primary(path: Path | None) -> dict:
    if path is None:
        raise ValueError("Select the actual earlier public response explicitly")
    response = read(path)
    if response.get("status") != "ok":
        raise ValueError("Earlier response is not an available output")
    return artifact(response["result"]["artifact"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=["describe", "source", "observe", "context", "preflight", "dispatch", "observe-attempt", "wait", "capture", "check", "read-evidence"])
    parser.add_argument("--id", required=True, help="Stable exact caller id; never changed to retry an unknown effect")
    parser.add_argument("--execute", action="store_true", help="Invoke exactly this public operation; does not authorize any later operation")
    parser.add_argument("--operation", help="Optional tools.describe operation")
    parser.add_argument("--source", default="TASK", help="Named SourceRef in source-index.json")
    parser.add_argument("--observation-response", type=Path)
    parser.add_argument("--context-response", type=Path)
    parser.add_argument("--preflight-response", type=Path)
    parser.add_argument("--attempt-response", type=Path)
    parser.add_argument("--observed-response", type=Path)
    parser.add_argument("--return-response", type=Path)
    parser.add_argument("--evidence-response", type=Path)
    parser.add_argument("--coordinate", choices=["evidence", "primary"], default="evidence")
    parser.add_argument("--after-event", type=int, default=0)
    parser.add_argument("--timeout-ms", type=int, default=5000)
    args = parser.parse_args()
    if not args.id or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_" for c in args.id):
        raise ValueError("Caller id must be a plain local filename coordinate")
    config = read(BASE / "CONFIGURATION.json")
    policy_path = BASE / config["executive_policy"]["path"]
    expected = config["executive_policy"]["sha256"]
    if hashlib.sha256(policy_path.read_bytes()).hexdigest() != expected:
        raise ValueError("Frozen Executive policy changed; no repinning")
    source_index = read(BASE / "source-index.json")
    grant = "urn:a-c:grant:T008:guide:001"
    operation: str
    arguments: dict
    phase = args.phase
    if phase == "describe":
        operation, arguments = "tools.describe", {}
        if args.operation:
            arguments["operation"] = args.operation
    elif phase == "source":
        selected = source_index[args.source]
        if not isinstance(selected, dict) or "engine" not in selected or selected.get("sha256") is None:
            raise ValueError("Select one actual readable pinned SourceRef")
        operation, arguments = "source.read", {"source": selected, "encoding": "utf8"}
    elif phase == "observe":
        # Stable governing/configuration input scope. The intended guide change
        # is not misrepresented as a permanently absent evaluation basis.
        operation = "workspace.observe"
        arguments = {"scope": read(BASE / "root-observation-scope.json")["scope"]}
    elif phase == "context":
        operation = "context.assemble"
        arguments = read(BASE / "context.assemble.request.json")["arguments"]
        arguments["packet"]["subject_basis"]["observations"] = [primary(args.observation_response)]
    elif phase == "preflight":
        operation = "contract.preflight"
        arguments = {"context": primary(args.context_response), "grant_id": grant, "executor_id": "claude-worker-001", "result_key": "urn:a-c:T008:worker-guide-result:001", "observations": [primary(args.observation_response)]}
    elif phase == "dispatch":
        operation, arguments = "dispatch.start", {"preflight": primary(args.preflight_response)}
    elif phase in ("observe-attempt", "wait"):
        attempt = primary(args.attempt_response)
        operation = "dispatch.observe" if phase == "observe-attempt" else "events.wait"
        arguments = {"attempt": attempt, "after_event": args.after_event}
        if phase == "wait":
            if not 0 <= args.timeout_ms <= 30000:
                raise ValueError("Wait is explicitly bounded to 0..30000ms")
            arguments.update(timeout_ms=args.timeout_ms, cadence_ms=250, purpose="Observe this one retained Attempt", stop_condition="new retained event or selected deadline")
    elif phase == "capture":
        if args.observed_response is None:
            raise ValueError("Select actual observed final stdout evidence")
        observed = read(args.observed_response)
        if observed.get("status") != "ok":
            raise ValueError("Actual observation response is unavailable")
        output = observed["result"]["value"]["output"]
        operation = "return.capture"
        arguments = {"attempt": primary(args.attempt_response), "payload": artifact(output["stdout"]), "return_contract": source_index["return_contract"]}
    elif phase == "check":
        operation = "return.check"
        arguments = {"return": primary(args.return_response), "context": primary(args.context_response), "consumer": "/root", "observations": [primary(args.observation_response)], "predicates": []}
    else:
        if args.evidence_response is None:
            raise ValueError("Select an actual public response to reacquire")
        previous = read(args.evidence_response)
        selected = previous["evidence"] if args.coordinate == "evidence" else previous["result"]["artifact"]
        operation, arguments = "evidence.read", {"artifact": artifact(selected)}
    request = {"schema": "a_c.fd-support.request/1", "id": args.id, "operation": operation, "arguments": arguments}
    argv = [str(Path(sys.executable).resolve()), str(ENTRY), "--policy", str(policy_path), "--policy-sha256", expected, "--principal", "/root", "call", "--request", "-"]
    if not args.execute:
        print(json.dumps({"mode": "preview-only", "argv": argv, "request": request}, indent=2))
        return 0
    # Preserve exact request/actual streams even when the public call is refused,
    # fails or times out. Never turn loss of an acknowledgment into another call.
    output = BASE / "root-operations" / args.id
    output.mkdir(parents=True, exist_ok=False)
    raw = (json.dumps(request, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
    (output / "request.json").write_bytes(raw)
    started = time.time_ns()
    try:
        run = subprocess.run(argv, input=raw, capture_output=True, timeout=45, check=False)
        stdout, stderr, code, state = run.stdout, run.stderr, run.returncode, "returned"
    except subprocess.TimeoutExpired as error:
        stdout, stderr, code, state = error.stdout or b"", error.stderr or b"", 124, "timeout-effect-unknown-no-retry"
    (output / "response.json").write_bytes(stdout)
    (output / "stderr.bin").write_bytes(stderr)
    (output / "execution.json").write_text(json.dumps({"argv": argv, "started_ns": started, "ended_ns": time.time_ns(), "exit_code": code, "state": state, "no_next_action": True}, indent=2) + "\n")
    sys.stdout.buffer.write(stdout)
    sys.stderr.buffer.write(stderr)
    return code


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("Preparation/selected operation unavailable: " + str(error), file=sys.stderr)
        raise SystemExit(2)
