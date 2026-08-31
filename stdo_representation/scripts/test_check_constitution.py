from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts/check_constitution.py"
SPEC = importlib.util.spec_from_file_location("check_constitution", MODULE_PATH)
assert SPEC and SPEC.loader
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class ThinConstitutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.axiom_root = (
            Path.home()
            / "Library/Application Support/Axiom Indexer/releases/v0.1.0-rc.1"
        )

    def test_current_tree_passes_focused_audit(self) -> None:
        result = CHECKER.audit(ROOT, self.axiom_root)
        self.assertTrue(result["valid"], result["failures"])
        self.assertEqual(result["product"]["member_count"], 8)

    def test_program_digest_matches_frozen_authoring_map(self) -> None:
        program = CHECKER.load_json(ROOT / CHECKER.PROGRAM_PATH)
        logical_map = CHECKER.load_json(ROOT / CHECKER.MAP_PATH)
        self.assertEqual(
            "sha256:" + CHECKER.canonical_sha256(program),
            logical_map["program_sha256"],
        )
        self.assertEqual(
            CHECKER.validate_program_map(program, logical_map),
            [],
        )

    def test_program_drift_invalidates_map_binding(self) -> None:
        program = CHECKER.load_json(ROOT / CHECKER.PROGRAM_PATH)
        logical_map = CHECKER.load_json(ROOT / CHECKER.MAP_PATH)
        changed = copy.deepcopy(program)
        changed["uri"] += ":changed"
        failures = CHECKER.validate_program_map(changed, logical_map)
        self.assertIn("Product map does not bind the Product program URI", failures)
        self.assertIn(
            "Product map does not bind the canonical Product program", failures
        )

    def test_overlay_rejects_heavy_tenant_reactivation(self) -> None:
        overlay = json.loads((ROOT / "stdo_representation.json").read_text())
        overlay["how"]["build_tenants"][0][
            "id"
        ] = "urn:stdo-representation:build-tenant:gtl"
        failures = CHECKER.validate_overlay(overlay)
        self.assertIn(
            "active build tenant is not the thin Axiom Indexer tenant",
            failures,
        )

    def test_frame_basis_binding_cannot_drift(self) -> None:
        overlay = json.loads((ROOT / "stdo_representation.json").read_text())
        overlay["reference_frame_bases"] = [{"uri": "urn:test:unaccepted"}]
        failures = CHECKER.validate_overlay(overlay)
        self.assertIn("accepted project frame basis binding is not exact", failures)

    def test_frame_acceptance_binds_exact_bytes(self) -> None:
        self.assertEqual(CHECKER.validate_frame_acceptance(ROOT), [])


if __name__ == "__main__":
    unittest.main()
