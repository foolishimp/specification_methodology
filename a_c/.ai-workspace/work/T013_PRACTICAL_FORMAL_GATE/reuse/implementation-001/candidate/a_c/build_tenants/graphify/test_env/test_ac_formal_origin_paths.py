"""Synthetic selected-path controls; no real origin, Lean, or actor invocation."""
from contextlib import contextmanager
import copy
import os
from pathlib import Path
import unittest
from unittest.mock import patch

import test_ac_formal_gate as controls
import ac_generate as generation
import ac_grounding as grounding
import ac_repair as repair
import ac_support_core as core

formal = core.ac_formal_gate


class FormalOriginPathControls(unittest.TestCase):
    setUp = controls.FormalGateControls.setUp
    retain_control = controls.FormalGateControls.retain_control
    identity = controls.FormalGateControls.identity
    fixture = controls.FormalGateControls.fixture

    def secret(self):
        path = self.checker / '.cache/formal-origin-v1/origin.key'
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():path.write_bytes(b'UNIT-SYNTHETIC-KEY-NOT-PRODUCTION')
        return path

    @contextmanager
    def no_secret_read(self, secret):
        original = Path.read_bytes
        original_open = os.open
        def checked(path):
            if path.exists() and path.is_file() and path.stat().st_ino == secret.stat().st_ino:
                raise AssertionError('protected synthetic bytes reached ordinary read')
            return original(path)
        def checked_open(path, *args, **kwargs):
            candidate = Path(path)
            if candidate.exists() and candidate.is_file() and candidate.stat().st_ino == secret.stat().st_ino:
                raise AssertionError('protected synthetic bytes reached ordinary descriptor open')
            return original_open(path, *args, **kwargs)
        with patch.object(Path, 'read_bytes', checked), patch.object(os, 'open', checked_open):
            yield

    def prepare(self, selected=True):
        ordinal = len(list(self.root.glob('run-*')))
        corpus = self.root / ('corpus-' + str(ordinal)); corpus.mkdir()
        raw = b'# Unit source\nA bounded source for acquisition controls.\n'
        (corpus / 'rules.md').write_bytes(raw)
        manifest = self.root / ('manifest-' + str(ordinal) + '.json')
        generation.save(manifest, {'profile': 'ac.generation.corpus/1', 'subject_id': 'repo://unit/path-controls/',
                                  'revision': 'unit-only', 'files': [{'path': 'rules.md', 'sha256': generation.sha(raw), 'bytes': len(raw)}]})
        output = self.root / ('run-' + str(ordinal))
        generation.prepare(corpus, manifest, output, 'direct', None, formal_checker=self.config if selected else None)
        return output

    def test_adapter_output_and_bundle_guard_precede_checker_or_retention(self):
        secret = self.secret()
        with patch.object(formal, 'current', side_effect=AssertionError('checker ran before path guard')):
            for output in (secret, secret.parent / 'out', self.checker):
                with self.assertRaises(formal.GateError):
                    formal.verify(self.config, b'unit', 'model', [], None, None, output)
            with self.assertRaises(formal.GateError):
                formal.recheck(self.config, {'bundle': str(secret.parent)}, self.root / 'recheck')
        self.assertFalse((secret.parent / 'out').exists())

    def test_initial_manifest_and_corpus_protection_precede_read_and_copy(self):
        secret = self.secret(); corpus = self.root / 'corpus'; corpus.mkdir()
        with self.no_secret_read(secret):
            with self.assertRaises(generation.ac_formal_gate.GateError):
                generation.prepare(corpus, secret, self.root / 'bad-manifest', 'direct', None, formal_checker=self.config)
        self.assertFalse((self.root / 'bad-manifest').exists())
        manifest = self.root / 'manifest.json'
        generation.save(manifest, {'subject_id': 'repo://unit/source/', 'files': [
            {'path': '.cache/formal-origin-v1/origin.key', 'sha256': '0' * 64}]})
        with self.no_secret_read(secret):
            with self.assertRaises(generation.ac_formal_gate.GateError):
                generation.prepare(self.checker, manifest, self.root / 'bad-corpus', 'direct', None, formal_checker=self.config)
        self.assertFalse((self.root / 'bad-corpus').exists())

    def test_shared_selected_checkpoint_blocks_aliases_before_every_resume_consumer(self):
        secret = self.secret()
        callers = [lambda p: generation.stage(p, 'author', execute=False),
                   lambda p: generation.build_discovery(p), lambda p: generation.assemble(p),
                   lambda p: generation.main(['run', '--output', str(p)]),
                   lambda p: grounding.normalize(p), lambda p: grounding.assemble(p),
                   lambda p: repair.choose_chunk(p, 'unused'), lambda p: repair.assemble(p)]
        for index, caller in enumerate(callers):
            for member in ('source-manifest.json', 'chunks.json', 'corpus/rules.md', 'upstream-extraction-spec.md', 'actor-journal.json'):
                with self.subTest(caller=index, member=member):
                    output = self.prepare()
                    target = output / member; target.unlink(missing_ok=True); os.link(secret, target)
                    with self.no_secret_read(secret), patch.object(generation, 'run_actor', side_effect=AssertionError('actor invoked')):
                        if index == 3:
                            self.assertEqual(caller(output), 2)
                        else:
                            with self.assertRaises(generation.ac_formal_gate.GateError):caller(output)
                    target.unlink()

    def test_metadata_scan_refuses_symlink_directories_without_following_or_reading(self):
        output = self.prepare(); secret = self.secret()
        (output / 'actor-alias').symlink_to(secret.parent, target_is_directory=True)
        with self.no_secret_read(secret):
            with self.assertRaises(generation.ac_formal_gate.GateError):generation.checkpoint(output)

    def test_direct_repair_and_grounding_entries_guard_before_first_journal_read(self):
        output = self.prepare(); secret = self.secret()
        attempt = output / repair.REPAIRS / 'chunk-unit' / 'attempt-001'; attempt.mkdir(parents=True)
        os.link(secret, attempt / 'request.json')
        with self.no_secret_read(secret):
            with self.assertRaises(generation.ac_formal_gate.GateError):repair.verify_request(output, attempt)
        (attempt / 'request.json').unlink()
        folder = output / 'normalization/chunk-unit'; folder.mkdir(parents=True)
        os.link(secret, folder / 'journal.json')
        with self.no_secret_read(secret):
            with self.assertRaises(generation.ac_formal_gate.GateError):grounding.verify_normalization(output, {}, {}, folder)
        (folder / 'journal.json').unlink()
        with self.no_secret_read(secret):
            with self.assertRaises(generation.GenerationError):grounding.verify_normalization(output, {}, {}, secret.parent)

    def test_explicit_first_selection_protects_checkpoint_before_persistence(self):
        output = self.prepare(False); secret = self.secret()
        (output / 'chunks.json').unlink(); os.link(secret, output / 'chunks.json')
        with self.no_secret_read(secret):
            with self.assertRaises(generation.ac_formal_gate.GateError):generation.assemble(output, formal_checker=self.config)
        self.assertFalse((output / 'formal-selection.json').exists())

    def test_inherited_resume_and_unselected_generation_need_no_new_flags_or_lean(self):
        selected = self.prepare()
        with patch.object(generation.ac_formal_gate, 'current', side_effect=AssertionError('checkpoint launched Lean')):
            plan, _ = generation.checkpoint(selected)
            self.assertEqual(plan['formal_checker'], self.config)
            self.assertEqual(generation.stage(selected, 'author', execute=False)['status'], 'incomplete')
        with patch.object(generation.ac_formal_gate, 'guard_path', side_effect=AssertionError('unselected origin dependency')):
            unselected = self.prepare(False)
            self.assertNotIn('formal_checker', generation.checkpoint(unselected)[0])
            self.assertEqual(generation.stage(unselected, 'author', execute=False)['status'], 'incomplete')

    def test_broad_registered_root_accepts_normal_source_but_reserves_actual_targets(self):
        secret = self.secret(); normal = self.checker / 'normal.txt'; normal.write_bytes(b'normal source')
        fixture = self.fixture()
        fixture.policy['sources']['broad'] = {'path': str(self.root), 'read_scope': [{'path': 'checker', 'kind': 'directory'}], 'kind': 'workspace', 'writable': True}
        runtime = fixture.runtime()
        ref = fixture.ref(normal, 'broad', 'checker/normal.txt')
        self.assertEqual(core.read_source(runtime, ref)['parent_sha256'], formal.sha(normal.read_bytes()))
        protected = dict(ref, path='checker/.cache/formal-origin-v1/origin.key')
        with self.no_secret_read(secret):
            with self.assertRaises(core.SupportError):core.read_source(runtime, protected)
        absent = dict(ref, path='checker/.cache/formal-origin-v1/absent')
        with self.assertRaises(core.SupportError):core.source_path(runtime, absent, write=True, allow_absent=True)
        with self.assertRaises(core.SupportError):core.source_path(runtime, dict(ref, path='checker'), write=True)
        alias = self.checker / 'alias.txt'; os.link(secret, alias)
        with self.no_secret_read(secret):
            with self.assertRaises(core.SupportError):core.read_source(runtime, dict(ref, path='checker/alias.txt'))
        alias.unlink()
        del fixture.policy['formal_gate']; runtime = fixture.runtime()
        with patch.object(formal, 'guard_path', side_effect=AssertionError('unselected source imported Lean policy')):
            self.assertEqual(core.source_path(runtime, ref), normal)

    def test_live_graphify_origin_pin_equality_remains_strict(self):
        selected = self.secret().with_name('selection.json'); selected.write_bytes(b'UNIT selected A')
        config = copy.deepcopy(self.config)
        config['runtime_identity']['pins']['.cache/formal-origin-v1/selection.json'] = formal.sha(selected.read_bytes())
        config['runtime_identity']['sha256'] = formal.sha(formal.canonical(config['runtime_identity']['pins']))
        selected.write_bytes(b'UNIT selected B')
        with patch.object(formal.subprocess, 'Popen', side_effect=AssertionError('stale live configuration executed')):
            with self.assertRaises(formal.GateError):formal.current(config)
            selected.unlink()
            with self.assertRaises(formal.GateError):formal.current(config)

    def test_case_alias_source_and_output_refuse_before_any_read(self):
        secret = self.secret()
        alias = Path(str(secret).replace('/.cache/', '/.CACHE/'))
        if not alias.exists() or not alias.samefile(secret):
            self.skipTest('selected filesystem has no case aliases')
        fixture = self.fixture()
        fixture.policy['sources']['broad'] = {'path': str(self.root), 'read_scope': [{'path': 'checker', 'kind': 'directory'}], 'kind': 'workspace', 'writable': True}
        runtime = fixture.runtime()
        ref = {'engine': 'workspace-regular-file', 'root': 'broad', 'path': 'checker/.CACHE/formal-origin-v1/origin.key',
               'object': None, 'sha256': '0' * 64, 'selector': None}
        with self.no_secret_read(secret):
            with self.assertRaises(core.SupportError):core.read_source(runtime, ref)
            with self.assertRaises(formal.GateError):formal.read_selected(self.config, alias)
            with self.assertRaises(formal.GateError):formal.guard_path(self.config, alias.parent / 'out', output=True)
            with self.assertRaises(formal.GateError):formal.guard_path(self.config, self.checker.with_name('CHECKER'), output=True)
        empty = self.root / 'empty-checker'; empty.mkdir()
        with self.assertRaises(formal.GateError):formal.guard_path(dict(self.config, root=str(empty)), empty / '.CACHE/FORMAL-ORIGIN-V1/out', output=True)


if __name__ == '__main__':
    unittest.main()
