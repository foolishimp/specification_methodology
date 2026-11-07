"""3.0.5-rc.1 public contracts against synthetic installed cuts; no F_P qualification."""
from pathlib import Path
import copy
import hashlib
import json
import shutil
import subprocess
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'code'))
import ac_support_core as c
import ac_support_effects as effects
import test_ac_support_effects as legacy
import test_ac_support_native301 as native301


class Native305PublicTests(unittest.TestCase):
    _public = legacy.PublicRetryTests._public
    _select_policy = legacy.PublicRetryTests._select_policy
    _ok = legacy.PublicRetryTests._ok
    _assemble = legacy.PublicRetryTests._assemble
    _admit = legacy.PublicRetryTests._admit
    _finished = legacy.PublicRetryTests._finished
    tearDown = legacy.PublicRetryTests.tearDown

    def setUp(self):
        legacy.PublicRetryTests.setUp(self)
        profile_path = self.code.parent / 'design/fd-method-stdo-3.0.5-rc.1.json'
        profile = json.loads(profile_path.read_text())
        self.profile = profile
        (self.f.authorities / 'profile.json').write_bytes(profile_path.read_bytes())
        self.native = {'id': c.NATIVE305_PROFILE_ID, 'sha256': c.NATIVE305_PROFILE_SHA256}
        self.f.basis['method_profile'] = self.native
        source = self.code.parents[3] / 'specification_methodology/v3/build_tenants/common'
        self.installation = self.root / 'method'; self.installation.mkdir()
        rows = [{'path': 'standards/' + row['member'], 'sha256': row['sha256']} for row in profile['members']] + profile['native_contracts']
        for row in rows:
            raw = (source / row['path']).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), row['sha256'])
            path = self.installation / row['path']; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(raw)
        (self.installation / 'LICENSE').write_text('synthetic installed-cut control\n')
        (self.installation / 'release').mkdir(); (self.installation / 'release/release-note.md').write_text('synthetic 3.0.5-rc.1 control\n')
        standards = [{'path': row['member'], 'sha256': row['sha256']} for row in profile['members']]
        plugin = [{'path': row['path'].removeprefix('plugins/spec/'), 'sha256': row['sha256']} for row in profile['native_contracts']]
        self.manifest = {'kind': 'stdo.installed-release-manifest', 'schema_version': 1, 'release': {'cut': 'v3.0.5-rc.1'},
            'standards': {'installed_root': 'standards', 'member_count': len(standards), 'members': standards},
            'auxiliary': {'plugin': {'installed_root': 'plugins/spec', 'member_count': len(plugin), 'members': plugin},
                          'license': {'path': 'LICENSE', 'sha256': c._sha((self.installation / 'LICENSE').read_bytes())},
                          'release_note': {'installed_path': 'release/release-note.md', 'sha256': c._sha((self.installation / 'release/release-note.md').read_bytes())}}}
        self.f.policy['method_profile'] = {**self.native, 'source': self.f.ref(self.f.authorities / 'profile.json', 'authority', 'profile.json')}
        self.f.policy['sources']['method'] = {'path': str(self.installation), 'kind': 'workspace', 'writable': False,
            'read_scope': [{'path': name, 'kind': 'file'} for name in ('manifest.json', 'LICENSE')] + [{'path': name, 'kind': 'directory'} for name in ('standards', 'plugins', 'release')]}
        self.f.policy['method_installation'] = {'root': 'method'}
        self.bind_manifest()

    def bind_manifest(self):
        (self.installation / 'manifest.json').write_bytes(c.canonical(self.manifest))
        definition = json.loads((self.f.workspace / 'Product.json').read_text())
        definition['constitution'] = {'stdo': {'basis': {'uri': 'stdo://releases/v3.0.5-rc.1/', 'manifest_sha256': c._sha((self.installation / 'manifest.json').read_bytes())}}}
        self.f.definition = self.f.write('Product.json', definition)
        self.f.policy['product']['definition'] = self.f.definition
        self._select_policy()

    def test_current_discovery_and_result_parent(self):
        value = self._ok(self._public('tools.describe', {}))
        self.assertEqual(value['method_profile'], self.native)
        self.assertEqual(value['builder']['uri'], 'stdo://releases/v3.0.4/')
        self.assertNotIn('results.conjoin', [row['name'] for row in value['operations']])
        response = self._public('source.read', {'source': self.f.law, 'encoding': 'utf8'})
        self._ok(response)
        self.assertEqual(response['operation_outcome']['source_parent']['sha256'], c.NATIVE305_FOUNDATIONS_SHA256)

    def test_current_mcp_discovery_and_source_transport(self):
        messages = [
            {'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {'protocolVersion': '2025-11-25', 'capabilities': {}, 'clientInfo': {'name': 'native305-control', 'version': '1'}}},
            {'jsonrpc': '2.0', 'method': 'notifications/initialized'},
            {'jsonrpc': '2.0', 'id': 2, 'method': 'tools/list', 'params': {}},
            {'jsonrpc': '2.0', 'id': 3, 'method': 'tools/call', 'params': {'name': 'source.read', 'arguments': {'schema': c.REQUEST, 'id': 'native305-mcp-source', 'operation': 'source.read', 'arguments': {'source': self.f.law, 'encoding': 'utf8'}}}},
        ]
        argv = [str(self.python), '-B', str(self.code / 'ac_support.py'), '--policy', str(self.policy_path), '--policy-sha256', self.policy_sha, '--principal', 'executive', 'mcp']
        raw = b''.join(c.canonical(message) + b'\n' for message in messages)
        result = subprocess.run(argv, input=raw, capture_output=True, timeout=30)
        folder = self.root / 'calls/mcp'; folder.mkdir(parents=True)
        (folder / 'stdin.jsonl').write_bytes(raw); (folder / 'stdout.jsonl').write_bytes(result.stdout); (folder / 'stderr.log').write_bytes(result.stderr)
        (folder / 'execution.json').write_bytes(c.canonical({'argv': argv, 'exit_code': result.returncode}))
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        replies = [json.loads(line) for line in result.stdout.splitlines()]
        self.assertEqual([reply['id'] for reply in replies], [1, 2, 3])
        self.assertEqual(replies[0]['result']['serverInfo']['version'], '3.0.5-rc.1')
        self.assertNotIn('results.conjoin', [tool['name'] for tool in replies[1]['result']['tools']])
        returned = replies[2]['result']['structuredContent']; self._ok(returned)
        self.assertEqual(returned['operation_outcome']['source_parent']['sha256'], c.NATIVE305_FOUNDATIONS_SHA256)
        self.assertEqual(returned['result']['value']['content'], 'one\ntwo\nthree\n')

    def test_wrong_cut_manifest_member_and_missing_installation(self):
        for variant in ('wrong_cut', 'predecessor_cut', 'wrong_manifest', 'changed_member', 'missing_selection'):
            with self.subTest(variant=variant):
                saved_policy = copy.deepcopy(self.f.policy)
                original = (self.installation / 'LICENSE').read_bytes()
                if variant in ('wrong_cut', 'predecessor_cut'):
                    value = json.loads((self.f.workspace / 'Product.json').read_text()); value['constitution']['stdo']['basis']['uri'] = 'stdo://releases/v3.0.4/' if variant == 'wrong_cut' else 'stdo://releases/v3.0.5/'
                    self.f.policy['product']['definition'] = self.f.write('Product.json', value)
                elif variant == 'wrong_manifest':
                    value = json.loads((self.f.workspace / 'Product.json').read_text()); value['constitution']['stdo']['basis']['manifest_sha256'] = '0' * 64
                    self.f.policy['product']['definition'] = self.f.write('Product.json', value)
                elif variant == 'changed_member':
                    (self.installation / 'LICENSE').write_text('changed')
                else:
                    del self.f.policy['method_installation']
                self._select_policy()
                with self.assertRaises(c.SupportError): c.Runtime.from_policy(self.policy_path, self.policy_sha, 'executive')
                self.f.policy = saved_policy; (self.installation / 'LICENSE').write_bytes(original); self.bind_manifest()

    def test_forged_matching_manifest_cannot_change_frozen_owner(self):
        target = self.installation / 'standards/ACTIVATION.md'; target.write_text('forged method owner')
        self.manifest['standards']['members'][0]['sha256'] = c._sha(target.read_bytes()); self.bind_manifest()
        with self.assertRaises(c.SupportError) as caught: c.Runtime.from_policy(self.policy_path, self.policy_sha, 'executive')
        self.assertEqual(caught.exception.code, 'basis_stale')

    def test_long_lived_runtime_rechecks_members_and_population(self):
        runtime = c.Runtime.from_policy(self.policy_path, self.policy_sha, 'executive')
        (self.installation / 'extra.txt').write_text('unselected')
        with self.assertRaises(c.SupportError): c.require_operation(runtime, 'tools.describe')
        (self.installation / 'extra.txt').unlink()
        (self.installation / 'standards/ACTIVATION.md').write_text('changed')
        with self.assertRaises(c.SupportError): c.require_operation(runtime, 'tools.describe')

    def storage_boundary(self, variant):
        def tree():
            return {p.relative_to(self.installation).as_posix(): ('symlink', str(p.readlink())) if p.is_symlink() else ('file', p.read_bytes()) if p.is_file() else ('directory', None) for p in self.installation.rglob('*')}
        before = tree()
        selected = self.installation / 'runtime-evidence'
        if variant == 'equal': selected = self.installation
        elif variant == 'ancestor': selected = self.installation.parent
        elif variant == 'ancestor-alias':
            alias = self.root / 'method-alias'; alias.symlink_to(self.installation, target_is_directory=True)
            selected = alias / 'runtime-evidence'
        elif variant == 'writable-source':
            self.f.policy['sources']['method-write-alias'] = {'path': str(self.installation), 'kind': 'workspace', 'writable': True, 'read_scope': [{'path': 'standards', 'kind': 'directory'}]}
            selected = self.root / 'disjoint-evidence'
        elif variant == 'disjoint': selected = self.root / 'disjoint-evidence'
        elif variant.startswith('case-'):
            alias = self.installation.with_name('METHOD')
            if not alias.exists() or not alias.samefile(self.installation): self.skipTest('Filesystem has no case alias for this control')
            self.assertNotEqual(alias.resolve(), self.installation.resolve())
            if variant == 'case-descendant': selected = alias / 'missing-parent' / 'runtime-evidence'
            elif variant == 'case-equal': selected = alias
            elif variant == 'case-ancestor': selected = self.root.with_name(self.root.name.upper())
            elif variant == 'case-writable-source':
                self.f.policy['sources']['method-write-alias'] = {'path': str(alias), 'kind': 'workspace', 'writable': True, 'read_scope': [{'path': 'standards', 'kind': 'directory'}]}
                selected = self.root / 'disjoint-evidence'
        self.f.policy['evidence_root'] = str(selected)
        self.f.policy['product']['authority_binding']['result_surface']['root'] = str(selected)
        self._select_policy()
        response = self.public_as('executive', 'tools.describe', {})
        after = tree()
        self.assertEqual(after, before, 'public startup must not mutate immutable method')
        if variant == 'disjoint':
            self._ok(response); self.assertTrue(selected.is_dir())
        else:
            self.assertEqual(response['status'], 'refused', response)
            self.assertEqual(response['refusal']['code'], 'role_effect_denied')
            self.assertIsNone(response['evidence'])
            if variant not in ('equal', 'ancestor', 'case-equal', 'case-ancestor'): self.assertFalse(selected.exists())

    def test_evidence_descendant_is_refused_before_effects(self): self.storage_boundary('descendant')
    def test_evidence_equal_is_refused_before_effects(self): self.storage_boundary('equal')
    def test_evidence_ancestor_is_refused_before_effects(self): self.storage_boundary('ancestor')
    def test_evidence_resolved_ancestor_alias_is_refused_before_effects(self): self.storage_boundary('ancestor-alias')
    def test_writable_method_alias_is_refused_before_effects(self): self.storage_boundary('writable-source')
    def test_disjoint_evidence_location_still_works(self): self.storage_boundary('disjoint')
    def test_case_alias_future_evidence_descendant_is_refused_before_effects(self): self.storage_boundary('case-descendant')
    def test_case_alias_evidence_equal_is_refused_before_effects(self): self.storage_boundary('case-equal')
    def test_case_alias_evidence_ancestor_is_refused_before_effects(self): self.storage_boundary('case-ancestor')
    def test_case_alias_writable_method_scope_is_refused_before_effects(self): self.storage_boundary('case-writable-source')

    def test_changed_boundary_helper_refuses_before_evidence(self):
        copied = self.root / 'copied-provider'
        shutil.copytree(self.code, copied, ignore=shutil.ignore_patterns('__pycache__'))
        helper = copied / 'ac_fs_boundary.py'
        helper.write_bytes(helper.read_bytes() + b'\n# changed dependency\n')
        self.code = copied
        evidence_root = Path(self.f.policy['evidence_root'])
        before = {p.relative_to(evidence_root).as_posix(): p.read_bytes() if p.is_file() else None for p in evidence_root.rglob('*')}
        response = self.public_as('executive', 'tools.describe', {})
        self.assertEqual(response['status'], 'refused', response)
        self.assertEqual(response['refusal']['code'], 'dependency_changed')
        self.assertIsNone(response['evidence'])
        after = {p.relative_to(evidence_root).as_posix(): p.read_bytes() if p.is_file() else None for p in evidence_root.rglob('*')}
        self.assertEqual(after, before)

    def test_supervisor_pins_boundary_helper_and_refuses_stale_or_missing_pin(self):
        runtime = c.Runtime.from_policy(self.policy_path, self.policy_sha, 'executive')
        ref = {'id': 'sha256:' + '0' * 64, 'sha256': '0' * 64}
        binding = effects._supervisor_binding(runtime, ref)
        helper = str((self.code / 'ac_fs_boundary.py').resolve())
        selected = [row for row in binding['modules'] if row['path'] == helper]
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0]['sha256'], c.FS_BOUNDARY_SHA256)
        effects._verify_supervisor(binding, runtime, ref)
        for variant in ('changed', 'missing'):
            changed = copy.deepcopy(binding)
            if variant == 'changed':
                next(row for row in changed['modules'] if row['path'] == helper)['sha256'] = '0' * 64
            else:
                changed['modules'] = [row for row in changed['modules'] if row['path'] != helper]
            with self.subTest(variant=variant), self.assertRaises(c.SupportError) as caught:
                effects._verify_supervisor(changed, runtime, ref)
            self.assertEqual(caught.exception.code, 'dependency_changed')

    def test_request_cannot_override_trusted_installation(self):
        request = self.f.request('tools.describe', {'method_installation': {'root': 'workspace'}})
        with self.assertRaises(c.SupportError): c.validate_request(request)
        request = self.f.request('tools.describe', {}); request['method_installation'] = {'root': 'workspace'}
        with self.assertRaises(c.SupportError): c.validate_request(request)

    def test_missing_issuer_and_recipient_grants_do_not_dispatch(self):
        self.f.policy['principals']['executive']['operations'].remove('dispatch.start'); self._select_policy()
        response = self._public('dispatch.start', {'preflight': {'id': 'sha256:' + '0' * 64, 'sha256': '0' * 64}})
        self.assertEqual(response['refusal']['code'], 'authority_missing')
        self.assertFalse(self.target.exists())
        self.f.policy['principals']['executive']['operations'].append('dispatch.start')
        self.f.policy['grants']['work']['targets'].remove('worker'); self._select_policy()
        context = self._assemble()
        response = self._public('contract.preflight', {'context': context, 'grant_id': 'work', 'executor_id': 'registered', 'result_key': 'missing-recipient', 'observations': []})
        value = self._ok(response)
        self.assertEqual(value['decision'], 'rejected')
        refused = self._public('dispatch.start', {'preflight': response['result']['artifact']})
        self.assertEqual(refused['status'], 'refused')
        self.assertFalse(self.target.exists())

    def test_uncertain_retry_retains_original_activation(self):
        legacy.PublicRetryTests.test_public_reassembled_context_cannot_reset_activation_history(self)

    def test_actual_process_capture_preserves_incomplete_report(self):
        native301.Native301PublicTests.test_actual_process_completion_capture_and_return_check(self)

    def public_as(self, principal, operation, arguments):
        self.sequence += 1; folder = self.root / 'calls' / (str(self.sequence).zfill(3) + '-' + principal + '-' + operation); folder.mkdir(parents=True)
        request = {'schema': c.REQUEST, 'id': 'public-' + str(self.sequence), 'operation': operation, 'arguments': arguments}
        path = folder / 'request.json'; path.write_bytes(c.canonical(request))
        argv = [str(self.python), '-B', str(self.code / 'ac_support.py'), '--policy', str(self.policy_path), '--policy-sha256', self.policy_sha, '--principal', principal, 'call', '--request', str(path)]
        result = subprocess.run(argv, capture_output=True, timeout=20)
        (folder / 'stdout.bin').write_bytes(result.stdout); (folder / 'stderr.bin').write_bytes(result.stderr)
        (folder / 'execution.json').write_bytes(c.canonical({'argv': argv, 'returncode': result.returncode}))
        return json.loads(result.stdout)

    def test_actual_reviewer_severity_return_is_preserved_without_priority(self):
        candidate = self.f.write('inputs/candidate.txt', b'candidate with bounded material defect')
        claim = self.f.write('inputs/claim.json', {'id': 'review-current-candidate', 'candidate_sources': [candidate]})
        actor_source = '''import sys,json,hashlib
body=json.loads(sys.stdin.read().split('\\n',1)[1]); p=body['packet']
finding={'severity':3,'scale':'1-highest-5-lowest','consequence':'bounded material failure','downstream_impact':'one declared dependency','containment':'not established','priority':None,'disposition':None}
result={'schema':'a_c.fd-support.closed-return/1','id':'reviewer-return','frame':{k:p['frame'][k] for k in ('id','revision')},'activation':{'id':p['activation']['id'],'sha256':hashlib.sha256(json.dumps(p,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()},'subject':p['subject_basis']['subject'],'basis':{k:p['subject_basis'][k] for k in ('method_profile','observations')},'actor':{'id':'reviewer','family':'B','authorship':'reviewer'},'consumer':'executive','evaluations':[{'id':'review','predicate':p['frame']['evaluation'],'domain_outcome':finding,'core_value':'falsified','evidence':[],'residuals':[],'invalidators':[]}],'not_performed':[],'work_result':None,'residuals':[],'invalidators':[]}
print(json.dumps(result,ensure_ascii=False,sort_keys=True,separators=(',',':')))
'''
        actor = self.f.write('inputs/reviewer.py', actor_source.encode())
        executor = self.f.policy['executors']['registered']; executor['actor_id'] = 'reviewer'
        executor['argv'] = [str(self.python), '-B', str(self.f.workspace / 'inputs/reviewer.py')]; executor['dependencies'] = [actor]
        self._select_policy()
        acquired = self.public_as('reviewer', 'source.read', {'source': self.f.law, 'encoding': 'utf8'})
        self._ok(acquired)
        evidence = self._ok(self.public_as('reviewer', 'evidence.read', {'artifact': acquired['evidence']}))
        source_inputs = evidence['envelope']['payload']['acquisitions']
        expectation = self._ok(self.public_as('reviewer', 'review.prepare', {'phase': 'expectation', 'claim': claim, 'sources': [self.f.law], 'candidate': candidate, 'proof': [], 'comparison': None, 'expectations': None, 'expectation_body': {'text': 'Derive expected behavior from the acquired law.', 'source_inputs': source_inputs}}))
        contract = {'schema': 'a_c.fd-support.return-contract/1', 'id': 'review-return', 'authority_source': self.f.owner, 'carrier': 'a_c.fd-support.closed-return/1', 'output_slot': 'final_stdout_object', 'required_evaluations': [{'id': 'review', 'predicate': self.f.law}], 'role': 'Reviewer', 'proof': {'claim': claim, 'expectations': expectation['expectations'], 'proof_sources': [], 'comparison': None, 'independence_policy': None, 'predicate_ids': []}}
        self.f.return_contract = self.f.write('inputs/review-return.json', contract)
        packet = self.f.packet('Reviewer'); packet['profile_additions']['reviewer']['claim'] = claim; packet['profile_additions']['reviewer']['severity_scale'] = self.f.law
        context = self._assemble(packet)
        started = self._public('dispatch.start', {'preflight': self._admit(context)}); self._ok(started)
        attempt = started['result']['artifact']; observed = self._ok(self._finished(attempt))
        captured = self._public('return.capture', {'attempt': attempt, 'payload': observed['output']['stdout'], 'return_contract': self.f.return_contract}); self._ok(captured)
        checked = self._ok(self._public('return.check', {'return': captured['result']['artifact'], 'context': context, 'consumer': 'executive', 'observations': [], 'predicates': []}))
        self.assertTrue(checked['consumable'], checked['gaps'])
        finding = checked['original']['evaluations'][0]['domain_outcome']
        self.assertEqual(finding['severity'], 3); self.assertEqual(finding['scale'], '1-highest-5-lowest')
        self.assertIsNone(finding['priority']); self.assertIsNone(finding['disposition'])
        self.assertEqual(checked['original']['evaluations'][0]['core_value'], 'falsified')

if __name__ == '__main__': unittest.main()
