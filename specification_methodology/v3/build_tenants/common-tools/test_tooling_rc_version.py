"""Actual standalone materializer paths accept only exact selected versions."""
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

import tooling_materialize as tool


class ToolingVersionTests(unittest.TestCase):
    def bundle(self, root, version, owner_version=None):
        selected = {'kind': 'stdo.current-tooling-selection/1', 'version': version,
                    'source_identity_sha256': 'a' * 64, 'owners': {}}
        rows = []; archive = io.BytesIO()
        with zipfile.ZipFile(archive, 'w') as zipped:
            for owner in sorted(['a_c', 'stdo_skills', 'stdo_representation', 'axiom_indexer']):
                path = owner + '/VERSION'; raw = (version + '\n').encode()
                row = {'path': path, 'sha256': tool.sha(raw), 'bytes': len(raw), 'git_mode': '100644'}
                selected['owners'][owner] = {'version': owner_version or version, 'members': [row]}
                rows.append({'archive_path': path, **{key: value for key, value in row.items() if key != 'path'}})
                entry = zipfile.ZipInfo(path, (1980, 1, 1, 0, 0, 0)); entry.create_system = 3; entry.external_attr = 0o100644 << 16
                zipped.writestr(entry, raw, compress_type=zipfile.ZIP_DEFLATED)
        files = {name: b'' for name in ('README.md', 'materialize.py', 'setup.py', 'runtime.py', 'payload_boundary.py')}
        files.update({'SELECTION.json': tool.encoded(selected), 'sources.zip': archive.getvalue()})
        meta = {'kind': 'stdo.installed-tooling/2', 'distribution_version': version,
                'selection_sha256': tool.sha(files['SELECTION.json']), 'source_identity_sha256': 'a' * 64,
                'sources': rows, 'source_inventory_sha256': tool.sha(tool.encoded(rows)),
                'distribution_members': {name: {'bytes': len(raw), 'sha256': tool.sha(raw)} for name, raw in files.items()}}
        files['TOOLING.json'] = tool.encoded(meta); root.mkdir()
        for name, raw in files.items(): (root / name).write_bytes(raw)

    def invoke(self, root, *args):
        return subprocess.run([sys.executable, '-B', tool.__file__, '--bundle', str(root), *args], capture_output=True)

    def test_stable_and_rc_public_check_materialize_and_verify(self):
        for version in ('3.0.5', '3.0.5-rc.1'):
            with self.subTest(version=version), tempfile.TemporaryDirectory() as temporary:
                base = Path(temporary).resolve(); bundle = base / 'bundle'; self.bundle(bundle, version)
                checked = self.invoke(bundle, 'check'); self.assertEqual(checked.returncode, 0, checked.stderr)
                self.assertEqual(json.loads(checked.stdout)['version'], version)
                materialized = self.invoke(bundle, 'materialize', '--destination', str(base / 'tools'))
                self.assertEqual(materialized.returncode, 0, materialized.stderr)
                verified = self.invoke(bundle, 'verify-tree', '--destination', str(base / 'tools'))
                self.assertEqual(verified.returncode, 0, verified.stderr)

    def test_malformed_and_mixed_versions_refuse_without_output(self):
        for version, owner in [('v3.0.5-rc.1', None), ('3.0.5rc1', None), ('3.0.5-rc.0', None),
                               ('3.0.5-rc.01', None), ('03.0.5', None), ('3.0.5-rc.1', '3.0.5')]:
            with self.subTest(version=version, owner=owner), tempfile.TemporaryDirectory() as temporary:
                base = Path(temporary).resolve(); bundle = base / 'bundle'; self.bundle(bundle, version, owner)
                result = self.invoke(bundle, 'materialize', '--destination', str(base / 'tools'))
                self.assertEqual(result.returncode, 2); self.assertEqual(json.loads(result.stderr)['status'], 'refused')
                self.assertFalse((base / 'tools').exists())


if __name__ == '__main__': unittest.main()
