"""Exact transport controls; synthetic files do not assert a Lean execution."""
import io
import json
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import patch

import proof_evidence as proof


class EvidenceTransportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='stdo-proof-zip-'); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve(); self.bundle = self.root / 'raw'; self.bundle.mkdir()
        data = {'GateModel.lean': b'exact synthetic source\n', 'GateModel.olean.private': b'compiled fixture bytes\0' * 1024,
                'input.json': b'{"toy": true}\n', 'supplied-views.json': b'[]\n'}
        request = {'schema': 'a_c.formal-gate.request/1', 'input': {'format': 'model', 'path': '/unavailable/construction/model.json', 'raw_sha256': proof.sha(data['input.json'])},
                   'supplied_views': {'path': '/unavailable/construction/views.json', 'raw_sha256': proof.sha(data['supplied-views.json'])},
                   'selections': [], 'context_binding': None}
        data['request.json'] = json.dumps(request).encode()
        manifest = {'schema': 'a_c.formal-gate.bundle/1', 'members': {n: proof.sha(raw) for n, raw in data.items()}}
        raw = (json.dumps(manifest, sort_keys=True, indent=2)+'\n').encode(); data['manifest.json'] = raw
        data['result.json'] = json.dumps({'schema': 'a_c.formal-gate.result/1', 'status': 'verified',
            'model': {'id': 'synthetic-transport-test-only', 'sha256': proof.sha(data['input.json'])}, 'selections': [], 'context_binding': None,
            'inputs': {'input': {'retained_path': 'input.json', 'raw_sha256': proof.sha(data['input.json'])},
                       'model': {'raw_sha256': proof.sha(data['input.json'])},
                       'supplied_views': {'retained_path': 'supplied-views.json', 'raw_sha256': proof.sha(data['supplied-views.json'])}},
            'evidence': {'manifest_sha256': proof.sha(raw), 'members': manifest['members']}}).encode()
        for n, raw in data.items(): (self.bundle/n).write_bytes(raw)
        self.archive = self.root / 'transport/evidence.zip'

    def test_actual_deterministic_roundtrip_with_original_raw_unavailable(self):
        first = proof.pack(self.bundle, self.archive)
        second = self.root / 'second/evidence.zip'; proof.pack(self.bundle, second)
        self.assertEqual(self.archive.read_bytes(), second.read_bytes())
        self.bundle.rename(self.root / 'unavailable-original')
        output = self.root / 'recovered'
        result = proof.materialize(self.archive, output, first['archive_sha256'])
        self.assertEqual(result['status'], 'materialized')
        proof.verify_tree(self.archive.read_bytes(), output, first['archive_sha256'])
        (output/'input.json').write_bytes(b'tamper')
        with self.assertRaisesRegex(ValueError, 'bytes differ'): proof.verify_tree(self.archive.read_bytes(), output)

    def test_private_key_or_unselected_member_cannot_enter_archive(self):
        (self.bundle/'origin-private.key').write_bytes(b'fixture-not-a-secret')
        with self.assertRaisesRegex(ValueError, 'unselected evidence member'): proof.pack(self.bundle, self.archive)
        self.assertFalse(self.archive.exists())

    def test_portable_request_public_command_preserves_original_and_rejects_changed_inputs(self):
        packed = proof.pack(self.bundle, self.archive)
        parts = self.root / 'parts'; selected = proof.split(self.archive, parts)
        original = (self.bundle / 'request.json').read_bytes()
        self.archive.unlink(); shutil.rmtree(self.bundle)
        recovered = self.root / 'recovered'; proof.materialize_transport(parts / 'TRANSPORT.json', recovered, selected['transport_sha256'])
        output = self.root / 'current-request.json'
        run = subprocess.run([sys.executable, '-I', '-B', proof.__file__, '--transport', str(parts / 'TRANSPORT.json'),
            '--transport-sha256', selected['transport_sha256'], 'request', '--evidence', str(recovered), '--output', str(output)], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        value = json.loads(output.read_bytes())
        self.assertEqual(value['input']['path'], str(recovered / 'input.json'))
        self.assertEqual(value['supplied_views']['path'], str(recovered / 'supplied-views.json'))
        self.assertNotIn('/unavailable/', output.read_text())
        self.assertEqual((recovered / 'request.json').read_bytes(), original)
        raw, _, _ = proof.read_transport(parts / 'TRANSPORT.json')
        with self.assertRaisesRegex(ValueError, 'absent request output'): proof.current_request(raw, recovered, output, parts)
        with self.assertRaisesRegex(ValueError, 'overlaps'): proof.current_request(raw, recovered, recovered / 'new-request.json', parts)
        (recovered / 'input.json').write_bytes(b'changed input')
        with self.assertRaisesRegex(ValueError, 'bytes differ'): proof.current_request(raw, recovered, self.root / 'bad.json', parts)
        self.assertFalse((self.root / 'bad.json').exists())

    def test_redirect_and_output_overlap_refuse(self):
        file = self.bundle/'input.json'; raw=file.read_bytes();file.unlink(); outside=self.root/'outside';outside.write_bytes(raw);file.symlink_to(outside)
        with self.assertRaisesRegex(ValueError, 'redirected'): proof.pack(self.bundle,self.archive)
        with self.assertRaisesRegex(ValueError, 'overlaps'): proof.pack(self.bundle,self.bundle/'archive.zip')

    def changed_archive(self, mutation):
        proof.pack(self.bundle,self.archive); source=self.archive.read_bytes(); out=io.BytesIO()
        with zipfile.ZipFile(io.BytesIO(source)) as original, zipfile.ZipFile(out,'w') as target:
            rows=[(i,original.read(i)) for i in original.infolist()]
            for info,raw in mutation(rows): target.writestr(info,raw)
        return out.getvalue()

    def test_traversal_symlink_duplicate_missing_extra_and_tampered_members_refuse(self):
        def change(rows, name=None, mode=None, raw=None):
            info,value=rows[0]
            if name is not None:info.filename=name
            if mode is not None:info.external_attr=mode<<16
            return [(info,raw if raw is not None else value),*rows[1:]]
        mutations=[lambda rows:change(rows,name='../escape'),lambda rows:change(rows,mode=stat.S_IFLNK|0o644),
                   lambda rows:[rows[0],*rows],lambda rows:rows[1:],lambda rows:change(rows,name='extra'),
                   lambda rows:change(rows,raw=b'changed')]
        for mutate in mutations:
            if self.archive.exists():self.archive.unlink()
            with self.subTest(mutation=mutate),self.assertRaises(ValueError):proof.inspect(self.changed_archive(mutate))

    def test_wrong_digest_existing_target_and_native_case_alias_refuse(self):
        value=proof.pack(self.bundle,self.archive); out=self.root/'out'
        with self.assertRaisesRegex(ValueError,'digest differs'):proof.materialize(self.archive,out,'0'*64)
        self.assertFalse(out.exists())
        out.mkdir()
        with self.assertRaisesRegex(ValueError,'absent'):proof.materialize(self.archive,out,value['archive_sha256'])
        alias=self.root/'TRANSPORT'
        if alias.exists():
            with self.assertRaisesRegex(ValueError,'aliases'):proof.materialize(self.archive,alias/'new',value['archive_sha256'])


    def test_ordered_parts_recover_without_raw_zip_and_reject_bad_parts(self):
        proof.pack(self.bundle,self.archive); directory=self.root/'parts'
        # Small part bound exercises multi-part mechanics; real-current controls use 64MiB.
        with patch.object(proof,'PART_BYTES',128):
            packed=proof.split(self.archive,directory); descriptor=(directory/'TRANSPORT.json').read_bytes()
            self.archive.unlink(); shutil.rmtree(self.bundle)
            value=proof.materialize_transport(directory/'TRANSPORT.json',self.root/'from-parts',packed['transport_sha256'])
            self.assertEqual(value['status'],'materialized'); self.assertGreater(len(value['parts']),1)
            original=json.loads(descriptor)
            for mutation in (lambda v:v['parts'].reverse(),lambda v:v['parts'].pop(),lambda v:v['parts'][0].update(sha256='0'*64)):
                changed=json.loads(descriptor);mutation(changed)
                with self.assertRaises(ValueError):proof.join(json.dumps(changed).encode(),lambda name:(directory/name).read_bytes())
            (directory/'extra').write_bytes(b'not selected')
            with self.assertRaisesRegex(ValueError,'population'):proof.read_transport(directory/'TRANSPORT.json')
            (directory/'extra').unlink(); part=directory/original['parts'][0]['path'];raw=part.read_bytes();part.unlink()
            outside=self.root/'outside-part';outside.write_bytes(raw);part.symlink_to(outside)
            with self.assertRaisesRegex(ValueError,'redirected'):proof.read_transport(directory/'TRANSPORT.json')


if __name__=='__main__':unittest.main()
