"""Fixed regular-file process fixture; no model/provider/network calls."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import signal
import subprocess
import sys
import time


def _public_writer(raw: bytes, target: Path) -> int:
    """A real composed Worker -> public MCP -> Writer call, no direct write."""
    activation = json.loads(raw)
    command = [sys.executable, sys.argv[4], "--policy", sys.argv[3], "--policy-sha256", activation["policy_sha256"], "--principal", "worker", "mcp"]
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    assert process.stdin is not None and process.stdout is not None
    trace: list[str] = []
    def exchange(message: dict[str, object], response: bool = True) -> dict[str, object]:
        process.stdin.write(json.dumps(message) + "\n")
        process.stdin.flush()
        if not response:
            return {}
        line = process.stdout.readline()
        trace.append(line)
        if not line:
            raise RuntimeError("Public MCP child ended before its response")
        decoded: dict[str, object] = json.loads(line)
        return decoded
    def interrupted(signum: int, frame: object) -> None:
        del signum, frame
        raise TimeoutError("Actor timed out waiting for its public Writer result")
    signal.signal(signal.SIGTERM, interrupted)
    try:
        exchange({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-11-25", "capabilities": {}, "clientInfo": {"name": "registered-fixture-worker", "version": "1"}}})
        exchange({"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}}, False)
        response = exchange({"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "work.write", "arguments": activation["request"]}})
        result = response.get("result")
        if not isinstance(result, dict) or not isinstance(result.get("structuredContent"), dict):
            raise RuntimeError("Public Writer returned no structured tool result")
        structured = result["structuredContent"]
        if structured.get("status") != "ok" or target.read_bytes() != b"actor-side tool progress":
            raise RuntimeError("Actor's public Writer did not establish its requested record")
        print(json.dumps({"fixture": "public-writer", "writer_progress_before_actor_exit": True, "target_sha256": hashlib.sha256(target.read_bytes()).hexdigest(), "mcp_raw_responses": trace, "tool_result": structured}), flush=True)
        return 0
    except (RuntimeError, TimeoutError) as error:
        print(json.dumps({"fixture": "public-writer", "writer_progress_before_actor_exit": False, "failure": str(error), "mcp_raw_responses": trace}), flush=True)
        return 4
    finally:
        # This fixture owns its MCP child. Cancellation still establishes no
        # rollback; before/after target bytes and raw responses remain evidence.
        if process.poll() is None:
            process.terminate()
        try:
            process.wait(timeout=1)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=1)
        for stream in (process.stdin, process.stdout, process.stderr):
            if stream is not None and not stream.closed:
                stream.close()


def main() -> int:
    mode = sys.argv[1]
    if mode == "hold":
        time.sleep(0.8)
        return 0
    raw = sys.stdin.buffer.read()
    target = Path(sys.argv[2])
    if mode == "public-writer":
        return _public_writer(raw, target)
    if mode == "count":
        count = int(target.read_text()) if target.exists() else 0
        target.write_text(str(count + 1))
    elif mode in ("partial", "ignore-term", "fail"):
        target.write_text("partial-effect")
        print("partial-output", flush=True)
        if mode == "ignore-term":
            signal.signal(signal.SIGTERM, signal.SIG_IGN)
        if mode == "fail":
            return 3
        time.sleep(2)
    elif mode == "descendant":
        subprocess.Popen([sys.executable, __file__, "hold"])
    print(json.dumps({"fixture": mode, "stdin_sha256": hashlib.sha256(raw).hexdigest()}), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
