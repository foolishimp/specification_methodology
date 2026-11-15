#!/usr/bin/env python3
"""Source-derived successor-boundary controls over an exact native index.

EVALUATION section 5 requires predecessor dispositions at successor acceptance;
RELEASE section 9 supplies their meaning. These controls do not assess semantics
or perform acceptance. --amend-authoring exercises a declared repair on the
original exact source before the successor native cut exists.
"""
from __future__ import annotations

import argparse
import copy
from pathlib import Path
import sys
import unittest

import rebuild_release_indexes as release

core = release.core
catalog = release.catalog
PRODUCT = release.PRODUCT

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("--method-root", type=Path, required=True)
parser.add_argument("--index-id", required=True)
parser.add_argument("--amend-authoring", type=Path)
args, unittest_args = parser.parse_known_args()


class SuccessorBoundaries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        directory = PRODUCT / release.INDEXES / args.index_id
        cls.index = core.read_json(directory / "INDEX.json")
        cls.purpose = core.read_json(directory / "PURPOSE.json")
        sources = core.read_json(directory / "SOURCES.json")
        cls.manifest = catalog.source_binding({"sources": sources}, args.method_root, sources["method"])
        cls.predecessor = core.read_json(PRODUCT / release.INDEXES /
                                        "stdo-3.1.0-rc.1-sdlc-workflow-v1/INDEX.json")
        if args.amend_authoring:
            cls.authoring = core.read_json(args.amend_authoring)
            release.apply_sdlc_amendments(cls.index["rules"], args.method_root, cls.authoring)
        core.validate_index(cls.index, cls.manifest, cls.purpose, core.corpus_view(cls.manifest))
        cls.query = core.read_json(PRODUCT / "authoring/sdlc-workflow/queries/boundary-assessment.json")
        cls.query["id"] = "source-derived-successor-boundary-control"
        cls.query["facts"].update(
            operative_basis=sources["method"]["uri"] + " manifest " + sources["method"]["manifest_sha256"],
            grant="STDO_3_1_RC2_2026-11-15 authorized finite counterexample controls",
            target_product="urn:stdo:trial:rc2-successor-boundary-control",
            task="Construct constraints for a hypothetical successor decision; no boundary decision is performed.")

    def compile(self, boundary="product_acceptance", *, reuse=False):
        query = copy.deepcopy(self.query)
        query["facts"]["boundary_kind"] = boundary
        query["facts"]["reuse_evidence"] = reuse
        if boundary == "none":
            query["facts"]["action"] = "work"
            query["facts"]["review_in_scope"] = False
        if boundary == "missing":
            del query["facts"]["boundary_kind"]
        return core.compile_context(self.index, query, self.manifest, self.purpose,
                                    trial_binding="finite successor-boundary control", byte_budget=262144)

    @staticmethod
    def rule(payload, ident):
        return next((row for row in payload["selected"] if row["rule"]["id"] == ident), None)

    def test_successor_acceptance_receives_predecessor_dispositions(self):
        for reuse in [False, True]:
            with self.subTest(reuse_evidence=reuse):
                result = self.compile(reuse=reuse)
                payload = result["payload"]
                self.assertEqual(payload["selection_status"], "ready")
                self.assertEqual(payload["gaps"], [])
                selected = self.rule(payload, "W35")
                self.assertIsNotNone(selected, "EVALUATION section 5 successor acceptance must retain RELEASE section 9")
                self.assertEqual(selected["applicability"], "true")
                self.assertIn("## W35 (obligation)", result["markdown"])
                self.assertIn("disposition every predecessor claim", selected["rule"]["text"])

    def test_qualification_and_release_preserve_conservation(self):
        for boundary in ["qualification", "release"]:
            with self.subTest(boundary=boundary):
                payload = self.compile(boundary)["payload"]
                self.assertEqual(self.rule(payload, "W35")["applicability"], "true")
                self.assertEqual(payload["gaps"], [])

    def test_ordinary_work_does_not_become_successor_acceptance(self):
        payload = self.compile("none")["payload"]
        self.assertIsNone(self.rule(payload, "W35"))
        self.assertIn("W35", payload["excluded"])

    def test_unknown_boundary_retains_the_obligation_as_unresolved(self):
        for boundary in ["missing", None, False, 3]:
            with self.subTest(boundary=boundary):
                payload = self.compile(boundary)["payload"]
                self.assertEqual(payload["selection_status"], "incomplete")
                self.assertEqual(self.rule(payload, "W35")["applicability"], "unknown")
                self.assertTrue(any(row["rule"] == "W35" for row in payload["gaps"]))
                self.assertFalse(payload["covered"])

    def test_dependencies_keep_their_own_applicability(self):
        payload = self.compile(reuse=False)["payload"]
        self.assertEqual(self.rule(payload, "W35")["applicability"], "true")
        self.assertEqual(self.rule(payload, "W26")["applicability"], "false")
        self.assertEqual(self.rule(payload, "W28")["applicability"], "false")
        self.assertEqual(self.compile("release")["payload"]["selection_status"], "ready")
        self.assertEqual(self.rule(self.compile("release")["payload"], "W26")["applicability"], "true")

    def test_only_w35_guard_changes_from_rc1(self):
        self.assertEqual(len(self.index["rules"]), 40)
        changes = {old["id"]: [field for field in old if old[field] != new[field]]
                   for old, new in zip(self.predecessor["rules"], self.index["rules"], strict=True)}
        self.assertEqual({ident: fields for ident, fields in changes.items() if fields}, {"W35": ["when"]})

    def test_delivery_does_not_manufacture_semantic_support_or_acceptance(self):
        payload = self.compile()["payload"]
        self.assertFalse(payload["covered"])
        self.assertEqual(payload["semantic_coverage"], {"assessment": None, "status": "unassessed"})
        self.assertEqual(payload["use"], "experimental-candidate")

    def test_preimage_guard_mismatch_refuses_reapplication(self):
        authoring = core.read_json(PRODUCT / "authoring/release-targets/3.1.0-rc.2.json")
        repaired = copy.deepcopy(self.predecessor["rules"])
        release.apply_sdlc_amendments(repaired, args.method_root, authoring)
        with self.assertRaisesRegex(core.Refusal, "amendment predecessor differs"):
            release.apply_sdlc_amendments(repaired, args.method_root, authoring)


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0], *unittest_args], verbosity=2)
