"""Consumer-boundary controls with explicitly synthetic protected history.

Actor authentication is a fixture premise; these are not ordinary actor trials.
Native301PublicTests separately covers the actual CLI/process return path.
"""
from pathlib import Path
import json
import tempfile
import unittest
import test_ac_support_core as t
c = t.c

class ConjunctionProofConsumerTests(unittest.TestCase):
    def check(self, native, conjunction):
        with tempfile.TemporaryDirectory(prefix='native-conjunction-') as temp:
            f = t.Fixture(Path(temp).resolve())
            legacy = f.runtime()
            historical = f.artifact(legacy, 'operation', {'request': f.request('results.conjoin', {
                'operator_id': 'claude-rc9.conjunction/1', 'plan': f.data,
                'returns': [], 'current_observations': []}), 'response_without_evidence': {'result': {'artifact': None, 'value': {'judgment': {'core_value': 'satisfied'}}}}})
            if native:
                profile = t.CODE.parent / 'design/fd-method-stdo-3.0.1.json'
                (f.authorities / 'profile.json').write_bytes(profile.read_bytes())
                f.basis['method_profile'] = {'id': c.NATIVE_PROFILE_ID, 'sha256': c.NATIVE_PROFILE_SHA256}
                definition = json.loads((f.workspace / 'Product.json').read_text())
                definition['constitution'] = {'stdo': {'basis': {'uri': 'stdo://releases/v3.0.1-rc.1/', 'manifest_sha256': c.NATIVE_MANIFEST_SHA256}}}
                f.definition = f.write('Product.json', definition)
                f.policy['product']['definition'] = f.definition
                f.policy['method_profile'] = {**f.basis['method_profile'], 'source': f.ref(f.authorities / 'profile.json', 'authority', 'profile.json')}
            f.return_contract = f.write('inputs/executive-return.json', {
                'schema': 'a_c.fd-support.return-contract/1', 'id': 'executive-return',
                'authority_source': f.law, 'carrier': 'a_c.fd-support.closed-return/1',
                'output_slot': 'final_stdout_object', 'required_evaluations': [], 'role': 'Executive',
                'proof': {'mandate': f.law, 'consumed_results': [],
                    'conjunction': historical if conjunction else None,
                    'disposition_authority': None, 'predicate_ids': []}})
            runtime = f.runtime()
            packet = f.packet('Executive')
            response, _ = f.run(runtime, 'context.assemble', {'packet': packet, 'models': [], 'sources': [], 'late_acquisition': [], 'envelope': {'capacity_bytes': None, 'boundary': 'executor-stdin-utf8', 'host_context': {'state': 'unknown', 'bytes': None, 'evidence': None}}})
            self.assertEqual(response['status'], 'ok', response)
            context = response['result']['artifact']
            attempt = f.artifact(runtime, 'attempt', {'fixture': 'controlled producer'})
            original = {'schema': 'a_c.fd-support.closed-return/1', 'id': 'executive-closed',
                'frame': {'id': 'frame', 'revision': '1'}, 'activation': c.activation_identity(packet),
                'subject': f.subject, 'basis': f.basis,
                'actor': {'id': 'executive', 'family': 'A', 'authorship': 'executive'},
                'consumer': 'executive', 'evaluations': [], 'not_performed': [],
                'work_result': None, 'residuals': [], 'invalidators': []}
            returned = f.artifact(runtime, 'return', {'attempt': attempt, 'original': original,
                'binding_checks': {'gaps': []}, 'return_contract': f.return_contract,
                'producer': {'authenticated': True}})
            readable, _ = f.run(runtime, 'evidence.read', {'artifact': historical})
            self.assertEqual(readable['status'], 'ok')
            self.assertEqual(readable['result']['value']['envelope']['provenance']['method_profile_sha256'], c.PROFILE_SHA256)
            checked, _ = f.run(runtime, 'return.check', {'return': returned, 'context': context,
                'consumer': 'executive', 'observations': [], 'predicates': []})
            self.assertEqual(checked['status'], 'ok', checked)
            return checked['result']['value']

    def test_native_rejects_historical_conjunction_proof(self):
        value = self.check(native=True, conjunction=True)
        self.assertFalse(value['consumable'], value)
        self.assertIn('Native conjunction proof is unsupported; historical evidence grants no translation', value['gaps'])

    def test_native_without_conjunction_stays_consumable(self):
        value = self.check(native=True, conjunction=False)
        self.assertTrue(value['consumable'], value['gaps'])

    def test_legacy_conjunction_behavior_is_preserved(self):
        value = self.check(native=False, conjunction=True)
        self.assertTrue(value['consumable'], value['gaps'])
