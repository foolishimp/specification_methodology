from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
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

    def copy_candidate_release_subject(self, target_root: Path) -> None:
        for path in CHECKER.PRODUCT_FILES:
            target = target_root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / path).read_bytes())
        for path in CHECKER.PRODUCT_LINKS:
            target = target_root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.symlink_to((ROOT / path).readlink())
        release_target = target_root / CHECKER.CANDIDATE_RELEASE_PATH
        release_target.parent.mkdir(parents=True, exist_ok=True)
        release_target.write_bytes((ROOT / CHECKER.CANDIDATE_RELEASE_PATH).read_bytes())

    def copy_native_layout(self, target_root: Path) -> None:
        for relative in (
            CHECKER.SKILL_ROOT / "SKILL.md",
            CHECKER.SKILL_ROOT / "references/codex.md",
            CHECKER.SKILL_ROOT / "references/claude.md",
        ):
            target = target_root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / relative).read_bytes())

    def test_current_tree_passes_focused_audit(self) -> None:
        result = CHECKER.audit(ROOT, self.axiom_root)
        self.assertTrue(result["valid"], result["failures"])
        self.assertEqual(result["product"]["member_count"], 8)
        self.assertEqual(result["product"]["version_line"], "2.5.0")
        self.assertEqual(result["product"]["represented_stdo_version"], "2.5.0")
        self.assertEqual(result["historical_bootstrap"]["status"], "conserved")
        self.assertEqual(result["candidate_release"]["status"], "frozen")
        self.assertEqual(result["frame_basis"]["status"], "accepted_and_bound")
        self.assertEqual(
            result["frame_basis"]["decision_sha256"],
            "sha256:" + CHECKER.FRAME_DECISION_SHA256,
        )
        self.assertEqual(
            result["candidate_release"]["inventory_sha256"],
            "sha256:" + CHECKER.CANDIDATE_INVENTORY_SHA256,
        )

    def test_representation_version_is_derived_from_represented_stdo(self) -> None:
        self.assertEqual(
            CHECKER.derive_represented_stdo_semver(CHECKER.STDO_BASIS),
            CHECKER.REPRESENTATION_VERSION,
        )
        self.assertEqual(
            CHECKER.validate_representation_version(
                CHECKER.REPRESENTATION_VERSION, CHECKER.STDO_BASIS
            ),
            [],
        )

    def test_representation_version_mismatch_is_rejected(self) -> None:
        failures = CHECKER.validate_representation_version("2.5.1", CHECKER.STDO_BASIS)
        self.assertIn(
            "Representation version does not match represented STDO semantic version",
            failures,
        )

    def test_non_exact_represented_stdo_basis_is_rejected(self) -> None:
        failures = CHECKER.validate_representation_version(
            CHECKER.REPRESENTATION_VERSION, "stdo://channels/2.5.0"
        )
        self.assertIn(
            "Source STDO basis does not encode an exact RC semantic version",
            failures,
        )

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
        self.assertEqual(CHECKER.validate_rc2_projection(program, logical_map), [])

    def test_program_drift_invalidates_map_binding(self) -> None:
        program = CHECKER.load_json(ROOT / CHECKER.PROGRAM_PATH)
        logical_map = CHECKER.load_json(ROOT / CHECKER.MAP_PATH)
        changed = copy.deepcopy(program)
        changed["uri"] += ":changed"
        failures = CHECKER.validate_program_map(changed, logical_map)
        self.assertIn(
            "Product index does not bind the Product compression URI", failures
        )
        self.assertIn(
            "Product index does not bind the canonical Product compression", failures
        )

    def test_index_source_drift_invalidates_compression_binding(self) -> None:
        compression = CHECKER.load_json(ROOT / CHECKER.COMPRESSION_PATH)
        logical_index = CHECKER.load_json(ROOT / CHECKER.INDEX_PATH)
        changed = copy.deepcopy(logical_index)
        changed["source_basis"] = "stdo://releases/v2.4.3-rc.3/standards/"
        failures = CHECKER.validate_compression_index(compression, changed)
        self.assertIn("Product index selects the wrong source basis", failures)

    def test_index_population_drift_invalidates_compression_binding(self) -> None:
        compression = CHECKER.load_json(ROOT / CHECKER.COMPRESSION_PATH)
        logical_index = CHECKER.load_json(ROOT / CHECKER.INDEX_PATH)
        changed = copy.deepcopy(logical_index)
        changed["clauses"][0]["uri"] += ":changed"
        failures = CHECKER.validate_compression_index(compression, changed)
        self.assertIn(
            "Product index changes the compression clauses identities", failures
        )
        self.assertIn("Product index source routes do not match index items", failures)

    def test_product_definition_identity_collapse_is_rejected(self) -> None:
        compression = CHECKER.load_json(ROOT / CHECKER.COMPRESSION_PATH)
        changed = copy.deepcopy(compression)
        clause = next(
            row
            for row in changed["clauses"]
            if row["uri"].endswith("product-definition-schema-closes-routing-shape")
        )
        clause["statement"] = "A Product Definition binds one Product identity."
        failures = CHECKER.validate_semantic_boundaries(changed)
        self.assertIn(
            "Product compression collapses Product-Definition and Product identity",
            failures,
        )

    def test_release_cut_install_collapse_is_rejected(self) -> None:
        compression = CHECKER.load_json(ROOT / CHECKER.COMPRESSION_PATH)
        changed = copy.deepcopy(compression)
        clause = next(
            row
            for row in changed["clauses"]
            if row["uri"].endswith("release-rc-is-immutable")
        )
        clause["arguments"][0][
            "ref"
        ] = "urn:stdo-representation:a-c-text:symbol:install"
        failures = CHECKER.validate_semantic_boundaries(changed)
        self.assertIn(
            "Product compression does not bind RC publication to Release Cut",
            failures,
        )

    def test_historical_bootstrap_release_record_cannot_drift(self) -> None:
        source = ROOT / CHECKER.HISTORICAL_BOOTSTRAP_RELEASE_PATH
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            self.assertEqual(
                CHECKER.validate_historical_bootstrap(temp_root),
                ["missing historical STDO Representation 0.1.0 release record"],
            )
            target = temp_root / CHECKER.HISTORICAL_BOOTSTRAP_RELEASE_PATH
            target.parent.mkdir(parents=True)
            target.write_bytes(source.read_bytes())
            self.assertEqual(CHECKER.validate_historical_bootstrap(temp_root), [])
            target.write_bytes(source.read_bytes() + b"\nchanged\n")
            self.assertEqual(
                CHECKER.validate_historical_bootstrap(temp_root),
                ["historical STDO Representation 0.1.0 release record changed"],
            )

    def test_candidate_member_byte_drift_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            self.copy_candidate_release_subject(temp_root)
            skill_path = temp_root / CHECKER.SKILL_ROOT / "SKILL.md"
            skill_path.write_bytes(skill_path.read_bytes() + b"\nchanged\n")
            failures = CHECKER.validate_candidate_release(temp_root)
            self.assertIn(
                "candidate release declared Product inventory does not match live member bytes",
                failures,
            )
            self.assertIn(
                "candidate Product inventory digest does not match frozen 2.5.0 inventory",
                failures,
            )

    def test_candidate_declared_inventory_drift_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            self.copy_candidate_release_subject(temp_root)
            release_path = temp_root / CHECKER.CANDIDATE_RELEASE_PATH
            record = release_path.read_text(encoding="utf-8")
            record = record.replace(
                "8abcf51c1d4d94e8183618898f7ae84829c12fc50458d9cd8555fa0ba661f4ab",
                "0" * 64,
                1,
            )
            release_path.write_text(record, encoding="utf-8")
            failures = CHECKER.validate_candidate_release(temp_root)
            self.assertIn(
                "candidate release declared Product inventory does not match live member bytes",
                failures,
            )

    def test_predecessor_disposition_drift_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            self.copy_candidate_release_subject(temp_root)
            release_path = temp_root / CHECKER.CANDIDATE_RELEASE_PATH
            record = release_path.read_text(encoding="utf-8")
            record = record.replace(
                "`STDO-REP-2.5-C02`: **superseded**",
                "`STDO-REP-2.5-C02`: **refined**",
                1,
            )
            release_path.write_text(record, encoding="utf-8")
            failures = CHECKER.validate_candidate_release(temp_root)
            self.assertTrue(
                any(
                    failure.startswith(
                        "candidate release lacks exact predecessor disposition"
                    )
                    for failure in failures
                )
            )

    def test_rc2_projection_rejects_mutable_or_rc1_routes(self) -> None:
        compression = CHECKER.load_json(ROOT / CHECKER.COMPRESSION_PATH)
        logical_index = CHECKER.load_json(ROOT / CHECKER.INDEX_PATH)
        changed = copy.deepcopy(compression)
        changed["frame_refs"][0] = (
            "repo://specification-methodology/candidates/v2.5.0-rc.2/"
            "REFERENCE_FRAME_METHOD.md#reference-frame-laws"
        )
        changed["source_basis"] = "stdo://releases/v2.5.0-rc.1/standards/"
        failures = CHECKER.validate_rc2_projection(changed, logical_index)
        self.assertIn(
            "Product compression has the wrong RC2 frame references", failures
        )
        self.assertIn("RC2 Product artifacts retain mutable candidate routes", failures)
        self.assertIn("RC2 Product artifacts retain RC1 Source STDO routes", failures)

    def test_required_frame_clause_semantics_cannot_drift(self) -> None:
        compression = CHECKER.load_json(ROOT / CHECKER.COMPRESSION_PATH)
        logical_index = CHECKER.load_json(ROOT / CHECKER.INDEX_PATH)
        changed = copy.deepcopy(compression)
        clause = next(
            row
            for row in changed["clauses"]
            if row["uri"].endswith("engagement-return-topology")
        )
        clause["statement"] += " Reviewer assigns priority."
        failures = CHECKER.validate_rc2_projection(changed, logical_index)
        self.assertIn(
            "RC2 Product compression changes frame clause: engagement-return-topology",
            failures,
        )

    def test_native_layout_requires_open_space_and_action_last(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            self.copy_native_layout(temp_root)
            codex_path = temp_root / CHECKER.SKILL_ROOT / "references/codex.md"
            text = codex_path.read_text(encoding="utf-8")
            text = text.replace("7. `ACTION`", "0. `ACTION`", 1)
            text = text.replace(
                "not a prompt engine, schema, selector, or renderer",
                "a prompt engine",
                1,
            )
            codex_path.write_text(text, encoding="utf-8")
            failures = CHECKER.validate_native_layout(temp_root)
            self.assertIn(
                "codex layout does not preserve the seven-part order", failures
            )
            self.assertIn("codex layout loses the no-prompt-engine boundary", failures)

    def test_native_skill_preserves_reviewer_executive_split(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            self.copy_native_layout(temp_root)
            skill_path = temp_root / CHECKER.SKILL_ROOT / "SKILL.md"
            text = skill_path.read_text(encoding="utf-8").replace(
                "Executive alone consumes the complete Product view",
                "Reviewer assigns priority",
                1,
            )
            skill_path.write_text(text, encoding="utf-8")
            failures = CHECKER.validate_native_layout(temp_root)
            self.assertTrue(
                any(
                    failure.startswith("native skill lacks RC2 projection claim")
                    for failure in failures
                )
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

    def test_overlay_requires_exact_axiom_indexer_composition(self) -> None:
        overlay = json.loads((ROOT / "stdo_representation.json").read_text())
        overlay["composition"][0]["target_definition_id"] = "urn:test:wrong"
        failures = CHECKER.validate_overlay(overlay)
        self.assertIn(
            "Axiom Indexer Product dependency composition is not exact", failures
        )

    def test_accepted_frame_basis_binding_cannot_drift(self) -> None:
        overlay = json.loads((ROOT / "stdo_representation.json").read_text())
        overlay["reference_frame_bases"] = [{"uri": "urn:test:unaccepted"}]
        failures = CHECKER.validate_overlay(overlay)
        self.assertIn("accepted project frame basis binding is not exact", failures)

    def test_accepted_frame_basis_binds_exact_bytes(self) -> None:
        self.assertEqual(CHECKER.validate_frame_basis(ROOT), [])

    def test_frame_acceptance_decision_drift_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            for relative in (CHECKER.FRAME_PATH, CHECKER.FRAME_DECISION_PATH):
                target = temp_root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((ROOT / relative).read_bytes())
            decision_path = temp_root / CHECKER.FRAME_DECISION_PATH
            decision_path.write_bytes(decision_path.read_bytes() + b"\n")
            self.assertIn(
                "project frame-basis acceptance record bytes changed",
                CHECKER.validate_frame_basis(temp_root),
            )


if __name__ == "__main__":
    unittest.main()
