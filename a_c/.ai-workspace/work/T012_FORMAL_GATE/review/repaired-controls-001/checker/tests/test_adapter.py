"""Source-field, carrier and certificate controls for the independent adapter."""
from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import import_fixture as bridge


class AdapterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = bridge.load_checked(bridge.FIXTURE_DIR / "MODEL.json")
        cls.imported = bridge.import_model(cls.model)
        cls.carrier = bridge.read_json(bridge.FIXTURE_DIR / "CARRIER.json")

    def reject_model(self, change):
        model = deepcopy(self.model)
        change(model)
        with self.assertRaises(bridge.Refusal):
            bridge.import_model(model)

    def test_actual_custody_and_both_carrier_recoveries(self):
        result = bridge.verify_fixture()
        self.assertEqual(result["records"], 32)
        self.assertEqual(result["references"], 246)
        self.assertEqual(result["edges"], 47)
        self.assertEqual(result["model_sha256"], bridge.MODEL_SHA256)
        self.assertEqual(result["singleton_closure_histogram"], {"2": 6, "3": 9, "4": 4, "6": 8, "11": 5})

    def test_application_neutral_toy_has_all_eight_families_and_exact_preservation(self):
        report = bridge.verify_toy_fixture()
        self.assertEqual((report["records"], report["references"], report["edges"]), (14, 124, 29))
        self.assertTrue(all(report["families"][family] > 0 for family in bridge.FAMILIES))
        source = bridge.load_checked(bridge.TOY_FIXTURE_DIR / "MODEL.json")
        imported = bridge.import_model(source)
        self.assertEqual(bridge.reconstruct(imported), source)
        for seed in range(14):
            result = bridge.closure_certificate(imported, [seed])
            self.assertTrue(bridge.check_certificate(imported, result))
            self.assertEqual(result["records"], [imported["records"][i] for i in result["included"]])
            with self.assertRaises(bridge.Refusal):
                bridge.closure_certificate(imported, [seed], len(result["included"]) - 1)
        malformed = deepcopy(source)
        malformed["populations"]["judgments"][0]["id"] = source["populations"]["objects"][0]["id"]
        with self.assertRaisesRegex(bridge.Refusal, "duplicate local identity"):
            bridge.import_model(malformed)

    def test_toy_parallel_self_discovery_and_repeated_reference_distinctions(self):
        imported = bridge.import_model(bridge.load_checked(bridge.TOY_FIXTURE_DIR / "MODEL.json"))
        result = bridge.closure_certificate(imported, [1], 9)
        self.assertEqual(result["included"], [1, 2, 3, 4, 5, 6, 8, 9, 10])
        self.assertEqual(bridge.closure_certificate(imported, [0])["included"], [0])
        self.assertNotEqual(imported["records"][3]["record"]["id"], imported["records"][4]["record"]["id"])
        self.assertEqual(imported["records"][6]["record"]["source"], imported["records"][6]["record"]["target"])
        repeated = [r for r in imported["references"] if r["owner"] == 3 and r["path"][0] == "qualifiers"]
        self.assertEqual([r["path"] for r in repeated], [["qualifiers", "arguments", 0], ["qualifiers", "arguments", 1]])
        self.assertEqual([r["target"] for r in repeated], [1, 1])
        traversal = bridge.closure_certificate(imported, [11])
        self.assertNotIn(0, traversal["included"])
        omitted = traversal["boundary"]["non_governing_references"]
        self.assertEqual([(r["path"], r["target"]) for r in omitted if r["owner"] == 11],
                         [(["evidence", 0], 0), (["provenance", 0], 0)])

    def test_complete_source_field_reconstruction_and_family_order(self):
        self.assertEqual(bridge.reconstruct(self.imported), self.model)
        self.assertEqual(list(bridge.reconstruct(self.imported)["populations"]), list(bridge.FAMILIES))
        for item in self.imported["records"]:
            self.assertEqual(item["record"], self.model["populations"][item["family"]][item["ordinal"]])
        self.assertEqual({k: len(v) for k, v in self.model["populations"].items()},
                         dict(zip(bridge.FAMILIES, (10, 3, 10, 6, 3, 0, 0, 0))))

    def test_fixture_byte_change_is_refused_before_model_use(self):
        with tempfile.TemporaryDirectory() as tmp:
            for name in (*bridge.RAW_SHA256, "CUSTODY.json"):
                shutil.copyfile(bridge.FIXTURE_DIR / name, Path(tmp) / name)
            with (Path(tmp) / "MODEL.json").open("a") as file:
                file.write("\n")
            with self.assertRaisesRegex(bridge.Refusal, "raw fixture digest"):
                bridge.verify_fixture(tmp)

    def test_duplicate_json_keys_and_unsupported_numbers_refuse(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            for text in ('{"x":1,"x":2}', '{"x":NaN}', '{"x":1.0}', '{"x":"\\ud800"}', '{"x":' + '1' * 5000 + '}'):
                with self.subTest(text=text[:80]):
                    path.write_text(text)
                    with self.assertRaises(bridge.Refusal):
                        bridge.read_json(path)

    def test_closed_model_population_and_record_shapes(self):
        changes = [
            lambda m: m.update(extra=True),
            lambda m: m["populations"].pop("judgments"),
            lambda m: m["populations"].update(ninth=[]),
            lambda m: m["populations"]["objects"][0].update(extra=True),
            lambda m: m["populations"]["objects"][0]["value"].pop("exceptions"),
        ]
        for change in changes:
            with self.subTest(change=change):
                self.reject_model(change)

    def test_schema_cannot_weaken_ref_domain_or_governing_role(self):
        for field, value in (("governing", False), ("local_families", ["residuals"])):
            model = deepcopy(self.model)
            model["signature"]["definition"]["fields"]["relations"]["source"][field] = value
            model["signature"]["sha256"] = bridge.digest({k: v for k, v in model["signature"].items() if k != "sha256"})
            with self.assertRaisesRegex(bridge.Refusal, "pinned signature"):
                bridge.import_model(model)

    def test_local_duplicate_and_external_collision_refuse(self):
        self.reject_model(lambda m: m["populations"]["objects"].append(deepcopy(m["populations"]["objects"][0])))
        self.reject_model(lambda m: m["external_resolutions"][0].update(external_identity=m["populations"]["objects"][0]["id"]))
        self.reject_model(lambda m: m["external_resolutions"].append(deepcopy(m["external_resolutions"][0])))

    def test_dangling_wrong_family_unknown_kind_refuse(self):
        self.reject_model(lambda m: m["populations"]["relations"][0].update(source="urn:missing"))
        self.reject_model(lambda m: m["populations"]["relations"][0].update(source=m["populations"]["residuals"][0]["id"]))
        self.reject_model(lambda m: m["populations"]["constraints"][0].update(kind="urn:unknown:constraint"))
        self.reject_model(lambda m: m["populations"]["constraints"][0].update(latitude_ref=[m["populations"]["objects"][0]["id"]]))

    def test_record_coordinates_external_basis_and_contract_refuse(self):
        for field in ("basis", "owner", "context"):
            self.reject_model(lambda m, f=field: m["populations"]["objects"][0].update({f: "urn:changed"}))
        for field in ("resolution_basis", "reference_domain", "external_target_kind", "basis_relation"):
            self.reject_model(lambda m, f=field: m["external_resolutions"][-1].update({f: "urn:changed"}))

    def test_identity_universe_and_selection_ledger_must_be_complete(self):
        self.reject_model(lambda m: m["identity_universe"].pop())
        self.reject_model(lambda m: m["identity_universe"].append("urn:unowned"))
        self.reject_model(lambda m: m["interpretation"]["dispositions"].pop())
        model = deepcopy(self.model)
        model["interpretation"]["dispositions"][0]["records"].pop()
        model["interpretation"]["selection_ledger"]["sha256"] = bridge.digest(model["interpretation"]["dispositions"])
        with self.assertRaisesRegex(bridge.Refusal, "incomplete source/record"):
            bridge.import_model(model)

    def test_unknown_governing_relation_and_missing_attachment_family_refuse(self):
        self.reject_model(lambda m: m["dependency_contract"]["required_relation_kinds"].append("urn:missing"))
        self.reject_model(lambda m: m["dependency_contract"]["attachment_families"].remove("residuals"))

    def test_source_reference_paths_reach_exact_fields(self):
        for ref in self.imported["references"]:
            value = self.imported["records"][ref["owner"]]["record"]
            for step in ref["path"]:
                self.assertIs(type(step), int if isinstance(value, list) else str)
                value = value[step]
            target = ref["target"]
            expected = self.imported["records"][target]["record"]["id"] if type(target) is int else target
            self.assertEqual(value, expected)
        self.assertTrue(any(any(type(step) is int for step in r["path"]) for r in self.imported["references"]))

    def test_field_named_zero_and_array_index_zero_do_not_collapse(self):
        schema = next(r["schema"] for r in self.imported["references"] if type(r["target"]) is str)
        target = next(r["target"] for r in self.imported["references"] if r["schema"] == schema)
        external = {r["external_identity"]: r for r in self.model["external_resolutions"]}
        refs = []
        bridge._check_value({"0": target}, {"type": "object", "fields": {"0": schema}}, 0, (), {}, external, refs)
        bridge._check_value([target], {"type": "array", "items": schema}, 0, (), {}, external, refs)
        self.assertEqual([r["path"] for r in refs], [["0"], [0]])

    def test_repeated_reference_occurrences_are_preserved(self):
        model = deepcopy(self.model)
        subject = model["populations"]["constraints"][0]["applies_to"][0]
        model["populations"]["constraints"][0]["applies_to"].append(subject)
        imported = bridge.import_model(model)
        refs = [r for r in imported["references"] if r["owner"] == 13 and r["path"][0] == "applies_to"]
        self.assertEqual([r["path"] for r in refs], [["applies_to", 0], ["applies_to", 1]])
        self.assertEqual(len(imported["references"]), 247)
        self.assertEqual(imported["edges"], self.imported["edges"])

    def test_direction_is_not_inferred_from_undirected_connectivity(self):
        self.assertEqual(bridge.closure_certificate(self.imported, [2])["included"], [2, 15])
        self.assertEqual(bridge.closure_certificate(self.imported, [3])["included"], [2, 3, 10, 15, 16, 25])
        model = deepcopy(self.model)
        relation = model["populations"]["relations"][0]
        relation["source"], relation["target"] = relation["target"], relation["source"]
        reversed_model = bridge.import_model(model)
        self.assertIn(3, bridge.closure_certificate(reversed_model, [2])["included"])
        self.assertNotIn(2, bridge.closure_certificate(reversed_model, [3])["included"])

    def test_cycles_and_self_relation_terminate_with_exact_closure(self):
        model = deepcopy(self.model)
        relation = model["populations"]["relations"][0]
        relation["target"] = relation["source"]
        imported = bridge.import_model(model)
        result = bridge.closure_certificate(imported, [3])
        self.assertEqual(result["included"], [3, 10, 16, 25])
        self.assertTrue(bridge.check_certificate(imported, result))

    def test_all_selectors_match_independent_transitive_closure(self):
        count = len(self.imported["records"])
        reachable = [[i == j for j in range(count)] for i in range(count)]
        for source, target in self.imported["edges"]:
            reachable[source][target] = True
        for intermediate in range(count):
            for source in range(count):
                for target in range(count):
                    reachable[source][target] |= reachable[source][intermediate] and reachable[intermediate][target]
        sizes = Counter()
        for seed in range(count):
            expected = [i for i in range(count) if reachable[seed][i]]
            result = bridge.closure_certificate(self.imported, [seed], len(expected))
            self.assertEqual(result["included"], expected)
            self.assertTrue(bridge.check_certificate(self.imported, result))
            with self.assertRaisesRegex(bridge.Refusal, "without truncation"):
                bridge.closure_certificate(self.imported, [seed], len(expected) - 1)
            sizes[len(expected)] += 1
        self.assertEqual(sizes, {2: 6, 3: 9, 4: 4, 6: 8, 11: 5})

    def test_multiseed_and_whole_model(self):
        self.assertEqual(bridge.closure_certificate(self.imported, [0, 1])["included"], [0, 1, 13, 14, 23, 24])
        result = bridge.closure_certificate(self.imported, list(range(32)), 32)
        self.assertEqual(result["included"], list(range(32)))
        self.assertEqual(result["order"], [])
        self.assertEqual(result["excluded"], [])

    def test_non_governing_reference_is_visible_without_forcing_dependency(self):
        model = deepcopy(self.model)
        # A synthetic structural extension under the same frozen signature,
        # not an assertion that the source prose calls for this traversal.
        domain_schema = model["signature"]["definition"]["fields"]["traversals"]["domain"]
        resolution = deepcopy(model["external_resolutions"][0])
        resolution.update(external_identity="urn:test:domain", resolved_target_identity="urn:test:domain",
                          external_target_kind=domain_schema["external_kinds"][0])
        model["external_resolutions"].append(resolution)
        tid = "urn:test:traversal"
        model["identity_universe"].extend(["urn:test:domain", tid])
        traversal = {"id": tid, **deepcopy(model["coordinates"]), "basis": model["basis"]["id"],
                     "domain": "urn:test:domain", "codomain": "urn:test:domain",
                     "preconditions": [], "postconditions": [],
                     "authority": model["interpretation"]["authority"]["id"],
                     "evidence": [model["populations"]["objects"][0]["id"]], "provenance": [],
                     "stop_states": model["signature"]["definition"]["stop_kinds"]}
        model["populations"]["traversals"].append(traversal)
        model["functor_bindings"][tid] = "urn:stdo:concept:axiomatic-calculus:f-d"
        model["interpretation"]["dispositions"][0]["records"].append(tid)
        model["interpretation"]["selection_ledger"]["sha256"] = bridge.digest(model["interpretation"]["dispositions"])
        model["populations"]["residuals"][0]["re_entry"] = [tid]
        imported = bridge.import_model(model)
        result = bridge.closure_certificate(imported, [4])
        self.assertEqual(result["included"], [2, 4, 11, 15, 17, 29])
        self.assertEqual([(r["owner"], r["path"], r["target"]) for r in result["boundary"]["non_governing_references"]],
                         [(29, ["re_entry", 0], 32)])
        traversal_result = bridge.closure_certificate(imported, [32])
        self.assertEqual(traversal_result["included"], [32])
        self.assertEqual(traversal_result["boundary"]["non_governing_references"][0]["target"], 0)
        self.assertTrue(result["boundary"]["external"])
        self.assertFalse(any(ref["governing"] for ref in imported["references"] if ref["path"][0] == "owner"))
        # Removing optional governing-relation selection changes source contract,
        # not plain provenance references or immutable records.
        model["dependency_contract"]["required_relation_kinds"] = []
        reduced = bridge.import_model(model)
        self.assertNotIn(10, bridge.closure_certificate(reduced, [3])["included"])

    def test_all_residuals_remain_retained_or_explicitly_excluded(self):
        for seed in range(32):
            result = bridge.closure_certificate(self.imported, [seed])
            boundary = result["boundary"]
            self.assertEqual(sorted(boundary["retained_residuals"] + boundary["excluded_residuals"]), [29, 30, 31])
            for key, full_key in (("retained_residuals", "unresolved_residual_records"), ("excluded_residuals", "excluded_residual_records")):
                self.assertEqual(boundary[full_key], [self.imported["records"][i] for i in boundary[key]])

    def test_stale_imported_edge_reference_and_boolean_index_refuse(self):
        imported = deepcopy(self.imported)
        imported["edges"].remove([4, 29])
        with self.assertRaises(bridge.Refusal):
            bridge.closure_certificate(imported, [4])
        imported = deepcopy(self.imported)
        imported["references"][0]["path"] = ["changed"]
        with self.assertRaises(bridge.Refusal):
            bridge.check_imported(imported)
        imported = deepcopy(self.imported)
        imported["records"][0]["index"] = False
        with self.assertRaises(bridge.Refusal):
            bridge.check_imported(imported)

    def test_certificate_omitted_required_residual_is_refused(self):
        result = bridge.closure_certificate(self.imported, [4])
        result["included"].remove(29)
        result["order"].remove(29)
        result["excluded"].append(29)
        result["excluded"].sort()
        with self.assertRaisesRegex(bridge.Refusal, "dependency-closed"):
            bridge.check_certificate(self.imported, result)

    def test_certificate_unreachable_extra_and_invalid_order_refuse(self):
        result = bridge.closure_certificate(self.imported, [0])
        result["order"].append(1)
        result["included"].append(1)
        result["included"].sort()
        result["excluded"].remove(1)
        with self.assertRaisesRegex(bridge.Refusal, "unreachable"):
            bridge.check_certificate(self.imported, result)
        result = bridge.closure_certificate(self.imported, [3])
        result["order"] = list(reversed(result["order"]))
        with self.assertRaises(bridge.Refusal):
            bridge.check_certificate(self.imported, result)

    def test_projection_tampering_cannot_pass_a_core_certificate(self):
        for field in ("owner", "basis", "id", "context"):
            result = bridge.closure_certificate(self.imported, [0])
            result["records"][0]["record"][field] = "urn:changed"
            with self.assertRaises(bridge.Refusal):
                bridge.check_certificate(self.imported, result)
        for change in (
            lambda r: r["boundary"].update(excluded_residual_records=[]),
            lambda r: r["parent"].update(sha256="0" * 64),
            lambda r: r["selection"].update(seeds=[1]),
            lambda r: r["included"].__setitem__(0, False),
        ):
            result = bridge.closure_certificate(self.imported, [0])
            change(result)
            with self.assertRaises(bridge.Refusal):
                bridge.check_certificate(self.imported, result)

    def test_invalid_seed_and_budget_inputs_refuse(self):
        for seeds in ([], [32], [-1], [0, 0], [True], ["0"]):
            with self.assertRaises(bridge.Refusal):
                bridge.closure_certificate(self.imported, seeds)
        for budget in (-1, True, 3.0, "3"):
            with self.assertRaises(bridge.Refusal):
                bridge.closure_certificate(self.imported, [0], budget)

    def test_carrier_order_and_undirected_endpoint_reversal_preserve_model(self):
        carrier = deepcopy(self.carrier)
        carrier["nodes"].reverse()
        carrier["links"].reverse()
        for edge in carrier["links"]:
            edge["source"], edge["target"] = edge["target"], edge["source"]
        self.assertEqual(bridge.recover_carrier(carrier), self.model)

    def test_carrier_missing_duplicate_or_changed_edges_refuse(self):
        for mutate in (
            lambda c: c["links"].pop(),
            lambda c: c["links"].append(deepcopy(c["links"][0])),
            lambda c: c["links"][0].update(target="urn:missing"),
            lambda c: c["links"][0].update(ac_role="reference-target"),
        ):
            carrier = deepcopy(self.carrier)
            mutate(carrier)
            with self.assertRaises(bridge.Refusal):
                bridge.recover_carrier(carrier)

    def test_carrier_payload_display_or_occurrence_tamper_refuses(self):
        for role, mutate in (
            ("record", lambda n: n["ac_payload"]["record"].update(owner="urn:changed")),
            ("record", lambda n: n.update(label="false display")),
            ("record", lambda n: n["attributes"].update(semantic_identity="urn:changed")),
            ("reference-occurrence", lambda n: n["ac_payload"].update(path=["wrong"])),
            ("external", lambda n: n["ac_payload"].update(resolved_target_identity="urn:changed")),
            ("metadata", lambda n: n["ac_payload"]["model_identity"].update(sha256="0" * 64)),
        ):
            carrier = deepcopy(self.carrier)
            node = next(n for n in carrier["nodes"] if n["ac_role"] == role)
            mutate(node)
            with self.assertRaises(bridge.Refusal):
                bridge.recover_carrier(carrier)

    def test_carrier_contradictory_flags_and_extra_population_snapshot_refuse(self):
        for flag in ("directed", "multigraph"):
            for value in (True, 0):
                carrier = deepcopy(self.carrier)
                carrier[flag] = value
                with self.assertRaises(bridge.Refusal):
                    bridge.recover_carrier(carrier)
        carrier = deepcopy(self.carrier)
        next(n for n in carrier["nodes"] if n["ac_role"] == "metadata")["ac_payload"]["envelope"]["populations"] = {}
        with self.assertRaises(bridge.Refusal):
            bridge.recover_carrier(carrier)

    def test_actual_cli_success_and_budget_refusal(self):
        script = Path(bridge.__file__)
        success = subprocess.run([sys.executable, "-B", str(script), "--seed", "4", "--budget", "6"], capture_output=True, text=True)
        self.assertEqual(success.returncode, 0, success.stderr)
        self.assertEqual(json.loads(success.stdout)["result"]["included"], [2, 4, 11, 15, 17, 29])
        failure = subprocess.run([sys.executable, "-B", str(script), "--seed", "4", "--budget", "5"], capture_output=True, text=True)
        self.assertEqual(failure.returncode, 2, failure.stderr)
        refused = json.loads(failure.stdout)
        self.assertEqual(refused["status"], "refused")
        self.assertNotIn("result", refused)


if __name__ == "__main__":
    unittest.main()
