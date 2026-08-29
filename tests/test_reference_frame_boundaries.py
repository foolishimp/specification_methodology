from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
METHOD = ROOT / "specification/standards/REFERENCE_FRAME_METHOD.md"
PROFILE = ROOT / "specification/standards/STDO_REFERENCE_FRAME_BASELINE.md"
SPEC_METHOD = ROOT / "specification/standards/SPEC_METHOD.md"
PRODUCT = ROOT / "specification/PRODUCT.md"
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

        self.assertNotIn("Project Reference-Frame Basis", method)
        self.assertIn("optional derived role and evaluation profile", profile)
        self.assertIn("does not adopt it", profile)
        self.assertIn("Product-owned accepted declaration", spec_method)
        self.assertIn("Profile availability, Product adoption", spec_method)
        self.assertIn("### Fundamental Invariant Conservation Frame", product)
        self.assertIn(
            "urn:stdo:reference-frame:fundamental-invariant-conservation:v1",
            product,
        )
        for coordinate in "QBMCI AEXRJKD".replace(" ", ""):
            self.assertIn(f"| `{coordinate}` |", product)

    def test_worker_mutation_requires_exact_owner_grant_and_territory(self) -> None:
        text = PROFILE.read_text(encoding="utf-8")
        self.assertIn("The Worker label grants no mutation authority", text)
        self.assertIn(
            "exact inherited owner grant names the subject and write territory", text
        )
        self.assertIn("out-of-territory mutation refuses", text)
        self.assertNotIn("no admission, publication, mutation", text)

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
        text = PRODUCT.read_text(encoding="utf-8")
        self.assertIn("A changed basis or subject", text)
        self.assertIn("creates a new activation", text)
        self.assertIn("author-independent capable Reviewer", text)
        self.assertIn("cannot qualify its own", text)
        self.assertIn("invariant-affecting candidate", text)


if __name__ == "__main__":
    unittest.main()
