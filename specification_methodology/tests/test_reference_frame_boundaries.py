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
BASIS_TEMPLATE = (
    ROOT / "specification/standards/templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md"
)


def markdown_table(text: str, heading: str) -> list[dict[str, str]]:
    section = text.split(heading, 1)[1]
    lines = section.splitlines()
    table: list[list[str]] = []
    started = False
    for line in lines:
        if line.startswith("|"):
            started = True
            table.append([cell.strip() for cell in line.strip("|").split("|")])
        elif started:
            break
    if len(table) < 3:
        raise AssertionError(f"missing table under {heading}")
    headers = table[0]
    return [dict(zip(headers, row, strict=True)) for row in table[2:]]


def indexed_markdown_table(
    text: str,
    heading: str,
    key: str,
) -> dict[str, dict[str, str]]:
    rows = markdown_table(text, heading)
    indexed = {row[key]: row for row in rows}
    if len(indexed) != len(rows):
        raise AssertionError(f"duplicate {key} under {heading}")
    return indexed


def reviewer_projection(
    profile: str,
    result: str,
    *,
    out_of_frame_cause: str | None = None,
) -> dict[str, str]:
    results = indexed_markdown_table(
        profile,
        "### Reviewer Result And Triage Projection",
        "Reference Frame Method result",
    )
    row = results[f"`{result}`"]
    if result != "out_of_frame":
        if out_of_frame_cause is not None:
            raise AssertionError("out-of-frame cause supplied for another result")
        return row
    if out_of_frame_cause is None:
        raise AssertionError("out_of_frame requires an exact cause")
    branches = indexed_markdown_table(
        profile,
        "### Reviewer Out-Of-Frame Branch Projection",
        "Out-of-frame cause",
    )
    return branches[out_of_frame_cause]


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

    def test_method_is_directly_bindable_without_a_representation(self) -> None:
        text = METHOD.read_text(encoding="utf-8")
        for required in (
            "an evaluation contract that defines the",
            "finite attention scope",
            "## Minimal Frame Activation Binding",
            "## Worked Binding: Product-Chain Drift Evaluation",
            "The binding may be expressed entirely in source-linked prose",
            "axiomatic model or other carrier",
            "coordinates and equality:",
            "configuration and time:",
            "acquisition and provenance:",
        ):
            self.assertIn(required, text)

        self.assertNotIn("conjunction:executive", text)

        self.assertIn("# Project Reference-Frame Basis", BASIS_TEMPLATE.read_text())

    def test_executive_controls_attention_evaluation_action_and_drift(self) -> None:
        text = PROFILE.read_text(encoding="utf-8")
        for required in (
            "## Executive Attention, Evaluation, And Action",
            "**attention management**",
            "**evaluation orchestration**",
            "**authorized action selection**",
            "dependency-ready activation set sufficient",
            "### Executive Drift Locks",
            "### Product-Chain Basis",
            "| **Product Composition** |",
            "does not make a Source Project immutable",
            "No lateral handoff",
        ):
            self.assertIn(required, text)

        for forbidden in ("ABIogenesis", "ABG", "HoG", "GTL"):
            self.assertNotIn(forbidden, text)

    def test_reviewer_triages_and_executive_dispositions(self) -> None:
        profile = PROFILE.read_text(encoding="utf-8")
        template = BASIS_TEMPLATE.read_text(encoding="utf-8")
        compression = COMPRESSION.read_text(encoding="utf-8")

        for required in (
            "### Technical triage, severity, priority, and boundary effect",
            "Reviewer grades severity. Executive assigns priority.",
            "This profile imposes no universal numeric scale.",
            "cause, blast radius, workaround, or repair risk",
            "Severity does not mechanically select priority or block promotion.",
            "Reviewer assigns priority, blocks promotion, directs repair",
            "current MVP or release mandate",
        ):
            self.assertIn(required, profile)

        for required in (
            "## Technical Triage And Promotion Policy",
            "Product-selected severity scale",
            "Product-selected priority scale",
            "current-boundary decision cutoff",
            "non-waivable authority, safety, integrity",
            "including a `P2` decision cutoff",
        ):
            self.assertIn(required, template)

        for required in (
            "Reviewer owns evidence-bound technical triage",
            "Executive consumes that technical triage",
            "the profile imposes no universal numeric scale",
            "Its payload projection is total",
        ):
            self.assertIn(required, compression)
        self.assertNotIn(
            "Reviewer returns only a Reference Frame Method result",
            compression,
        )

        pure_method = METHOD.read_text(encoding="utf-8")
        self.assertNotIn("Technical triage", pure_method)
        self.assertNotIn("promotion-boundary effect", pure_method)

    def test_reviewer_result_projection_is_total_and_exclusive(self) -> None:
        profile = PROFILE.read_text(encoding="utf-8")
        rows = markdown_table(profile, "### Reviewer Result And Triage Projection")
        by_result = indexed_markdown_table(
            profile,
            "### Reviewer Result And Triage Projection",
            "Reference Frame Method result",
        )
        self.assertEqual(len(rows), 5)
        self.assertEqual(
            set(by_result),
            {
                "`satisfied`",
                "`falsified`",
                "`indeterminate`",
                "`out_of_frame`",
                "`invalid_basis`",
            },
        )
        self.assertIn(
            "no-finding", by_result["`satisfied`"]["Finding and triage payload"]
        )
        self.assertIn(
            "`not_applicable`",
            by_result["`satisfied`"]["Finding and triage payload"],
        )
        self.assertIn(
            "one or more exact findings",
            by_result["`falsified`"]["Finding and triage payload"],
        )
        self.assertIn(
            "`indeterminate`",
            by_result["`indeterminate`"]["Finding and triage payload"],
        )
        self.assertIn(
            "undeclared material relation or capability",
            by_result["`out_of_frame`"]["Finding and triage payload"],
        )
        self.assertIn(
            "refuse result consumption",
            by_result["`invalid_basis`"]["Executive consumption constraint"],
        )

    def test_reviewer_projection_executes_each_result_and_refusal_branch(self) -> None:
        profile = PROFILE.read_text(encoding="utf-8")
        cases = (
            ("satisfied", None, "no-finding", "`not_applicable`"),
            ("falsified", None, "exact findings", "mechanically mapping severity"),
            ("indeterminate", None, "evidence gaps", "do not consume it"),
            (
                "out_of_frame",
                "observation outside the exact evaluated claim",
                "`not_applicable`",
                "do not create a claim-relative block",
            ),
            (
                "out_of_frame",
                "evaluated claim requires an undeclared material relation or "
                "evaluator capability",
                "same affected claim",
                "refine or reconfigure a capable activation",
            ),
            ("invalid_basis", None, "basis failure", "refuse result consumption"),
        )
        for result, cause, payload_text, constraint_text in cases:
            with self.subTest(result=result, cause=cause):
                row = reviewer_projection(
                    profile,
                    result,
                    out_of_frame_cause=cause,
                )
                self.assertIn(payload_text, row["Finding and triage payload"])
                self.assertIn(
                    constraint_text,
                    row["Executive consumption constraint"],
                )

        with self.assertRaisesRegex(AssertionError, "requires an exact cause"):
            reviewer_projection(profile, "out_of_frame")
        with self.assertRaisesRegex(AssertionError, "another result"):
            reviewer_projection(
                profile,
                "satisfied",
                out_of_frame_cause="observation outside the exact evaluated claim",
            )

    def test_projection_table_refuses_duplicate_result_rows(self) -> None:
        profile = PROFILE.read_text(encoding="utf-8")
        heading = "### Reviewer Result And Triage Projection"
        rows = markdown_table(profile, heading)
        duplicate = "| " + " | ".join(rows[0].values()) + " |"
        mutated = profile.replace(
            "\n\n### Reviewer Out-Of-Frame Branch Projection",
            f"\n{duplicate}\n\n### Reviewer Out-Of-Frame Branch Projection",
            1,
        )
        with self.assertRaisesRegex(AssertionError, "duplicate"):
            indexed_markdown_table(
                mutated,
                heading,
                "Reference Frame Method result",
            )

    def test_executive_promotion_constraints_cover_negative_cases(self) -> None:
        profile = PROFILE.read_text(encoding="utf-8")
        rows = markdown_table(
            profile,
            "### Executive Promotion Constraint Projection",
        )
        self.assertEqual(len(rows), 4)
        constraints = {
            row["Consumed condition"]: row["Required Executive constraint"]
            for row in rows
        }
        hard_stop = next(
            value for key, value in constraints.items() if "hard stop" in key
        )
        below_cutoff = next(
            value for key, value in constraints.items() if "below" in key
        )
        outside_claim = next(
            value for key, value in constraints.items() if "outside" in key
        )
        unsupported = next(
            value for key, value in constraints.items() if "unsupported" in key
        )
        self.assertIn("blocks regardless", hard_stop)
        self.assertIn("no mechanical block", below_cutoff)
        self.assertIn("do not create a claim-relative block", outside_claim)
        self.assertIn("do not rewrite Reviewer evidence", unsupported)

    def test_product_composition_and_integration_remain_distinct(self) -> None:
        text = PROFILE.read_text(encoding="utf-8")
        self.assertIn("twelve generic specialist-frame families", text)
        self.assertIn("Product Composition, Design", text)
        self.assertIn("A chain is evaluated through bounded edge activations", text)
        self.assertIn("### Derived Integration Frame", text)

        compression = COMPRESSION.read_text(encoding="utf-8")
        self.assertIn("twelve generic specialist-frame families", compression)
        self.assertIn("executable\n  Integration remains a distinct", compression)

        spec_method = SPEC_METHOD.read_text(encoding="utf-8")
        self.assertIn(
            "urn:stdo:concept:recursive-product-taxonomy:development-product",
            spec_method,
        )
        self.assertIn("role of one exact Install of a released Product", spec_method)
        self.assertNotIn("Development Product identities", spec_method)
        self.assertNotIn("Development Product identities", text)
        self.assertNotIn("Development Product identities", compression)

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
