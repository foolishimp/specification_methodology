from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
METHOD = ROOT / "specification/standards/REFERENCE_FRAME_METHOD.md"
PROFILE = ROOT / "specification/standards/STDO_REFERENCE_FRAME_BASELINE.md"
SPEC_METHOD = ROOT / "specification/standards/SPEC_METHOD.md"
PRODUCT = ROOT / "specification/PRODUCT.md"
BASIS = ROOT / "specification/REFERENCE_FRAME_BASIS.md"
DEFINITION = ROOT / "stdo_default.json"
COMPRESSION = ROOT / "specification/standards/authority_compressions/stdo_compressed.md"


class ReferenceFrameBoundaryTests(unittest.TestCase):
    def test_pure_method_excludes_profiles_consumers_and_runtimes(self) -> None:
        text = METHOD.read_text(encoding="utf-8")
        for forbidden in (
            "ABIogenesis",
            "ABG",
            "HoG",
            "GTL",
            "STDO_REFERENCE_FRAME_BASELINE.md",
            "Executive",
            "Worker",
            "Reviewer",
            "Application-Profile Composition Qualification",
            "Relationship To STDO",
            "Discovery Provenance",
        ):
            self.assertNotIn(forbidden, text)

    def test_profile_and_product_binding_have_distinct_owners(self) -> None:
        method = METHOD.read_text(encoding="utf-8")
        profile = PROFILE.read_text(encoding="utf-8")
        spec_method = SPEC_METHOD.read_text(encoding="utf-8")
        product = PRODUCT.read_text(encoding="utf-8")
        basis = BASIS.read_text(encoding="utf-8")

        self.assertNotIn("Project Reference-Frame Basis", method)
        self.assertIn("optional derived role and evaluation profile", profile)
        self.assertIn("does not adopt it", profile)
        self.assertIn("Product-owned accepted declaration", spec_method)
        self.assertIn("Profile availability, Product adoption", spec_method)
        self.assertIn("[`REFERENCE_FRAME_BASIS.md`](REFERENCE_FRAME_BASIS.md)", product)
        self.assertIn("# STDO Source Project Reference-Frame Basis", basis)
        self.assertIn(
            "urn:stdo:reference-frame:fundamental-invariant-conservation:v1",
            basis,
        )
        for coordinate in "QBMCI AEXRJKD".replace(" ", ""):
            self.assertIn(f"| `{coordinate}` |", basis)

    def test_project_basis_binds_exact_immutable_method_coordinates(self) -> None:
        text = BASIS.read_text(encoding="utf-8")
        for required in (
            "stdo://releases/v2.4.3-rc.3/",
            "312c84609866a4b8ea665bbbc87eb16ef3a3bb28acc234da6d081065af40d551",
            "a270453802ae03d6871c408d782094180b938aca22399ce817451fdd4551b174",
            "9a4c1d6743a7ddaab920f3323232f822f1a45dcbad5034b65b1c0859b47ba6b9",
            "50b825969ae23c5a42f7f3776fd2ab4146836349dfd4ef7a548dc2b6349b389c",
            "mutable successor standards",
            "candidate subjects, not bootstrap authority",
            "alter an immutable release",
            "urn:stdo:decision:specification-methodology:reference-frame-basis:v1",
            "direct_human_authorization_2026-08-29",
            "urn:stdo:actor:specification-methodology:codex:t-016-pen-holder",
        ):
            self.assertIn(required, text)

        definition = json.loads(DEFINITION.read_text(encoding="utf-8"))
        self.assertEqual(
            definition["reference_frame_bases"],
            [
                {
                    "uri": "./specification/REFERENCE_FRAME_BASIS.md",
                    "authority": ["./specification/PRODUCT.md"],
                    "applies_to": [
                        "urn:stdo:product-definition:specification-methodology"
                    ],
                }
            ],
        )

    def test_project_basis_dispositions_every_profile_family(self) -> None:
        text = BASIS.read_text(encoding="utf-8")
        for identity in (
            "specification-methodology:executive:v1",
            "specification-methodology:worker:v1",
            "specification-methodology:reviewer:v1",
            "fundamental-invariant-conservation:v1",
            "specialist:product:v1",
            "specialist:design:v1",
            "specialist:design-component:v1",
            "specialist:public-boundary:v1",
            "specialist:entity:v1",
            "specialist:operator:v1",
            "specialist:owner:v1",
            "specialist:effect:v1",
            "specialist:reuse-foundation:v1",
            "specialist:install:v1",
            "specialist:proof:v1",
            "test:user-acceptance:v1",
            "test:end-to-end:v1",
            "test:integration:v1",
            "test:unit:v1",
        ):
            self.assertIn(identity, text)

        for required in (
            "## Evaluation Inventory And Coverage Ledger",
            "## Activation, Results, And Conjunction",
            "## Lifecycle Triggers, Invalidation, And Revision",
            "conditionally_covered",
            "excluded_by_authority",
            "activation_refusal",
            "accept | local_repair | re_enter | reject",
        ):
            self.assertIn(required, text)

    def test_worker_mutation_requires_exact_owner_grant_and_territory(self) -> None:
        text = PROFILE.read_text(encoding="utf-8")
        self.assertIn("The Worker label grants no mutation authority", text)
        self.assertIn(
            "exact inherited owner grant names the subject and write territory", text
        )
        self.assertIn("out-of-territory mutation refuses", text)
        self.assertNotIn("no admission, publication, mutation", text)

        basis = BASIS.read_text(encoding="utf-8")
        self.assertIn(
            "at activation produces `activation_refusal` and no Worker result",
            basis,
        )
        self.assertIn("returns the closed `refused` result", basis)

    def test_reference_frame_compression_preserves_boundary(self) -> None:
        text = COMPRESSION.read_text(encoding="utf-8")
        section = text.split("## Reference Frame Engagement Compression", 1)[1].split(
            "\n## ", 1
        )[0]
        for forbidden in ("ABIogenesis", "ABG", "HoG", "GTL"):
            self.assertNotIn(forbidden, section)
        self.assertIn("Keep three owners distinct", section)
        self.assertIn("The pure method imports no consumer profile", section)
        self.assertIn("each Product owns its concrete Project Reference-Frame", section)
        self.assertIn("write territory", section)

    def test_product_binding_requires_reactivation_and_independent_review(self) -> None:
        text = BASIS.read_text(encoding="utf-8")
        self.assertIn("A repair or any material subject/basis change", text)
        self.assertIn("creates a new candidate and new", text)
        self.assertIn("author-independent capable Reviewer", text)
        self.assertIn("candidate through self-review", text)


if __name__ == "__main__":
    unittest.main()
