from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

import check_constitution as subject


TEST_STORE = Path("/tmp/axiom-indexer-injected-stdo-store")


def valid_stdo_status(store: Path, definition: Path) -> dict[str, object]:
    resolved_store = store.expanduser().absolute()
    return {
        "basis": subject.TARGET_STDO_BASIS,
        "cut": subject.TARGET_STDO_CUT,
        "definition": str(definition),
        "definition_id": "urn:stdo:product-definition:axiom-indexer",
        "failures": [],
        "installed": True,
        "manifest_sha256": subject.TARGET_STDO_MANIFEST,
        "path": str(resolved_store / "releases" / subject.TARGET_STDO_CUT),
        "release": {
            "commit": subject.SOURCE_STDO_COMMIT,
            "cut": subject.TARGET_STDO_CUT,
            "project_release_namespace": "specification_methodology",
            "project_subtree_root": "specification_methodology",
            "project_subtree_tree": subject.SOURCE_STDO_SUBTREE_TREE,
            "qualified_ref": subject.SOURCE_STDO_QUALIFIED_REF,
            "standards_tree": subject.SOURCE_STDO_STANDARDS_TREE,
            "tag_object": subject.SOURCE_STDO_TAG_OBJECT,
            "tree": subject.SOURCE_STDO_REPOSITORY_TREE,
        },
        "schema": str(
            resolved_store
            / "releases"
            / subject.TARGET_STDO_CUT
            / "standards"
            / "schemas"
            / "product-definition.schema.json"
        ),
        "valid": True,
    }


class CutAlignmentTests(unittest.TestCase):
    def test_exact_rc4_alignment_passes(self) -> None:
        self.assertEqual(
            [],
            subject.validate_cut_alignment(
                "v2.5.0-rc.4", "stdo://releases/v2.5.0-rc.4/"
            ),
        )

    def test_different_rc_ordinal_fails(self) -> None:
        self.assertEqual(
            ["Axiom product-local cut does not match Source STDO cut"],
            subject.validate_cut_alignment(
                "v2.5.0-rc.3", "stdo://releases/v2.5.0-rc.4/"
            ),
        )

    def test_channel_is_not_an_exact_cut(self) -> None:
        self.assertEqual(
            ["Source STDO basis does not name one exact release cut"],
            subject.validate_cut_alignment("v2.5.0-rc.4", "stdo://channels/2.5.0"),
        )


class ConstitutionTests(unittest.TestCase):
    def test_readme_passes_an_explicit_verified_store_to_check(self) -> None:
        readme = (subject.ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(
            'STDO_STORE="${STDO_STORE:-$HOME/Library/Application Support/STDO}"',
            readme,
        )
        self.assertIn('stdo --store "$STDO_STORE" verify v2.5.0-rc.4', readme)
        self.assertIn(
            'python3 scripts/check_constitution.py --stdo-store "$STDO_STORE"',
            readme,
        )

    def test_product_member_inventory_is_exact(self) -> None:
        failures, digest = subject.verify_product_members()
        self.assertEqual([], failures)
        self.assertEqual(subject.PRODUCT_INVENTORY_SHA256, digest)

    def test_current_constitution_is_valid(self) -> None:
        result = subject.check_constitution(
            stdo_store=TEST_STORE,
            status_runner=valid_stdo_status,
        )
        self.assertTrue(result["dependency_valid"], result["failures"])
        self.assertTrue(result["governance_valid"], result["failures"])
        self.assertTrue(result["mechanics_valid"], result["failures"])
        self.assertTrue(result["release_ready"], result["failures"])
        self.assertTrue(result["stdo_status_valid"], result["failures"])
        self.assertEqual("target", result["basis_state"])
        self.assertEqual("completed-and-closed", result["publication_phase"])
        self.assertEqual(
            subject.FRAME_DECISION_PUBLISHED_AXIOM,
            result["published_axiom"],
        )

    def test_missing_explicit_store_is_not_release_ready(self) -> None:
        result = subject.check_constitution(status_runner=valid_stdo_status)
        self.assertFalse(result["dependency_valid"])
        self.assertFalse(result["release_ready"])
        self.assertIn(
            "explicit STDO store is required for release readiness",
            result["failures"],
        )


class FrameDecisionTests(unittest.TestCase):
    @staticmethod
    def _decision() -> dict[str, object]:
        return json.loads((subject.ROOT / subject.FRAME_DECISION_PATH).read_text())

    def test_current_decision_structure_is_exact(self) -> None:
        self.assertEqual([], subject.validate_frame_decision(self._decision()))

    def test_kind_and_scope_tamper_fail_closed(self) -> None:
        for field, value in (
            ("kind", "axiom-indexer.frame-basis-proposal"),
            ("scope", "all Axiom and Representation bytes"),
        ):
            with self.subTest(field=field):
                decision = self._decision()
                decision[field] = value
                failures = subject.validate_frame_decision(decision)
                self.assertIn(f"frame-basis decision mismatch: {field}", failures)

    def test_publication_identity_and_acceptance_tamper_fail_closed(self) -> None:
        cases = (
            ("publication_phase", None, "open"),
            ("product_acceptance", None, "accepted"),
            ("published_axiom", "tag_object", "0" * 40),
            ("source_stdo", "tag_object", "1" * 40),
        )
        for field, nested, value in cases:
            with self.subTest(field=field, nested=nested):
                decision = self._decision()
                if nested is None:
                    decision[field] = value
                else:
                    container = decision[field]
                    self.assertIsInstance(container, dict)
                    container[nested] = value
                failures = subject.validate_frame_decision(decision)
                self.assertIn(f"frame-basis decision mismatch: {field}", failures)


class ReleaseRecordTests(unittest.TestCase):
    @staticmethod
    def _release_bytes() -> bytes:
        return (subject.ROOT / subject.RELEASE_PATH).read_bytes()

    def test_current_release_record_is_exact(self) -> None:
        self.assertEqual(
            [], subject.validate_release_record_bytes(self._release_bytes())
        )

    def test_candidate_status_tamper_fails_closed(self) -> None:
        text = self._release_bytes().decode("utf-8")
        tampered = text.replace(
            subject.RELEASE_STATUS,
            "Status: published and accepted Product.",
            1,
        ).encode("utf-8")
        failures = subject.validate_release_record_bytes(tampered)
        self.assertIn("release record digest mismatch", failures)
        self.assertIn("release record candidate status mismatch", failures)

    def test_semantic_claim_tamper_fails_closed(self) -> None:
        text = self._release_bytes().decode("utf-8")
        tampered = text.replace(
            subject.RELEASE_SEMANTIC_CLAIM,
            subject.RELEASE_SEMANTIC_CLAIM.replace(
                "emits deterministic diagnostics", "certifies semantic truth"
            ),
            1,
        ).encode("utf-8")
        failures = subject.validate_release_record_bytes(tampered)
        self.assertIn("release record digest mismatch", failures)
        self.assertIn("release record semantic claim mismatch", failures)

    def test_predecessor_disposition_tamper_fails_closed(self) -> None:
        text = self._release_bytes().decode("utf-8")
        tampered = text.replace(
            subject.RELEASE_PREDECESSOR_DISPOSITION,
            subject.RELEASE_PREDECESSOR_DISPOSITION.replace(
                "**conserved**", "**withdrawn**"
            ),
            1,
        ).encode("utf-8")
        failures = subject.validate_release_record_bytes(tampered)
        self.assertIn("release record digest mismatch", failures)
        self.assertIn("release record predecessor disposition mismatch", failures)


class STDOStatusEvidenceTests(unittest.TestCase):
    def test_unavailable_status_fails_closed(self) -> None:
        def unavailable(_store: Path, _definition: Path) -> dict[str, object]:
            raise RuntimeError("injected unavailable store")

        failures: list[str] = []
        status = subject.verify_stdo_status(TEST_STORE, failures, unavailable)
        self.assertIsNone(status)
        self.assertEqual(
            ["STDO status evidence unavailable: injected unavailable store"], failures
        )

    def test_basis_manifest_and_release_identity_mismatch_fail_closed(self) -> None:
        cases = (
            ("basis", None, "stdo://releases/v2.5.0-rc.3/"),
            ("manifest_sha256", None, "0" * 64),
            ("valid", None, False),
            ("tag_object", "release", "0" * 40),
            ("commit", "release", "1" * 40),
            ("tree", "release", "2" * 40),
        )
        definition = (subject.ROOT / "stdo_default.json").resolve()
        for key, container, value in cases:
            with self.subTest(key=key):
                status = copy.deepcopy(valid_stdo_status(TEST_STORE, definition))
                target = status if container is None else status[container]
                self.assertIsInstance(target, dict)
                target[key] = value

                def runner(_store: Path, _definition: Path) -> dict[str, object]:
                    return status

                failures: list[str] = []
                subject.verify_stdo_status(TEST_STORE, failures, runner)
                self.assertTrue(failures, f"{key} mismatch was accepted")


if __name__ == "__main__":
    unittest.main()
