"""Current documentation must retain the published example without relabelling it."""
import json
import os
from pathlib import Path
import unittest

import current_assets as assets
import documentation_current as docs


@unittest.skipUnless(os.environ.get("STDO_CURRENT_DOCUMENTATION"), "select an exact generated documentation fixture")
class FrozenCodeExampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = assets.read_tree(Path(os.environ["STDO_CURRENT_DOCUMENTATION"]))

    def selection(self, files, edit):
        value = json.loads(files["SELECTION.json"])
        edit(value)
        files["SELECTION.json"] = assets.encoded(value)

    def test_complete_current_payload_and_distinct_frozen_subject(self):
        result = docs.check_files(self.files)
        metadata = json.loads(self.files["DOCUMENTATION.json"])
        example = json.loads(self.files["code-explorer/EXAMPLE.json"])
        proof = json.loads(self.files["proofs/PROOFS.json"])
        self.assertEqual(result["status"], "checked")
        self.assertEqual(example["role"], "frozen-example-only")
        self.assertEqual(example["publication"]["commit"], "16bc30d215915a4b7b3ed2f13e52e14510ae1c9d")
        self.assertEqual(assets.sha(self.files["code-explorer/index.html"]), "26e8e1e93221781b7a25fc48ad457c7ea97275cd08dcadba91075cbf8b1be8c9")
        self.assertEqual(metadata["retained_examples"], [example])
        self.assertEqual(proof["model"], metadata["model"])
        self.assertNotEqual(example["model"]["id"], metadata["model"]["id"])
        self.assertIn(b'Frozen ABI code example', self.files["index.html"])
        self.assertIn(b'not current ABI qualification', self.files["README.md"])

    def test_missing_promised_route_or_identity_refuses(self):
        for path in ("code-explorer/index.html", "code-explorer/EXAMPLE.json"):
            with self.subTest(path=path):
                files = dict(self.files); del files[path]
                with self.assertRaisesRegex(ValueError, "required frozen ABI example"):
                    docs.check_files(files)

    def test_tampered_example_refuses_even_with_rehashed_selection(self):
        files = dict(self.files); files["code-explorer/index.html"] += b"\n"
        self.selection(files, lambda value: value["code_example"]["artifact"].update(sha256=assets.sha(files["code-explorer/index.html"])))
        with self.assertRaisesRegex(ValueError, "published ABI example bytes differ"):
            docs.check_files(files)

    def test_current_qualification_label_or_false_publication_refuses(self):
        for edit in (lambda value: value["code_example"].update(role="current-qualified"),
                     lambda value: value["code_example"]["publication"].update(commit="0" * 40)):
            files = dict(self.files); self.selection(files, edit)
            with self.assertRaisesRegex(ValueError, "frozen ABI example selection differs"):
                docs.check_files(files)

    def test_relabelled_example_metadata_refuses(self):
        files = dict(self.files); metadata = json.loads(files["code-explorer/EXAMPLE.json"])
        metadata["limits"] = []; files["code-explorer/EXAMPLE.json"] = assets.encoded(metadata)
        with self.assertRaisesRegex(ValueError, "frozen example metadata differs"):
            docs.check_files(files)

    def test_frozen_example_cannot_substitute_for_current_viewer(self):
        files = dict(self.files); files["constraint-explorer/index.html"] = files["code-explorer/index.html"]
        self.selection(files, lambda value: value["viewer"].update(sha256=assets.sha(files["constraint-explorer/index.html"])))
        with self.assertRaisesRegex(ValueError, "viewer/model identity differs"):
            docs.check_files(files)


if __name__ == "__main__":
    unittest.main()
