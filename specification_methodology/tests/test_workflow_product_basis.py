from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "spec"
BASIS_REFERENCE = PLUGIN / "references" / "PRODUCT_BASIS.md"
WORKFLOW_SKILLS = (
    "stdo-help",
    "stdo-review",
    "stdo-status",
    "stdo-ticket",
    "stdo-work",
)


def normalized(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


class WorkflowProductBasisTests(unittest.TestCase):
    def test_shared_reference_selects_one_scope_bound_verified_basis(self) -> None:
        text = normalized(BASIS_REFERENCE)
        ordered_claims = (
            "State the requested Product scope",
            "Discover candidate `stdo_<label>.json` definitions",
            "Determine applicability from each definition's Product-definition identity",
            "Require exactly one applicable definition",
            "Verify the selected definition read-only",
            "Return the requested Product scope, definition identity and path",
        )
        positions = [text.index(claim) for claim in ordered_claims]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("directory nesting is discovery evidence only", text)
        self.assertIn(
            "explicit composition bindings",
            text,
        )
        self.assertIn(
            "stdo status --definition <selected-definition> --verify",
            text,
        )
        for claim in (
            "Zero definitions",
            "multiple applicable definitions",
            "failed verification",
            "manifest",
            "stops the calling skill before effects",
        ):
            self.assertIn(claim, text)
        self.assertIn("Do not sync, adopt, install", text)

    def test_all_five_workflows_require_the_packaged_reference(self) -> None:
        expected_link = "../../references/PRODUCT_BASIS.md"
        for name in WORKFLOW_SKILLS:
            with self.subTest(skill=name):
                skill = PLUGIN / "skills" / name / "SKILL.md"
                text = normalized(skill)
                self.assertIn("Read and apply", text)
                self.assertIn(expected_link, text)
                self.assertIn("exactly-one verified selection", text)
                self.assertTrue((skill.parent / expected_link).resolve().is_file())

    def test_selection_does_not_widen_workflow_effects(self) -> None:
        for name in ("stdo-help", "stdo-status", "stdo-review"):
            with self.subTest(skill=name):
                self.assertIn(
                    "This skill remains read-only",
                    normalized(PLUGIN / "skills" / name / "SKILL.md"),
                )

        ticket = normalized(PLUGIN / "skills/stdo-ticket/SKILL.md")
        self.assertIn("selection grants no ticket-state authority", ticket)
        self.assertIn(
            "Confirm explicit authority to create or update ticket state", ticket
        )
        self.assertIn("stop without writing", ticket)

        work = normalized(PLUGIN / "skills/stdo-work/SKILL.md")
        self.assertIn("selection grants no work or mutation authority", work)
        self.assertIn("Establish applicable upstream work authority", work)
        self.assertIn("Continue only after deterministic admission", work)


if __name__ == "__main__":
    unittest.main()
