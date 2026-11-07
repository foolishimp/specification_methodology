"""Deterministic installation controls; synthetic manager is not host qualification."""
from pathlib import Path
import argparse
import importlib.util
import json
import os
import subprocess
import venv
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
spec = importlib.util.spec_from_file_location('install305', ROOT / 'scripts/manage_skills.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)


class Install305Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve(); self.workspace = self.root / 'workspace'; self.workspace.mkdir()
        self.method = self.root / 'method'; native = self.method / 'plugins/spec'; native.mkdir(parents=True)
        source = REPO / 'specification_methodology/v3/build_tenants/common/plugins/spec'
        for name, raw in m.tree(source).items():
            path = native / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(raw)
        files = m.tree(native)
        manifest = {'release': {'cut': 'v3.0.5'}, 'auxiliary': {'plugin': {'installed_root': 'plugins/spec', 'member_count': len(files), 'members': [{'path': k, 'sha256': m.sha(v)} for k, v in files.items()]}}}
        (self.method / 'manifest.json').write_bytes(m.encode(manifest)); digest = m.sha((self.method / 'manifest.json').read_bytes())
        self.definition = self.workspace / 'Product.json'
        self.definition.write_bytes(m.encode({'constitution': {'stdo': {'basis': {'uri': 'stdo://releases/v3.0.5/', 'manifest_sha256': digest}}}}))
        self.manager = self.root / 'manager'
        status = {'basis': 'stdo://releases/v3.0.5/', 'manifest_sha256': digest, 'installed': True, 'valid': True, 'failures': [], 'path': str(self.method), 'definition': str(self.definition)}
        self.manager.write_text('#!/usr/bin/env python3\nprint(' + repr(json.dumps(status)) + ')\n'); self.manager.chmod(0o755)
        self.ac = self.root / 'ac'; self.ac.mkdir(); (self.ac / 'VERSION').write_text('3.0.5\n')
        for name in ['build_tenants/graphify/design/fd-method-stdo-3.0.5.json', 'build_tenants/lean/toolchain-lock.json', 'build_tenants/lean/lake-manifest.json']:
            p = self.ac / name; p.parent.mkdir(parents=True, exist_ok=True); p.write_text('{}\n')
        self.args = argparse.Namespace(command='install', package=ROOT, workspace=self.workspace, host='codex', definition=self.definition, method_root=self.method, ac_root=self.ac, stdo=str(self.manager), python=m.sys.executable)

    def selected_store_launcher(self):
        status = json.loads(subprocess.check_output([str(self.manager)], text=True))
        store = self.root / 'selected store'; target = store / 'releases/v3.0.5'
        target.parent.mkdir(parents=True); self.method.rename(target); self.method = target
        self.args.method_root = target; status['path'] = str(target)
        self.manager.write_text('#!/usr/bin/env python3\nimport sys\nassert sys.argv[1:3] == ' + repr(['--store', str(store)]) + '\nprint(' + repr(json.dumps(status)) + ')\n')
        owner = REPO / 'specification_methodology/v3/build_tenants/common-tools/tooling_setup.py'
        spec = importlib.util.spec_from_file_location('tooling_setup_test', owner)
        setup = importlib.util.module_from_spec(spec); spec.loader.exec_module(setup)
        contract = {'manager': str(self.manager), 'manager_sha256': m.sha(self.manager.read_bytes()),
                    'store': str(store), 'manifest': str(target / 'manifest.json'), 'manifest_sha256': status['manifest_sha256']}
        launcher = self.root / 'anchor/stdo'; launcher.parent.mkdir()
        launcher.write_bytes(setup.launcher_source(contract)); launcher.chmod(0o755)
        self.args.stdo = str(launcher)
        return launcher, contract

    def check_runtime(self, bundle, environment=None):
        result = subprocess.run([m.sys.executable, str(bundle / 'manage_skills.py'), 'check-runtime', '--configuration', str(bundle / 'CONFIG.json')], capture_output=True, text=True, env=environment)
        return result, json.loads(result.stdout)

    def test_install_verify_links_and_remove_preserves_unrelated(self):
        other = self.workspace / '.agents/skills/unrelated/SKILL.md'; other.parent.mkdir(parents=True); other.write_text('unrelated')
        installed = m.install(self.args)
        base, receipt, value = m.current(self.workspace, 'codex', installed['receipt_sha256'])
        for path in ['skills/stdo-work/SKILL.md', 'stdo-3.0.5/native/references/COORDINATED_HANDOFF.md', 'skills/stdo-project/references/formal.md']:
            self.assertTrue((base / path).is_file())
        self.assertFalse((self.workspace / '.claude').exists())
        config = json.loads((base / 'stdo-3.0.5/CONFIG.json').read_text())
        self.assertEqual(config['method_selection_scope'], 'runtime-installation-anchor-only')
        for directory in value['roots']:
            shutil.rmtree(base / directory)
        receipt.unlink(); self.assertEqual(other.read_text(), 'unrelated')

    def test_both_hosts_independently_install(self):
        self.args.host = 'claude'; installed = m.install(self.args)
        m.current(self.workspace, 'claude', installed['receipt_sha256'])
        self.assertTrue((self.workspace / '.claude/skills/stdo-refresh/SKILL.md').is_file())
        self.assertFalse((self.workspace / '.agents').exists())

    def test_plan_has_no_effect(self):
        self.args.command = 'plan'; self.assertEqual(m.install(self.args)['status'], 'planned')
        self.assertFalse((self.workspace / '.agents').exists())

    def test_collision_refuses_before_writing(self):
        path = self.workspace / '.agents/skills/stdo-work'; path.mkdir(parents=True)
        with self.assertRaises(ValueError): m.install(self.args)
        self.assertFalse((self.workspace / '.agents/stdo-3.0.5').exists())

    def test_changed_owned_file_and_receipt_refuse(self):
        installed = m.install(self.args)
        with self.assertRaises(ValueError): m.current(self.workspace, 'codex', '0' * 64)
        (self.workspace / '.agents/skills/stdo-project/SKILL.md').write_text('changed')
        with self.assertRaises(ValueError): m.current(self.workspace, 'codex', installed['receipt_sha256'])

    def test_extra_empty_directory_refuses(self):
        installed = m.install(self.args)
        (self.workspace / '.agents/skills/stdo-project/extra').mkdir()
        with self.assertRaises(ValueError): m.current(self.workspace, 'codex', installed['receipt_sha256'])

    def test_altered_native_member_and_wrong_cut_refuse(self):
        (self.method / 'plugins/spec/skills/stdo-work/SKILL.md').write_text('changed')
        with self.assertRaises(ValueError): m.install(self.args)
        d = json.loads(self.definition.read_text()); d['constitution']['stdo']['basis']['uri'] = 'stdo://releases/v3.0.4/'
        self.definition.write_bytes(m.encode(d))
        with self.assertRaises(ValueError): m.install(self.args)

    def test_selected_venv_survives_both_installed_host_routes(self):
        selected = os.environ.get('STDO305_TEST_PYTHON')
        if selected is None:
            environment = self.root / 'private-venv'
            subprocess.run([m.sys.executable, '-m', 'venv', '--without-pip', str(environment)], check=True)
            self.assertTrue((environment / 'bin/python').is_symlink(), 'POSIX venv regression requires symlink invocation')
            selected = str(environment / 'bin/python')
            site = subprocess.check_output([selected, '-c', 'import sysconfig; print(sysconfig.get_path("purelib"))'], text=True).strip()
            (Path(site) / '_stdo305_probe.py').write_text('VALUE = "private-venv"\n')
            probe = 'import _stdo305_probe,sys; print(_stdo305_probe.VALUE); print(sys.prefix)'
        else:
            probe = 'import networkx,sys; print(networkx.__version__); print(sys.prefix)'
        expected = subprocess.check_output([selected, '-c', probe], text=True)
        for host in ('codex', 'claude'):
            self.args.host = host; self.args.python = selected
            m.install(self.args)
            base, bundle, _ = m.paths(self.workspace, host)
            result = subprocess.run([m.sys.executable, str(bundle / 'manage_skills.py'), 'check-runtime', '--configuration', str(bundle / 'CONFIG.json')], capture_output=True, text=True, check=True)
            configuration = json.loads(result.stdout)['configuration']
            actual = subprocess.run([configuration['python'], '-c', probe], capture_output=True, text=True)
            self.assertEqual(actual.returncode, 0, actual.stderr)
            self.assertEqual(actual.stdout, expected)
            self.assertEqual(configuration['python'], str(Path(selected).absolute()))

    def test_both_host_routes_preserve_explicit_store_without_ambient_environment(self):
        launcher, contract = self.selected_store_launcher()
        for host in ('codex', 'claude'):
            self.args.host = host; m.install(self.args)
            _, bundle, _ = m.paths(self.workspace, host)
            for ambient in (None, str(self.root / 'wrong-store')):
                environment = dict(os.environ); environment.pop('STDO_STORE', None)
                if ambient is not None: environment['STDO_STORE'] = ambient
                result, body = self.check_runtime(bundle, environment)
                self.assertEqual(result.returncode, 0, body)
                identity = body['configuration']['manager_identity']
                self.assertEqual(identity['invocation'], str(launcher))
                self.assertEqual(identity['runtime_launcher'], {'path': str(launcher), 'sha256': m.sha(launcher.read_bytes()), **contract})
                direct = subprocess.run([body['configuration']['stdo'], 'status', '--definition', str(self.definition), '--verify'], capture_output=True, text=True, env=environment)
                self.assertEqual(direct.returncode, 0, direct.stdout)
                self.assertEqual(json.loads(direct.stdout)['runtime_launcher'], identity['runtime_launcher'])
        override = subprocess.run([str(launcher), '--store', str(self.root / 'wrong-store'), 'status'], capture_output=True, text=True)
        self.assertEqual(override.returncode, 2)
        self.assertIn('store is fixed', override.stdout)

    def test_changed_launcher_manager_and_store_manifest_refuse_before_invocation(self):
        launcher, contract = self.selected_store_launcher(); m.install(self.args)
        _, bundle, _ = m.paths(self.workspace, 'codex')
        for target in (launcher, self.manager, self.method / 'manifest.json'):
            original = target.read_bytes()
            try:
                target.write_bytes(original + b'\n# changed selected input\n')
                result, body = self.check_runtime(bundle)
                self.assertEqual(result.returncode, 2, body)
            finally: target.write_bytes(original)
        config = bundle / 'CONFIG.json'; value = json.loads(config.read_text())
        value['manager_identity']['runtime_launcher']['store'] = str(self.root)
        config.write_bytes(m.encode(value))
        result, body = self.check_runtime(bundle)
        self.assertEqual(result.returncode, 2, body)
        self.assertIn('does not belong to its store', body['error'])

    def test_old_basis_refusal_never_adopts_or_rewrites_product(self):
        value = json.loads(self.definition.read_text())
        value['constitution']['stdo']['basis'] = {'uri': 'stdo://releases/v3.0.4/', 'manifest_sha256': 'a' * 64}
        self.definition.write_bytes(m.encode(value)); original = self.definition.read_bytes()
        with self.assertRaisesRegex(ValueError, 'exact selected 3.0.5'):
            m.install(self.args)
        self.assertEqual(self.definition.read_bytes(), original)
        self.assertFalse((self.workspace / '.agents').exists())

    def test_different_method_root_is_not_manager_verified(self):
        copy = self.root / 'copy'; shutil.copytree(self.method, copy); self.args.method_root = copy
        with self.assertRaises(ValueError): m.install(self.args)

if __name__ == '__main__': unittest.main()
