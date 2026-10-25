from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from stdo_toolchain.composition import verify_composition
from stdo_toolchain.store import Store
from tests.test_toolchain import ReleaseFixture, definition_document


class CompositionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="stdo-composition-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.fixture = ReleaseFixture(self.root)
        self.store = Store(self.root / "store")
        self.installed = self.store.install(str(self.fixture.repository), "v1.0.0-rc.1")
        self.workspace = self.root / "workspace"
        self.workspace.mkdir()
        self.a = self.definition("a")
        self.b = self.definition("b")
        self.relate(self.a, self.b)

    def definition(self, name: str) -> Path:
        directory = self.workspace / name
        directory.mkdir(parents=True)
        path = directory / f"stdo_{directory.name}.json"
        doc = definition_document(self.fixture.repository, self.installed.uri, self.installed.manifest_sha256)
        doc["product"]["definition_id"] = f"urn:test:composition:{name}"
        self.write(path, doc)
        (directory / "contract.md").write_text("# Contract\n\nPublic contract.\n")
        return path

    @staticmethod
    def write(path: Path, doc: dict) -> None:
        path.write_text(json.dumps(doc, indent=2) + "\n")

    def relate(self, source: Path, target: Path) -> None:
        doc = json.loads(source.read_text())
        doc["composition"].append({
            "product_definition": os.path.relpath(target, source.parent),
            "target_definition_id": json.loads(target.read_text())["product"]["definition_id"],
            "relation": "contract.md#contract",
            "contracts": [os.path.relpath(target.parent / "contract.md", source.parent) + "#contract"],
        })
        self.write(source, doc)

    def cli(self, root: Path | None = None, *, resolver_root: Path | None = None) -> tuple[dict, int]:
        command = [sys.executable, "-B", "-m", "stdo_toolchain.cli", "--store", str(self.store.root), "fleet", "verify", "--root", str(root or self.workspace)]
        if resolver_root is not None:
            command += ["--resolver-root", str(resolver_root)]
        environment = dict(os.environ)
        environment["PYTHONPATH"] = str(Path(__file__).resolve().parents[1] / "src")
        result = subprocess.run(command, capture_output=True, text=True, env=environment, timeout=30)
        self.assertEqual(result.stderr, "", result.stderr)
        return json.loads(result.stdout), result.returncode

    def source(self, report: dict, path: Path | None = None) -> dict:
        return next(item for item in report["definitions"] if item["definition"] == str(path or self.a))

    def assert_failure(self, code: str, *, root: Path | None = None) -> dict:
        report, status = self.cli(root)
        self.assertEqual(status, 1, report)
        self.assertFalse(report["valid"])
        self.assertIn(code, json.dumps(report))
        return report

    def test_public_cli_control_and_four_original_defects(self) -> None:
        original = json.loads(self.a.read_text())
        report, status = self.cli()
        self.assertEqual(status, 0, report)
        self.assertTrue(report["valid"])
        for field, value, code in [
            ("target_definition_id", "urn:wrong:target", "target_identity_mismatch"),
            ("product_definition", "../absent/stdo_missing.json", "unresolved_reference"),
            ("relation", "contract.md#absent", "missing_fragment"),
            ("contracts", ["../b/missing.md"], "unresolved_reference"),
        ]:
            with self.subTest(field=field):
                changed = copy.deepcopy(original)
                changed["composition"][0][field] = value
                self.write(self.a, changed)
                failed = self.assert_failure(code)
                self.assertFalse(self.source(failed)["valid"])
                self.assertTrue(self.source(failed)["failures"])
        self.write(self.a, original)

    def test_shared_nested_target_and_cycle_preserve_each_edge(self) -> None:
        c = self.definition("nested/c")
        d = self.definition("nested/deeper/d")
        self.relate(self.a, d)
        self.relate(self.b, c)
        self.relate(self.b, d)
        self.relate(c, self.a)
        report, status = self.cli(self.a, resolver_root=self.workspace)
        self.assertEqual(status, 0, report)
        self.assertEqual(len(report["definitions"]), 4)
        self.assertEqual(sum(len(x["composition"]) for x in report["definitions"]), 5)
        self.assertEqual(sum(x["selected"] for x in report["definitions"]), 1)
        d_edges = [e for item in report["definitions"] for e in item["composition"] if e["target_definition"] == str(d)]
        self.assertEqual(len(d_edges), 2)
        self.assertNotEqual(d_edges[0]["source_definition"], d_edges[1]["source_definition"])

    def test_file_selection_needs_explicit_sibling_boundary(self) -> None:
        self.assert_failure("outside_boundary", root=self.a)
        unrelated = self.workspace / "unrelated"
        unrelated.mkdir()
        (unrelated / "stdo_invalid.json").write_text("not json")
        report, status = self.cli(self.a, resolver_root=self.workspace)
        self.assertEqual(status, 0, report)
        self.assertEqual(len(report["definitions"]), 2)

    def test_selection_outside_explicit_boundary_refuses_before_discovery(self) -> None:
        report, status = self.cli(self.workspace, resolver_root=self.a.parent)
        self.assertEqual(status, 2)
        self.assertIn("outside resolver boundary", report["error"])

    def test_symlinked_target_and_symlink_ancestor_refuse(self) -> None:
        original = json.loads(self.a.read_text())
        link = self.a.parent / "link.json"
        link.symlink_to(self.b)
        changed = copy.deepcopy(original)
        changed["composition"][0]["product_definition"] = "link.json"
        self.write(self.a, changed)
        self.assert_failure("symlink_reference")
        link.unlink()
        link = self.a.parent / "linked-directory"
        link.symlink_to(self.b.parent, target_is_directory=True)
        changed["composition"][0]["product_definition"] = "linked-directory/../b/stdo_b.json"
        self.write(self.a, changed)
        self.assert_failure("symlink_reference")

    def test_symlinked_selected_file_and_root_refuse(self) -> None:
        link = self.workspace / "selected.json"
        link.symlink_to(self.a)
        report, status = self.cli(link, resolver_root=self.workspace)
        self.assertEqual(status, 2)
        self.assertIn("symlink", report["error"])
        directory = self.root / "linked-workspace"
        directory.symlink_to(self.workspace, target_is_directory=True)
        report, status = self.cli(directory)
        self.assertEqual(status, 2)
        self.assertIn("symlink", report["error"])

    def test_local_file_uri_directory_and_markdown_anchors(self) -> None:
        contract = self.b.parent / "a space.md"
        contract.write_text('# First!\n\n# First!\n\n<a id="Exact_ID"></a>\n')
        doc = json.loads(self.a.read_text())
        doc["composition"][0]["contracts"] = [contract.as_uri() + "#first-1", "../b/a%20space.md#Exact_ID", "../b/"]
        self.write(self.a, doc)
        report, status = self.cli()
        self.assertEqual(status, 0, report)
        observations = self.source(report)["composition"][0]["references"]["contracts"]
        self.assertEqual(observations[-1]["kind"], "directory")
        self.assertNotIn("sha256", observations[-1])

    def test_fragment_inside_example_or_comment_is_not_a_document_anchor(self) -> None:
        (self.a.parent / "contract.md").write_text('# Contract\n\n```md\n# Forged\n<a id="forged-id"></a>\n```\n<!-- # Comment -->\n`<a id="inline"></a>`\n')
        doc = json.loads(self.a.read_text())
        for fragment in ["forged", "forged-id", "comment", "inline"]:
            with self.subTest(fragment=fragment):
                doc["composition"][0]["relation"] = "contract.md#" + fragment
                self.write(self.a, doc)
                self.assert_failure("missing_fragment")

    def test_markdown_literal_markup_cannot_satisfy_relation_fragment(self) -> None:
        doc = json.loads(self.a.read_text())
        cases = [
            ("escaped-tag", '\\<a id="absent"></a>\n', "absent"),
            ("odd-escape-run", '\\\\\\<a id="absent"></a>\n', "absent"),
            ("multiline-code", '`literal\n<a id="absent"></a>\nliteral`\n', "absent"),
            ("indented-code-continuation", '`literal\n    still the same paragraph\n<a id="absent"></a>\nliteral`\n', "absent"),
            ("indented-code-block", 'Paragraph.\n\n    <a id="absent"></a>\n', "absent"),
            ("two-backticks", '``literal `\n<a id="absent"></a>\n` literal``\n', "absent"),
            ("longer-run-does-not-close", 'text ``literal ``` <a id="absent"></a> literal``\n', "absent"),
            ("escaped-backtick-run", '\\``literal\n<a id="absent"></a>\nliteral`\n', "absent"),
            ("encoded-tag", '&lt;a id="absent"&gt;&lt;/a&gt;\n', "absent"),
            ("escaped-heading", '\\# Absent\n', "absent"),
        ]
        for name, contents, fragment in cases:
            with self.subTest(case=name):
                (self.a.parent / "contract.md").write_text(contents)
                doc["composition"][0]["relation"] = "contract.md#" + fragment
                self.write(self.a, doc)
                report = self.assert_failure("missing_fragment")
                source = self.source(report)
                edge = source["composition"][0]
                self.assertFalse(source["valid"])
                self.assertFalse(edge["valid"])
                self.assertEqual(edge["references"]["relation"]["status"], "failed")
                self.assertEqual(edge["references"]["relation"]["code"], "missing_fragment")

    def test_real_markdown_anchors_survive_inline_literal_filter(self) -> None:
        (self.a.parent / "contract.md").write_text(
            '# Contract\n\n'
            'before <a id="actual"></a> after\n\n'
            'before <a\nid="multiline-tag"></a> after\n\n'
            '\\\\<a id="even-escape"></a>\n\n'
            '\\`literal <a id="escaped-opener"></a>\n\n'
            'text ``unmatched <a id="unmatched-run"></a> `\n\n'
            '`literal\\` <a id="after-closer"></a>\n\n'
            '`literal\n    literal` <a id="after-indented-closer"></a>\n\n'
            '`unclosed in this paragraph\n\n'
            '<a id="new-paragraph"></a> trailing `\n\n'
            'before <a title="`" id="tag-attribute"></a> trailing `\n\n'
            'before <a name="named-anchor"></a> after\n\n'
            '# Heading <a id="heading-anchor"></a>\n'
        )
        fragments = ["actual", "multiline-tag", "even-escape", "escaped-opener",
                     "unmatched-run", "after-closer", "after-indented-closer", "new-paragraph", "tag-attribute",
                     "named-anchor", "heading-anchor"]
        doc = json.loads(self.a.read_text())
        doc["composition"][0]["contracts"] = ["contract.md#" + value for value in fragments]
        self.write(self.a, doc)
        report, status = self.cli()
        self.assertEqual(status, 0, report)
        self.assertTrue(report["valid"])
        observations = self.source(report)["composition"][0]["references"]["contracts"]
        self.assertEqual([item["fragment"] for item in observations], fragments)
        self.assertTrue(all(item["status"] == "resolved" for item in observations))

    def test_json_pointer_and_html_fragment(self) -> None:
        (self.b.parent / "contract.json").write_text('{"a/b":{"~key":[42]}}')
        (self.b.parent / "contract.html").write_text('<section id="part"><a name="legacy"></a></section>')
        doc = json.loads(self.a.read_text())
        doc["composition"][0]["contracts"] = ["../b/contract.json#/a~1b/~0key/0", "../b/contract.html#legacy"]
        self.write(self.a, doc)
        report, status = self.cli()
        self.assertEqual(status, 0, report)
        for invalid in ["../b/contract.json#/a~1b/~0key/01", "../b/contract.json#/wrong", "../b/contract.html#absent"]:
            doc["composition"][0]["contracts"] = [invalid]
            self.write(self.a, doc)
            self.assert_failure("missing_fragment")

    def test_unsupported_fragment_and_remote_uri_are_distinct(self) -> None:
        (self.b.parent / "contract.txt").write_text("contract")
        doc = json.loads(self.a.read_text())
        for ref, code in [("../b/contract.txt#name", "unsupported_fragment"), ("https://example.invalid/contract#x", "unsupported_reference"), ("../b/contract.md?query=1", "unsupported_reference")]:
            with self.subTest(reference=ref):
                doc["composition"][0]["contracts"] = [ref]
                self.write(self.a, doc)
                report = self.assert_failure(code)
                self.assertEqual(self.source(report)["composition"][0]["references"]["contracts"][0]["status"], "unsupported")

    def test_exact_installed_contract_and_uninstalled_cut(self) -> None:
        doc = json.loads(self.a.read_text())
        doc["composition"][0]["contracts"] = ["stdo://releases/v1.0.0-rc.1/standards/SPEC_METHOD.md#spec-one"]
        self.write(self.a, doc)
        report, status = self.cli()
        self.assertEqual(status, 0, report)
        doc["composition"][0]["contracts"] = ["stdo://releases/v1.0.0-rc.99/standards/SPEC_METHOD.md"]
        self.write(self.a, doc)
        self.assert_failure("unresolved_installed_reference")
        self.assertFalse((self.store.releases_root / "v1.0.0-rc.99").exists())

    def test_target_own_schema_and_basis_are_required(self) -> None:
        doc = json.loads(self.b.read_text())
        doc["constitution"]["stdo"]["basis"]["manifest_sha256"] = "0" * 64
        self.write(self.b, doc)
        report = self.assert_failure("invalid_target_definition")
        self.assertFalse(self.source(report, self.a)["valid"])
        self.assertFalse(self.source(report, self.b)["valid"])

    def test_duplicate_identity_and_malformed_target_fail_closed(self) -> None:
        doc = json.loads(self.b.read_text())
        doc["product"]["definition_id"] = json.loads(self.a.read_text())["product"]["definition_id"]
        self.write(self.b, doc)
        self.assert_failure("Duplicate Product-Definition Identity")
        self.b.write_text("not JSON")
        self.assert_failure("invalid_target_definition")

    def test_special_file_is_refused_without_open(self) -> None:
        fifo = self.b.parent / "pipe"
        os.mkfifo(fifo)
        doc = json.loads(self.a.read_text())
        doc["composition"][0]["contracts"] = ["../b/pipe"]
        self.write(self.a, doc)
        self.assert_failure("unsupported_entry")

    def test_graph_and_byte_limits_refuse(self) -> None:
        for kwargs in [{"max_definitions": 1}, {"max_edges": 1}, {"max_file_bytes": 20}]:
            with self.subTest(limits=kwargs):
                if "max_edges" in kwargs:
                    self.relate(self.b, self.a)
                report = verify_composition([self.a], self.store, resolver_root=self.workspace, **kwargs)
                self.assertFalse(report["valid"], report)
                self.assertIn("resource_limit", json.dumps(report))

    def test_actual_bytes_change_without_any_source_commit_change(self) -> None:
        first, status = self.cli()
        self.assertEqual(status, 0, first)
        (self.b.parent / "contract.md").write_text("# Contract\n\nDifferent current source bytes.\n")
        second, status = self.cli()
        self.assertEqual(status, 0, second)
        a = self.source(first)["composition"][0]["references"]["contracts"][0]
        b = self.source(second)["composition"][0]["references"]["contracts"][0]
        self.assertNotEqual(a["sha256"], b["sha256"])
        self.assertEqual(self.source(first)["document_sha256"], self.source(second)["document_sha256"])

    def test_external_schema_ref_does_not_trigger_retrieval(self) -> None:
        schema = self.a.parent / "schema.json"
        schema.write_text('{"$ref":"https://example.invalid/schema.json"}')
        doc = json.loads(self.a.read_text())
        doc["$schema"] = "schema.json"
        self.write(self.a, doc)
        with patch("urllib.request.urlopen", side_effect=AssertionError("network forbidden")) as fetch:
            report = verify_composition([self.a], self.store, resolver_root=self.workspace)
            fetch.assert_not_called()
        self.assertFalse(report["valid"])
        self.assertIn("unsupported_schema_reference", json.dumps(report))

    def test_missing_local_schema_anchor_is_a_reported_failure(self) -> None:
        schema = self.a.parent / "schema.json"
        schema.write_text('{"$id":"https://example.invalid/schema", "$ref":"#absent"}')
        doc = json.loads(self.a.read_text())
        doc["$schema"] = "schema.json"
        self.write(self.a, doc)
        report, status = self.cli()
        self.assertEqual(status, 1, report)
        self.assertFalse(self.source(report)["valid"])
        self.assertIn("schema cannot be evaluated", json.dumps(report))


if __name__ == "__main__":
    unittest.main()
