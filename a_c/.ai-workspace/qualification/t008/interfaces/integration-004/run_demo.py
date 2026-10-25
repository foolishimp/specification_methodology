"""Retain the documented ordinary read-only path; no model or authority grant."""
from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time

from run_checks import HERE, PYTHON, ROOT, TENANT, gate, save, sources


def main() -> int:
    gate()
    target = HERE / "ordinary-demo-001"
    target.mkdir()
    before = sources()
    save(target / "sources-before.json", before)
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"

    def call(name: str, command: list[str], raw: bytes = b"") -> subprocess.CompletedProcess[bytes]:
        start = time.time_ns()
        result = subprocess.run(command, cwd=ROOT / "a_c", input=raw, capture_output=True,
                                timeout=30, env=env, check=False)
        end = time.time_ns()
        (target / (name + ".stdin")).write_bytes(raw)
        (target / (name + ".stdout")).write_bytes(result.stdout)
        (target / (name + ".stderr")).write_bytes(result.stderr)
        save(target / (name + ".json"), {"command": command, "started_ns": start, "ended_ns": end,
                                       "returncode": result.returncode, "actual_actor_calls": 0})
        return result

    checks: dict[str, bool] = {}
    with tempfile.TemporaryDirectory(prefix="a-c-ordinary-demo-") as temporary:
        output = Path(temporary).resolve() / "demo"
        env["TMPDIR"] = str(Path(temporary).resolve())
        env["PYTHONPYCACHEPREFIX"] = str(Path(temporary).resolve() / "pycache")
        try:
            setup = call("01-setup", [str(PYTHON), str(TENANT / "examples/fd-support/prepare_readonly.py"),
                         "--out", str(output), "--product-root", str(ROOT / "a_c")])
            assert setup.returncode == 0, setup.stderr
            settings = json.loads(setup.stdout)
            checks["demo_grants_no_work_or_executors"] = settings["Product_work_grants"] == settings["registered_executors"] == settings["model_calls"] == 0
            base = [str(PYTHON), str(TENANT / "code/ac_support.py"), "--policy", str(output / "policy.json"),
                    "--policy-sha256", settings["policy_sha256"]]
            for index, principal, filename, expected in ((2, "executive", "describe.json", 0),
                    (3, "worker", "read-product.json", 0), (4, "executive", "observe.json", 0),
                    (5, "executive", "denied-preflight.json", 2)):
                result = call(f"{index:02}-" + filename, base + ["--principal", principal, "call", "--request", str(output / "requests" / filename)])
                response = json.loads(result.stdout)
                checks[filename + "_exit_and_status"] = result.returncode == expected and response["status"] == ("refused" if expected else "ok")
                if filename == "read-product.json":
                    checks["readable_exact_product"] = response["result"]["value"]["content"] == (ROOT / "a_c/stdo_a_c.json").read_text()
                if filename == "denied-preflight.json":
                    checks["denied_preflight_not_publication_failure"] = response["refusal"]["code"] != "evidence_publication_failed" and response["evidence"] is not None
            mcp = call("06-mcp", base + ["--principal", "reviewer", "mcp"], (output / "mcp-session.jsonl").read_bytes())
            messages = [json.loads(line) for line in mcp.stdout.splitlines()]
            checks["MCP_initialized_and_three_responses"] = mcp.returncode == 0 and [message["id"] for message in messages] == [1, 2, 3]
            checks["MCP_exact_readable_product"] = messages[-1]["result"]["structuredContent"]["result"]["value"]["content"] == (ROOT / "a_c/stdo_a_c.json").read_text()
            checks["MCP_text_equals_structured"] = json.loads(messages[-1]["result"]["content"][0]["text"]) == messages[-1]["result"]["structuredContent"]
        finally:
            if output.exists():
                shutil.copytree(output, target / "retained-demo", symlinks=True)
            save(target / "checks.json", {"checks": checks, "actual_actor_calls": 0, "scope": "ordinary public read-only example; no real authority or semantic actor qualification"})
            gate()
            gate()
            after = sources()
            save(target / "sources-after.json", after)
    success = bool(checks) and all(checks.values()) and before == after
    print(json.dumps({"passed": success, "checks": checks, "sources_unchanged": before == after}))
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
