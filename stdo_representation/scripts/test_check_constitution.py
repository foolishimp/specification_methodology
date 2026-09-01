from __future__ import annotations

import copy
import hashlib
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
        cls.axiom_root = ROOT.parent / "axiom_indexer"

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
        self.assertEqual(result["product"]["exact_version"], "2.5.0-rc.4")
        self.assertEqual(result["product"]["version_line"], "2.5.0")
        self.assertEqual(result["product"]["represented_stdo_version"], "2.5.0")
        self.assertEqual(result["historical_bootstrap"]["status"], "conserved")
        self.assertEqual(result["candidate_release"]["status"], "frozen")
        self.assertEqual(result["frame_basis"]["status"], "accepted_and_bound")
        self.assertTrue(result["stdo_status"]["valid"])
        self.assertEqual(result["stdo_status"]["toolchain"], "stdo 0.1.2")
        self.assertEqual(
            result["frame_basis"]["decision_sha256"],
            "sha256:" + CHECKER.FRAME_DECISION_SHA256,
        )
        self.assertEqual(
            result["candidate_release"]["inventory_sha256"],
            "sha256:" + CHECKER.CANDIDATE_INVENTORY_SHA256,
        )
        self.assertEqual(
            result["candidate_release"]["release_record_sha256"],
            "sha256:" + CHECKER.CANDIDATE_RELEASE_SHA256,
        )

    def test_representation_version_is_derived_from_represented_stdo(self) -> None:
        self.assertEqual(
            CHECKER.derive_represented_stdo_semver(CHECKER.STDO_BASIS),
            CHECKER.REPRESENTATION_VERSION_LINE,
        )
        self.assertEqual(
            CHECKER.validate_representation_version(
                CHECKER.REPRESENTATION_VERSION_LINE, CHECKER.STDO_BASIS
            ),
            [],
        )

    def test_representation_version_mismatch_is_rejected(self) -> None:
        failures = CHECKER.validate_representation_version("2.5.1", CHECKER.STDO_BASIS)
        self.assertIn(
            "Representation version does not match represented STDO semantic version",
            failures,
        )

    def test_exact_cohort_versions_match_without_collapsing_products(self) -> None:
        self.assertEqual(
            CHECKER.validate_coordinated_versions(
                "2.5.0-rc.4",
                "stdo://releases/v2.5.0-rc.4/",
                "2.5.0-rc.4",
            ),
            [],
        )

    def test_exact_cohort_rejects_any_suffix_mismatch(self) -> None:
        failures = CHECKER.validate_coordinated_versions(
            "2.5.0-rc.4",
            "stdo://releases/v2.5.0-rc.3/",
            "2.5.0-rc.2",
        )
        self.assertIn(
            "Representation exact version does not match Source STDO", failures
        )
        self.assertIn(
            "Axiom Indexer exact version does not match Representation", failures
        )

    def test_standards_delta_conserves_and_changes_by_exact_digest(self) -> None:
        delta = CHECKER.standards_member_delta(
            [
                {"path": "A.md", "sha256": "a" * 64},
                {"path": "B.md", "sha256": "b" * 64},
            ],
            [
                {"path": "A.md", "sha256": "a" * 64},
                {"path": "B.md", "sha256": "c" * 64},
            ],
        )
        self.assertEqual(
            delta,
            {"conserved": ["A.md"], "changed": ["B.md"], "added": [], "removed": []},
        )

    def test_predecessor_delta_reacquires_only_immutable_stdo_tags(self) -> None:
        rc2, rc2_failures = CHECKER.immutable_stdo_standards_members(ROOT, "RC2")
        rc3, rc3_failures = CHECKER.immutable_stdo_standards_members(ROOT, "RC3")
        self.assertEqual(rc2_failures, [])
        self.assertEqual(rc3_failures, [])
        self.assertEqual(len(rc2), 52)
        self.assertEqual(len(rc3), 52)
        self.assertFalse(
            hasattr(CHECKER, "TRANSITION_SOURCE_CORPUS_PATH"),
            "the candidate must not consume the excluded RC3 draft corpus",
        )

    def test_program_conservation_protects_entries_outside_changed_members(
        self,
    ) -> None:
        previous = {
            "source_basis": "stdo://releases/v2.5.0-rc.3/standards/",
            "symbols": [
                {
                    "uri": "urn:test:stable",
                    "label": "Stable",
                    "source_refs": [
                        "stdo://releases/v2.5.0-rc.3/standards/STABLE.md#law"
                    ],
                },
                {
                    "uri": "urn:test:changed",
                    "label": "Before",
                    "source_refs": [
                        "stdo://releases/v2.5.0-rc.3/standards/CHANGED.md#law"
                    ],
                },
            ],
            "clauses": [],
            "residuals": [],
        }
        current = copy.deepcopy(previous)
        current["source_basis"] = "stdo://releases/v2.5.0-rc.4/standards/"
        encoded = json.dumps(current).replace("v2.5.0-rc.3", "v2.5.0-rc.4")
        current = json.loads(encoded)
        current["symbols"][1]["label"] = "After"
        self.assertEqual(
            CHECKER.validate_program_conservation(previous, current, {"CHANGED.md"}),
            [],
        )
        current["symbols"][0]["label"] = "Drift"
        self.assertTrue(
            any(
                failure.startswith("unaffected symbols entry was not conserved")
                for failure in CHECKER.validate_program_conservation(
                    previous, current, {"CHANGED.md"}
                )
            )
        )

    def test_source_corpus_binds_overlay_manifest_and_derived_routes(self) -> None:
        corpus_path = (
            ROOT
            / "build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.4"
            / "source-corpus.json"
        )
        if not corpus_path.is_file():
            self.skipTest("RC4 source corpus is not present")
        overlay = json.loads((ROOT / "stdo_representation.json").read_text())
        corpus = json.loads(corpus_path.read_text())
        installed_path = (
            Path.home()
            / "Library/Application Support/STDO/releases/v2.5.0-rc.4/manifest.json"
        )
        installed_bytes = installed_path.read_bytes()
        installed = json.loads(installed_bytes)
        compression = json.loads(
            (corpus_path.parent / "axiomatic-program.json").read_text()
        )
        logical_index = json.loads(
            (corpus_path.parent / "logical-constraint-map.json").read_text()
        )
        self.assertEqual(
            CHECKER.validate_source_corpus(
                corpus,
                overlay,
                installed,
                hashlib.sha256(installed_bytes).hexdigest(),
                compression,
                logical_index,
            ),
            [],
        )

    def test_same_version_axiom_candidate_binds_exact_conserved_mechanics(self) -> None:
        axiom_root = ROOT.parent / "axiom_indexer"
        self.assertEqual(CHECKER.validate_axiom_candidate(axiom_root, "2.5.0-rc.4"), [])

    def test_non_exact_represented_stdo_basis_is_rejected(self) -> None:
        failures = CHECKER.validate_representation_version(
            CHECKER.REPRESENTATION_VERSION_LINE, "stdo://channels/2.5.0"
        )
        self.assertIn(
            "Source STDO basis does not encode an exact RC semantic version",
            failures,
        )

    def test_live_stdo_status_rejects_overlay_selector_drift(self) -> None:
        overlay = json.loads((ROOT / "stdo_representation.json").read_text())
        overlay["constitution"]["stdo"]["selector"] = "stdo://channels/9.9.9"
        manifest_path = (
            Path.home()
            / "Library/Application Support/STDO/releases/v2.5.0-rc.4/manifest.json"
        )
        manifest_bytes = manifest_path.read_bytes()
        failures, evidence = CHECKER.validate_live_stdo_status(
            ROOT,
            overlay,
            json.loads(manifest_bytes),
            hashlib.sha256(manifest_bytes).hexdigest(),
        )
        self.assertIn("live stdo status has wrong selector", failures)
        self.assertFalse(evidence["valid"])

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
        self.assertEqual(CHECKER.validate_current_projection(program, logical_map), [])

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

    def test_validation_report_material_tamper_is_rejected(self) -> None:
        compression = CHECKER.load_json(ROOT / CHECKER.COMPRESSION_PATH)
        logical_index = CHECKER.load_json(ROOT / CHECKER.INDEX_PATH)
        with tempfile.TemporaryDirectory() as temp_dir:
            report_path = Path(temp_dir) / "validation-report.json"
            report_path.write_bytes(
                (ROOT / CHECKER.VALIDATION_REPORT_PATH).read_bytes()
            )
            self.assertEqual(
                CHECKER.validate_validation_report(
                    report_path,
                    compression,
                    logical_index,
                ),
                [],
            )
            report = CHECKER.load_json(report_path)
            report["program_sha256"] = "sha256:" + "0" * 64
            report["program_uri"] = "urn:wrong:program"
            report["resolved_sources"] = []
            report_path.write_text(json.dumps(report), encoding="utf-8")
            failures = CHECKER.validate_validation_report(
                report_path,
                compression,
                logical_index,
            )
            self.assertIn("exact RC4 validation report bytes changed", failures)
            self.assertIn(
                "RC4 validation report binds the wrong program digest", failures
            )
            self.assertIn("RC4 validation report binds the wrong program URI", failures)
            self.assertIn(
                "RC4 validation report changes the resolved source closure", failures
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
                "1896829cf06a4fba45f6e8092fc54cf8e958ca5d15ba84f5542eaef966f2a4ab",
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

    def test_c04_semantic_inversion_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            self.copy_candidate_release_subject(temp_root)
            release_path = temp_root / CHECKER.CANDIDATE_RELEASE_PATH
            record = release_path.read_text(encoding="utf-8")
            record = record.replace(
                "Hashes prove identity and frontier membership, not semantic\n"
                "  qualification.",
                "Hashes alone prove semantic qualification.",
                1,
            )
            release_path.write_text(record, encoding="utf-8")
            failures = CHECKER.validate_candidate_release(temp_root)
            self.assertIn("candidate release record bytes changed", failures)
            self.assertIn(
                "candidate release record lacks exact C04 semantics", failures
            )

    def test_current_projection_rejects_mutable_or_foreign_routes(self) -> None:
        compression = CHECKER.load_json(ROOT / CHECKER.COMPRESSION_PATH)
        logical_index = CHECKER.load_json(ROOT / CHECKER.INDEX_PATH)
        changed = copy.deepcopy(compression)
        changed["frame_refs"][0] = (
            "repo://specification-methodology/candidates/v2.5.0-rc.2/"
            "REFERENCE_FRAME_METHOD.md#reference-frame-laws"
        )
        changed["source_basis"] = "stdo://releases/v2.5.0-rc.1/standards/"
        failures = CHECKER.validate_current_projection(changed, logical_index)
        self.assertIn(
            "Product compression has the wrong current RC4 frame references", failures
        )
        self.assertIn(
            "current RC4 Product artifacts retain mutable candidate routes", failures
        )
        self.assertIn(
            "current RC4 Product artifacts retain foreign STDO routes", failures
        )

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
        failures = CHECKER.validate_current_projection(changed, logical_index)
        self.assertIn(
            "current RC4 Product compression changes required clause: engagement-return-topology",
            failures,
        )

    def test_required_cohort_clause_semantics_cannot_drift(self) -> None:
        compression = CHECKER.load_json(ROOT / CHECKER.COMPRESSION_PATH)
        logical_index = CHECKER.load_json(ROOT / CHECKER.INDEX_PATH)
        changed = copy.deepcopy(compression)
        clause = next(
            row
            for row in changed["clauses"]
            if row["uri"].endswith("cohort-publication-fails-closed")
        )
        clause["statement"] = "Publish each Product sequentially."
        failures = CHECKER.validate_current_projection(changed, logical_index)
        self.assertIn(
            "current RC4 Product compression changes required clause: "
            "cohort-publication-fails-closed",
            failures,
        )

    def test_changed_frontier_clause_route_cannot_drift(self) -> None:
        compression = CHECKER.load_json(ROOT / CHECKER.COMPRESSION_PATH)
        logical_index = CHECKER.load_json(ROOT / CHECKER.INDEX_PATH)
        changed = copy.deepcopy(compression)
        clause = next(
            row
            for row in changed["clauses"]
            if row["uri"].endswith("bootstrap-resolves-exact-basis")
        )
        clause["source_refs"] = [
            CHECKER.STDO_BASIS + "standards/RELEASE_METHOD.md#position"
        ]
        failures = CHECKER.validate_current_projection(changed, logical_index)
        self.assertIn(
            "current RC4 Product compression changes required source routes: "
            "bootstrap-resolves-exact-basis",
            failures,
        )

    def test_quickstart_passes_explicit_verified_store_to_axiom_checker(self) -> None:
        quickstart = (ROOT / "QUICKSTART.md").read_text(encoding="utf-8")
        self.assertIn(
            'STDO_STORE="${STDO_STORE:-$HOME/Library/Application Support/STDO}"',
            quickstart,
        )
        self.assertIn(
            '"$AXIOM_INDEXER_ROOT/scripts/check_constitution.py" \\\n  --stdo-store "$STDO_STORE"',
            quickstart,
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
                    failure.startswith("native skill lacks current projection claim")
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
