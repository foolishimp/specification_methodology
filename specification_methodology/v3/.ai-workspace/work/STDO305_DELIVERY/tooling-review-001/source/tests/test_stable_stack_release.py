from __future__ import annotations

import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
import zipfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import check_stack_release as api
import stable_stack_release as stable
import stdo_source_freeze as freeze


def put(root, name, value):
    p = root / name; p.parent.mkdir(parents=True, exist_ok=True)
    raw = value if isinstance(value, bytes) else api.canonical_json_bytes(value)
    p.write_bytes(raw)
    return {'path': name, 'sha256': api.sha256(raw), 'bytes': len(raw)}


def manifest():
    value = json.loads((ROOT / 'stack_release.json').read_bytes())
    value['cohort']['status'] = 'candidate'
    value['third_party_dependencies'] = [{'name': 'independent-runtime', 'version': '4.24.0', 'sha256': 'e' * 64, 'provenance': 'test exact runtime'}]
    for name, product in value['products'].items():
        product['subject'] = {'sha256': hashlib.sha256(name.encode()).hexdigest()}
    value['components']['representation']['facts'] = {'model_sha256': 'c' * 64}
    return value


class StableShapeTests(unittest.TestCase):
    def test_exact_five_product_stable_profile(self):
        stable.check_shape(manifest())

    def test_assembling_never_ready(self):
        value = manifest(); value['cohort']['status'] = 'assembling'
        with self.assertRaisesRegex(ValueError, 'assembling'):
            stable.check_shape(value)

    def test_missing_extra_mismatched_and_rc_members_refuse(self):
        for mutation in (
            lambda v: v['products'].pop('stdo_skills'),
            lambda v: v['products'].update(extra={}),
            lambda v: v['products']['a_c'].update(version='3.0.4'),
            lambda v: v['components']['lean'].update(version='3.0.4'),
            lambda v: v['components'].pop('proof_reader'),
            lambda v: v['cohort'].update(version='3.0.5-rc.1', cut='v3.0.5-rc.1'),
            lambda v: v['components']['lean'].update(required_claims=['installed_lean']),
            lambda v: v['dependency_edges'].pop(),
            lambda v: v.update(third_party_dependencies=[]),
        ):
            with self.subTest(mutation=mutation):
                value = manifest(); mutation(value)
                with self.assertRaises((ValueError, KeyError)):
                    stable.check_shape(value)

    def test_historical_fixture_retains_exact_bytes_and_schema(self):
        raw = (ROOT / 'scripts/fixtures/stack_release-v2.5.1-rc.2.json').read_bytes()
        self.assertEqual(api.sha256(raw), '1af97aeb7df12cd31dbddc04fad55a3ef6b3552c6e246a1c257aa942ec8ace18')
        failures = []; api.validate_shape(json.loads(raw), failures)
        self.assertEqual(failures, [])


class SubjectTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name); self.view = api.View(self.root)
        put(self.root, 'package/a.txt', b'exact A')
        put(self.root, 'package/b.txt', b'exact B')
        self.subject = stable.collect_subject(self.view, ['package'], api)

    def test_positive_exact_closure(self):
        self.assertEqual(stable.subject(self.view, self.subject, api), self.subject)

    def test_missing_extra_changed_and_duplicate_members_refuse(self):
        for operation in ('missing', 'extra', 'changed', 'duplicate'):
            with self.subTest(operation=operation):
                selected = copy.deepcopy(self.subject)
                if operation == 'missing': selected['members'].pop()
                if operation == 'extra': selected['members'].append({'path': 'package/extra', 'bytes': 1, 'sha256': 'a' * 64})
                if operation == 'changed': selected['members'][0]['sha256'] = 'b' * 64
                if operation == 'duplicate': selected['members'].append(selected['members'][0])
                with self.assertRaisesRegex(ValueError, 'inventory differs'):
                    stable.subject(self.view, selected, api)

    def test_live_extra_file_is_not_hidden_by_recomputed_count(self):
        put(self.root, 'package/new.txt', b'new')
        with self.assertRaisesRegex(ValueError, 'inventory differs'):
            stable.subject(self.view, self.subject, api)

    def test_symlink_is_not_dereferenced(self):
        (self.root / 'package/link').symlink_to('../outside')
        put(self.root, 'outside', b'external')
        with self.assertRaisesRegex(ValueError, 'regular contained'):
            stable.collect_subject(self.view, ['package'], api)

    def test_unsafe_scope_refuses(self):
        for name in ('../package', '/package', 'package//a', 'package\\a'):
            with self.assertRaises(ValueError): stable.collect_subject(self.view, [name], api)


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name); self.view = api.View(self.root); self.manifest = manifest()
        self.result = {'status': 'verified', 'actual_operation': {'input_count': 68, 'failed': []}}
        self.result_ref = put(self.root, 'run/result.json', self.result)
        self.producer = put(self.root, 'tools/qualifier.py', b'qualified producer fixture\n')
        self.record = {'kind': 'stdo.cohort-evidence/1', 'claim': 'installed_graphify', 'status': 'passed',
                       'source_identity_sha256': self.manifest['source']['source_identity_sha256'],
                       'subjects': {'a_c': self.manifest['products']['a_c']['subject']['sha256']},
                       'category': 'execution', 'limits': ['bounded fixture operation'], 'producer': self.producer,
                       'operation': 'installed-model-projection', 'execution': {'argv': ['python3', 'tools/qualifier.py'], 'returncode': 0,
                       'environment': {'python': '3.11'}, 'stdout': put(self.root, 'run/stdout', b'actual execution output'),
                       'stderr': put(self.root, 'run/stderr', b''), 'inputs': [put(self.root, 'input.json', {'records': 68})],
                       'outputs': [self.result_ref]}, 'result': self.result_ref,
                       'observations': [{'pointer': '/actual_operation/input_count', 'equals': 68}, {'pointer': '/actual_operation/failed', 'equals': []}]}

    def check(self, record=None, claim='installed_graphify'):
        ref = put(self.root, 'evidence.json', record or self.record)
        return stable.evidence(self.view, ref, claim, self.manifest, api)

    def test_actual_output_binding_passes(self):
        self.check()

    def test_label_only_stale_subject_failed_execution_and_false_observation_refuse(self):
        mutations = [lambda r: r.pop('execution'), lambda r: r.update(source_identity_sha256='d' * 64),
                     lambda r: r['subjects'].update(a_c='d' * 64), lambda r: r['execution'].update(returncode=1),
                     lambda r: r.update(operation='--help'), lambda r: r['observations'][0].update(equals=69),
                     lambda r: r['execution'].update(outputs=[]), lambda r: r['execution'].update(argv=['other.py'])]
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                record = copy.deepcopy(self.record); mutation(record)
                with self.assertRaises((ValueError, KeyError)): self.check(record)

    def test_changed_transcript_is_rejected(self):
        (self.root / 'run/stdout').write_bytes(b'different execution')
        with self.assertRaisesRegex(ValueError, 'artifact bytes differ'): self.check()

    def lean(self):
        result = {'schema': 'a_c.formal-gate.result/1', 'status': 'verified', 'model': {'sha256': 'c' * 64},
                  'requested_claims': ['whole-model-source-correspondence'], 'checked_claims': ['whole-model-source-correspondence'],
                  'observations': {'current_dynamic_proof_invocations': 7, 'current_kernel_replay_invocations': 1,
                                   'current_runtime_invocations': 1, 'stages': [{'stage': 'kernel', 'exit_code': 0}]},
                  'runtime_identity': {'pins': {'lean': '4.24.0'}}, 'evidence': {'members': [{'path': 'GateModel.olean'}]}}
        record = copy.deepcopy(self.record); record['claim'] = 'exact_candidate_lean_result'
        model_ref = put(self.root, 'current-model.json', {'model': 'current'})
        source_ref = put(self.root, 'selected-source.json', {'source': 'current'})
        self.manifest['components']['representation']['facts']['model'] = model_ref
        self.manifest['components']['representation']['facts']['model_sha256'] = model_ref['sha256']
        self.manifest['source']['sha256'] = source_ref['sha256']
        result['model']['sha256'] = model_ref['sha256']
        record['execution']['inputs'].extend([model_ref, source_ref])
        return result, record

    def test_current_lean_requires_exact_model_and_real_completed_stages(self):
        result, record = self.lean()
        for mutation in (None, lambda r: r['model'].update(sha256='d' * 64),
                         lambda r: r['observations'].update(current_dynamic_proof_invocations=0),
                         lambda r: r['observations']['stages'][0].update(exit_code=1),
                         lambda r: r.update(checked_claims=[]), lambda r: r['evidence'].update(members=[])):
            current = copy.deepcopy(result)
            if mutation: mutation(current)
            reference = put(self.root, 'run/lean.json', current); record['result'] = reference; record['execution']['outputs'] = [reference]
            if mutation:
                with self.assertRaises(ValueError): self.check(record, 'exact_candidate_lean_result')
            else: self.check(record, 'exact_candidate_lean_result')

    def test_independent_review_requires_exact_report_author_separation_and_disposition(self):
        record = {'kind': 'stdo.cohort-evidence/1', 'claim': 'independent_release_review', 'status': 'passed',
                  'source_identity_sha256': self.manifest['source']['source_identity_sha256'],
                  'subjects': {p: v['subject']['sha256'] for p, v in self.manifest['products'].items()},
                  'category': 'independent_assessment', 'assessor': 'reviewer', 'authors': ['writer'],
                  'conclusion': 'satisfied', 'open_required_findings': [], 'executive_disposition': 'accepted_for_release_scope',
                  'report': put(self.root, 'review.md', b'Exact bounded independent assessment.'), 'limits': []}
        self.check(record, 'independent_release_review')
        for mutation in (lambda r: r.update(assessor='writer'), lambda r: r.update(open_required_findings=['S3']),
                         lambda r: r.pop('executive_disposition')):
            current = copy.deepcopy(record); mutation(current)
            with self.assertRaises(ValueError): self.check(current, 'independent_release_review')


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name); self.manifest = manifest(); self.carrier = 'b' * 40; self.native = 'a' * 40
        self.manifest['native'] = {'manifest': put(self.root, 'native.json', {'release': {'commit': self.native}})}
        self.local = {'refs/heads/main': self.carrier}; self.tags = {}
        for index, (name, product) in enumerate(sorted(self.manifest['products'].items())):
            commit = self.native if name == 'specification_methodology' else self.carrier
            tag = str(index + 1) * 40; self.tags[product['release_ref']] = (tag, commit)
            if product.get('release_branch'): self.local[product['release_branch']] = commit
        self.previous = {'refs/tags/specification_methodology/v3.0.4': 'd' * 40, 'refs/tags/specification_methodology/v3.0.4^{}': 'e' * 40}
        expected = {'refs/heads/main': 'c' * 40}
        for product in self.manifest['products'].values():
            expected[product['release_ref']] = None
            if product.get('release_branch'): expected[product['release_branch']] = None
        self.manifest['publication']['expected_remote'] = expected
        self.manifest['publication']['preserved_immutable_refs'] = self.previous.copy()
        self.remote = {**self.previous, 'refs/heads/main': 'c' * 40}
        def git(_root, *args, **kwargs):
            if args[0] == 'rev-parse': return SimpleNamespace(stdout=self.carrier)
            if args[0] == 'ls-remote': return SimpleNamespace(stdout='\n'.join(v + '\t' + k for k, v in self.remote.items()))
            raise AssertionError(args)
        self.adapter = SimpleNamespace(**{k: getattr(api, k) for k in ('sha256', 'canonical_value_sha256')},
            View=lambda root, revision=None: api.View(root), git=git,
            direct_ref_oid=lambda root, ref: self.local.get(ref),
            annotated_ref=lambda root, ref, failures: self.tags.get(ref),
            validate_remote_endpoint=lambda root, remote, url, failures: None)

    def check(self, phase='refs'):
        return stable.ref_graph(self.root, self.manifest, self.carrier, phase, 'origin', self.adapter)

    def test_exact_plan_has_six_leased_immutable_object_refspecs(self):
        result = self.check(); argv = result['push_argv']
        self.assertEqual(argv[:3], ['git', 'push', '--atomic'])
        self.assertEqual(len([x for x in argv if x.startswith('--force-with-lease=')]), 6)
        self.assertEqual(len([x for x in argv if ':refs/' in x and not x.startswith('--')]), 6)
        self.assertFalse(any('HEAD:' in x for x in argv))

    def test_explicit_optional_branch_is_included_in_exact_atomic_set(self):
        branch = 'refs/heads/release/a_c/3.0.5'
        self.manifest['products']['a_c']['release_branch'] = branch
        self.manifest['publication']['expected_remote'][branch] = None
        self.local[branch] = self.carrier
        result = self.check()
        self.assertIn(self.carrier + ':' + branch, result['push_argv'])
        self.assertEqual(len([x for x in result['push_argv'] if x.startswith('--force-with-lease=')]), 7)

    def test_remote_drift_partial_expectation_preserved_drift_and_local_move_refuse(self):
        self.remote['refs/heads/main'] = 'f' * 40
        with self.assertRaisesRegex(ValueError, 'drifted'): self.check()
        self.remote['refs/heads/main'] = 'c' * 40
        self.manifest['publication']['expected_remote'].pop('refs/heads/main')
        with self.assertRaisesRegex(ValueError, 'complete push set'): self.check()
        self.manifest['publication']['expected_remote']['refs/heads/main'] = 'c' * 40
        self.remote['refs/tags/specification_methodology/v3.0.4'] = 'f' * 40
        with self.assertRaisesRegex(ValueError, 'preserved'): self.check()
        self.remote.update(self.previous); self.local['refs/heads/main'] = 'f' * 40
        with self.assertRaisesRegex(ValueError, 'carrier'): self.check()

    def test_published_graph_requires_every_direct_object_and_peel(self):
        self.remote['refs/heads/main'] = self.carrier
        for product in self.manifest['products'].values():
            ref = product['release_ref']; tag, target = self.tags[ref]
            self.remote.update({ref: tag, ref + '^{}': target})
            if product.get('release_branch'): self.remote[product['release_branch']] = target
        self.check('published')
        self.remote.pop('refs/tags/a_c/v3.0.5^{}')
        with self.assertRaisesRegex(ValueError, 'peel'): self.check('published')


class ManagerWheelTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name); self.view = api.View(self.root); self.value = manifest()
        self.source = 'manager/src/stdo_toolchain'
        put(self.root, self.source + '/__init__.py', b'__version__ = "3.0.5"\n')
        put(self.root, self.source + '/cli.py', b'def main(): return 0\n')

    def make(self, altered=False):
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, 'w') as archive:
            for name in ('__init__.py', 'cli.py'):
                raw = (self.root / self.source / name).read_bytes()
                archive.writestr('stdo_toolchain/' + name, raw + (b'changed' if altered else b''))
            archive.writestr('stdo_toolchain-3.0.5.dist-info/METADATA', 'Name: stdo-toolchain\nVersion: 3.0.5\n')
        ref = put(self.root, 'assets/stdo_toolchain-3.0.5-py3-none-any.whl', stream.getvalue())
        self.value['components']['manager']['facts'] = {'wheel': ref, 'source_root': self.source}

    def test_matching_wheel_source_and_runtime_version_pass(self):
        self.make(); stable.manager(self.view, self.value, api)

    def test_relabelled_different_wheel_source_refuses(self):
        self.make(altered=True)
        with self.assertRaisesRegex(ValueError, 'exact selected source'):
            stable.manager(self.view, self.value, api)

    def test_stale_runtime_version_refuses_even_if_wheel_matches_source(self):
        put(self.root, self.source + '/__init__.py', b'__version__ = "0.1.6"\n')
        self.make()
        with self.assertRaisesRegex(ValueError, 'runtime version'):
            stable.manager(self.view, self.value, api)


class PublicReadbackTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name); self.view = api.View(self.root); self.manifest = manifest()
        self.manifest['native'] = {'manifest': {'sha256': 'a' * 64}}
        base = 'https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology%2Fv3.0.5/'
        self.asset = {'name': 'manager.whl', 'url': base + 'manager.whl', **put(self.root, 'assets/manager.whl', b'bound wheel bytes')}
        self.manifest['publication']['assets'] = [self.asset]
        self.external = self.manifest['publication']['external_manifest_asset']
        self.raw = api.canonical_json_bytes(self.manifest); put(self.root, 'frozen.json', self.raw)
        self.receipt = {'kind': 'stdo.public-cohort-readback/1', 'status': 'verified',
                        'source_identity_sha256': self.manifest['source']['source_identity_sha256'],
                        'unauthenticated': True, 'assets': [self.asset], 'fresh_store': 'fresh/store',
                        'installed_manifest_sha256': 'a' * 64,
                        'external_manifest': {**self.external, 'sha256': api.sha256(self.raw)},
                        'installed_qualification': {'path': 'installed.json', 'sha256': 'b' * 64}}

    def check(self, responses):
        ref = put(self.root, 'readback.json', self.receipt)
        with patch.object(stable.urllib.request, 'urlopen', side_effect=[io.BytesIO(value) for value in responses]) as request, patch.object(stable, 'evidence'):
            result = stable.public(self.view, self.manifest, 'frozen.json', ref['path'], ref['sha256'], api)
            return result, request

    def test_public_gate_reacquires_wheel_and_external_manifest_anonymously(self):
        _, request = self.check([b'bound wheel bytes', self.raw])
        self.assertEqual(request.call_count, 2)
        for call in request.call_args_list:
            self.assertNotIn('Authorization', call.args[0].headers)
            self.assertNotIn('Cookie', call.args[0].headers)

    def test_staged_file_does_not_excuse_wrong_public_bytes(self):
        with self.assertRaisesRegex(ValueError, 'fresh anonymous public asset differs'):
            self.check([b'wrong publicly downloaded bytes'])

    def test_external_manifest_does_not_contain_its_own_digest(self):
        self.assertNotIn('sha256', self.manifest['publication']['external_manifest_asset'])
        self.receipt['external_manifest']['sha256'] = 'c' * 64
        with self.assertRaisesRegex(ValueError, 'exact frozen B'):
            self.check([])


class NativeConfigurationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup); self.root = Path(self.tmp.name)
        spec = importlib.util.spec_from_file_location('native_under_test', ROOT / 'specification_methodology/v3/build_tenants/common-tools/native_release.py')
        self.tool = importlib.util.module_from_spec(spec); spec.loader.exec_module(self.tool)
        self.value = json.loads((ROOT / 'stack_release.json').read_bytes())

    def select(self, value=None):
        ref = put(self.root, 'candidate.json', value or self.value)
        return self.tool.configure(self.root / ref['path'], ref['sha256'])

    def test_default_history_and_configured_successor_are_distinct(self):
        self.assertEqual(self.tool.VERSION, '3.0.4'); self.assertEqual(self.tool.record_kind('native-identity'), 'stdo304.native-identity/1')
        self.select(); self.assertEqual(self.tool.VERSION, '3.0.5')
        self.assertEqual(self.tool.PREDECESSOR, '16bc30d215915a4b7b3ed2f13e52e14510ae1c9d')
        self.assertEqual(self.tool.MANAGER_WHEEL, 'stdo_toolchain-3.0.5-py3-none-any.whl')
        self.assertEqual(self.tool.record_kind('native-identity'), 'stdo.native-identity/1')
        self.assertNotIn('historical representation', self.tool.tag_message({'commit': 'a', 'package_path': 'b', 'package_tree': 'c'}).decode())

    def test_configured_cohort_cannot_emit_standalone_push(self):
        self.select()
        with self.assertRaisesRegex(ValueError, 'standalone native push is forbidden'):
            self.tool.publication_plan(SimpleNamespace())

    def test_native_preparation_refuses_semantic_drift_before_packaging(self):
        self.select()
        record = json.loads((ROOT / self.value['source']['path']).read_bytes())
        package = ROOT / record['source_root']
        data = {row['path']: (package / row['path']).read_bytes() for row in record['members'] + record['native_contracts']}
        data['plugins/spec/references/REFRESH.md'] += b'\nchanged procedure\n'
        with self.assertRaisesRegex(ValueError, 'semantic member changed'):
            self.tool.validate_payload([{'path': name} for name in data], data)

    def test_wrong_pin_version_output_territory_and_manager_refuse(self):
        ref = put(self.root, 'candidate.json', self.value)
        with self.assertRaisesRegex(ValueError, 'digest mismatch'): self.tool.configure(self.root / ref['path'], 'f' * 64)
        for mutation in (lambda v: v['cohort'].update(version='3.0.5-rc.1'),
                         lambda v: v['native_preparation'].update(output_root='../outside'),
                         lambda v: v['native_preparation'].update(manager_wheel='stdo_toolchain-0.1.6-py3-none-any.whl')):
            value = copy.deepcopy(self.value); mutation(value)
            with self.assertRaises(ValueError): self.select(value)


if __name__ == '__main__':
    unittest.main()
