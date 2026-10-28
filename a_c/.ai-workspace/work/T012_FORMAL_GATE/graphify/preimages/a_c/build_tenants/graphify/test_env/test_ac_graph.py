from __future__ import annotations

from collections.abc import Iterator, Sequence
from contextlib import redirect_stderr, redirect_stdout
import copy
from dataclasses import replace
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from fixture_support import TENANT, jo, seal, simulated_judgment, toy_model, uid

sys.path.insert(0, str(TENANT / "code"))
import ac_graph as codec  # noqa: E402
from ac_graph import (  # noqa: E402
    CORE_FIELDS, GraphCarrier, JSON, Model, Object, Reference, Refusal, canonical,
    carrier_identity, decode, digest, extraction, find, inspect, main,
    materialize, obj, project, project_many, read_json, seq, validate, write_json,
)


class CountedReferences(tuple[Reference, ...]):
    visits = 0

    def __iter__(self) -> Iterator[Reference]:
        for reference in super().__iter__():
            self.visits += 1
            yield reference


class CountedPopulation(list[JSON]):
    visits = 0

    def __iter__(self) -> Iterator[JSON]:
        for value in super().__iter__():
            self.visits += 1
            yield value


class RealizationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.document = toy_model()

    def model(self) -> Model:
        return validate(self.document)

    def record(self, family: str, index: int = 0) -> Object:
        return obj(seq(obj(self.document["populations"], "populations")[family], family)[index], "record")

    def signature(self) -> Object:
        return obj(obj(self.document["signature"], "signature")["definition"], "definition")

    def test_round_trip_every_family_and_population_order(self) -> None:
        original = self.model()
        recovered = decode(materialize(original))
        self.assertEqual(original.document, recovered.document)
        self.assertEqual(original.sha256, recovered.sha256)
        self.assertEqual(set(CORE_FIELDS), {r.family for r in recovered.records.values()})
        # c,a,b deliberately differs from lexical node identity order.
        objects = seq(obj(recovered.document["populations"], "populations")["objects"], "objects")
        self.assertEqual(obj(objects[0], "object")["id"], uid("object:c"))

    def test_optimization_preserves_existing_carrier_and_projection_bytes(self) -> None:
        # Exact pre-optimization canonical bytes for the existing authored fixture.
        model = self.model()
        self.assertEqual(digest(materialize(model).document), "032073faa4c329bf9d60c6d639b0c25ec7a925eae66195e2fcfc6b880f25fff5")
        self.assertEqual(digest([result for result in project_many(model, [([rid], None) for rid in model.records])]), "6413ff5132ac7fd003d31bdd55cc1a86997bffae736d470dd7b1c30b7e1bf4b9")

    def test_extraction_round_trip(self) -> None:
        model = self.model()
        self.assertEqual(decode(GraphCarrier(extraction(materialize(model)))).document, model.document)

    def test_example_is_reproducible_and_source_bytes_match(self) -> None:
        fixture = read_json(TENANT / "test_env" / "fixtures" / "toy_model.json")
        self.assertEqual(fixture, self.document)
        import hashlib
        source_digest = hashlib.sha256((TENANT / "examples" / "subject.md").read_bytes()).hexdigest()
        self.assertEqual(obj(obj(fixture["basis"], "basis")["subject"], "subject")["sha256"], source_digest)

    def test_missing_or_unknown_population_refuses(self) -> None:
        for family in CORE_FIELDS:
            candidate = copy.deepcopy(self.document)
            obj(candidate["populations"], "populations").pop(family)
            with self.subTest(family=family), self.assertRaises(Refusal):
                validate(candidate)
        obj(self.document["populations"], "populations")["ninth-family"] = []
        with self.assertRaises(Refusal):
            self.model()

    def test_missing_unknown_and_duplicate_record_fields_refuse(self) -> None:
        for mutation in ("missing", "unknown", "duplicate"):
            self.setUp()
            if mutation == "missing":
                self.record("objects").pop("scope")
            elif mutation == "unknown":
                self.record("objects")["hidden"] = "payload"
            else:
                self.record("constraints")["id"] = self.record("objects")["id"]
            with self.subTest(mutation=mutation), self.assertRaises(Refusal):
                self.model()

    def test_wrong_family_and_dangling_refs_refuse(self) -> None:
        for target in (uid("constraint:review"), uid("missing")):
            candidate = copy.deepcopy(self.document)
            objects = seq(obj(candidate["populations"], "populations")["objects"], "objects")
            obj(obj(objects[1], "a")["value"], "value")["arguments"] = [target]
            with self.subTest(target=target), self.assertRaises(Refusal):
                validate(candidate)

    def test_wrong_target_sort_refuses(self) -> None:
        definition = self.signature()
        variants = obj(definition["sorts"], "sorts")
        variants[uid("sort:other")] = copy.deepcopy(variants[uid("sort:statement")])
        external = seq(self.document["external_resolutions"], "resolutions")
        resolution = copy.deepcopy(next(obj(r, "r") for r in external if obj(r, "r")["external_identity"] == uid("sort:statement")))
        resolution["external_identity"] = uid("sort:other")
        external.append(resolution)
        seq(self.document["identity_universe"], "I").append(uid("sort:other"))
        self.record("objects", 2)["sort"] = uid("sort:other")
        seal(self.document)
        with self.assertRaisesRegex(Refusal, "wrong target sort"):
            self.model()

    def test_unknown_sort_or_schema_refuses(self) -> None:
        self.record("objects")["sort"] = uid("sort:unknown")
        with self.assertRaises(Refusal):
            self.model()
        self.setUp()
        fields = obj(obj(self.signature()["fields"], "fields")["objects"], "objects")
        fields["value"] = jo(type="arbitrary-python")
        seal(self.document)
        with self.assertRaisesRegex(Refusal, "unsupported schema"):
            self.model()

    def test_signature_cannot_retarget_fixed_core_record_links(self) -> None:
        for family, field, array in (
            ("transformations", "traversal", False),
            ("constraints", "latitude_ref", True),
            ("transformations", "residuals", True),
        ):
            self.setUp()
            declared = obj(obj(self.signature()["fields"], "fields")[family], family)
            domain = obj(declared[field], field)
            if array:
                domain = obj(domain["items"], field)
            domain["local_families"] = ["objects"]
            domain["local_sorts"] = []
            self.record(family)[field] = [uid("object:a")] if array else uid("object:a")
            seal(self.document)
            with self.subTest(field=field), self.assertRaisesRegex(Refusal, "fixed core family"):
                self.model()

    def test_complete_model_and_external_delta_coordinates_are_not_local_records(self) -> None:
        for field, array in (("domain_model", False), ("codomain_model", False), ("external_preserved", True), ("external_introduced", True), ("external_removed", True), ("external_resolution_witnesses", True)):
            self.setUp()
            declared = obj(obj(self.signature()["fields"], "fields")["transformations"], "transformations")
            domain = obj(declared[field], field)
            if array:
                domain = obj(domain["items"], field)
            domain["local_families"] = ["objects"]
            domain["external_kinds"] = []
            self.record("transformations")[field] = [uid("object:a")] if array else uid("object:a")
            seal(self.document)
            with self.subTest(field=field), self.assertRaisesRegex(Refusal, "not local core records"):
                self.model()

    def test_unknown_signature_field_refuses(self) -> None:
        self.signature()["new-field"] = True
        seal(self.document)
        with self.assertRaises(Refusal):
            self.model()

    def test_empty_required_population_refuses(self) -> None:
        obj(self.document["populations"], "populations")["transformations"] = []
        with self.assertRaisesRegex(Refusal, "required population empty"):
            self.model()

    def test_closed_identity_universe_and_external_collision_refuse(self) -> None:
        seq(self.document["identity_universe"], "I").append(uid("hidden"))
        with self.assertRaisesRegex(Refusal, "identity universe"):
            self.model()
        self.setUp()
        external = seq(self.document["external_resolutions"], "external")
        duplicate = copy.deepcopy(obj(external[0], "external"))
        duplicate["external_identity"] = uid("object:a")
        external.append(duplicate)
        with self.assertRaisesRegex(Refusal, "collision"):
            self.model()

    def test_duplicate_external_resolution_refuses(self) -> None:
        external = seq(self.document["external_resolutions"], "external")
        external.append(copy.deepcopy(external[0]))
        with self.assertRaises(Refusal):
            self.model()

    def append_unused_external(self, **changes: JSON) -> None:
        resolutions = seq(self.document["external_resolutions"], "external")
        candidate = copy.deepcopy(obj(resolutions[0], "resolution"))
        candidate["external_identity"] = uid("external:unused")
        candidate["resolved_target_identity"] = uid("resolved:unused")
        candidate.update(changes)
        resolutions.append(candidate)
        seq(self.document["identity_universe"], "I").append(uid("external:unused"))

    def test_unused_external_must_match_declared_contract(self) -> None:
        for field in ("reference_domain", "external_target_kind", "basis_relation", "all"):
            self.setUp()
            changes: Object = {}
            for name in ("reference_domain", "external_target_kind", "basis_relation"):
                if field in (name, "all"):
                    changes[name] = uid("UNDECLARED:" + name)
            self.append_unused_external(**changes)
            with self.subTest(field=field), self.assertRaisesRegex(Refusal, "no declared reference-domain contract"):
                self.model()

    def test_unused_external_with_declared_contract_remains_lawful(self) -> None:
        self.append_unused_external()
        model = self.model()
        self.assertNotIn(uid("external:unused"), {r.target for r in model.references})
        recovered = decode(materialize(model))
        self.assertEqual(recovered.external[uid("external:unused")], model.external[uid("external:unused")])

    def test_external_contracts_include_nested_variant_only_schemas(self) -> None:
        sort = obj(obj(self.signature()["sorts"], "sorts")[uid("sort:statement")], "sort")
        fields = obj(obj(sort["value"], "value")["fields"], "fields")
        domain = jo(type="ref", domain=uid("reference-domain:variant-only"), local_families=[], local_sorts=[], external_kinds=[uid("external-kind:variant-only")], basis_relation=uid("basis-relation:variant-only"), governing=False)
        fields["unused_nested_refs"] = jo(type="array", items=jo(type="object", fields=jo(target=domain)), min_items=0)
        for value in seq(obj(self.document["populations"], "populations")["objects"], "objects"):
            obj(obj(value, "record")["value"], "value")["unused_nested_refs"] = []
        self.append_unused_external(reference_domain=uid("reference-domain:variant-only"), external_target_kind=uid("external-kind:variant-only"), basis_relation=uid("basis-relation:variant-only"))
        seal(self.document)
        model = self.model()
        self.assertIn(uid("external:unused"), model.external)
        self.assertNotIn(uid("external:unused"), {r.target for r in model.references})
        self.assertEqual(decode(materialize(model)).document, model.document)

    def test_stale_or_mixed_basis_and_scope_refuse(self) -> None:
        for key, value in (("basis", uid("other-basis")), ("owner", uid("other-owner")), ("scope", [uid("other-scope")])):
            self.setUp()
            from typing import cast
            self.record("objects")[key] = cast(JSON, value)
            with self.subTest(key=key), self.assertRaises(Refusal):
                self.model()
        self.setUp()
        obj(obj(self.document["basis"], "basis")["calculus"], "calculus")["sha256"] = "0" * 64
        with self.assertRaisesRegex(Refusal, "calculus basis"):
            self.model()

    def test_external_domain_and_resolution_basis_refuse(self) -> None:
        for field in ("reference_domain", "external_target_kind", "basis_relation", "resolution_basis"):
            self.setUp()
            obj(seq(self.document["external_resolutions"], "external")[0], "resolution")[field] = uid("wrong")
            with self.subTest(field=field), self.assertRaises(Refusal):
                self.model()

    def test_stale_signature_and_ledger_commitments_refuse(self) -> None:
        self.signature()["required_families"] = []
        with self.assertRaisesRegex(Refusal, "signature digest"):
            self.model()
        self.setUp()
        interpretation = obj(self.document["interpretation"], "interpretation")
        obj(seq(interpretation["dispositions"], "dispositions")[0], "d")["reason"] = "Changed meaning selection basis."
        with self.assertRaisesRegex(Refusal, "ledger digest"):
            self.model()

    def test_ledger_coverage_refuses_unmapped_record(self) -> None:
        interpretation = obj(self.document["interpretation"], "interpretation")
        disposition = obj(seq(interpretation["dispositions"], "d")[0], "d")
        seq(disposition["records"], "records").pop()
        seal(self.document)
        with self.assertRaisesRegex(Refusal, "every local record"):
            self.model()

    def test_semantic_float_and_duplicate_json_names_refuse(self) -> None:
        self.record("objects")["value"] = 1.5
        with self.assertRaisesRegex(Refusal, "floating point"):
            self.model()
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "duplicate.json"
            path.write_text('{"profile":"first","profile":"second"}', encoding="utf-8")
            with self.assertRaisesRegex(Refusal, "duplicate key"):
                read_json(path)

    def test_parallel_reversed_self_and_repeated_occurrences_survive(self) -> None:
        model = decode(materialize(self.model()))
        relations = [r for r in model.records.values() if r.family == "relations"]
        parallel = [r for r in relations if r.fields["source"] == uid("object:a") and r.fields["target"] == uid("object:b")]
        self.assertEqual(len(parallel), 2)
        self.assertTrue(any(r.fields["source"] == uid("object:b") and r.fields["target"] == uid("object:a") for r in relations))
        self.assertTrue(any(r.fields["source"] == r.fields["target"] for r in relations))
        repeated = [r for r in model.references if r.owner == uid("object:a") and r.path[:2] == ("value", "arguments")]
        self.assertEqual([r.target for r in repeated], [uid("object:a"), uid("object:a"), uid("object:b")])
        self.assertEqual([r.path[-1] for r in repeated], ["0", "1", "2"])

    def test_missing_occurrence_or_link_refuses(self) -> None:
        for component in ("nodes", "links"):
            graph = materialize(self.model()).document
            values = seq(graph[component], component)
            if component == "nodes":
                index = next(i for i, n in enumerate(values) if obj(n, "node")["ac_role"] == "reference-occurrence")
                values.pop(index)
            else:
                values.pop()
            with self.subTest(component=component), self.assertRaises(Refusal):
                decode(GraphCarrier(graph))

    def test_occurrence_payload_and_record_tampering_refuse(self) -> None:
        for role in ("reference-occurrence", "record"):
            graph = materialize(self.model()).document
            node = next(obj(n, "node") for n in seq(graph["nodes"], "nodes") if obj(n, "node")["ac_role"] == role)
            payload = obj(node["ac_payload"], "payload")
            if role == "reference-occurrence":
                payload["target"] = uid("object:c")
            else:
                obj(payload["record"], "record")["owner"] = uid("forged")
            with self.subTest(role=role), self.assertRaises(Refusal):
                decode(GraphCarrier(graph))

    def test_extra_semantic_node_and_duplicate_edge_refuse(self) -> None:
        for component in ("nodes", "links"):
            graph = materialize(self.model()).document
            values = seq(graph[component], component)
            values.append(copy.deepcopy(values[0]))
            with self.subTest(component=component), self.assertRaises(Refusal):
                decode(GraphCarrier(graph))

    def test_native_search_excerpts_are_exact_derived_content(self) -> None:
        graph = materialize(self.model()).document
        node = next(obj(n, "node") for n in seq(graph["nodes"], "nodes") if obj(n, "node")["ac_role"] == "record")
        attributes = obj(node["attributes"], "attributes")
        self.assertIn("semantic_identity", attributes)
        attributes["record_family"] = "forged family"
        with self.assertRaisesRegex(Refusal, "semantic encoding"):
            decode(GraphCarrier(graph))

    def test_incidental_upstream_attributes_preserve_semantic_identity(self) -> None:
        original = materialize(self.model())
        graph = copy.deepcopy(original.document)
        for value in seq(graph["nodes"], "nodes"):
            obj(value, "node")["community"] = 1
        for value in seq(graph["links"], "links"):
            edge = obj(value, "edge")
            edge["confidence_score"] = 1.0
            edge["source"], edge["target"] = edge["target"], edge["source"]
        self.assertEqual(carrier_identity(original), carrier_identity(GraphCarrier(graph)))

    def test_stale_validated_api_model_refuses(self) -> None:
        model = self.model()
        self.record("objects")["value"] = jo(text="Changed after validation", arguments=[])
        for operation in (lambda: materialize(model), lambda: find(model, "changed"), lambda: inspect(model, uid("object:a")), lambda: project(model, [uid("object:a")]), lambda: project_many(model, [([uid("object:a")], None)]), lambda: project_many(model, [])):
            with self.assertRaisesRegex(Refusal, "changed"):
                operation()
        self.setUp()
        with self.assertRaises(Refusal):
            materialize(replace(self.model(), records={}))

    def test_container_flags_and_profile_contradictions_refuse(self) -> None:
        for field, bad in (("directed", True), ("directed", "bogus"), ("directed", 0), ("multigraph", True), ("multigraph", "false")):
            graph = materialize(self.model()).document
            graph[field] = bad
            with self.subTest(field=field, value=bad):
                with self.assertRaisesRegex(Refusal, "Boolean false"):
                    decode(GraphCarrier(graph))
                with self.assertRaises(Refusal):
                    carrier_identity(GraphCarrier(graph))
        graph = materialize(self.model()).document
        obj(graph["graph"], "graph")["ac_profile"] = "unsupported/carrier/999"
        with self.assertRaisesRegex(Refusal, "graph.ac_profile"):
            decode(GraphCarrier(graph))
        with self.assertRaises(Refusal):
            carrier_identity(GraphCarrier(graph))

    def test_flagless_and_incidental_graph_metadata_remain_supported(self) -> None:
        original = materialize(self.model())
        extraction_input = extraction(original)
        self.assertEqual(carrier_identity(GraphCarrier(extraction_input)), carrier_identity(original))
        graph = copy.deepcopy(original.document)
        graph["graph"] = {"upstream_annotation": 0.5}
        self.assertEqual(carrier_identity(GraphCarrier(graph)), carrier_identity(original))

    def test_supplied_acceptance_coordinates_are_separate_evidence(self) -> None:
        model = self.model()
        first = materialize(model, simulated_judgment(self.document, "one"))
        second = materialize(model, simulated_judgment(self.document, "two"))
        self.assertNotEqual(first.document["ac_evidence"], second.document["ac_evidence"])
        self.assertEqual(carrier_identity(first), carrier_identity(second))
        self.assertEqual(carrier_identity(first), carrier_identity(materialize(model)))
        self.assertEqual(decode(first).document, self.document)

    def test_wrong_or_incomplete_supplied_judgment_refuses(self) -> None:
        for field, value in (("subject_digest", "0" * 64), ("subject", uid("other")), ("decision", "indeterminate"), ("evidence", []), ("provenance", []), ("authority", jo(id=uid("forged"), sha256="0" * 64))):
            judgment = simulated_judgment(self.document)
            judgment[field] = value
            with self.subTest(field=field), self.assertRaises(Refusal):
                materialize(self.model(), judgment)

    def test_governing_closure_preserves_residual_latitude_and_cycle(self) -> None:
        result = project(self.model(), [uid("object:a")])
        included = seq(result["included"], "included")
        self.assertEqual(len(included), 9)
        for name in ("object:a", "object:b", "constraint:review", "latitude:wording", "residual:reading", "relation:parallel:one", "relation:parallel:two", "relation:reverse", "relation:self"):
            self.assertIn(uid(name), included)
        self.assertNotIn(uid("object:c"), included)
        self.assertNotIn(uid("traversal:review"), included)
        boundary = obj(result["boundary"], "boundary")
        self.assertIn(uid("residual:reading"), seq(boundary["unresolved_residuals"], "residuals"))
        self.assertTrue(any(obj(r, "ref")["target"] == uid("traversal:review") for r in seq(boundary["non_governing_references"], "refs")))
        self.assertTrue(any(obj(r, "relation")["id"] == uid("relation:discovery") for r in seq(boundary["crossing_relations"], "relations")))

    def test_budget_and_bad_seed_refuse_without_partial_success(self) -> None:
        model = self.model()
        self.assertEqual(len(seq(project(model, [uid("object:a")], 9)["included"], "included")), 9)
        for seeds, budget in (([uid("object:a")], 8), ([uid("missing")], None), ([], None), ([uid("object:a"), uid("object:a")], None)):
            with self.subTest(seeds=seeds, budget=budget), self.assertRaises(Refusal):
                project(model, seeds, budget)

    def test_project_many_matches_individual_selections_and_order(self) -> None:
        model = self.model()
        selections: list[tuple[Sequence[str], int | None]] = [
            ([uid("object:c")], 1),
            ([uid("object:b"), uid("object:a")], 9),
            ([uid("residual:reading")], None),
            ([uid("object:a")], 9),
        ]
        expected = [project(model, seeds, budget) for seeds, budget in selections]
        self.assertEqual(project_many(model, selections), expected)
        self.assertEqual(project_many(model, []), [])
        self.assertEqual(decode(materialize(model)).sha256, model.sha256)

    def test_project_many_refuses_invalid_selection_after_valid_selection(self) -> None:
        model = self.model()
        invalid: list[tuple[Sequence[str], int | None]] = [
            ([uid("object:a")], 8), ([uid("missing")], None),
            ([], None), ([uid("object:a"), uid("object:a")], None),
            ([uid("object:c")], -1),
        ]
        for selection in invalid:
            with self.subTest(selection=selection), self.assertRaises(Refusal):
                project_many(model, [([uid("object:c")], 1), selection])
        self.assertEqual(len(seq(project_many(model, [([uid("object:a")], 9)])[0]["included"], "included")), 9)

    def test_project_many_revalidates_after_success_and_derived_tampering(self) -> None:
        model = self.model()
        selection = [([uid("object:c")], 1)]
        self.assertEqual(len(project_many(model, selection)), 1)
        with self.assertRaisesRegex(Refusal, "changed"):
            project_many(replace(model, references=()), selection)
        self.record("objects")["value"] = jo(text="Changed after the successful batch", arguments=[])
        for selections in (selection, []):
            with self.subTest(selections=selections), self.assertRaisesRegex(Refusal, "changed"):
                project_many(model, selections)

    def generated_cycle(self, size: int) -> tuple[Model, list[str]]:
        """A longer authored reference cycle with repeated argument occurrences."""
        objects = seq(obj(self.document["populations"], "populations")["objects"], "objects")
        template = copy.deepcopy(self.record("objects"))
        identities = [uid(f"scale:object:{i}") for i in range(size)]
        for i, rid in enumerate(identities):
            record = copy.deepcopy(template)
            record["id"] = rid
            record["value"] = jo(text=f"Scaling fixture statement {i}", arguments=[identities[(i + 1) % size]] * 8)
            objects.append(record)
        seq(self.document["identity_universe"], "identities").extend(identities)
        interpretation = obj(self.document["interpretation"], "interpretation")
        disposition = obj(seq(interpretation["dispositions"], "dispositions")[0], "disposition")
        seq(disposition["records"], "records").extend(identities)
        seal(self.document)
        return self.model(), identities

    def test_batch_indexes_references_once_and_preserves_long_cycle(self) -> None:
        model, identities = self.generated_cycle(96)
        references = CountedReferences(model.references)
        fresh_operation = codec._fresh

        def fresh_counted(candidate: Model) -> Model:
            return replace(fresh_operation(candidate), references=references)

        with patch("ac_graph._fresh", side_effect=fresh_counted) as freshness:
            results = project_many(model, [([rid], 96) for rid in identities])
        self.assertEqual(freshness.call_count, 1)
        self.assertEqual(references.visits, len(model.references))
        self.assertEqual(len(results), len(identities))
        for rid, result in zip(identities, results):
            self.assertEqual(result["included"], sorted(identities))
            self.assertEqual(obj(result["selection"], "selection")["seeds"], [rid])
            self.assertEqual(seq(obj(result["populations"], "populations")["objects"], "objects"), [model.records[identity].fields for identity in identities])
        with self.assertRaisesRegex(Refusal, "needs 96 records"):
            project_many(model, [([identities[0]], 95)])

    def test_materialize_reads_population_ordinals_once(self) -> None:
        model, _ = self.generated_cycle(96)
        populations = obj(model.document["populations"], "populations")
        counted = CountedPopulation(seq(populations["objects"], "objects"))
        populations["objects"] = counted
        fresh_operation = codec._fresh

        def fresh_counted(candidate: Model) -> Model:
            current = fresh_operation(candidate)
            counted.visits = 0
            return current

        with patch("ac_graph._fresh", side_effect=fresh_counted) as freshness:
            carrier = materialize(model)
        self.assertEqual(freshness.call_count, 1)
        self.assertEqual(counted.visits, len(counted))
        self.assertEqual(decode(carrier).document, model.document)

    def test_required_relation_endpoints_survive_false_field_roles(self) -> None:
        def clear_governing(value: JSON) -> None:
            if isinstance(value, dict):
                if value.get("type") == "ref":
                    value["governing"] = False
                for child in value.values():
                    clear_governing(child)
            elif isinstance(value, list):
                for child in value:
                    clear_governing(child)

        clear_governing(self.signature())
        seal(self.document)
        model = self.model()
        for seed in (uid("object:a"), uid("relation:parallel:one")):
            with self.subTest(seed=seed):
                result = project(model, [seed])
                included = seq(result["included"], "included")
                self.assertIn(uid("object:a"), included)
                self.assertIn(uid("object:b"), included)
                self.assertIn(uid("relation:parallel:one"), included)
                self.assertNotIn(uid("object:c"), included)

    def test_literal_find_and_inspect_report_scope(self) -> None:
        model = self.model()
        result = find(model, "PROVENANCE-ONLY")
        self.assertTrue(any(obj(m, "match")["id"] == uid("object:c") for m in seq(result["matches"], "matches")))
        record = inspect(model, uid("object:a"))
        self.assertEqual(record["record"], model.records[uid("object:a")].fields)
        self.assertIn("structural", str(record["claim"]))

    def cli(self, args: list[str]) -> tuple[int, str, str]:
        output, errors = io.StringIO(), io.StringIO()
        with redirect_stdout(output), redirect_stderr(errors):
            result = main(args)
        return result, output.getvalue(), errors.getvalue()

    def test_cli_runnable_proposal_and_projection(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            model_path, graph_path, projection_path = (root / name for name in ("model.json", "graph.json", "projection.json"))
            write_json(model_path, self.document)
            status, stdout, _ = self.cli(["materialize", str(model_path), "--out", str(graph_path)])
            self.assertEqual(status, 0)
            self.assertIn("proposal-view", stdout)
            self.assertNotIn("ac_evidence", read_json(graph_path))
            self.assertEqual(self.cli(["project", str(graph_path), "--seed", uid("object:a"), "--out", str(projection_path)])[0], 0)
            self.assertEqual(len(seq(read_json(projection_path)["included"], "included")), 9)
            output = root / "refused.json"
            self.assertEqual(self.cli(["project", str(graph_path), "--seed", uid("object:a"), "--budget", "8", "--out", str(output)])[0], 2)
            self.assertFalse(output.exists())

    def test_cli_protects_unchanged_subject_paths_and_existing_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "model.json"
            write_json(source, self.document)
            original = source.read_bytes()
            link = root / "symlink.json"
            link.symlink_to(source)
            hardlink = root / "hardlink.json"
            hardlink.hardlink_to(source)
            existing = root / "existing.json"
            existing.write_text("old artifact", encoding="utf-8")
            for target in (source, link, hardlink, existing):
                with self.subTest(target=target):
                    self.assertEqual(self.cli(["materialize", str(source), "--out", str(target)])[0], 2)
                    self.assertEqual(source.read_bytes(), original)
            self.assertEqual(existing.read_text(encoding="utf-8"), "old artifact")

    def test_unsupported_operations_explicitly_refuse(self) -> None:
        for command in ("transform", "overlay", "execute", "evaluate-predicate"):
            with self.subTest(command=command):
                status, _, errors = self.cli([command])
                self.assertEqual(status, 2)
                self.assertIn("unsupported", errors)

    def test_canonical_grammar_is_integer_only_and_order_sensitive(self) -> None:
        self.assertEqual(canonical(jo(b=2, a="é")), b'{"a":"\xc3\xa9","b":2}')
        self.assertNotEqual(digest([1, 2]), digest([2, 1]))
        with self.assertRaises(Refusal):
            canonical(float("nan"))


if __name__ == "__main__":
    unittest.main()
