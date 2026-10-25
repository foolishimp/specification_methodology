"""Synthetic binding controls using the real authored model/carriers; no Git effects."""
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import copy
import importlib.util
import json
import subprocess
import sys
import tarfile
import tempfile
import unittest

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[5]
spec=importlib.util.spec_from_file_location('supplement',HERE/'supplement.py');s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)

class Controls(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='supplement-fixture-',dir=HERE)
        self.root=Path(self.temp.name)
    def tearDown(self):self.temp.cleanup()
    def args(self):
        plan=s.read(HERE.parent/'representation/PLAN.json')
        rows=[{'path':x['path'],'sha256':x['sha256']} for x in plan['files']]
        rows.append({'path':'LICENSE','sha256':s.sha((REPO/'specification_methodology/v3/build_tenants/common/LICENSE').read_bytes())})
        native={'cut':'v3.0.2','commit':'1'*40,'tag_object':'2'*40,'tree':'3'*40,'standards_tree':'4'*40,'qualified_ref':'refs/tags/specification_methodology/v3.0.2','package_path':'specification_methodology/v3','package_tree':'5'*40}
        release={k:native[k] for k in ('cut','commit','tag_object','tree','standards_tree','qualified_ref')}
        release.update(profile='stable-v1',project_subtree_root=native['package_path'],project_subtree_tree=native['package_tree'])
        manifest=s.canonical({'release':release,'standards':{'members':[{'path':x['path'].removeprefix('standards/'),'sha256':x['sha256']} for x in rows if x['path'].startswith('standards/')]}})
        native['manifest_sha256']=s.sha(manifest)
        selection=s.canonical({'kind':'a_c.stdo302.native-source-selection/1','native':native,'files':rows,'fixture':'synthetic metadata only; not a Git release'})
        (self.root/'SOURCE_SELECTION.json').write_bytes(selection);(self.root/'stdo-v3.0.2-manifest.json').write_bytes(manifest)
        return SimpleNamespace(repo=REPO,representation=HERE.parent/'representation',selection=self.root/'SOURCE_SELECTION.json',selection_sha256=s.sha(selection),bundle=self.root/'bundle',archive=self.root/'out.tar.gz')
    def test_portable_archive_verification_from_outside_workspace(self):
        args=self.args();result=s.build(args);self.assertEqual(result['verification']['recovery'],'equal JSON values; raw serialization equality not claimed')
        extracted=self.root/'extracted'
        with tarfile.open(args.archive) as tar:tar.extractall(extracted,filter='data')
        bundle=extracted/s.PREFIX
        p=subprocess.run([sys.executable,'-I','-B',str(bundle/'supplement.py'),'verify','--bundle',str(bundle)],cwd='/tmp',capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stdout+p.stderr)
    def test_archive_inside_bundle_refused_before_write(self):
        args=self.args();args.archive=args.bundle/'out.tar.gz'
        with self.assertRaisesRegex(ValueError,'overlapping'):s.build(args)
        self.assertFalse(args.bundle.exists())
    def test_parent_traversal_output_refused(self):
        args=self.args();args.bundle=HERE/'..'/'escaped'
        with self.assertRaisesRegex(ValueError,'outside'):s.build(args)
    def test_refreshed_inventory_cannot_hide_identity_contradiction(self):
        args=self.args();s.build(args);payload=s.files(args.bundle)
        manifest=json.loads(payload['NATIVE_MANIFEST.json']);manifest['release']['commit']='9'*40
        payload['NATIVE_MANIFEST.json']=s.canonical(manifest)
        selection=json.loads(payload['SOURCE_SELECTION.json']);selection['native']['manifest_sha256']=s.sha(payload['NATIVE_MANIFEST.json']);payload['SOURCE_SELECTION.json']=s.canonical(selection)
        with self.assertRaisesRegex(ValueError,'native identity mismatch: commit'):s.check_binding(payload)
    def test_native_source_change_refuses(self):
        args=self.args();s.build(args);payload=s.files(args.bundle);payload['source/standards/RELEASE.md']+=b'changed\n'
        with self.assertRaisesRegex(ValueError,'source mismatch'):s.check_binding(payload)

if __name__=='__main__':unittest.main(verbosity=2)
