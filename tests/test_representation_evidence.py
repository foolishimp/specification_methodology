"""Finite fixture controls for the current model construction evidence adapter.

These test receipt interpretation, not process provenance. The release work
retains a separate actual owner readback against the full current model.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_stack_release as api
import stable_release_evidence as owner


class RepresentationEvidenceTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.run = "stdo_representation/run"
        self.prefix = "source"
        source = self.put("stdo_representation/source/standards/ONE.md", b"one exact source\n")
        members = [{"path": "standards/ONE.md", "bytes": source["bytes"], "sha256": source["sha256"]}]
        files = [{**members[0], "path": "source/standards/ONE.md"}]
        basis = {"uri": "stdo://releases/v3.0.4/", "manifest_sha256": "a" * 64}
        definition = {"product": {"definition_id": "fixture-product"}, "constitution": {"stdo": {"basis": basis}}}
        defined = self.put("stdo_representation/product.json", definition)
        retained = self.put(self.run + "/product-definition.json", definition)
        corpus = self.put(self.run + "/source-manifest.json", {"files": files, "subject_id": "fixture-source",
            "definition_id": "fixture-product", "definition_sha256": defined["sha256"], "method": basis})
        plan = self.put(self.run + "/generation/plan.json", {"files": files, "subject_id": "fixture-source"})
        project = self.put(self.run + "/PROJECT.json", {"profile": "a_c.project-build/1", "files": files,
            "subject_id": "fixture-source", "project": str(self.root / "stdo_representation"),
            "definition": str(self.root / defined["path"]), "definition_sha256": defined["sha256"],
            "manifest_sha256": corpus["sha256"], "plan_sha256": plan["sha256"], "method": basis})
        model = {"id": "fixture-model", "profile": "a_c.graphify.model/1",
                 "basis": {"subject": {"id": "fixture-source", "sha256": api.canonical_value_sha256(files)}}}
        canonical = self.put("stdo_representation/model.json", model)
        generated = self.put(self.run + "/generation/proposal/model.json", model)
        identity = {"id": model["id"], "sha256": api.canonical_value_sha256(model), "profile": model["profile"]}
        semantic = self.put("source-freeze.json", {"members": members, "native_contracts": []})
        binding = self.put("binding.json", {"source_identity_sha256": "b" * 64,
            "source_freeze_raw_sha256": semantic["sha256"], "model_raw_sha256": canonical["sha256"], "model_identity": identity})
        self.facts = {"model": canonical, "model_sha256": canonical["sha256"],
            "model_canonical_sha256": identity["sha256"], "build_run": self.run,
            "source_copy_prefix": self.prefix, "current_binding": binding, "project": project,
            "source_manifest": corpus, "generation_plan": plan, "definition": defined,
            "retained_definition": retained, "generated_model": generated}
        self.manifest = {"source": {**semantic, "source_identity_sha256": "b" * 64},
            "products": {"stdo_representation": {"source_root": "stdo_representation"}},
            "components": {"representation": {"facts": self.facts}}}
        result = {"profile": "a_c.project-build-result/1", "status": "reused", "method": basis,
            "project_sha256": project["sha256"], "source_manifest_sha256": corpus["sha256"],
            "subject_id": "fixture-source", "model": {"id": identity["id"], "sha256": identity["sha256"]},
            "artifacts": {"model": str(self.root / generated["path"])},
            "files": {"generation/proposal/model.json": generated["sha256"]}}
        output = self.put("stdout.json", result)
        stderr = self.put("stderr", b"")
        producer = self.put(owner.PROJECT, b"# controlled synthetic receipt fixture; never executed\n")
        python = Path(sys.executable)
        self.record = {"producer": producer, "result": output, "operation": "current_build_readback",
            "execution": {"argv": [str(python), "-B", str(self.root / owner.PROJECT), "build", "--run", str(self.root / self.run)],
                "cwd": str(self.root), "returncode": 0, "environment": {"python": {
                    "invocation": str(python), "executable_realpath": str(python.resolve()),
                    "sha256": hashlib.sha256(python.resolve().read_bytes()).hexdigest(), "version": sys.version.split()[0]}},
                "inputs": [project, corpus, plan, defined, retained, generated], "outputs": [output],
                "stdout": output, "stderr": stderr}}

    def put(self, name, value):
        raw = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return {"path": name, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}

    def check(self):
        return owner.representation(api.View(self.root, None), self.record, "source_current_model", self.manifest, api)

    def rewrite_fact(self, key, mutation):
        old = self.facts[key]
        value = json.loads((self.root / old["path"]).read_bytes())
        mutation(value)
        new = self.put(old["path"], value)
        self.facts[key] = new
        self.record["execution"]["inputs"] = [new if row == old else row for row in self.record["execution"]["inputs"]]

    def rewrite_result(self, mutation):
        value = json.loads((self.root / self.record["result"]["path"]).read_bytes())
        mutation(value)
        result = self.put("stdout.json", value)
        self.record["result"] = self.record["execution"]["stdout"] = result
        self.record["execution"]["outputs"] = [result]

    def test_readback_binds_inputs_and_current_artifact(self):
        self.check()

    def test_built_status_requires_produced_model_output(self):
        self.rewrite_result(lambda result: result.update(status="built"))
        self.record["operation"] = "emitted_model"
        with self.assertRaisesRegex(ValueError, "produced/read-back role"):
            self.check()
        self.record["execution"]["outputs"].append(self.facts["generated_model"])
        self.check()

    def test_wrong_project_root_refuses_even_rehashed(self):
        self.rewrite_fact("project", lambda value: value.update(project=str(self.root / "other")))
        with self.assertRaisesRegex(ValueError, "project/source/plan"):
            self.check()

    def test_wrong_source_input_refuses_even_rehashed(self):
        self.rewrite_fact("source_manifest", lambda value: value.update(files=[]))
        with self.assertRaisesRegex(ValueError, "project/source/plan"):
            self.check()

    def test_wrong_plan_input_refuses_even_rehashed(self):
        self.rewrite_fact("generation_plan", lambda value: value.update(subject_id="different"))
        with self.assertRaisesRegex(ValueError, "project/source/plan"):
            self.check()

    def test_wrong_generated_model_refuses_even_rehashed(self):
        self.rewrite_fact("generated_model", lambda value: value.update(id="different"))
        with self.assertRaisesRegex(ValueError, "actual generated model"):
            self.check()

    def test_readback_cannot_be_labelled_emission(self):
        self.record["operation"] = "emitted_model"
        with self.assertRaisesRegex(ValueError, "status/operation"):
            self.check()

    def test_result_cannot_name_another_project(self):
        self.rewrite_result(lambda value: value.update(project_sha256="c" * 64))
        with self.assertRaisesRegex(ValueError, "different construction project"):
            self.check()

    def test_actual_construction_inputs_cannot_be_replaced_by_canonical_output(self):
        self.record["execution"]["inputs"] = [self.facts["model"]]
        with self.assertRaisesRegex(ValueError, "input closure"):
            self.check()


if __name__ == "__main__":
    unittest.main()
