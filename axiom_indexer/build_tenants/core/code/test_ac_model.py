import copy
import unittest
import ac_model as convert


class ModelConversionTest(unittest.TestCase):
    def setUp(self):
        self.ground = [{'path':'source/rules.md','section':'urn:source:rules','start_line':1,'end_line':1,'quote':'Declared rule.'}]
        self.model = {'id':'urn:model:test','basis':{'id':'urn:basis:test'},'populations':{f:[] for f in convert.FAMILIES}}
        p=self.model['populations']
        p['objects']=[{'id':'urn:object:test','value':{'label':'Café','definition':'A governed concept.','conditions':['Admitted use'],'exceptions':['Unknown basis'],'grounding':self.ground}}]
        p['relations']=[{'id':'urn:relation:test','source':'urn:object:test','target':'urn:object:test','qualifiers':{'meaning':'An explicitly declared self relation.','conditions':[],'exceptions':[],'grounding':self.ground}}]
        p['constraints']=[{'id':'urn:constraint:test','applies_to':['urn:object:test'],'predicate':{'statement':'Do not infer authority.','conditions':['Before effects'],'exceptions':[],'grounding':self.ground}}]
        p['latitude']=[{'id':'urn:latitude:test','applies_to':['urn:object:test'],'allowed_variation':{'statements':['Internal choice'],'grounding':self.ground},'forbidden_variation':{'statements':['Changed authority'],'grounding':self.ground}}]
        p['residuals']=[{'id':'urn:residual:test','subject':'urn:constraint:test','uncertainty':{'statement':'Evidence absent.','grounding':self.ground},'consequence':'Withhold dependent claim.'}]
        self.config={'program_uri':'urn:program:test','source_basis':'urn:source:test','calculus_ref':'repo://source/rules.md','metadata_source_ref':'repo://source/rules.md','source_mappings':[{'path_prefix':'source/','uri_prefix':'repo://source/'}],'frame_indexes':[{'uri':'urn:index:test','frame_ref':'repo://source/rules.md','scope':'Inspect declared constraint and supporting closure.','clause_refs':['urn:constraint:test'],'residual_refs':[],'source_refs':['repo://source/rules.md']}]}

    def test_roundtrip_and_exact_fields(self):
        original=copy.deepcopy(self.model)
        program=convert.convert(self.model,self.config)
        self.assertEqual(convert.restore(program),original)
        self.assertEqual(self.model,original)
        constraint=next(x for x in program['clauses'] if x['uri']=='urn:constraint:test')
        self.assertIn('urn:object:test',[a.get('ref') for a in constraint['arguments']])
        self.assertEqual(constraint['statement'],'Do not infer authority.')
        self.assertEqual(program['residuals'][0]['subject_refs'],['urn:constraint:test'])

    def test_tampered_visible_statement_refused(self):
        program=convert.convert(self.model,self.config)
        program['clauses'][0]['statement']='Invented meaning.'
        with self.assertRaisesRegex(ValueError,'exact model derivation'):convert.restore(program)

    def test_dangling_attachment_refused(self):
        self.model['populations']['constraints'][0]['applies_to']=['urn:missing']
        with self.assertRaisesRegex(ValueError,'dangling attachment'):convert.convert(self.model,self.config)

    def test_unsupported_operation_refused(self):
        self.model['populations']['judgments']=[{'id':'urn:judgment:test'}]
        with self.assertRaisesRegex(ValueError,'operational populations'):convert.convert(self.model,self.config)

    def test_duplicate_identity_refused(self):
        self.model['populations']['constraints'][0]['id']='urn:object:test'
        with self.assertRaisesRegex(ValueError,'duplicate'):convert.convert(self.model,self.config)

    def test_missing_source_mapping_refused(self):
        self.config['source_mappings'][0]['path_prefix']='unrelated/'
        with self.assertRaisesRegex(ValueError,'missing source mapping'):convert.convert(self.model,self.config)

    def test_tampered_reference_refused(self):
        program=convert.convert(self.model,self.config)
        clause=next(x for x in program['clauses'] if x['uri']=='urn:constraint:test')
        clause['arguments'][0]['ref']='urn:relation:test'
        with self.assertRaisesRegex(ValueError,'exact model derivation'):convert.restore(program)

if __name__=='__main__':unittest.main()
