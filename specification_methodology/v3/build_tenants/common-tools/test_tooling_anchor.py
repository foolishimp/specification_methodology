"""Use the real manager binding parser and optional installed host boundary."""
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import tooling_setup as setup

REPOSITORY = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPOSITORY / 'specification_methodology/v2/src'))
from stdo_toolchain.errors import StdoError
from stdo_toolchain.product_definition import load_binding


class AnchorBindingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='stdo-anchor-binding-')
        self.addCleanup(self.temporary.cleanup)
        self.path = Path(self.temporary.name).resolve() / 'stdo_runtime.json'

    def selected(self, version):
        value = setup.anchor_definition(version, 'a' * 64, 'https://example.test/repository.git')
        self.path.write_text(json.dumps(value))
        return value, load_binding(self.path)

    def test_stable_and_rc_channel_with_exact_basis_and_schema(self):
        for version in ('3.0.4', '3.0.5', '3.0.5-rc.1', '3.0.10-rc.12'):
            with self.subTest(version=version):
                value, observed = self.selected(version)
                self.assertEqual(observed.version_line, version.split('-rc.', 1)[0])
                self.assertEqual(observed.cut, 'v' + version)
                self.assertEqual(observed.basis_uri, 'stdo://releases/v' + version + '/')
                self.assertEqual(value['$schema'], observed.basis_uri + 'standards/schemas/product-definition.schema.json')

    def test_previous_rc_selector_is_refused_by_real_owner(self):
        value, _ = self.selected('3.0.5-rc.1')
        value['constitution']['stdo']['selector'] = 'stdo://channels/3.0.5-rc.1'
        self.path.write_text(json.dumps(value))
        with self.assertRaisesRegex(StdoError, 'Invalid STDO version line'):
            load_binding(self.path)

    def test_schema_cannot_silently_select_base_cut(self):
        value, _ = self.selected('3.0.5-rc.1')
        value['$schema'] = 'stdo://releases/v3.0.5/standards/schemas/product-definition.schema.json'
        self.path.write_text(json.dumps(value))
        with self.assertRaisesRegex(StdoError, 'differs from its basis'):
            load_binding(self.path)


@unittest.skipUnless(os.environ.get('STDO_TEST_ANCHOR_MANAGER'), 'explicit installed manager/store/manifest required')
class InstalledAnchorTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='stdo-installed-anchor-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.definition = self.root / 'stdo_runtime.json'
        self.manager = Path(os.environ['STDO_TEST_ANCHOR_MANAGER'])
        self.store = Path(os.environ['STDO_TEST_ANCHOR_STORE'])
        self.manifest = Path(os.environ['STDO_TEST_ANCHOR_MANIFEST'])
        import hashlib
        self.digest = hashlib.sha256(self.manifest.read_bytes()).hexdigest()
        self.value = setup.anchor_definition('3.0.5-rc.1', self.digest, 'https://github.com/foolishimp/specification_methodology.git')
        (self.root / 'README.md').write_text(setup.ANCHOR_GUIDE)
        (self.root / 'AGENTS.md').write_text('Read README.md.\n')
        (self.root / 'INSTALLATION.json').write_text('{}\n')
        for name in ('tickets/backlog', 'tickets/active', 'tickets/completed', 'comments'):
            (self.root / 'work' / name).mkdir(parents=True)
        self.definition.write_text(json.dumps(self.value))
        self.environment = dict(os.environ, STDO_STORE=str(self.store))

    def status(self):
        return subprocess.run([str(self.manager), '--store', str(self.store), 'status', '--definition', str(self.definition), '--verify'],
                              capture_output=True, text=True, timeout=60, env=self.environment)

    def test_actual_status_and_skills_verification_accept_correct_rc_anchor(self):
        result = self.status()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        observed = json.loads(result.stdout)
        self.assertTrue(observed['installed'] and observed['valid'])
        self.assertEqual(observed['failures'], [])
        self.assertEqual(observed['basis'], 'stdo://releases/v3.0.5-rc.1/')
        self.assertEqual(observed['manifest_sha256'], self.digest)
        code = ('import importlib.util,pathlib,sys;'
                'p=pathlib.Path(sys.argv[1]);s=importlib.util.spec_from_file_location("actual_skills",p);'
                'm=importlib.util.module_from_spec(s);s.loader.exec_module(m);'
                'm.verified_method(pathlib.Path(sys.argv[2]),pathlib.Path(sys.argv[3]),sys.argv[4]);print("verified")')
        result = subprocess.run([sys.executable, '-B', '-c', code, str(REPOSITORY / 'stdo_skills/scripts/manage_skills.py'),
                                 str(self.definition), str(self.manifest.parent), str(self.manager)],
                                capture_output=True, text=True, timeout=60, env=self.environment)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stdout.strip(), 'verified')

    def test_actual_status_rejects_old_suffix_selector(self):
        value = copy.deepcopy(self.value)
        value['constitution']['stdo']['selector'] = 'stdo://channels/3.0.5-rc.1'
        self.definition.write_text(json.dumps(value))
        result = self.status()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Invalid STDO version line', result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
