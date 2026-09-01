from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STACK_ROOT = ROOT.parent
PLUGIN = ROOT / "plugins" / "spec"
WORKFLOW_SKILLS = {
    "stdo-help",
    "stdo-review",
    "stdo-status",
    "stdo-ticket",
    "stdo-work",
}


def frontmatter(path: Path) -> dict[str, str | bool]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(?P<body>.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise AssertionError(f"missing frontmatter: {path}")
    values: dict[str, str | bool] = {}
    for line in match.group("body").splitlines():
        key, separator, value = line.partition(":")
        if not separator:
            continue
        normalized = value.strip().strip('"')
        values[key.strip()] = (
            normalized == "true" if normalized in {"true", "false"} else normalized
        )
    return values


def skill_names(root: Path) -> set[str]:
    return {path.parent.name for path in root.glob("*/SKILL.md")}


class PluginDistributionTests(unittest.TestCase):
    def test_hosts_share_five_workflows_and_claude_refresh_is_explicit(self) -> None:
        claude = json.loads(
            (PLUGIN / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
        )
        codex = json.loads(
            (PLUGIN / ".codex-plugin/plugin.json").read_text(encoding="utf-8")
        )

        self.assertEqual(skill_names(PLUGIN / "skills"), WORKFLOW_SKILLS)
        self.assertEqual(skill_names(PLUGIN / "claude-skills"), {"refresh"})
        self.assertEqual(
            {Path(path).name for path in claude["skills"]},
            {"refresh"},
        )
        self.assertEqual(codex["skills"], "./skills/")
        self.assertEqual(claude["name"], codex["name"])
        self.assertEqual(claude["version"], codex["version"])
        self.assertEqual(claude["version"], "2.5.0-rc.3")

    def test_workflow_metadata_has_positive_and_negative_trigger_bounds(self) -> None:
        for name in sorted(WORKFLOW_SKILLS):
            with self.subTest(skill=name):
                skill = PLUGIN / "skills" / name / "SKILL.md"
                values = frontmatter(skill)
                metadata = json.loads(
                    (PLUGIN / "skills" / name / "agents/openai.yaml").read_text(
                        encoding="utf-8"
                    )
                )

                self.assertEqual(values.get("name"), name)
                self.assertIn(name.replace("-", " "), str(values["description"]))
                self.assertIn("STDO", str(values["description"]))
                self.assertIn("Do not invoke", str(values["description"]))
                self.assertTrue(metadata["policy"]["allow_implicit_invocation"])
                self.assertIn(f"$spec:{name}", metadata["interface"]["default_prompt"])

    def test_claude_refresh_is_manual_only_and_uses_packaged_procedure(self) -> None:
        claude = frontmatter(PLUGIN / "claude-skills/refresh/SKILL.md")
        procedure = (PLUGIN / "references/REFRESH.md").read_text(encoding="utf-8")

        self.assertIs(claude["disable-model-invocation"], True)
        self.assertIn(
            "references/REFRESH.md",
            (PLUGIN / "claude-skills/refresh/SKILL.md").read_text(),
        )
        self.assertIn("product-local cut", procedure)
        self.assertIn("project-qualified", procedure)

    def test_workflow_skills_preserve_effect_and_role_boundaries(self) -> None:
        help_text = (PLUGIN / "skills/stdo-help/SKILL.md").read_text()
        ticket_text = (PLUGIN / "skills/stdo-ticket/SKILL.md").read_text()
        work_text = (PLUGIN / "skills/stdo-work/SKILL.md").read_text()
        review_text = (PLUGIN / "skills/stdo-review/SKILL.md").read_text()
        status_text = (PLUGIN / "skills/stdo-status/SKILL.md").read_text()
        ticket_normalized = " ".join(ticket_text.split())
        work_normalized = " ".join(work_text.split())

        self.assertIn(
            "Start read-only", (PLUGIN / "references/GETTING_STARTED.md").read_text()
        )
        self.assertIn("installation is authorized", help_text)
        self.assertIn("stop without writing", ticket_text)
        for field in (
            "`id`",
            "`title`",
            "`ticket_category`",
            "`goal`",
            "`triaged_at`",
            "`created_at`",
            "`updated_at`",
        ):
            self.assertIn(field, ticket_text)
        self.assertIn("target_truth", ticket_text)
        self.assertIn("Do not create a ticket merely", ticket_normalized)
        self.assertIn("execution-contract state as `drafted`", ticket_text)
        self.assertIn("Ticket creation, lane placement", ticket_text)
        self.assertIn("supersede or withdraw", work_text)
        self.assertIn("Do not invoke `stdo-ticket` automatically", work_text)
        ordered_carriers = (
            "reuse an exact admitted durable ticket",
            "otherwise require one authorized durable ticket",
            "otherwise use the admitted sprint",
            "otherwise use an intake draft",
        )
        positions = [work_normalized.index(claim) for claim in ordered_carriers]
        self.assertEqual(positions, sorted(positions))
        self.assertIn(
            "Drafting, admission, and\n   execution may occur in the same invocation",
            work_text,
        )
        self.assertIn("Continue only after deterministic admission", work_normalized)
        self.assertIn(
            "Product-bound admitting mechanism and authority", work_normalized
        )
        self.assertIn("exact contract identity or digest", work_normalized)
        self.assertIn("Product-bound durable result/evidence surface", work_normalized)
        self.assertIn(
            "conversation return alone is not durable evidence", work_normalized
        )
        self.assertIn(
            "do not claim closure or create a ticket without authority",
            work_normalized,
        )
        self.assertIn(
            "only when the current exact grant already includes ticket-state mutation",
            work_normalized,
        )
        self.assertIn(
            "an explicit `stdo-ticket` route without invoking it",
            work_normalized,
        )
        self.assertIn("mark closure withheld", work_normalized)
        self.assertIn("Return the exact candidate and stop", work_text)
        self.assertIn("separately activates `stdo-review`", work_text)
        self.assertIn("qualification", work_text)
        self.assertIn("Review is read-only", review_text)
        self.assertIn("does not\nrepair", review_text)
        self.assertIn("exact affected Product claims", review_text)
        self.assertIn("Reviewer capability\n   envelope", review_text)
        self.assertIn("STDO engagement-profile technical-triage fields", review_text)
        self.assertIn("Product-selected severity scale", review_text)
        self.assertIn("Do not create\n   tickets", status_text)
        self.assertIn("Product-owned", status_text)

    def test_guide_is_packaged_and_distinguishes_method_and_plugin_cuts(self) -> None:
        guide = (PLUGIN / "references/GETTING_STARTED.md").read_text(encoding="utf-8")

        for heading in (
            "## 1. Get Ready To Work",
            "## 2. Iterate Requirements",
            "## 3. Start Code Development And Testing",
            "## 4. Monitor And Help Triage",
        ):
            self.assertIn(heading, guide)
        for name in WORKFLOW_SKILLS:
            self.assertIn(f"`{name}`", guide)
            self.assertIn(f"`{name.replace('-', ' ')}`", guide)
        self.assertIn("STDO_CUT='v2.5.0-rc.3'", guide)
        self.assertIn("STDO_REF='specification_methodology/v2.5.0-rc.3'", guide)
        self.assertIn("SPEC_PLUGIN_REF=", guide)
        self.assertIn("plugin version and immutable repository cut are aligned", guide)
        self.assertIn("spec@specification_stack", guide)
        self.assertIn("stabilize one exact review subject", guide)
        self.assertIn("where generic-method qualification requires it", guide)
        for field in (
            "`id`",
            "`title`",
            "`ticket_category`",
            "`goal`",
            "`triaged_at`",
            "`created_at`",
            "`updated_at`",
        ):
            self.assertIn(field, guide)
        for name in WORKFLOW_SKILLS:
            self.assertIn(f"$spec:{name}", guide)
        self.assertIn("#subdirectory=specification_methodology", guide)
        self.assertIn("`RELEASE_METHOD.md`", guide)
        self.assertIn(
            "plugins/spec/references/GETTING_STARTED.md",
            (ROOT / "README.md").read_text(),
        )
        self.assertIn(
            "plugins/spec/references/GETTING_STARTED.md",
            (ROOT / "QUICKSTART.md").read_text(),
        )

    def test_root_and_local_marketplaces_use_one_selector(self) -> None:
        root_marketplace = json.loads(
            (STACK_ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8")
        )
        local_marketplace = json.loads(
            (ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8")
        )

        self.assertEqual(root_marketplace["name"], "specification_stack")
        self.assertEqual(local_marketplace["name"], root_marketplace["name"])
        self.assertTrue(root_marketplace["description"])
        self.assertTrue(local_marketplace["description"])
        self.assertNotIn("1 command", json.dumps(local_marketplace))

    def test_quickstart_uses_rc3_coordinates_and_atomic_setup_route(self) -> None:
        quickstart = (ROOT / "QUICKSTART.md").read_text(encoding="utf-8")

        self.assertIn("specification_methodology/v2.5.0-rc.3", quickstart)
        self.assertIn("#subdirectory=specification_methodology", quickstart)
        self.assertIn("stdo-toolchain 0.1.2", quickstart)
        self.assertIn("Do not copy either target separately", quickstart)
        self.assertIn(
            "plugins/spec/references/GETTING_STARTED.md#new-project", quickstart
        )
        self.assertNotIn('target.open("xb")', quickstart)
        self.assertNotIn("Advance `v<version>`", quickstart)


if __name__ == "__main__":
    unittest.main()
