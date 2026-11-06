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
import stable_release_evidence as owner_evidence


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
        self.root = Path(self.tmp.name).resolve(); self.view = api.View(self.root); self.manifest = manifest()

    def record(self, claim):
        return {'kind': 'stdo.cohort-evidence/1', 'claim': claim, 'status': 'passed',
                'source_identity_sha256': self.manifest['source']['source_identity_sha256'],
                'subjects': {p: v['subject']['sha256'] for p, v in self.manifest['products'].items()}, 'limits': []}

    def check(self, record):
        ref = put(self.root, 'evidence.json', record)
        return stable.evidence(self.view, ref, record['claim'], self.manifest, api)

    def test_generic_verified_observation_cannot_establish_any_execution_claim(self):
        for claim in sorted({c for _, claims in stable.COMPONENTS.values() for c in claims} - stable.ASSESSMENTS):
            with self.subTest(claim=claim):
                record = self.record(claim)
                record.update(category='execution', operation='current', observations=[{'pointer': '/status', 'equals': 'verified'}],
                              result=put(self.root, 'result.json', {'status': 'verified'}), execution={'argv': ['qualifier.py', '--help'], 'returncode': 0})
                with self.assertRaises((ValueError, KeyError)):
                    self.check(record)

    def test_unknown_claim_is_not_a_success_extension_point(self):
        with self.assertRaisesRegex(ValueError, 'unknown required'):
            self.check(self.record('anything-that-says-verified'))

    def test_independent_review_requires_exact_report_author_separation_and_disposition(self):
        record = self.record('independent_release_review')
        record.update(category='independent_assessment', assessor='reviewer', authors=['writer'], conclusion='satisfied',
                      open_required_findings=[], executive_disposition='accepted_for_release_scope', report=put(self.root, 'review.md', b'Exact bounded independent assessment.'))
        self.check(record)
        for mutation in (lambda r: r.update(assessor='writer'), lambda r: r.update(open_required_findings=['S3']),
                         lambda r: r.pop('executive_disposition'), lambda r: r['subjects'].pop('stdo_skills')):
            current = copy.deepcopy(record); mutation(current)
            with self.assertRaises(ValueError): self.check(current)


class InstalledEvidenceTests(unittest.TestCase):
    """A real isolated Python loads exact fixture manager sources and verifies
    its store. The fixture is test data, never release qualification evidence.
    """
    def setUp(self):
        import venv
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name).resolve(); self.root = self.base / 'repository'; self.root.mkdir()
        self.workspace = self.base / 'installed'; self.workspace.mkdir(); self.view = api.View(self.root); self.manifest = manifest()
        self.store = self.workspace / 'store'; self.native = self.store / 'releases/v3.0.5'; self.native.mkdir(parents=True)
        self.manager_root = 'specification_methodology/v2/src/stdo_toolchain'
        native_source = 'specification_methodology/v3/build_tenants/common/standards/CURRENT.md'
        self.sources = {native_source: b'current semantic owner\n', self.manager_root + '/__init__.py': b'__version__ = "3.0.5"\n',
                       self.manager_root + '/cli.py': b'''import sys,json,hashlib\nfrom pathlib import Path\ndef main():\n a=sys.argv[1:];store=Path(a[a.index('--store')+1]);cut=a[a.index('verify')+1];root=store/'releases'/cut;raw=(root/'manifest.json').read_bytes();m=json.loads(raw);print(json.dumps({'cut':cut,'uri':'stdo://releases/'+cut+'/','path':str(root),'manifest_sha256':hashlib.sha256(raw).hexdigest(),'valid':True,'failures':[],'manifest':m}))\nif __name__=='__main__':main()\n'''}
        for product in stable.PRODUCTS - {'specification_methodology'}:
            self.sources[product + '/VERSION'] = b'3.0.5\n'
        for name, raw in self.sources.items(): put(self.root, name, raw)
        for name, product in self.manifest['products'].items():
            scope = sorted(p for p in self.sources if p.startswith(name + '/'))
            product['subject'] = stable.collect_subject(self.view, scope, api)
        self.semantic = {'members': [{'path': 'standards/CURRENT.md', 'sha256': api.sha256(self.sources[native_source]), 'bytes': len(self.sources[native_source])}], 'native_contracts': []}
        self.manifest['source'] = {**put(self.root, 'source.json', self.semantic), 'source_identity_sha256': '5' * 64}
        self.native_manifest = {'kind': 'stdo.installed-release-manifest', 'release': {'cut': 'v3.0.5', 'commit': 'a' * 40},
                                'standards': {'members': [{'path': 'CURRENT.md', 'sha256': api.sha256(self.sources[native_source])}]}, 'auxiliary': {}}
        self.manifest['native'] = {'manifest': put(self.root, 'assets/stdo-v3.0.5-manifest.json', self.native_manifest)}
        (self.native / 'manifest.json').write_bytes((self.root / self.manifest['native']['manifest']['path']).read_bytes())
        (self.native / 'standards').mkdir(); (self.native / 'standards/CURRENT.md').write_bytes(self.sources[native_source])
        env = self.workspace / 'manager'; venv.create(env, with_pip=False)
        self.python = env / 'bin/python3'
        site = next((env / 'lib').glob('python*/site-packages')); package = site / 'stdo_toolchain'; package.mkdir()
        self.mapping = {}
        for source, raw in self.sources.items():
            if source.startswith(self.manager_root + '/'):
                destination = package / source.removeprefix(self.manager_root + '/')
            elif source == native_source:
                destination = self.native / 'standards/CURRENT.md'
            else:
                destination = self.workspace / 'products' / source
            destination.parent.mkdir(parents=True, exist_ok=True); destination.write_bytes(raw); self.mapping[source] = str(destination)
        self.physical = self.python.resolve(); self.runtime = {'invocation': str(self.python), 'executable_realpath': str(self.physical), 'sha256': api.sha256(self.physical.read_bytes()), 'version': '3.' + str(sys.version_info.minor)}
        entry = env / 'bin/stdo'; entry.write_text('#!' + str(self.python) + '\nfrom stdo_toolchain.cli import main\nmain()\n'); entry.chmod(0o755)
        wheel = put(self.root, 'assets/stdo_toolchain-3.0.5-py3-none-any.whl', b'exact fixture wheel')
        self.manifest['components']['manager']['facts'] = {'source_root': self.manager_root, 'wheel': wheel}
        shared = {'cut': 'v3.0.5', 'uri': 'stdo://releases/v3.0.5/', 'path': str(self.native), 'manifest_sha256': self.manifest['native']['manifest']['sha256']}
        verified = {**shared, 'valid': True, 'failures': [], 'manifest': self.native_manifest}
        installed = {**shared, 'status': 'installed', 'release': self.native_manifest['release']}
        self.installation = {'kind': 'stdo.installed-cohort/1', 'version': '3.0.5', 'source_identity_sha256': '5' * 64,
            'acquisition': {'mode': 'public_readback', 'repository': self.manifest['publication']['repository_url']},
            'subjects': {p: v['subject']['sha256'] for p, v in self.manifest['products'].items()},
            'workspace': str(self.workspace), 'store': str(self.store), 'native_root': str(self.native), 'files': self.mapping,
            'manager': {'version': '3.0.5', 'python': self.runtime, 'executable': {'path': str(entry), 'sha256': api.sha256(entry.read_bytes())}}}
        for command, result in [('install', installed), ('verify', verified)]:
            argv = [str(entry), '--store', str(self.store), command, 'v3.0.5']
            if command == 'install': argv += ['--repository', self.manifest['publication']['repository_url']]
            argv += ['--manifest-sha256', shared['manifest_sha256']]
            self.installation[command] = {'execution': {'argv': argv, 'returncode': 0,
                'stdout': put(self.root, command + '.stdout', result), 'stderr': put(self.root, command + '.stderr', b'')},
                'result': put(self.root, command + '.json', result)}
        self.record = {'kind': 'stdo.cohort-evidence/1', 'claim': 'installed_manager', 'status': 'passed', 'category': 'execution',
                       'source_identity_sha256': '5' * 64, 'subjects': self.installation['subjects'], 'limits': ['synthetic fixture only'],
                       **self.installation['verify']}
        self.refresh()

    def refresh(self):
        self.record['installation'] = put(self.root, 'installed.json', self.installation)
        return self.record['installation']

    def check(self, record=None):
        record = record or self.record
        return stable.evidence(self.view, put(self.root, 'evidence.json', record), record['claim'], self.manifest, api)

    def test_actual_current_manager_source_store_and_output_pass(self):
        self.check()

    def test_explicit_local_native_cut_passes_only_with_exact_annotated_ref(self):
        acquisition = {'mode': 'local_prepublication', 'repository': str(self.root.absolute()),
            'ref': 'refs/tags/specification_methodology/v3.0.5', 'commit': self.native_manifest['release']['commit'],
            'manifest_sha256': self.manifest['native']['manifest']['sha256']}
        self.installation['acquisition'] = acquisition
        argv = self.installation['install']['execution']['argv']; argv[argv.index('--repository') + 1] = str(self.root.absolute())
        self.refresh()
        with patch.object(api, 'git', side_effect=[SimpleNamespace(stdout='tag\n'), SimpleNamespace(stdout=acquisition['commit']+'\n')]):
            self.check()
        self.installation['acquisition']['commit'] = '0' * 40; self.refresh()
        with self.assertRaisesRegex(ValueError, 'local install source/cut/native identity differs'): self.check()

    def test_local_unannotated_or_wrong_tag_cannot_qualify(self):
        self.installation['acquisition'] = {'mode': 'local_prepublication', 'repository': str(self.root.absolute()),
            'ref': 'refs/tags/specification_methodology/v3.0.5', 'commit': self.native_manifest['release']['commit'],
            'manifest_sha256': self.manifest['native']['manifest']['sha256']}
        argv = self.installation['install']['execution']['argv']; argv[argv.index('--repository') + 1] = str(self.root.absolute())
        self.refresh()
        with patch.object(api, 'git', return_value=SimpleNamespace(stdout='commit\n')):
            with self.assertRaisesRegex(ValueError, 'local installed native tag/commit differs'): self.check()

    def test_claims_reject_help_with_an_otherwise_complete_installed_context(self):
        record = copy.deepcopy(self.record); record['claim'] = 'installed_graphify'
        model = {'id': 'urn:current', 'profile': 'a_c.graphify.model/1'}
        model_ref = put(self.root, 'model.json', model)
        self.manifest['components']['representation']['facts'] = {'model': model_ref, 'model_sha256': model_ref['sha256'], 'model_canonical_sha256': api.canonical_value_sha256(model), 'carrier': model_ref}
        record.update(producer=put(self.root, 'tools/qualifier.py', b'pass\n'), observations=[{'pointer': '/status', 'equals': 'verified'}])
        record['execution']['argv'] = [str(self.python), 'tools/qualifier.py', '--help']
        with self.assertRaises((ValueError, KeyError)): self.check(record)

    def test_current_native_bytes_and_complete_product_population_are_required(self):
        self.installation['files'].pop('a_c/VERSION'); self.refresh()
        with self.assertRaisesRegex(ValueError, 'member closure'): self.check()

    def test_caller_cannot_supply_an_unverified_runtime_remapping(self):
        self.installation['runtime_files'] = {'a_c/VERSION': str(self.workspace / 'other/VERSION')}
        self.refresh()
        with self.assertRaisesRegex(ValueError, 'internal runtime mapping'): self.check()

    def test_stale_actual_install_result_is_not_repaired_by_current_wrapper_labels(self):
        result = json.loads((self.root / 'install.json').read_bytes()); result['manifest_sha256'] = '0' * 64; result['cut'] = 'v3.0.4'
        self.installation['install']['result'] = put(self.root, 'install.json', result)
        self.installation['install']['execution']['stdout'] = put(self.root, 'install.stdout', result); self.refresh()
        with self.assertRaisesRegex(ValueError, 'actual manager result'): self.check()

    def test_different_store_extra_native_file_and_symlink_each_refuse(self):
        original = copy.deepcopy(self.installation)
        self.installation['store'] = str(self.workspace / 'invented-store'); self.refresh()
        with self.assertRaisesRegex(ValueError, 'declared fresh store'): self.check()
        self.installation = original; self.refresh()
        (self.native / 'extra').write_bytes(b'not selected')
        with self.assertRaisesRegex(ValueError, 'population differs'): self.check()
        (self.native / 'extra').unlink()
        selected = Path(self.mapping['a_c/VERSION']); selected.unlink(); selected.symlink_to(self.workspace / 'products/axiom_indexer/VERSION')
        with self.assertRaisesRegex(ValueError, 'redirects'): self.check()

    def test_installed_runtime_version_cannot_be_faked_in_receipt(self):
        Path(self.mapping[self.manager_root + '/__init__.py']).write_text('__version__ = "3.0.4"\n')
        with self.assertRaisesRegex(ValueError, 'actual installed artifact differs'): self.check()

    def test_all_five_subjects_are_required_on_aggregate_through_evidence_consumer(self):
        record = copy.deepcopy(self.record); record.update(claim='complete_installed_cohort', category='installed_aggregate', component_evidence={})
        record['subjects'] = {'a_c': self.manifest['products']['a_c']['subject']['sha256']}
        with self.assertRaisesRegex(ValueError, 'required current Product subject'): self.check(record)
        record['subjects'] = self.installation['subjects']
        with self.assertRaisesRegex(ValueError, 'missing required current component'): self.check(record)


class NativeMCPResponseTests(unittest.TestCase):
    def setUp(self):
        self.raw = b'current anchor definition\n'; self.source = {'sha256': api.sha256(self.raw), 'root': 'product', 'path': 'stdo_runtime.json'}
        self.replies = [{'jsonrpc': '2.0', 'id': 1, 'result': {'protocolVersion': '2025-11-25', 'serverInfo': {'name': 'a_c.graphify.fd-support', 'version': '3.0.5'}}},
            {'jsonrpc': '2.0', 'id': 2, 'result': {'tools': [{'name': 'source.read'}]}},
            {'jsonrpc': '2.0', 'id': 3, 'result': {'isError': False, 'structuredContent': {'schema': 'a_c.fd-support.response/1', 'status': 'ok', 'id': 'readonly-product-001',
                'result': {'value': {'source': self.source, 'content': self.raw.decode(), 'encoding': 'utf8', 'parent_sha256': self.source['sha256'], 'selected_sha256': self.source['sha256'], 'size_bytes': len(self.raw)}},
                'operation_outcome': {'core_value': 'satisfied', 'value': 'returned', 'source_parent': {'clause': 'results', 'member': 'FOUNDATIONS.md', 'sha256': 'f' * 64}}}}}]

    def check(self, replies=None):
        replies = self.replies if replies is None else replies
        return owner_evidence.mcp_response(b'\n'.join(json.dumps(r).encode() for r in replies), '3.0.5', self.source, self.raw, 'f' * 64)

    def test_current_initialized_provider_and_exact_source_read(self):
        self.assertEqual(self.check(), self.replies)

    def test_old_server_help_missing_source_read_changed_anchor_and_old_method_refuse(self):
        changes = [lambda r:r[0]['result']['serverInfo'].update(version='0.1.0'), lambda r:r.pop(),
            lambda r:r[2]['result']['structuredContent']['result']['value'].update(content='other anchor'),
            lambda r:r[2]['result']['structuredContent']['operation_outcome']['source_parent'].update(sha256='0' * 64),
            lambda r:r[2]['result'].update(isError=True)]
        for change in changes:
            replies=copy.deepcopy(self.replies);change(replies)
            with self.assertRaises(ValueError):self.check(replies)


class OwnedVersionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup); self.root = Path(self.temp.name)
        self.view = api.View(self.root); self.value = manifest()
        for name in stable.PRODUCTS - {'specification_methodology'}:
            row = put(self.root, name + '/VERSION', b'3.0.5\n'); self.value['products'][name]['subject']['members'] = [row]
        self.lean = 'a_c/build_tenants/lean/lakefile.toml'; self.server = 'a_c/build_tenants/graphify/code/ac_support.py'
        for member, raw in ((self.lean, b'name = "ac_lean"\nversion = "3.0.5"\n'), (self.server, b'SERVER_VERSION = "3.0.5"\n')):
            self.value['products']['a_c']['subject']['members'].append(put(self.root, member, raw))

    def test_both_owned_package_versions_match(self):
        stable.owned_versions(self.view, self.value, api)

    def test_content_refuses_old_owned_metadata_despite_current_product_marker(self):
        for member, raw, message in ((self.lean, b'name = "ac_lean"\nversion = "0.1.0"\n', 'owned Lean package version'),
                                     (self.server, b'SERVER_VERSION = "0.1.0"\n', 'owned MCP server version')):
            original = (self.root / member).read_bytes(); put(self.root, member, raw)
            with patch.object(stable, 'source', return_value={}), patch.object(stable, 'subject'), self.assertRaisesRegex(ValueError, message):
                stable.content(self.view, self.value, api)
            (self.root / member).write_bytes(original)


class FormalEvidenceTests(EvidenceTests):
    def setUp(self):
        super().setUp()
        self.model = {'id': 'urn:test:model', 'profile': 'a_c.graphify.model/1'}
        model_ref = put(self.root, 'model.json', self.model); self.model_identity = {'id': self.model['id'], 'sha256': api.canonical_value_sha256(self.model)}
        self.manifest['components']['representation']['facts'] = {'model': model_ref, 'model_sha256': model_ref['sha256'], 'model_canonical_sha256': self.model_identity['sha256']}
        source = put(self.root, 'source.json', {'source': 'test'}); self.manifest['source'].update(source)
        request = {'schema': 'a_c.formal-gate.request/1', 'input': {'format': 'model', 'path': str(self.root / 'model.json'), 'raw_sha256': model_ref['sha256']},
                   'selections': [{'seeds': ['urn:test:seed'], 'budget_records': None}], 'supplied_views': {'path': 'views.json', 'raw_sha256': 'b' * 64}, 'context_binding': None}
        views_ref = put(self.root, 'views.json', [{'current': 'view'}])
        selections_ref = put(self.root, 'selections.json', request['selections'])
        request['supplied_views'] = {'path': str(self.root / 'views.json'), 'raw_sha256': views_ref['sha256']}
        request_ref = put(self.root, 'request.json', request)
        producer = put(self.root, 'a_c/build_tenants/lean/scripts/formal_gate.py', b'raise SystemExit(2)\n')
        self.result = {'schema': 'a_c.formal-gate.result/1', 'status': 'verified', 'model': self.model_identity,
                      'inputs': {'model': {'canonical_sha256': self.model_identity['sha256']}, 'input': {'raw_sha256': model_ref['sha256']}},
                      'requested_claims': ['imported-model-well-formedness', 'whole-model-source-correspondence', 'declared-closure-and-projection', 'record-budget-result', 'supplied-graphify-view-correspondence'],
                      'observations': {'current_dynamic_proof_invocations': 7, 'current_kernel_replay_invocations': 1, 'current_runtime_invocations': 1},
                      'runtime_identity': {'pins': {'lean': 'unknown-old-runtime'}}}
        self.result['checked_claims'] = self.result['requested_claims'].copy()
        self.bundle = {'schema': 'a_c.formal-gate.bundle/1', 'members': {'GateModel.olean': '0' * 64}}
        self.bundle_ref = put(self.root, 'bundle/manifest.json', self.bundle)
        self.result['evidence'] = {'manifest_sha256': self.bundle_ref['sha256'], 'members': self.bundle['members']}
        self.manifest['components']['lean']['facts'] = {'request': request_ref, 'bundle': 'bundle', 'bundle_manifest': self.bundle_ref, 'selections': selections_ref, 'supplied_views': views_ref}
        python = Path(sys.executable); physical = python.resolve()
        self.formal_record = self.record('exact_candidate_lean_result'); self.formal_record.update(category='execution', producer=producer,
             execution={'argv': [str(python), '-I', '-S', '-B', str(self.root / producer['path']), 'verify', '--request', str(self.root / 'request.json'), '--output', str(self.root / 'bundle')],
                        'cwd': str(self.root), 'returncode': 0, 'environment': {'python': {'invocation': str(python), 'executable_realpath': str(physical), 'sha256': api.sha256(physical.read_bytes()), 'version': '3.12'}},
                        'inputs': [model_ref, request_ref, views_ref], 'stderr': put(self.root, 'formal.stderr', b'')})

    def run_formal(self):
        ref = put(self.root, 'bundle/result.json', self.result); self.formal_record['result'] = ref
        self.formal_record['execution'].update(stdout=put(self.root, 'formal.stdout', self.result), outputs=[ref])
        if all((self.root / 'bundle' / name).is_file() for name in self.bundle['members']):
            helper = 'specification_methodology/v3/build_tenants/common-tools/proof_evidence.py'
            put(self.root, helper, (ROOT / helper).read_bytes())
            spec = importlib.util.spec_from_file_location('transport_control', self.root / helper)
            transport = importlib.util.module_from_spec(spec); spec.loader.exec_module(transport)
            transport.pack(self.root / 'bundle', self.root / 'proof.zip')
            transport.split(self.root / 'proof.zip', self.root / 'transport')
            self.manifest['components']['lean']['facts']['bundle_archive'] = put(self.root, 'transport/TRANSPORT.json', (self.root / 'transport/TRANSPORT.json').read_bytes())
        return self.check(self.formal_record)

    def test_arbitrary_equal_claims_refuse_after_fixed_command_and_current_model_checks(self):
        self.result['requested_claims'] = self.result['checked_claims'] = ['unrelated-trivial-claim']
        with self.assertRaisesRegex(ValueError, 'obligation coverage'): self.run_formal()

    def test_missing_proof_is_dereferenced_after_complete_required_population(self):
        modules = ['GateData', 'GateLocalNames', 'GateExternalNames', 'GateIdentities', 'GateBounds', 'GateModel', 'GateViews', 'GateRun']
        names = ['request.json', 'replay-request.json', 'input.json', 'model.json', 'supplied-views.json', 'certificates.json', 'view-comparison.json']
        names += [name + '.lean' for name in modules] + [name + '.olean' for name in modules[:-1]]
        self.bundle['members'] = {name: '0' * 64 for name in names}
        self.bundle_ref = put(self.root, 'bundle/manifest.json', self.bundle); self.manifest['components']['lean']['facts']['bundle_manifest'] = self.bundle_ref
        self.result['evidence'] = {'manifest_sha256': self.bundle_ref['sha256'], 'members': self.bundle['members']}
        with self.assertRaisesRegex(ValueError, 'regular contained file|complete Lean evidence archive'): self.run_formal()

    def test_unknown_runtime_refuses_even_with_all_declared_files_present(self):
        modules = ['GateData', 'GateLocalNames', 'GateExternalNames', 'GateIdentities', 'GateBounds', 'GateModel', 'GateViews', 'GateRun']
        names = ['request.json', 'replay-request.json', 'input.json', 'model.json', 'supplied-views.json', 'certificates.json', 'view-comparison.json']
        names += [name + '.lean' for name in modules] + [name + '.olean' for name in modules[:-1]]
        self.bundle['members'] = {name: put(self.root, 'bundle/' + name, b'present, but no proof')['sha256'] for name in names}
        self.bundle_ref = put(self.root, 'bundle/manifest.json', self.bundle)
        self.manifest['components']['lean']['facts']['bundle_manifest'] = self.bundle_ref
        self.result['evidence'] = {'manifest_sha256': self.bundle_ref['sha256'], 'members': self.bundle['members']}
        runtime = {'pins': {'lean': 'unknown-old-runtime'}}
        runtime['sha256'] = api.canonical_value_sha256(runtime['pins'])
        self.result['runtime_identity'] = runtime
        self.manifest['components']['lean']['facts']['runtime_identity'] = put(self.root, 'runtime.json', runtime)
        with self.assertRaisesRegex(ValueError, 'invalid SHA-256'):
            self.run_formal()

    def test_truthy_unknown_runtime_and_nonexistent_proof_never_pass(self):
        with self.assertRaisesRegex(ValueError, 'actual Lean proof artifacts'): self.run_formal()


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

    def test_same_version_RC_is_rejected_in_both_namespaces_even_if_preserved(self):
        for namespace in ('', 'a_c/'):
            ref = 'refs/tags/' + namespace + 'v3.0.5-rc.1'
            self.remote[ref] = '9' * 40; self.manifest['publication']['preserved_immutable_refs'][ref] = '9' * 40
            with self.assertRaisesRegex(ValueError, 'collides'):
                self.check()
            self.remote.pop(ref); self.manifest['publication']['preserved_immutable_refs'].pop(ref)

    def test_other_version_bare_RC_history_is_preserved_and_allowed(self):
        ref = 'refs/tags/v3.0.4-rc.1'
        self.remote[ref] = '9' * 40; self.manifest['publication']['preserved_immutable_refs'][ref] = '9' * 40
        self.check()

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
    refresh = InstalledEvidenceTests.refresh

    def setUp(self):
        InstalledEvidenceTests.setUp(self)
        base = 'https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology%2Fv3.0.5/'
        refs = [self.manifest['native']['manifest'], self.manifest['components']['manager']['facts']['wheel']]
        self.assets = [{**ref, 'name': Path(ref['path']).name, 'url': base + Path(ref['path']).name} for ref in refs]
        self.manifest['publication']['assets'] = self.assets
        self.external = self.manifest['publication']['external_manifest_asset']
        self.raw = api.canonical_json_bytes(self.manifest); put(self.root, 'frozen.json', self.raw)
        self.aggregate = copy.deepcopy(self.record)
        self.aggregate.update(claim='complete_installed_cohort', category='installed_aggregate', component_evidence={})
        self.receipt = {'kind': 'stdo.public-cohort-readback/1', 'status': 'verified',
            'source_identity_sha256': self.manifest['source']['source_identity_sha256'], 'unauthenticated': True, 'assets': self.assets,
            'fresh_store': str(self.store), 'installed_manifest_sha256': self.manifest['native']['manifest']['sha256'],
            'external_manifest': {**self.external, 'sha256': api.sha256(self.raw)},
            'installed_qualification': put(self.root, 'aggregate.json', self.aggregate)}

    def check(self, responses=None):
        if responses is None:
            responses = [(self.root / asset['path']).read_bytes() for asset in self.assets] + [self.raw]
        ref = put(self.root, 'readback.json', self.receipt)
        with patch.object(stable.urllib.request, 'urlopen', side_effect=[io.BytesIO(raw) for raw in responses]) as request:
            self.requests = request
            return stable.public(self.view, self.manifest, 'frozen.json', ref['path'], ref['sha256'], api)

    def test_anonymous_current_assets_do_not_substitute_for_all_component_results(self):
        with self.assertRaisesRegex(ValueError, 'missing required current component'):
            self.check()
        self.assertEqual(self.requests.call_count, 3)
        for call in self.requests.call_args_list:
            self.assertNotIn('Authorization', call.args[0].headers)
            self.assertNotIn('Cookie', call.args[0].headers)

    def test_missing_native_manifest_asset_refuses_before_download(self):
        self.manifest['publication']['assets'] = self.assets[1:]
        with self.assertRaisesRegex(ValueError, 'asset closure'): self.check([])
        self.assertEqual(self.requests.call_count, 0)

    def test_arbitrary_same_named_wheel_and_extra_asset_refuse(self):
        self.assets[1]['sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'required exact current artifact'): self.check([])
        self.assets[1]['sha256'] = self.manifest['components']['manager']['facts']['wheel']['sha256']
        self.assets.append({**self.assets[1], 'name': 'unselected.whl'})
        with self.assertRaisesRegex(ValueError, 'asset closure'): self.check([])

    def test_staged_file_does_not_excuse_wrong_public_bytes(self):
        with self.assertRaisesRegex(ValueError, 'fresh anonymous public asset differs'):
            self.check([b'wrong publicly downloaded bytes'])

    def test_actual_single_product_and_old_store_cannot_be_relabelled_fresh(self):
        self.aggregate['subjects'] = {'a_c': self.manifest['products']['a_c']['subject']['sha256']}
        self.receipt['installed_qualification'] = put(self.root, 'aggregate.json', self.aggregate)
        with self.assertRaisesRegex(ValueError, 'all Products'): self.check()
        self.aggregate['subjects'] = self.installation['subjects']
        self.receipt['installed_qualification'] = put(self.root, 'aggregate.json', self.aggregate)
        self.receipt['fresh_store'] = str(self.workspace / 'invented-fresh-store')
        with self.assertRaisesRegex(ValueError, 'declared fresh store'): self.check()

    def test_actual_zero_native_install_identity_cannot_be_relabelled_current(self):
        result = json.loads((self.root / 'install.json').read_bytes()); result['manifest_sha256'] = '0' * 64
        self.installation['install']['result'] = put(self.root, 'install.json', result)
        self.aggregate['installation'] = self.refresh()
        self.receipt['installed_qualification'] = put(self.root, 'aggregate.json', self.aggregate)
        with self.assertRaisesRegex(ValueError, 'actual result differs'): self.check()

    def test_external_manifest_does_not_contain_its_own_digest(self):
        self.assertNotIn('sha256', self.manifest['publication']['external_manifest_asset'])
        self.receipt['external_manifest']['sha256'] = 'c' * 64
        with self.assertRaisesRegex(ValueError, 'exact frozen B'): self.check([])

    def test_local_install_cannot_be_promoted_as_public_receipt(self):
        self.installation['acquisition']['mode'] = 'local_prepublication'
        self.aggregate['installation'] = self.refresh()
        self.receipt['installed_qualification'] = put(self.root, 'aggregate.json', self.aggregate)
        with self.assertRaisesRegex(ValueError, 'local prepublication acquisition cannot establish public'):
            self.check()


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

    def test_dedicated_configuration_does_not_depend_on_final_manifest(self):
        ref = self.value['native_preparation']['configuration']
        selected = json.loads((ROOT / ref['path']).read_bytes())
        actual = self.select(selected)
        self.assertEqual(set(actual), {'configuration_sha256', 'source', 'version'})
        self.assertEqual(actual['configuration_sha256'], ref['sha256'])
        selected['native_preparation']['manager_wheel'] = 'old.whl'
        with self.assertRaisesRegex(ValueError, 'manager component version differs'): self.select(selected)

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
