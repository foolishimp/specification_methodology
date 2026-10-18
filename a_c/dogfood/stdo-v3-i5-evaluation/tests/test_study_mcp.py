"""Reader boundary/budget/protocol tests, plus opt-in actual pinned Graphify tests.

Run all checks with the existing qualification environment:
AC_STUDY_UPSTREAM=/absolute/pinned/checkout a_c/.venv/bin/python -m unittest
discover -s a_c/dogfood/stdo-v3-i5-evaluation/tests -v
"""
from __future__ import annotations

import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("study_mcp_test_target", ROOT / "tools/study_mcp.py")
mcp = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = mcp
SPEC.loader.exec_module(mcp)


def fixture(root: Path, source: bytes | None = None) -> dict:
    source = source or "# Title\r\n\r\nExact café λ.\r\n\r\n## Section\r\nObligation.\r\n".encode()
    program = {"kind": "axiom-indexer.axiomatic-program", "schema_version": 1, "uri": "urn:test:program",
               "source_basis": "repo://test/", "calculus_ref": "stdo://test/calculus",
               "vocabulary_refs": ["repo://test/FILE.md#title"], "frame_refs": [], "symbols": [],
               "clauses": [{"uri": "urn:test:clause", "statement": "Exact café λ.", "arguments": [],
                            "source_refs": ["repo://test/FILE.md#section"]}],
               "residuals": [], "frame_indexes": []}
    coverage = {"scope": "fixture only", "limits": ["No semantic acceptance."]}
    files = {"program.json": mcp.encoded(program), "coverage.json": mcp.encoded(coverage), "sources/package/FILE.md": source}
    for name, raw in files.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
    manifest = {"profile": "ac.eval.native-baseline/1", "tenant": "codex", "input": {"package_commit": "test"},
                "source_roots": [{"uri_prefix": "repo://test/", "path_prefix": "package/"}],
                "native_program": {"path": "program.json", "sha256": mcp.sha(files["program.json"]), "bytes": len(files["program.json"])},
                "coverage_path": "coverage.json", "coverage_sha256": mcp.sha(files["coverage.json"]),
                "files": [{"path": "package/FILE.md", "sha256": mcp.sha(source), "bytes": len(source)}]}
    (root / "manifest.json").write_bytes(mcp.encoded(manifest))
    return program


def body(result: dict) -> dict:
    return json.loads(result["content"][0]["text"]) if result["content"] else {}


class ReaderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ac-study-test-")
        self.root = Path(self.temp.name)
        self.baseline = self.root / "baseline"
        self.baseline.mkdir()
        self.program = fixture(self.baseline)
        self.created = []
        self.serial = 0

    def tearDown(self):
        for server in self.created:
            if not server.audit.handle.closed:
                server.audit.handle.close()
        self.temp.cleanup()

    def server(self, *extra: str):
        log = self.root / f"audit-{self.serial}.jsonl"
        self.serial += 1
        args = mcp.arguments(["--baseline", str(self.baseline), "--tenant", "codex", "--condition", "direct", "--log", str(log), *extra])
        server = mcp.Server(args)
        self.created.append(server)
        return server

    def test_native_content_pointer_and_source_routes_are_exact(self):
        server = self.server()
        result = body(server.call("read_record", {"id": "urn:test:clause"}))
        self.assertEqual(result["record"], self.program["clauses"][0])
        self.assertEqual(result["source_routes"][0]["path"], "package/FILE.md")
        self.assertEqual(result["observation"]["documentary_text_emitted"], [])
        result = body(server.call("read_record", {"id": "urn:test:clause", "pointer": "/source_refs/0"}))
        self.assertEqual(result["record"], "repo://test/FILE.md#section")
        self.assertEqual(body(server.call("read_record", {"id": "urn:test:clause", "pointer": "/absent"}))["code"], "unknown_pointer")

    def test_source_read_preserves_exact_utf8_crlf_and_anchor(self):
        server = self.server()
        result = body(server.call("read_source", {"path": "package/FILE.md", "start_line": 1, "end_line": 6}))
        self.assertEqual(result["content"].encode(), (self.baseline / "sources/package/FILE.md").read_bytes())
        result = body(server.call("read_source", {"path": "repo://test/FILE.md#section"}))
        self.assertEqual(result["content"], "## Section\r\nObligation.\r\n")
        self.assertEqual(result["observation"]["source_coordinate_pins"][0]["sha256"], mcp.sha((self.baseline / "sources/package/FILE.md").read_bytes()))
        self.assertEqual(result["observation"]["documentary_text_emitted"][0]["utf8_bytes"], len(result["content"].encode()))

    def test_source_path_escape_and_nonallowlisted_paths_refuse(self):
        server = self.server()
        for path in ("/etc/passwd", "../manifest.json", "sources/../../manifest.json", "repo://test/%2e%2e/manifest.json", "package/missing.md", "package\\FILE.md"):
            result = server.call("read_source", {"path": path})
            self.assertTrue(result["isError"], path)
            self.assertNotIn("content", body(result))

    def test_symlink_and_pin_drift_refuse_at_startup(self):
        path = self.baseline / "sources/package/FILE.md"
        original = path.read_bytes()
        path.write_bytes(original + b"changed")
        with self.assertRaisesRegex(mcp.Refusal, "frozen pin"):
            self.server()
        path.unlink()
        target = self.root / "outside.md"
        target.write_bytes(original)
        path.symlink_to(target)
        with self.assertRaises(mcp.Refusal):
            self.server()

    def test_literal_discovery_is_explicitly_paginated_and_line_exact(self):
        server = self.server()
        result = body(server.call("search", {"query": ".", "scope": "source", "limit": 1}))
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["matches_total"], 2)
        self.assertEqual(len(result["matches"]), 1)
        self.assertEqual(result["next_offset"], 1)
        second = body(server.call("search", {"query": ".", "scope": "source", "limit": 1, "offset": 1}))
        self.assertEqual(second["matches"][0]["line"], 6)
        self.assertIsNone(second["next_offset"])
        result = body(server.call("search", {"query": "café", "scope": "source"}))
        self.assertEqual(result["matches"][0]["line"], 3)
        self.assertEqual(result["matches"][0]["text"], "Exact café λ.\r\n")

    def test_oversized_read_refuses_then_explicit_narrow_read_succeeds(self):
        fixture(self.baseline, b"# Title\n" + b"Private-tail-sentinel\n" * 2000)
        server = self.server("--max-bytes", "8000")
        result = body(server.call("read_source", {"path": "package/FILE.md"}))
        self.assertEqual(result["code"], "narrow_read_required")
        self.assertNotIn("content", result)
        self.assertEqual(server.audit.pending_read_refusals, 1)
        result = body(server.call("read_source", {"path": "package/FILE.md", "start_line": 1, "end_line": 1}))
        self.assertEqual(result["content"], "# Title\n")

    def test_call_and_byte_caps_count_refusals_and_multibyte_bytes(self):
        server = self.server("--max-calls", "2", "--max-bytes", "4000")
        first = server.call("read_record", {"id": "urn:test:clause"})
        second = server.call("missing", {})
        third = server.call("info", {})
        self.assertEqual(body(third)["code"], "call_budget_exhausted")
        self.assertEqual(server.audit.calls_attempted, 3)
        self.assertEqual(server.audit.calls_admitted, 2)
        emitted = sum(len(row["text"].encode("utf-8")) for result in (first, second, third) for row in result["content"])
        self.assertEqual(server.audit.content_bytes, emitted)
        self.assertLessEqual(emitted, 4000)

    def test_exhausted_bytes_emit_no_over_budget_text(self):
        server = self.server("--max-bytes", "10")
        for _ in range(3):
            self.assertEqual(server.call("info", {})["content"], [])
        self.assertEqual(server.audit.content_bytes, 0)

    def test_common_tool_surface_has_no_graph_and_strict_arguments(self):
        server = self.server()
        names = {tool["name"] for tool in server.definitions}
        self.assertEqual(names, {"info", "list_sources", "search", "read_source", "list_records", "read_record"})
        self.assertTrue(server.call("graph_query", {"question": "test"})["isError"])
        self.assertTrue(server.call("info", {"unexpected": "test"})["isError"])
        self.assertTrue(server.call("list_sources", {"limit": True})["isError"])

    def test_ndjson_initialize_list_call_and_private_logging(self):
        server = self.server()
        requests = [{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05"}},
                    {"jsonrpc": "2.0", "method": "notifications/initialized"},
                    {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
                    {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "info", "arguments": {}}}]
        output = io.BytesIO()
        server.serve(io.BytesIO(b"".join(mcp.encoded(row) + b"\n" for row in requests)), output)
        results = [json.loads(line) for line in output.getvalue().splitlines()]
        self.assertEqual([row["id"] for row in results], [1, 2, 3])
        self.assertEqual(results[0]["result"]["serverInfo"]["name"], "ac_study")
        self.assertNotIn(str(self.root), output.getvalue().decode())
        log = [json.loads(line) for line in server.args.log.read_text().splitlines()]
        calls = [row for row in log if row["event"] == "tool_call"]
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0]["emitted_utf8_bytes"], len(calls[0]["emitted_text"].encode()))
        self.assertEqual(log[-1]["wire_bytes"], len(output.getvalue()))

    def test_content_length_and_malformed_json_framing(self):
        server = self.server()
        raw = mcp.encoded({"jsonrpc": "2.0", "id": 1, "method": "ping"})
        output = io.BytesIO()
        server.serve(io.BytesIO(b"Content-Length: " + str(len(raw)).encode() + b"\r\n\r\n" + raw), output)
        response, framing = mcp.read_message(io.BytesIO(output.getvalue()))
        self.assertEqual(framing, "headers")
        self.assertEqual(json.loads(response)["result"], {})
        server = self.server()
        output = io.BytesIO()
        server.serve(io.BytesIO(b"{broken}\n"), output)
        self.assertEqual(json.loads(output.getvalue())["error"]["code"], -32700)

    def test_subprocess_stdio_smoke(self):
        command = [sys.executable, str(ROOT / "tools/study_mcp.py"), "--baseline", str(self.baseline),
                   "--tenant", "codex", "--condition", "direct", "--log", str(self.root / "process.jsonl")]
        request = {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "read_record", "arguments": {"id": "urn:test:clause"}}}
        process = subprocess.run(command, input=mcp.encoded(request) + b"\n", capture_output=True, check=False)
        self.assertEqual(process.returncode, 0, process.stderr.decode())
        self.assertEqual(body(json.loads(process.stdout)["result"])["record"], self.program["clauses"][0])


class OutputSchemaTests(unittest.TestCase):
    def test_every_object_is_closed_and_all_fields_required(self):
        schema = json.loads((ROOT / "output.schema.json").read_bytes())
        def visit(value):
            if isinstance(value, dict):
                if value.get("type") == "object":
                    self.assertIs(value["additionalProperties"], False)
                    self.assertEqual(set(value["required"]), set(value["properties"]))
                for child in value.values():
                    visit(child)
            elif isinstance(value, list):
                for child in value:
                    visit(child)
        visit(schema)


@unittest.skipUnless(os.environ.get("AC_STUDY_UPSTREAM"), "set AC_STUDY_UPSTREAM for actual pinned Graphify trial")
class ActualGraphifyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="ac-study-actual-")
        cls.servers = {}
        for tenant in ("codex", "claude"):
            args = mcp.arguments(["--tenant", tenant, "--condition", "graphify", "--baseline", str(ROOT / "baselines" / tenant),
                                  "--log", str(Path(cls.temp.name) / (tenant + ".jsonl")), "--upstream", os.environ["AC_STUDY_UPSTREAM"]])
            server = mcp.Server(args)
            server.graph.load()
            cls.servers[tenant] = server

    @classmethod
    def tearDownClass(cls):
        for server in cls.servers.values():
            server.audit.handle.close()
        cls.temp.cleanup()

    def test_actual_pinned_query_and_warm_reuse(self):
        for tenant, server in self.servers.items():
            with self.subTest(tenant=tenant):
                startup = server.audit.graph_startup_seconds
                result = server.graph.query("authority kinds", 1, 600)
                self.assertEqual(result["graph_pins"]["upstream_commit"], mcp.UPSTREAM_COMMIT)
                self.assertIsInstance(result["result"], str)
                self.assertGreater(len(result["result"]), 0)
                self.assertEqual(server.audit.graph_startup_seconds, startup)
                self.assertTrue(server.graph.query_function.__module__.startswith("graphify.serve"))

    def test_discovery_contains_only_allowlisted_sources_and_no_metadata(self):
        for tenant, server in self.servers.items():
            with self.subTest(tenant=tenant):
                excluded = 0
                retained_source_paths = set()
                for _, data in server.graph.graph.nodes(data=True):
                    self.assertNotEqual(data.get("ac_role"), "metadata")
                    self.assertNotIn("community", data)
                    self.assertNotIn("community_name", data)
                    if data.get("ac_role") == "record":
                        record = data["ac_payload"]["record"]
                        value = record.get("value", {})
                        if value.get("native_family") == "source_members":
                            native = json.loads(value["native_json"])
                            self.assertIn(native["path"], server.baseline.sources)
                            self.assertEqual(native["text"].encode(), server.baseline.sources[native["path"]])
                            retained_source_paths.add(native["path"])
                for record in server.graph.model.records.values():
                    value = record.fields.get("value", {})
                    if value.get("native_family") == "source_members" and json.loads(value["native_json"])["path"] not in server.baseline.sources:
                        excluded += 1
                self.assertEqual(excluded, server.graph.discovery_scope["excluded_source_members"])
                self.assertTrue(retained_source_paths)
                self.assertGreater(excluded, 0)

    def test_all_complete_selector_manifests_and_exact_materialization(self):
        for tenant, server in self.servers.items():
            with self.subTest(tenant=tenant):
                selector = next(iter(server.graph.catalog))
                manifest = server.graph.select([selector])
                self.assertFalse(manifest["native_payload_acquired"])
                self.assertFalse(manifest["documentary_source_text_acquired"])
                self.assertEqual(manifest["included"], server.graph.catalog[selector]["required_records"])
                selected = server.graph.select([selector], True)
                actual = {row["uri"]: (family, row) for family, records in selected["native"].items() for row in records}
                self.assertEqual(set(actual), set(manifest["included"]))
                self.assertEqual(actual, {identity: server.baseline.records[identity] for identity in manifest["included"]})
                self.assertEqual(len(server.graph.catalog), len(server.baseline.program["frame_indexes"]))

    def test_codex_oversized_materialization_refuses_with_complete_manifest(self):
        server = self.servers["codex"]
        # Use actual authored closure and a reduced test byte envelope. A huge
        # closure may legitimately have a manifest that itself cannot fit.
        selector = next(iter(server.graph.catalog))
        manifest_bytes = len(mcp.encoded(server.graph.select([selector])))
        test_budget = min(mcp.MAX_BYTES, manifest_bytes + 5000)
        self.assertGreater(len(mcp.encoded(server.graph.select([selector], True))), test_budget)
        server.args.max_bytes = test_budget
        result = body(server.call("graph_select", {"selectors": [selector], "materialize": True}))
        self.assertEqual(result["status"], "refused")
        self.assertEqual(result["code"], "narrow_read_required")
        self.assertEqual([row["id"] for row in result["manifest"]], server.graph.catalog[selector]["required_records"])
        self.assertNotIn("native", result)
        self.assertLessEqual(server.audit.content_bytes, mcp.MAX_BYTES)


if __name__ == "__main__":
    unittest.main()
