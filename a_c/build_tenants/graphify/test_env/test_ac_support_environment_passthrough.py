"""Actual native dispatch transport controls; no credential or model is acquired.

The only credential-like value is freshly generated test data. A loopback test
oracle compares its actual child value in memory, retaining only a boolean.
All public requests, responses, helper evidence and test files are scanned for
the synthetic value before custody. Fixtures do not establish Product authority.
"""
from pathlib import Path
import hashlib
import json
import os
import secrets
import socket
import subprocess
import sys
import threading
import time
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))
import ac_support_core as c
import test_ac_support_native301 as native


NAME = "CLAUDE_CODE_OAUTH_TOKEN"


class EnvironmentPassthroughTests(unittest.TestCase):
    _select_policy = native.Native301PublicTests._select_policy
    _ok = native.Native301PublicTests._ok
    _assemble = native.Native301PublicTests._assemble
    _admit = native.Native301PublicTests._admit
    _finished = native.Native301PublicTests._finished
    tearDown = native.Native301PublicTests.tearDown

    def setUp(self):
        native.Native301PublicTests.setUp(self)
        # Never copy the real test runner's environment or read its credentials.
        self.dispatch_environment = {"PATH": os.defpath, "PYTHONDONTWRITEBYTECODE": "1"}
        self.sentinel = secrets.token_urlsafe(48)
        self.oracle_observations = []

    def _public(self, operation, arguments):
        self.sequence += 1
        folder = self.root / "calls" / (str(self.sequence).zfill(3) + "-" + operation)
        folder.mkdir(parents=True)
        request = {"schema": c.REQUEST, "id": "public-" + str(self.sequence),
                   "operation": operation, "arguments": arguments}
        path = folder / "request.json"
        path.write_bytes(c.canonical(request))
        argv = [str(self.python), "-B", str(self.code / "ac_support.py"),
                "--policy", str(self.policy_path), "--policy-sha256", self.policy_sha,
                "--principal", "executive", "call", "--request", str(path)]
        started = time.time_ns()
        result = subprocess.run(argv, cwd=self.root, capture_output=True, timeout=10,
                                env=self.dispatch_environment, check=False)
        (folder / "stdout.bin").write_bytes(result.stdout)
        (folder / "stderr.bin").write_bytes(result.stderr)
        (folder / "execution.json").write_bytes(c.canonical({
            "argv": argv, "started_ns": started, "ended_ns": time.time_ns(),
            "returncode": result.returncode, "policy_sha256": self.policy_sha}))
        response = c.parse_json(result.stdout)
        self.assertIsNotNone(response["evidence"], response)
        return response

    def _prepare(self, executor_selected, helper_selected, supplied):
        if supplied:
            self.dispatch_environment[NAME] = self.sentinel
        listener = socket.socket()
        listener.bind(("127.0.0.1", 0))
        listener.listen(1)
        listener.settimeout(8)
        self.addCleanup(listener.close)
        port = listener.getsockname()[1]

        def oracle():
            try:
                connection, _ = listener.accept()
                with connection:
                    raw = b""
                    while True:
                        part = connection.recv(1024)
                        if not part:
                            break
                        raw += part
                    # No synthetic value or digest leaves this test process.
                    self.oracle_observations.append({
                        "present": raw[:1] == b"1",
                        "unchanged": raw == b"1" + self.sentinel.encode(),
                    })
            except OSError:
                self.oracle_observations.append({"oracle_failed": True})

        self.oracle_thread = threading.Thread(target=oracle, daemon=True)
        self.oracle_thread.start()
        vendor = self.f.write("inputs/synthetic_vendor.py", b'''import json,os,socket,sys
sys.stdin.buffer.read()
value=os.environ.get("CLAUDE_CODE_OAUTH_TOKEN")
with socket.create_connection(("127.0.0.1",int(sys.argv[1])),timeout=3) as connection:
 connection.sendall(b"0" if value is None else b"1"+value.encode())
 connection.shutdown(socket.SHUT_WR)
if value is None:
 print(json.dumps({"type":"result","subtype":"error","is_error":True,"error":"authentication_failed","result":"Synthetic credential missing","total_cost_usd":0}))
 raise SystemExit(1)
print(json.dumps({"type":"result","subtype":"success","is_error":False,"result":json.dumps({"schema":"a_c.fd-support.closed-return/1","opaque":"synthetic transport only"})}))
''')
        tenant = self.code.parent
        helper = tenant / "examples/fd-support/actor_cli.py"
        core = self.code / "ac_support_core.py"
        self.f.policy["sources"]["tool"] = {
            "path": str(tenant), "kind": "workspace", "writable": False,
            "read_scope": [{"path": "code", "kind": "directory"},
                           {"path": "examples/fd-support", "kind": "directory"}]}
        settings = {"scope": "synthetic transport control only"}
        if helper_selected:
            settings["environment_passthrough"] = [NAME]
        document = {
            "schema": "a_c.fd-support.actor-cli-plan/1", "id": "synthetic-auth-transport",
            "backend": "claude",
            "executable": {"path": str(self.python), "sha256": hashlib.sha256(self.python.read_bytes()).hexdigest()},
            "argv": [str(self.python), "-B", str(self.f.workspace / vendor["path"]), str(port)],
            "dependencies": [{"path": str(self.f.workspace / vendor["path"]), "sha256": vendor["sha256"]}],
            "cwd": str(self.f.workspace), "environment": {"PYTHONDONTWRITEBYTECODE": "1"},
            "settings": settings, "decoder": "claude-result-json/1",
            "evidence_directory": str(self.root / "helper-output"),
            "limits": {"max_input_bytes": 1048576, "max_output_bytes": 1048576,
                       "timeout_ms": 3000, "termination_grace_ms": 100}}
        plan_ref = self.f.write("inputs/actor-plan.json", document)
        executor = self.f.policy["executors"]["registered"]
        executor["argv"] = [str(self.python), "-B", str(helper), "--plan",
                            str(self.f.workspace / plan_ref["path"]), "--plan-sha256", plan_ref["sha256"]]
        executor["dependencies"] = [vendor, plan_ref,
            self.f.ref(helper, "tool", "examples/fd-support/actor_cli.py"),
            self.f.ref(core, "tool", "code/ac_support_core.py")]
        executor["settings"] = {"timeout_ms": 5000, "termination_grace_ms": 100}
        if executor_selected:
            executor["settings"]["environment_passthrough"] = [NAME]
        self._select_policy()
        return document

    def _whole_path(self, *, executor_selected, helper_selected, supplied):
        self._prepare(executor_selected, helper_selected, supplied)
        receipt = self._admit(self._assemble())
        started = self._public("dispatch.start", {"preflight": receipt})
        self._ok(started)
        attempt = started["result"]["artifact"]
        observed = self._ok(self._finished(attempt, timeout=8))
        self.oracle_thread.join(timeout=2)
        expected = executor_selected and helper_selected and supplied
        self.assertEqual(self.oracle_observations, [{"present": expected, "unchanged": expected}])
        result = json.loads((self.root / "helper-output/result.json").read_bytes())
        self.assertEqual(result["output_available"], expected)
        self.assertIsNone(result["semantic_result"])
        self.assertEqual(observed["process_end"]["returncode"], 0 if expected else 1)
        invocation = json.loads((self.root / "helper-output/invocation.json").read_bytes())
        if helper_selected:
            self.assertEqual(invocation["environment_passthrough"],
                             [{"name": NAME, "present": executor_selected and supplied}])
        else:
            self.assertNotIn("environment_passthrough", invocation)
        retained = self._ok(self._public("evidence.read", {"artifact": attempt}))["envelope"]["payload"]
        if executor_selected:
            self.assertEqual(retained["invocation"]["environment_passthrough"], [{"name": NAME, "present": supplied}])
        else:
            self.assertNotIn("environment_passthrough", retained["invocation"])
        (self.root / "ORACLE.json").write_bytes(c.canonical({
            "observations": self.oracle_observations,
            "scope": "Synthetic value compared in memory after actual dispatcher/supervisor/helper/vendor traversal; no model or real credentials"}))
        for path in self.root.rglob("*"):
            if path.is_file():
                self.assertFalse(self.sentinel.encode() in path.read_bytes(), str(path.relative_to(self.root)))

    def test_selected_value_crosses_complete_native_path_without_retention(self):
        self._whole_path(executor_selected=True, helper_selected=True, supplied=True)

    def test_selected_missing_value_remains_missing_and_transport_fails(self):
        self._whole_path(executor_selected=True, helper_selected=True, supplied=False)

    def test_no_selection_preserves_exact_environment_behavior(self):
        self._whole_path(executor_selected=False, helper_selected=False, supplied=True)

    def test_helper_selection_cannot_recover_value_dropped_by_supervisor(self):
        self._whole_path(executor_selected=False, helper_selected=True, supplied=True)

    def test_executor_selection_does_not_enable_unselected_helper(self):
        self._whole_path(executor_selected=True, helper_selected=False, supplied=True)

    def test_preflight_refuses_unsupported_or_value_bearing_selection(self):
        for selected in (["PATH"], [NAME, NAME], {NAME: "not-a-credential"}, NAME):
            with self.subTest(selection_type=type(selected).__name__):
                self.f.policy["executors"]["registered"]["settings"]["environment_passthrough"] = selected
                self._select_policy()
                response = self._public("contract.preflight", {"context": self._assemble(),
                    "grant_id": "work", "executor_id": "registered", "result_key": "refused-selection", "observations": []})
                self.assertEqual(response["refusal"]["code"], "unsupported_executor")

    def test_serialized_credential_is_refused_by_preflight_and_helper(self):
        document = self._prepare(True, True, False)
        executor = self.f.policy["executors"]["registered"]
        executor["environment"][NAME] = "invalid-inline-test-data"
        self._select_policy()
        refused = self._public("contract.preflight", {"context": self._assemble(),
            "grant_id": "work", "executor_id": "registered", "result_key": "refused-inline", "observations": []})
        self.assertEqual(refused["refusal"]["code"], "unsupported_executor")
        helper = self.code.parent / "examples/fd-support/actor_cli.py"
        for selected, explicit, backend in [(["PATH"], {}, "claude"), ([NAME, NAME], {}, "claude"),
                                            ([NAME], {NAME: "invalid-inline-test-data"}, "claude"),
                                            ([NAME], {}, "codex")]:
            document["settings"]["environment_passthrough"] = selected
            document["environment"] = explicit
            document["backend"] = backend
            document["decoder"] = "claude-result-json/1" if backend == "claude" else "codex-final-jsonl/1"
            path = self.root / "invalid-plan.json"
            path.write_bytes(c.canonical(document))
            result = subprocess.run([str(self.python), "-B", str(helper), "--plan", str(path),
                    "--plan-sha256", hashlib.sha256(path.read_bytes()).hexdigest()],
                    input=b"", capture_output=True, env=self.dispatch_environment, timeout=5)
            self.assertEqual(result.returncode, 2)
            self.assertFalse((self.root / "helper-output").exists())


if __name__ == "__main__":
    unittest.main()
