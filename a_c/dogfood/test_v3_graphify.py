"""Transport counterexamples; semantic acceptance is outside these tests."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest

import v3_graphify as v


class TransportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory(prefix="ac-v3-transport-test-")
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        (root / "input").mkdir()
        self.uri = lambda value: "urn:transport-test:" + value
        self.source = "repo://fixture/standards/source.md"
        self.a, self.b, self.c, self.sym, self.res = [self.uri(k) for k in ("a", "b", "c", "symbol", "residual")]
        self.i, self.j = [self.uri("index:" + k) for k in ("required", "other")]
        role = self.uri("role")
        route_role = self.uri("vocab#acquisition-route")
        def clause(identity, arguments):
            return dict(uri=identity, clause_type="relation", operator=self.uri("operator"),
                        arguments=arguments, statement="Authored " + identity, source_refs=[self.source])
        conditional = dict(acquisition="conditional", target=self.c, target_index=self.j,
                           qualification="only if the separately established domain applies")
        self.program = dict(kind="axiom-indexer.axiomatic-program", schema_version=1,
                            uri=self.uri("program"), calculus_ref=v.ac.CALCULUS_URI, source_basis="repo://fixture/",
                            frame_refs=[self.source + "#selected"], vocabulary_refs=[role, route_role, self.uri("operator"), self.uri("symbol-kind")],
                            symbols=[dict(uri=self.sym, kind=self.uri("symbol-kind"), label="A symbol", source_refs=[self.source])],
                            clauses=[clause(self.a, [dict(role=role, ref=self.b), dict(role=role, ref=self.b),
                                                     dict(role=role, ref=self.sym), dict(role=route_role, literal=json.dumps(conditional))]),
                                     clause(self.b, [dict(role=role, ref=self.a)]), clause(self.c, [])],
                            residuals=[dict(uri=self.res, kind="unknown", subject_refs=[self.a, self.sym],
                                            detail="Unresolved authored question", re_entry_refs=[self.source], source_refs=[self.source])],
                            frame_indexes=[dict(uri=self.i, frame_ref=self.source + "#selected", scope="Required cyclic context",
                                                clause_refs=[self.a], residual_refs=[], source_refs=[self.source]),
                                           dict(uri=self.j, frame_ref=self.source + "#selected", scope="Separate domain",
                                                clause_refs=[self.c], residual_refs=[], source_refs=[self.source])])
        config = dict(tenant="codex", program_path="program.json",
                      source_roots=[dict(uri_prefix="repo://fixture/", path_prefix="")], coverage={})
        manifest = dict(archive=dict(sha256="0" * 64))
        (root / "subject.json").write_bytes(v.pretty(config))
        (root / "input/manifest.json").write_bytes(v.pretty(manifest))
        members = {"program.json": v.pretty(self.program), "standards/source.md": b"# Selected\nLiteral source-only discovery sentence.\n"}
        self.subject = v.Subject(root, config, manifest, members, self.program)
        v.validate_native(self.subject)
        self.model = v.build_model(self.subject)

    def test_full_program_and_empty_populations_round_trip(self):
        recovered = v.ac.decode(v.ac.materialize(self.model))
        self.assertEqual(v.recover_program(recovered), self.program)
        self.assertTrue(v.verify_transport(self.subject, recovered)["all_required_closures_match"])
        self.assertEqual(set(recovered.document["populations"]), set(v.ac.CORE_FIELDS))
        self.assertTrue(all(not value for key, value in recovered.document["populations"].items() if key != "objects"))

    def test_symbols_cycles_parallel_refs_and_multi_subject_residual(self):
        result = v.select(self.subject, self.model, [self.i])
        self.assertEqual(set(result["projection"]["included"]), {self.i, self.a, self.b, self.sym, self.res})
        self.assertEqual(result["native"]["residuals"][0]["subject_refs"], [self.a, self.sym])
        refs = self.model.records[self.a].fields["value"]["required_refs"]
        self.assertEqual(sum(edge["target"] == self.b for edge in refs), 2)

    def test_conditional_route_and_source_do_not_become_required(self):
        result = v.select(self.subject, self.model, [self.i])
        self.assertNotIn(self.c, result["projection"]["included"])
        self.assertNotIn(self.j, result["projection"]["included"])
        self.assertNotIn(self.subject.source_id("standards/source.md"), result["projection"]["included"])
        self.assertEqual(len(result["acquisition_routes"]), 1)
        self.assertIn("separately established domain", result["acquisition_routes"][0]["payload"])

    def test_explicit_combined_selection_adds_the_domain(self):
        result = v.select(self.subject, self.model, [self.i, self.j])
        self.assertEqual(set(result["projection"]["included"]), {self.i, self.j, self.a, self.b, self.c, self.sym, self.res})

    def test_budget_refuses_without_truncating(self):
        with self.assertRaisesRegex(v.ac.Refusal, "budget"):
            v.select(self.subject, self.model, [self.i], 4)
        self.assertEqual(len(v.select(self.subject, self.model, [self.i], 5)["projection"]["included"]), 5)
        with self.assertRaises(v.ac.Refusal):
            v.select(self.subject, self.model, [self.i], -1)

    def test_source_discovery_is_available_without_added_coverage(self):
        found = v.ac.find(self.model, "source-only discovery")
        self.assertEqual([row["id"] for row in found["matches"]], [self.subject.source_id("standards/source.md")])
        self.assertEqual(self.subject.source_path(self.source + "#selected"), "standards/source.md")
        with self.assertRaises(v.ac.Refusal):
            self.subject.source_path("repo://fixture/%2e%2e/outside")

    def test_payload_tamper_refuses_even_when_generic_model_is_valid(self):
        raw = copy.deepcopy(self.model.document)
        record = next(row for row in raw["populations"]["objects"] if row["id"] == self.a)
        record["value"]["native_json"] = record["value"]["native_json"].replace("Authored ", "Altered ")
        with self.assertRaisesRegex(v.ac.Refusal, "round trip"):
            v.verify_transport(self.subject, v.ac.validate(raw))

    def test_ref_edge_tamper_cannot_hide_in_unchanged_native_json(self):
        raw = copy.deepcopy(self.model.document)
        record = next(row for row in raw["populations"]["objects"] if row["id"] == self.a)
        record["value"]["required_refs"][0]["target"] = self.c
        with self.assertRaisesRegex(v.ac.Refusal, "occurrences"):
            v.verify_transport(self.subject, v.ac.validate(raw))

    def test_ordinal_collision_refuses(self):
        raw = copy.deepcopy(self.model.document)
        record = next(row for row in raw["populations"]["objects"] if row["id"] == self.b)
        record["value"]["ordinal"] = 0
        with self.assertRaisesRegex(v.ac.Refusal, "ordinal"):
            v.recover_program(v.ac.validate(raw))

    def test_source_payload_tamper_refuses(self):
        raw = copy.deepcopy(self.model.document)
        record = next(row for row in raw["populations"]["objects"] if row["value"]["native_family"] == "source_members")
        record["value"]["a_text"] += " invented rule"
        with self.assertRaisesRegex(v.ac.Refusal, "source content"):
            v.verify_transport(self.subject, v.ac.validate(raw))

    def test_missing_reference_and_wrong_selector_kind_refuse(self):
        invalid = copy.deepcopy(self.program)
        invalid["clauses"][0]["arguments"][0]["ref"] = self.uri("missing")
        bad = v.Subject(self.subject.root, self.subject.config, self.subject.manifest, self.subject.members, invalid)
        with self.assertRaisesRegex(v.ac.Refusal, "unresolved"):
            v.validate_native(bad)
        invalid = copy.deepcopy(self.program)
        invalid["frame_indexes"][0]["clause_refs"] = [self.sym]
        bad = v.Subject(self.subject.root, self.subject.config, self.subject.manifest, self.subject.members, invalid)
        with self.assertRaisesRegex(v.ac.Refusal, "root kind"):
            v.validate_native(bad)

    def test_duplicate_unknown_selectors_refuse(self):
        for names in ([self.i, self.i], ["missing"], [self.a]):
            with self.assertRaises(v.ac.Refusal):
                v.select(self.subject, self.model, names)

    def test_both_native_selector_prefixes_support_exact_short_names(self):
        self.assertEqual(v.choose_selectors(self.program, ["required"])[0]["uri"], self.i)
        other = copy.deepcopy(self.program)
        other["frame_indexes"][0]["uri"] = self.uri("frame-index:required")
        self.assertEqual(v.choose_selectors(other, ["required"])[0]["uri"], self.uri("frame-index:required"))

    def test_output_protection_and_idempotence(self):
        protected = self.subject.root / "input"
        with self.assertRaises(v.ac.Refusal):
            v.emit(protected / "new.json", b"no", [protected])
        target = self.subject.root / "new.json"
        v.emit(target, b"same")
        v.emit(target, b"same")
        with self.assertRaises(v.ac.Refusal):
            v.emit(target, b"different")
        alias = self.subject.root / "alias"
        alias.hardlink_to(self.subject.root / "subject.json")
        with self.assertRaisesRegex(v.ac.Refusal, "hardlink"):
            v.emit(alias, b"different", [self.subject.root / "subject.json"])


class FrozenInputTests(unittest.TestCase):
    def test_both_exact_inputs_and_current_counts(self):
        for tenant, expected in (("codex", (0, 712, 5, 732)), ("claude", (39, 155, 0, 5))):
            with self.subTest(tenant=tenant):
                subject = v.load_subject(tenant)
                self.assertEqual(tuple(len(subject.program[k]) for k in v.FAMILIES), expected)

    def test_frozen_archive_drift_refuses(self):
        with tempfile.TemporaryDirectory(prefix="ac-v3-input-drift-") as tmp:
            root = Path(tmp)
            source = v.HERE / "stdo-v3-i5-claude"
            shutil.copytree(source / "input", root / "input")
            shutil.copyfile(source / "subject.json", root / "subject.json")
            archive = root / "input/candidate.tar.gz"
            raw = bytearray(archive.read_bytes())
            raw[-1] ^= 1
            archive.write_bytes(raw)
            with self.assertRaisesRegex(v.ac.Refusal, "archive drift"):
                v.load_subject("claude", root)

    def test_frozen_manifest_drift_refuses(self):
        with tempfile.TemporaryDirectory(prefix="ac-v3-manifest-drift-") as tmp:
            root = Path(tmp)
            source = v.HERE / "stdo-v3-i5-claude"
            shutil.copytree(source / "input", root / "input")
            shutil.copyfile(source / "subject.json", root / "subject.json")
            path = root / "input/manifest.json"
            path.write_bytes(path.read_bytes() + b" ")
            with self.assertRaisesRegex(v.ac.Refusal, "manifest drift"):
                v.load_subject("claude", root)


if __name__ == "__main__":
    unittest.main()
