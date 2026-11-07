"""Installed proof-document links retain exact source custody and immutable targets."""
from __future__ import annotations

import json
from pathlib import Path
import posixpath
import re
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import urlsplit

import current_assets as a
import proof_reader_current as proof

ROOT = Path(__file__).resolve().parents[4]
PROOFS = ROOT / "specification_methodology/v3/build_tenants/common/standards/documentation/proofs"


def git_source(path):
    return subprocess.check_output(["git", "--no-optional-locks", "-C", str(ROOT), "show",
                                    proof.DOCUMENT_SOURCE_COMMIT + ":" + path])


class ProofDocumentLinks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.selection = json.loads((PROOFS / "SELECTION.json").read_bytes())
        cls.originals = {name: git_source(cls.selection[key]["path"])
                         for name, (key, _) in proof.DOCUMENT_LINKS.items()}

    def projected(self):
        files = dict(self.originals)
        proof.project_documents(files)
        return files

    def test_exact_source_bytes_are_retained_and_projection_is_distinct(self):
        files = self.projected()
        self.assertEqual(proof.source_document_files(files), self.originals)
        for name, (key, _) in proof.DOCUMENT_LINKS.items():
            self.assertEqual(a.sha(self.originals[name]), self.selection[key]["sha256"])
            self.assertNotEqual(files[name], self.originals[name])
            self.assertIn(b"require network access", files[name])
            self.assertIn(b"remain available offline", files[name])

    def test_all_five_targets_and_fragment_exist_at_exact_immutable_commit(self):
        count = 0
        for name, (key, links) in proof.DOCUMENT_LINKS.items():
            for relative, target in links:
                with self.subTest(target=target):
                    path, _, fragment = target.partition("#")
                    source_path = posixpath.normpath(posixpath.join(posixpath.dirname(self.selection[key]["path"]), relative))
                    self.assertEqual(source_path, target)
                    raw = git_source(path)
                    self.assertTrue(raw)
                    if path.endswith(".json"):
                        self.assertIsInstance(json.loads(raw), dict)
                    if fragment:
                        headings = re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", raw.decode(), re.M)
                        anchors = {re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-") for h in headings}
                        self.assertIn(fragment, anchors)
                    count += 1
        self.assertEqual(count, 5)

    def test_presented_links_are_exact_immutable_or_local_custody_targets(self):
        files = self.projected()
        for name, (_, links) in proof.DOCUMENT_LINKS.items():
            actual = re.findall(r"\]\(([^)]+)\)", files[name].decode())
            expected = ["source-documents/" + name + ".txt"] + [proof.DOCUMENT_SOURCE_URL + target for _, target in links]
            self.assertCountEqual(actual, expected)
            for target in actual:
                if urlsplit(target).scheme:
                    self.assertTrue(target.startswith(proof.DOCUMENT_SOURCE_URL))
                else:
                    self.assertIn(target, files)

    def test_unexpected_missing_or_duplicate_source_link_refuses(self):
        relative = proof.DOCUMENT_LINKS["correspondence.md"][1][0][0].encode()
        raw = self.originals["correspondence.md"]
        for changed in (raw.replace(relative, b"wrong.md"), raw + b"\n[duplicate](" + relative + b")\n"):
            with self.assertRaisesRegex(ValueError, "source documentation differs"):
                proof.project_document("correspondence.md", changed)

    def test_missing_custody_and_tampered_presentation_refuse(self):
        files = self.projected()
        del files["source-documents/correspondence.md.txt"]
        with self.assertRaisesRegex(ValueError, "custody missing"):
            proof.source_document_files(files)
        files = self.projected()
        files["correspondence.md"] = files["correspondence.md"].replace(proof.DOCUMENT_SOURCE_COMMIT.encode(), b"main")
        with self.assertRaisesRegex(ValueError, "projection differs"):
            proof.source_document_files(files)

    def test_current_generated_routes_and_source_pins_match_projection(self):
        files = self.projected()
        for path, raw in files.items():
            self.assertEqual((PROOFS / path).read_bytes(), raw)
        page = (PROOFS / "index.html").read_text()
        catalog = json.loads((PROOFS / "PROOFS.json").read_bytes())
        projection = catalog["documentation_projection"]
        self.assertEqual(projection["source_commit"], proof.DOCUMENT_SOURCE_COMMIT)
        for row in projection["documents"]:
            path = row["presentation"]["path"]
            self.assertIn('href="' + path + '"', page)
            self.assertEqual(row["presentation"]["sha256"], a.sha(files[path]))
            self.assertEqual(row["source"]["sha256"], a.sha(files[row["retained_path"]]))
        # The old library provenance remains historical; projection adds no proof.
        self.assertIn(b"2.5.1-rc.2", files["library-provenance.md"])
        self.assertIn(b"3.0.2", files["library-provenance.md"])

    def test_exact_pre_correction_payload_stays_checkable_without_a_link_claim(self):
        files = proof.source_document_files(a.read_tree(PROOFS))
        for name in ("PROOFS.json", "index.html"):
            relative = (PROOFS / name).relative_to(ROOT).as_posix()
            files[name] = subprocess.check_output(["git", "--no-optional-locks", "-C", str(ROOT), "show",
                                                   "6edfffb2f8a35b244782749383fb19105d9227d9:" + relative])
        result = proof.check_files(files)
        self.assertEqual(result["status"], "checked")
        self.assertEqual(result["documentation_links"], "retained-source-relative; installed targets not qualified")
        files["source-documents/correspondence.md.txt"] = files["correspondence.md"]
        with self.assertRaisesRegex(ValueError, "projection differs"):
            proof.check_files(files)


class RCProofDocumentLinks(unittest.TestCase):
    def test_rc_projection_uses_actual_checkpoint_and_current_product_targets(self):
        version = '3.0.5-rc.1'
        correspondence = f'a_c/build_tenants/graphify/design/fd-support-stdo-{version}.md'
        targets = ['a_c/specification/RELEASE_3_0_5.md',
                   f'a_c/build_tenants/graphify/design/fd-method-stdo-{version}.json',
                   'a_c/build_tenants/graphify/design/fd-support-stdo-3.0.1.md']
        library = proof.DOCUMENT_SOURCE_PINS['library_provenance']
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            def git(*args):
                return subprocess.check_output(['git','-c','user.name=Fixture','-c','user.email=fixture@example.invalid',
                                               '-c','commit.gpgsign=false','-C',str(root),*args],stderr=subprocess.PIPE)
            def write(path, raw):
                p=root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
            git('init','-q')
            for path in [library['path'], *(target for _, target in proof.DOCUMENT_LINKS['library-provenance.md'][1])]:
                write(path,git_source(path))
            git('add','.');git('commit','-qm','historical fixture');historical=git('rev-parse','HEAD').decode().strip()
            for path in [correspondence,*targets]:write(path,(ROOT/path).read_bytes())
            git('add','.');git('commit','-qm','current RC fixture');current=git('rev-parse','HEAD').decode().strip()
            def pin(path):return {'path':path,'sha256':a.sha((root/path).read_bytes())}
            selected={'version':version,'correspondence':pin(correspondence),'library_provenance':library,
                      'document_source_commit':current,'document_targets':[pin(path) for path in targets]}
            originals={'SELECTION.json':a.encoded(selected),'correspondence.md':(root/correspondence).read_bytes(),
                       'library-provenance.md':(root/library['path']).read_bytes()}
            with patch.object(proof,'DOCUMENT_SOURCE_COMMIT',historical):
                proof.validate_document_sources(root,originals)
                files=dict(originals);proof.project_documents(files)
                self.assertEqual(proof.source_document_files(files),originals)
                self.assertIn(current.encode(),files['correspondence.md'])
                self.assertIn(historical.encode(),files['library-provenance.md'])
                self.assertNotIn(current.encode(),files['library-provenance.md'])
                for _,target in proof.document_profile(originals)['correspondence.md']['links']:
                    self.assertIn(('/blob/'+current+'/'+target).encode(),files['correspondence.md'])
                # A real immutable target alone is insufficient when current
                # selected Product bytes have changed.
                target=root/targets[0];raw=target.read_bytes();target.write_bytes(raw+b'changed')
                with self.assertRaisesRegex(ValueError,'selected input differs'):proof.validate_document_sources(root,originals)
                target.write_bytes(raw)
                selected['document_source_commit']=historical
                originals['SELECTION.json']=a.encoded(selected)
                with self.assertRaisesRegex(ValueError,'unavailable'):proof.validate_document_sources(root,originals)

    def test_missing_rc_projection_selection_refuses(self):
        for selected in ({'version':'3.0.5-rc.1'}, {'version':'3.0.5-rc.1','document_source_commit':'main'}):
            with self.assertRaisesRegex(ValueError,'actual immutable'):
                proof.document_profile({'SELECTION.json':a.encoded(selected)})


if __name__ == "__main__":
    unittest.main()
