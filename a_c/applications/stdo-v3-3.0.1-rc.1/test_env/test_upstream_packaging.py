"""Actual pinned Graphify boundary on an explicitly synthetic, actor-free fixture."""
from pathlib import Path
from types import SimpleNamespace
import json
import os
import shutil
import subprocess
import sys
import unittest
from unittest.mock import patch

from test_application import APP, TemporaryFixture, synthetic_source, write
import application_contract as c
import bundle_check as checks
import public_receipts as receipts
import package_release as package
import ac_generate as g
import ac_graph as ac
import run_generation as runner


@unittest.skipUnless(os.environ.get("STDO301_GRAPHIFY_UPSTREAM"), "set explicit pinned upstream path for the actual-boundary fixture")
class ActualUpstreamPackaging(TemporaryFixture):
    def test_frozen_plan_tampering_refuses_at_actual_dispatch_boundary(self):
        synthetic_source(self.root)
        run = self.root / "synthetic-run"
        private = self.root / "private"; private.mkdir()
        upstream = Path(os.environ["STDO301_GRAPHIFY_UPSTREAM"])
        with patch.object(runner, "ROOT", self.root), patch.object(runner, "RUN", run), patch.object(runner, "PRIVATE", private):
            runner.prepare(upstream)
            plan, chunks = runner.checkpoint()
            self.assertGreater(len(g.graph_context(run, chunks[0], 40000)["nodes"]), len(g.graph_context(run, chunks[0], 1000)["nodes"]))
            grant_path = self.root / "synthetic-grant.json"
            write(grant_path, {"kind": "a_c.stdo301.generation-grant/1", "grant_id": "SIMULATION", "issuer": "/root",
                "source_contract_sha256": c.sha((self.root / "source-contract.json").read_bytes()),
                "scheduler_sha256": c.sha(Path(runner.__file__).read_bytes()), "operations": ["initial-batch"], "max_new_calls": 2})
            grant_sha = c.sha(grant_path.read_bytes())
            mutations = {"graph_chars": 1000, "chunk_chars": 1000, "mode": "direct",
                         "semantic_extraction_profile": "SIMULATION_WRONG", "calculus": {"uri": "urn:wrong", "sha256": "0" * 64},
                         "chunks": [], "claim": "SIMULATION_WRONG"}
            with patch.object(runner, "author_one", side_effect=RuntimeError("SIMULATION dispatch reached")) as dispatch, \
                 patch.object(runner, "actor_preflight", return_value=({"settings": {"model": "SIMULATION"}, "cli_version": "SIMULATION"}, {})) as preflight:
                for key, wrong in mutations.items():
                    with self.subTest(plan_field=key):
                        write(run / "plan.json", {**plan, key: wrong})
                        value = runner.grant(grant_path, grant_sha, "initial-batch")
                        with self.assertRaisesRegex(ValueError, "generation plan differs"):
                            runner.author_batch("initial-batch", value, grant_sha, "SIMULATION", [])
                        dispatch.assert_not_called(); preflight.assert_not_called()
                        self.assertFalse((private / "batches").exists())
                write(run / "plan.json", plan)
                value = runner.grant(grant_path, grant_sha, "initial-batch")
                with self.assertRaisesRegex(RuntimeError, "dispatch reached"):
                    runner.author_batch("initial-batch", value, grant_sha, "SIMULATION", [])
                dispatch.assert_called_once(); preflight.assert_called_once()

    def test_actual_python_source_graph_carrier_bundle_and_portable_rebuild(self):
        synthetic_source(self.root)
        upstream = Path(os.environ["STDO301_GRAPHIFY_UPSTREAM"])
        # Only synthetic test data is prepared. No CLI actor, native cut or actual review is used.
        run = self.root / "synthetic-run"
        plan = g.prepare(self.root / "source", self.root / "source-manifest.json", run, "graphify-ac", upstream)
        discovery = g.build_discovery(run, upstream)
        self.assertEqual(discovery["status"], "completed")
        structural = g.load(run / "discovery/structural.json")
        self.assertFalse(structural.get("failed_sources"))
        self.assertIn(str(run / "corpus/standards/examples/deterministic_contracts.py"), structural["extracted_sources"])
        chunks = g.load(run / "chunks.json")
        answers = {}
        for chunk in chunks:
            answer = {"concepts": [], "relations": [], "constraints": [], "latitude": [], "residuals": [], "dispositions": [],
                      "limitations": ["SIMULATION: hand-authored mechanics fixture, not semantic assessment or a native representation."]}
            for index, segment in enumerate(chunk["segments"]):
                key = "fixture_" + str(index)
                ground = {"section_id": segment["id"], "start_line": segment["start_line"], "end_line": segment["end_line"], "quote": segment["text"]}
                answer["concepts"].append({"key": key, "label": "Synthetic record " + str(index), "definition": "Synthetic record for carrier and browser plumbing tests.",
                                           "conditions": [], "exceptions": [], "grounding": [ground]})
                answer["dispositions"].append({"section_id": segment["id"], "decision": "retained", "keys": [key], "reason": "SIMULATION mechanics fixture."})
            g.author_check(answer, chunk)
            answers[chunk["id"]] = answer
        model, coverage = g.model_from_answers(plan, chunks, answers, [{"kind": "SIMULATION", "claim": "No actor call or semantic assessment."}])
        checked = ac.validate(model)
        carrier = ac.materialize(checked)
        modules = g.upstream_modules(upstream)
        graph = modules["build"].build_from_json(ac.extraction(carrier), dedup=False)
        communities = modules["cluster"].cluster(graph)
        proposal = self.root / "synthetic-proposal"; proposal.mkdir()
        self.assertTrue(modules["export"].to_json(graph, communities, str(proposal / "graph.json"), force=True, built_at_commit=g.UPSTREAM_COMMIT))
        self.assertEqual(ac.decode(ac.GraphCarrier(g.load(proposal / "graph.json"))).document, model)
        for name, value in (("model.json", model), ("carrier.json", carrier.document), ("coverage.json", coverage)):
            write(proposal / name, value)
        result = {"model_id": checked.identity, "model_sha256": checked.sha256, "processing_complete": True,
                  "family_counts": {key: len(value) for key, value in model["populations"].items()},
                  "files": {path.name: c.sha(path.read_bytes()) for path in proposal.iterdir()}}
        write(proposal / "result.json", result)
        shutil.copytree(APP / "release_tools", self.root / "release_tools", dirs_exist_ok=True)
        bindings = receipts.expected_bindings(self.root, checked, {name: proposal / name for name in receipts.ARTIFACTS})
        common = {"bindings": bindings, "scope": "SIMULATION: test-only packaging grammar and plumbing. No actual construction/review claim.", "details": {"simulation": True}}
        write(self.root / "synthetic-construction.json", {**common, "kind": receipts.CONSTRUCTION, "receipt_id": "urn:fixture:construction", "issuer": "urn:fixture:author", "construction_state": "complete", "private_material_included": False})
        write(self.root / "synthetic-review.json", {**common, "kind": receipts.REVIEW, "receipt_id": "urn:fixture:review", "issuer": "urn:fixture:reviewer", "review_state": "closed", "outcome": "SIMULATION", "independence": {"simulation": True}, "reports": []})
        bundle = self.root / "first/bundle"; dist = self.root / "first/dist"
        with patch.object(package, "ROOT", self.root):
            built = package.build(SimpleNamespace(proposal=proposal, graph=None, public_evidence=self.root / "synthetic-construction.json",
                review=[self.root / "synthetic-review.json"], upstream=upstream, bundle=bundle, dist=dist, display_limit=5000))
        self.assertEqual(built["checks"]["status"], "passed")
        replay = subprocess.run([sys.executable, "-B", "-S", str(bundle / "release_tools/bundle_check.py"), str(bundle)], capture_output=True, text=True)
        self.assertEqual(replay.returncode, 0, replay.stderr)
        self.assertEqual(json.loads(replay.stdout)["status"], "passed")
        for arguments in ([str(bundle / "release_tools/source_reentry.py"), "standards/ACTIVATION.md", "--start", "1", "--end", "3"],
                          [str(bundle / "codec/ac_graph.py"), "find", str(bundle / "carrier.json"), "Synthetic"],
                          [str(bundle / "codec/ac_graph.py"), "inspect", str(bundle / "carrier.json"), next(iter(checked.records))],
                          [str(bundle / "codec/ac_graph.py"), "project", str(bundle / "carrier.json"), "--seed", next(iter(checked.records)), "--out", str(self.root / "synthetic-projection.json")]):
            command = subprocess.run([sys.executable, "-B", "-S", *arguments], capture_output=True, text=True)
            self.assertEqual(command.returncode, 0, command.stderr)
            if "source_reentry.py" in arguments[0]:
                self.assertEqual(json.loads(command.stdout)["text"], (bundle / "source/standards/ACTIVATION.md").read_text())
        rebuilt_bundle = self.root / "second/bundle"; rebuilt_dist = self.root / "second/dist"
        rebuilt = subprocess.run([sys.executable, "-B", str(bundle / "package_release.py"), "build", "--proposal", str(bundle),
            "--public-evidence", str(bundle / "evidence/authoring-public.json"), "--review", str(bundle / "evidence/reviews/review-001/receipt.json"),
            "--upstream", str(upstream), "--bundle", str(rebuilt_bundle), "--dist", str(rebuilt_dist)], capture_output=True, text=True)
        self.assertEqual(rebuilt.returncode, 0, rebuilt.stderr)
        self.assertEqual(c.files(bundle), c.files(rebuilt_bundle))
        for name in c.files(bundle):
            self.assertEqual((bundle / name).read_bytes(), (rebuilt_bundle / name).read_bytes(), name)
        self.assertEqual((dist / (package.ARTIFACT + ".tar.gz")).read_bytes(), (rebuilt_dist / (package.ARTIFACT + ".tar.gz")).read_bytes())
        # Refreshing the transport inventory cannot authorize a duplicated identity.
        original_release = (bundle / "RELEASE.json").read_bytes()
        original_inventory = (bundle / "inventory.json").read_bytes()
        original_sums = (bundle / "SHA256SUMS").read_bytes()
        mutations = {"source_contract_sha256": "0" * 64, "represented_cut": "v3.0.0-rc.1",
            "builder_manifest_sha256": "0" * 64, "graphify_commit": "0" * 40, "codec_sha256": "0" * 64,
            "artifact": "wrong-artifact", "predecessor": "stdo://releases/v0.0.0/", "builder_basis": "stdo://releases/v3.0.1-rc.1/",
            "source_commit": "0" * 40, "package_tree": "0" * 40, "subject": "urn:wrong", "kind": "wrong-release"}
        for key, wrong in mutations.items():
            for missing in (False, True):
                with self.subTest(release_field=key, missing=missing):
                    release = json.loads(original_release)
                    if missing:
                        del release[key]
                    else:
                        release[key] = wrong
                    write(bundle / "RELEASE.json", release)
                    inventory = json.loads(original_inventory)
                    for row in inventory["files"]:
                        if row["path"] == "RELEASE.json":
                            row.update(bytes=(bundle / "RELEASE.json").stat().st_size, sha256=c.sha((bundle / "RELEASE.json").read_bytes()))
                    write(bundle / "inventory.json", inventory)
                    names = sorted([row["path"] for row in inventory["files"]] + ["inventory.json"])
                    (bundle / "SHA256SUMS").write_text("".join(f"{c.sha((bundle / name).read_bytes())}  {name}\n" for name in names))
                    replay = subprocess.run([sys.executable, "-B", "-S", str(bundle / "release_tools/bundle_check.py"), str(bundle)], capture_output=True, text=True)
                    self.assertEqual(replay.returncode, 2, replay.stdout)
                    self.assertIn("release identity differs from authenticated owner: " + key, replay.stderr)
        (bundle / "RELEASE.json").write_bytes(original_release)
        (bundle / "inventory.json").write_bytes(original_inventory)
        (bundle / "SHA256SUMS").write_bytes(original_sums)
        self.assertEqual(checks.check(bundle)["status"], "passed")
        changed = c.load(bundle / "carrier.json"); changed["nodes"].pop()
        write(bundle / "carrier.json", changed)
        with self.assertRaisesRegex(ValueError, "bundle bytes changed"):
            checks.check(bundle)


if __name__ == "__main__":
    unittest.main(verbosity=2)
