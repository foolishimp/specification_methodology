from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
METHOD = ROOT / "specification/standards/REFERENCE_FRAME_METHOD.md"
PROFILE = ROOT / "specification/standards/STDO_REFERENCE_FRAME_BASELINE.md"
SPEC_METHOD = ROOT / "specification/standards/SPEC_METHOD.md"
PRODUCT = ROOT / "specification/PRODUCT.md"
BASIS = ROOT / "specification/REFERENCE_FRAME_BASIS.md"
DEFINITION = ROOT / "stdo_default.json"
DECISION = (
    ROOT
    / ".ai-workspace/decisions/20260901T163724Z_stdo_rc4_source_basis_acceptance.json"
)
DECISION_SHA256 = "08cb9738b486f6478ef538bafec616e57309cfc3ff57d792b532c250b27159fb"
COMPRESSION = ROOT / "specification/standards/authority_compressions/stdo_compressed.md"
BASIS_TEMPLATE = (
    ROOT / "specification/standards/templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md"
)


def markdown_table(text: str, heading: str) -> list[dict[str, str]]:
    if text.count(heading) != 1:
        raise AssertionError(f"expected one {heading}")
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
    if any(len(row) != len(headers) for row in table):
        raise AssertionError(f"inconsistent table width under {heading}")
    if any(re.fullmatch(r":?-{3,}:?", cell) is None for cell in table[1]):
        raise AssertionError(f"malformed delimiter under {heading}")
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
) -> dict[str, str]:
    results = indexed_markdown_table(
        profile,
        "### Reviewer Result And Triage Projection",
        "Reference Frame Method result",
    )
    return results[f"`{result}`"]


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
            "They do not establish\nsemantic truth",
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
            "they do not supply semantic truth",
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
            "undeclared material relation or evaluator capability",
            by_result["`out_of_frame`"]["Finding and triage payload"],
        )
        self.assertIn(
            "refuse result consumption",
            by_result["`invalid_basis`"]["Executive consumption constraint"],
        )

    def test_reviewer_projection_executes_each_result_and_refusal_branch(self) -> None:
        profile = PROFILE.read_text(encoding="utf-8")
        cases = (
            ("satisfied", "no-finding", "`not_applicable`"),
            ("falsified", "exact findings", "mechanically mapping severity"),
            ("indeterminate", "evidence gaps", "do not consume it"),
            (
                "out_of_frame",
                "evaluated claim requires an undeclared material relation",
                "refine or reconfigure a capable activation",
            ),
            ("invalid_basis", "basis failure", "refuse result consumption"),
        )
        for result, payload_text, constraint_text in cases:
            with self.subTest(result=result):
                row = reviewer_projection(profile, result)
                self.assertIn(payload_text, row["Finding and triage payload"])
                self.assertIn(
                    constraint_text,
                    row["Executive consumption constraint"],
                )

    def test_projection_table_refuses_malformed_or_duplicate_structure(self) -> None:
        profile = PROFILE.read_text(encoding="utf-8")
        heading = "### Reviewer Result And Triage Projection"
        rows = markdown_table(profile, heading)
        duplicate = "| " + " | ".join(rows[0].values()) + " |"
        mutated = profile.replace(
            "\n\nAn adjacent observation outside the evaluated claim",
            f"\n{duplicate}\n\nAn adjacent observation outside the evaluated claim",
            1,
        )
        with self.assertRaisesRegex(AssertionError, "duplicate"):
            indexed_markdown_table(
                mutated,
                heading,
                "Reference Frame Method result",
            )
        with self.assertRaisesRegex(AssertionError, "malformed delimiter"):
            table_start = (
                "| Reference Frame Method result | Finding and triage payload | "
                "Executive consumption constraint |\n|---|---|---|"
            )
            markdown_table(
                profile.replace(table_start, table_start.replace("|---", "| x "), 1),
                heading,
            )
        with self.assertRaisesRegex(AssertionError, "expected one"):
            markdown_table(f"{profile}\n\n{heading}\n", heading)

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
            "stdo://releases/v2.5.0-rc.4/",
            "4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e",
            "032dac0c833111547f7dd4b290c5316ed9b70f97",
            "7a25668a8fecfd26f895759af3bec4708727964a",
            "737af9a7a2779dbf59e7c81232e7efd4dd98692a",
            "a9565f923213759984f936d087cd7cebd0f44a74",
            "d6642edac9fb509a68b2ffc81d3404f2360b34e4",
            "504db879867f60e46ed4dea60509d12056d10cdd8c3460dc94abf7bc56542656",
            "80a66946d4767b1ff857aad4bbaba696b591cd7e7529324c2ece8ced9754ced5",
            "c7f7abfa620d73e209463605517075ac375d8e79e0273d3f435c4e36155de5d8",
            "6013e42693066127d729580ac3d01d31c2a82f00adea9d0fb1af3494b4ad9c3e",
            "Mutable successor standards",
            "candidate subjects, not bootstrap authority",
            "alter an\nimmutable release",
            "urn:stdo:decision:specification-methodology:reference-frame-basis:v2",
            "20260901T163724Z_stdo_rc4_source_basis_acceptance.json",
            "urn:openai:codex:delegated-rc4-source-adoption",
        ):
            self.assertIn(required, text)
        self.assertNotIn("stdo://releases/v2.4.3-rc.3/", text)

        definition = json.loads(DEFINITION.read_text(encoding="utf-8"))
        self.assertEqual(
            definition["reference_frame_bases"],
            [
                {
                    "uri": "./specification/REFERENCE_FRAME_BASIS.md",
                    "authority": [
                        "./specification/PRODUCT.md#reference-frame-engagement",
                        "./.ai-workspace/decisions/20260901T163724Z_stdo_rc4_source_basis_acceptance.json",
                    ],
                    "applies_to": [
                        "urn:stdo:product-definition:specification-methodology"
                    ],
                }
            ],
        )
        decision = json.loads(DECISION.read_text(encoding="utf-8"))
        self.assertEqual(
            hashlib.sha256(DECISION.read_bytes()).hexdigest(), DECISION_SHA256
        )
        self.assertEqual(
            decision["subject_sha256"],
            "sha256:" + hashlib.sha256(BASIS.read_bytes()).hexdigest(),
        )
        self.assertEqual(
            decision["adoption_plan"]["plan_sha256"],
            "sha256:bb38e6b613730ec2073f0b2072c054860c846d35c1cadcfc806bbefd1a38d6b4",
        )
        self.assertEqual(
            decision["decision_id"],
            "urn:stdo:decision:specification-methodology:reference-frame-basis:v2",
        )
        self.assertEqual(decision["change_class"], "product_reprice")
        self.assertEqual(decision["proxy_grant"]["delegation_rights"], "none")
        self.assertEqual(
            decision["proxy_grant"]["validity"]["current_status"],
            "exhausted-by-completed-decision-and-adoption",
        )
        self.assertEqual(
            decision["proxy_grant"]["revocation"]["status"],
            "not-revoked-before-completion",
        )
        operation_grant = decision["operation_grant"]
        self.assertEqual(
            operation_grant["operation"],
            {
                "kind": "stdo.product-definition.adopt",
                "definition_ref": "./stdo_default.json",
                "accepted_plan_sha256": decision["adoption_plan"]["plan_sha256"],
                "tool_basis": "stdo://releases/v2.5.0-rc.4/",
            },
        )
        self.assertEqual(
            operation_grant["mutation_subject"],
            {
                "definition_id": "urn:stdo:product-definition:specification-methodology",
                "preimage_sha256": decision["adoption_plan"]["definition_sha256"],
                "postimage_sha256": "sha256:c8c84cc29516b3c541e59a1643d63b93f45bd6d3a9a7050aedbaa806a9293f96",
            },
        )
        write_territory = operation_grant["write_territory"]
        self.assertEqual(write_territory, ["/$schema", "/constitution/stdo/basis"])
        self.assertEqual(
            set(operation_grant["permitted_effects"]), set(write_territory)
        )
        for forbidden_pointer in (
            "/constitution/stdo/selector",
            "/reference_frame_bases",
            "/what",
            "/how",
        ):
            self.assertNotIn(forbidden_pointer, write_territory)
            self.assertNotIn(forbidden_pointer, operation_grant["permitted_effects"])
        self.assertIn(
            "all-paths-outside-the-exact-write-territory",
            operation_grant["excluded_effects"],
        )
        self.assertEqual(operation_grant["delegation_rights"], "none")
        self.assertEqual(
            operation_grant["validity"]["current_status"],
            "exhausted-by-exact-postimage",
        )
        self.assertIn(
            "stop-after-the-first-exact-atomic-postimage",
            operation_grant["stop_conditions"],
        )
        self.assertTrue(decision["self_expansion_prohibited"])
        self.assertFalse(decision["human_exact_byte_inspection_claimed"])

    def test_project_basis_dispositions_every_profile_family(self) -> None:
        text = BASIS.read_text(encoding="utf-8")
        for identity in (
            "specification-methodology:executive:v1",
            "specification-methodology:worker:v1",
            "specification-methodology:reviewer:v1",
            "fundamental-invariant-conservation:v1",
            "specialist:product:v1",
            "specialist:product-composition:v1",
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
            "All twelve baseline families",
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
        self.assertIn("STDO_REFERENCE_FRAME_BASELINE.md#derived-worker-frame", basis)
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
