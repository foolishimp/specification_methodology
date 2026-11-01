import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import documentation as docs
import native_release as native

V3 = Path(__file__).resolve().parents[2]
PACKAGE = V3 / "build_tenants/common"


class DocumentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = {p.relative_to(PACKAGE).as_posix(): p.read_bytes()
                       for p in PACKAGE.rglob('*') if p.is_file()}

    def test_complete_current_payload_and_reviewed_source_identity(self):
        result = docs.check_payload(self.payload)
        self.assertEqual(result['viewer_sha256'], docs.VIEWER_SHA256)
        data = docs.viewer_data(self.payload[docs.DOC_ROOT + 'constraint-explorer/index.html'])
        self.assertEqual(data['basis']['subject']['id'], docs.SOURCE_ID)
        self.assertEqual(len(data['sources']), 58)

    def test_omission_and_extra_are_not_excused_by_refreshed_inventory(self):
        for removed in docs.MEMBERS:
            candidate = dict(self.payload)
            del candidate[docs.DOC_ROOT + removed]
            with self.subTest(removed=removed), self.assertRaises(ValueError):
                docs.check_payload(candidate)
        candidate = dict(self.payload)
        candidate[docs.DOC_ROOT + 'unexpected.txt'] = b'extra'
        with self.assertRaises(ValueError):
            docs.check_payload(candidate)

    def test_changed_viewer_and_source_metadata_refuse(self):
        candidate = dict(self.payload)
        candidate[docs.DOC_ROOT + 'constraint-explorer/index.html'] += b'changed'
        metadata = json.loads(candidate[docs.DOC_ROOT + 'DOCUMENTATION.json'])
        for row in metadata['members']:
            raw = candidate[docs.DOC_ROOT + row['path']]
            row.update(bytes=len(raw), sha256=docs.sha(raw))
        candidate[docs.DOC_ROOT + 'DOCUMENTATION.json'] = docs.encoded(metadata)
        with self.assertRaisesRegex(ValueError, 'selected documentation artifact'):
            docs.check_payload(candidate)
        candidate = dict(self.payload)
        metadata = json.loads(candidate[docs.DOC_ROOT + 'DOCUMENTATION.json'])
        metadata['source']['commit'] = '0' * 40
        candidate[docs.DOC_ROOT + 'DOCUMENTATION.json'] = docs.encoded(metadata)
        with self.assertRaisesRegex(ValueError, 'source identity'):
            docs.check_payload(candidate)

    def test_installed_entrypoints_are_required(self):
        for path in ('standards/README.md', 'plugins/spec/references/GETTING_STARTED.md'):
            candidate = dict(self.payload)
            candidate[path] = b'No documentation route\n'
            with self.subTest(path=path), self.assertRaises(ValueError):
                docs.check_payload(candidate)

    def test_navigation_requires_links_and_current_resolve_command(self):
        path = 'plugins/spec/references/GETTING_STARTED.md'
        original = self.payload[path]
        mutations = [
            original.replace(b'../../../standards/documentation/', b'../../standards/documentation/'),
            original.replace(b'stdo://releases/v3.0.3/standards/documentation/index.html',
                             b'stdo://releases/v3.0.2/standards/documentation/index.html'),
            b'documentation/index.html standards/documentation/index.html\n',
            b'```md\n' + original + b'\n```\n',
            b'<!-- unfinished comment\n' + original,
        ]
        destinations = [b'../../../standards/documentation/' + name.encode()
                        for name in ('index.html', 'README.md', 'constraint-explorer/index.html')]
        command = b'\nstdo resolve stdo://releases/v3.0.3/standards/documentation/index.html\n'
        mutations += [b'\n'.join(b'[unused]: ' + dest for dest in destinations) + command,
                      b'\n'.join(b'![image](' + dest + b')' for dest in destinations) + command]
        for index, content in enumerate(mutations):
            candidate = dict(self.payload)
            candidate[path] = content
            with self.subTest(mutation=index), self.assertRaises(ValueError):
                docs.check_payload(candidate)

    def test_metadata_format_discriminator_is_required(self):
        candidate = dict(self.payload)
        path = docs.DOC_ROOT + 'DOCUMENTATION.json'
        metadata = json.loads(candidate[path])
        metadata['kind'] = 'unrelated.kind'
        candidate[path] = docs.encoded(metadata)
        with self.assertRaisesRegex(ValueError, 'distribution contract'):
            docs.check_payload(candidate)

    def test_native_release_gate_cannot_omit_documentation(self):
        native.validate_payload([{'path': p} for p in self.payload], self.payload)
        incomplete = {p: b for p, b in self.payload.items() if not p.startswith(docs.DOC_ROOT)}
        with self.assertRaisesRegex(ValueError, 'member set'):
            native.validate_payload([{'path': p} for p in incomplete], incomplete)

    def test_native_assets_require_manifest_and_wheel_without_supplement(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            manifest = root / native.MANIFEST_NAME
            manifest.write_bytes(b'{"synthetic_manifest":true}\n')
            wheel = root / native.MANAGER_WHEEL
            wheel.write_bytes(b'fixture wheel; this checks asset selection only')
            selection = {"native": {"manifest_sha256": native.sha(manifest.read_bytes())}}
            for ordinal, files in enumerate(([manifest], [wheel], [manifest, wheel])):
                run = root / str(ordinal); run.mkdir()
                raw = native.canonical(selection)
                (run / 'SOURCE_SELECTION.json').write_bytes(raw)
                args = SimpleNamespace(run=run, selection_sha256=native.sha(raw), file=files)
                with patch.object(native, 'BASE', root):
                    if len(files) < 2:
                        with self.assertRaisesRegex(ValueError, 'manifest asset missing|manager wheel missing'):
                            native.assets(args)
                        self.assertFalse((run / 'assets.json').exists())
                        self.assertFalse((run / 'asset-checksums').exists())
                    else:
                        native.assets(args)
                        result = json.loads((run / 'assets.json').read_bytes())
                        self.assertEqual({row['name'] for row in result['files']},
                                         {manifest.name, wheel.name, manifest.name + '.sha256', wheel.name + '.sha256'})
            selected = {'commit': 'a'*40, 'package_path': 'candidate', 'package_tree': 'b'*40}
            self.assertIn(b'installed offline documentation', native.tag_message(selected))
            self.assertNotIn(b'representation is supplemental', native.tag_message(selected))

    def test_tools_work_without_work_records_and_missing_helper_refuses(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            tools = root / 'build_tenants/common-tools'; tools.mkdir(parents=True)
            for name in ('documentation.py', 'package_tools.py', 'native_release.py'):
                shutil.copyfile(Path(__file__).with_name(name), tools / name)
            package = root / 'build_tenants/common'
            shutil.copytree(PACKAGE, package)
            command = [sys.executable, '-I', '-B', str(tools / 'documentation.py'), 'check', str(package)]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)['status'], 'checked')
            self.assertFalse((root / '.ai-workspace').exists())
            # The registered native validator also acquires only sibling tools.
            script = ('import importlib.util,pathlib; '
                      f'p=pathlib.Path({str(tools / "native_release.py")!r}); '
                      's=importlib.util.spec_from_file_location("native",p); '
                      'm=importlib.util.module_from_spec(s);s.loader.exec_module(m); '
                      f'r=pathlib.Path({str(package)!r}); '
                      'd={p.relative_to(r).as_posix():p.read_bytes() for p in r.rglob("*") if p.is_file()}; '
                      'm.validate_payload([{"path":p} for p in d],d)')
            result = subprocess.run([sys.executable, '-I', '-B', '-c', script], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            (tools / 'package_tools.py').unlink()
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(json.loads(result.stderr)['status'], 'refused')
            self.assertIn('required package checker unavailable', json.loads(result.stderr)['reason'])
            self.assertNotIn('Traceback', result.stderr)

    def test_packaging_refuses_existing_output_and_import_overlap(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'viewer.html'
            source.write_bytes(self.payload[docs.DOC_ROOT + 'constraint-explorer/index.html'])
            before = source.read_bytes()
            with self.assertRaises(ValueError):
                docs.bundle(source, root)
            result = docs.bundle(source, root / 'fresh')
            self.assertEqual(result['members'], 4)
            self.assertEqual(source.read_bytes(), before)
            with self.assertRaises(ValueError):
                docs.bundle(source, root / 'fresh')


if __name__ == '__main__':
    unittest.main()
