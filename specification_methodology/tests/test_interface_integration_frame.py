"""Mechanical source-contract checks, not semantic review or executed LLM UAT.

Cases inspect the owning declaration, routes and qualification distinctions.
They neither classify real interactions nor manufacture frame verdicts.
"""
from __future__ import annotations

import re
import unittest

from test_reference_frame_boundaries import (
    BOOTSTRAP,
    COMPRESSION,
    PROFILE,
    indexed_markdown_table,
)


HEADING = "## Derived End-To-End Interface Integration Frame"
CLAIMS = "### Interface Integration Claim Boundaries"
CASES = "### Interface Integration Qualification"
ROUTE = "STDO_REFERENCE_FRAME_BASELINE.md#derived-end-to-end-interface-integration-frame"


def section(text: str) -> str:
    if text.count(HEADING) != 1:
        raise AssertionError("expected one interface integration frame")
    return text.split(HEADING, 1)[1].split("\n## ", 1)[0]


class InterfaceIntegrationFrameSourceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.profile = PROFILE.read_text(encoding="utf-8")
        self.frame = section(self.profile)
        self.normalized = " ".join(self.frame.split())

    def test_complete_source_linked_declaration_and_local_routes(self) -> None:
        self.assertIn(
            "urn:stdo:reference-frame:end-to-end-interface-integration:v1",
            self.frame,
        )
        self.assertIn("exact selected baseline basis", self.frame)
        declaration = indexed_markdown_table(self.profile, HEADING, "Frame element")
        self.assertEqual(
            set(declaration),
            {
                "evaluation family", "subject and basis", "material manifold",
                "coordinates and equality", "governing invariants", "authority",
                "evidence", "capability envelope", "exclusions",
                "result and relations", "invalidation", "qualification",
            },
        )
        for result in (
            "satisfied", "falsified", "indeterminate", "out_of_frame", "invalid_basis"
        ):
            self.assertIn(f"`{result}`", declaration["result and relations"]["Derived application"])
        # Resolve every local heading route rather than treating link spelling as proof.
        headings = {
            re.sub(r"[^\w\s-]", "", match.lower()).replace(" ", "-")
            for match in re.findall(r"^#{1,6} (.+)$", self.profile, re.MULTILINE)
        }
        for anchor in re.findall(r"\]\(#([^)]*)\)", self.frame):
            self.assertIn(anchor, headings, anchor)
        self.assertEqual(
            len(re.findall(r"\]\(#([^)]*)\)", self.frame)), 7
        )
        for path in (COMPRESSION, BOOTSTRAP):
            self.assertIn(ROUTE, path.read_text(encoding="utf-8"))

    def test_four_claims_and_evidence_altitudes_stay_distinct(self) -> None:
        declaration = indexed_markdown_table(self.profile, HEADING, "Frame element")
        self.assertIn(
            "declared participant roles, functional path, dependencies, configuration and capabilities for design",
            declaration["subject and basis"]["Derived application"],
        )
        self.assertIn(
            "design relations and explicitly unresolved realization facts for design claims",
            declaration["evidence"]["Derived application"],
        )
        rows = indexed_markdown_table(self.profile, CLAIMS, "Claim")
        self.assertEqual(list(rows), [
            "Contract sufficiency", "Boundary congruence",
            "Path realization", "User usability",
        ])
        for claim, discriminator in (
            ("Contract sufficiency", "without an implemented runtime"),
            ("Boundary congruence", "Acquire both sides and their exchanges"),
            ("Path realization", "exact runnable subject"),
            ("User usability", "only its declared context, access"),
        ):
            self.assertIn(discriminator, rows[claim]["Evaluation and evidence boundary"])
        for condition in (
            "scope reason for unselected claims",
            "Design-only work does not require unavailable runtime evidence",
            "An unknown material condition keeps its dependent claim unresolved",
            "requires all four distinct results and their explicit conjunction",
            "Transport, parse, admission, semantic satisfaction, operation completion and user success are not interchangeable",
        ):
            self.assertIn(condition, self.normalized)

    def test_contract_context_time_cause_and_authority_are_not_shape_checks(self) -> None:
        for condition in (
            "producer success postconditions, consumer preconditions",
            "candidate output, later admission and semantic assessment remain distinct",
            "normal model refusal or inadmissible candidate does not by itself falsify",
            "an exact locator the actor can lawfully resolve",
            "Generic governance access does not replace the Product-specific contract",
            "reuse or proven equivalent projections",
            "accepted loss, provenance, governing owner and refusal conditions",
            "active input from historical context",
            "relevant current mutable workspace for each later operation",
            "unaffected accepted work remains reusable",
            "not merely the first log or clock occurrence",
            "joint causes, alternative frontiers and indeterminacy",
            "Product redaction rules",
            "diagnosis grants no repair or retry",
            "Computed facts, contextual judgments and reserved owner rulings retain their distinct owners",
        ):
            with self.subTest(condition=condition):
                self.assertIn(condition, self.normalized)

    def test_live_claims_and_proportionality_keep_honest_evidence_scope(self) -> None:
        for condition in (
            "clean-room LLM UAT with the ordinary supplied context and permitted tools",
            "Expected outcomes precede response inspection",
            "sunny case and ordinary ambiguity/negative cases material to the claim",
            "not live-provider usability",
            "Do not edit responses or silently retry until green",
            "not a new universal live-provider requirement during design",
            "no exhaustive-hardening prerequisite, scenario quota, controller",
            "not acceptance or a next-action grant",
        ):
            with self.subTest(condition=condition):
                self.assertIn(condition, self.normalized)
        for forbidden in ("ABIogenesis", "ABG", "HoG", "GTL", "predecessorStatementRefs"):
            self.assertNotIn(forbidden, self.frame)

    def test_qualification_preserves_each_named_counterexample_distinction(self) -> None:
        rows = indexed_markdown_table(self.profile, CASES, "Case")
        expected = {
            "Empty and nonempty eligible domains": "universal empty-value workaround",
            "Adequate candidate contract and rejected response": "model variability alone is not frame failure",
            "Same-response or historical-only reference": "not automatically current admissible inputs",
            "Individually valid but temporally mismatched carriers": "despite matching shapes",
            "Meaning-changing translation": "even when both shapes validate",
            "Fixture knows a hidden rule": "user usability unproved",
            "Expected output through a forbidden path": "Path realization is falsified",
            "Changed workspace and reusable accepted work": "preserving unaffected valid work",
            "Wrapped or ambiguous failure": "invented unique cause",
            "Design-only sufficient contract": "no runtime/UAT satisfaction is inferred",
        }
        self.assertEqual(set(rows), set(expected))
        for name, distinction in expected.items():
            with self.subTest(case=name):
                self.assertIn(distinction, rows[name]["Required discrimination"])
        self.assertIn("not an executed trial", self.normalized)

    def test_source_parser_rejects_duplicate_or_missing_claim_structure(self) -> None:
        rows = indexed_markdown_table(self.profile, CLAIMS, "Claim")
        first = rows["Contract sufficiency"]
        duplicate = "| " + " | ".join(first.values()) + " |"
        mutated = self.profile.replace(
            "\n\nThe activation selects claims from the work's applicability",
            f"\n{duplicate}\n\nThe activation selects claims from the work's applicability",
            1,
        )
        with self.assertRaisesRegex(AssertionError, "duplicate"):
            indexed_markdown_table(mutated, CLAIMS, "Claim")
        with self.assertRaisesRegex(AssertionError, "expected one"):
            section(self.profile.replace(HEADING, "## Removed frame", 1))


if __name__ == "__main__":
    unittest.main()
