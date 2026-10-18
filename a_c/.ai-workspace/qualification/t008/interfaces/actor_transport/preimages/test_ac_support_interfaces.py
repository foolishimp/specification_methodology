"""Source-derived controls for actual public CLI and legacy MCP subprocesses.

The operator example supplies deterministic boundary fixtures only. These tests
make no F_P usability, independent semantic review or benefit claim.
"""
from __future__ import annotations

from collections.abc import Iterator, Sequence
from decimal import Decimal
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any, cast
import unittest


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
        self.parent = Path(self.temporary.name)
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

    def command(self, principal: str = "executive", *, sha: str | None = None) -> list[str]:
        return [sys.executable, str(ADAPTER), "--policy", str(self.policy),
                "--policy-sha256", self.sha if sha is None else sha, "--principal", principal]

    def invoke(self, request: dict[str, Any] | bytes, *, principal: str = "executive",
               sha: str | None = None) -> tuple[subprocess.CompletedProcess[bytes], dict[str, Any]]:
        raw = request if isinstance(request, bytes) else canonical(request)
        result = subprocess.run(self.command(principal, sha=sha) + ["call", "--request", "-"],
                                input=raw, capture_output=True, timeout=30, env=self.environment, check=False)
        response = cast(dict[str, Any], json.loads(result.stdout))
        self.assertEqual(set(response), RESPONSE_KEYS)
        self.assertEqual(len(result.stdout.splitlines()), 1)
        return result, response

    def session(self, messages: Sequence[dict[str, Any] | bytes], *, principal: str = "reviewer") -> tuple[subprocess.CompletedProcess[bytes], list[dict[str, Any]]]:
        raw = b"".join((message if isinstance(message, bytes) else canonical(message)) + b"\n" for message in messages)
        result = subprocess.run(self.command(principal) + ["mcp"], input=raw, capture_output=True,
                                timeout=30, env=self.environment, check=False)
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


if __name__ == "__main__":
    unittest.main()
