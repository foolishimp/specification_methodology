"""Meaningful source custody, authoring-boundary and actual-upstream checks.

Authored fixture answers below are test data, not evidence of LLM quality.
Set AC_GRAPHIFY_UPSTREAM to run the real pinned extraction/build/export test.
"""
from __future__ import annotations

import copy
from contextlib import redirect_stderr, redirect_stdout
import io
import json
import os
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

TENANT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TENANT / "code"))
import ac_generate as gen
import ac_graph


SOURCE = "# Rules\nA may proceed only when evidence is complete.\nIf missing, refuse; wording may vary but prerequisites cannot.\nMeaning of external policy remains unresolved.\n"


def fixture_answer(chunk: dict) -> dict:
    section = chunk["segments"][0]
    ground = {"section_id": section["id"], "start_line": 2, "end_line": 2,
              "quote": "A may proceed only when evidence is complete."}
    def common(key: str) -> dict:
        return {"key": key, "grounding": [copy.deepcopy(ground)]}
    answer = {"concepts": [{**common("proceed"), "label": "Proceed", "definition": "An action requiring complete evidence.",
                            "conditions": ["Evidence is complete."], "exceptions": []},
                           {**common("evidence"), "label": "Evidence", "definition": "The evidence required before proceeding.", "conditions": [], "exceptions": []}],
              "relations": [{**common("proceed_requires_evidence"), "kind": "requires", "source_key": "proceed", "target_key": "evidence",
                              "meaning": "Proceeding requires complete evidence.", "governing": True, "conditions": [], "exceptions": []}],
              "constraints": [{**common("complete_evidence"), "applies_to_keys": ["proceed"], "statement": "Proceed only with complete evidence; otherwise refuse.",
                               "conditions": ["A request to proceed is considered."], "exceptions": [], "uncertainty": ""}],
              "latitude": [{**common("wording"), "applies_to_keys": ["proceed"], "allowed": ["Wording may vary."], "forbidden": ["Removing the prerequisite."]}],
              "residuals": [{**common("external_policy"), "subject_key": "proceed", "uncertainty": "External policy meaning is unresolved.", "consequence": "Re-enter exact policy before relying on it."}],
              "dispositions": [{"section_id": section["id"], "decision": "residual", "keys": ["proceed", "evidence", "proceed_requires_evidence", "complete_evidence", "wording", "external_policy"],
                                "reason": "Retains prerequisite, refusal, wording latitude and unresolved external meaning."}],
              "limitations": ["No external-policy meaning or semantic acceptance established."]}
    answer["latitude"][0]["grounding"] = [{"section_id": section["id"], "start_line": 3, "end_line": 3,
                                            "quote": "wording may vary but prerequisites cannot."}]
    answer["residuals"][0]["grounding"] = [{"section_id": section["id"], "start_line": 4, "end_line": 4,
                                             "quote": "Meaning of external policy remains unresolved."}]
    return answer


class GenerationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.corpus = self.root / "input"
        self.corpus.mkdir()
        (self.corpus / "rules.md").write_text(SOURCE)
        self.manifest = self.root / "manifest.json"
        gen.save(self.manifest, {"profile": "ac.generation.corpus/1", "subject_id": "repo://test/source/", "revision": "test",
                                 "files": [{"path": "rules.md", "sha256": gen.sha(SOURCE.encode()), "bytes": len(SOURCE.encode()), "git_blob": "test-only"}]})
        self.output = self.root / "direct"
        self.plan = gen.prepare(self.corpus, self.manifest, self.output, "direct", None, 1000)
        self.chunks = gen.load(self.output / "chunks.json")
        self.answer = fixture_answer(self.chunks[0])

    def tearDown(self) -> None:
        self.temp.cleanup()

    def fake_attempt(self, stage: str, answer: dict, output: Path | None = None, *,
                     ordinal: int = 1, validated: bool = True) -> Path:
        """Complete synthetic CLI capture with the exact frozen stage contract."""
        output = output or self.output
        plan, chunks = gen.checkpoint(output)
        chunk = chunks[0]
        path = output / "actors" / stage / chunk["id"] / f"attempt-{ordinal:03d}"
        path.mkdir(parents=True)
        (path / "empty-workspace").mkdir()
        gen.save(path / "answer.json", answer)
        prompt = gen.extraction_prompt(plan, chunk, output) if stage == "extract" else gen.author_prompt(plan, chunk, output)
        (path / "prompt.txt").write_text(prompt)
        schema = gen.ASSETS / ("extraction.schema.json" if stage == "extract" else "author.schema.json")
        self.assertEqual(gen.schema_errors(answer, gen.load(schema)), [])
        if stage == "extract":
            gen.semantic_check(answer, chunk, output, gen.upstream_modules(Path(plan["upstream"]["root"])))
        else:
            gen.author_check(answer, chunk)
        settings = {"model": "test-model", "model_reasoning_effort": "high"}
        version = "codex-cli synthetic-test-only"
        gen.save(output / "actor-settings.json", {"settings": settings, "cli_version": version})
        overrides = {**settings, "features.shell_tool": False, "features.apps": False, "features.multi_agent": False,
                     "features.memories": False, "features.js_repl": False, "web_search": "disabled", "project_doc_max_bytes": 0}
        command = ["/test-only/codex", "exec", "--json", "--ephemeral", "--sandbox", "read-only", "--skip-git-repo-check", "--color", "never",
                   "--output-schema", str(schema.resolve()), "--output-last-message", str((path / "answer.json").resolve()),
                   "--cd", str((path / "empty-workspace").resolve())]
        for key, value in overrides.items():
            command.extend(["-c", key + "=" + json.dumps(value)])
        command.append("-")
        gen.save(path / "invocation.json", {"profile": "ac.generation.actor-invocation/1", "settings": settings, "cli_version": version,
                 "prompt_sha256": gen.sha(prompt.encode()), "schema_sha256": gen.sha(schema.read_bytes()), "inline_overrides": overrides,
                 "effective_mcp_inventory": [], "command": command, "cwd": str(path / "empty-workspace"),
                 "config_path": "/test-only/config.toml", "config_sha256": "f" * 64})
        usage = [{"input_tokens": 123, "output_tokens": 456}]
        events = [{"type": "item.completed", "item": {"type": "agent_message"}}, {"type": "turn.completed", "usage": usage[0]}]
        (path / "events.jsonl").write_text("".join(json.dumps(event) + "\n" for event in events))
        (path / "stderr.txt").write_text("")
        gen.save(path / "usage.json", {"usage_events": usage})
        gen.save(path / "result.json", {"profile": "ac.generation.actor-result/1", "status": "completed", "failures": [],
                 "cli_exit_code": 0, "timed_out": False, "user_config_unchanged": True, "schema_errors": [], "unexpected_item_types": [],
                 "answer_sha256": gen.sha((path / "answer.json").read_bytes()), "events_sha256": gen.sha((path / "events.jsonl").read_bytes()),
                 "stderr_sha256": gen.sha((path / "stderr.txt").read_bytes()), "settings": settings, "cli_version": version, "usage_events": usage})
        if validated:
            gen.save(path / "validation.json", {"status": "structurally_valid_proposal", "answer_sha256": gen.sha((path / "answer.json").read_bytes()), "chunk_sha256": gen.digest(chunk)})
        return path

    def test_snapshot_and_chunks_cover_exact_original_source(self) -> None:
        self.assertEqual((self.output / "corpus/rules.md").read_bytes(), SOURCE.encode())
        self.assertEqual("".join(s["text"] for c in self.chunks for s in c["segments"]), SOURCE)
        self.assertEqual(gen.checkpoint(self.output)[0], self.plan)

    def test_heading_identity_survives_inserted_lines_and_fences(self) -> None:
        first = gen.sections("rules.md", SOURCE, "repo://test/source/")[0]["id"]
        moved = gen.sections("rules.md", "Introduction.\n\n" + SOURCE, "repo://test/source/")
        self.assertEqual(moved[-1]["id"], first)
        fenced = gen.sections("doc.md", "# A\n```md\n# Not a section\n```\n# B\n", "repo://test/")
        self.assertEqual(len(fenced), 2)

    def test_fence_width_marker_indentation_and_closing_content_preserve_partitions(self) -> None:
        cases = {
            "backtick-control": "```md\n# Hidden\n```",
            "wide-backtick-inner-shorter": "````md\n```\n# Hidden\n````",
            "wide-tilde-inner-shorter": "~~~~md\n~~~\n# Hidden\n~~~~",
            "longer-closer": "````md\n# Hidden\n`````",
            "different-marker": "````md\n~~~~\n# Hidden\n````",
            "closing-content-is-data": "````md\n```` trailing\n# Hidden\n````",
            "closing-info-is-data": "~~~md\n~~~md\n# Hidden\n~~~",
            "three-space-indent": "   ````md\n  ```\n# Hidden\n   ````\t ",
            "overindented-close-is-data": "```md\n    ```\n# Hidden\n```",
            "tilde-info-can-contain-backticks": "~~~md`info\n# Hidden\n~~~",
        }
        expected_ids = [s["id"] for s in gen.sections("doc.md", "# Before\n# Real\n", "repo://test/")]
        for name, block in cases.items():
            with self.subTest(name=name):
                source = "# Before\n" + block + "\n# Real\nBody.\n"
                sections = gen.sections("doc.md", source, "repo://test/")
                self.assertEqual([s["heading"] for s in sections], ["Before", "Real"])
                self.assertEqual([s["id"] for s in sections], expected_ids)
                self.assertEqual("".join(s["text"] for s in sections), source)
                chunks = gen.make_chunks(sections, 1000)
                self.assertEqual("".join(s["text"] for c in chunks for s in c["segments"]), source)
                self.assertEqual(sections[-1]["start_line"], len(source.splitlines()) - 1)
        for invalid_opening in ("    ```md", "\t```md", "```md`info"):
            source = "# Before\n" + invalid_opening + "\n# Real\n"
            self.assertEqual([s["heading"] for s in gen.sections("doc.md", source, "repo://test/")], ["Before", "Real"])
        self.assertEqual(len(gen.sections("doc.md", "# Before\n````\n# Hidden\n", "repo://test/")), 1)
        self.assertEqual(len(gen.sections("doc.txt", "# Before\n# Real\n", "repo://test/")), 1)

    def test_chunks_pack_files_and_split_sections_without_loss(self) -> None:
        text = "# Large\n" + "word " * 10 + "\n" + ("next line\n" * 200)
        sections = gen.sections("large.md", text, "repo://test/") + gen.sections("small.md", "Small.\n", "repo://test/")
        chunks = gen.make_chunks(sections, 1000)
        self.assertTrue(all(chunk["source_chars"] <= 1000 for chunk in chunks))
        self.assertEqual("".join(s["text"] for c in chunks for s in c["segments"]), text + "Small.\n")
        self.assertTrue(any("parent_section_id" in s for c in chunks for s in c["segments"]))

    def test_oversize_single_line_explicitly_refuses(self) -> None:
        with self.assertRaisesRegex(gen.GenerationError, "single line exceeds"):
            gen.make_chunks(gen.sections("x.json", "x" * 1001, "repo://test/"), 1000)

    def test_stale_source_and_path_escape_refuse(self) -> None:
        manifest = gen.load(self.manifest)
        manifest["files"][0]["path"] = "../outside.md"
        gen.save(self.manifest, manifest)
        with self.assertRaises(gen.GenerationError):
            gen.prepare(self.corpus, self.manifest, self.root / "bad", "direct", None)
        (self.output / "corpus/rules.md").write_text("tampered")
        with self.assertRaisesRegex(gen.GenerationError, "frozen source"):
            gen.checkpoint(self.output)

    def test_source_symlink_escape_refuses_before_snapshot(self) -> None:
        outside = self.root / "outside.md"
        outside.write_text(SOURCE)
        (self.corpus / "rules.md").unlink()
        (self.corpus / "rules.md").symlink_to(outside)
        with self.assertRaisesRegex(gen.GenerationError, "symlink escapes"):
            gen.prepare(self.corpus, self.manifest, self.root / "bad", "direct", None)
        self.assertFalse((self.root / "bad").exists())

    def test_exact_quote_and_range_are_checked(self) -> None:
        gen.author_check(self.answer, self.chunks[0])
        wrong = copy.deepcopy(self.answer)
        wrong["concepts"][0]["grounding"][0]["quote"] = "A may proceed without evidence."
        with self.assertRaisesRegex(gen.GenerationError, "not exact source"):
            gen.author_check(wrong, self.chunks[0])
        wrong = copy.deepcopy(self.answer)
        wrong["concepts"][0]["grounding"][0]["end_line"] = 2000
        with self.assertRaisesRegex(gen.GenerationError, "line range escapes"):
            gen.author_check(wrong, self.chunks[0])

    def test_dangling_links_and_ungrounded_dispositions_refuse(self) -> None:
        wrong = copy.deepcopy(self.answer)
        wrong["relations"][0]["target_key"] = "undeclared"
        with self.assertRaisesRegex(gen.GenerationError, "endpoints"):
            gen.author_check(wrong, self.chunks[0])
        wrong = copy.deepcopy(self.answer)
        wrong["dispositions"][0]["keys"] = []
        with self.assertRaisesRegex(gen.GenerationError, "requires authored records"):
            gen.author_check(wrong, self.chunks[0])

    def test_extra_author_fields_and_missing_source_disposition_refuse(self) -> None:
        wrong = copy.deepcopy(self.answer)
        wrong["accepted"] = True
        with self.assertRaisesRegex(gen.GenerationError, "schema"):
            gen.author_check(wrong, self.chunks[0])
        wrong = copy.deepcopy(self.answer)
        wrong["dispositions"] = []
        with self.assertRaises(gen.GenerationError):
            gen.author_check(wrong, self.chunks[0])

    def test_adapter_preserves_declared_meaning_and_optional_families(self) -> None:
        model, coverage = gen.model_from_answers(self.plan, self.chunks, {self.chunks[0]["id"]: self.answer}, [])
        checked = ac_graph.validate(model)
        self.assertEqual(ac_graph.decode(ac_graph.materialize(checked)).document, model)
        self.assertEqual(set(model["populations"]), set(ac_graph.CORE_FIELDS))
        for family in ("traversals", "transformations", "judgments"):
            self.assertEqual(model["populations"][family], [])
        constraint = model["populations"]["constraints"][0]
        self.assertEqual(constraint["predicate"]["conditions"], self.answer["constraints"][0]["conditions"])
        self.assertEqual(constraint["predicate"]["exceptions"], [])
        self.assertEqual(constraint["predicate"]["grounding"][0]["quote"], self.answer["constraints"][0]["grounding"][0]["quote"])
        self.assertEqual(coverage["semantic_acceptance"], "not requested or issued")
        self.assertEqual(model["basis"]["calculus"]["sha256"], ac_graph.CALCULUS_SHA256)

    def test_governing_role_is_author_declared_not_inferred(self) -> None:
        model, _ = gen.model_from_answers(self.plan, self.chunks, {self.chunks[0]["id"]: self.answer}, [])
        self.assertEqual(len(model["dependency_contract"]["required_relation_kinds"]), 1)
        other = copy.deepcopy(self.answer)
        other["relations"][0]["governing"] = False
        model, _ = gen.model_from_answers(self.plan, self.chunks, {self.chunks[0]["id"]: other}, [])
        self.assertEqual(model["dependency_contract"]["required_relation_kinds"], [])

    def test_semantic_contradiction_is_not_claimed_detected_by_adapter(self) -> None:
        # Grounding proves re-entry. Deliberately wrong meaning can still be
        # well-shaped: this passing structural check is NOT semantic acceptance.
        wrong = copy.deepcopy(self.answer)
        wrong["concepts"][0]["definition"] = "A may proceed without any evidence."
        gen.author_check(wrong, self.chunks[0])
        model, coverage = gen.model_from_answers(self.plan, self.chunks, {self.chunks[0]["id"]: wrong}, [])
        self.assertEqual(coverage["semantic_completeness"], "unassessed")
        self.assertIn("without any evidence", model["populations"]["objects"][0]["value"]["definition"])

    def test_partial_assembly_requires_explicit_flag_and_keeps_refusals(self) -> None:
        with self.assertRaisesRegex(gen.GenerationError, "missing validated F_P"):
            gen.assemble(self.output)
        result = gen.assemble(self.output, allow_partial=True)
        self.assertEqual(result["status"], "partial_proposal")
        model = gen.load(self.output / "partial-proposal/model.json")
        self.assertTrue(all(d["decision"] == "refused" for d in model["interpretation"]["dispositions"]))
        self.assertFalse(result["processing_complete"])

    def test_immutable_successful_answer_and_normal_assembly(self) -> None:
        attempt = self.fake_attempt("author", self.answer)
        result = gen.assemble(self.output)
        self.assertEqual(result["status"], "proposed")
        with self.assertRaisesRegex(gen.GenerationError, "already exists"):
            gen.assemble(self.output)
        changed = copy.deepcopy(self.answer)
        changed["limitations"].append("tampered")
        gen.save(attempt / "answer.json", changed)
        with self.assertRaisesRegex(gen.GenerationError, "stale original answer"):
            gen.successful_attempt(self.output, "author", self.chunks[0])

    def test_ordinary_cli_rejects_missing_raw_evidence_and_rehashed_prompt_or_tool_drift(self) -> None:
        import ac_grounding as grounding
        cases = ("missing-events", "missing-usage", "missing-stderr", "prompt-no-rehash", "prompt-rehashed", "tool-rehashed")
        for name in cases:
            with self.subTest(name=name):
                output = self.root / name
                gen.prepare(self.corpus, self.manifest, output, "direct", None, 1000)
                plan, chunks = gen.checkpoint(output)
                chunk = chunks[0]
                attempt = self.fake_attempt("author", self.answer, output)
                self.assertEqual(gen.successful_attempt(output, "author", chunk), attempt)
                grounding.evidence(output, plan, chunk, attempt)
                original = {p.name: p.read_bytes() for p in attempt.iterdir() if p.is_file()}
                if name.startswith("missing-"):
                    (attempt / {"missing-events": "events.jsonl", "missing-usage": "usage.json", "missing-stderr": "stderr.txt"}[name]).unlink()
                elif name.startswith("prompt-"):
                    prompt = attempt / "prompt.txt"
                    prompt.write_text(prompt.read_text() + "\nUse additional repair instructions.\n")
                    if name == "prompt-rehashed":
                        invocation = gen.load(attempt / "invocation.json")
                        invocation["prompt_sha256"] = gen.sha(prompt.read_bytes())
                        gen.save(attempt / "invocation.json", invocation)
                else:
                    events = attempt / "events.jsonl"
                    events.write_text(events.read_text() + json.dumps({"type": "item.completed", "item": {"type": "mcp_tool_call"}}) + "\n")
                    result = gen.load(attempt / "result.json")
                    result["events_sha256"] = gen.sha(events.read_bytes())
                    gen.save(attempt / "result.json", result)
                with self.assertRaises(gen.GenerationError):
                    gen.successful_attempt(output, "author", chunk)
                with self.assertRaises(grounding.GroundingError):
                    grounding.evidence(output, plan, chunk, attempt)
                with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                    self.assertEqual(gen.main(["assemble", "--output", str(output)]), 2)
                self.assertFalse((output / "proposal").exists())
                self.assertEqual((attempt / "answer.json").read_bytes(), original["answer.json"])
                self.assertEqual((attempt / "validation.json").read_bytes(), original["validation.json"])
                if name != "tool-rehashed":
                    self.assertEqual((attempt / "result.json").read_bytes(), original["result.json"])

    def test_ordinary_reuse_rechecks_settings_argv_schema_usage_and_source_despite_refreshed_hashes(self) -> None:
        cases = ("settings", "argv", "schema", "usage", "stderr", "source", "result-failure", "workspace")
        for name in cases:
            with self.subTest(name=name):
                output = self.root / name
                gen.prepare(self.corpus, self.manifest, output, "direct", None, 1000)
                chunk = gen.load(output / "chunks.json")[0]
                attempt = self.fake_attempt("author", self.answer, output)
                self.assertEqual(gen.successful_attempt(output, "author", chunk), attempt)
                result = gen.load(attempt / "result.json")
                invocation = gen.load(attempt / "invocation.json")
                if name == "settings":
                    result["settings"]["model"] = "different-model"
                elif name == "argv":
                    invocation["command"][invocation["command"].index("--sandbox") + 1] = "workspace-write"
                elif name == "schema":
                    invocation["schema_sha256"] = "0" * 64
                elif name == "usage":
                    gen.save(attempt / "usage.json", {"usage_events": [{"input_tokens": 1, "output_tokens": 2}]})
                elif name == "stderr":
                    (attempt / "stderr.txt").write_text("Changed raw stderr\n")
                elif name == "source":
                    answer = copy.deepcopy(self.answer)
                    answer["concepts"][0]["grounding"][0]["quote"] = "Not present in the source."
                    gen.save(attempt / "answer.json", answer)
                    result["answer_sha256"] = gen.sha((attempt / "answer.json").read_bytes())
                    gen.save(attempt / "validation.json", {"answer_sha256": result["answer_sha256"], "chunk_sha256": gen.digest(chunk)})
                elif name == "result-failure":
                    result["failures"] = ["isolation_violation"]
                else:
                    (attempt / "empty-workspace/extra.txt").write_text("No longer empty.")
                gen.save(attempt / "invocation.json", invocation)
                gen.save(attempt / "result.json", result)
                with self.assertRaises(gen.GenerationError):
                    gen.successful_attempt(output, "author", chunk)

    def test_latest_failed_or_unfinished_attempt_blocks_older_success_and_requires_explicit_retry(self) -> None:
        first = self.fake_attempt("author", self.answer)
        original = {p.name: p.read_bytes() for p in first.iterdir() if p.is_file()}
        newer = first.parent / "attempt-002"
        newer.mkdir()
        self.assertIsNone(gen.successful_attempt(self.output, "author", self.chunks[0]))
        with self.assertRaisesRegex(gen.GenerationError, "missing validated F_P"):
            gen.assemble(self.output)
        newer.rmdir()
        newer = self.fake_attempt("author", self.answer, ordinal=2, validated=False)
        failure = gen.load(newer / "result.json")
        failure.update(status="failed", failures=["cli_nonzero_exit"], cli_exit_code=1)
        gen.save(newer / "result.json", failure)
        self.assertIsNone(gen.successful_attempt(self.output, "author", self.chunks[0]))
        partial = gen.assemble(self.output, allow_partial=True)
        self.assertFalse(partial["processing_complete"])
        self.assertEqual(partial["family_counts"]["objects"], 0)
        settings = gen.load(self.output / "actor-settings.json")
        def capture(prompt, schema, path, *args):
            captured = self.fake_attempt("author", self.answer, ordinal=3, validated=False)
            self.assertEqual(captured, path)
            self.assertEqual(prompt, (captured / "prompt.txt").read_text())
            return gen.load(captured / "result.json")
        with patch.object(gen, "actor_settings", return_value=(None, None, settings)), patch.object(gen, "run_actor", side_effect=capture) as runner:
            with self.assertRaisesRegex(gen.GenerationError, "explicit --retry-failed"):
                gen.stage(self.output, "author", execute=True)
            runner.assert_not_called()
            result = gen.stage(self.output, "author", execute=True, retry_failed=True)
            self.assertEqual(result["status"], "completed")
            self.assertEqual(runner.call_count, 1)
        self.assertEqual(gen.successful_attempt(self.output, "author", self.chunks[0]).name, "attempt-003")
        self.assertEqual(gen.assemble(self.output)["status"], "proposed")
        for name, raw in original.items():
            self.assertEqual((first / name).read_bytes(), raw)
        self.assertEqual(gen.load(newer / "result.json")["status"], "failed")

    def test_graph_treatments_use_stage_specific_frozen_contracts_and_revalidate_source(self) -> None:
        # Synthetic upstream/discovery receipts isolate the stage contract here;
        # separate enabled boundary tests exercise unchanged actual upstream.
        modules = {"semantic_cleanup": SimpleNamespace(validate_semantic_fragment=lambda answer: [])}
        for mode, stage in (("graphify-ac", "author"), ("graphify", "extract"), ("graphify", "author")):
            for drift in ("prompt", "tool", "source"):
                with self.subTest(mode=mode, stage=stage, drift=drift):
                    output = self.root / f"{mode}-{stage}-{drift}"
                    upstream = self.root / f"upstream-{mode}-{stage}-{drift}"
                    reference = upstream / gen.UPSTREAM_PROMPT
                    reference.parent.mkdir(parents=True)
                    reference.write_text("```\nSynthetic extraction contract FILE_LIST CHUNK_NUM TOTAL_CHUNKS DEEP_MODE\n```\n")
                    record = {"root": str(upstream), "commit": gen.UPSTREAM_COMMIT, "prompt_path": gen.UPSTREAM_PROMPT,
                              "prompt_sha256": gen.sha(reference.read_bytes())}
                    with patch.object(gen, "verify_upstream", return_value=record):
                        gen.prepare(self.corpus, self.manifest, output, mode, upstream, 1000)
                    plan, chunks = gen.checkpoint(output)
                    chunk = chunks[0]
                    semantic = {"nodes": [{"id": "rules", "label": "Rules", "file_type": "document",
                                  "source_file": str((output / "corpus/rules.md").resolve()), "source_location": "L1",
                                  "source_url": None, "captured_at": None, "author": None, "contributor": None, "rationale": None}],
                                "edges": [], "hyperedges": [], "input_tokens": 0, "output_tokens": 0}
                    with patch.object(gen, "upstream_modules", return_value=modules):
                        extraction = self.fake_attempt("extract", semantic, output) if mode == "graphify" else None
                        if stage == "author":
                            folder = output / "discovery"
                            folder.mkdir()
                            gen.save(folder / "graph.json", {"nodes": [], "links": []})
                            entry = {"id": chunk["id"]}
                            if extraction:
                                entry.update(attempt=str(extraction.relative_to(output)), answer_sha256=gen.sha((extraction / "answer.json").read_bytes()))
                            gen.save(folder / "coverage.json", {"chunks": [entry]})
                            gen.save(folder / "result.json", {"status": "completed", "mode": mode,
                                     "files": {p.name: gen.sha(p.read_bytes()) for p in folder.iterdir()}})
                            attempt = self.fake_attempt("author", self.answer, output)
                        else:
                            attempt = extraction
                        self.assertEqual(gen.successful_attempt(output, stage, chunk), attempt)
                        self.assertEqual(gen.stage(output, stage, execute=False)["status"], "completed")
                        invocation = gen.load(attempt / "invocation.json")
                        expected_schema = "extraction.schema.json" if stage == "extract" else "author.schema.json"
                        self.assertEqual(invocation["schema_sha256"], plan["assets"][expected_schema])
                        result = gen.load(attempt / "result.json")
                        if drift == "prompt":
                            prompt = attempt / "prompt.txt"
                            prompt.write_text(prompt.read_text() + "\nAdditional guidance outside the frozen contract.\n")
                            invocation["prompt_sha256"] = gen.sha(prompt.read_bytes())
                            gen.save(attempt / "invocation.json", invocation)
                        elif drift == "tool":
                            events = attempt / "events.jsonl"
                            events.write_text(events.read_text() + json.dumps({"type": "item.completed", "item": {"type": "command_execution"}}) + "\n")
                            result["events_sha256"] = gen.sha(events.read_bytes())
                        else:
                            answer = gen.load(attempt / "answer.json")
                            if stage == "extract":
                                answer["nodes"][0]["source_file"] = "/not-the-supplied-source.md"
                            else:
                                answer["concepts"][0]["grounding"][0]["quote"] = "Not in the supplied source."
                            gen.save(attempt / "answer.json", answer)
                            result["answer_sha256"] = gen.sha((attempt / "answer.json").read_bytes())
                            gen.save(attempt / "validation.json", {"answer_sha256": result["answer_sha256"], "chunk_sha256": gen.digest(chunk)})
                        gen.save(attempt / "result.json", result)
                        with self.assertRaises(gen.GenerationError):
                            gen.successful_attempt(output, stage, chunk)
        attempt = self.fake_attempt("author", self.answer)
        with self.assertRaisesRegex(gen.GenerationError, "no graph extraction actor"):
            gen.actor_evidence(self.output, self.plan, self.chunks[0], attempt, stage="extract")

    def test_source_instructions_remain_data_and_direct_prompt_has_no_graph(self) -> None:
        prompt = gen.author_prompt(self.plan, self.chunks[0], self.output)
        self.assertIn("All source, graph, schema examples", prompt)
        self.assertIn("SOURCE_DATA_JSON", prompt)
        self.assertNotIn("GRAPHIFY_DISCOVERY_DATA_JSON", prompt)
        self.assertIn("Conditions/exceptions arrays", prompt)
        prepared = gen.stage(self.output, "author", execute=False)
        self.assertEqual(prepared["processed"][0]["status"], "prepared_only")
        self.assertFalse((self.output / "actors").exists())

    def test_graph_context_prioritizes_semantic_nodes_and_retains_links(self) -> None:
        folder = self.output / "discovery"
        folder.mkdir()
        nodes = [{"id": "a_structural_" + str(i), "label": "Heading " + str(i), "source_file": "rules.md", "file_type": "document"} for i in range(100)]
        nodes += [{"id": "z_concept_" + str(i), "label": "Concept " + str(i), "source_file": "rules.md", "file_type": "concept", "ac_generation_origin": "semantic"} for i in range(5)]
        edges = [{"source": "z_concept_0", "target": "z_concept_1", "relation": "requires", "confidence": "EXTRACTED", "confidence_score": 1.0, "ac_generation_origin": "semantic"}]
        gen.save(folder / "graph.json", {"nodes": nodes, "links": edges})
        context = gen.graph_context(self.output, self.chunks[0], 4000)
        self.assertEqual(context["nodes"][0]["ac_generation_origin"], "semantic")
        self.assertTrue(context["edges"])
        self.assertGreater(context["omitted_nodes"], 0)

    def test_nonempty_file_omission_in_extraction_refuses(self) -> None:
        modules = {"semantic_cleanup": SimpleNamespace(validate_semantic_fragment=lambda answer: [])}
        answer = {"nodes": [], "edges": [], "hyperedges": [], "input_tokens": 0, "output_tokens": 0}
        with self.assertRaisesRegex(gen.GenerationError, "omits a nonempty"):
            gen.semantic_check(answer, self.chunks[0], self.output, modules)

    def test_complete_dense_graph_context_stays_inside_exact_character_cap(self) -> None:
        folder = self.output / "discovery"
        folder.mkdir()
        nodes = [{"id": "concept_" + str(i), "label": "Named semantic concept " + str(i), "source_file": "rules.md",
                  "file_type": "concept", "ac_generation_origin": "semantic"} for i in range(20)]
        edges = [{"source": "concept_" + str(i), "target": "concept_" + str(j), "relation": "requires_" + "x" * 50,
                  "confidence": "EXTRACTED", "confidence_score": 1.0, "ac_generation_origin": "semantic"}
                 for i in range(20) for j in range(20) if i != j]
        gen.save(folder / "graph.json", {"nodes": nodes, "links": edges})
        for cap in (1000, 4000, 40_000):
            context = gen.graph_context(self.output, self.chunks[0], cap)
            self.assertLessEqual(len(gen.canonical(context).decode()), cap)
            self.assertIn("full_graph_sha256", context)
            self.assertIn("semantic_seed_nodes", context)
        self.assertTrue(gen.graph_context(self.output, self.chunks[0], 4000)["edges"])

    def test_structural_failure_is_retained_and_blocks_discovery_success(self) -> None:
        # Structural failure is independent of the optional extraction actor.
        plan = {**self.plan, "mode": "graphify-ac", "upstream": {"root": "unused"}}
        failed = {"nodes": [], "edges": [], "failed_sources": ["rules.md"], "extracted_sources": []}
        modules = {"extract": SimpleNamespace(extract=lambda *args, **kwargs: failed)}
        with patch.object(gen, "checkpoint", return_value=(plan, self.chunks)), patch.object(gen, "upstream_modules", return_value=modules):
            with self.assertRaisesRegex(gen.GenerationError, "structural extraction failed"):
                gen.build_discovery(self.output)
        self.assertEqual(gen.load(self.output / "discovery/structural.json")["failed_sources"], ["rules.md"])
        self.assertFalse((self.output / "discovery/graph.json").exists())

    def test_wrong_chunk_custody_and_nonfinite_json_refuse(self) -> None:
        attempt = self.fake_attempt("author", self.answer)
        gen.save(attempt / "validation.json", {"answer_sha256": gen.sha((attempt / "answer.json").read_bytes()), "chunk_sha256": "0" * 64})
        with self.assertRaisesRegex(gen.GenerationError, "different answer/chunk"):
            gen.successful_attempt(self.output, "author", self.chunks[0])
        bad = self.root / "nan.json"
        bad.write_text('{"value":NaN}')
        with self.assertRaisesRegex(gen.GenerationError, "non-finite"):
            gen.load(bad)

    def test_fake_cli_isolated_invocation_usage_and_unexpected_tool_refusal(self) -> None:
        # A tiny local protocol fake exercises runner isolation/auditing. This
        # invokes NO LLM, uses no authentication and is not quality evidence.
        config_home = self.root / "config"
        config_home.mkdir()
        config = config_home / "config.toml"
        config.write_text('model="test-model"\nmodel_reasoning_effort="high"\n')
        original = config.read_bytes()
        fake = self.root / "fake-codex"
        fake.write_text("#!" + sys.executable + "\n" + '''import json,os,sys
from pathlib import Path
args=sys.argv[1:]
if args==['--version']:
 print('codex-cli test-only');sys.exit()
if args[:2]==['mcp','list']:
 print(json.dumps([{'name':'cua_repl','enabled':not any('mcp_servers.cua_repl.enabled=false' in x for x in args)}]));sys.exit()
sys.stdin.read()
answer=ANSWER_VALUE
Path(args[args.index('--output-last-message')+1]).write_text(json.dumps(answer))
kind='mcp_tool_call' if os.environ.get('FAKE_TOOL_VIOLATION') else 'agent_message'
print(json.dumps({'type':'item.completed','item':{'type':kind}}))
print(json.dumps({'type':'turn.completed','usage':{'input_tokens':42,'cached_input_tokens':0,'output_tokens':12}}))
'''.replace("ANSWER_VALUE", repr(self.answer)))
        fake.chmod(0o755)
        with patch.dict(os.environ, {"CODEX_HOME": str(config_home)}):
            result = gen.run_actor("Synthetic source DATA only.", gen.ASSETS / "author.schema.json", self.root / "actor", str(fake), 20)
            self.assertEqual(result["status"], "completed")
            self.assertEqual(result["usage_events"][0]["input_tokens"], 42)
            invocation = gen.load(self.root / "actor/invocation.json")
            self.assertEqual(invocation["effective_mcp_inventory"], [{"name": "cua_repl", "enabled": False}])
            self.assertFalse(invocation["inline_overrides"]["features.shell_tool"])
            self.assertEqual(invocation["inline_overrides"]["project_doc_max_bytes"], 0)
            with patch.dict(os.environ, {"FAKE_TOOL_VIOLATION": "yes"}):
                failed = gen.run_actor("Synthetic source DATA only.", gen.ASSETS / "author.schema.json", self.root / "bad-actor", str(fake), 20)
                self.assertIn("isolation_violation", failed["failures"])
        self.assertEqual(config.read_bytes(), original)

    def test_a_c_aware_mode_names_custom_profile_and_refuses_stock_extraction(self) -> None:
        upstream = self.root / "upstream"
        upstream.mkdir()
        record = {"root": str(upstream), "commit": gen.UPSTREAM_COMMIT, "prompt_path": gen.UPSTREAM_PROMPT,
                  "prompt_sha256": "0" * 64}
        output = self.root / "aware"
        with patch.object(gen, "verify_upstream", return_value=record):
            plan = gen.prepare(self.corpus, self.manifest, output, "graphify-ac", upstream, 1000)
        self.assertEqual(plan["semantic_extraction_profile"], "a_c.graphify.source-semantic-extraction/1")
        self.assertFalse((output / "upstream-extraction-spec.md").exists())
        self.assertEqual(plan["assets"]["author.schema.json"], self.plan["assets"]["author.schema.json"])
        with self.assertRaisesRegex(gen.GenerationError, "no graph extraction actor"):
            gen.stage(output, "extract", execute=False)
        with self.assertRaisesRegex(gen.GenerationError, "before authoring"):
            gen.stage(output, "author", execute=False)

    def test_a_c_aware_run_builds_graph_before_only_one_authoring_stage(self) -> None:
        order = []
        plan = {**self.plan, "mode": "graphify-ac"}
        def graph(*args, **kwargs):
            order.append("graph")
            return {"status": "completed"}
        def author(output, stage, **kwargs):
            order.append(stage)
            return {"status": "completed"}
        def assembly(*args, **kwargs):
            order.append("assemble")
            return {"status": "proposed"}
        with patch.object(gen, "checkpoint", return_value=(plan, self.chunks)), patch.object(gen, "build_discovery", side_effect=graph), \
                patch.object(gen, "stage", side_effect=author), patch.object(gen, "assemble", side_effect=assembly), redirect_stdout(io.StringIO()):
            self.assertEqual(gen.main(["run", "--output", str(self.output), "--execute"]), 0)
        self.assertEqual(order, ["graph", "author", "assemble"])

    @unittest.skipUnless(os.environ.get("AC_GRAPHIFY_UPSTREAM"), "set AC_GRAPHIFY_UPSTREAM for actual pinned-upstream boundary test")
    def test_actual_upstream_one_pass_a_c_aware_creation_and_discovery_custody(self) -> None:
        upstream = Path(os.environ["AC_GRAPHIFY_UPSTREAM"])
        output = self.root / "aware"
        schema_text = json.dumps({"$schema": "https://json-schema.org/draft/2020-12/schema", "type": "object", "properties": {"name": {"type": "string"}}}, indent=2) + "\n"
        (self.corpus / "example.schema.json").write_text(schema_text)
        manifest = gen.load(self.manifest)
        manifest["files"].append({"path": "example.schema.json", "sha256": gen.sha(schema_text.encode()), "bytes": len(schema_text.encode())})
        gen.save(self.manifest, manifest)
        plan = gen.prepare(self.corpus, self.manifest, output, "graphify-ac", upstream, 1000)
        discovery = gen.build_discovery(output, upstream)
        self.assertEqual(discovery["mode"], "graphify-ac")
        self.assertGreater(discovery["counts"]["structural_nodes"], 0)
        self.assertEqual(discovery["counts"]["raw_semantic_nodes"], 0)
        self.assertEqual(discovery["counts"]["raw_semantic_edges"], 0)
        self.assertFalse((output / "actors/extract").exists())
        coverage = gen.load(output / "discovery/coverage.json")
        self.assertEqual(coverage["discovery_profile"], "a_c.graphify.structural-discovery/1")
        self.assertEqual(len(coverage["chunks"]), len(self.chunks))
        self.assertNotIn("attempt", coverage["chunks"][0])
        chunk = gen.load(output / "chunks.json")[0]
        self.assertEqual(len(chunk["segments"]), 2)
        prompt = gen.author_prompt(plan, chunk, output)
        self.assertIn("GRAPHIFY_DISCOVERY_DATA_JSON", prompt)
        self.assertIn("a_c.graphify.source-semantic-extraction/1", prompt)
        self.assertNotIn("You are a graphify extraction subagent", prompt)
        answer = copy.deepcopy(self.answer)
        section = next(segment for segment in chunk["segments"] if segment["path"] == "example.schema.json")
        line = next(index for index, value in enumerate(schema_text.splitlines(), 1) if '"type": "object"' in value)
        answer["concepts"].append({"key": "schema_document", "label": "Example schema", "definition": "A JSON schema describes the permitted object data shape.",
                                   "conditions": [], "exceptions": [], "grounding": [{"section_id": section["id"], "start_line": line, "end_line": line, "quote": '"type": "object"'}]})
        answer["dispositions"].append({"section_id": section["id"], "decision": "retained", "keys": ["schema_document"], "reason": "Describe the JSON schema as source data; do not instantiate its subject."})
        self.fake_attempt("author", answer, output)
        result = gen.assemble(output, upstream=upstream)
        self.assertEqual(result["mode"], "graphify-ac")
        self.assertEqual(result["upstream_trial"]["commit"], gen.UPSTREAM_COMMIT)
        self.assertEqual(result["family_counts"]["constraints"], 1)
        self.assertEqual(result["family_counts"]["judgments"], 0)
        (output / "discovery/structural.json").write_text("tampered")
        with self.assertRaisesRegex(gen.GenerationError, "discovery graph changed"):
            gen.assemble(output, upstream=upstream)

    @unittest.skipUnless(os.environ.get("AC_GRAPHIFY_UPSTREAM"), "set AC_GRAPHIFY_UPSTREAM for actual pinned-upstream boundary test")
    def test_actual_upstream_source_extract_and_generated_model_round_trip(self) -> None:
        upstream = Path(os.environ["AC_GRAPHIFY_UPSTREAM"])
        output = self.root / "graphify"
        gen.prepare(self.corpus, self.manifest, output, "graphify", upstream, 1000)
        path = str((output / "corpus/rules.md").resolve())
        semantic = {"nodes": [{"id": "rules_proceed", "label": "Proceed", "file_type": "concept", "source_file": path, "source_location": "L2", "source_url": None,
                               "captured_at": None, "author": None, "contributor": None, "rationale": "Complete evidence is required."},
                              {"id": "rules_evidence", "label": "Evidence", "file_type": "rationale", "source_file": path, "source_location": "2", "source_url": None,
                               "captured_at": None, "author": None, "contributor": None, "rationale": None}],
                    "edges": [{"source": "rules_proceed", "target": "rules_evidence", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0,
                               "source_file": path, "source_location": "2", "weight": 1.0}], "hyperedges": [], "input_tokens": 0, "output_tokens": 0}
        modules = gen.upstream_modules(upstream)
        gen.semantic_check(semantic, self.chunks[0], output, modules)
        self.fake_attempt("extract", semantic, output)
        discovery = gen.build_discovery(output, upstream)
        self.assertEqual(discovery["counts"]["raw_semantic_nodes"], 2)
        graph = gen.load(output / "discovery/graph.json")
        self.assertTrue(any(node.get("file_type") == "concept" for node in graph["nodes"]))
        self.assertTrue(any(node.get("file_type") == "rationale" for node in graph["nodes"]))
        self.assertTrue(any(node.get("_origin") == "semantic" for node in graph["nodes"]))
        self.fake_attempt("author", self.answer, output)
        result = gen.assemble(output, upstream=upstream)
        self.assertEqual(result["upstream_trial"]["commit"], gen.UPSTREAM_COMMIT)
        self.assertEqual(gen.load(output / "proposal/model.json")["populations"]["judgments"], [])
        (output / "discovery/graph.json").write_text("tampered")
        with self.assertRaisesRegex(gen.GenerationError, "discovery graph changed"):
            gen.assemble(output, upstream=upstream)


if __name__ == "__main__":
    unittest.main()
