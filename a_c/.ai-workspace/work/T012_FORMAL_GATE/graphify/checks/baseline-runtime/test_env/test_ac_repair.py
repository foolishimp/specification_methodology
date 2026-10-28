"""Grounding-patch contract tests; all actor calls are synthetic local doubles."""
from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import shutil
import sys
import unittest
from unittest.mock import patch

TENANT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TENANT / "code"))
import ac_generate as g
import ac_graph
import ac_grounding as h
import ac_repair as repair
import test_ac_grounding as grounding_fixtures


class RepairTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = grounding_fixtures.GroundingTests(methodName="runTest")
        self.fixture.setUp()
        self.output = self.fixture.output.resolve()
        self.chunk = self.fixture.chunk
        self.clean = self.fixture.answer
        self.raw = copy.deepcopy(self.clean)
        self.raw["concepts"][0]["grounding"][0]["section_id"] = "repo://misspelled/source"
        self.original = self.fixture.actor(self.raw, failed=True).resolve()

    def tearDown(self) -> None:
        self.fixture.tearDown()

    def fix(self, family: str = "concepts", key: str = "proceed") -> dict:
        return {"decision": "patch", "patches": [{"family": family, "record_key": key, "grounding_index": 0,
                "replacement": copy.deepcopy(self.clean[family][0]["grounding"][0]), "reason": "The exact supplied rule supports the unchanged evidence prerequisite."}],
                "refusal_reason": "", "limitations": ["New evidence selection; independent semantic assessment remains open."]}

    def actor_double(self, response: dict, *, failed: bool = False, tool: bool = False):
        """Produce retained protocol artifacts without any CLI or model call."""
        def run(prompt, schema, actor, codex, timeout, expected_settings=None):
            actor.mkdir(parents=True)
            (actor / "empty-workspace").mkdir()
            (actor / "prompt.txt").write_text(prompt)
            g.save(actor / "answer.json", response)
            original = g.load(self.original / "invocation.json")
            invocation = copy.deepcopy(original)
            invocation.update(prompt_sha256=g.sha(prompt.encode()), schema_sha256=g.sha(schema.read_bytes()), cwd=str(actor / "empty-workspace"))
            command = ["/test-only/codex", "exec", "--json", "--ephemeral", "--sandbox", "read-only", "--skip-git-repo-check", "--color", "never",
                       "--output-schema", str(schema.resolve()), "--output-last-message", str((actor / "answer.json").resolve()), "--cd", str((actor / "empty-workspace").resolve())]
            for key, value in invocation["inline_overrides"].items():
                command.extend(["-c", key + "=" + json.dumps(value, ensure_ascii=False)])
            command.append("-")
            invocation["command"] = command
            g.save(actor / "invocation.json", invocation)
            usage = [{"input_tokens": 800, "output_tokens": 80}]
            events = [{"type": "item.completed", "item": {"type": "mcp_tool_call" if tool else "agent_message"}}, {"type": "turn.completed", "usage": usage[0]}]
            (actor / "events.jsonl").write_text("".join(json.dumps(value) + "\n" for value in events))
            (actor / "stderr.txt").write_text("")
            g.save(actor / "usage.json", {"usage_events": usage})
            result = {"profile": "ac.generation.actor-result/1", "status": "failed" if failed else "completed", "failures": ["process_timeout"] if failed else [],
                      "timed_out": failed, "user_config_unchanged": True, "cli_exit_code": 1 if failed else 0, "schema_errors": [], "unexpected_item_types": [],
                      "settings": expected_settings, "cli_version": original["cli_version"], "usage_events": usage,
                      "answer_sha256": g.sha((actor / "answer.json").read_bytes()), "events_sha256": g.sha((actor / "events.jsonl").read_bytes()), "stderr_sha256": g.sha((actor / "stderr.txt").read_bytes())}
            g.save(actor / "result.json", result)
            return result
        return run

    def execute(self, attempt: Path, response: dict, **options):
        fixed = g.load(self.output / "actor-settings.json")
        settings = {"settings": fixed["settings"], "cli_version": fixed["cli_version"]}
        with patch.object(g, "actor_settings", return_value=("/test-only/codex", {}, settings)), patch.object(g, "run_actor", side_effect=self.actor_double(response, **options)):
            return repair.execute(self.output, attempt)

    def test_prepare_is_model_free_expands_exact_coordinates_and_preserves_original(self) -> None:
        before = {path.name: path.read_bytes() for path in self.original.iterdir() if path.is_file()}
        attempt = repair.prepare(self.output, self.chunk["id"])
        self.assertFalse((attempt / "actor").exists())
        schema = g.load(attempt / "patch.schema.json")
        prop = schema["properties"]["patches"]["items"]["properties"]
        self.assertEqual(prop["replacement"]["properties"]["section_id"]["enum"], [value["id"] for value in self.chunk["segments"]])
        self.assertEqual(prop["record_key"]["enum"], ["proceed"])
        self.assertIn("merely related quotation", (attempt / "prompt.txt").read_text())
        for name, raw in before.items():
            self.assertEqual((self.original / name).read_bytes(), raw)

    def test_only_invalid_grounding_entries_can_change(self) -> None:
        derived, error = repair.apply_patch(self.raw, self.chunk, self.fix())
        self.assertIsNone(error)
        self.assertEqual(g.canonical(repair.meaning_payload(self.raw)), g.canonical(repair.meaning_payload(derived)))
        self.assertEqual(derived["dispositions"], self.raw["dispositions"])
        with self.assertRaisesRegex(repair.RepairError, "already strict-valid"):
            repair.apply_patch(self.raw, self.chunk, self.fix("constraints", "evidence_requirement"))
        duplicate = self.fix()
        duplicate["patches"].append(copy.deepcopy(duplicate["patches"][0]))
        with self.assertRaisesRegex(repair.RepairError, "duplicate"):
            repair.apply_patch(self.raw, self.chunk, duplicate)

    def test_outside_source_and_non_exact_replacement_refuse(self) -> None:
        bad = self.fix()
        bad["patches"][0]["replacement"]["section_id"] = "repo://outside"
        with self.assertRaisesRegex(repair.RepairError, "outside the exact"):
            repair.apply_patch(self.raw, self.chunk, bad)
        bad = self.fix()
        bad["patches"][0]["replacement"]["quote"] = "Related but absent quotation."
        with self.assertRaisesRegex(repair.RepairError, "not exact source"):
            repair.apply_patch(self.raw, self.chunk, bad)

    def test_non_grounding_changes_or_defects_are_outside_profile(self) -> None:
        bad = self.fix()
        bad["statement"] = "New statement."
        with self.assertRaisesRegex(repair.RepairError, "schema"):
            repair.apply_patch(self.raw, self.chunk, bad)
        wrong = copy.deepcopy(self.raw)
        wrong["constraints"][0]["applies_to_keys"] = ["invented"]
        with self.assertRaisesRegex(repair.RepairError, "non-grounding attachment"):
            repair.preflight(wrong, self.chunk)

    def test_complete_anchor_fix_with_other_consistency_failure_is_not_incomplete_chain(self) -> None:
        chunk = copy.deepcopy(self.chunk)
        second = {**chunk["segments"][0], "id": "repo://second/section", "text": "An unrelated source section.\n", "sha256": g.sha(b"An unrelated source section.\n")}
        chunk["segments"].append(second)
        raw = copy.deepcopy(self.raw)
        raw["dispositions"].append({"section_id": second["id"], "decision": "retained", "keys": ["proceed"], "reason": "Claims coverage but no grounded record actually retains this section."})
        with self.assertRaisesRegex(repair.RepairError, "outside invalid-grounding repair scope"):
            repair.apply_patch(raw, chunk, self.fix())

    def test_explicit_refusal_and_unsupported_statement_remain_refused(self) -> None:
        response = {"decision": "refuse", "patches": [], "refusal_reason": "The unchanged statement is not supported by this exact source.", "limitations": []}
        attempt = repair.prepare(self.output, self.chunk["id"])
        journal = self.execute(attempt, response)
        self.assertEqual(journal["status"], "refused")
        self.assertFalse((attempt / "derived-answer.json").exists())
        self.assertIsNone(repair.verify(self.output, attempt, require_complete=False)[0])
        with self.assertRaisesRegex(repair.RepairError, "explicitly refused"):
            repair.verify(self.output, attempt)

    def test_complete_repair_full_custody_and_separate_proposal(self) -> None:
        attempt = repair.prepare(self.output, self.chunk["id"])
        journal = self.execute(attempt, self.fix())
        self.assertEqual(journal["status"], "complete_patch")
        derived, verified = repair.verify(self.output, attempt)
        g.author_check(derived, self.chunk)
        self.assertEqual(verified["usage_events"], [{"input_tokens": 800, "output_tokens": 80}])
        result = repair.assemble(self.output)
        self.assertEqual(result["status"], "proposed")
        self.assertTrue((self.output / "repaired-proposal/model.json").exists())
        self.assertFalse((self.output / "grounded-proposal").exists())
        self.assertFalse((self.output / "proposal").exists())

    def test_incomplete_chain_is_repair_input_only_and_replays_to_original(self) -> None:
        # Two broken anchors, each corrected by a distinct small F_P patch.
        raw = copy.deepcopy(self.raw)
        raw["constraints"][0]["grounding"][0]["quote"] = "Paraphrased evidence prerequisite."
        shutil.rmtree(self.original)
        self.original = self.fixture.actor(raw, failed=True).resolve()
        first = repair.prepare(self.output, self.chunk["id"])
        self.assertEqual(self.execute(first, self.fix())["status"], "incomplete_patch")
        with self.assertRaisesRegex(repair.RepairError, "incomplete repair"):
            repair.verify(self.output, first)
        second = repair.prepare(self.output, self.chunk["id"], parent_repair=first)
        self.assertEqual(self.execute(second, self.fix("constraints", "evidence_requirement"))["status"], "complete_patch")
        derived, journal = repair.verify(self.output, second)
        self.assertEqual(g.canonical(repair.meaning_payload(raw)), g.canonical(repair.meaning_payload(derived)))
        self.assertEqual(len(repair.call_inventory(self.output, self.chunk["id"])), 3)
        with self.assertRaisesRegex(repair.RepairError, "ceiling exhausted"):
            repair.prepare(self.output, self.chunk["id"])
        self.assertEqual(repair.assemble(self.output)["status"], "proposed")

    def test_failed_or_incomplete_calls_share_budget_and_no_namespace_bypass(self) -> None:
        for number in (2, 3):
            (self.original.parent / f"attempt-{number:03d}").mkdir()
        with self.assertRaisesRegex(repair.RepairError, "ceiling exhausted"):
            repair.prepare(self.output, self.chunk["id"])
        # Assembly also checks the ceiling for strict-original/excluded cases.
        (self.original.parent / "attempt-004").mkdir()
        with self.assertRaisesRegex(repair.RepairError, "ceiling exceeded"):
            repair.assemble(self.output, allow_partial=True)

    def test_pending_repair_reservation_and_schema_drift_fail_closed(self) -> None:
        attempt = repair.prepare(self.output, self.chunk["id"])
        with self.assertRaisesRegex(repair.RepairError, "unfinished"):
            repair.prepare(self.output, self.chunk["id"])
        schema = g.load(attempt / "patch.schema.json")
        schema["properties"]["patches"]["items"]["properties"]["replacement"]["properties"]["section_id"]["enum"] = ["repo://outside"]
        g.save(attempt / "patch.schema.json", schema)
        with self.assertRaisesRegex(repair.RepairError, "schema changed"):
            repair.verify_request(self.output, attempt)

    def test_statement_tampering_does_not_pass_by_hash_refresh(self) -> None:
        attempt = repair.prepare(self.output, self.chunk["id"])
        self.execute(attempt, self.fix())
        derived = g.load(attempt / "derived-answer.json")
        derived["concepts"][0]["definition"] = "No evidence is required."
        g.save(attempt / "derived-answer.json", derived)
        journal = g.load(attempt / "journal.json")
        journal["derived_answer_sha256"] = g.sha((attempt / "derived-answer.json").read_bytes())
        g.save(attempt / "journal.json", journal)
        with self.assertRaisesRegex(repair.RepairError, "differs from exact patch"):
            repair.verify(self.output, attempt)
        with self.assertRaisesRegex(repair.RepairError, "differs from exact patch"):
            repair.assemble(self.output, allow_partial=True)

    def test_failed_actor_and_invalid_patch_can_only_be_excluded_explicitly(self) -> None:
        attempt = repair.prepare(self.output, self.chunk["id"])
        journal = self.execute(attempt, self.fix(), failed=True)
        self.assertEqual(journal["status"], "failed_actor")
        self.assertIsNone(repair.verify(self.output, attempt, require_complete=False)[0])
        self.assertEqual(repair.assemble(self.output, allow_partial=True)["status"], "partial_proposal")

    def test_disallowed_tool_usage_and_expanded_schema_reject_bad_output(self) -> None:
        attempt = repair.prepare(self.output, self.chunk["id"])
        journal = self.execute(attempt, self.fix(), tool=True)
        self.assertEqual(journal["status"], "invalid_patch")
        self.assertIn("disallowed tool", journal["failure"])
        self.assertIsNone(repair.verify(self.output, attempt, require_complete=False)[0])

    def test_refused_fd_journal_remains_partial_scope(self) -> None:
        self.assertEqual(h.normalize(self.output)["chunks"][0]["status"], "refused")
        result = repair.assemble(self.output, allow_partial=True)
        self.assertEqual(result["status"], "partial_proposal")
        coverage = g.load(self.output / "repaired-partial-proposal/coverage.json")
        self.assertEqual(coverage["grounding_repair"]["selections"][0]["status"], "excluded_f-d-refusal")

    def test_verified_fd_and_strict_originals_are_supported_without_fp_repair(self) -> None:
        shutil.rmtree(self.original)
        self.original = self.fixture.actor(self.clean).resolve()
        self.assertEqual(h.normalize(self.output)["chunks"][0]["status"], "validated_original")
        result = repair.assemble(self.output)
        self.assertEqual(result["status"], "proposed")
        coverage = g.load(self.output / "repaired-proposal/coverage.json")
        self.assertEqual(coverage["grounding_repair"]["selections"][0]["derivation"], "verified_f-d-grounding")
        self.assertEqual(len(repair.call_inventory(self.output, self.chunk["id"])), 1)

    @unittest.skipUnless(os.environ.get("AC_GRAPHIFY_UPSTREAM"), "set AC_GRAPHIFY_UPSTREAM for actual pinned-upstream trial")
    def test_actual_upstream_repaired_proposal_round_trip(self) -> None:
        upstream = Path(os.environ["AC_GRAPHIFY_UPSTREAM"])
        output = self.fixture.root / "graphify"
        g.prepare(self.fixture.corpus, self.fixture.manifest, output, "graphify-ac", upstream, 1000)
        g.build_discovery(output, upstream)
        self.output = output.resolve()
        self.original = self.fixture.actor(self.raw, output=output, failed=True).resolve()
        attempt = repair.prepare(self.output, self.chunk["id"])
        self.execute(attempt, self.fix())
        result = repair.assemble(self.output, upstream=upstream)
        self.assertEqual(result["upstream_trial"]["commit"], g.UPSTREAM_COMMIT)
        model = g.load(self.output / "repaired-proposal/model.json")
        graph = g.load(self.output / "repaired-proposal/graph.json")
        self.assertEqual(ac_graph.decode(ac_graph.GraphCarrier(graph)).document, model)
        self.assertEqual(model["populations"]["judgments"], [])


if __name__ == "__main__":
    unittest.main()
