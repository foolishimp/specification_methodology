"""Counterexamples over the actual frozen V3 I3 corpus and its generated carrier."""
from __future__ import annotations

import copy
from pathlib import Path
import tempfile
import unittest

import representation as r
import ac_graph as ac
from ac_graph import Object


class FrozenV3TransportTests(unittest.TestCase):
    subject: r.NativeSubject
    model: ac.Model
    carrier: ac.GraphCarrier
    files: dict[str, bytes]
    manifest: Object

    @classmethod
    def setUpClass(cls) -> None:
        cls.subject = r.load_frozen()
        cls.model = r.build_model(cls.subject)
        cls.carrier = ac.materialize(cls.model)
        cls.files, cls.manifest = r.artifact_bundle(cls.subject, cls.model, cls.carrier)

    def test_complete_input_custody_and_source_pins(self) -> None:
        self.assertEqual(len(self.subject.members), 89)
        self.assertEqual(len(ac.seq(self.subject.inventory["document_members"], "inventory")), 80)
        self.assertEqual(self.subject.pin_counts, {"owner_body_pins": 701, "source_block_pins": 3476})

    def test_program_and_generic_graph_round_trip(self) -> None:
        recovered = ac.decode(self.carrier)
        self.assertEqual(recovered.document, self.model.document)
        self.assertEqual(r.recover_program(recovered), self.subject.program)
        self.assertNotEqual(r.sha_bytes(self.subject.members[r.PROGRAM_FILE]), ac.digest(self.subject.program))
        self.assertNotIn("ac_evidence", self.carrier.document)

    def test_lawful_empty_populations_do_not_invent_authority(self) -> None:
        populations = ac.obj(self.model.document["populations"], "populations")
        self.assertEqual(set(populations), set(ac.CORE_FIELDS))
        for family in ("relations", "constraints", "latitude", "traversals", "transformations", "judgments"):
            self.assertEqual(populations[family], [])
        self.assertEqual(len(ac.seq(populations["objects"], "objects")), 1431)
        self.assertEqual(len(ac.seq(populations["residuals"], "residuals")), 2)

    def test_all_original_selectors_match_independent_native_reference_closure(self) -> None:
        result = r.compare_selectors(self.subject, self.model)
        self.assertEqual(result["selectors_compared"], 725)
        self.assertEqual(result["required_clause_closure"], {"min": 6, "median": 18, "max": 131})

    def test_reference_roles_pointers_ordinals_and_multiplicity_survive(self) -> None:
        count = 0
        repeated = False
        for native in r.objects(self.subject.program["clauses"], "clauses"):
            record = self.model.records[r.text(native["uri"], "uri")]
            value = ac.obj(record.fields["value"], "value")
            expected = r.required_pairs(native)
            self.assertEqual(value["required_refs"], expected)
            targets = [row["target"] for row in expected]
            repeated = repeated or len(set(r.text(t, "target") for t in targets)) < len(targets)
            count += len(expected)
        self.assertEqual(count, 7741)
        self.assertTrue(repeated)
        required = [ref for ref in self.model.references if ref.path[:2] == ("value", "required_refs")]
        self.assertEqual(len(required), 7741)
        self.assertTrue(all(ref.schema["governing"] is True for ref in required))

    def test_inline_contracts_stay_at_uses_without_synthetic_global_owners(self) -> None:
        inline: set[str] = set()
        occurrences = 0
        for clause in r.objects(self.subject.program["clauses"], "clauses"):
            for argument in r.objects(clause["arguments"], "arguments"):
                if argument["role"] == r.VOCABULARY + "inlined-contract":
                    payload = r.parse(r.text(argument["literal"], "literal"), "inline")
                    inline.add(r.text(payload["identity"], "inline/identity"))
                    occurrences += 1
        self.assertEqual(occurrences, 410)
        self.assertEqual(len(inline), 33)
        self.assertFalse(inline.intersection(self.model.records))
        self.assertEqual(len(ac.obj(self.subject.account["semantic_contracts"], "contracts")), 37)

    def test_route_references_are_non_governing_and_keep_exact_payloads(self) -> None:
        refs = [ref for ref in self.model.references if ref.path[:2] == ("value", "routes")]
        self.assertEqual(len(refs), 4152)
        self.assertTrue(all(ref.schema["governing"] is False for ref in refs))
        for clause in r.objects(self.subject.program["clauses"], "clauses"):
            value = ac.obj(self.model.records[r.text(clause["uri"], "uri")].fields["value"], "value")
            self.assertEqual(value["routes"], r.route_occurrences(clause))

    def test_conditional_and_provenance_targets_are_not_promoted(self) -> None:
        selection = r.select(self.subject, self.model, "AXIOMATIC_CALCULUS.ac-001-closed-signature")
        routes = ac.obj(selection["acquisition_routes"], "routes")
        conditional = r.objects(routes["conditional"], "conditional")
        provenance = r.objects(routes["provenance"], "provenance")
        conditional_outside = [row for row in conditional if row["target_already_required"] is False]
        provenance_outside = [row for row in provenance if row["target_already_required"] is False]
        self.assertTrue(conditional_outside)
        self.assertTrue(provenance_outside)
        for row in conditional_outside:
            route = ac.obj(row["route"], "route")
            self.assertTrue(ac.obj(route["qualification"], "qualification")["required_when"])
            self.assertIn("do not perform", r.text(route["unknown_applicability"], "unknown applicability"))
            self.assertFalse(row["target_index_selected"])
        self.assertIn("withholds dependent action", r.text(selection["conditional_rule"], "conditional rule"))

    def test_release_selection_retains_both_original_residuals(self) -> None:
        selection = r.select(self.subject, self.model, "RELEASE_METHOD.open-questions")
        view = ac.obj(selection["projection"], "projection")
        populations = ac.obj(view["populations"], "populations")
        actual = r.objects(populations["residuals"], "residuals")
        self.assertEqual(len(actual), 2)
        recovered = [r.parse(r.text(ac.obj(row["uncertainty"], "uncertainty")["native_json"], "native_json"), "residual") for row in actual]
        self.assertEqual(recovered, self.subject.program["residuals"])
        self.assertEqual(populations["judgments"], [])

    def test_writing_selection_and_budget_refusal(self) -> None:
        selected = r.select(self.subject, self.model, "WRITING_GUIDE.good-prose")
        summary = r.selection_summary(selected)
        self.assertEqual(summary["clauses"], 12)
        view = ac.obj(selected["projection"], "projection")
        size = len(ac.seq(view["included"], "included"))
        self.assertEqual(r.select(self.subject, self.model, "WRITING_GUIDE.good-prose", size)["projection"], {**view, "selection": {**ac.obj(view["selection"], "selection"), "budget_records": size}})
        with self.assertRaisesRegex(ac.Refusal, "without truncation"):
            r.select(self.subject, self.model, "WRITING_GUIDE.good-prose", size - 1)

    def test_native_discovery_display_uses_exact_authored_predicate(self) -> None:
        clause_id = "urn:codex-stdo3:iteration-3-r2:clause:AXIOMATIC_CALCULUS.ac-001-closed-signature"
        record = self.model.records[clause_id]
        display = ac.obj(record.fields["value"], "value")["a_summary"]
        self.assertEqual(display, "Every admitted fundamental record occurs exactly once in the total population under one declared signature and record kind.")
        nodes = r.objects(self.carrier.document["nodes"], "nodes")
        matching = [node for node in nodes if node.get("ac_role") == "record" and ac.obj(node["ac_payload"], "payload")["record"] == record.fields]
        self.assertEqual(len(matching), 1)
        self.assertIn("Every admitted fundamental record", r.text(matching[0]["label"], "label"))

    def test_owner_body_pin_and_block_pin_tampering_refuses(self) -> None:
        changed = copy.deepcopy(self.subject.account)
        first = r.objects(changed["determinations"], "determinations")[0]
        ac.obj(first["owner"], "owner")["body_sha256"] = "0" * 64
        with self.assertRaisesRegex(ac.Refusal, "owner body pin drift"):
            r.verify_owner_pins(self.subject.members, changed)
        changed = copy.deepcopy(self.subject.account)
        first = r.objects(changed["determinations"], "determinations")[0]
        r.objects(first["source_clauses"], "blocks")[0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ac.Refusal, "block pin drift"):
            r.verify_owner_pins(self.subject.members, changed)

    def test_archive_and_manifest_tampering_refuse(self) -> None:
        with tempfile.TemporaryDirectory(prefix=".test-custody-", dir=r.HERE) as name:
            root = Path(name)
            manifest = (r.HERE / "input/manifest.json").read_bytes()
            archive = (r.HERE / "input/candidate.tar.gz").read_bytes()
            (root / "manifest.json").write_bytes(manifest)
            (root / "candidate.tar.gz").write_bytes(archive[:-1] + bytes([archive[-1] ^ 1]))
            with self.assertRaisesRegex(ac.Refusal, "archive drift"):
                r.load_frozen(root)
            (root / "candidate.tar.gz").write_bytes(archive)
            (root / "manifest.json").write_bytes(manifest + b" ")
            with self.assertRaisesRegex(ac.Refusal, "manifest drift"):
                r.load_frozen(root)

    def test_loss_of_mapped_required_occurrence_refuses_even_with_intact_native_json(self) -> None:
        changed = copy.deepcopy(self.model.document)
        first = r.objects(ac.obj(changed["populations"], "populations")["objects"], "objects")[0]
        refs = ac.seq(ac.obj(first["value"], "value")["required_refs"], "required_refs")
        refs.pop()
        changed_model = ac.validate(changed)
        self.assertEqual(r.recover_program(changed_model), self.subject.program)
        with self.assertRaisesRegex(ac.Refusal, "deterministic native transport"):
            r.verify_transport(self.subject, changed_model)

    def test_graph_payload_and_missing_occurrence_tampering_refuse(self) -> None:
        document = copy.deepcopy(self.carrier.document)
        nodes = r.objects(document["nodes"], "nodes")
        node = next(node for node in nodes if node.get("ac_role") == "record")
        payload = ac.obj(node["ac_payload"], "payload")
        record = ac.obj(payload["record"], "record")
        if "value" in record:
            ac.obj(record["value"], "value")["ordinal"] = 99999
        else:
            record["consequence"] = "Tampered consequence"
        with self.assertRaises(ac.Refusal):
            ac.decode(ac.GraphCarrier(document))
        document = dict(self.carrier.document)
        document["nodes"] = [node for node in ac.seq(document["nodes"], "nodes") if ac.obj(node, "node")["id"] != "urn:a-c:graph:occurrence:0"]
        with self.assertRaises(ac.Refusal):
            ac.decode(ac.GraphCarrier(document))

    def _write_bundle(self, root: Path, replacements: dict[str, bytes] | None = None) -> None:
        files = {**self.files, **(replacements or {})}
        for name, payload in files.items():
            (root / name).write_bytes(payload)

    def test_manifest_count_drift_refuses(self) -> None:
        changed = copy.deepcopy(self.manifest)
        ac.obj(changed["counts"], "counts")["clauses"] = 704
        with tempfile.TemporaryDirectory(prefix=".test-manifest-", dir=r.HERE) as name:
            root = Path(name)
            self._write_bundle(root, {"manifest.json": ac.canonical(changed) + b"\n"})
            with self.assertRaisesRegex(ac.Refusal, "manifest metadata differs"):
                r.load_representation(root)

    def test_catalogue_repinning_cannot_hide_wrong_source_clause_count(self) -> None:
        catalog = r.parse(self.files["selectors.json"], "catalog")
        r.objects(catalog["selectors"], "selectors")[0]["required_clauses"] = 1
        catalog_bytes = ac.canonical(catalog) + b"\n"
        changed_manifest = copy.deepcopy(self.manifest)
        pins = ac.obj(changed_manifest["artifacts"], "artifacts")
        pins["selectors.json"] = r.jo(bytes=len(catalog_bytes), sha256=r.sha_bytes(catalog_bytes))
        with tempfile.TemporaryDirectory(prefix=".test-catalogue-", dir=r.HERE) as name:
            root = Path(name)
            self._write_bundle(root, {"selectors.json": catalog_bytes, "manifest.json": ac.canonical(changed_manifest) + b"\n"})
            with self.assertRaisesRegex(ac.Refusal, "manifest metadata differs|source-derived expectation"):
                r.load_representation(root)

    def test_input_custody_cannot_be_an_output(self) -> None:
        before = (r.HERE / "input/manifest.json").read_bytes()
        with self.assertRaisesRegex(ac.Refusal, "frozen input custody"):
            r.emit(r.HERE / "input/manifest.json", b"replacement")
        self.assertEqual((r.HERE / "input/manifest.json").read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
