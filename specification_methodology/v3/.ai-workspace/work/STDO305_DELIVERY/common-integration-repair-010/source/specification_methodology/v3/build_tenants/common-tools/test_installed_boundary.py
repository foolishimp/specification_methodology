"""Public installed-output regressions; synthetic payloads assert no Lean result.

Set STDO_BOUNDARY_EVIDENCE_ROOT to an absent directory to retain full fixtures,
argv/stdout/stderr and native pre/post inventories. STDO_BOUNDARY_SOURCE_DIR can
select an exact predecessor snapshot for the same falsification tests. No
production module is imported and no bootstrap dependency is acquired.
"""
from __future__ import annotations

import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
import zipfile

HERE = Path(__file__).resolve().parent
PROFILE = 'build_tenants/lean/profiles/proof-support-v1.json'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()


def write(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)


def archive(files):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w') as target:
        for name, raw in sorted(files.items()):
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            target.writestr(info, raw, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return stream.getvalue()


def tree(root):
    """Include directories, modes, mtimes and bytes; omit read-only atime changes."""
    rows = {}
    for path in [root, *sorted(root.rglob('*'))]:
        observed = path.lstat()
        row = {'mode': stat.S_IMODE(observed.st_mode), 'mtime_ns': observed.st_mtime_ns}
        if path.is_symlink():
            row.update(kind='symlink', target=os.readlink(path))
        elif path.is_dir():
            row.update(kind='directory')
        else:
            row.update(kind='file', bytes=observed.st_size, sha256=sha(path.read_bytes()))
        rows[path.relative_to(root).as_posix()] = row
    return rows


class PayloadFixture:
    """Explicit public payload formats; bootstrap is a marker-only failing stub."""
    def __init__(self, root, source):
        self.root, self.source = root, source
        root.mkdir(parents=True)
        self.native = root / 'native'
        self.proofs = self.native / 'standards/documentation/proofs'
        self.tooling = self.native / 'standards/tooling'
        self.standalone = root / 'standalone'
        self.marker = root / 'bootstrap-invoked.marker'
        self.raw = root / 'inputs/raw'
        self.zip = root / 'inputs/archive/evidence.zip'
        self.transport = root / 'inputs/transport/TRANSPORT.json'
        self.tools = root / 'selected-tools'
        self.calls = []
        self.source_pins = {}
        for original, destination in [('proof_evidence.py', 'materialize.py'), ('payload_boundary.py', 'payload_boundary.py')]:
            if (source / original).exists():
                raw = (source / original).read_bytes()
                self.source_pins[original] = sha(raw)
                write(self.proofs / destination, raw)
                write(self.standalone / 'proofs' / destination, raw)
        self.proof_files = self.make_proof()
        for name, raw in self.proof_files.items():
            write(self.raw / name, raw)
        packed = archive(self.proof_files)
        write(self.zip, packed)
        descriptor = {'kind': 'stdo.formal-evidence-transport/1', 'archive_sha256': sha(packed),
            'archive_bytes': len(packed), 'expanded_bytes': sum(map(len, self.proof_files.values())),
            'manifest_sha256': sha(self.proof_files['manifest.json']), 'result_sha256': sha(self.proof_files['result.json']),
            'members': {name: {'bytes': len(raw), 'sha256': sha(raw)} for name, raw in self.proof_files.items()},
            'parts': [{'path': 'part-001.bin', 'bytes': len(packed), 'sha256': sha(packed)}]}
        for parent in (self.transport.parent, self.proofs / 'transport'):
            write(parent / 'TRANSPORT.json', encoded(descriptor))
            write(parent / 'part-001.bin', packed)
        write(self.proofs / 'PROOFS.json', encoded({'transport_sha256': sha(encoded(descriptor))}))
        self.make_tools()
        write(self.native / 'manifest.json', encoded({'fixture': 'synthetic native layout; not an installed release verdict'}))
        write(self.native / 'plugins/sentinel.txt', b'whole native payload protection includes plugin siblings\n')
        alias = root / 'NATIVE'
        self.case_alias = alias.exists() and os.path.samefile(alias, self.native)
        self.alias = alias
        write(root / 'FIXTURE.json', encoded({'scope': 'Synthetic source/transport and marker bootstrap; no Lean or native host',
            'source_directory': str(source), 'source_pins': self.source_pins,
            'case_alias': {'supported': self.case_alias, 'canonical': str(self.native), 'alias': str(alias),
                           'samefile': self.case_alias, 'canonical_resolve': str(self.native.resolve()),
                           'alias_resolve': str(alias.resolve()) if self.case_alias else None}}))

    @staticmethod
    def make_proof():
        files = {'input.json': b'{"synthetic":true}\n', 'supplied-views.json': b'[]\n',
                 'GateModel.lean': b'-- transport fixture, never presented as a proof\n',
                 'GateModel.olean': b'synthetic compiled carrier\x00'}
        request = {'schema': 'a_c.formal-gate.request/1', 'input': {'format': 'model', 'path': '/construction/input.json', 'raw_sha256': sha(files['input.json'])},
            'supplied_views': {'path': '/construction/views.json', 'raw_sha256': sha(files['supplied-views.json'])},
            'selections': [], 'context_binding': None}
        files['request.json'] = encoded(request)
        members = {name: sha(raw) for name, raw in files.items()}
        files['manifest.json'] = encoded({'schema': 'a_c.formal-gate.bundle/1', 'members': members})
        files['result.json'] = encoded({'schema': 'a_c.formal-gate.result/1', 'status': 'verified',
            'model': {'id': 'synthetic-boundary-fixture-only', 'sha256': sha(files['input.json'])}, 'selections': [], 'context_binding': None,
            'inputs': {'input': {'retained_path': 'input.json', 'raw_sha256': sha(files['input.json'])},
                       'model': {'raw_sha256': sha(files['input.json'])},
                       'supplied_views': {'retained_path': 'supplied-views.json', 'raw_sha256': sha(files['supplied-views.json'])}},
            'evidence': {'manifest_sha256': sha(files['manifest.json']), 'members': members}})
        return files

    def make_tools(self):
        bootstrap = ('from pathlib import Path\nimport sys\n'
                     'Path(' + repr(str(self.marker)) + ').write_text("selected fixture bootstrap invoked\\n")\n'
                     'print("marker-only fixture; no Lean or downloads")\nraise SystemExit(23)\n').encode()
        sources = {'a_c/VERSION': b'3.0.5\n', 'a_c/scripts/bootstrap.py': bootstrap,
                   'a_c/' + PROFILE: encoded({'fixture': 'selected source profile only'}),
                   'stdo_skills/VERSION': b'3.0.5\n', 'stdo_representation/VERSION': b'3.0.5\n',
                   'axiom_indexer/VERSION': b'3.0.5\n'}
        owners = {}
        rows = []
        for name, raw in sorted(sources.items()):
            row = {'path': name, 'bytes': len(raw), 'sha256': sha(raw), 'git_mode': '100644'}
            owners.setdefault(name.split('/')[0], {'version': '3.0.5', 'members': []})['members'].append(row)
            rows.append({'archive_path': name, **{key: row[key] for key in ('bytes', 'sha256', 'git_mode')}})
            write(self.tools / name, raw)
        selection = encoded({'kind': 'stdo.current-tooling-selection/1', 'version': '3.0.5',
                             'owners': owners, 'source_identity_sha256': '1' * 64})
        files = {'README.md': b'Synthetic selected tooling; boundary tests only.\n', 'SELECTION.json': selection,
                 'sources.zip': archive(sources)}
        for original, name in [('tooling_materialize.py', 'materialize.py'), ('tooling_setup.py', 'setup.py'),
                               ('tooling_runtime.py', 'runtime.py'), ('payload_boundary.py', 'payload_boundary.py')]:
            if (self.source / original).exists():
                files[name] = (self.source / original).read_bytes()
                self.source_pins[original] = sha(files[name])
        files['TOOLING.json'] = encoded({'kind': 'stdo.installed-tooling/2', 'distribution_version': '3.0.5',
            'source_identity_sha256': '1' * 64, 'selection_sha256': sha(selection), 'sources': rows,
            'source_inventory_sha256': sha(encoded(rows)),
            'distribution_members': {name: {'bytes': len(raw), 'sha256': sha(raw)} for name, raw in files.items()}})
        for parent in (self.tooling, self.standalone / 'tooling'):
            for name, raw in files.items(): write(parent / name, raw)

    def invoke(self, script, *arguments, no_bytecode=False):
        # The documented command uses ordinary Python, without -B. Remove only
        # the ambient bytecode override so import-time native writes are visible.
        env = dict(os.environ)
        env.pop('PYTHONDONTWRITEBYTECODE', None)
        before = tree(self.native)
        argv = [sys.executable, *(['-B'] if no_bytecode else []), str(script), *map(str, arguments)]
        run = subprocess.run(argv, cwd=self.root, env=env, capture_output=True, timeout=30)
        after = tree(self.native)
        directory = self.root / 'observations' / str(len(self.calls) + 1).zfill(3)
        write(directory / 'stdout', run.stdout); write(directory / 'stderr', run.stderr)
        try: result = json.loads(run.stdout)
        except (ValueError, UnicodeDecodeError): result = None
        row = {'argv': argv, 'returncode': run.returncode, 'result': result, 'before': before, 'after': after,
               'native_unchanged': before == after, 'bootstrap_invoked': self.marker.exists(),
               'stdout_sha256': sha(run.stdout), 'stderr_sha256': sha(run.stderr)}
        write(directory / 'execution.json', encoded(row))
        self.calls.append(row)
        return row

    def proof_arguments(self, operation, output, *, transport=None):
        transport = transport or self.transport
        if operation == 'pack': return ['pack', '--bundle', self.raw, '--output', output]
        if operation == 'split': return ['split', '--input', self.zip, '--destination', output]
        prefix = ['--archive', self.zip, '--archive-sha256', sha(self.zip.read_bytes())] if operation.endswith('-raw') else [
            '--transport', transport, '--transport-sha256', sha(transport.read_bytes())]
        if operation.startswith('materialize'): return [*prefix, 'materialize', '--destination', output]
        return [*prefix, 'request', '--evidence', self.raw, '--output', output]

    def derive(self, destination, receipt, *, script=None, no_bytecode=False):
        return self.invoke(script or self.tooling / 'setup.py', 'derive-runtime', '--tools', self.tools,
                           '--destination', destination, '--receipt', receipt, no_bytecode=no_bytecode)

    def prepare_runtime(self):
        runtime, receipt = self.root / 'runtime', self.root / 'derivation.json'
        result = self.derive(runtime, receipt, no_bytecode=True)
        if result['returncode'] != 0:
            raise AssertionError('Public fixture preparation failed: ' + str(result['result']))
        return runtime, receipt


class InstalledBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.source = Path(os.environ.get('STDO_BOUNDARY_SOURCE_DIR', str(HERE))).resolve()
        retained = os.environ.get('STDO_BOUNDARY_EVIDENCE_ROOT')
        if retained:
            self.root = Path(retained).absolute() / self._testMethodName
            self.root.mkdir(parents=True, exist_ok=False)
        else:
            temporary = tempfile.TemporaryDirectory(prefix='stdo-installed-boundary-')
            self.addCleanup(temporary.cleanup)
            self.root = Path(temporary.name).resolve()

    def fixture(self, label):
        return PayloadFixture(self.root / label, self.source)

    def assert_refused_unchanged(self, fixture, row, *outputs):
        self.assertEqual(row['returncode'], 2, row['result'])
        self.assertTrue(row['result'] and row['result']['status'] in ('refused', 'refused_or_incomplete'), row)
        self.assertTrue(row['native_unchanged'], 'Native payload changed; inspect retained execution.json before/after')
        self.assertFalse(fixture.marker.exists(), 'Bootstrap was invoked before boundary refusal')
        for output in outputs: self.assertFalse(output.exists(), str(output))

    def proof_native_cases(self, aliases):
        for operation in ('pack', 'split', 'materialize-transport', 'materialize-raw', 'request-transport', 'request-raw'):
            with self.subTest(operation=operation, case_alias=aliases):
                fixture = self.fixture(operation)
                if aliases and not fixture.case_alias: self.skipTest('Filesystem has no actual samefile case alias')
                native = fixture.alias if aliases else fixture.native
                script = native / ('STANDARDS/DOCUMENTATION/PROOFS/materialize.py' if aliases else 'standards/documentation/proofs/materialize.py')
                transport = native / ('STANDARDS/DOCUMENTATION/PROOFS/TRANSPORT/TRANSPORT.json' if aliases else 'standards/documentation/proofs/transport/TRANSPORT.json')
                output = native / ('forbidden-' + operation)
                row = fixture.invoke(script, *fixture.proof_arguments(operation, output, transport=transport))
                self.assert_refused_unchanged(fixture, row, output)

    def test_proof_all_write_commands_refuse_whole_native_outputs(self):
        self.proof_native_cases(False)

    def test_proof_actual_case_aliases_refuse_including_raw_external_inputs(self):
        self.proof_native_cases(True)

    def test_documented_default_transport_and_B_invocations_have_no_import_effects(self):
        for flag in (False, True):
            with self.subTest(no_bytecode=flag):
                fixture = self.fixture('B' if flag else 'ordinary')
                output = fixture.native / 'not-allowed'
                row = fixture.invoke(fixture.proofs / 'materialize.py', 'materialize', '--destination', output, no_bytecode=flag)
                self.assert_refused_unchanged(fixture, row, output)

    def test_proof_external_and_standalone_operations_preserve_native_and_originals(self):
        for standalone in (False, True):
            for operation in ('pack', 'split', 'materialize-transport', 'materialize-raw', 'request-transport', 'request-raw'):
                with self.subTest(standalone=standalone, operation=operation):
                    fixture = self.fixture(str(standalone) + '-' + operation)
                    script = (fixture.standalone / 'proofs' if standalone else fixture.proofs) / 'materialize.py'
                    original = tree(fixture.raw)
                    output = fixture.root / 'outside-output'
                    row = fixture.invoke(script, *fixture.proof_arguments(operation, output))
                    self.assertEqual(row['returncode'], 0, row['result'])
                    self.assertTrue(row['native_unchanged'])
                    self.assertEqual(original, tree(fixture.raw))
                    self.assertTrue(output.exists())
                    if operation.startswith('materialize'):
                        self.assertEqual({p.name: p.read_bytes() for p in output.iterdir()}, fixture.proof_files)
                    elif operation.startswith('request'):
                        value = json.loads(output.read_bytes())
                        self.assertEqual(value['input']['path'], str(fixture.raw / 'input.json'))
                        self.assertEqual(value['supplied_views']['path'], str(fixture.raw / 'supplied-views.json'))
                    elif operation == 'pack':
                        self.assertEqual(output.read_bytes(), fixture.zip.read_bytes())
                    else:
                        descriptor = json.loads((output / 'TRANSPORT.json').read_bytes())
                        self.assertEqual(b''.join((output / part['path']).read_bytes() for part in descriptor['parts']), fixture.zip.read_bytes())

    def test_runtime_destination_and_receipt_are_checked_together_before_effects(self):
        # -B isolates the original storage defect from the separately observed
        # module-loader side effect in ordinary documented invocation.
        for aliases, no_bytecode in ((False, False), (True, False), (False, True), (True, True)):
            for protected_slot in ('destination', 'receipt'):
                with self.subTest(case_alias=aliases, protected_slot=protected_slot, no_bytecode=no_bytecode):
                    fixture = self.fixture(str(aliases) + '-' + protected_slot + '-' + str(no_bytecode))
                    if aliases and not fixture.case_alias: self.skipTest('Filesystem has no actual samefile case alias')
                    native = fixture.alias if aliases else fixture.native
                    script = native / ('STANDARDS/TOOLING/setup.py' if aliases else 'standards/tooling/setup.py')
                    destination = (native if protected_slot == 'destination' else fixture.root) / 'derived-runtime'
                    receipt = (native if protected_slot == 'receipt' else fixture.root) / 'derived-receipt.json'
                    row = fixture.derive(destination, receipt, script=script, no_bytecode=no_bytecode)
                    self.assert_refused_unchanged(fixture, row, destination, receipt)

    def test_derive_and_materialize_external_or_standalone_still_work(self):
        for standalone in (False, True):
            with self.subTest(standalone=standalone):
                fixture = self.fixture(str(standalone))
                bundle = fixture.standalone / 'tooling' if standalone else fixture.tooling
                destination = fixture.root / 'materialized-source'
                row = fixture.invoke(bundle / 'materialize.py', 'materialize', '--destination', destination)
                self.assertEqual(row['returncode'], 0, row['result'])
                self.assertTrue(row['native_unchanged'])
                fixture.tools = destination
                runtime, receipt = fixture.root / 'derived', fixture.root / 'derived.json'
                row = fixture.derive(runtime, receipt, script=bundle / 'setup.py')
                self.assertEqual(row['returncode'], 0, row['result'])
                self.assertTrue(row['native_unchanged'])
                record = json.loads(receipt.read_bytes())
                self.assertEqual(record['runtime_root'], str(runtime))
                for name, selected in record['source_members'].items():
                    self.assertEqual(sha((runtime / name).read_bytes()), selected['sha256'])

    def test_bootstrap_native_output_or_runtime_refuses_before_marker(self):
        for aliases, no_bytecode in ((False, False), (True, False), (False, True), (True, True)):
            for protected_slot in ('output', 'runtime'):
                with self.subTest(case_alias=aliases, protected_slot=protected_slot, no_bytecode=no_bytecode):
                    fixture = self.fixture(str(aliases) + '-' + protected_slot + '-' + str(no_bytecode))
                    if aliases and not fixture.case_alias: self.skipTest('Filesystem has no actual samefile case alias')
                    runtime, receipt = fixture.prepare_runtime()
                    native = fixture.alias if aliases else fixture.native
                    script = native / ('STANDARDS/TOOLING/setup.py' if aliases else 'standards/tooling/setup.py')
                    output = (native if protected_slot == 'output' else fixture.root) / 'bootstrap-evidence'
                    if protected_slot == 'runtime':
                        # A structurally complete retained prepared receipt can
                        # nominate an unsafe runtime; setup must reject it before invocation.
                        shutil.copytree(runtime, fixture.native / 'retained-runtime')
                        record = json.loads(receipt.read_bytes())
                        record['runtime_root'] = str(native / 'retained-runtime')
                        receipt.write_bytes(encoded(record))
                    row = fixture.invoke(script, 'bootstrap-lean', '--derivation', receipt,
                        '--derivation-sha256', sha(receipt.read_bytes()), '--python', sys.executable, '--output', output,
                        no_bytecode=no_bytecode)
                    self.assert_refused_unchanged(fixture, row, output)

    def test_external_bootstrap_invokes_only_marker_and_retains_its_deliberate_failure(self):
        fixture = self.fixture('outside')
        _, receipt = fixture.prepare_runtime()
        output = fixture.root / 'bootstrap-evidence'
        row = fixture.invoke(fixture.tooling / 'setup.py', 'bootstrap-lean', '--derivation', receipt,
            '--derivation-sha256', sha(receipt.read_bytes()), '--python', sys.executable, '--output', output)
        self.assertEqual(row['returncode'], 2)
        self.assertIn('bootstrap incomplete', row['result']['reason'])
        self.assertTrue(row['native_unchanged'])
        self.assertEqual(fixture.marker.read_text(), 'selected fixture bootstrap invoked\n')
        execution = json.loads((output / 'execution.json').read_bytes())
        self.assertEqual(execution['returncode'], 23)
        self.assertEqual(set(p.name for p in output.iterdir()), {'execution.json', 'stdout.txt', 'stderr.txt'})

    def test_equal_ancestor_symlink_and_existing_outputs_preserve_preimage(self):
        for relation in ('equal', 'ancestor', 'symlink', 'existing'):
            with self.subTest(relation=relation):
                fixture = self.fixture(relation)
                output = fixture.native if relation == 'equal' else fixture.root if relation == 'ancestor' else fixture.native / 'sentinel-output'
                if relation == 'symlink':
                    link = fixture.root / 'linked-native'; link.symlink_to(fixture.native, target_is_directory=True)
                    output = link / 'not-allowed'
                if relation == 'existing': write(output, b'preexisting selected user bytes\n')
                row = fixture.invoke(fixture.proofs / 'materialize.py', *fixture.proof_arguments('request-raw', output))
                self.assertEqual(row['returncode'], 2)
                self.assertTrue(row['native_unchanged'])
                if relation == 'existing': self.assertEqual(output.read_bytes(), b'preexisting selected user bytes\n')
                if relation == 'symlink': self.assertFalse(output.exists())


if __name__ == '__main__':
    unittest.main()
