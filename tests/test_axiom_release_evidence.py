"""Actual current owner API and one coherently altered map carrier control.

The positive uses the retained real validator execution. The negative is an
explicit synthetic receipt mutation in a temporary tree, never an execution
claim. Neither test invokes the validator's map-writing command.
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORK = "specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/"
sys.path.insert(0, str(ROOT / "scripts"))
import check_stack_release as api

selected = Path(os.environ.get("STDO_EVIDENCE_TEST_SOURCE", ROOT / "scripts/stable_release_evidence.py"))
spec = importlib.util.spec_from_file_location("axiom_release_test_owner", selected)
owner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(owner)


class AxiomReleaseEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((ROOT / (WORK + "axiom-evidence-repair-017/manifest-fixture.json")).read_bytes())
        self.record = json.loads((ROOT / (WORK + "cohort-binding-001/axiom-validation-017/source_current_map.json")).read_bytes())

    def test_real_current_owner_relation(self):
        owner.representation(api.View(ROOT), self.record, "source_current_map", self.manifest, api)

    def test_rehashed_malformed_map_relation_refused(self):
        with tempfile.TemporaryDirectory(prefix="stdo-axiom-consumer-") as temporary:
            root = Path(temporary).resolve()
            facts = self.manifest["components"]["representation"]["facts"]
            refs = [self.manifest["source"], self.record["producer"], self.record["result"],
                    self.record["execution"]["stdout"], self.record["execution"]["stderr"],
                    *self.record["execution"]["inputs"], *self.record["execution"]["outputs"],
                    *(facts[key] for key in ("program", "model", "map", "bindings", "source_corpus", "preservation"))]
            helper = "axiom_indexer/build_tenants/core/code/ac_model.py"
            refs.append(next(row for row in self.manifest["products"]["axiom_indexer"]["subject"]["members"] if row["path"] == helper))
            for ref in refs:
                dest = root / ref["path"]
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes((ROOT / ref["path"]).read_bytes())
            record = copy.deepcopy(self.record)
            record["execution"]["argv"] = [arg.replace(str(ROOT), str(root), 1) if arg.startswith(str(ROOT) + "/") else arg
                                             for arg in record["execution"]["argv"]]
            record["execution"]["cwd"] = str(root)
            map_ref = facts["map"]
            value = json.loads((root / map_ref["path"]).read_bytes())
            value["injected_unowned_relation"] = "not emitted by the current owner"
            raw = (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()
            (root / map_ref["path"]).write_bytes(raw)
            changed = {"path": map_ref["path"], "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}
            facts["map"] = changed
            record["execution"]["outputs"] = [changed if row["path"] == changed["path"] else row
                                                for row in record["execution"]["outputs"]]
            with self.assertRaisesRegex(ValueError, "owning conversion/map functions"):
                owner.representation(api.View(root), record, "source_current_map", self.manifest, api)


if __name__ == "__main__":
    unittest.main()
