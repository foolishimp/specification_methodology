"""RC five-Product controls; fixture bytes are not release evidence."""
from __future__ import annotations

import copy
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_stable_stack_release as legacy
from test_stable_stack_release import ROOT, api, manifest, put, stable


def rc_manifest():
    value = manifest()
    value['profile'] = stable.RC_PROFILE
    value['cohort'].update(version='3.0.5-rc.1', cut='v3.0.5-rc.1', version_line='3.0.5')
    for name, product in value['products'].items():
        product.update(version='3.0.5-rc.1', release_ref=f'refs/tags/{name}/v3.0.5-rc.1',
                       selector_ref=f'refs/tags/{name}/v3.0.5', release_branch=None)
    for component in value['components'].values():
        component['version'] = '3.0.5-rc.1'
    value['components']['manager']['facts']['python_distribution_version'] = '3.0.5rc1'
    value['publication']['expected_version_lines'] = {name: [] for name in stable.PRODUCTS}
    return value


class RCShapeTests(unittest.TestCase):
    def test_exact_rc_versions_and_explicit_python_normalization(self):
        value = rc_manifest(); stable.check_shape(value)
        self.assertEqual(stable.manager_version(value), '3.0.5rc1')
        stable.check_shape(manifest())

    def test_mixed_version_line_cut_profile_selector_and_python_mapping_refuse(self):
        for change in (
            lambda v: v['cohort'].update(version_line='3.0.4'),
            lambda v: v['cohort'].update(cut='v3.0.5'),
            lambda v: v.update(profile=stable.PROFILE),
            lambda v: v['products']['a_c'].update(version='3.0.5'),
            lambda v: v['products']['stdo_skills'].update(selector_ref='refs/tags/stdo_skills/v3.0.4'),
            lambda v: v['components']['manager']['facts'].update(python_distribution_version='3.0.5'),
            lambda v: v['components']['manager']['facts'].pop('python_distribution_version'),
        ):
            with self.subTest(change=change):
                value = rc_manifest(); change(value)
                with self.assertRaises((ValueError, KeyError)): stable.check_shape(value)

    def test_noncanonical_rc_versions_refuse(self):
        for version in ('3.0.5-rc.0', '3.0.5-rc.01', '3.0.5rc1', 'v3.0.5-rc.1'):
            value = rc_manifest(); value['cohort'].update(version=version, cut='v'+version)
            with self.assertRaises(ValueError): stable.check_shape(value)

    def test_exact_reset_custody_and_other_lines_cannot_use_exception(self):
        value = rc_manifest()
        name = 'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET/release-tools/RESET_CONTRACT.json'
        raw = (ROOT/name).read_bytes()
        value['publication']['reset'] = {'path': name, 'sha256': api.sha256(raw)}
        reset = stable.reset_record(api.View(ROOT), value, api)
        self.assertEqual(set(reset['archives'].values()), set(stable.RESET_305_TAGS.values()))
        value['cohort'].update(cut='v3.0.6-rc.1')
        with self.assertRaisesRegex(ValueError, 'limited'): stable.reset_record(api.View(ROOT), value, api)
        value = manifest(); value['publication']['reset'] = {'path': name, 'sha256': api.sha256(raw)}
        with self.assertRaisesRegex(ValueError, 'not a stable'): stable.check_shape(value)


class RCPublicationTests(unittest.TestCase):
    def setUp(self):
        legacy.PublicationTests.setUp(self)
        self.manifest = rc_manifest()
        self.manifest['native'] = {'manifest': put(self.root, 'native.json', {'release': {'commit': self.native}})}
        self.tags = {}; self.local = {'refs/heads/main': self.carrier}
        expected = {'refs/heads/main': 'c'*40}
        for index, (name, product) in enumerate(sorted(self.manifest['products'].items())):
            target = self.native if name == 'specification_methodology' else self.carrier
            for field, offset in [('release_ref', 1), ('selector_ref', 6)]:
                ref = product[field]; oid = f'{index+offset:040x}'
                self.tags[ref] = (oid, target); expected[ref] = None
        self.manifest['publication']['expected_remote'] = expected
        self.manifest['publication']['preserved_immutable_refs'] = self.previous.copy()
        old_git = self.adapter.git
        def git(root, *args, **kwargs):
            if args[0] == 'cat-file':
                return SimpleNamespace(stdout='tag '+args[-1].removeprefix('refs/tags/')+'\n\nRC selector\n')
            return old_git(root, *args, **kwargs)
        self.adapter.git = git; self.adapter.rc_ref_ordinal = api.rc_ref_ordinal

    def check(self, phase='refs'):
        return stable.ref_graph(self.root, self.manifest, self.carrier, phase, 'origin', self.adapter)

    def test_new_line_emits_one_eleven_ref_atomic_vector(self):
        argv = self.check()['push_argv']
        self.assertEqual(argv[:3], ['git', 'push', '--atomic'])
        self.assertEqual(sum(x.startswith('--force-with-lease=') for x in argv), 11)

    def test_existing_stable_selector_requires_bounded_exception(self):
        ref = self.manifest['products']['a_c']['selector_ref']
        self.manifest['publication']['expected_remote'][ref] = stable.RESET_305_TAGS['a_c']
        self.remote[ref] = stable.RESET_305_TAGS['a_c']
        with self.assertRaisesRegex(ValueError, 'bounded reset'): self.check()

    def reset(self):
        archives = {f'refs/tags/archive/stdo305-stable-reset-20261107/{n}/v3.0.5': oid for n, oid in stable.RESET_305_TAGS.items()}
        selectors = {f'refs/tags/{n}/v3.0.5': oid for n, oid in stable.RESET_305_TAGS.items()}
        for ref, oid in archives.items(): self.local[ref] = oid; self.manifest['publication']['expected_remote'][ref] = None
        for ref, oid in selectors.items(): self.remote[ref] = oid; self.manifest['publication']['expected_remote'][ref] = oid
        return patch.object(stable, 'reset_record', return_value={'archives': archives, 'former_selectors': selectors})

    def test_reset_exact_sixteen_refs_include_original_archive_objects(self):
        with self.reset():
            argv = self.check()['push_argv']
            self.assertEqual(sum(x.startswith('--force-with-lease=') for x in argv), 16)
            for name, oid in stable.RESET_305_TAGS.items():
                self.assertIn(oid+f':refs/tags/archive/stdo305-stable-reset-20261107/{name}/v3.0.5', argv)
                self.assertIn(f'--force-with-lease=refs/tags/{name}/v3.0.5:'+oid, argv)

    def test_wrong_archive_selector_lease_and_existing_rc_refuse(self):
        with self.reset():
            archive = next(k for k in self.local if '/archive/' in k)
            old = self.local[archive]; self.local[archive] = 'f'*40
            with self.assertRaisesRegex(ValueError, 'archive'): self.check()
            self.local[archive] = old
            selector = 'refs/tags/a_c/v3.0.5'; self.manifest['publication']['expected_remote'][selector] = 'f'*40
            with self.assertRaisesRegex(ValueError, 'exact former'): self.check()
            self.manifest['publication']['expected_remote'][selector] = stable.RESET_305_TAGS['a_c']
            ref = 'refs/tags/a_c/v3.0.5-rc.1'; self.remote[ref] = 'f'*40
            with self.assertRaisesRegex(ValueError, 'version-line'): self.check()

    def test_published_exact_selectors_and_archives_required(self):
        with self.reset():
            self.remote.update(self.local)
            for ref, (oid, target) in self.tags.items(): self.remote.update({ref: oid, ref+'^{}': target})
            self.check('published')
            self.remote['refs/tags/a_c/v3.0.5^{}'] = 'f'*40
            with self.assertRaisesRegex(ValueError, 'selector'): self.check('published')

    def test_generic_successor_rc_preserves_preceding_cut_and_requires_highest_selector(self):
        for product in self.manifest['products'].values():
            old = product['release_ref']; new = old.replace('-rc.1', '-rc.2')
            tag, target = self.tags.pop(old); self.tags[new] = (tag, target); product['release_ref'] = new
            self.manifest['publication']['expected_remote'].pop(old); self.manifest['publication']['expected_remote'][new] = None
            row = {'ordinal': 1, 'ref': old, 'tag_object': 'd'*40, 'peeled_commit': 'e'*40}
            self.manifest['publication']['expected_version_lines'][product['namespace']] = [row]
            self.remote.update({old: row['tag_object'], old+'^{}': row['peeled_commit'], product['selector_ref']: 'f'*40, product['selector_ref']+'^{}': 'e'*40})
            self.manifest['publication']['preserved_immutable_refs'].update({old:'d'*40, old+'^{}':'e'*40})
            self.manifest['publication']['expected_remote'][product['selector_ref']] = 'f'*40
        self.manifest['cohort'].update(version='3.0.5-rc.2', cut='v3.0.5-rc.2')
        self.check()
        prior_git = self.adapter.git
        def stable_selector(root, *args, **kwargs):
            if args == ('cat-file', '-p', 'f'*40):
                return SimpleNamespace(stdout='tag a_c/v3.0.5\n\nSTDO-Release-Profile: stable-v1\n')
            return prior_git(root, *args, **kwargs)
        self.adapter.git = stable_selector
        with self.assertRaisesRegex(ValueError, 'stable-profile selector'): self.check()
        self.adapter.git = prior_git
        self.remote['refs/tags/a_c/v3.0.5^{}'] = 'a'*40
        with self.assertRaisesRegex(ValueError, 'greatest preceding'): self.check()

    def test_same_ordinal_historical_aliases_must_have_identical_tag_objects(self):
        value=rc_manifest(); value['cohort'].update(version='3.0.5-rc.2',cut='v3.0.5-rc.2')
        rows=[{'ordinal':1,'ref':ref,'tag_object':oid,'peeled_commit':'e'*40} for ref,oid in
              [('refs/tags/specification_methodology/v3.0.5-rc.1','d'*40),('refs/tags/v3.0.5-rc.1','c'*40)]]
        rows.sort(key=lambda r:(r['ordinal'],r['ref']))
        value['publication']['expected_version_lines']['specification_methodology']=rows
        observed={row['ref']:row['tag_object'] for row in rows}
        observed.update({row['ref']+'^{}':row['peeled_commit'] for row in rows})
        with self.assertRaisesRegex(ValueError,'conflicting identities'):
            stable.rc_version_lines(value,observed,{}, {p['selector_ref']:None for p in value['products'].values()},'refs',None,api)


class RCNativeTests(unittest.TestCase):
    def test_onboarding_keeps_canonical_native_dependencies(self):
        guide=(ROOT/'specification_methodology/v3/build_tenants/common/plugins/spec/references/GETTING_STARTED.md').read_text()
        self.assertNotIn('cp -R "$STDO_PLUGIN_ROOT"',guide)
        self.assertNotIn('codex plugin marketplace add',guide)
        self.assertIn('Its wrappers resolve the verified canonical native files',guide)
        self.assertIn('`$stdo-work`',guide)
        self.assertIn('claude --plugin-dir "$STDO_PLUGIN_ROOT"',guide)

    def test_published_recipe_checks_exact_five_assets_before_install(self):
        guide=(ROOT/'specification_methodology/v3/build_tenants/common/plugins/spec/references/GETTING_STARTED.md').read_text()
        script=guide.split("<<'PYVERIFY'\n",1)[1].split('\nPYVERIFY',1)[0]
        self.assertNotIn('$asset.sha256',guide)
        names=['stdo_toolchain-3.0.5rc1-py3-none-any.whl','stdo-v3.0.5-rc.1-manifest.json',
               'stdo-manager-runtime-v3.0.5-rc.1-macos-arm64-cp313.zip',
               'stdo-manager-constraints-v3.0.5-rc.1-python313.txt','stack-release-v3.0.5-rc.1.json']
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); assets=[]
            for name in names:
                raw=name.encode(); (root/name).write_bytes(raw)
                assets.append({'name':name,'size':len(raw),'digest':'sha256:'+api.sha256(raw)})
            release={'tag_name':'specification_methodology/v3.0.5-rc.1','draft':False,'prerelease':False,'assets':assets}
            def run(value):
                (root/'release.json').write_text(json.dumps(value))
                return subprocess.run([sys.executable,'-B','-c',script,str(root)],capture_output=True).returncode
            self.assertEqual(run(release),0)
            for mutate in [lambda v:v.update(tag_name='specification_methodology/v3.0.5'),
                           lambda v:v.update(prerelease=True),lambda v:v.update(draft=True),
                           lambda v:v['assets'].pop(),lambda v:v['assets'].append(v['assets'][0]),
                           lambda v:v['assets'][0].update(digest='sha256:'+'0'*64),
                           lambda v:v['assets'][0].update(size=1),lambda v:v['assets'][0].pop('digest')]:
                current=copy.deepcopy(release);mutate(current);self.assertNotEqual(run(current),0)

    def test_native_configuration_annotation_and_manager_spelling(self):
        p = ROOT/'specification_methodology/v3/build_tenants/common-tools/native_release.py'
        spec = importlib.util.spec_from_file_location('rc_native_control', p)
        native = importlib.util.module_from_spec(spec); spec.loader.exec_module(native)
        with tempfile.TemporaryDirectory() as tmp:
            value = {'kind':'stdo.native-preparation-config/1','version':'3.0.5-rc.1','cut':'v3.0.5-rc.1','source':{},
                     'repository_url':'https://github.com/foolishimp/specification_methodology.git',
                     'native_preparation':{'output_root':'specification_methodology/v3/.ai-workspace/work/RC_FIXTURE',
                       'package_path':'specification_methodology/v3','predecessor_native_commit':'a'*40,
                       'manager_wheel':'stdo_toolchain-3.0.5rc1-py3-none-any.whl','scope':'isolated test'}}
            ref=put(Path(tmp),'config.json',value); native.configure(Path(tmp)/'config.json',ref['sha256'])
            message = native.tag_message({'commit':'b'*40,'package_path':'test','package_tree':'c'*40})
            self.assertIn(b'v3.0.5-rc.1',message); self.assertNotIn(b'STDO-Release-Profile:',message)
            self.assertIsNone(native.PROFILE)
            value['native_preparation']['manager_wheel']='stdo_toolchain-3.0.5-rc.1-py3-none-any.whl'
            ref=put(Path(tmp),'config.json',value)
            with self.assertRaisesRegex(ValueError,'PEP 440'):native.configure(Path(tmp)/'config.json',ref['sha256'])

    def test_manager_wheel_explicit_normalization_and_source_equality(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); value=rc_manifest(); source='manager/stdo_toolchain'
            put(root,source+'/__init__.py',b'__version__ = "3.0.5rc1"\n')
            stream=io.BytesIO()
            with zipfile.ZipFile(stream,'w') as z:
                z.writestr('stdo_toolchain/__init__.py',(root/source/'__init__.py').read_bytes())
                z.writestr('stdo_toolchain-3.0.5rc1.dist-info/METADATA','Name: stdo-toolchain\nVersion: 3.0.5rc1\n')
            value['components']['manager']['facts'].update(source_root=source,wheel=put(root,'assets/stdo_toolchain-3.0.5rc1-py3-none-any.whl',stream.getvalue()))
            stable.manager(api.View(root),value,api)
            value['components']['manager']['facts']['python_distribution_version']='3.0.5'
            with self.assertRaisesRegex(ValueError,'mapping'):stable.manager(api.View(root),value,api)


if __name__ == '__main__':
    unittest.main()
