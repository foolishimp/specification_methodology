"""Reusable adapter/gate controls. Real kernel qualification is a separate retained run."""
from copy import deepcopy
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import formal_gate as gate
import formal_support as support
import import_fixture as bridge
from generation_profile import validate_generation_profile,ProfileError
from generate_fixture import lean_string
GRAPHIFY=ROOT.parent/'graphify'
sys.path.insert(0,str(GRAPHIFY/'code'))
import ac_graph
import ac_generate as generation
spec=importlib.util.spec_from_file_location('graphify_authored_test_data',GRAPHIFY/'test_env/test_ac_generate.py')
authored=importlib.util.module_from_spec(spec);spec.loader.exec_module(authored)


def new_subject(directory,subject='repo://formal-gate/unseen-alpha/',payload=None):
    directory=Path(directory);corpus=directory/'corpus';corpus.mkdir(parents=True)
    raw=authored.SOURCE.encode();(corpus/'rules.md').write_bytes(raw)
    manifest=directory/'manifest.json'
    generation.save(manifest,{'profile':'ac.generation.corpus/1','subject_id':subject,'revision':'formal-test-authored',
        'files':[{'path':'rules.md','sha256':generation.sha(raw),'bytes':len(raw),'git_blob':'test-authored'}]})
    plan=generation.prepare(corpus,manifest,directory/'prepared','direct',None,1000)
    chunks=generation.load(directory/'prepared/chunks.json');answer=authored.fixture_answer(chunks[0])
    if payload is not None:answer['concepts'][0]['definition']=payload
    model,coverage=generation.model_from_answers(plan,chunks,{chunks[0]['id']:answer},[])
    generation.save(directory/'authored-answer.json',answer)
    generation.save(directory/'model.json',model)
    return model


def request_for(path,selections=None,views=None):
    return {'schema':'a_c.formal-gate.request/1','input':{'format':'model','path':str(path),'raw_sha256':support.sha(path)},
        'selections':selections or [],'supplied_views':views,'context_binding':None}


class FormalGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        (ROOT/'.cache').mkdir(exist_ok=True)
        cls.tmp=tempfile.TemporaryDirectory(dir=ROOT/'.cache');cls.directory=Path(cls.tmp.name)
        cls.model=new_subject(cls.directory/'subject')
        cls.imported=bridge.import_model(cls.model)
    @classmethod
    def tearDownClass(cls):cls.tmp.cleanup()
    def test_unseen_subject_is_parameterized_not_signature_allowlisted(self):
        self.assertNotIn(self.model['signature']['sha256'],[bridge.SIGNATURE_SHA256,bridge.TOY_SIGNATURE_SHA256])
        self.assertEqual(validate_generation_profile(self.model)['profile'],'a_c.lean.generation-signature/1')
        self.assertEqual(bridge.reconstruct(self.imported),self.model)
    def test_new_signature_cannot_weaken_governing_schema(self):
        m=deepcopy(self.model);next(iter(m['signature']['definition']['relation_kinds'].values()))['source']['governing']=False
        m['signature']['sha256']=bridge.digest({'id':m['signature']['id'],'definition':m['signature']['definition']})
        with self.assertRaises(ProfileError):validate_generation_profile(m)
        with self.assertRaises(bridge.Refusal):bridge.import_model(m)
    def test_new_signature_cannot_change_required_relation_catalog(self):
        m=deepcopy(self.model);m['dependency_contract']['required_relation_kinds']=[]
        with self.assertRaises(ProfileError):validate_generation_profile(m)
    def test_unknown_signature_identity_is_unsupported(self):
        m=deepcopy(self.model);m['signature']['id']='urn:arbitrary:signature'
        with self.assertRaises(ProfileError) as e:validate_generation_profile(m)
        self.assertTrue(e.exception.unsupported)
    def test_actual_graphify_mapping_all_primary_and_toy_selectors(self):
        for model in (self.model,bridge.load_checked(bridge.FIXTURE_DIR/'MODEL.json'),bridge.load_checked(bridge.TOY_FIXTURE_DIR/'MODEL.json')):
            imported=bridge.import_model(model);checked=ac_graph.validate(model)
            choices=[([r['record']['id']],None) for r in imported['records']]
            actual=ac_graph.project_many(checked,choices)
            for idx,(seeds,budget) in enumerate(choices):
                cert=bridge.closure_certificate(imported,[idx]);selection={'seeds':seeds,'budget_records':budget}
                self.assertEqual(gate.graphify_view(imported,cert,selection),actual[idx])
    def test_carrier_recovers_unseen_whole_subject(self):
        carrier=ac_graph.materialize(ac_graph.validate(self.model)).document
        self.assertEqual(bridge.recover_carrier(carrier),self.model)
    def test_model_only_no_projection_claim_requested(self):
        gate.validate_request(request_for(self.directory/'subject/model.json'))
        req=request_for(self.directory/'subject/model.json',views={'path':'views.json','raw_sha256':'0'*64})
        with self.assertRaises(gate.GateError):gate.validate_request(req)
    def test_refused_duplicate_selection_and_boolean_budget(self):
        seed=self.imported['records'][0]['record']['id']
        for s in ({'seeds':[seed,seed],'budget_records':None},{'seeds':[seed],'budget_records':True}):
            with self.assertRaises(gate.GateError):gate.validate_request(request_for(self.directory/'subject/model.json',[s]))
    def test_unknown_request_schema_unsupported(self):
        req=request_for(self.directory/'subject/model.json');req['schema']='future/99'
        result=gate.verify(req,self.directory/'unknown-schema')
        self.assertEqual(result['status'],'unsupported')
        self.assertFalse((self.directory/'unknown-schema').exists())
    def test_input_hash_tamper_refuses_without_proof(self):
        req=request_for(self.directory/'subject/model.json');req['input']['raw_sha256']='0'*64
        result=gate.verify(req,self.directory/'bad-hash')
        self.assertEqual(result['status'],'refused');self.assertEqual(result['checked_claims'],[])
    def test_resource_byte_limit_is_incomplete(self):
        result=gate.verify(request_for(self.directory/'subject/model.json'),self.directory/'byte-limit',{'max_input_bytes':1})
        self.assertEqual(result['status'],'incomplete')
    def test_existing_output_and_input_alias_never_overwritten(self):
        p=self.directory/'subject/model.json';before=p.read_bytes()
        result=gate.verify(request_for(p),p)
        self.assertEqual(result['status'],'refused');self.assertEqual(p.read_bytes(),before)
        result=gate.verify(request_for(p),p.parent)
        self.assertEqual(result['status'],'refused');self.assertEqual(p.read_bytes(),before)
    def test_forged_evidence_success_label_cannot_admit(self):
        fake=self.directory/'fake';fake.mkdir();(fake/'result.json').write_text('{"status":"verified"}')
        result=gate.check_evidence(fake,self.directory/'replay-fake')
        self.assertEqual(result['status'],'refused');self.assertEqual(result['checked_claims'],[])
    def test_unknown_axiom_or_missing_dynamic_theorem_rejected(self):
        for log in ("'model' depends on axioms: [sorryAx]", "'another' depends on axioms: [propext]"):
            with self.assertRaises(gate.GateError):gate._audit(log,['model'])
    def test_source_string_escapes_controls_without_interpolation(self):
        text='"\\\n\t\x00\x1f\x7f λ雪😀 ${bad} -- /-'
        encoded=lean_string(text)
        self.assertNotIn('\x00',encoded);self.assertIn('\\x00',encoded);self.assertIn('\\"',encoded)
        self.assertNotIn('\\u{',encoded)
    def test_tool_environment_discards_caller_module_and_loader_overrides(self):
        with patch.dict(os.environ,{'LEAN_PATH':'/hostile','LEAN_SYSROOT':'/hostile','LAKE_HOME':'/hostile','DYLD_LIBRARY_PATH':'/hostile','LD_PRELOAD':'/hostile','PYTHONPATH':'/hostile'}):
            _,env,_=support.tools()
        for key in ('LEAN_PATH','LEAN_SYSROOT','LAKE_HOME','DYLD_LIBRARY_PATH','LD_PRELOAD','PYTHONPATH'):self.assertNotIn(key,env)

if __name__=='__main__':unittest.main()
