"""Tampering controls over an actual cold bundle; run with explicit fixture paths."""
from pathlib import Path
import copy
import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import formal_gate as gate


@unittest.skipUnless(os.environ.get('AC_INSPECTION_BUNDLE') and os.environ.get('AC_INSPECTION_REQUEST'), 'Select an actual cold proof fixture for inspection controls')
class InspectionTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name).resolve();self.bundle=self.root/'bundle'
        shutil.copytree(os.environ['AC_INSPECTION_BUNDLE'],self.bundle)
        self.request=json.loads(Path(os.environ['AC_INSPECTION_REQUEST']).read_text())
        self.result=json.loads((self.bundle/'result.json').read_text())

    def write(self,name,value): (self.bundle/name).write_text(json.dumps(value,sort_keys=True,indent=2)+'\n')

    def reseal(self):
        manifest={'schema':'a_c.formal-gate.bundle/1','members':{p.name:gate.support.sha(p) for p in self.bundle.iterdir() if p.name not in ('result.json','manifest.json','local-origin.json')}}
        self.write('manifest.json',manifest)
        self.result['evidence']={'manifest_sha256':gate.support.sha(self.bundle/'manifest.json'),'members':manifest['members']}
        self.write('result.json',self.result)

    def inspect(self): return gate.inspect_evidence(self.bundle,self.request)

    def test_actual_cold_bundle_is_consistent_without_effects(self):
        before={p.name:p.read_bytes() for p in self.bundle.iterdir()}
        result=self.inspect();self.assertEqual(result['status'],'consistent',result)
        self.assertEqual(len(result['required_claims']),5)
        self.assertEqual({p.name:p.read_bytes() for p in self.bundle.iterdir()},before)
        self.assertIn('not a new execution verdict',result['limits'][0])

    def test_equal_arbitrary_claim_lists_are_refused(self):
        self.result['requested_claims']=self.result['checked_claims']=['invented-obligation']
        self.write('result.json',self.result)
        self.assertNotEqual(self.inspect()['status'],'consistent')

    def test_missing_object_is_refused_even_after_manifest_resealed(self):
        (self.bundle/'GateModel.olean').unlink();self.reseal()
        self.assertNotEqual(self.inspect()['status'],'consistent')

    def test_uninventoried_extra_file_is_refused(self):
        (self.bundle/'unexpected').write_text('extra')
        self.assertNotEqual(self.inspect()['status'],'consistent')

    def test_self_consistent_fake_runtime_pins_are_refused(self):
        pins={'invented.py':'0'*64};self.result['runtime_identity']={'sha256':gate.digest(pins),'pins':pins}
        self.write('result.json',self.result)
        self.assertNotEqual(self.inspect()['status'],'consistent')

    def test_unsupported_axiom_is_refused_after_all_saved_claims_are_changed(self):
        (self.bundle/'GateModel.log').write_text("'AC.GateData.model_checked' depends on axioms: [sorryAx]\n")
        self.result['observations']['theorem_audit']['AC.GateData.model_checked']=['sorryAx'];self.reseal()
        self.assertNotEqual(self.inspect()['status'],'consistent')

    def test_later_duplicate_cannot_hide_an_unsupported_axiom(self):
        log=(self.bundle/'GateModel.log').read_text()
        (self.bundle/'GateModel.log').write_text("'AC.GateData.model_checked' depends on axioms: [sorryAx]\n"+log)
        self.reseal();self.assertNotEqual(self.inspect()['status'],'consistent')

    def test_zero_execution_counters_do_not_claim_cold_replay(self):
        self.result['observations']['current_kernel_replay_invocations']=0;self.write('result.json',self.result)
        self.assertNotEqual(self.inspect()['status'],'consistent')

    def test_changed_generated_proof_source_is_refused_after_reseal(self):
        with (self.bundle/'GateViews.lean').open('a') as stream:stream.write('\n-- altered proof source\n')
        self.reseal();self.assertNotEqual(self.inspect()['status'],'consistent')

    def test_supplied_view_omission_refuses_consistent_rebinding(self):
        views=json.loads((self.bundle/'supplied-views.json').read_text())
        population=next(rows for rows in views[0]['populations'].values() if rows)
        population.pop()
        self.write('supplied-views.json',views)
        raw=(self.bundle/'supplied-views.json').read_bytes();sha=gate.reuse.sha(raw)
        self.request['supplied_views']={'path':str(self.bundle/'supplied-views.json'),'raw_sha256':sha}
        original=json.loads((self.bundle/'request.json').read_text());original['supplied_views']=self.request['supplied_views']
        replay=copy.deepcopy(original);replay['input']['path']='input.json';replay['supplied_views']['path']='supplied-views.json'
        self.write('request.json',original);self.write('replay-request.json',replay)
        self.result['request_sha256']=gate.digest(original)
        self.result['inputs']['supplied_views'].update(raw_sha256=sha,bytes=len(raw))
        comparison=json.loads((self.bundle/'view-comparison.json').read_text());comparison['supplied_sha256']=sha
        self.write('view-comparison.json',comparison);self.reseal()
        self.assertNotEqual(self.inspect()['status'],'consistent')

if __name__=='__main__':unittest.main()
