"""Source-derived controls for actual public CLI and legacy MCP subprocesses.

The operator example supplies deterministic boundary fixtures only. These tests
make no F_P usability, independent semantic review or benefit claim.
"""
from __future__ import annotations

import base64
from collections.abc import Iterator, Sequence
from decimal import Decimal
import fcntl
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from typing import Any, cast
import unittest
from test_ac_support_core import Fixture
import ac_support_core as core


TENANT = Path(__file__).resolve().parents[1]
PRODUCT = TENANT.parents[1]
ADAPTER = TENANT / "code" / "ac_support.py"
PREPARE = TENANT / "examples" / "fd-support" / "prepare_readonly.py"
OPERATIONS = {
    "tools.describe", "workspace.observe", "source.read", "records.find", "records.read",
    "graph.project", "relations.query", "context.assemble", "contract.preflight", "dispatch.start",
    "dispatch.observe", "dispatch.cancel", "events.wait", "return.capture", "return.check",
    "review.prepare", "checks.evaluate", "results.conjoin", "work.project", "work.write",
    "refresh.prepare", "resources.aggregate", "evidence.read",
}
RESPONSE_KEYS = {"schema", "id", "operation", "status", "result", "refusal", "operation_outcome", "evidence"}


def canonical(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def descendants(value: object) -> Iterator[object]:
    yield value
    if isinstance(value, dict):
        for item in value.values():
            yield from descendants(item)
    elif isinstance(value, list):
        for item in value:
            yield from descendants(item)


class PublicInterfaceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="a-c-interface-")
        self.addCleanup(self.temporary.cleanup)
        self.parent = Path(self.temporary.name).resolve()
        self.addCleanup(self.retain_public_evidence)
        self.call_sequence = 0
        self.example = self.parent / "demo"
        self.environment = dict(os.environ)
        self.environment["PYTHONDONTWRITEBYTECODE"] = "1"
        result = subprocess.run(
            [sys.executable, str(PREPARE), "--out", str(self.example), "--product-root", str(PRODUCT)],
            capture_output=True, timeout=30, env=self.environment, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr.decode("utf-8", errors="replace"))
        self.setup = cast(dict[str, Any], json.loads(result.stdout))
        self.policy = self.example / "policy.json"
        self.sha = cast(str, self.setup["policy_sha256"])

    def retain_public_evidence(self) -> None:
        destination = os.environ.get("AC_PUBLIC_INTERFACE_TEST_EVIDENCE")
        if destination is not None:
            import shutil
            target = Path(destination) / self.id().rsplit(".", 1)[-1]
            shutil.copytree(self.parent, target, symlinks=True)

    def retain_call(self, command: list[str], raw: bytes, result: subprocess.CompletedProcess[bytes]) -> None:
        self.call_sequence += 1
        target = self.parent / "transport-calls" / str(self.call_sequence)
        target.mkdir(parents=True)
        (target / "stdin").write_bytes(raw)
        (target / "stdout").write_bytes(result.stdout)
        (target / "stderr").write_bytes(result.stderr)
        (target / "call.json").write_bytes(canonical({"command": command, "returncode": result.returncode,
                                                     "scope": "actual local CLI/MCP boundary fixture; no F_P actor"}))

    def command(self, principal: str = "executive", *, sha: str | None = None) -> list[str]:
        return [sys.executable, str(ADAPTER), "--policy", str(self.policy),
                "--policy-sha256", self.sha if sha is None else sha, "--principal", principal]

    def invoke(self, request: dict[str, Any] | bytes, *, principal: str = "executive",
               sha: str | None = None) -> tuple[subprocess.CompletedProcess[bytes], dict[str, Any]]:
        raw = request if isinstance(request, bytes) else canonical(request)
        result = subprocess.run(self.command(principal, sha=sha) + ["call", "--request", "-"],
                                input=raw, capture_output=True, timeout=30, env=self.environment, check=False)
        self.retain_call(self.command(principal, sha=sha) + ["call", "--request", "-"], raw, result)
        response = cast(dict[str, Any], json.loads(result.stdout))
        self.assertEqual(set(response), RESPONSE_KEYS)
        self.assertEqual(len(result.stdout.splitlines()), 1)
        return result, response

    def session(self, messages: Sequence[dict[str, Any] | bytes], *, principal: str = "reviewer") -> tuple[subprocess.CompletedProcess[bytes], list[dict[str, Any]]]:
        raw = b"".join((message if isinstance(message, bytes) else canonical(message)) + b"\n" for message in messages)
        result = subprocess.run(self.command(principal) + ["mcp"], input=raw, capture_output=True,
                                timeout=30, env=self.environment, check=False)
        self.retain_call(self.command(principal) + ["mcp"], raw, result)
        responses = [cast(dict[str, Any], json.loads(line)) for line in result.stdout.splitlines()]
        self.assertTrue(all(message["jsonrpc"] == "2.0" for message in responses))
        return result, responses

    def request_file(self, name: str) -> dict[str, Any]:
        return cast(dict[str, Any], json.loads((self.example / "requests" / name).read_bytes()))

    def rewrite_policy(self, policy: dict[str, Any]) -> None:
        raw = canonical(policy)
        self.policy.write_bytes(raw)
        self.sha = hashlib.sha256(raw).hexdigest()

    @staticmethod
    def initialize(version: str = "2025-11-25") -> list[dict[str, Any]]:
        return [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
                "protocolVersion": version, "capabilities": {}, "clientInfo": {"name": "ordinary-control", "version": "1"},
            }},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
        ]

    def test_demo_is_readonly_and_does_not_overwrite_existing_configuration(self) -> None:
        policy = json.loads(self.policy.read_bytes())
        self.assertEqual(policy["grants"], {})
        self.assertEqual(policy["executors"], {})
        self.assertEqual(self.setup["model_calls"], 0)
        before = self.policy.read_bytes()
        result = subprocess.run([sys.executable, str(PREPARE), "--out", str(self.example)],
                                capture_output=True, timeout=30, env=self.environment, check=False)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(self.policy.read_bytes(), before)

    def test_all_three_principals_discover_real_contracts(self) -> None:
        for principal in ("executive", "worker", "reviewer"):
            with self.subTest(principal=principal):
                result, response = self.invoke(self.request_file("describe.json"), principal=principal)
                self.assertEqual(result.returncode, 0, response)
                self.assertEqual(response["status"], "ok")
                value = response["result"]["value"]
                self.assertEqual({item["name"] for item in value["operations"]}, OPERATIONS)
                self.assertIn("RelationDeclarations", value["content_schemas"]["$defs"])
                self.assertIn("RelationQueryResult", value["content_schemas"]["$defs"])
                self.assertEqual(response["operation_outcome"]["value"], "returned")
                self.assertTrue(response["evidence"]["id"].startswith("sha256:"))

    def test_setup_selects_canonical_operator_paths_before_runtime_binding(self) -> None:
        actual_parent = self.parent / "actual-operator-directory"
        actual_parent.mkdir()
        alias = self.parent / "operator-parent-alias"
        alias.symlink_to(actual_parent, target_is_directory=True)
        output = alias / "canonical-demo"
        setup = subprocess.run([sys.executable, str(PREPARE), "--out", str(output), "--product-root", str(PRODUCT)],
                               capture_output=True, timeout=30, env=self.environment, check=False)
        self.assertEqual(setup.returncode, 0, setup.stderr)
        selected = json.loads(setup.stdout)
        self.assertEqual(Path(selected["output"]), actual_parent / "canonical-demo")
        command = [sys.executable, str(ADAPTER), "--policy", selected["policy"], "--policy-sha256",
                   selected["policy_sha256"], "--principal", "worker", "call", "--request", "-"]
        raw = (Path(selected["output"]) / "requests/read-product.json").read_bytes()
        result = subprocess.run(command, input=raw, capture_output=True, timeout=30, env=self.environment, check=False)
        self.retain_call(command, raw, result)
        self.assertEqual(result.returncode, 0, result.stdout)
        # A separately selected bad policy with an aliased protected evidence
        # binding is refused. The test does not invent a prohibition on a
        # trusted startup policy locator's ancestors when its bytes match.
        bad_policy = json.loads(Path(selected["policy"]).read_bytes())
        bad_policy["evidence_root"] = str(output / "evidence")
        bad_policy["product"]["authority_binding"]["result_surface"]["root"] = str(output / "evidence")
        bad_path = Path(selected["output"]) / "aliased-evidence-policy.json"
        bad_raw = canonical(bad_policy)
        bad_path.write_bytes(bad_raw)
        command[command.index("--policy") + 1] = str(bad_path)
        command[command.index("--policy-sha256") + 1] = hashlib.sha256(bad_raw).hexdigest()
        refused = subprocess.run(command, input=raw, capture_output=True, timeout=30, env=self.environment, check=False)
        self.retain_call(command, raw, refused)
        self.assertEqual(refused.returncode, 2, refused.stdout)
        self.assertEqual(json.loads(refused.stdout)["refusal"]["code"], "path_refused")

    def test_file_and_stdin_acquire_actual_source_for_worker(self) -> None:
        request = self.request_file("read-product.json")
        result, response = self.invoke(request, principal="worker")
        self.assertEqual(result.returncode, 0, response)
        content = (PRODUCT / "stdo_a_c.json").read_text(encoding="utf-8")
        self.assertIn(content, list(descendants(response["result"])))
        result = subprocess.run(self.command("worker") + ["call", "--request", str(self.example / "requests" / "read-product.json")],
                                capture_output=True, timeout=30, env=self.environment, check=False)
        self.assertEqual(result.returncode, 0, result.stdout.decode("utf-8", errors="replace"))
        self.assertIn(content, list(descendants(json.loads(result.stdout)["result"])))

    def test_original_operation_evidence_is_acquirable_in_fresh_cli(self) -> None:
        _, response = self.invoke(self.request_file("read-product.json"), principal="worker")
        evidence = response["evidence"]
        request = {"schema": "a_c.fd-support.request/1", "id": "fresh-evidence-reader",
                   "operation": "evidence.read", "arguments": {"artifact": evidence}}
        result, acquired = self.invoke(request, principal="reviewer")
        self.assertEqual(result.returncode, 0, acquired)
        envelopes = [item for item in descendants(acquired["result"]) if isinstance(item, dict)
                     and item.get("schema") == "a_c.fd-support.artifact/1" and item.get("kind") == "operation"]
        self.assertTrue(envelopes, acquired)
        self.assertTrue(any(hashlib.sha256(canonical(item)).hexdigest() == evidence["sha256"] for item in envelopes))

    def test_strict_cli_input_rejects_unbound_grammar(self) -> None:
        controls = [
            b'{"schema":"a_c.fd-support.request/1","id":"a","id":"b","operation":"tools.describe","arguments":{}}',
            b'{"schema":"a_c.fd-support.request/1","id":"a","operation":"tools.describe","arguments":{"operation":1.0}}',
            b'{"schema":"a_c.fd-support.request/2","id":"a","operation":"tools.describe","arguments":{}}',
            b'{"schema":"a_c.fd-support.request/1","id":"a","operation":"unknown","arguments":{}}',
            b'{"schema":"a_c.fd-support.request/1","id":"a","operation":"tools.describe","arguments":{},"principal":"owner"}',
            b'\xff',
        ]
        for raw in controls:
            with self.subTest(raw=raw):
                result, response = self.invoke(raw)
                self.assertEqual(result.returncode, 2, response)
                self.assertEqual(response["status"], "refused")
                self.assertIsNone(response["operation_outcome"])
                self.assertIsNone(response["evidence"])

    def test_unavailable_ref_preserves_original_cli_refusal_and_durable_operation(self) -> None:
        missing = {"id": "sha256:" + "0" * 64, "sha256": "0" * 64}
        request = {"schema": "a_c.fd-support.request/1", "id": "missing-evidence-cli",
                   "operation": "evidence.read", "arguments": {"artifact": missing}}
        result, refused = self.invoke(request, principal="reviewer")
        self.assertEqual(result.returncode, 2, refused)
        self.assertEqual(refused["status"], "refused")
        self.assertEqual(refused["refusal"]["code"], "source_missing")
        self.assertEqual(refused["operation_outcome"]["value"], "refused(basis)")
        self.assertIsNotNone(refused["evidence"])
        acquisition = {"schema": "a_c.fd-support.request/1", "id": "acquire-missing-evidence-refusal",
                       "operation": "evidence.read", "arguments": {"artifact": refused["evidence"]}}
        acquired_result, acquired = self.invoke(acquisition, principal="reviewer")
        self.assertEqual(acquired_result.returncode, 0, acquired)
        values = list(descendants(acquired["result"]))
        self.assertIn(request, values)
        self.assertIn(refused["refusal"], values)

    def test_unavailable_ref_is_mcp_tool_refusal_with_acquirable_original_evidence(self) -> None:
        request = {"schema": "a_c.fd-support.request/1", "id": "missing-evidence-mcp", "operation": "evidence.read",
                   "arguments": {"artifact": {"id": "sha256:" + "0" * 64, "sha256": "0" * 64}}}
        result, messages = self.session([*self.initialize(), {"jsonrpc": "2.0", "id": 2, "method": "tools/call",
                                       "params": {"name": "evidence.read", "arguments": request}}])
        self.assertEqual(result.returncode, 0, result.stderr)
        tool = messages[-1]["result"]
        self.assertTrue(tool["isError"])
        response = tool["structuredContent"]
        self.assertEqual(json.loads(tool["content"][0]["text"]), response)
        self.assertEqual(response["refusal"]["code"], "source_missing")
        self.assertEqual(response["operation_outcome"]["value"], "refused(basis)")
        result, acquired = self.invoke({"schema": "a_c.fd-support.request/1", "id": "mcp-refusal-fresh-cli",
                                       "operation": "evidence.read", "arguments": {"artifact": response["evidence"]}}, principal="reviewer")
        self.assertEqual(result.returncode, 0, acquired)
        self.assertIn(request, list(descendants(acquired["result"])))

    def test_policy_digest_and_fixed_principal_cannot_be_replaced_by_request(self) -> None:
        _, response = self.invoke(self.request_file("describe.json"), sha="0" * 64)
        self.assertEqual(response["refusal"]["code"], "digest_mismatch")
        self.assertIsNone(response["operation_outcome"])
        _, response = self.invoke(self.request_file("describe.json"), principal="caller-minted-owner")
        self.assertEqual(response["refusal"]["code"], "authority_missing")
        self.assertIsNone(response["evidence"])

    def test_valid_preflight_is_denied_without_work_grant_or_executor(self) -> None:
        result, response = self.invoke(self.request_file("denied-preflight.json"))
        self.assertEqual(result.returncode, 2, response)
        self.assertEqual(response["status"], "refused")
        self.assertIsNotNone(response["refusal"])
        self.assertNotEqual(response.get("result", {}), {"decision": "admitted"})

    def test_documented_mcp_session_uses_shared_schemas_and_actual_source(self) -> None:
        raw = (self.example / "mcp-session.jsonl").read_bytes()
        result = subprocess.run(self.command("reviewer") + ["mcp"], input=raw, capture_output=True,
                                timeout=30, env=self.environment, check=False)
        self.assertEqual(result.returncode, 0, result.stderr.decode("utf-8", errors="replace"))
        responses = [json.loads(line) for line in result.stdout.splitlines()]
        self.assertEqual([item["id"] for item in responses], [1, 2, 3])
        self.assertEqual(responses[0]["result"]["protocolVersion"], "2025-11-25")
        tools = responses[1]["result"]["tools"]
        self.assertEqual({item["name"] for item in tools}, OPERATIONS)
        self.assertEqual([item["name"] for item in tools], sorted(OPERATIONS))
        for tool in tools:
            self.assertEqual(tool["inputSchema"]["properties"]["operation"]["const"], tool["name"])
            self.assertEqual(set(tool["inputSchema"]["required"]), {"schema", "id", "operation", "arguments"})
            self.assertEqual(tool["outputSchema"]["type"], "object")
            self.assertEqual(set(tool["outputSchema"]["required"]), RESPONSE_KEYS)
        returned = responses[2]["result"]
        self.assertFalse(returned["isError"])
        self.assertEqual(json.loads(returned["content"][0]["text"]), returned["structuredContent"])
        self.assertIn((PRODUCT / "stdo_a_c.json").read_text(), list(descendants(returned["structuredContent"]["result"])))

    def test_mcp_protocol_errors_are_separate_from_bound_tool_refusal(self) -> None:
        read = self.request_file("read-product.json")
        denied = self.request_file("denied-preflight.json")
        messages = [
            {"jsonrpc": "2.0", "id": "early", "method": "tools/list"},
            *self.initialize("2099-01-01"),
            {"jsonrpc": "2.0", "id": 2, "method": "ping"},
            {"jsonrpc": "2.0", "id": 3, "method": "server/discover"},
            {"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "unknown", "arguments": read}},
            {"jsonrpc": "2.0", "id": 5, "method": "tools/call", "params": {"name": "tools.describe", "arguments": read}},
            {"jsonrpc": "2.0", "id": 6, "method": "tools/call", "params": {"name": "source.read", "arguments": {"source": {}}}},
            {"jsonrpc": "2.0", "id": 7, "method": "tools/call", "params": {"name": "contract.preflight", "arguments": denied}},
            {"jsonrpc": "2.0", "id": 8, "method": "tools/call", "params": {"name": "source.read", "arguments": read}},
        ]
        result, responses = self.session(messages)
        self.assertEqual(result.returncode, 0)
        by_id = {item["id"]: item for item in responses}
        self.assertIn("error", by_id["early"])
        self.assertEqual(by_id[1]["result"]["protocolVersion"], "2025-11-25")
        self.assertEqual(by_id[2]["result"], {})
        self.assertEqual(by_id[3]["error"]["code"], -32601)
        for identity in (4, 5, 6):
            self.assertEqual(by_id[identity]["error"]["code"], -32602)
        self.assertTrue(by_id[7]["result"]["isError"])
        self.assertEqual(by_id[7]["result"]["structuredContent"]["status"], "refused")
        self.assertFalse(by_id[8]["result"]["isError"])
        self.assertEqual(by_id[8]["result"]["structuredContent"]["id"], read["id"])

    def test_mcp_notifications_never_run_a_tool_or_emit_responses(self) -> None:
        result, responses = self.session([
            *self.initialize(),
            {"jsonrpc": "2.0", "method": "tools/call", "params": {"name": "source.read", "arguments": self.request_file("read-product.json")}},
            {"jsonrpc": "2.0", "method": "notifications/cancelled", "params": {"requestId": 99}},
        ])
        self.assertEqual(result.returncode, 0)
        self.assertEqual([item["id"] for item in responses], [1])
        self.assertEqual(list((self.example / "evidence").rglob("*.json")), [])

    def test_mcp_strict_json_and_invalid_id_do_not_activate_tools(self) -> None:
        result, responses = self.session([
            b'{"jsonrpc":"2.0","id":NaN,"method":"ping"}',
            b'{"jsonrpc":"2.0","id":1,"id":2,"method":"ping"}',
            b'\xff',
            {"jsonrpc": "2.0", "id": True, "method": "ping"},
            *self.initialize(),
        ])
        self.assertEqual(result.returncode, 0)
        self.assertEqual([item["error"]["code"] for item in responses[:4]], [-32700, -32700, -32700, -32600])
        self.assertEqual(responses[-1]["result"]["protocolVersion"], "2025-11-25")

    def test_framing_bound_refuses_before_parsing_or_effect(self) -> None:
        policy = json.loads(self.policy.read_bytes())
        policy["limits"]["max_message_bytes"] = 256
        self.rewrite_policy(policy)
        result, response = self.invoke(b" " * 1024)
        self.assertEqual(result.returncode, 2)
        self.assertIsNone(response["operation_outcome"])
        result, responses = self.session([b" " * 1024])
        self.assertEqual(result.returncode, 2)
        self.assertEqual(responses[0]["error"]["code"], -32700)

    def test_mcp_optional_metadata_client_info_and_capabilities_are_data(self) -> None:
        opening = self.initialize()
        opening[0]["params"].update({
            "_meta": {"progressToken": 1.0, "example.org/trace": {"ratio": 0.5}},
            "clientInfo": {"name": "ordinary-extended-client", "version": "1", "title": "Caller",
                           "description": "Public protocol control", "websiteUrl": "https://example.org",
                           "icons": [{"src": "https://example.org/icon.png", "mimeType": "image/png", "sizes": ["48x48"]}]},
            "capabilities": {"roots": {"listChanged": True}, "sampling": {}, "elicitation": {"form": {}},
                             "experimental": {"example.org/timing": {"ratio": 0.25}}},
        })
        opening[1]["params"] = {"_meta": {"example.org/ready": {"ratio": 0.5}}}
        read = self.request_file("read-product.json")
        result, responses = self.session([
            *opening,
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {"_meta": {"progressToken": "list-token"}}},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {
                "name": "source.read", "arguments": read,
                "_meta": {"progressToken": 2.5, "example.org/trace": {"ratio": 0.125, "principal": "caller-minted-owner"}},
            }},
        ])
        self.assertEqual(result.returncode, 0, result.stderr.decode("utf-8", errors="replace"))
        self.assertEqual([item["id"] for item in responses], [1, 2, 3])
        self.assertEqual(responses[0]["result"]["protocolVersion"], "2025-11-25")
        tool = responses[2]["result"]
        self.assertFalse(tool["isError"])
        self.assertEqual(set(tool["structuredContent"]), RESPONSE_KEYS)
        self.assertEqual(tool["structuredContent"]["id"], read["id"])

    def test_mcp_numeric_transport_ids_roundtrip_without_float_rounding(self) -> None:
        numeric_id = "9007199254740993.0000000000000001"
        raw = ('{"jsonrpc":"2.0","id":' + numeric_id + ',"method":"ping","params":{"_meta":{"ratio":0.25}}}').encode()
        result, responses = self.session([raw])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(responses[0]["result"], {})
        self.assertIn(('"id":' + numeric_id).encode(), result.stdout)
        exact = json.loads(result.stdout, parse_float=Decimal)
        self.assertEqual(exact["id"], Decimal(numeric_id))

    def test_mcp_decimal_and_exponent_tokens_stay_refused_in_public_envelope(self) -> None:
        request = self.request_file("read-product.json")
        request["arguments"]["max_content_bytes"] = 1
        for token in (b"1.0", b"1e0", b"1E+0"):
            with self.subTest(token=token):
                raw = canonical({"jsonrpc": "2.0", "id": 7, "method": "tools/call", "params": {
                    "name": "source.read", "arguments": request, "_meta": {"ratio": 0.5},
                }})
                raw = raw.replace(b'"max_content_bytes":1', b'"max_content_bytes":' + token)
                result, responses = self.session([*self.initialize(), raw])
                self.assertEqual(result.returncode, 0)
                self.assertEqual(responses[-1]["error"]["code"], -32602)
                self.assertNotIn("result", responses[-1])

    def test_nonfinite_transport_metadata_and_duplicate_keys_remain_parse_errors(self) -> None:
        result, responses = self.session([
            b'{"jsonrpc":"2.0","id":1,"method":"ping","params":{"_meta":{"ratio":Infinity}}}',
            b'{"jsonrpc":"2.0","id":2,"method":"ping","params":{"_meta":{"ratio":-Infinity}}}',
            b'{"jsonrpc":"2.0","id":3,"method":"ping","params":{"_meta":{"ratio":NaN}}}',
            b'{"jsonrpc":"2.0","id":4,"method":"ping","params":{"_meta":{"trace":1,"trace":2}}}',
        ])
        self.assertEqual(result.returncode, 0)
        self.assertEqual([item["error"]["code"] for item in responses], [-32700] * 4)

    def test_source_symlink_refuses_through_public_source_route(self) -> None:
        policy = json.loads(self.policy.read_bytes())
        policy["sources"]["operator"]["read_scope"].append({"path": "link.md", "kind": "file"})
        self.rewrite_policy(policy)
        (self.example / "control" / "link.md").symlink_to("OPERATOR.md")
        ref = policy["principals"]["worker"]["role_binding"].copy()
        ref["path"] = "link.md"
        result, response = self.invoke({"schema": "a_c.fd-support.request/1", "id": "symlink-control", "operation": "source.read", "arguments": {"source": ref, "encoding": "utf8"}}, principal="worker")
        self.assertEqual(result.returncode, 2, response)
        self.assertEqual(response["refusal"]["code"], "path_refused")
        self.assertNotIn((self.example / "control" / "OPERATOR.md").read_text(), list(descendants(response["result"])))

    def test_observe_sees_dirty_bytes_without_a_commit_proxy(self) -> None:
        policy = json.loads(self.policy.read_bytes())
        policy["sources"]["operator"]["read_scope"].append({"path": "OBSERVED.txt", "kind": "file"})
        self.rewrite_policy(policy)
        observed = self.example / "control" / "OBSERVED.txt"
        observed.write_bytes(b"before\n")
        request: dict[str, Any] = {"schema": "a_c.fd-support.request/1", "id": "observe-before", "operation": "workspace.observe",
                                   "arguments": {"scope": [{"root": "operator", "path": "OBSERVED.txt", "kind": "file"}]}}
        result, before = self.invoke(request)
        self.assertEqual(result.returncode, 0, before)
        observed.write_bytes(b"after\n")
        request["id"] = "observe-after"
        request["arguments"]["previous"] = before["result"]["artifact"]
        result, after = self.invoke(request)
        self.assertEqual(result.returncode, 0, after)
        self.assertIn(hashlib.sha256(b"after\n").hexdigest(), list(descendants(after["result"])))
        self.assertIn(hashlib.sha256(b"before\n").hexdigest(), list(descendants(after["result"])))


class PublicWriterReplayTests(unittest.TestCase):
    """Real CLI/MCP Writer composition; injected barriers are test-only."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="ac-public-writer-")
        self.root = Path(self.temporary.name).resolve()
        self.f = Fixture(self.root)
        self.sequence = 0
        self.python = Path(sys.executable).resolve()
        self.environment = {"PATH": os.defpath, "PYTHONDONTWRITEBYTECODE": "1"}
        self.policy = self.root / "policy.json"
        self.select_policy()

    def tearDown(self) -> None:
        selected = os.environ.get("AC_PUBLIC_INTERFACE_TEST_EVIDENCE")
        if selected is not None:
            import shutil
            shutil.copytree(self.root, Path(selected) / self.id().rsplit(".", 1)[-1])
        self.temporary.cleanup()

    def select_policy(self) -> None:
        raw = canonical(self.f.policy)
        self.policy.write_bytes(raw)
        self.policy_sha = hashlib.sha256(raw).hexdigest()

    def request(self, identity: str, mode: str = "append") -> dict[str, Any]:
        target = self.f.write("outputs/" + identity + ".txt", b"before\n")
        return {"schema": "a_c.fd-support.request/1", "id": identity, "operation": "work.write", "arguments": {"grant_id": "work", "target": target, "mode": mode, "record": {"text": "after\n", "provenance": self.f.law}, "interpretation": None, "observations": []}}

    def prepare_call(self, request: dict[str, Any], *, principal: str = "worker", transport: str = "cli", hook: str | None = None) -> tuple[list[str], bytes | None, Path]:
        self.sequence += 1
        folder = self.root / "calls" / str(self.sequence).zfill(3)
        folder.mkdir(parents=True)
        (folder / "request.json").write_bytes(canonical(request))
        entry = ADAPTER
        if hook is not None:
            entry = folder / "barrier.py"
            source = "import sys,time\nfrom pathlib import Path\nfrom contextlib import contextmanager\n"
            source += f"sys.path.insert(0,{str(ADAPTER.parent)!r})\nimport ac_support as a,ac_support_core as c,ac_support_effects as e\n"
            if hook in ("plan", "contender"):
                source += "original_plan=c.prepare_write\ndef plan(runtime,request):\n"
                source += f" Path({str(self.root / (hook + '-planning'))!r}).write_text(str(time.time_ns()))\n"
                if hook == "plan":
                    source += f" deadline=time.monotonic()+8\n while not Path({str(self.root / 'release-planning')!r}).exists():\n  if time.monotonic()>deadline: raise RuntimeError('Test barrier expired')\n  time.sleep(0.005)\n"
                source += " return original_plan(runtime,request)\nc.prepare_write=plan\n"
                if hook == "contender":
                    source += "original_lock=e.EvidenceStore._lock\n@contextmanager\ndef lock(store,identity,*,nonblocking=False):\n"
                    source += f" if identity.startswith('request:'): Path({str(self.root / 'contender-attempted')!r}).write_text(str(time.time_ns()))\n"
                    source += " with original_lock(store,identity,nonblocking=nonblocking):\n"
                    source += f"  if identity.startswith('request:'): Path({str(self.root / 'contender-acquired')!r}).write_text(str(time.time_ns()))\n  yield\ne.EvidenceStore._lock=lock\n"
            else:
                boundary = "writer:after_target_publication" if hook == "fatal-target" else "writer_intent:before_publish"
                source += f"def fault(point):\n if point=={boundary!r}: raise SystemExit(77)\ne._fault=fault\n"
            entry.write_text(source + "raise SystemExit(a.main())\n")
        argv = [str(self.python), "-B", str(entry), "--policy", str(self.policy), "--policy-sha256", self.policy_sha, "--principal", principal]
        wire = None
        if transport == "mcp":
            argv.append("mcp")
            messages = [{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-11-25", "capabilities": {}, "clientInfo": {"name": "writer-control", "version": "1"}}}, {"jsonrpc": "2.0", "method": "notifications/initialized"}, {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "work.write", "arguments": request}}]
            wire = b"".join(canonical(message) + b"\n" for message in messages)
            (folder / "stdin").write_bytes(wire)
        else:
            argv += ["call", "--request", str(folder / "request.json")]
        (folder / "command.json").write_bytes(canonical({"argv": argv, "cwd": str(self.root), "policy_sha256": self.policy_sha, "transport": transport, "test_hook": hook, "started_ns": time.time_ns()}))
        return argv, wire, folder

    def record(self, folder: Path, result: subprocess.CompletedProcess[bytes]) -> None:
        (folder / "stdout").write_bytes(result.stdout); (folder / "stderr").write_bytes(result.stderr)
        (folder / "ended.json").write_bytes(canonical({"returncode": result.returncode, "ended_ns": time.time_ns()}))

    @staticmethod
    def response(folder: Path, transport: str = "cli") -> dict[str, Any]:
        if transport == "mcp":
            messages = [json.loads(line) for line in (folder / "stdout").read_bytes().splitlines()]
            return cast(dict[str, Any], next(message for message in messages if message.get("id") == 2)["result"]["structuredContent"])
        return cast(dict[str, Any], json.loads((folder / "stdout").read_bytes()))

    def call(self, request: dict[str, Any], *, principal: str = "worker", transport: str = "cli", hook: str | None = None) -> Path:
        argv, wire, folder = self.prepare_call(request, principal=principal, transport=transport, hook=hook)
        result = subprocess.run(argv, input=wire, capture_output=True, cwd=self.root, env=self.environment, timeout=12, check=False)
        self.record(folder, result)
        return folder

    def target(self, request: dict[str, Any]) -> Path:
        return self.f.workspace / cast(str, request["arguments"]["target"]["path"])

    def isolated(self, name: str) -> None:
        root = self.root / name; root.mkdir()
        self.f = Fixture(root)
        self.select_policy()

    def remove_owner(self, request: dict[str, Any], suffix: str) -> None:
        key = core.digest({"product": "urn:test:product", "principal": "worker", "id": request["id"]})
        marker = self.f.evidence / "requests" / (key + "." + suffix + ".json")
        before = {str(path.relative_to(self.f.evidence)): hashlib.sha256(path.read_bytes()).hexdigest() for path in self.f.evidence.rglob("*") if path.is_file()}
        saved = self.root / "removed-owners" / (str(self.sequence) + "-" + suffix)
        saved.mkdir(parents=True)
        (saved / "marker.bin").write_bytes(marker.read_bytes())
        marker.unlink()
        after = {str(path.relative_to(self.f.evidence)): hashlib.sha256(path.read_bytes()).hexdigest() for path in self.f.evidence.rglob("*") if path.is_file()}
        self.assertEqual(set(before) - set(after), {str(marker.relative_to(self.f.evidence))})
        self.assertTrue(all(before[name] == value for name, value in after.items()))
        (saved / "removal.json").write_bytes(canonical({"removed_only": str(marker), "sha256": hashlib.sha256((saved / "marker.bin").read_bytes()).hexdigest(), "other_files_unchanged": len(after)}))

    def claim_path(self, request: dict[str, Any]) -> Path:
        key = core.digest({"product": "urn:test:product", "principal": "worker", "id": request["id"]})
        return self.f.evidence / "requests" / (key + ".claim.json")

    def test_lost_claim_cli_mcp_distinguish_known_conflict_from_exact_history_gap(self) -> None:
        for transport in ("cli", "mcp"):
            for changed in (False, True):
                with self.subTest(transport=transport, changed=changed):
                    self.isolated(transport + "-" + str(changed))
                    request = self.request("lost-claim")
                    first = self.response(self.call(request, transport=transport), transport)
                    self.assertEqual(first["status"], "ok", first)
                    self.remove_owner(request, "claim")
                    replay = json.loads(json.dumps(request))
                    if changed:
                        replay["arguments"]["record"]["text"] = "different requested record\n"
                    response = self.response(self.call(replay, transport=transport), transport)
                    self.assertEqual(response["refusal"]["code"], "request_identity_conflict" if changed else "history_incomplete")
                    self.assertIsNone(response["result"])
                    self.assertFalse(self.claim_path(request).exists())
                    self.assertEqual(self.target(request).read_bytes(), b"before\nafter\n")
                    if changed and transport == "cli":
                        fresh = json.loads(json.dumps(replay)); fresh["id"] = "genuine-fresh-id"
                        fresh["arguments"]["target"]["sha256"] = hashlib.sha256(self.target(request).read_bytes()).hexdigest()
                        response = self.response(self.call(fresh))
                        self.assertEqual(response["status"], "ok", response)
                        self.assertEqual(self.target(request).read_bytes(), b"before\nafter\ndifferent requested record\n")

    def test_lost_claim_changed_valid_policy_cannot_attribute_old_completion(self) -> None:
        request = self.request("lost-policy")
        first = self.response(self.call(request)); self.assertEqual(first["status"], "ok", first)
        self.remove_owner(request, "claim")
        self.f.policy["id"] = "distinct-valid-policy"
        self.select_policy()
        replay = self.response(self.call(request))
        self.assertEqual(replay["refusal"]["code"], "request_identity_conflict")
        self.assertIsNone(replay["result"])
        self.assertFalse(self.claim_path(request).exists())
        self.assertEqual(self.target(request).read_bytes(), b"before\nafter\n")

    def test_lost_claim_uncertain_intent_and_further_owner_loss_never_repeat(self) -> None:
        for variant in ("exact", "changed", "all-owners"):
            with self.subTest(variant=variant):
                self.isolated(variant)
                request = self.request("uncertain-lost-claim")
                failed = self.call(request, hook="fatal-target")
                self.assertEqual(json.loads((failed / "ended.json").read_text())["returncode"], 77)
                self.remove_owner(request, "claim")
                if variant == "all-owners":
                    self.remove_owner(request, "intent")
                replay = json.loads(json.dumps(request))
                if variant == "changed":
                    replay["arguments"]["record"]["text"] = "changed uncertain request"
                response = self.response(self.call(replay))
                self.assertEqual(response["refusal"]["code"], "request_identity_conflict" if variant == "changed" else "history_incomplete")
                self.assertFalse(self.claim_path(request).exists())
                self.assertEqual(self.target(request).read_bytes(), b"before\nafter\n")

    def test_ownerless_same_id_history_blocks_a_changed_request_digest(self) -> None:
        request = self.request("pre-owner-changed")
        failed = self.call(request, hook="uncommitted-intent")
        self.assertEqual(json.loads((failed / "ended.json").read_text())["returncode"], 77)
        self.remove_owner(request, "claim")
        replay = json.loads(json.dumps(request))
        replay["arguments"]["record"]["text"] = "a different digest at the same identity\n"
        response = self.response(self.call(replay))
        self.assertEqual(response["refusal"]["code"], "history_incomplete")
        self.assertIsNone(response["result"])
        self.assertFalse(self.claim_path(request).exists())
        self.assertEqual(list((self.f.evidence / "requests").glob("*.intent.json")), [])
        self.assertEqual(self.target(request).read_bytes(), b"before\n")

    def test_cli_mcp_append_replace_recover_original_unconsumed_result(self) -> None:
        for transport in ("cli", "mcp"):
            for mode in ("append", "replace"):
                with self.subTest(transport=transport, mode=mode):
                    request = self.request(transport + "-" + mode, mode)
                    prior_intents = len(list((self.f.evidence / "requests").glob("*.intent.json"))) if (self.f.evidence / "requests").exists() else 0
                    first_path = self.call(request, transport=transport)
                    # Keep exact first bytes without consuming the response yet.
                    postimage = self.target(request).read_bytes()
                    replay = self.response(self.call(request, transport=transport), transport)
                    first = self.response(first_path, transport)
                    self.assertEqual(first["status"], "ok", first)
                    self.assertEqual(replay["status"], "ok", replay)
                    self.assertEqual(first["result"], replay["result"])
                    self.assertEqual(self.target(request).read_bytes(), postimage)
                    self.assertEqual(len(list((self.f.evidence / "requests").glob("*.intent.json"))), prior_intents + 1)
                    conflict = json.loads(json.dumps(request)); conflict["arguments"]["record"]["text"] = "conflict"
                    refused = self.response(self.call(conflict, transport=transport), transport)
                    self.assertEqual(refused["refusal"]["code"], "request_identity_conflict")
                    self.assertEqual(self.target(request).read_bytes(), postimage)

    def wait_for(self, path: Path) -> None:
        deadline = time.monotonic() + 5
        while not path.exists() and time.monotonic() < deadline:
            time.sleep(0.005)
        self.assertTrue(path.exists(), path)

    def test_simultaneous_identical_cli_calls_serialize_before_fresh_planning(self) -> None:
        request = self.request("concurrent")
        first_argv, _, first_folder = self.prepare_call(request, hook="plan")
        second_argv, _, second_folder = self.prepare_call(request, hook="contender")
        first = subprocess.Popen(first_argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=self.root, env=self.environment)
        second: subprocess.Popen[bytes] | None = None
        try:
            self.wait_for(self.root / "plan-planning")
            second = subprocess.Popen(second_argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=self.root, env=self.environment)
            self.wait_for(self.root / "contender-attempted")
            key = core.digest({"product": "urn:test:product", "principal": "worker", "id": request["id"]})
            lock_path = self.f.evidence / "locks" / (hashlib.sha256(("request:" + key).encode()).hexdigest() + ".lock")
            with lock_path.open("rb") as handle, self.assertRaises(BlockingIOError):
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            self.assertFalse((self.root / "contender-acquired").exists())
            self.assertFalse((self.root / "contender-planning").exists())
        finally:
            (self.root / "release-planning").write_text("release after observed request lock contention")
            stdout, stderr = first.communicate(timeout=10)
            self.record(first_folder, subprocess.CompletedProcess(first_argv, first.returncode, stdout, stderr))
            if second is not None:
                stdout, stderr = second.communicate(timeout=10)
                self.record(second_folder, subprocess.CompletedProcess(second_argv, second.returncode, stdout, stderr))
        first_response = self.response(first_folder); second_response = self.response(second_folder)
        self.assertEqual(first_response["status"], "ok", first_response)
        self.assertEqual(second_response["status"], "ok", second_response)
        self.assertEqual(first_response["result"], second_response["result"])
        self.assertEqual(self.target(request).read_bytes(), b"before\nafter\n")
        self.assertTrue((self.root / "contender-acquired").exists())
        self.assertFalse((self.root / "contender-planning").exists())

    def test_replay_checks_current_roles_principals_grants_and_authority(self) -> None:
        authority = self.f.write("inputs/writer-authority.txt", b"exact current Writer authority")
        core.as_list(core.as_object(core.as_object(self.f.policy["grants"])["work"])["authority_sources"]).append(authority)
        self.select_policy()
        request = self.request("authority")
        first = self.response(self.call(request)); self.assertEqual(first["status"], "ok", first)
        postimage = self.target(request).read_bytes()
        for principal in ("executive", "reviewer", "unregistered"):
            response = self.response(self.call(request, principal=principal))
            self.assertEqual(response["refusal"]["code"], "authority_missing" if principal == "unregistered" else "role_effect_denied")
        grant = core.as_object(core.as_object(self.f.policy["grants"])["work"])
        grant["principals"] = ["executive"]
        self.select_policy()
        self.assertEqual(self.response(self.call(request))["refusal"]["code"], "authority_missing")
        grant["principals"] = ["executive", "worker"]
        self.select_policy()
        (self.f.workspace / "inputs/writer-authority.txt").write_bytes(b"authority advanced")
        self.assertEqual(self.response(self.call(request))["refusal"]["code"], "digest_mismatch")
        self.assertEqual(self.target(request).read_bytes(), postimage)

    def test_fatal_post_target_publication_recovers_held_intent_without_repeat(self) -> None:
        request = self.request("uncertain")
        failed = self.call(request, hook="fatal-target")
        self.assertEqual(json.loads((failed / "ended.json").read_text())["returncode"], 77)
        self.assertEqual((failed / "stdout").read_bytes(), b"")
        self.assertEqual(self.target(request).read_bytes(), b"before\nafter\n")
        recovered = self.response(self.call(request))
        self.assertEqual(recovered["refusal"]["code"], "effect_unreconciled")
        self.assertEqual(recovered["operation_outcome"]["value"], "held(effect)")
        self.assertFalse(recovered["result"]["value"]["repeated"])
        self.assertEqual(self.response(self.call(request))["result"], recovered["result"])
        self.assertEqual(self.target(request).read_bytes(), b"before\nafter\n")

    def test_same_request_under_different_valid_policy_is_a_conflict(self) -> None:
        request = self.request("policy-conflict")
        first = self.response(self.call(request)); self.assertEqual(first["status"], "ok", first)
        self.f.policy["id"] = "valid-distinct-policy-identity"
        self.select_policy()
        refused = self.response(self.call(request))
        self.assertEqual(refused["refusal"]["code"], "request_identity_conflict")
        self.assertEqual(self.target(request).read_bytes(), b"before\nafter\n")

    def test_uncommitted_intent_envelope_is_unknown_history_not_effect_proof(self) -> None:
        request = self.request("uncommitted")
        failed = self.call(request, hook="uncommitted-intent")
        self.assertEqual(json.loads((failed / "ended.json").read_text())["returncode"], 77)
        self.assertEqual(self.target(request).read_bytes(), b"before\n")
        self.assertEqual(list((self.f.evidence / "requests").glob("*.intent.json")), [])
        held = self.response(self.call(request))
        self.assertEqual(held["refusal"]["code"], "history_incomplete")
        self.assertIsNone(held["result"])
        self.assertEqual(self.target(request).read_bytes(), b"before\n")

    def test_missing_tampered_support_and_missing_owner_never_repeat(self) -> None:
        for variant in ("missing-support", "tampered-support", "missing-owner"):
            with self.subTest(variant=variant):
                isolated = self.root / variant
                isolated.mkdir()
                self.f = Fixture(isolated)
                self.select_policy()
                request = self.request(variant)
                first = self.response(self.call(request)); self.assertEqual(first["status"], "ok", first)
                if variant == "missing-owner":
                    key = core.digest({"product": "urn:test:product", "principal": "worker", "id": request["id"]})
                    for suffix in ("outcome", "intent"):
                        (self.f.evidence / "requests" / (key + "." + suffix + ".json")).unlink()
                else:
                    support = self.f.evidence / "objects" / (first["result"]["artifact"]["sha256"] + ".json")
                    if variant == "missing-support":
                        support.unlink()
                    else:
                        support.write_bytes(b"tampered protected support")
                replay = self.response(self.call(request))
                self.assertEqual(replay["refusal"]["code"], {"missing-support": "source_missing", "tampered-support": "digest_mismatch", "missing-owner": "history_incomplete"}[variant])
                self.assertEqual(self.target(request).read_bytes(), b"before\nafter\n")


class PublicJudgmentIngressTests(unittest.TestCase):
    """Registered local stdout -> public capture/check -> relation conditions.

    Fixture verdicts are supplied assertions. Process/capture/consumer evidence
    is observed through fresh public CLI calls, without protected-record writes.
    """

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="ac-fix-judgments-public-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.addCleanup(self.retain_fixture_evidence)
        self.f = Fixture(self.root)
        self.sequence = 0
        self.environment = dict(os.environ)
        self.environment.update({"PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(self.root)})
        self.policy = self.root / "policy.json"
        self.write_policy()
        self.declarations = self.f.relations()
        for raw in core.as_list(self.declarations["applicability"]):
            row = core.as_object(raw)
            if row["target"] == {"kind": "relation", "id": "e1"}:
                row["condition"] = {"predicate": self.f.law, "evaluation": None}
        self.missing = self.query("missing", None)
        self.f.subject = core.as_object(self.edge(self.missing)["expected_subject"])
        self.script = self.f.write("inputs/local-return-producer.py", (
            b"import sys\nfrom pathlib import Path\n"
            b"Path(sys.argv[2]).write_bytes(sys.stdin.buffer.read())\n"
            b"sys.stdout.buffer.write(Path(sys.argv[1]).read_bytes())\n"
            b"sys.stdout.buffer.flush()\n"
        ))

    def retain_fixture_evidence(self) -> None:
        destination = os.environ.get("AC_JUDGMENT_INGRESS_TEST_EVIDENCE")
        if destination is not None:
            import shutil
            target = Path(destination) / self.id().rsplit(".", 1)[-1]
            shutil.copytree(self.root, target)

    def write_policy(self) -> None:
        raw = canonical(self.f.policy)
        self.policy.write_bytes(raw)
        self.policy_sha256 = hashlib.sha256(raw).hexdigest()

    def public(self, operation: str, arguments: object) -> dict[str, Any]:
        self.sequence += 1
        request = {"schema": core.REQUEST, "id": "judgment-ingress-" + str(self.sequence),
                   "operation": operation, "arguments": arguments}
        command = [sys.executable, "-B", str(ADAPTER), "--policy", str(self.policy),
                   "--policy-sha256", self.policy_sha256, "--principal", "executive",
                   "call", "--request", "-"]
        raw = canonical(request)
        started = time.time_ns()
        result = subprocess.run(command, input=raw, capture_output=True, cwd=self.root,
                                timeout=15, env=self.environment, check=False)
        directory = self.root / "calls" / str(self.sequence)
        directory.mkdir(parents=True)
        (directory / "request.json").write_bytes(raw)
        (directory / "stdout").write_bytes(result.stdout)
        (directory / "stderr").write_bytes(result.stderr)
        (directory / "execution.json").write_bytes(canonical({
            "argv": command, "cwd": str(self.root), "exit": result.returncode,
            "started_ns": started, "ended_ns": time.time_ns(),
            "scope": "actual public CLI observation; controlled local producer only",
        }))
        self.assertEqual(result.returncode, 0, (operation, result.stdout, result.stderr))
        response = cast(dict[str, Any], json.loads(result.stdout))
        self.assertEqual(response["status"], "ok", response)
        self.assertIsNotNone(response["evidence"], response)
        return response

    @staticmethod
    def edge(result: dict[str, Any]) -> dict[str, Any]:
        return next(cast(dict[str, Any], row) for row in result["applicability"]
                    if row["target"] == {"kind": "relation", "id": "e1"})

    def query(self, label: str, evaluation: object) -> dict[str, Any]:
        declarations = core.document(self.declarations)
        for raw in core.as_list(declarations["applicability"]):
            row = core.as_object(raw)
            if row["target"] == {"kind": "relation", "id": "e1"}:
                row["condition"] = core.document({"predicate": self.f.law, "evaluation": evaluation})
        source = self.f.write("inputs/relations-" + label + ".json", declarations)
        response = self.public("relations.query", {"model": self.f.model, "declarations": source,
                                                 "query": "dependencies", "seeds": ["urn:a-c:toy:object:a"]})
        return cast(dict[str, Any], response["result"]["value"])

    def roundtrip(self, label: str, value: str, *, wrong_activation: bool = False,
                  nested: bool = False) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
        packet = self.f.packet()
        core.as_object(packet["activation"])["id"] = "activation-" + label
        domain: object = {"original_domain": value, "arbitrary": [None, True, 4, {"a/b~": "unchanged"}]}
        if nested:
            domain = {"nested": {"id": "nested-not-performed", "predicate": self.f.law,
                                 "domain_outcome": False, "core_value": "falsified",
                                 "evidence": [self.f.data], "residuals": [], "invalidators": []},
                      "arbitrary": domain}
        original = core.document({
            "schema": "a_c.fd-support.closed-return/1", "id": "return-" + label,
            "frame": {"id": "frame", "revision": "1"}, "activation": core.activation_identity(packet),
            "subject": self.f.subject, "basis": self.f.basis,
            "actor": {"id": "worker", "family": "A", "authorship": "worker"}, "consumer": "executive",
            "evaluations": [{"id": "actual-evaluation", "predicate": self.f.law,
                             "domain_outcome": domain, "core_value": value,
                             "evidence": [self.f.data], "residuals": [], "invalidators": []}],
            "not_performed": ["nested-not-performed"] if nested else [],
            "work_result": None, "residuals": [], "invalidators": [],
        })
        if wrong_activation:
            core.as_object(original["activation"])["sha256"] = "0" * 64
        payload = self.f.write("inputs/stdout-" + label + ".json", original)
        stdin_path = self.f.workspace / "outputs" / (label + ".stdin")
        executor_id = "local-" + label
        executor = core.document(core.as_object(self.f.policy["executors"])["registered"])
        executor.update({
            "id": executor_id,
            "argv": [str(Path(sys.executable).resolve()), "-B", str(self.f.workspace / "inputs/local-return-producer.py"),
                     str(self.f.workspace / core.text(payload["path"])), str(stdin_path)],
            "dependencies": [self.script, payload],
            "environment": {"PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(self.root)},
            "settings": {"timeout_ms": 2000, "termination_grace_ms": 100},
        })
        core.as_object(self.f.policy["executors"])[executor_id] = executor
        core.as_list(core.as_object(core.as_object(self.f.policy["grants"])["work"])["executors"]).append(executor_id)
        self.write_policy()
        (self.root / (label + "-assertions.json")).write_bytes(canonical({
            "kind": "fixture assertions, not execution observations", "original": original,
            "expected_binding_gap": "activation" if wrong_activation else None,
            "expected_nested_pointer_eligible": False if nested else None,
        }))
        assembled = self.public("context.assemble", {
            "packet": packet, "models": [], "sources": [self.f.law], "late_acquisition": [],
            "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8",
                         "host_context": {"state": "unknown", "bytes": None, "evidence": None}},
        })
        self.assertEqual(assembled["result"]["value"]["activation_identity"], core.activation_identity(packet))
        context = assembled["result"]["artifact"]
        preflight = self.public("contract.preflight", {"context": context, "grant_id": "work",
                                                      "executor_id": executor_id, "result_key": label, "observations": []})
        self.assertEqual(preflight["result"]["value"]["decision"], "admitted")
        dispatched = self.public("dispatch.start", {"preflight": preflight["result"]["artifact"]})
        attempt = dispatched["result"]["artifact"]
        deadline = time.monotonic() + 6
        while True:
            observed = self.public("dispatch.observe", {"attempt": attempt, "after_event": 0})["result"]["value"]
            if observed["process_end"] is not None and observed["output"] is not None:
                break
            self.assertLess(time.monotonic(), deadline, observed)
            time.sleep(0.03)
        self.assertEqual(observed["process_end"]["returncode"], 0)
        self.assertTrue(stdin_path.read_bytes())
        raw_ref = observed["output"]["stdout"]
        raw = self.public("evidence.read", {"artifact": raw_ref})["result"]["value"]["envelope"]["payload"]
        self.assertEqual(base64.b64decode(raw["bytes_base64"], validate=True), canonical(original))
        self.assertIs(raw["complete"], True)
        self.assertEqual(raw["slot"], "final_stdout_object")
        captured = self.public("return.capture", {"attempt": attempt, "payload": raw_ref,
                                                  "return_contract": self.f.return_contract})
        capture = cast(dict[str, Any], captured["result"]["value"])
        self.assertIs(capture["producer"]["authenticated"], True)
        self.assertIs(capture["binding_checks"]["format_valid"], True)
        self.assertEqual(capture["original"], original)
        reference = cast(dict[str, Any], captured["result"]["artifact"])
        checked = self.public("return.check", {"return": reference, "context": context,
                                               "consumer": "executive", "observations": [], "predicates": []})
        return reference, capture, cast(dict[str, Any], checked["result"]["value"])

    def assert_unresolved_dependency(self, result: dict[str, Any]) -> dict[str, Any]:
        fact = self.edge(result)
        self.assertIsNone(fact["core_value"])
        self.assertIs(fact["excluded"], False); self.assertIs(fact["unresolved"], True)
        self.assertEqual(result["records"], ["urn:a-c:toy:object:a", "urn:a-c:toy:object:b"])
        self.assertIn("e1", result["traversed_relations"])
        self.assertIn("e1", result["boundary"]["unresolved_traversal_relations"])
        self.assertTrue(fact["gaps"])
        return fact

    def test_missing_judgment_preserves_unknown_required_dependency(self) -> None:
        fact = self.assert_unresolved_dependency(self.missing)
        self.assertEqual(fact["gaps"], ["Missing actual condition judgment"])

    def test_wrong_activation_return_cannot_exclude_required_dependency(self) -> None:
        reference, capture, checked = self.roundtrip("wrong-activation", "falsified", wrong_activation=True)
        self.assertFalse(checked["consumable"])
        binding_gaps = capture["binding_checks"]["gaps"]
        self.assertEqual([gap["binding"] for gap in binding_gaps if isinstance(gap, dict) and "binding" in gap], ["activation"])
        result = self.query("wrong-activation", {"record": reference, "pointer": "/payload/original/evaluations/0"})
        fact = self.assert_unresolved_dependency(result)
        self.assertTrue(any(isinstance(gap, dict) and gap.get("code") == "basis_missing"
                            and gap.get("gaps") == binding_gaps for gap in fact["gaps"]))

    def test_nested_not_performed_domain_data_cannot_exclude_required_dependency(self) -> None:
        reference, capture, checked = self.roundtrip("nested", "satisfied", nested=True)
        self.assertTrue(checked["consumable"])
        self.assertEqual(capture["original"]["not_performed"], ["nested-not-performed"])
        nested = self.query("nested-data", {"record": reference, "pointer": "/payload/original/evaluations/0/domain_outcome/nested"})
        fact = self.assert_unresolved_dependency(nested)
        self.assertTrue(any(isinstance(gap, dict) and gap.get("code") == "basis_missing" for gap in fact["gaps"]))
        direct = self.query("nested-direct", {"record": reference, "pointer": "/payload/original/evaluations/0"})
        self.assertEqual(self.edge(direct)["core_value"], "satisfied")
        self.assertFalse(self.edge(direct)["unresolved"])
        self.assertEqual(direct["records"], ["urn:a-c:toy:object:a", "urn:a-c:toy:object:b"])

    def test_direct_performed_satisfied_and_falsified_conditions_remain_usable(self) -> None:
        for value in ("satisfied", "falsified"):
            with self.subTest(value=value):
                reference, _, checked = self.roundtrip(value, value)
                self.assertTrue(checked["consumable"])
                result = self.query(value, {"record": reference, "pointer": "/payload/original/evaluations/0"})
                fact = self.edge(result)
                self.assertEqual(fact["core_value"], value)
                self.assertEqual(fact["excluded"], value == "falsified")
                self.assertFalse(fact["unresolved"]); self.assertEqual(fact["gaps"], [])
                expected = ["urn:a-c:toy:object:a"] if value == "falsified" else ["urn:a-c:toy:object:a", "urn:a-c:toy:object:b"]
                self.assertEqual(result["records"], expected)


class ActorCliTransportTests(unittest.TestCase):
    """Controlled process transports only; no provider or F_P actor is run."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="a-c-actor-transport-")
        self.addCleanup(self.temporary.cleanup)
        self.parent = Path(self.temporary.name).resolve()
        self.addCleanup(self.retain_fixture_evidence)
        self.helper = TENANT / "examples" / "fd-support" / "actor_cli.py"
        self.python = Path(sys.executable).resolve()
        self.environment = dict(os.environ)
        self.environment["PYTHONDONTWRITEBYTECODE"] = "1"
        self.counter = 0

    def retain_fixture_evidence(self) -> None:
        destination = os.environ.get("AC_ACTOR_TRANSPORT_TEST_EVIDENCE")
        if destination is not None:
            import shutil
            target = Path(destination) / self.id().rsplit(".", 1)[-1]
            shutil.copytree(self.parent, target)

    @staticmethod
    def payload() -> bytes:
        # A deliberately opaque specimen, not a valid semantic Worker return.
        # Return.capture/check remain responsible for their actual contracts.
        return b' \n{"schema":"a_c.fd-support.closed-return/1","opaque":"unchanged", "n":1}\t'

    @staticmethod
    def claude(answer: bytes, **extra: Any) -> bytes:
        return canonical({"type": "result", "subtype": "success", "is_error": False,
                          "result": answer.decode("utf-8"), **extra})

    def prepare(self, raw: bytes, *, backend: str = "claude", decoder: str = "claude-result-json/1",
                stderr: bytes = b"fixture stderr\n", delay: float = 0, exit_code: int = 0,
                max_input: int = 131072, max_output: int = 131072, timeout_ms: int = 3000) -> tuple[Path, dict[str, Any]]:
        self.counter += 1
        directory = self.parent / str(self.counter)
        directory.mkdir()
        fixture = directory / "fixture.py"
        fixture.write_text(
            "import json,os,sys,time\nfrom pathlib import Path\n"
            "data=sys.stdin.buffer.read()\nPath(sys.argv[1]).write_bytes(data)\n"
            "Path(sys.argv[2]).write_text(json.dumps({k:os.environ.get(k) for k in "
            "('HOME','home','CODEX_HOME','AC_TEST_SETTING')}))\n"
            f"sys.stdout.buffer.write({raw!r});sys.stdout.buffer.flush()\n"
            f"sys.stderr.buffer.write({stderr!r});sys.stderr.buffer.flush()\n"
            f"time.sleep({delay!r})\nraise SystemExit({exit_code})\n",
            encoding="utf-8",
        )
        document: dict[str, Any] = {
            "schema": "a_c.fd-support.actor-cli-plan/1", "id": f"fixture-only-{self.counter}",
            "backend": backend,
            "executable": {"path": str(self.python), "sha256": hashlib.sha256(self.python.read_bytes()).hexdigest()},
            "argv": [str(self.python), str(fixture), str(directory / "received.bin"), str(directory / "environment.json")],
            "dependencies": [{"path": str(fixture), "sha256": hashlib.sha256(fixture.read_bytes()).hexdigest()}],
            "cwd": str(directory), "environment": {"PYTHONDONTWRITEBYTECODE": "1", "AC_TEST_SETTING": "fixed-fixture"},
            "settings": {"scope": "fixture only", "selected_model": None, "selected_effort": None},
            "decoder": decoder, "evidence_directory": str(directory / "evidence"),
            "limits": {"max_input_bytes": max_input, "max_output_bytes": max_output,
                       "timeout_ms": timeout_ms, "termination_grace_ms": 200},
        }
        plan = directory / "plan.json"
        plan.write_bytes(canonical(document))
        return plan, document

    def invoke(self, plan: Path, *, payload: bytes = b"sealed Context\n", sha: str | None = None,
               extra: Sequence[str] = ()) -> subprocess.CompletedProcess[bytes]:
        return subprocess.run(
            [str(self.python), str(self.helper), "--plan", str(plan), "--plan-sha256",
             hashlib.sha256(plan.read_bytes()).hexdigest() if sha is None else sha, *extra],
            input=payload, capture_output=True, timeout=10, env=self.environment, check=False,
        )

    @staticmethod
    def evidence(document: dict[str, Any], name: str) -> dict[str, Any]:
        return cast(dict[str, Any], json.loads((Path(document["evidence_directory"]) / name).read_bytes()))

    def test_claude_json_forwards_exact_context_and_opaque_answer_with_raw_float_metadata(self) -> None:
        answer = self.payload()
        raw = self.claude(answer, usage={"input_tokens": 17}, total_cost_usd=0.0123, modelUsage={"fixture": {"costUSD": 0.0123}})
        plan, document = self.prepare(raw)
        context = b"sealed\x00Context\r\n$(touch should-not-exist); `false` \xe2\x98\x83\n"
        result = self.invoke(plan, payload=context)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, answer)
        output = Path(document["evidence_directory"])
        self.assertEqual((plan.parent / "received.bin").read_bytes(), context)
        self.assertEqual((output / "context.bin").read_bytes(), context)
        self.assertEqual((output / "vendor.stdout").read_bytes(), raw)
        self.assertEqual((output / "final.payload").read_bytes(), answer)
        self.assertFalse((plan.parent / "should-not-exist").exists())
        invocation = self.evidence(document, "invocation.json")
        self.assertEqual(invocation["argv"], document["argv"])
        self.assertEqual(invocation["settings_declared"], document["settings"])
        self.assertEqual(invocation["input_sha256"], hashlib.sha256(context).hexdigest())
        decoded = self.evidence(document, "decoded.json")
        self.assertEqual(decoded["final_source"]["pointer"], "/result")
        self.assertIn("/total_cost_usd", decoded["vendor_observations"][0]["pointers"])
        self.assertIsNone(self.evidence(document, "result.json")["semantic_result"])

    def test_claude_jsonl_selects_terminal_result_and_preserves_partial_events(self) -> None:
        answer = self.payload()
        raw = canonical({"type": "assistant", "message": {"content": "partial only"}}) + b"\n" + self.claude(answer) + b"\n"
        plan, document = self.prepare(raw, decoder="claude-result-jsonl/1")
        result = self.invoke(plan)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, answer)
        self.assertEqual(self.evidence(document, "decoded.json")["final_source"]["line"], 2)
        self.assertEqual((Path(document["evidence_directory"]) / "vendor.stdout").read_bytes(), raw)

    def test_codex_jsonl_selects_last_completed_message_without_concatenation(self) -> None:
        answer = self.payload()
        events = [
            {"type": "thread.started", "thread_id": "fixture"},
            {"type": "item.completed", "item": {"type": "agent_message", "text": "Earlier commentary is not the final answer"}},
            {"type": "item.completed", "item": {"type": "agent_message", "text": answer.decode()}},
            {"type": "turn.completed", "usage": {"input_tokens": 100, "cached_input_tokens": 20, "output_tokens": 30}, "fixture_ratio": 0.25},
        ]
        raw = b"\n".join(canonical(event) for event in events) + b"\n"
        plan, document = self.prepare(raw, backend="codex", decoder="codex-final-jsonl/1")
        result = self.invoke(plan)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, answer)
        self.assertEqual(self.evidence(document, "decoded.json")["final_source"]["line"], 3)
        self.assertEqual((Path(document["evidence_directory"]) / "vendor.stdout").read_bytes(), raw)

    def test_public_payload_decimal_exponent_duplicate_nonfinite_and_fences_are_not_repaired(self) -> None:
        invalid = [
            b'{"schema":"a_c.fd-support.closed-return/1","n":1.0}',
            b'{"schema":"a_c.fd-support.closed-return/1","n":1e0}',
            b'{"schema":"a_c.fd-support.closed-return/1","n":NaN}',
            b'{"schema":"a_c.fd-support.closed-return/1","n":1,"n":2}',
            b'```json\n{"schema":"a_c.fd-support.closed-return/1"}\n```',
            b'{"schema":"other"}',
        ]
        for answer in invalid:
            with self.subTest(answer=answer):
                raw = self.claude(answer)
                plan, document = self.prepare(raw)
                result = self.invoke(plan)
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertEqual(result.stdout, b"")
                output = Path(document["evidence_directory"])
                self.assertEqual((output / "vendor.stdout").read_bytes(), raw)
                self.assertFalse((output / "final.payload").exists())
                self.assertFalse(self.evidence(document, "result.json")["output_available"])

    def test_missing_ambiguous_failed_or_nonterminal_claude_results_fail(self) -> None:
        valid = self.claude(self.payload())
        invalid = [
            b'{"type":"assistant"}',
            valid + b"\n" + valid,
            valid + b'\n{"type":"after-terminal"}',
            self.claude(self.payload(), is_error=True),
            self.claude(self.payload(), subtype="error_max_turns"),
            self.claude(b""),
            b'{"type":"result","subtype":"success","is_error":false,"structured_output":{"schema":"a_c.fd-support.closed-return/1"}}',
        ]
        for raw in invalid:
            with self.subTest(raw=raw):
                plan, document = self.prepare(raw, decoder="claude-result-jsonl/1")
                result = self.invoke(plan)
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertEqual(result.stdout, b"")
                self.assertFalse(self.evidence(document, "result.json")["output_available"])

    def test_codex_missing_message_failed_turn_or_multiple_turns_fail(self) -> None:
        message = canonical({"type": "item.completed", "item": {"type": "agent_message", "text": self.payload().decode()}})
        completed = canonical({"type": "turn.completed"})
        invalid = [completed, message, message + b'\n{"type":"turn.failed","error":{"message":"fixture failure"}}',
                   message + b"\n" + completed + b"\n" + completed,
                   message + b"\n" + completed + b'\n{"type":"item.completed"}']
        for raw in invalid:
            with self.subTest(raw=raw):
                plan, document = self.prepare(raw, backend="codex", decoder="codex-final-jsonl/1")
                result = self.invoke(plan)
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertEqual(result.stdout, b"")
                self.assertFalse(self.evidence(document, "result.json")["output_available"])

    def test_malformed_duplicate_nonfinite_vendor_data_and_invalid_utf8_fail(self) -> None:
        invalid = [b"{", b'{"type":"result","type":"result"}',
                   b'{"type":"result","cost":Infinity}', b'\xff']
        for raw in invalid:
            with self.subTest(raw=raw):
                plan, document = self.prepare(raw)
                result = self.invoke(plan)
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertEqual(result.stdout, b"")
                self.assertEqual((Path(document["evidence_directory"]) / "vendor.stdout").read_bytes(), raw)

    def test_valid_payload_with_nonzero_process_exit_is_not_a_success(self) -> None:
        raw = self.claude(self.payload())
        plan, document = self.prepare(raw, exit_code=9)
        result = self.invoke(plan)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertEqual(result.stdout, b"")
        self.assertEqual(self.evidence(document, "process.json")["returncode"], 9)
        self.assertEqual((Path(document["evidence_directory"]) / "vendor.stdout").read_bytes(), raw)

    def test_timeout_preserves_raw_partials_and_keeps_unobserved_effect_scope_unknown(self) -> None:
        plan, document = self.prepare(b'{"type":"partial"}\n', stderr=b"partial error\n", delay=5, timeout_ms=150)
        result = self.invoke(plan)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertEqual(result.stdout, b"")
        output = Path(document["evidence_directory"])
        self.assertEqual((output / "vendor.stdout").read_bytes(), b'{"type":"partial"}\n')
        self.assertEqual((output / "vendor.stderr").read_bytes(), b"partial error\n")
        observed = self.evidence(document, "process.json")
        self.assertIn("timeout", observed["failure"])
        self.assertIsNotNone(observed["returncode"])
        self.assertEqual(observed["termination_requests"][0]["scope"], "registered parent process only")
        self.assertTrue(any("descendant" in unknown for unknown in observed["unknowns"]))

    def test_output_bound_does_not_turn_a_retained_prefix_into_success(self) -> None:
        plan, document = self.prepare(self.claude(self.payload()), max_output=16)
        result = self.invoke(plan)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertEqual(result.stdout, b"")
        self.assertIn("output byte bound", self.evidence(document, "process.json")["failure"])
        self.assertGreater((Path(document["evidence_directory"]) / "vendor.stdout").stat().st_size, 16)

    def test_input_bound_launches_no_actor_and_retains_the_actual_bounded_prefix(self) -> None:
        plan, document = self.prepare(self.claude(self.payload()), max_input=4)
        result = self.invoke(plan, payload=b"more than four bytes")
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(result.stdout, b"")
        self.assertFalse((plan.parent / "received.bin").exists())
        self.assertEqual((Path(document["evidence_directory"]) / "context.bin").read_bytes(), b"more ")
        self.assertFalse(self.evidence(document, "result.json")["actor_launched"])

    def test_plan_digest_and_dependency_tamper_refuse_before_actor_launch(self) -> None:
        plan, document = self.prepare(self.claude(self.payload()))
        result = self.invoke(plan, sha="0" * 64)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertFalse(Path(document["evidence_directory"]).exists())
        Path(document["dependencies"][0]["path"]).write_text("raise SystemExit(0)\n")
        result = self.invoke(plan)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertFalse((plan.parent / "received.bin").exists())
        self.assertFalse(Path(document["evidence_directory"]).exists())

    def test_symlink_plan_and_dependency_are_refused(self) -> None:
        plan, document = self.prepare(self.claude(self.payload()))
        link = plan.parent / "linked-plan.json"
        link.symlink_to(plan.name)
        result = self.invoke(link)
        self.assertEqual(result.returncode, 2, result.stderr)
        fixture = Path(document["dependencies"][0]["path"])
        fixture_link = plan.parent / "linked-fixture.py"
        fixture_link.symlink_to(fixture.name)
        document["dependencies"][0]["path"] = str(fixture_link)
        plan.write_bytes(canonical(document))
        result = self.invoke(plan)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertFalse((plan.parent / "received.bin").exists())

    def test_backend_decoder_unknown_fields_and_extra_cli_arguments_are_refused(self) -> None:
        for change in ({"decoder": "codex-final-jsonl/1"}, {"backend": "unregistered"}, {"extra": "caller argument"}):
            with self.subTest(change=change):
                plan, document = self.prepare(self.claude(self.payload()))
                document.update(change)
                plan.write_bytes(canonical(document))
                result = self.invoke(plan)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertFalse((plan.parent / "received.bin").exists())
        plan, document = self.prepare(self.claude(self.payload()))
        result = self.invoke(plan, extra=("--model", "caller-selected"))
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertFalse(Path(document["evidence_directory"]).exists())

    def test_protected_home_paths_are_only_unchanged_actual_pass_through(self) -> None:
        plan, document = self.prepare(self.claude(self.payload()))
        result = self.invoke(plan)
        self.assertEqual(result.returncode, 0, result.stderr)
        actual = json.loads((plan.parent / "environment.json").read_bytes())
        inherited = {name: os.environ[name] for name in ("HOME", "home", "CODEX_HOME") if name in os.environ}
        for name in ("HOME", "home", "CODEX_HOME"):
            self.assertEqual(actual[name], inherited.get(name))
        self.assertEqual(actual["AC_TEST_SETTING"], "fixed-fixture")
        self.assertEqual(self.evidence(document, "invocation.json")["protected_environment_pass_through"], inherited)
        for name in ("HOME", "home", "CODEX_HOME"):
            with self.subTest(name=name):
                bad_plan, bad_document = self.prepare(self.claude(self.payload()))
                bad_document["environment"][name] = "/operator-requested-replacement"
                bad_plan.write_bytes(canonical(bad_document))
                refused = self.invoke(bad_plan)
                self.assertEqual(refused.returncode, 2, refused.stderr)
                self.assertFalse(Path(bad_document["evidence_directory"]).exists())

    def test_evidence_is_fresh_and_missing_usage_is_not_invented(self) -> None:
        plan, document = self.prepare(self.claude(self.payload()))
        result = self.invoke(plan)
        self.assertEqual(result.returncode, 0, result.stderr)
        decoded = self.evidence(document, "decoded.json")
        self.assertEqual(decoded["vendor_observations"], [])
        original = (Path(document["evidence_directory"]) / "vendor.stdout").read_bytes()
        again = self.invoke(plan)
        self.assertEqual(again.returncode, 2, again.stderr)
        self.assertEqual(again.stdout, b"")
        self.assertEqual((Path(document["evidence_directory"]) / "vendor.stdout").read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
