from pathlib import Path
import contextlib, datetime, json, os, sys, tempfile, time, unittest
out=Path(__file__).resolve().parent
copy=json.loads((out/'COPY.json').read_text())
scratch=Path(copy['scratch'])
tenant=scratch/'product/build_tenants/graphify'
os.environ['TMPDIR']=str(scratch/'tmp')
os.environ['PYTHONDONTWRITEBYTECODE']='1'
os.environ['PYTHONPYCACHEPREFIX']=str(scratch/'cache')
os.environ['AC_JUDGMENT_INGRESS_TEST_EVIDENCE']=str(scratch/'proof/judgments')
os.environ['AC_SUPPORT_EFFECTS_PROOF_ROOT']=str(scratch/'proof/effects')
tempfile.tempdir=str(scratch/'tmp')
sys.path[:0]=[str(tenant/'test_env'),str(tenant/'code')]
from test_ac_support_interfaces import PublicJudgmentIngressTests
import test_ac_support_effects
import ac_support_core as core

class ReviewerPublicControls(PublicJudgmentIngressTests):
    def test_other_material_binding_coordinates_remain_unresolved(self):
        write=self.f.write
        for coordinate,replacement in [('frame',{'id':'other-frame','revision':'1'}),('actor',{'id':'other-worker','family':'A','authorship':'other-worker'}),('consumer','other-consumer')]:
            with self.subTest(coordinate=coordinate):
                label='reviewer-wrong-'+coordinate
                def selected(name,value):
                    if name=='inputs/stdout-'+label+'.json':
                        value[coordinate]=replacement
                    return write(name,value)
                self.f.write=selected
                try:
                    reference,capture,checked=self.roundtrip(label,'falsified')
                    self.assertTrue(capture['producer']['authenticated'])
                    self.assertFalse(checked['consumable'])
                    self.assertEqual([g['binding'] for g in capture['binding_checks']['gaps'] if isinstance(g,dict) and 'binding' in g],[coordinate])
                    self.assert_unresolved_dependency(self.query(label,{'record':reference,'pointer':'/payload/original/evaluations/0'}))
                finally:
                    self.f.write=write

    def test_canonical_membership_public_discriminators(self):
        reference,capture,checked=self.roundtrip('reviewer-pointer','falsified',nested=True)
        self.assertTrue(checked['consumable'])
        self.assertEqual(capture['original']['not_performed'],['nested-not-performed'])
        suffixes=['00','-1','+0','1','0/','0/domain_outcome/nested']
        for n,suffix in enumerate(suffixes):
            with self.subTest(suffix=suffix):
                self.assert_unresolved_dependency(self.query('reviewer-invalid-'+str(n),{'record':reference,'pointer':'/payload/original/evaluations/'+suffix}))
        direct=self.query('reviewer-direct',{'record':reference,'pointer':'/payload/original/evaluations/0'})
        self.assertEqual(self.edge(direct)['core_value'],'falsified')
        self.assertTrue(self.edge(direct)['excluded'])

    def test_known_final_provenance_survives_unrelated_incomplete_history(self):
        reference,capture,_=self.roundtrip('reviewer-known-history','falsified')
        core.as_object(self.f.policy['limits'])['max_history_records']=1
        self.write_policy()
        recaptured=self.public('return.capture',{'attempt':capture['attempt'],'payload':capture['raw_payload'],'return_contract':self.f.return_contract})
        result=recaptured['result']['value']
        self.assertTrue(result['producer']['authenticated'])
        self.assertTrue(any(isinstance(g,dict) and 'history' in g for g in result['binding_checks']['gaps']))
        self.assertFalse(any(isinstance(g,dict) and 'binding' in g for g in result['binding_checks']['gaps']))
        queried=self.query('reviewer-history-gap',{'record':recaptured['result']['artifact'],'pointer':'/payload/original/evaluations/0'})
        self.assertEqual(self.edge(queried)['core_value'],'falsified')
        self.assertTrue(self.edge(queried)['excluded'])
        self.assertFalse(self.edge(queried)['unresolved'])

names=[
 'test_ac_support_interfaces.PublicJudgmentIngressTests.test_missing_judgment_preserves_unknown_required_dependency',
 'test_ac_support_interfaces.PublicJudgmentIngressTests.test_wrong_activation_return_cannot_exclude_required_dependency',
 'test_ac_support_interfaces.PublicJudgmentIngressTests.test_nested_not_performed_domain_data_cannot_exclude_required_dependency',
 'test_ac_support_interfaces.PublicJudgmentIngressTests.test_direct_performed_satisfied_and_falsified_conditions_remain_usable',
 'test_ac_support_effects.PublicRetryTests.test_public_reassembled_context_cannot_reset_activation_history',
 'test_ac_support_effects.PublicRetryTests.test_public_distinct_activation_keeps_its_own_attempt_population',
 'test_ac_support_effects.PublicRetryTests.test_public_selected_retry_survives_context_reassembly',
 'test_ac_support_effects.PublicRetryTests.test_public_retry_requires_actual_check',
 'test_ac_support_effects.PublicRetryTests.test_public_retry_refuses_invalid_check_basis',
 'test_ac_support_effects.PublicRetryTests.test_public_retry_refuses_wrong_predecessor',
 'test_ac_support_effects.PublicRetryTests.test_public_timeout_finalizes_while_descendant_still_holds_pipes',
 'test_ac_support_effects.PublicRetryTests.test_public_cancel_finalizes_while_descendant_still_holds_pipes',
 'test_ac_support_effects.PublicRetryTests.test_public_timeout_bounds_continuously_readable_descendant_tail',
 'test_ac_support_effects.PublicRetryTests.test_public_timeout_honors_selected_grace_before_local_kill',
]
suite=unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromName(n) for n in names)
for n in ['test_other_material_binding_coordinates_remain_unresolved','test_canonical_membership_public_discriminators','test_known_final_provenance_survives_unrelated_incomplete_history']:
    suite.addTest(ReviewerPublicControls(n))
started=time.time_ns()
with (out/'targeted.stdout').open('x') as log, (out/'targeted.stderr').open('x') as err:
    with contextlib.redirect_stdout(log),contextlib.redirect_stderr(err):
        result=unittest.TextTestRunner(stream=log,verbosity=2).run(suite)
record={'started_ns':started,'ended_ns':time.time_ns(),'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skipped':len(result.skipped),'successful':result.wasSuccessful(),'cases':names+['ReviewerPublicControls.'+n for n in ['test_other_material_binding_coordinates_remain_unresolved','test_canonical_membership_public_discriminators','test_known_final_provenance_survives_unrelated_incomplete_history']],'runtime_cwd':os.getcwd(),'scratch':str(scratch),'scope':'Targeted ordinary public CLI registered local-process controls; fixture judgments are supplied assertions, not semantic F_P assessments. Author tests are inspected harnesses; source-first EXPECTATIONS.md is oracle. No full suite.','copied_subject_pins':copy['copied_files']}
with (out/'TARGETED.json').open('x') as f: json.dump(record,f,indent=2);f.write('\n')
print(json.dumps({k:record[k] for k in ['tests','failures','errors','skipped','successful','scratch']}))
raise SystemExit(0 if result.wasSuccessful() else 1)
