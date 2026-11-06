"""Public installed-upstream route controls; select a real bootstrapped runtime."""
from pathlib import Path
import copy
import json
import os
import subprocess
import shutil
import hashlib
import sys
import tempfile
import unittest

CODE=Path(__file__).resolve().parents[1]/'code';sys.path.insert(0,str(CODE))
import ac_graph

@unittest.skipUnless(os.environ.get('AC_UPSTREAM_RUNTIME'),'Select a real private bootstrap receipt')
class UpstreamTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name).resolve()
        self.runtime=Path(os.environ['AC_UPSTREAM_RUNTIME']);self.selection=json.loads(self.runtime.read_text())
        self.model=json.loads((Path(__file__).parent/'fixtures/toy_model.json').read_text())
        self.save('model.json',self.model);self.save('carrier.json',ac_graph.materialize(ac_graph.validate(self.model)).document)
        self.save('selections.json',[{'seeds':['urn:a-c:toy:object:a'],'budget_records':None}])
    def save(self,name,value): (self.root/name).write_text(json.dumps(value,sort_keys=True,indent=2)+'\n')
    def call(self,runtime=None,*,output=None,upstream=None):
        argv=[self.selection['python'],'-B',str(CODE.parents[2]/'scripts/ac.py'),'upstream','--model',str(self.root/'model.json'),'--carrier',str(self.root/'carrier.json'),'--selections',str(self.root/'selections.json'),'--upstream',str(upstream or self.selection['upstream']),'--runtime',str(runtime or self.runtime),'--output',str(output or self.root/'output')]
        result=subprocess.run(argv,capture_output=True,text=True,timeout=30)
        return result,json.loads(result.stdout)
    def test_actual_roundtrip_and_loaded_module_pins(self):
        process,result=self.call();self.assertEqual(process.returncode,0,process.stderr)
        self.assertEqual(result['schema'],'a_c.graphify.current-roundtrip/1')
        self.assertEqual(result['model']['canonical_sha256'],ac_graph.validate(self.model).sha256)
        self.assertEqual(result['runtime']['python_invocation'],self.selection['python'])
        self.assertNotEqual(result['runtime']['prefix'],result['runtime']['base_prefix'])
        self.assertIn('graphify.build',result['runtime']['loaded_modules'])
        self.assertEqual(result['runtime']['source_pins']['ac_fs_boundary.py'],hashlib.sha256((CODE/'ac_fs_boundary.py').read_bytes()).hexdigest())
    def containment(self,variant):
        protected=self.root/'protected';shutil.copytree(self.selection['upstream'],protected,symlinks=True)
        runtime=copy.deepcopy(self.selection);runtime['upstream']=str(protected);self.save('relocated-runtime.json',runtime)
        def tree():
            result={}
            for path in protected.rglob('*'):
                name=path.relative_to(protected).as_posix()
                result[name]=('symlink',str(path.readlink())) if path.is_symlink() else ('file',hashlib.sha256(path.read_bytes()).hexdigest()) if path.is_file() else ('directory',None)
            return result
        output=protected/'review-output';upstream=protected
        if variant=='equal':output=protected
        elif variant=='ancestor':output=self.root
        elif variant in ('input-alias','output-alias'):
            alias=self.root/'alias';alias.symlink_to(protected,target_is_directory=True)
            if variant=='input-alias':upstream=alias
            else:output=alias/'review-output'
        elif variant=='resolved-parent':output=protected/'absent'/'..'/'review-output'
        elif variant=='disjoint':output=self.root/'protected-sibling'
        elif variant.startswith('case-'):
            alias=protected.with_name('PROTECTED')
            if not alias.exists() or not alias.samefile(protected):self.skipTest('Filesystem has no case alias for this control')
            self.assertNotEqual(alias.resolve(),protected.resolve())
            if variant=='case-descendant':output=alias/'missing-parent'/'review-output'
            elif variant=='case-equal':output=alias
            elif variant=='case-ancestor':output=self.root.with_name(self.root.name.upper())
            elif variant=='case-input':upstream=alias
        before=tree()
        process,result=self.call(self.root/'relocated-runtime.json',output=output,upstream=upstream)
        if variant=='disjoint':
            self.assertEqual(process.returncode,0,process.stderr);self.assertEqual(result['status'],'verified')
            self.assertTrue((output/'result.json').is_file())
        else:
            self.assertEqual(process.returncode,2,result)
            self.assertIn(result['reason'],('Output overlaps an input','Output must be a fresh non-redirected directory'))
            self.assertEqual(tree(),before,'refusal must precede all dependency-tree effects')
            self.assertFalse((protected/'review-output').exists())
    def test_output_inside_upstream_refuses_before_effects(self):self.containment('inside')
    def test_output_equal_upstream_refuses_before_effects(self):self.containment('equal')
    def test_output_ancestor_upstream_refuses_before_effects(self):self.containment('ancestor')
    def test_resolved_input_alias_overlap_refuses_before_effects(self):self.containment('input-alias')
    def test_output_alias_overlap_refuses_before_effects(self):self.containment('output-alias')
    def test_resolved_parent_overlap_refuses_before_effects(self):self.containment('resolved-parent')
    def test_legitimate_adjacent_output_remains_usable(self):self.containment('disjoint')
    def test_case_alias_future_descendant_refuses_before_effects(self):self.containment('case-descendant')
    def test_case_alias_equal_refuses_before_effects(self):self.containment('case-equal')
    def test_case_alias_ancestor_refuses_before_effects(self):self.containment('case-ancestor')
    def test_case_alias_selected_upstream_refuses_before_effects(self):self.containment('case-input')

    def test_missing_protected_upstream_refuses_before_output(self):
        process,result=self.call(upstream=self.root/'missing-upstream')
        self.assertEqual(process.returncode,2,result);self.assertFalse((self.root/'output').exists())

    def test_other_model_cannot_reuse_carrier(self):
        changed=copy.deepcopy(self.model);changed['id']+='-other';self.save('model.json',changed)
        process,result=self.call();self.assertEqual(process.returncode,2);self.assertFalse((self.root/'output').exists())
    def test_wrong_runtime_python_refuses_before_output(self):
        changed=copy.deepcopy(self.selection);changed['python']=sys.executable;self.save('runtime.json',changed)
        process,result=self.call(self.root/'runtime.json');self.assertEqual(process.returncode,2);self.assertFalse((self.root/'output').exists())
    def test_wrong_runtime_commit_refuses_before_output(self):
        changed=copy.deepcopy(self.selection);changed['upstream_commit']='0'*40;self.save('runtime.json',changed)
        process,result=self.call(self.root/'runtime.json');self.assertEqual(process.returncode,2);self.assertFalse((self.root/'output').exists())
    def test_existing_output_is_never_replaced(self):
        (self.root/'output').mkdir();(self.root/'output/sentinel').write_text('preserve')
        process,result=self.call();self.assertEqual(process.returncode,2);self.assertEqual((self.root/'output/sentinel').read_text(),'preserve')

if __name__=='__main__':unittest.main()
