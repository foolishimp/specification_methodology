from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STANDARD = ROOT / "specification/standards/AXIOMATIC_CALCULUS.md"
PRODUCT = ROOT / "specification/PRODUCT.md"
COMPRESSION = (
    ROOT
    / "specification/standards/authority_compressions/axiomatic_calculus.compressed.md"
)


def record_body(text: str, name: str) -> str:
    match = re.search(
        rf"^{re.escape(name)} = \{{\n(.*?)^\}}$", text, re.MULTILINE | re.DOTALL
    )
    if match is None:
        raise AssertionError(f"missing record {name}")
    return match.group(1)


class AxiomaticCalculusTests(unittest.TestCase):
    def test_calculus_declares_closed_carrier_neutral_kernel(self) -> None:
        text = STANDARD.read_text(encoding="utf-8")
        for declaration in (
            "# The STDO Axiomatic Calculus for Governed Symbolic Systems",
            "urn:stdo:concept:axiomatic-calculus:a-c",
            "urn:stdo:bounded-context:axiomatic-calculus",
            "Sigma = (",
            "ResidualKind,",
            "M_b = (b, I, O, E, C, L, X)",
            "### AC-001 Closed Signature",
            "### AC-019 Valid Model",
            "a_c       = the pure calculus",
            "a_c.X     = subject X interpreted as a model of a_c",
            "a_c.X.C   = that accepted model encoded in carrier C",
        ):
            self.assertIn(declaration, text)
        for non_claim in (
            "universal applicability",
            "logical completeness",
            "consistency",
            "decidability",
            "soundness",
            "category-theoretic status",
        ):
            self.assertIn(non_claim, text)

    def test_functor_kinds_are_exact_and_vector_qualified(self) -> None:
        text = STANDARD.read_text(encoding="utf-8")
        for identity in (
            "F_D = urn:stdo:concept:axiomatic-calculus:f-d",
            "F_P = urn:stdo:concept:axiomatic-calculus:f-p",
            "F_H = urn:stdo:concept:axiomatic-calculus:f-h",
            "F_K[v](X_v) -> Y_v | Omega_v",
        ):
            self.assertIn(identity, text)
        self.assertIsNone(re.search(r"\bF_[DPH]\s*\(", text))

    def test_admission_is_a_judgment_over_unchanged_carrier(self) -> None:
        text = STANDARD.read_text(encoding="utf-8")
        self.assertIn(
            "D_C = F_D[v_carrier_admission](G_C, Profile_C, CarrierBasis_C)",
            text,
        )
        self.assertIn("`D_C` is a judgment over unchanged carrier bytes", text)
        self.assertNotRegex(
            text,
            r"F_D\[v_carrier_admission\]\([^)]*\)\s*->\s*G_C",
        )
        self.assertIn("It is not embedded in `id(a_c.X)`", text)
        self.assertIn(
            "is not embedded in `id(a_c.X.C)`",
            text,
        )
        self.assertNotIn("+ semantic acceptance identity", text)
        self.assertNotIn("+ carrier admission judgment identity", text)
        self.assertIn("derivation_basis", text)
        self.assertIn("publication_basis", text)
        self.assertIn("distinct immutable successor carrier", text)
        self.assertIn("a_c.X + exact accepted semantic judgment J_X", text)
        self.assertNotIn("a_c.X + exact carrier C", text)
        self.assertNotIn("same-release semantic addresses", text)

    def test_fundamental_records_carry_direct_coordinates(self) -> None:
        text = STANDARD.read_text(encoding="utf-8")
        for name in (
            "SemanticObject",
            "TypedRelation",
            "Constraint",
            "Latitude",
            "Residual",
            "Judgment",
            "v",
            "t",
        ):
            body = record_body(text, name)
            for coordinate in ("context", "owner", "scope", "basis"):
                self.assertRegex(body, rf"\b{coordinate}\b", f"{name}.{coordinate}")
        self.assertRegex(record_body(text, "Constraint"), r"\bjudgment_kind\b")
        self.assertRegex(record_body(text, "t"), r"\bpreservation_relation\b")

    def test_calculus_has_no_application_or_runtime_binding(self) -> None:
        for path in (STANDARD, COMPRESSION):
            text = path.read_text(encoding="utf-8")
            for forbidden in (
                "ABIogenesis",
                "ABG",
                "HoG",
                "graph-native-odd",
                "ODD_METHOD.md",
                "## STDO Application",
                "a_c.STDO",
                "a_c.STDO.GTL",
                "Encode_GTL",
            ):
                self.assertNotIn(forbidden, text, f"{path.name}: {forbidden}")

    def test_stdo_product_keeps_the_three_layers_distinct(self) -> None:
        text = PRODUCT.read_text(encoding="utf-8")
        self.assertIn("## Axiomatic Calculus Boundary", text)
        self.assertIn("STDO principles -> a_c", text)
        self.assertIn("a_c + exact subject X -> a_c.X", text)
        self.assertIn(
            "a_c.X + exact accepted semantic judgment J_X -> accepted a_c.X", text
        )
        self.assertIn("accepted a_c.X + exact carrier C -> a_c.X.C", text)
        self.assertIn("distinct governed layers", text)
        self.assertIn("not automatically independently released", text)


if __name__ == "__main__":
    unittest.main()
