"""Synthetic audit/anchor fixtures; no model is invoked or semantically accepted."""
from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

TENANT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TENANT / "code"))
import ac_generate as generation
import ac_graph
import ac_grounding as grounding

SOURCE = "# Rule\nA requires complete\n  evidence before proceeding.\nMissing evidence means refusal.\n"


def answer_for(chunk: dict) -> dict:
    section = chunk["segments"][0]
    ground = {"section_id": section["id"], "start_line": 2, "end_line": 3,
              "quote": "A requires complete\n  evidence before proceeding."}
    return {"concepts": [{"key": "proceed", "label": "Proceed", "definition": "Proceeding requires complete evidence.",
                           "conditions": ["Complete evidence exists."], "exceptions": [], "grounding": [copy.deepcopy(ground)]}],
            "relations": [], "constraints": [{"key": "evidence_requirement", "applies_to_keys": ["proceed"],
                "statement": "Complete evidence is required; missing evidence means refusal.", "conditions": ["An action is considered."], "exceptions": [], "uncertainty": "",
                "grounding": [copy.deepcopy(ground)]}], "latitude": [], "residuals": [],
            "dispositions": [{"section_id": section["id"], "decision": "retained", "keys": ["proceed", "evidence_requirement"], "reason": "Retains the evidence prerequisite and refusal."}],
            "limitations": ["No semantic acceptance or operation execution."]}


def section(text: str) -> dict:
    return {"id": "repo://test/section", "path": "test.md", "text": text,
            "start_line": 10, "end_line": 10 + len(text.splitlines()) - 1, "sha256": generation.sha(text.encode())}


def misplaced(quote: str) -> dict:
    return {"section_id": "repo://test/section", "start_line": 500, "end_line": 500, "quote": quote}


class GroundingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.corpus = self.root / "source"
        self.corpus.mkdir()
        (self.corpus / "rules.md").write_text(SOURCE)
        self.manifest = self.root / "manifest.json"
        generation.save(self.manifest, {"subject_id": "repo://test/source/", "files": [{"path": "rules.md", "sha256": generation.sha(SOURCE.encode())}]})
        self.output = self.root / "run"
        self.plan = generation.prepare(self.corpus, self.manifest, self.output, "direct", None, 1000)
        self.chunk = generation.load(self.output / "chunks.json")[0]
        self.answer = answer_for(self.chunk)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def actor(self, answer: dict, *, output: Path | None = None, failed: bool = False, tool_violation: bool = False) -> Path:
        output = output or self.output
        plan, chunks = generation.checkpoint(output)
        chunk = chunks[0]
        attempt = output / "actors/author" / chunk["id"] / "attempt-001"
        attempt.mkdir(parents=True)
        (attempt / "empty-workspace").mkdir()
        generation.save(attempt / "answer.json", answer)
        prompt = generation.author_prompt(plan, chunk, output)
        (attempt / "prompt.txt").write_text(prompt)
        settings = {"model": "test-model", "model_reasoning_effort": "high"}
        version = "codex-cli synthetic-test-only"
        generation.save(output / "actor-settings.json", {"settings": settings, "cli_version": version})
        overrides = {**settings, "features.shell_tool": False, "features.apps": False, "features.multi_agent": False,
                     "features.memories": False, "features.js_repl": False, "web_search": "disabled", "project_doc_max_bytes": 0}
        schema = generation.ASSETS / "author.schema.json"
        command = ["/test-only/codex", "exec", "--json", "--ephemeral", "--sandbox", "read-only", "--skip-git-repo-check", "--color", "never",
                   "--output-schema", str(schema.resolve()), "--output-last-message", str((attempt / "answer.json").resolve()), "--cd", str((attempt / "empty-workspace").resolve())]
        for key, value in overrides.items():
            command.extend(["-c", key + "=" + json.dumps(value, ensure_ascii=False)])
        command.append("-")
        invocation = {"profile": "ac.generation.actor-invocation/1", "settings": settings, "cli_version": version,
                      "schema_sha256": generation.sha(schema.read_bytes()), "prompt_sha256": generation.sha(prompt.encode()),
                      "inline_overrides": overrides, "effective_mcp_inventory": [], "command": command, "cwd": str(attempt / "empty-workspace"),
                      "config_path": "/test-only/config.toml", "config_sha256": "f" * 64}
        generation.save(attempt / "invocation.json", invocation)
        usage = [{"input_tokens": 123, "output_tokens": 456}]
        events = [{"type": "item.completed", "item": {"type": "mcp_tool_call" if tool_violation else "agent_message"}}, {"type": "turn.completed", "usage": usage[0]}]
        (attempt / "events.jsonl").write_text("".join(json.dumps(event) + "\n" for event in events))
        (attempt / "stderr.txt").write_text("")
        generation.save(attempt / "usage.json", {"usage_events": usage})
        validation_error = None
        try:
            generation.author_check(answer, chunk)
        except generation.GenerationError as exc:
            validation_error = str(exc)
        result = {"profile": "ac.generation.actor-result/1", "status": "failed" if failed else "completed", "failures": ["source_or_semantic_fragment_validation"] if failed else [],
                  "validation_error": validation_error if failed else None,
                  "cli_exit_code": 0, "timed_out": False, "user_config_unchanged": True, "schema_errors": [], "unexpected_item_types": [],
                  "answer_sha256": generation.sha((attempt / "answer.json").read_bytes()), "events_sha256": generation.sha((attempt / "events.jsonl").read_bytes()),
                  "stderr_sha256": generation.sha((attempt / "stderr.txt").read_bytes()), "settings": settings, "cli_version": version, "usage_events": usage}
        generation.save(attempt / "result.json", result)
        return attempt

    def test_wrapped_indent_recovery_preserves_exact_words_and_boundaries(self) -> None:
        raw = misplaced("A requires complete\nevidence before proceeding.")
        recovered, witness = grounding.recover_anchor(raw, section("A requires complete\n  evidence before proceeding.\n"))
        self.assertEqual(recovered["quote"], "A requires complete\n  evidence before proceeding.")
        self.assertEqual((recovered["start_line"], recovered["end_line"]), (10, 11))
        self.assertTrue(witness["word_boundaries_preserved"])

    def test_coordinate_only_exact_quote_recovery(self) -> None:
        recovered, witness = grounding.recover_anchor(misplaced("Complete evidence."), section("Heading\nComplete evidence.\n"))
        self.assertEqual(recovered["quote"], "Complete evidence.")
        self.assertEqual(recovered["start_line"], 11)
        self.assertEqual(witness["normalized_occurrence_count"], 1)

    def test_lexical_word_boundary_case_and_punctuation_changes_refuse(self) -> None:
        for quote, source in (("in valid", "invalid"), ("ab", "a b"), ("a b", "ab"), ("Evidence", "evidence"), ("Evidence!", "Evidence.")):
            with self.subTest(quote=quote, source=source), self.assertRaisesRegex(grounding.GroundingError, "no whitespace-run-equivalent"):
                grounding.recover_anchor(misplaced(quote), section(source))

    def test_unique_exact_match_does_not_override_second_normalized_match(self) -> None:
        with self.assertRaisesRegex(grounding.GroundingError, "ambiguous"):
            grounding.recover_anchor(misplaced("A requires evidence."), section("A requires evidence.\nA  requires evidence.\n"))

    def test_unicode_whitespace_kind_and_outer_trim_only(self) -> None:
        recovered, witness = grounding.recover_anchor(misplaced(" \tA\trequires evidence.\n"), section("A\u00a0 requires evidence.\n"))
        self.assertEqual(recovered["quote"], "A\u00a0 requires evidence.")
        self.assertTrue(witness["outer_whitespace_search_trimmed"])

    def test_strict_anchor_is_noop_without_a_recovery_claim(self) -> None:
        ground = {"section_id": "repo://test/section", "quote": "A requires evidence.", "start_line": 10, "end_line": 10}
        result, witness = grounding.recover_anchor(ground, section("A requires evidence.\nA  requires evidence.\n"))
        self.assertEqual(result, ground)
        self.assertIsNone(witness)

    def test_all_meaning_fields_and_section_ids_remain_canonically_identical(self) -> None:
        raw = copy.deepcopy(self.answer)
        for _, _, ground in grounding.anchors(raw):
            ground["quote"] = ground["quote"].replace("\n  ", "\n")
        derived, changes = grounding.normalize_answer(raw, self.chunk)
        self.assertEqual(len(changes), 2)
        self.assertEqual(generation.canonical(grounding.nongrounding(raw)), generation.canonical(grounding.nongrounding(derived)))
        self.assertEqual(raw["constraints"][0]["statement"], derived["constraints"][0]["statement"])
        self.assertEqual(raw["constraints"][0]["conditions"], derived["constraints"][0]["conditions"])
        generation.author_check(derived, self.chunk)

    def test_outside_section_and_non_grounding_reference_errors_refuse(self) -> None:
        raw = copy.deepcopy(self.answer)
        raw["concepts"][0]["grounding"][0]["section_id"] = "repo://outside/source"
        with self.assertRaisesRegex(grounding.GroundingError, "outside this exact"):
            grounding.normalize_answer(raw, self.chunk)
        raw = copy.deepcopy(self.answer)
        raw["constraints"][0]["applies_to_keys"] = ["invented_target"]
        with self.assertRaisesRegex(generation.GenerationError, "attachment targets"):
            grounding.normalize_answer(raw, self.chunk)

    def test_normalization_retains_original_failure_usage_and_immutable_answers(self) -> None:
        raw = copy.deepcopy(self.answer)
        raw["concepts"][0]["grounding"][0]["quote"] = raw["concepts"][0]["grounding"][0]["quote"].replace("\n  ", "\n")
        attempt = self.actor(raw, failed=True)
        original = {path.name: path.read_bytes() for path in attempt.iterdir() if path.is_file()}
        result = grounding.normalize(self.output)
        self.assertEqual(result["chunks"][0]["status"], "derived_validated")
        self.assertEqual(result["new_fp_calls"], 0)
        for name, expected in original.items():
            self.assertEqual((attempt / name).read_bytes(), expected)
        folder = self.output / "normalization" / self.chunk["id"]
        derived, journal = grounding.verify_normalization(self.output, self.plan, self.chunk, folder)
        self.assertEqual(journal["original_evidence"]["original_status"], "failed")
        self.assertEqual(journal["original_evidence"]["original_usage_events"], [{"input_tokens": 123, "output_tokens": 456}])
        self.assertGreaterEqual(journal["fd_elapsed_seconds"], 0)
        self.assertEqual(grounding.normalize(self.output)["chunks"][0]["reused"], True)
        assembled = grounding.assemble(self.output)
        self.assertEqual(assembled["status"], "proposed")
        self.assertEqual(assembled["new_fp_calls"], 0)
        self.assertFalse((self.output / "proposal").exists())

    def test_clean_original_noop_and_stale_original_sha_refusal(self) -> None:
        attempt = self.actor(self.answer)
        normalized = grounding.normalize(self.output)
        self.assertEqual(normalized["chunks"][0]["status"], "validated_original")
        self.assertEqual(normalized["chunks"][0]["changes"], 0)
        (attempt / "answer.json").write_text("{}")
        with self.assertRaisesRegex(grounding.GroundingError, "stale normalization evidence"):
            grounding.assemble(self.output)

    def test_meaning_rewrite_and_witness_hash_refresh_do_not_pass(self) -> None:
        self.actor(self.answer)
        grounding.normalize(self.output)
        folder = self.output / "normalization" / self.chunk["id"]
        derived = generation.load(folder / "derived-answer.json")
        derived["constraints"][0]["statement"] = "Proceed without evidence."
        generation.save(folder / "derived-answer.json", derived)
        journal = generation.load(folder / "journal.json")
        journal["derived_answer_sha256"] = generation.sha((folder / "derived-answer.json").read_bytes())
        generation.save(folder / "journal.json", journal)
        with self.assertRaisesRegex(grounding.GroundingError, "differs from deterministic"):
            grounding.assemble(self.output)
        with self.assertRaisesRegex(grounding.GroundingError, "differs from deterministic"):
            grounding.assemble(self.output, allow_partial=True)

    def test_actual_tool_event_and_cli_timeout_are_not_excused(self) -> None:
        self.actor(self.answer, tool_violation=True)
        result = grounding.normalize(self.output)
        self.assertEqual(result["chunks"][0]["status"], "refused")
        self.assertIn("actual actor tool", result["chunks"][0]["refusal"])
        path = self.output / "actors/author" / self.chunk["id"] / "attempt-001/result.json"
        failed = generation.load(path)
        failed["failures"] = ["process_timeout", "source_or_semantic_fragment_validation"]
        failed["timed_out"] = True
        generation.save(path, failed)
        result = grounding.normalize(self.output, name="normalization-timeout")
        self.assertEqual(result["chunks"][0]["status"], "refused")

    def test_appended_fp_repair_guidance_breaks_exact_frozen_prompt_custody(self) -> None:
        attempt = self.actor(self.answer)
        prompt = attempt / "prompt.txt"
        prompt.write_text(prompt.read_text() + "\nUse extra repair guidance.\n")
        invocation = generation.load(attempt / "invocation.json")
        invocation["prompt_sha256"] = generation.sha(prompt.read_bytes())
        generation.save(attempt / "invocation.json", invocation)
        result = grounding.normalize(self.output)
        self.assertEqual(result["chunks"][0]["status"], "refused")
        self.assertIn("exact source chunk", result["chunks"][0]["refusal"])

    def test_source_drift_and_missing_chunks_fail_closed(self) -> None:
        with self.assertRaisesRegex(grounding.GroundingError, "missing valid"):
            grounding.assemble(self.output)
        partial = grounding.assemble(self.output, allow_partial=True)
        self.assertFalse(partial["processing_complete"])
        (self.output / "corpus/rules.md").write_text("changed")
        with self.assertRaisesRegex(generation.GenerationError, "frozen source"):
            grounding.normalize(self.output)

    def test_newer_unfinished_actor_attempt_blocks_normalization_and_assembly(self) -> None:
        attempt = self.actor(self.answer)
        grounding.normalize(self.output)
        (attempt.parent / "attempt-002").mkdir()
        with self.assertRaisesRegex(grounding.GroundingError, "incomplete"):
            grounding.normalize(self.output)
        with self.assertRaisesRegex(grounding.GroundingError, "incomplete"):
            grounding.assemble(self.output)

    def test_explicit_partial_assembly_retains_existing_refusal_scope(self) -> None:
        raw = copy.deepcopy(self.answer)
        raw["concepts"][0]["grounding"][0]["section_id"] = "repo://outside/source"
        self.actor(raw, failed=True)
        refused = grounding.normalize(self.output)
        self.assertEqual(refused["chunks"][0]["status"], "refused")
        result = grounding.assemble(self.output, allow_partial=True)
        self.assertEqual(result["status"], "partial_proposal")
        coverage = generation.load(self.output / "grounded-partial-proposal/coverage.json")
        self.assertEqual(len(coverage["grounding_normalization"]["excluded_refusals"]), 1)
        model = generation.load(self.output / "grounded-partial-proposal/model.json")
        self.assertEqual(model["interpretation"]["dispositions"][0]["decision"], "refused")

    def test_recorded_source_failure_must_match_exact_recomputation(self) -> None:
        raw = copy.deepcopy(self.answer)
        raw["concepts"][0]["grounding"][0]["quote"] = "Lexically unrelated text."
        attempt = self.actor(raw, failed=True)
        result = generation.load(attempt / "result.json")
        result["validation_error"] = "A different stale failure."
        generation.save(attempt / "result.json", result)
        refused = grounding.normalize(self.output)
        self.assertIn("contradicts exact recomputation", refused["chunks"][0]["refusal"])
        journal = generation.load(self.output / "normalization" / self.chunk["id"] / "journal.json")
        self.assertEqual(journal["selected_original_attempt"], str(attempt.relative_to(self.output)))
        self.assertTrue(journal["unverified_original_pins"])

    def test_noop_cannot_be_relabelled_recovery_and_output_symlink_refuses(self) -> None:
        self.actor(self.answer)
        grounding.normalize(self.output)
        folder = self.output / "normalization" / self.chunk["id"]
        journal = generation.load(folder / "journal.json")
        journal["status"] = "derived_validated"
        generation.save(folder / "journal.json", journal)
        with self.assertRaisesRegex(grounding.GroundingError, "misstates no-op"):
            grounding.assemble(self.output)
        outside = self.root / "outside"
        outside.mkdir()
        (self.output / "normalization-outside").symlink_to(outside)
        with self.assertRaisesRegex(grounding.GroundingError, "symlink escapes"):
            grounding.normalize(self.output, name="normalization-outside")

    @unittest.skipUnless(os.environ.get("AC_GRAPHIFY_UPSTREAM"), "set AC_GRAPHIFY_UPSTREAM for actual pinned-upstream trial")
    def test_actual_upstream_grounded_proposal_round_trip(self) -> None:
        output = self.root / "graphify"
        upstream = Path(os.environ["AC_GRAPHIFY_UPSTREAM"])
        plan = generation.prepare(self.corpus, self.manifest, output, "graphify-ac", upstream, 1000)
        generation.build_discovery(output, upstream)
        raw = answer_for(generation.load(output / "chunks.json")[0])
        raw["concepts"][0]["grounding"][0]["quote"] = raw["concepts"][0]["grounding"][0]["quote"].replace("\n  ", "\n")
        self.actor(raw, output=output, failed=True)
        grounding.normalize(output)
        result = grounding.assemble(output, upstream=upstream)
        self.assertEqual(result["upstream_trial"]["commit"], generation.UPSTREAM_COMMIT)
        model = generation.load(output / "grounded-proposal/model.json")
        graph = generation.load(output / "grounded-proposal/graph.json")
        self.assertEqual(ac_graph.decode(ac_graph.GraphCarrier(graph)).document, model)
        self.assertEqual(model["basis"]["calculus"], plan["calculus"])
        self.assertEqual(model["populations"]["judgments"], [])


if __name__ == "__main__":
    unittest.main()
