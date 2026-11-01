"""Code-overlay custody and negative controls; fixture mappings are not F_P evidence."""
from __future__ import annotations

import copy
import builtins
from contextlib import redirect_stderr, redirect_stdout
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))
import ac_code as code
import ac_explore
import ac_generate as gen
import ac_graph
from test_ac_generate import SOURCE, fixture_answer

UPSTREAM = os.environ.get("AC_GRAPHIFY_UPSTREAM")
PYTHON = ('raise RuntimeError("subject must never execute")\n'
          'def require_evidence(complete):\n'
          '    if not complete:\n'
          '        raise ValueError("incomplete")\n'
          '    return True\n')
TEST = ('import { requireEvidence } from "../src/evidence.ts";\n'
        'function testEvidence() { return requireEvidence(true); }\n'
        'throw new Error("test source must never execute");\n')
TYPESCRIPT = ('export function requireEvidence(complete: boolean): boolean {\n'
              '  if (!complete) throw new Error("incomplete");\n'
              '  return true;\n'
              '}\n')


class NormalizationTests(unittest.TestCase):
    def test_parallel_self_missing_and_ambiguous_are_retained(self):
        root = Path("/selected")
        raw = {"nodes": [{"id": "a", "label": "A", "type": "function", "source_file": "x.py", "source_location": "L1"},
                         {"id": "a", "label": "A second occurrence", "type": "function", "source_file": "x.py", "source_location": "L2"},
                         {"id": "b", "label": "B", "type": "function", "source_file": "x.py", "source_location": "L3"}],
               "edges": [{"source": "b", "target": "b", "relation": "calls", "confidence_score": 0.875},
                         {"source": "b", "target": "b", "relation": "calls", "confidence_score": 0.5},
                         {"source": "b", "target": "missing", "relation": "calls"},
                         {"source": "b", "target": "a", "relation": "calls"}]}
        before = copy.deepcopy(raw)
        result = code.normalize(raw, root, [{"path": "x.py", "role": "code"}],
                                {"x.py": "def a(): pass\ndef a(): pass\ndef b(): pass\n"}, "test")
        self.assertEqual(raw, before)
        self.assertEqual(len(result["links"]), 4)
        self.assertEqual(len({link["id"] for link in result["links"]}), 4)
        self.assertEqual(result["links"][0]["source"], result["links"][0]["target"])
        ambiguous = [node for node in result["nodes"] if node["record"].get("reason") == "multiple raw identity occurrences"]
        self.assertEqual(len(ambiguous), 1)
        self.assertEqual(len(ambiguous[0]["record"]["candidates"]), 2)
        self.assertEqual(result["links"][3]["target"], ambiguous[0]["id"])
        self.assertEqual(json.loads(result["links"][0]["detail"]["raw_extraction_json"])["confidence_score"], 0.875)
        def floats(value):
            if isinstance(value, float):
                return True
            if isinstance(value, dict):
                return any(floats(item) for item in value.values())
            return isinstance(value, list) and any(floats(item) for item in value)
        self.assertFalse(floats(result))

    def test_outside_missing_and_invalid_locations_do_not_get_fabricated_ranges(self):
        nodes = [{"id": str(index), "type": "function", "source_file": source, "source_location": location}
                 for index, (source, location) in enumerate((("../secret.py", "L1"), ("x.py", "L99"),
                                                            ("x.py", None), ("/outside.py", "L1")))]
        result = code.normalize({"nodes": nodes, "edges": []}, Path("/selected"),
                                [{"path": "x.py", "role": "code"}], {"x.py": "def x(): pass\n"}, "test")
        self.assertTrue(all(node["family"] == "code_external" and node["record"]["grounding"] == [] for node in result["nodes"]))
        self.assertEqual(result["coverage"]["files_without_grounded_nodes"], ["x.py"])


@unittest.skipUnless(UPSTREAM, "select the pinned real Graphify checkout with AC_GRAPHIFY_UPSTREAM")
class CodeOverlayTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="ac-code-tests-")
        self.root = Path(self.tmp.name).resolve()
        self.project = self.root / "project"
        (self.project / "specification").mkdir(parents=True)
        (self.project / "src").mkdir()
        (self.project / "tests").mkdir()
        (self.project / "specification/rules.md").write_text(SOURCE)
        (self.project / "src/evidence.py").write_text(PYTHON)
        (self.project / "src/evidence.ts").write_text(TYPESCRIPT)
        (self.project / "tests/evidence.test.mjs").write_text(TEST)
        self.manifest = self.root / "manifest.json"
        gen.save(self.manifest, {"profile": "ac.generation.corpus/1", "subject_id": "urn:example:code-overlay-test",
                                 "files": [{"path": "specification/rules.md", "sha256": gen.sha(SOURCE.encode()),
                                            "bytes": len(SOURCE.encode()), "git_blob": "ancillary-custody"}]})
        generation = self.root / "base-generation"
        plan = gen.prepare(self.project, self.manifest, generation, "direct", None)
        chunks = gen.load(generation / "chunks.json")
        answers = {chunk["id"]: fixture_answer(chunk) for chunk in chunks}
        model, _ = gen.model_from_answers(plan, chunks, answers, [{"author": "synthetic test data"}])
        self.model = self.root / "model.json"
        gen.save(self.model, model)
        self.base = model
        self.run = self.root / "run"
        self.mapping = self.root / "mapping.json"
        self.upstream = Path(UPSTREAM).resolve()

    def tearDown(self):
        self.tmp.cleanup()

    def prepare(self, **changes):
        args = dict(root=self.project, model=self.model, manifest=self.manifest, source_root=self.project,
                    output=self.run, code=["src"], tests=["tests"], upstream=self.upstream)
        args.update(changes)
        return code.prepare(**args)

    def mapping_value(self):
        task = code.task(self.run)
        result = copy.deepcopy(task["template"])
        requirement = next(record for record in task["base_records"] if record["family"] == "constraints")
        implementation = next(node for node in task["code_entities"] if node["family"] == "code"
                              and node["label"] == "requireEvidence()")
        test = next(node for node in task["code_entities"] if node["family"] == "test" and node["label"] == "testEvidence()")
        source_ground = next(ac_explore.groundings(requirement["record"]))
        source_ground = {key: source_ground[key] for key in ("path", "start_line", "end_line", "quote")}
        result["links"] = [
            {"id": "implementation", "kind": "proposed_realization", "source": requirement["id"], "target": implementation["id"],
             "rationale": "Synthetic mapping of the availability condition to the function guard.", "conditions": [],
             "limitations": ["Fixture assertion; no semantic acceptance."],
             "grounding": [source_ground, *implementation["record"]["grounding"]]},
            {"id": "test", "kind": "test_source_for", "source": implementation["id"], "target": test["id"],
             "rationale": "The selected test source calls the selected function.", "conditions": [],
             "limitations": ["No test execution or coverage result."],
             "grounding": [*implementation["record"]["grounding"], *test["record"]["grounding"]]},
        ]
        result["unresolved"] = [{"subject": requirement["id"], "reason": "The external policy remains unresolved."}]
        return result

    def complete(self):
        self.prepare()
        gen.save(self.mapping, self.mapping_value())
        return code.build(self.run, self.mapping, "synthetic-fixture-author")

    def cli(self, *args):
        result = subprocess.run([sys.executable, "-B", str(code.HERE / "ac_code.py"), *map(str, args)],
                                capture_output=True, text=True, timeout=60)
        payload = json.loads(result.stdout if result.returncode == 0 else result.stderr)
        return result, payload

    def test_actual_python_typescript_and_mjs_full_path_preserves_base(self):
        original = self.model.read_bytes()
        result = self.complete()
        self.assertEqual(result["status"], "built")
        self.assertEqual(self.model.read_bytes(), original)
        self.assertEqual(code.status(self.run)["status"], "built")
        self.assertEqual(code.build(self.run, self.mapping, "synthetic-fixture-author")["status"], "reused")
        data = gen.load(self.run / "built/view-data.json")
        expected = ac_explore.view_data(self.base, self.project)
        for field in ("model", "basis", "interpretation", "counts"):
            self.assertEqual(data[field], expected[field])
        self.assertEqual(data["nodes"][:len(expected["nodes"])], expected["nodes"])
        self.assertEqual(data["links"][:len(expected["links"])], expected["links"])
        self.assertEqual(data["focus"], self.mapping_value()["links"][0]["source"])
        self.assertEqual(data["code_overlay"]["counts"]["trace_links"], 2)
        self.assertIn("not an executed test result", data["code_overlay"]["standing"]["trace"])
        if os.environ.get("AC_CODE_READER_FIXTURE"):
            path = Path(os.environ["AC_CODE_READER_FIXTURE"])
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(self.run / "built/explorer.html", path)
            gen.save(path.with_suffix(".json"), data)

    def test_public_cli_and_formal_mode_refusal_before_input_acquisition(self):
        process, result = self.cli("prepare", "--project", self.project, "--model", self.model,
                                   "--manifest", self.manifest, "--source-root", self.project,
                                   "--code", "src", "--test", "tests", "--upstream", self.upstream, "--out", self.run)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(result["status"], "prepared")
        process, task = self.cli("task", "--run", self.run)
        self.assertEqual(process.returncode, 0, process.stderr)
        gen.save(self.mapping, self.mapping_value())
        process, result = self.cli("build", "--run", self.run, "--mapping", self.mapping, "--author", "CLI fixture")
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(result["status"], "built")
        process, result = self.cli("status", "--run", self.run)
        self.assertEqual(process.returncode, 0, process.stderr)
        process, result = self.cli("prepare", "--project", "missing", "--model", "missing", "--manifest", "missing",
                                   "--source-root", "missing", "--code", "missing", "--upstream", "missing",
                                   "--out", self.root / "forbidden", "--formal-checker", "missing")
        self.assertEqual(process.returncode, 2)
        self.assertIn("formal-checker mode is unsupported", result["reason"])
        self.assertFalse((self.root / "forbidden").exists())

    def test_base_drift_before_prepare_and_current_reuse_refuse(self):
        self.complete()
        (self.project / "specification/rules.md").write_text(SOURCE + "Changed.\n")
        with self.assertRaisesRegex(gen.GenerationError, "base corpus changed"):
            code.status(self.run)
        other = self.root / "other"
        with self.assertRaisesRegex(gen.GenerationError, "base corpus changed"):
            self.prepare(output=other)
        self.assertFalse(other.exists())

    def test_frozen_corpus_cannot_hide_live_project_drift(self):
        corpus = self.root / "historical"
        (corpus / "specification").mkdir(parents=True)
        (corpus / "specification/rules.md").write_text(SOURCE)
        (self.project / "specification/rules.md").write_text(SOURCE + "Changed.\n")
        with self.assertRaisesRegex(gen.GenerationError, "nominated project base source changed"):
            self.prepare(source_root=corpus)
        self.assertFalse(self.run.exists())

    def test_manifest_subject_file_identity_and_model_grounding_refuse(self):
        manifest = gen.load(self.manifest)
        manifest["subject_id"] = "urn:other"
        gen.save(self.manifest, manifest)
        with self.assertRaisesRegex(gen.GenerationError, "subject differs"):
            self.prepare()
        manifest["subject_id"] = self.base["basis"]["subject"]["id"]
        gen.save(self.manifest, manifest)
        changed = copy.deepcopy(self.base)
        changed["populations"]["objects"][0]["value"]["grounding"][0]["quote"] = "fabricated"
        gen.save(self.model, changed)
        with self.assertRaisesRegex(gen.GenerationError, "quote is not exact"):
            self.prepare()

    def test_public_path_preserves_terminal_lf_grounding_without_quote_normalization(self):
        changed = copy.deepcopy(self.base)
        changed["populations"]["objects"][0]["value"]["grounding"][0]["quote"] += "\n"
        gen.save(self.model, changed)
        self.base = changed
        process, prepared = self.cli("prepare", "--project", self.project, "--model", self.model,
                                    "--manifest", self.manifest, "--source-root", self.project,
                                    "--code", "src", "--test", "tests", "--upstream", self.upstream, "--out", self.run)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(prepared["status"], "prepared")
        mapping = json.loads(json.dumps(self.mapping_value()))
        for link in mapping["links"]:
            for grounding in link["grounding"]:
                grounding["quote"] += "\n"
        incorrect = copy.deepcopy(mapping)
        incorrect["links"][0]["grounding"][0]["quote"] += "\n"
        gen.save(self.mapping, incorrect)
        process, refused = self.cli("build", "--run", self.run, "--mapping", self.mapping, "--author", "LF fixture")
        self.assertEqual(process.returncode, 2)
        self.assertIn("quote is not exact source", refused["reason"])
        self.assertFalse((self.run / "built").exists())
        gen.save(self.mapping, mapping)
        process, built = self.cli("build", "--run", self.run, "--mapping", self.mapping, "--author", "LF fixture")
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(built["status"], "built")
        retained = gen.load(self.run / "built/overlay.json")
        self.assertEqual(retained["mapping"], mapping)
        self.assertEqual(gen.load(self.run / "base/model.json"), changed)

    def test_live_code_and_directory_membership_changes_refuse(self):
        self.prepare()
        source = self.project / "src/evidence.py"
        source.write_text(PYTHON + "# change\n")
        with self.assertRaisesRegex(gen.GenerationError, "code/test source or membership changed"):
            code.task(self.run)
        source.write_text(PYTHON)
        (self.project / "src/extra.py").write_text("def extra(): pass\n")
        with self.assertRaisesRegex(gen.GenerationError, "membership changed"):
            code.status(self.run)

    def test_unsupported_redirect_escape_role_conflict_and_overlap_refuse(self):
        (self.project / "src/notes.txt").write_text("not code")
        with self.assertRaisesRegex(gen.GenerationError, "unsupported selected code"):
            self.prepare()
        self.assertFalse(self.run.exists())
        (self.project / "src/notes.txt").unlink()
        with self.assertRaisesRegex(gen.GenerationError, "escapes"):
            self.prepare(code=["../outside.py"])
        (self.project / "alias.py").symlink_to(self.project / "src/evidence.py")
        with self.assertRaisesRegex(gen.GenerationError, "symlink"):
            self.prepare(code=["alias.py"])
        with self.assertRaisesRegex(gen.GenerationError, "both code and test"):
            self.prepare(tests=["src/evidence.py"])
        with self.assertRaisesRegex(gen.GenerationError, "overlap|inside selected"):
            self.prepare(output=self.project / "src/output")

    def test_unknown_trace_false_quote_range_and_wrong_role_refuse_without_output(self):
        self.prepare()
        original = self.mapping_value()
        mutants = []
        changed = copy.deepcopy(original); changed["links"][0]["target"] = "urn:unknown"; mutants.append(changed)
        changed = copy.deepcopy(original); changed["links"][0]["grounding"][0]["quote"] = "fabricated"; mutants.append(changed)
        changed = copy.deepcopy(original); changed["links"][0]["grounding"][0]["end_line"] = 999; mutants.append(changed)
        changed = copy.deepcopy(original); changed["links"][0]["target"] = changed["links"][1]["target"]; mutants.append(changed)
        changed = copy.deepcopy(original); changed["links"][0]["grounding"] = changed["links"][0]["grounding"][:1]; mutants.append(changed)
        changed = copy.deepcopy(original); changed["base_model_sha256"] = "0" * 64; mutants.append(changed)
        changed = copy.deepcopy(original); changed["links"][1]["id"] = changed["links"][0]["id"]; mutants.append(changed)
        changed = copy.deepcopy(original); changed["links"][0]["accepted"] = True; mutants.append(changed)
        for value in mutants:
            with self.subTest(value=value):
                gen.save(self.mapping, value)
                with self.assertRaises(gen.GenerationError):
                    code.build(self.run, self.mapping, "fixture")
                self.assertFalse((self.run / "built").exists())

    def test_mapping_live_bytes_author_and_frozen_mapping_invalidate(self):
        self.complete()
        original = self.mapping.read_bytes()
        self.mapping.write_bytes(original + b"\n")
        with self.assertRaisesRegex(gen.GenerationError, "mapping changed"):
            code.status(self.run)
        self.mapping.write_bytes(original)
        with self.assertRaisesRegex(gen.GenerationError, "mapping or author selection changed"):
            code.build(self.run, self.mapping, "changed author")
        (self.run / "built/mapping.json").write_bytes(original + b"\n")
        with self.assertRaisesRegex(gen.GenerationError, "mapping changed"):
            code.status(self.run)

    def test_changed_machinery_refuses_current_result(self):
        self.complete()
        with patch.object(code, "machinery", return_value={"changed": "fixture"}):
            with self.assertRaisesRegex(gen.GenerationError, "machinery changed"):
                code.status(self.run)

    def test_malformed_mapping_types_have_public_json_refusals(self):
        self.prepare()
        valid = self.mapping_value()
        values = [[], None, {**valid, "links": None}, {**valid, "unresolved": [{"subject": [], "reason": "bad"}]}]
        for field, value in (("start_line", True), ("end_line", -1), ("quote", 42), ("path", [])):
            changed = copy.deepcopy(valid)
            changed["links"][0]["grounding"][0][field] = value
            values.append(changed)
        for value in values:
            with self.subTest(value=value):
                gen.save(self.mapping, value)
                out, err = io.StringIO(), io.StringIO()
                with redirect_stdout(out), redirect_stderr(err):
                    result = code.main(["build", "--run", str(self.run), "--mapping", str(self.mapping), "--author", "fixture"])
                self.assertEqual(result, 2)
                self.assertEqual(json.loads(err.getvalue())["status"], "refused")
                self.assertEqual(out.getvalue(), "")
                self.assertFalse((self.run / "built").exists())

    def test_built_directory_symlink_is_refused_before_readback(self):
        self.complete()
        elsewhere = self.root / "elsewhere"
        (self.run / "built").rename(elsewhere)
        (self.run / "built").symlink_to(elsewhere, target_is_directory=True)
        with self.assertRaisesRegex(gen.GenerationError, "redirected retained artifact"):
            code.status(self.run)

    def test_extraction_diagnostics_remain_visible_in_exported_reader_data(self):
        modules = gen.upstream_modules(self.upstream)
        extract = modules["extract"].extract
        def diagnostic_extract(*args, **kwargs):
            print("Explicit fixture: partial parse warning for selected source", file=sys.stderr)
            return extract(*args, **kwargs)
        with patch.object(modules["extract"], "extract", side_effect=diagnostic_extract):
            self.prepare()
        gen.save(self.mapping, code.task(self.run)["template"])
        result = code.build(self.run, self.mapping, "fixture")
        data = gen.load(Path(result["artifacts"]["view_data"]))
        self.assertIn("partial parse warning", data["code_overlay"]["coverage"]["extractor_diagnostics"])
        self.assertEqual(data["code_overlay"]["coverage"]["raw_edges"], len(gen.load(self.run / "structural.json")["edges"]))

    def test_actual_ambient_tsconfig_extends_and_package_metadata_are_unavailable(self):
        (self.project / "src/evidence.ts").write_text(
            'import { hidden } from "@outside";\nimport { other } from "#private";\n'
            'export function requireEvidence(complete: boolean) { return hidden(complete) + other(); }\n')
        config = self.root / "tsconfig.json"
        extended = self.root / "external-config.json"
        package = self.root / "package.json"
        outside = self.root / "not-selected.ts"
        config.write_text('{"extends":"./external-config.json"}')
        extended.write_text('{"compilerOptions":{"paths":{"@outside":["./not-selected.ts"]}}}')
        package.write_text('{"workspaces":["packages/*"],"imports":{"#private":"./not-selected.ts"}}')
        outside.write_text('export function hidden(v) { return v; }\nexport function other() { return 1; }\n')
        watched = {config, extended, package, outside}
        reads, metadata = [], []
        original_read, original_stat = Path.read_text, os.stat
        def read_spy(path, *args, **kwargs):
            if path in watched:
                reads.append(str(path))
            return original_read(path, *args, **kwargs)
        def stat_spy(path, *args, **kwargs):
            if not isinstance(path, int) and Path(path) in watched:
                metadata.append(str(path))
            return original_stat(path, *args, **kwargs)
        with patch.object(Path, "read_text", read_spy), patch.object(os, "stat", stat_spy):
            self.prepare()
        self.assertEqual(reads, [])
        self.assertEqual(metadata, [])
        acquisition = gen.load(self.run / "ACQUISITION.json")
        self.assertEqual(acquisition["denied_content_attempts"], [])
        self.assertIn(str(config), acquisition["outside_metadata_paths"])
        first = gen.load(self.run / "structural.json")
        self.assertFalse(any(str(outside) in json.dumps(item) for item in first["nodes"] + first["edges"]))
        extended.write_text('{"compilerOptions":{"paths":{"@outside":["./different.ts"]}}}')
        package.write_text('{"imports":{"#private":"./different.ts"}}')
        self.assertEqual(code.status(self.run)["status"], "mapping_required")
        second = self.root / "second"
        self.prepare(output=second)
        raw = gen.load(second / "structural.json")
        self.assertEqual((first["nodes"], first["edges"]), (raw["nodes"], raw["edges"]))

    def test_python_parent_package_metadata_does_not_change_guarded_extraction(self):
        selected = self.root / "acme/selected"
        selected.mkdir(parents=True)
        app, helper = selected / "app.py", selected / "helper.py"
        app.write_text('from acme.selected.helper import value\ndef run(): return value()\n')
        helper.write_text('def value(): return 1\n')
        modules = gen.upstream_modules(self.upstream)
        modules["extract"]._check_tree_sitter_version()
        __import__("tree_sitter_python")
        __import__("graphify.cache", fromlist=["x"])._grammar_fingerprint()
        def extract():
            with tempfile.TemporaryDirectory(dir=self.root) as folder:
                with code.extraction_boundary([app, helper], selected, Path(folder)) as observed:
                    raw = modules["extract"].extract([app, helper], root=selected, cache_root=Path(folder), parallel=False)
                self.assertEqual(observed["denied_content_attempts"], [])
                return raw
        first = extract()
        marker = selected.parent / "__init__.py"
        marker.write_text("")
        seen = []
        original_stat = os.stat
        def stat_spy(path, *args, **kwargs):
            if not isinstance(path, int) and Path(path) == marker:
                seen.append(str(path))
            return original_stat(path, *args, **kwargs)
        with patch.object(os, "stat", stat_spy):
            second = extract()
        self.assertEqual(seen, [])
        self.assertEqual((first["nodes"], first["edges"]), (second["nodes"], second["edges"]))

    def test_extraction_guard_blocks_cached_open_aliases_and_restores_on_failure(self):
        selected = self.project / "src/evidence.py"
        original = (os.stat, os.lstat, os.scandir, os.listdir, builtins.open, io.open, os.open, Path.resolve)
        outside = self.root / "not-selected.txt"
        outside.write_text("secret fixture")
        cached_open = io.open
        with tempfile.TemporaryDirectory(dir=self.root) as folder:
            with self.assertRaises(PermissionError):
                with code.extraction_boundary([selected], selected.parent, Path(folder)) as observed:
                    self.assertFalse(outside.exists())
                    with cached_open(outside):
                        self.fail("outside content reached")
        self.assertEqual(original, (os.stat, os.lstat, os.scandir, os.listdir, builtins.open, io.open, os.open, Path.resolve))
        self.assertIsNone(code._ACTIVE_EXTRACTION)
        self.assertEqual(observed["denied_content_attempts"], [{"path": str(outside), "operation": "read"}])
        self.assertEqual(outside.read_text(), "secret fixture")

    def test_tampered_missing_extra_artifact_and_resealed_incorrect_view_refuse(self):
        self.complete()
        page = self.run / "built/explorer.html"
        raw = page.read_bytes()
        page.write_bytes(raw + b"tamper")
        with self.assertRaisesRegex(gen.GenerationError, "artifact inventory or bytes changed"):
            code.status(self.run)
        page.unlink()
        with self.assertRaisesRegex(gen.GenerationError, "artifact inventory or bytes changed"):
            code.status(self.run)
        page.write_bytes(raw)
        extra = self.run / "built/extra.txt"; extra.write_text("extra")
        with self.assertRaisesRegex(gen.GenerationError, "artifact inventory or bytes changed"):
            code.status(self.run)
        extra.unlink()
        data = gen.load(self.run / "built/view-data.json")
        data["code_overlay"]["standing"]["formal"] = "proved"
        gen.save(self.run / "built/view-data.json", data)
        result = gen.load(self.run / "BUILD.json")
        result["files"] = code.inventory(self.run / "built")
        gen.save(self.run / "BUILD.json", result)
        with self.assertRaisesRegex(gen.GenerationError, "representation no longer corresponds"):
            code.status(self.run)

    def test_frozen_input_changed_refuses(self):
        self.prepare()
        (self.run / "code/src/evidence.py").write_text("changed")
        with self.assertRaisesRegex(gen.GenerationError, "frozen preparation artifacts changed"):
            code.status(self.run)

    def test_partial_build_is_preserved_and_does_not_complete(self):
        self.prepare()
        gen.save(self.mapping, self.mapping_value())
        (self.run / "built").mkdir()
        (self.run / "built/partial.txt").write_text("retained")
        with self.assertRaisesRegex(gen.GenerationError, "partial build"):
            code.build(self.run, self.mapping, "fixture")
        self.assertFalse((self.run / "BUILD.json").exists())
        self.assertEqual((self.run / "built/partial.txt").read_text(), "retained")

    def test_raw_failure_retained_without_completed_preparation(self):
        modules = gen.upstream_modules(self.upstream)
        failure = {"nodes": [], "edges": [], "failed_sources": ["src/evidence.py"], "extracted_sources": []}
        with patch.object(modules["extract"], "extract", return_value=failure):
            with self.assertRaisesRegex(gen.GenerationError, "extraction failed"):
                self.prepare()
        self.assertEqual(gen.load(self.run / "structural.json"), failure)
        self.assertFalse((self.run / "PREPARE.json").exists())
        self.assertEqual(gen.load(self.run / "FAILURE.json")["status"], "incomplete")
        with self.assertRaisesRegex(gen.GenerationError, "preparation incomplete"):
            code.status(self.run)

    def test_unmapped_view_retains_explicit_absence_and_unknown_task_refuses(self):
        self.prepare()
        task = code.task(self.run)
        gen.save(self.mapping, task["template"])
        result = code.build(self.run, self.mapping, "empty fixture mapping")
        data = gen.load(Path(result["artifacts"]["view_data"]))
        self.assertEqual(data["code_overlay"]["counts"]["trace_links"], 0)
        self.assertEqual(data["focus"], ac_explore.view_data(self.base)["focus"])
        with self.assertRaisesRegex(gen.GenerationError, "unknown or repeated"):
            code.task(self.run, ["urn:unknown"])


if __name__ == "__main__":
    unittest.main()
