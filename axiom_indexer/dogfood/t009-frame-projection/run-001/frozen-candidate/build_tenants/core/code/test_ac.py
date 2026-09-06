from __future__ import annotations

import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from ac import Resolver, canonical_bytes, instantiate, join_sections, project_program, sha256, validate_program


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


def frame_program() -> dict:
    value = program()
    role = "urn:axiom-indexer:role:"
    clause = "urn:example:clause:"
    value["vocabulary_refs"] = sorted(VOCABULARY + [role + name for name in ("exception", "premise", "qualification", "support")])
    value["frame_refs"].append("repo://fixture/frame.md#other-frame")

    def row(name: str, statement: str, arguments: list[dict]) -> dict:
        return {
            "uri": clause + name, "clause_type": "constraint",
            "operator": "urn:axiom-indexer:operator:requires",
            "arguments": arguments, "statement": statement,
            "source_refs": ["repo://fixture/docs.md#product"],
        }

    subject = {"role": role + "condition", "ref": "urn:example:symbol:tool"}
    value["clauses"] = [
        row("common-rule", "Use current evidence and preserve unknowns.", [
            subject, {"role": role + "qualification", "literal": "Unknown evidence stays unknown."},
        ]),
        row("contents-pass", "The package contents check has passed.", [subject]),
        row("destination-ready", "The selected destination is ready to receive the package.", [subject]),
        row("quarantine", "An applicable quarantine prevents transfer.", [subject]),
        row("transfer", "Transfer is supported only with both premises and no applicable quarantine.", [
            {"role": role + "support", "ref": clause + "common-rule"},
            {"role": role + "premise", "ref": clause + "contents-pass"},
            {"role": role + "premise", "ref": clause + "destination-ready"},
            {"role": role + "exception", "ref": clause + "quarantine"},
            {"role": role + "qualification", "literal": "Both premises require current support; quarantine must be false."},
        ]),
        row("unrelated", "An unrelated inventory question remains outside these frames.", [
            {"role": role + "condition", "ref": "urn:example:symbol:source"},
        ]),
    ]
    value["residuals"] = [{
        "uri": "urn:example:residual:availability", "kind": "unresolved",
        "subject_refs": [clause + "destination-ready"],
        "detail": "A missing destination observation remains unknown.",
        "re_entry_refs": ["repo://fixture/details.md#unknown"],
        "source_refs": ["repo://fixture/docs.md#intent"],
    }]
    value["frame_indexes"] = [
        {"uri": "urn:example:index:quarantine", "frame_ref": value["frame_refs"][1],
         "scope": "Assess the selected package quarantine under current evidence.",
         "clause_refs": [clause + "common-rule", clause + "quarantine"],
         "residual_refs": [], "source_refs": [value["frame_refs"][1]]},
        {"uri": "urn:example:index:transfer", "frame_ref": value["frame_refs"][0],
         "scope": "Assess this package transfer; the index grants no action.",
         "clause_refs": [clause + "transfer"], "residual_refs": [],
         "source_refs": [value["frame_refs"][0]]},
    ]
    return value


class FrameProjectionTests(unittest.TestCase):
    def setUp(self) -> None:
        ACProgramTests.setUp(self)
        (self.root / "docs.md").write_text(
            "# Intent\n\nEvaluate one package transfer with explicit evidence; missing destination evidence is unknown.\n\n"
            "# Product\n\nUse current evidence and preserve unknowns. Transfer requires a passed contents check and a ready destination, "
            "and is prevented by applicable quarantine. Both premises require current support; quarantine must be false. "
            "The quarantine frame assesses only quarantine using the shared current-evidence rule. "
            "An unrelated inventory question is outside both frames. Evaluation grants no operation authority.\n",
            encoding="utf-8",
        )
        (self.root / "frame.md").write_text(
            "# Core Frame\n\nAssess transfer using both premises, the quarantine exception and unresolved evidence.\n\n"
            "# Other Frame\n\nAssess quarantine under the same current-evidence rule.\n",
            encoding="utf-8",
        )
        (self.root / "details.md").write_text("# Unknown\n\nMissing destination evidence requires source re-entry.\n", encoding="utf-8")
        self.value = frame_program()
        self.indexes = ["urn:example:index:quarantine", "urn:example:index:transfer"]
        self.resolver = Resolver(self.binding_path, self.binding_value)
        self.validation = validate_program(self.value, self.resolver)
        self.assertEqual(self.validation["status"], "valid", self.validation)
        self.logical_map = instantiate(self.value, self.validation)
        self.program_path = self.root / "program.json"
        self.map_path = self.root / "map.json"
        self.program_path.write_bytes(canonical_bytes(self.value))
        self.map_path.write_bytes(canonical_bytes(self.logical_map))

    def tearDown(self) -> None:
        self.temp.cleanup()

    def project(self, *, value=None, logical_map=None, indexes=None, mode="reference-only", resolver=None):
        return project_program(
            self.value if value is None else value,
            self.logical_map if logical_map is None else logical_map,
            self.resolver if resolver is None else resolver,
            self.indexes if indexes is None else indexes,
            mode,
        )

    def cli(self, *, output=None, indexes=None, mode="reference-only"):
        args = [sys.executable, str(Path(__file__).with_name("ac.py")), "project",
                "--program", str(self.program_path), "--map", str(self.map_path),
                "--bindings", str(self.binding_path), "--mode", mode]
        for ref in self.indexes if indexes is None else indexes:
            args.extend(["--frame-index", ref])
        if output is not None:
            args.extend(["--output", str(output)])
        return subprocess.run(args, capture_output=True, check=False)

    def test_both_views_preserve_exact_closure_roles_literals_and_content(self) -> None:
        original = canonical_bytes(self.value)
        reference_report, reference = self.project()
        material_report, material = self.project(mode="materialized", indexes=list(reversed(self.indexes)))
        self.assertEqual(reference_report["status"], material_report["status"])
        self.assertEqual(reference_report["status"], "valid")
        expected_clauses = ["urn:example:clause:" + name for name in
                            ("common-rule", "contents-pass", "destination-ready", "quarantine", "transfer")]
        self.assertEqual(reference["closure"], {
            "symbols": ["urn:example:symbol:tool"], "clauses": expected_clauses,
            "residuals": ["urn:example:residual:availability"],
        })
        for key in reference:
            if key not in {"mode", "projection_sha256"}:
                self.assertEqual(reference[key], material[key], key)
        self.assertNotIn("clauses", reference)
        for family in ("symbols", "clauses", "residuals"):
            self.assertEqual(material[family], [row for row in self.value[family] if row["uri"] in reference["closure"][family]])
        self.assertEqual(len([row for row in material["clauses"] if row["uri"].endswith(":common-rule")]), 1)
        transfer = next(row for row in reference["clause_relations"] if row["uri"].endswith(":transfer"))
        self.assertEqual(transfer["arguments"], self.value["clauses"][4]["arguments"])
        self.assertEqual(self.project()[1], reference)
        material["clauses"][0]["statement"] = "A view cannot edit its source object."
        self.assertEqual(canonical_bytes(self.value), original)

    def test_frame_scope_and_affected_residuals_do_not_infer_inverse_clauses(self) -> None:
        _, view = self.project(indexes=[self.indexes[0]])
        self.assertEqual(view["closure"]["clauses"], ["urn:example:clause:common-rule", "urn:example:clause:quarantine"])
        self.assertEqual(view["closure"]["residuals"], [])
        self.assertEqual(view["frame_indexes"], [self.value["frame_indexes"][0]])
        self.assertNotIn("urn:example:clause:transfer", view["closure"]["clauses"])
        changed = copy.deepcopy(self.value)
        changed["frame_indexes"][0]["clause_refs"] = []
        changed["frame_indexes"][0]["residual_refs"] = [changed["residuals"][0]["uri"]]
        report = validate_program(changed, self.resolver)
        _, view = self.project(value=changed, logical_map=instantiate(changed, report), indexes=[self.indexes[0]])
        self.assertEqual(view["closure"]["clauses"], ["urn:example:clause:destination-ready"])
        self.assertEqual(view["closure"]["residuals"], ["urn:example:residual:availability"])

    def test_cycles_terminate_as_reference_closure(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["clauses"][1]["arguments"].append({"role": "urn:axiom-indexer:role:support", "ref": "urn:example:clause:transfer"})
        valid = validate_program(changed, self.resolver)
        evaluation, view = self.project(value=changed, logical_map=instantiate(changed, valid))
        self.assertEqual(evaluation["status"], "valid")
        self.assertEqual(len(view["closure"]["clauses"]), 5)
        self.assertEqual(view["closure"]["clauses"], self.project()[1]["closure"]["clauses"])

    def test_index_schema_kind_identity_and_grounding_refusals(self) -> None:
        variants = [
            ("scope", " ", "empty_scope"), ("frame_ref", "urn:missing:frame", "undeclared_frame"),
            ("clause_refs", ["urn:example:symbol:tool"], "wrong_ref_kind"),
            ("residual_refs", ["urn:example:clause:transfer"], "wrong_ref_kind"),
            ("clause_refs", ["urn:missing:clause"], "dangling_ref"),
            ("source_refs", [], "empty_set"), ("extra", True, "unknown_field"),
            ("uri", "urn:example:clause:transfer", "duplicate_identity"),
            ("uri", ["not-an-identity"], "invalid_uri"),
        ]
        for field, value, expected in variants:
            with self.subTest(field=field, value=value):
                changed = copy.deepcopy(self.value)
                changed["frame_indexes"][0][field] = value
                report = validate_program(changed, self.resolver)
                self.assertIn(expected, {d["code"] for d in report["diagnostics"]})
        changed = copy.deepcopy(self.value)
        changed["frame_indexes"].append(copy.deepcopy(changed["frame_indexes"][0]))
        self.assertIn("duplicate_identity", {d["code"] for d in validate_program(changed, self.resolver)["diagnostics"]})
        changed = copy.deepcopy(self.value)
        changed["frame_indexes"][0]["clause_refs"] = []
        self.assertIn("empty_selection", {d["code"] for d in validate_program(changed, self.resolver)["diagnostics"]})

    def test_selection_refuses_absent_duplicate_unknown_wrong_kind_and_mode(self) -> None:
        for indexes, mode, expected in [
            ([], "reference-only", "empty_selection"),
            ([self.indexes[0], self.indexes[0]], "reference-only", "duplicate_selection"),
            (["urn:missing:index"], "reference-only", "unknown_frame_index"),
            (["urn:example:clause:transfer"], "reference-only", "wrong_selection_kind"),
            ([self.value["frame_refs"][0]], "reference-only", "wrong_selection_kind"),
            (["not a uri"], "reference-only", "invalid_uri"),
            (self.indexes, "guess", "invalid_projection_mode"),
        ]:
            with self.subTest(indexes=indexes, mode=mode):
                report, view = self.project(indexes=indexes, mode=mode)
                self.assertIsNone(view)
                self.assertIn(expected, {d["code"] for d in report["diagnostics"]})

    def test_missing_dependency_never_materializes(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["clauses"][4]["arguments"][2]["ref"] = "urn:missing:premise"
        report, view = self.project(value=changed, mode="materialized")
        self.assertIsNone(view)
        self.assertIn("dangling_ref", {d["code"] for d in report["diagnostics"]})

    def test_forged_maps_and_omitted_source_observations_refuse(self) -> None:
        variants = []
        for key in ("program_sha256", "map_sha256", "frame_indexes", "resolved_sources"):
            changed = copy.deepcopy(self.logical_map)
            del changed[key]
            variants.append(changed)
        changed = copy.deepcopy(self.logical_map)
        changed["clauses"][4]["arguments"].pop(3)
        del changed["map_sha256"]
        changed["map_sha256"] = sha256(canonical_bytes(changed))
        variants.append(changed)
        changed = copy.deepcopy(self.logical_map)
        changed["schema_version"] = True
        variants.append(changed)
        for changed in variants:
            report, view = self.project(logical_map=changed)
            self.assertIsNone(view)
            self.assertIn("map_mismatch", {d["code"] for d in report["diagnostics"]})

    def test_current_source_reentry_and_map_freshness_are_required(self) -> None:
        details = self.root / "details.md"
        original = details.read_bytes()
        details.write_bytes(original + b"Changed evidence.\n")
        report, view = self.project()
        self.assertIsNone(view)
        self.assertIn("source_observation_mismatch", {d["code"] for d in report["diagnostics"]})
        details.unlink()
        report, view = self.project()
        self.assertIsNone(view)
        self.assertIn("missing_resource", {d["code"] for d in report["diagnostics"]})
        details.write_bytes(original)
        self.assertEqual(self.project()[0]["status"], "valid")

    def test_physical_relocation_keeps_projection_identity(self) -> None:
        moved = self.root / "moved"
        moved.mkdir()
        for name in ("docs.md", "frame.md", "calculus.md", "details.md"):
            (moved / name).write_bytes((self.root / name).read_bytes())
        bindings = {**self.binding_value, "bindings": [{"uri_prefix": "repo://fixture/", "path": str(moved)}]}
        resolver = Resolver(self.binding_path, bindings)
        self.assertEqual(self.project(resolver=resolver)[1], self.project()[1])

    def test_cli_positive_views_and_refusal_remove_safe_stale_output(self) -> None:
        output = self.root / "projection.json"
        for mode in ("reference-only", "materialized"):
            result = self.cli(output=output, mode=mode)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(json.loads(output.read_bytes()), self.project(mode=mode)[1])
        self.assertEqual(json.loads(self.cli().stdout), self.project()[1])
        result = self.cli(output=output, indexes=[])
        self.assertEqual(result.returncode, 1)
        self.assertFalse(output.exists())
        for broken in (b"{}", b"not-json"):
            output.write_text("stale", encoding="utf-8")
            self.map_path.write_bytes(broken)
            result = self.cli(output=output)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(output.exists())

    def test_cli_preserves_direct_symlink_and_hardlink_inputs_and_sources(self) -> None:
        protected = [self.program_path, self.map_path, self.binding_path,
                     self.root / "docs.md", self.root / "details.md", self.root / "frame.md"]
        for number, source in enumerate(protected):
            original = source.read_bytes()
            symbolic = self.root / f"alias-{number}.json"
            hard = self.root / f"hard-{number}.json"
            symbolic.symlink_to(source)
            os.link(source, hard)
            for output in (source, symbolic, hard):
                with self.subTest(source=source.name, output=output.name):
                    result = self.cli(output=output)
                    self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
                    self.assertIn("input_output_path_alias", {d["code"] for d in json.loads(result.stdout)["diagnostics"]})
                    self.assertEqual(source.read_bytes(), original)
                    self.assertTrue(output.exists())
            self.assertTrue(symbolic.is_symlink())

    def test_invalid_fragment_refusal_cannot_remove_source_alias(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["residuals"][0]["re_entry_refs"] = ["repo://fixture/details.md#missing"]
        self.program_path.write_bytes(canonical_bytes(changed))
        source = self.root / "details.md"
        original = source.read_bytes()
        alias = self.root / "invalid-source-alias.json"
        os.link(source, alias)
        result = self.cli(output=alias)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(source.read_bytes(), original)
        self.assertTrue(alias.exists())
        codes = {d["code"] for d in json.loads(result.stdout)["diagnostics"]}
        self.assertIn("unresolved_fragment", codes)
        self.assertIn("input_output_path_alias", codes)

    def test_ambiguous_binding_refuses_without_touching_uncertain_output(self) -> None:
        changed = copy.deepcopy(self.binding_value)
        changed["bindings"].append(changed["bindings"][0])
        self.binding_path.write_bytes(canonical_bytes(changed))
        output = self.root / "projection.json"
        output.write_bytes(b"retained but explicitly unsafe")
        result = self.cli(output=output)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(output.read_bytes(), b"retained but explicitly unsafe")
        self.assertIn("output_safety_unresolved", {d["code"] for d in json.loads(result.stdout)["diagnostics"]})

    def test_programs_without_indexes_keep_their_existing_map_shape(self) -> None:
        plain = program()
        valid = validate_program(plain, self.resolver)
        logical_map = instantiate(plain, valid)
        self.assertEqual(valid["status"], "valid")
        self.assertNotIn("frame_indexes", logical_map)
        report, view = self.project(value=plain, logical_map=logical_map)
        self.assertIsNone(view)
        self.assertIn("unknown_frame_index", {d["code"] for d in report["diagnostics"]})


if __name__ == "__main__":
    unittest.main()
