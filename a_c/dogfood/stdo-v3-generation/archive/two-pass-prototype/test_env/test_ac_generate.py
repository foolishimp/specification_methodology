"""Meaningful source custody, authoring-boundary and actual-upstream checks.

Authored fixture answers below are test data, not evidence of LLM quality.
Set AC_GRAPHIFY_UPSTREAM to run the real pinned extraction/build/export test.
"""
from __future__ import annotations

import copy
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

    def fake_attempt(self, stage: str, answer: dict, output: Path | None = None) -> Path:
        output = output or self.output
        chunk = gen.load(output / "chunks.json")[0]
        path = output / "actors" / stage / chunk["id"] / "attempt-001"
        path.mkdir(parents=True)
        gen.save(path / "answer.json", answer)
        (path / "prompt.txt").write_text("Test-only fixture, no actor invoked.")
        schema = gen.ASSETS / ("extraction.schema.json" if stage == "extract" else "author.schema.json")
        gen.save(path / "invocation.json", {"prompt_sha256": gen.sha((path / "prompt.txt").read_bytes()), "schema_sha256": gen.sha(schema.read_bytes())})
        gen.save(path / "validation.json", {"answer_sha256": gen.sha((path / "answer.json").read_bytes()), "chunk_sha256": gen.digest(chunk)})
        gen.save(path / "result.json", {"status": "completed"})
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
        with self.assertRaisesRegex(gen.GenerationError, "changed after validation"):
            gen.successful_attempt(self.output, "author", self.chunks[0])

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
        self.fake_attempt("extract", {"test": "only structural failure path used"})
        plan = {**self.plan, "mode": "graphify", "upstream": {"root": "unused"}}
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
        with self.assertRaisesRegex(gen.GenerationError, "different source chunk"):
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
