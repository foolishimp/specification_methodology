"""Native public-path fixtures; no LLM/semantic/production admission qualification."""
from pathlib import Path
import json
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'code'))
import ac_support_core as c
import test_ac_support_effects as legacy_tests

class Native301PublicTests(unittest.TestCase):
    _public = legacy_tests.PublicRetryTests._public
    _select_policy = legacy_tests.PublicRetryTests._select_policy
    _ok = legacy_tests.PublicRetryTests._ok
    _assemble = legacy_tests.PublicRetryTests._assemble
    _admit = legacy_tests.PublicRetryTests._admit
    _finished = legacy_tests.PublicRetryTests._finished
    tearDown = legacy_tests.PublicRetryTests.tearDown

    def setUp(self):
        legacy_tests.PublicRetryTests.setUp(self)
        profile = self.code.parent / 'design/fd-method-stdo-3.0.1.json'
        (self.f.authorities / 'profile.json').write_bytes(profile.read_bytes())
        self.native = {'id': c.NATIVE_PROFILE_ID, 'sha256': c.NATIVE_PROFILE_SHA256}
        self.f.basis['method_profile'] = self.native
        definition = json.loads((self.f.workspace / 'Product.json').read_text())
        definition['constitution'] = {'stdo': {'basis': {'uri': 'stdo://releases/v3.0.1-rc.1/', 'manifest_sha256': c.NATIVE_MANIFEST_SHA256}}}
        self.f.definition = self.f.write('Product.json', definition)
        self.f.policy['product']['definition'] = self.f.definition
        self.f.policy['method_profile'] = {**self.native, 'source': self.f.ref(self.f.authorities / 'profile.json', 'authority', 'profile.json')}
        self._select_policy()

    def test_discovery_acquisition_observation_and_native_provenance(self):
        discovery = self._ok(self._public('tools.describe', {'method_profile': self.native}))
        self.assertEqual(discovery['method_profile'], self.native)
        self.assertNotIn('results.conjoin', [x['name'] for x in discovery['operations']])
        source = self._public('source.read', {'source': self.f.law, 'encoding': 'utf8'})
        self.assertEqual(self._ok(source)['content'], 'one\ntwo\nthree\n')
        self.assertEqual(source['operation_outcome']['source_parent']['sha256'], c.NATIVE_FOUNDATIONS_SHA256)
        operation = self._ok(self._public('evidence.read', {'artifact': source['evidence']}))
        self.assertEqual(operation['envelope']['provenance']['method_profile_sha256'], c.NATIVE_PROFILE_SHA256)
        observed = self._ok(self._public('workspace.observe', {'scope': [{'root': 'workspace', 'path': 'inputs/law.txt', 'kind': 'file'}]}))
        self.assertTrue(observed['entries'])
        refused = self._public('tools.describe', {'operation': 'results.conjoin'})
        self.assertEqual(refused['refusal']['code'], 'unsupported_check')

    def test_legacy_packet_is_not_relabelled_native(self):
        packet = self.f.packet()
        packet['subject_basis']['method_profile'] = {'id': c.PROFILE_ID, 'sha256': c.PROFILE_SHA256}
        response = self._public('context.assemble', {'packet': packet, 'models': [], 'sources': [], 'late_acquisition': [], 'envelope': {'capacity_bytes': None, 'boundary': 'executor-stdin-utf8', 'host_context': {'state': 'unknown', 'bytes': None, 'evidence': None}}})
        self.assertEqual(response['refusal']['code'], 'basis_stale')

    def test_native_profile_requires_exact_product_basis(self):
        value = json.loads((self.f.workspace / 'Product.json').read_text())
        value['constitution']['stdo']['basis']['manifest_sha256'] = '0' * 64
        self.f.definition = self.f.write('Product.json', value)
        self.f.policy['product']['definition'] = self.f.definition
        self._select_policy()
        with self.assertRaises(c.SupportError) as raised:
            c.Runtime.from_policy(self.policy_path, self.policy_sha, 'executive')
        self.assertEqual(raised.exception.code, 'basis_stale')

    def test_native_public_retry_keeps_activation_history(self):
        legacy_tests.PublicRetryTests.test_public_reassembled_context_cannot_reset_activation_history(self)

    def test_native_stale_source_stops_dispatch(self):
        material = self.f.write('inputs/material.txt', b'original deciding material')
        packet = self.f.packet()
        packet['attention']['semantic_sources'].append(material)
        context = self._assemble(packet)
        receipt = self._admit(context)
        (self.f.workspace / 'inputs/material.txt').write_text('changed deciding source\n')
        response = self._public('dispatch.start', {'preflight': receipt})
        self.assertNotEqual(response['status'], 'ok')
        self.assertFalse(self.target.exists())

    def test_actual_process_completion_capture_and_return_check(self):
        packet = self.f.packet()
        original = {'schema': 'a_c.fd-support.closed-return/1', 'id': 'fixture-return', 'frame': {k: packet['frame'][k] for k in ('id','revision')}, 'activation': c.activation_identity(packet), 'subject': self.f.subject, 'basis': self.f.basis, 'actor': {'id': 'worker','family': 'A','authorship': 'worker'}, 'consumer': 'executive', 'evaluations': [], 'not_performed': [], 'work_result': {'value': 'incomplete', 'cause': 'bounded fixture constructs no candidate', 'candidate': None, 'evidence': [], 'residuals': ['semantic work unperformed']}, 'residuals': ['semantic actor qualification not performed'], 'invalidators': []}
        payload = self.f.write('inputs/closed-return.json', original)
        actor = self.f.write('inputs/closed_actor.py', b'import sys\nfrom pathlib import Path\nsys.stdin.buffer.read()\nsys.stdout.buffer.write(Path(sys.argv[1]).read_bytes())\n')
        executor = self.f.policy['executors']['registered']
        executor['argv'] = [str(self.python), '-B', str(self.f.workspace / 'inputs/closed_actor.py'), str(self.f.workspace / 'inputs/closed-return.json')]
        executor['dependencies'] = [actor, payload]
        self._select_policy()
        context = self._assemble(packet)
        started = self._public('dispatch.start', {'preflight': self._admit(context)})
        attempt = started['result']['artifact']
        observed = self._ok(self._finished(attempt))
        self.assertEqual(observed['process_end']['returncode'], 0)
        captured = self._public('return.capture', {'attempt': attempt, 'payload': observed['output']['stdout'], 'return_contract': self.f.return_contract})
        value = self._ok(captured)
        self.assertTrue(value['producer']['authenticated'])
        self.assertEqual(value['binding_checks']['gaps'], [])
        checked = self._ok(self._public('return.check', {'return': captured['result']['artifact'], 'context': context, 'consumer': 'executive', 'observations': [], 'predicates': []}))
        self.assertTrue(checked['consumable'], checked['gaps'])
        self.assertEqual(checked['original']['work_result']['value'], 'incomplete')
        self.assertEqual(checked['original']['evaluations'], [])

if __name__ == '__main__':
    unittest.main()
