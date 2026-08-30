from __future__ import annotations

import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from ac import Resolver, instantiate, join_sections, validate_program


VOCABULARY = [
    "urn:axiom-indexer:kind:product",
    "urn:axiom-indexer:operator:requires",
    "urn:axiom-indexer:role:condition",
    "urn:axiom-indexer:role:consequence",
]


def program() -> dict:
    return {
        "kind": "axiom-indexer.axiomatic-program",
        "schema_version": 1,
        "uri": "urn:example:program:mvp",
        "calculus_ref": "repo://fixture/calculus.md",
        "source_basis": "repo://fixture/",
        "frame_refs": ["repo://fixture/frame.md#core-frame"],
        "vocabulary_refs": VOCABULARY,
        "symbols": [
            {
                "uri": "urn:example:symbol:source",
                "kind": "urn:axiom-indexer:kind:product",
                "label": "Source",
                "source_refs": ["repo://fixture/docs.md#intent"],
            },
            {
                "uri": "urn:example:symbol:tool",
                "kind": "urn:axiom-indexer:kind:product",
                "label": "Tool",
                "source_refs": ["repo://fixture/docs.md#product"],
            },
        ],
        "clauses": [
            {
                "uri": "urn:example:clause:source-required",
                "clause_type": "constraint",
                "operator": "urn:axiom-indexer:operator:requires",
                "arguments": [
                    {
                        "role": "urn:axiom-indexer:role:condition",
                        "ref": "urn:example:symbol:tool",
                    },
                    {
                        "role": "urn:axiom-indexer:role:consequence",
                        "ref": "urn:example:symbol:source",
                    },
                ],
                "statement": "The tool requires its source.",
                "source_refs": ["repo://fixture/docs.md#product"],
            }
        ],
        "residuals": [
            {
                "uri": "urn:example:residual:scope",
                "kind": "ambiguity",
                "subject_refs": ["urn:example:symbol:tool"],
                "detail": "Later scope is unresolved.",
                "re_entry_refs": ["repo://fixture/docs.md#intent"],
                "source_refs": ["repo://fixture/docs.md#intent"],
            }
        ],
    }


class ACProgramTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "docs.md").write_text(
            "# Intent\n\nSource intent.\n\n# Product\n\nProduct law.\n",
            encoding="utf-8",
        )
        (self.root / "frame.md").write_text("# Core Frame\n", encoding="utf-8")
        (self.root / "calculus.md").write_text("# Calculus\n", encoding="utf-8")
        self.binding_path = self.root / "bindings.json"
        self.binding_value = {
            "kind": "axiom-indexer.binding-set",
            "schema_version": 1,
            "bindings": [{"uri_prefix": "repo://fixture/", "path": "."}],
        }
        self.binding_path.write_text(json.dumps(self.binding_value), encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def validate(
        self,
        value: dict,
        *,
        binding_path: Path | None = None,
        binding_value: dict | None = None,
    ) -> dict:
        path = binding_path or self.binding_path
        resolver = Resolver(path, binding_value or self.binding_value)
        return validate_program(value, resolver)

    def codes(self, value: dict) -> set[str]:
        return {row["code"] for row in self.validate(value)["diagnostics"]}

    def test_valid_program_instantiates_map(self) -> None:
        value = program()
        validation = self.validate(value)
        self.assertEqual(validation["status"], "valid")
        logical_map = instantiate(value, validation)
        self.assertEqual(
            logical_map["constraints"], ["urn:example:clause:source-required"]
        )
        self.assertEqual(
            logical_map["outgoing_clause_refs"]["urn:example:symbol:tool"],
            ["urn:example:clause:source-required"],
        )
        self.assertEqual(logical_map["calculus_ref"], value["calculus_ref"])
        self.assertEqual(len(logical_map["resolved_sources"]), 4)

    def test_malformed_absolute_uris_refuse(self) -> None:
        for uri in ("urn:axiom indexer:bad", "x:\\bad", "https://", "urn:bad:%zz"):
            with self.subTest(uri=uri):
                value = program()
                value["uri"] = uri
                self.assertIn("invalid_uri", self.codes(value))

    def test_directory_source_grounding_refuses(self) -> None:
        value = program()
        value["symbols"][0]["source_refs"] = ["repo://fixture/"]
        self.assertIn("resource_not_file", self.codes(value))

    def test_map_keeps_edges_to_every_local_family(self) -> None:
        value = program()
        residual_uri = value["residuals"][0]["uri"]
        value["clauses"][0]["arguments"][1]["ref"] = residual_uri
        validation = self.validate(value)
        self.assertEqual(validation["status"], "valid")
        logical_map = instantiate(value, validation)
        self.assertEqual(
            logical_map["outgoing_clause_refs"][residual_uri],
            ["urn:example:clause:source-required"],
        )

    def test_dangling_reference_refuses(self) -> None:
        value = program()
        value["clauses"][0]["arguments"][0]["ref"] = "urn:example:missing"
        self.assertIn("dangling_ref", self.codes(value))

    def test_duplicate_identity_refuses(self) -> None:
        value = program()
        duplicate = copy.deepcopy(value["symbols"][0])
        value["symbols"].append(duplicate)
        self.assertIn("duplicate_identity", self.codes(value))

    def test_unresolved_source_refuses(self) -> None:
        value = program()
        value["symbols"][0]["source_refs"] = ["repo://fixture/docs.md#missing"]
        self.assertIn("unresolved_fragment", self.codes(value))

    def test_malformed_clause_refuses(self) -> None:
        value = program()
        value["clauses"][0]["arguments"][0]["literal"] = "also present"
        self.assertIn("invalid_argument_value", self.codes(value))

    def test_ungrounded_item_refuses(self) -> None:
        value = program()
        value["symbols"][0]["source_refs"] = []
        self.assertIn("empty_set", self.codes(value))

    def test_physical_relocation_preserves_program_and_map(self) -> None:
        value = program()
        first = self.validate(value)
        first_map = instantiate(value, first)
        moved = self.root / "moved"
        moved.mkdir()
        (moved / "docs.md").write_bytes((self.root / "docs.md").read_bytes())
        (moved / "frame.md").write_bytes((self.root / "frame.md").read_bytes())
        (moved / "calculus.md").write_bytes((self.root / "calculus.md").read_bytes())
        moved_binding = self.root / "moved-bindings.json"
        moved_value = {
            "kind": "axiom-indexer.binding-set",
            "schema_version": 1,
            "bindings": [{"uri_prefix": "repo://fixture/", "path": "moved"}],
        }
        second = self.validate(
            value, binding_path=moved_binding, binding_value=moved_value
        )
        second_map = instantiate(value, second)
        self.assertEqual(second["status"], "valid")
        self.assertEqual(first["program_sha256"], second["program_sha256"])
        self.assertEqual(first_map["map_sha256"], second_map["map_sha256"])

    def test_cli_protects_inputs_and_clears_stale_map(self) -> None:
        program_path = self.root / "program.json"
        original = json.dumps(program()).encode()
        program_path.write_bytes(original)
        script = Path(__file__).with_name("ac.py")
        stale_alias_map = self.root / "alias-map.json"
        stale_alias_map.write_text("stale", encoding="utf-8")
        alias = subprocess.run(
            [
                sys.executable,
                str(script),
                "validate",
                "--program",
                str(program_path),
                "--bindings",
                str(self.binding_path),
                "--output",
                str(program_path),
                "--emit-map",
                str(stale_alias_map),
            ],
            check=False,
            capture_output=True,
        )
        self.assertEqual(alias.returncode, 2)
        self.assertEqual(program_path.read_bytes(), original)
        self.assertFalse(stale_alias_map.exists())

        hardlink = self.root / "program-hardlink.json"
        os.link(program_path, hardlink)
        hardlink_alias = subprocess.run(
            [
                sys.executable,
                str(script),
                "validate",
                "--program",
                str(program_path),
                "--bindings",
                str(self.binding_path),
                "--output",
                str(hardlink),
            ],
            check=False,
            capture_output=True,
        )
        self.assertEqual(hardlink_alias.returncode, 2)
        self.assertEqual(program_path.read_bytes(), original)

        shared_output = self.root / "shared-output.json"
        shared_output.write_text("stale", encoding="utf-8")
        shared_alias = subprocess.run(
            [
                sys.executable,
                str(script),
                "validate",
                "--program",
                str(program_path),
                "--bindings",
                str(self.binding_path),
                "--output",
                str(shared_output),
                "--emit-map",
                str(shared_output),
            ],
            check=False,
            capture_output=True,
        )
        self.assertEqual(shared_alias.returncode, 2)
        self.assertFalse(shared_output.exists())

        invalid = program()
        invalid["clauses"][0]["arguments"][0]["ref"] = "urn:example:missing"
        program_path.write_text(json.dumps(invalid), encoding="utf-8")
        map_path = self.root / "map.json"
        map_path.write_text("stale", encoding="utf-8")
        report_path = self.root / "report.json"
        result = subprocess.run(
            [
                sys.executable,
                str(script),
                "validate",
                "--program",
                str(program_path),
                "--bindings",
                str(self.binding_path),
                "--output",
                str(report_path),
                "--emit-map",
                str(map_path),
            ],
            check=False,
        )
        self.assertEqual(result.returncode, 1)
        self.assertFalse(map_path.exists())

    def test_join_sections_preserves_exact_order_and_text(self) -> None:
        sections = [
            {"label": "Z", "text": "First line\nSecond line"},
            {"label": "A", "text": "Unicode: λ"},
            {"label": "Z", "text": "Repeated label"},
            {"label": "", "text": ""},
        ]
        self.assertEqual(
            join_sections(sections),
            "Z\nFirst line\nSecond line\n\nA\nUnicode: λ\n\nZ\nRepeated label\n\n\n",
        )
        self.assertEqual(join_sections([]), "")

    def test_join_sections_refuses_only_malformed_shapes(self) -> None:
        invalid = [
            None,
            {},
            [None],
            [{}],
            [{"label": "A"}],
            [{"text": "B"}],
            [{"label": "A", "text": "B", "extra": "C"}],
            [{"label": 1, "text": "B"}],
            [{"label": "A", "text": 1}],
            [{"label": "\ud800", "text": "B"}],
        ]
        for value in invalid:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    join_sections(value)

    def test_join_cli_stdout_and_file_are_exact(self) -> None:
        script = Path(__file__).with_name("ac.py")
        sections_path = self.root / "sections.json"
        sections_path.write_text(
            json.dumps(
                [
                    {"label": "Reference frames", "text": "urn:frame:a"},
                    {"label": "Return", "text": "GO | HOLD"},
                ]
            ),
            encoding="utf-8",
        )
        expected = b"Reference frames\nurn:frame:a\n\nReturn\nGO | HOLD"
        stdout_result = subprocess.run(
            [sys.executable, str(script), "join", "--input", str(sections_path)],
            check=False,
            capture_output=True,
        )
        self.assertEqual(stdout_result.returncode, 0)
        self.assertEqual(stdout_result.stdout, expected)
        self.assertEqual(stdout_result.stderr, b"")

        output_path = self.root / "request.txt"
        file_result = subprocess.run(
            [
                sys.executable,
                str(script),
                "join",
                "--input",
                str(sections_path),
                "--output",
                str(output_path),
            ],
            check=False,
            capture_output=True,
        )
        self.assertEqual(file_result.returncode, 0)
        self.assertEqual(output_path.read_bytes(), expected)

    def test_join_cli_refuses_before_writing(self) -> None:
        script = Path(__file__).with_name("ac.py")
        invalid_path = self.root / "invalid-sections.json"
        invalid_path.write_text('{"label":"not-a-list"}', encoding="utf-8")
        output_path = self.root / "request.txt"
        output_path.write_text("preserve", encoding="utf-8")
        invalid_result = subprocess.run(
            [
                sys.executable,
                str(script),
                "join",
                "--input",
                str(invalid_path),
                "--output",
                str(output_path),
            ],
            check=False,
            capture_output=True,
        )
        self.assertEqual(invalid_result.returncode, 2)
        self.assertEqual(output_path.read_text(encoding="utf-8"), "preserve")

        invalid_utf8_path = self.root / "invalid-utf8.json"
        invalid_utf8_path.write_bytes(b"\xff")
        invalid_utf8_result = subprocess.run(
            [
                sys.executable,
                str(script),
                "join",
                "--input",
                str(invalid_utf8_path),
                "--output",
                str(output_path),
            ],
            check=False,
            capture_output=True,
        )
        self.assertEqual(invalid_utf8_result.returncode, 2)
        self.assertEqual(output_path.read_text(encoding="utf-8"), "preserve")

        alias_result = subprocess.run(
            [
                sys.executable,
                str(script),
                "join",
                "--input",
                str(invalid_path),
                "--output",
                str(invalid_path),
            ],
            check=False,
            capture_output=True,
        )
        self.assertEqual(alias_result.returncode, 2)
        self.assertEqual(
            invalid_path.read_text(encoding="utf-8"),
            '{"label":"not-a-list"}',
        )


if __name__ == "__main__":
    unittest.main()
