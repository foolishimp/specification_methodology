#!/usr/bin/env python3
"""Negative and optimization-mode tests for check_constitution.py."""

from __future__ import annotations

import ast
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import check_constitution as checker
import prepare_stdo_gtl_candidate as preparer


class ConstitutionCheckerTests(unittest.TestCase):
    def test_checker_contains_no_assert_statement(self) -> None:
        tree = ast.parse(Path(checker.__file__).read_text(encoding="utf-8"))
        self.assertEqual(
            [], [node for node in ast.walk(tree) if isinstance(node, ast.Assert)]
        )

    def test_duplicate_json_object_name_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"kind":"one","kind":"two"}\n', encoding="utf-8")
            with self.assertRaisesRegex(
                checker.CheckFailure, "duplicate JSON object name"
            ):
                checker.load_json_unique(path)

    def test_disambiguation_context_mutation_fails(self) -> None:
        definition = checker.load_json_unique(checker.ROOT / "stdo_representation.json")
        definition["local_constitution"]["disambiguations"][0][
            "context"
        ] = "urn:mutation:wrong-context"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stdo_representation.json"
            path.write_text(json.dumps(definition), encoding="utf-8")
            with self.assertRaisesRegex(
                checker.CheckFailure, "engagement-role disambiguation records"
            ):
                checker.check_definition(Path(directory))

    def test_singleton_functor_disambiguation_fails(self) -> None:
        definition = checker.load_json_unique(checker.ROOT / "stdo_representation.json")
        definition["local_constitution"]["disambiguations"].append(
            {
                "uri": "./specification/PRODUCT.md#fundamental-traversal-functor-binding",
                "term": "F_P",
                "context": "urn:stdo-representation:bounded-context:product",
                "disambiguates": ["urn:stdo:concept:axiomatic-calculus:f-p"],
                "resolves_to": "urn:stdo:concept:axiomatic-calculus:f-p",
                "authority": [],
                "basis": ["#/constitution/stdo/basis"],
                "applies_to": ["urn:stdo:product-definition:stdo-representation"],
            }
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stdo_representation.json"
            path.write_text(json.dumps(definition), encoding="utf-8")
            with self.assertRaisesRegex(
                checker.CheckFailure, "unexpected semantic disambiguation count"
            ):
                checker.check_definition(Path(directory))

    def test_role_import_target_mutation_fails(self) -> None:
        definition = checker.load_json_unique(checker.ROOT / "stdo_representation.json")
        executive = next(
            item
            for item in definition["local_constitution"]["disambiguations"]
            if item["term"] == "Executive"
        )
        executive["resolves_to"] = "urn:mutation:local-executive-persona"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stdo_representation.json"
            path.write_text(json.dumps(definition), encoding="utf-8")
            with self.assertRaisesRegex(
                checker.CheckFailure, "engagement-role disambiguation records"
            ):
                checker.check_definition(Path(directory))

    def test_missing_axiomatic_calculus_entrypoint_fails(self) -> None:
        definition = checker.load_json_unique(checker.ROOT / "stdo_representation.json")
        definition["constitution"]["entrypoints"] = [
            item
            for item in definition["constitution"]["entrypoints"]
            if item["uri"] != "standards/AXIOMATIC_CALCULUS.md"
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stdo_representation.json"
            path.write_text(json.dumps(definition), encoding="utf-8")
            with self.assertRaisesRegex(checker.CheckFailure, "Axiomatic Calculus"):
                checker.check_definition(Path(directory))

    def test_odd_method_entrypoint_fails(self) -> None:
        definition = checker.load_json_unique(checker.ROOT / "stdo_representation.json")
        definition["constitution"]["entrypoints"].append(
            {
                "basis": "#/constitution/stdo/basis",
                "uri": "standards/ODD_METHOD.md",
            }
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stdo_representation.json"
            path.write_text(json.dumps(definition), encoding="utf-8")
            with self.assertRaisesRegex(checker.CheckFailure, "ODD Method leaked"):
                checker.check_definition(Path(directory))

    def test_common_semantic_compile_surface_mutation_fails(self) -> None:
        definition = checker.load_json_unique(checker.ROOT / "stdo_representation.json")
        definition["how"]["common"] = []
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stdo_representation.json"
            path.write_text(json.dumps(definition), encoding="utf-8")
            with self.assertRaisesRegex(checker.CheckFailure, "semantic_compile"):
                checker.check_definition(Path(directory))

    def test_duplicate_ticket_header_key_fails(self) -> None:
        text = "# Ticket\n\nid: T-900\nid: T-901\n\n## Body\n"
        with self.assertRaisesRegex(checker.CheckFailure, "duplicate ticket metadata"):
            checker.parse_ticket_metadata(text, "mutation")

    def test_body_metadata_like_text_cannot_override_header(self) -> None:
        text = "# Ticket\n\nid: T-900\nstatus: active\n\nstatus: completed\n"
        values = checker.parse_ticket_metadata(text, "bounded-header")
        self.assertEqual("active", values["status"])

    def test_missing_ticket_field_fails(self) -> None:
        values = {
            "id": "T-900",
            "title": "Mutation",
            "type": "bug",
            "ticket_category": "ordinary",
            "status": "active",
            "goal": "GOAL-001",
            "change_intent": "exercise refusal",
            "change_class": "intent_reprice",
            "re_entry_point": "Intent",
            "triaged_at": "2026-08-27T00:00:00+10:00",
            "created_at": "2026-08-27T00:00:00+10:00",
        }
        with self.assertRaisesRegex(checker.CheckFailure, "missing ticket metadata"):
            checker.validate_ticket_metadata(
                values, Path(".ai-workspace/tickets/active/T-900.md")
            )

    def test_wrong_ticket_lane_status_fails(self) -> None:
        values = {
            "id": "T-900",
            "title": "Mutation",
            "type": "bug",
            "ticket_category": "ordinary",
            "status": "completed",
            "goal": "GOAL-001",
            "change_intent": "exercise refusal",
            "change_class": "intent_reprice",
            "re_entry_point": "Intent",
            "triaged_at": "2026-08-27T00:00:00+10:00",
            "created_at": "2026-08-27T00:00:00+10:00",
            "updated_at": "2026-08-27T00:00:00+10:00",
        }
        with self.assertRaisesRegex(checker.CheckFailure, "status/lane mismatch"):
            checker.validate_ticket_metadata(
                values, Path(".ai-workspace/tickets/active/T-900.md")
            )

    def test_carrier_coordinate_digest_is_reproducible(self) -> None:
        digest = checker.sha256_bytes(
            checker.canonical_ascii_coordinate_bytes(checker.GTL_CARRIER_COORDINATE)
        )
        self.assertEqual(
            "b5becdf2801577f00bbc119a6bb23e0015a2007147818557ee2e770bc682b703",
            digest,
        )

    def test_bare_functor_application_fails(self) -> None:
        with self.assertRaisesRegex(
            checker.CheckFailure, "bypasses functor application"
        ):
            checker.check_functor_application_notation(
                {Path("mutation.md"): "F_P(source, intent) -> candidate"}
            )

    def test_tenant_profile_in_semantic_compiler_fails(self) -> None:
        with self.assertRaisesRegex(
            checker.CheckFailure, "tenant profile leaked into carrier-neutral"
        ):
            checker.check_carrier_neutral_compiler(
                "F_P[v_compile](S_B, G_profile)", "carrier neutral"
            )

    def test_carrier_admission_cannot_return_promoted_carrier(self) -> None:
        path = checker.SPEC / "PRODUCT.md"
        text = path.read_text(encoding="utf-8")
        lawful = """D_{G,T} =
  F_D[v_carrier_admission](G_{B,T}, Profile_T, CarrierBasis_T)
    -> admitted | refuse"""
        legacy = """F_D[v_carrier_admission](G_{B,T}*, Profile_T, CarrierBasis_T)
  -> G_{B,T} | refuse"""
        mutated = text.replace(lawful, legacy, 1)
        self.assertNotEqual(text, mutated)
        with self.assertRaisesRegex(checker.CheckFailure, "D_\\{G,T\\}"):
            checker.check_carrier_admission_judgment(mutated, path)

    def test_selection_ledger_cannot_require_second_acceptance(self) -> None:
        path = checker.SPEC / "PRODUCT.md"
        product = path.read_text(encoding="utf-8").replace(
            '"interpreted_model" | "product",',
            '"semantic_selection_ledger" | "interpreted_model" | "product",',
            1,
        )
        selection_path = (
            checker.SPEC / "requirements" / "REQ-P-SELECTION-AND-ACCEPTANCE.md"
        )
        with self.assertRaisesRegex(checker.CheckFailure, "second acceptance record"):
            checker.check_selection_acceptance_topology(
                product,
                selection_path.read_text(encoding="utf-8"),
                path,
            )

    def test_missing_compiler_candidate_provenance_fails(self) -> None:
        path = checker.SPEC / "requirements" / "REQ-P-SELECTION-AND-ACCEPTANCE.md"
        text = path.read_text(encoding="utf-8").replace(
            "compiler_invocation: CompilerInvocation",
            "compiler_invocation_removed: CompilerInvocation",
            1,
        )
        with self.assertRaisesRegex(
            checker.CheckFailure, "compiler_invocation: CompilerInvocation"
        ):
            checker.check_semantic_compilation_contract(text, path)

    def test_quickstart_role_claim_without_disclaimer_fails(self) -> None:
        path = checker.ROOT / "QUICKSTART.md"
        text = path.read_text(encoding="utf-8").replace(
            "This bare model call is exploratory probabilistic processing.",
            "This is an activated Reviewer call.",
            1,
        )
        with self.assertRaisesRegex(checker.CheckFailure, "exploratory probabilistic"):
            checker.check_exploratory_quickstart(text, path)

    def test_legacy_preparer_refuses_active_what(self) -> None:
        with self.assertRaisesRegex(
            preparer.PreparationFailure, "legacy preparer is historical-only"
        ):
            preparer.require_historical_preparation_basis(
                "sha256:" + "0" * 64,
                preparer.HISTORICAL_PROFILE_SHA256,
                preparer.HISTORICAL_FRAME_BASIS_SHA256,
            )

    def test_legacy_preparer_admits_only_historical_exact_basis(self) -> None:
        preparer.require_historical_preparation_basis(
            preparer.HISTORICAL_WHAT_MEMBER_SET_IDENTITY,
            preparer.HISTORICAL_PROFILE_SHA256,
            preparer.HISTORICAL_FRAME_BASIS_SHA256,
        )

    def test_checker_passes_with_python_optimization(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(Path(checker.__file__))],
            cwd=checker.ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        result = json.loads(completed.stdout)
        self.assertTrue(result["structural_checks_pass"])
        self.assertNotIn("valid", result)


if __name__ == "__main__":
    unittest.main()
