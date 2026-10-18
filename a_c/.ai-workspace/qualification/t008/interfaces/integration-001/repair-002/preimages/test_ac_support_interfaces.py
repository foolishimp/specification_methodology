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
        # Preparation resolves the operator's new parent; an admitted runtime
        # still refuses an alias instead of changing a trusted path silently.
        command[command.index("--policy") + 1] = str(output / "policy.json")
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
