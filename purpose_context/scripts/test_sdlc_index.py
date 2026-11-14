#!/usr/bin/env python3
"""Finite mechanical controls; these supply no semantic assessment verdict."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

PRODUCT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRODUCT / "skills/stdo-context/scripts"))
import context_core as core
import context_catalog as catalog
import context as cli
import rebuild_sdlc_index as rebuild


class SDLCControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pin = core.raw_digest((PRODUCT / "PUBLIC_MANIFEST.json").read_bytes())
        cls.access = catalog.public_bundle(cls.pin)
        cls.item = catalog.find_entry(cls.access, rebuild.INDEX_ID)
        cls.source = PRODUCT / rebuild.RELATIVE / "source"
        cls.query = core.read_json(PRODUCT / "authoring/sdlc-workflow/queries/ordinary-repair.json")

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="sdlc-control-")
        self.root = Path(self.temporary.name).resolve()
        self.addCleanup(self.temporary.cleanup)

    def bind(self, item=None, root=None):
        item = item or self.item
        return catalog.source_binding(item, root or self.source, item["sources"]["method"])

    def changed_source(self):
        target = self.root / "source"
        shutil.copytree(self.source, target)
        return target

    def repin_candidate(self, source, change):
        manifest = core.read_json(source / "manifest.json")
        change(manifest)
        (source / "manifest.json").write_bytes(rebuild.encoded(manifest))
        item = copy.deepcopy(self.item)
        item["sources"]["method"]["manifest_sha256"] = core.raw_digest((source / "manifest.json").read_bytes())
        return item

    def bundle(self):
        bundle = self.root / "bundle"
        manifest = self.bind()
        cli.prepare_manifest(manifest, self.item["purpose"], bundle)
        cli.write_new(bundle / "REUSE-BINDING.json", catalog.binding_receipt(self.access, self.item, self.source))
        return bundle, *cli.load_bundle(bundle)

    def selected(self, query):
        bundle, manifest, purpose, view = self.bundle()
        return catalog.select(self.access, bundle, manifest, purpose, view, query, rebuild.INDEX_ID)[0]

    def compile(self, query=None, assessment=None, budget=131072):
        return core.compile_context(self.item["index"], query or self.query, self.bind(), self.item["purpose"],
                                    assessment, trial_binding="finite-author-control", byte_budget=budget)

    def test_candidate_exact_binding_and_selection(self):
        self.assertEqual(self.selected(self.query)["status"], "selected")

    def test_candidate_portable_copy(self):
        self.assertEqual(self.bind(root=self.changed_source())["method"], self.item["sources"]["method"])

    def test_actual_manifest_drift_refused(self):
        root = self.changed_source()
        with (root / "manifest.json").open("ab") as handle:
            handle.write(b" ")
        with self.assertRaisesRegex(core.Refusal, "actual method manifest differs"):
            self.bind(root=root)

    def test_actual_owner_drift_refused(self):
        root = self.changed_source()
        with (root / "standards/ACTIVATION.md").open("ab") as handle:
            handle.write(b"\nchanged source\n")
        with self.assertRaisesRegex(core.Refusal, "actual selected source differs"):
            self.bind(root=root)

    def test_missing_owner_refused(self):
        root = self.changed_source()
        (root / "standards/TICKETS.md").unlink()
        with self.assertRaises(core.Refusal):
            self.bind(root=root)

    def test_owner_symlink_refused(self):
        root = self.changed_source()
        path = root / "standards/TICKETS.md"
        path.unlink()
        path.symlink_to(self.source / "standards/TICKETS.md")
        with self.assertRaisesRegex(core.Refusal, "regular file"):
            self.bind(root=root)

    def test_development_cannot_impersonate_release(self):
        root = self.changed_source()
        item = self.repin_candidate(root, lambda value: value.update(method_uri="stdo://releases/v3.0.6/"))
        item["sources"]["method"]["uri"] = "stdo://releases/v3.0.6/"
        with self.assertRaisesRegex(core.Refusal, "development method identity"):
            self.bind(item, root)

    def test_development_cannot_claim_published_standing(self):
        root = self.changed_source()
        item = self.repin_candidate(root, lambda value: value.update(standing="published"))
        with self.assertRaisesRegex(core.Refusal, "development method identity"):
            self.bind(item, root)

    def test_candidate_member_order_refused(self):
        root = self.changed_source()
        item = self.repin_candidate(root, lambda value: value["standards"]["members"].reverse())
        with self.assertRaisesRegex(core.Refusal, "closure/order"):
            self.bind(item, root)

    def test_duplicate_candidate_member_refused(self):
        root = self.changed_source()
        item = self.repin_candidate(root, lambda value: value["standards"]["members"].append(value["standards"]["members"][0]))
        with self.assertRaisesRegex(core.Refusal, "unique"):
            self.bind(item, root)

    def test_candidate_member_path_escape_refused(self):
        root = self.changed_source()
        item = self.repin_candidate(root, lambda value: value["standards"]["members"][0].update(path="../manifest.json"))
        with self.assertRaisesRegex(core.Refusal, "nonportable"):
            self.bind(item, root)

    def test_wrong_selected_method_refused(self):
        wrong = {**self.item["sources"]["method"], "uri": "stdo://releases/v3.0.4/"}
        with self.assertRaisesRegex(core.Refusal, "selected method differs"):
            catalog.source_binding(self.item, self.source, wrong)

    def test_old_public_pin_refused(self):
        with self.assertRaisesRegex(core.Refusal, "public manifest differs"):
            catalog.public_bundle("0" * 64)

    def test_false_family_refused(self):
        query = copy.deepcopy(self.query)
        query["facts"]["adopted_defaults"] = False
        self.assertEqual(self.selected(query)["status"], "refused")

    def test_missing_family_incomplete(self):
        query = copy.deepcopy(self.query)
        del query["facts"]["adopted_defaults"]
        self.assertEqual(self.selected(query)["status"], "incomplete")

    def test_typed_family_no_integer_boolean_coercion(self):
        query = copy.deepcopy(self.query)
        query["facts"]["adopted_defaults"] = 1
        self.assertEqual(self.selected(query)["status"], "incomplete")

    def test_unsupported_boundary_refused(self):
        query = copy.deepcopy(self.query)
        query["facts"]["boundary_kind"] = "invented-boundary"
        self.assertEqual(self.selected(query)["status"], "refused")

    def test_unknown_boundary_incomplete(self):
        query = copy.deepcopy(self.query)
        del query["facts"]["boundary_kind"]
        self.assertEqual(self.selected(query)["status"], "incomplete")

    def test_unknown_conditional_fact_remains_gap(self):
        query = copy.deepcopy(self.query)
        del query["facts"]["profile_executive"]
        result = self.compile(query)["payload"]
        self.assertEqual(result["selection_status"], "incomplete")
        self.assertTrue(any(row["rule"] == "W20" for row in result["gaps"]))
        self.assertFalse(result["covered"])

    def test_actual_branch_selection(self):
        query = copy.deepcopy(self.query)
        adopted = self.compile(query)["payload"]
        query["facts"]["profile_executive"] = False
        other_configuration = self.compile(query)["payload"]
        self.assertIn("W20", other_configuration["excluded"])
        self.assertTrue(any(row["rule"]["id"] == "W20" and row["applicability"] == "true" for row in adopted["selected"]))

    def test_first_attempt_capability_limit_retains_diagnostic_constraint(self):
        query = core.read_json(PRODUCT / "authoring/sdlc-workflow/queries/first-capability-limit.json")
        self.assertIs(query["facts"]["recurring_failure"], False)
        first = self.compile(query)["payload"]
        query["facts"]["recurring_failure"] = True
        recurring = self.compile(query)["payload"]
        select = lambda value: [row for row in value["selected"] if row["rule"]["id"] == "W12"]
        self.assertEqual(len(select(first)), 1)
        self.assertEqual(select(first)[0]["applicability"], "true")
        self.assertEqual(select(first), select(recurring))

    def test_no_automatic_semantic_coverage(self):
        result = self.compile()["payload"]
        self.assertEqual(result["semantic_coverage"]["status"], "unassessed")
        self.assertFalse(result["covered"])

    def test_wrong_query_assessment_refused(self):
        value = {"index_sha256": core.digest(self.item["index"]), "corpus_sha256": self.item["index"]["corpus_sha256"],
                 "query_sha256": "0" * 64, "status": "unknown", "evaluator": "mechanical-negative-fixture", "evidence": ["No semantic assessment is claimed."]}
        with self.assertRaisesRegex(core.Refusal, "assessment exact subject differs"):
            self.compile(assessment=value)

    def test_complete_context_budget_refuses(self):
        result = self.compile()
        with self.assertRaisesRegex(core.Refusal, "budget insufficient"):
            self.compile(budget=len(core.canonical(result)))

    def test_rendered_delivery_mutation_refused(self):
        result = self.compile()
        result["markdown"] += "unexpected content\n"
        with self.assertRaises(core.Refusal):
            core.check_context(result, self.item["index"], self.query, self.bind(), self.item["purpose"], None,
                               trial_binding="finite-author-control")

    def test_same_index_reused_by_second_product(self):
        query = copy.deepcopy(self.query)
        query["id"] = "second-independent-query"
        query["facts"]["target_product"] = "urn:example:product:second"
        self.assertEqual(self.compile()["payload"]["index_sha256"], self.compile(query)["payload"]["index_sha256"])
        self.assertEqual(self.selected(query)["status"], "selected")

    def test_rebuild_exact_snapshot(self):
        output = self.root / "rebuilt"
        rebuild.generate(self.source / "standards", output)
        for path in output.rglob("*"):
            if path.is_file():
                self.assertEqual(path.read_bytes(), (PRODUCT / rebuild.RELATIVE / path.relative_to(output)).read_bytes())

    def test_changed_deciding_ground_requires_author_reentry(self):
        root = self.changed_source()
        path = root / "standards/SDLC_DEFAULTS.md"
        path.write_text(path.read_text().replace("merely installing or finding it selects nothing", "installing it automatically selects it"))
        with self.assertRaisesRegex(core.Refusal, "source ground changed"):
            rebuild.generate(root / "standards", self.root / "rebuild")


if __name__ == "__main__":
    unittest.main(verbosity=2)
