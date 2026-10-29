"""Synthetic origin/control evidence only: the proof and support engine is stubbed.

No real toolchain, support objects, established origin, full model or F_P actor
is acquired. Real cold/reuse qualification belongs to the final integrated cut.
"""
from contextlib import ExitStack
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import formal_gate as gate
import formal_reuse as reuse


class ReuseControls(unittest.TestCase):
    def setUp(self):
        temporary = ROOT / '.cache' / 'reuse-unit'
        temporary.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=temporary)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.checker = self.root / 'checker'; self.checker.mkdir()
        self.stack = ExitStack(); self.addCleanup(self.stack.close)
        self.stack.enter_context(patch.object(reuse, 'ROOT', self.checker))
        self.stack.enter_context(patch.object(gate, 'ROOT', self.checker))
        self.stack.enter_context(patch.object(gate, 'runtime_identity', side_effect=self.identity))
        self.support = self.stack.enter_context(patch.object(gate.support, 'check', return_value={'unit_stub': 'no proof/support qualification'}))
        self.stack.enter_context(patch.object(gate.support, 'proof_environment', return_value=(self.root / 'never-executed-toolchain', {}, None)))
        self.process = self.stack.enter_context(patch.object(gate.runtime_process, 'run', side_effect=self.proof_stub))
        self.subject = self.root / 'subject.json'
        self.subject.write_bytes((ROOT / 'fixtures/toy/MODEL.json').read_bytes())
        self.imported = gate.bridge.import_model(gate.read_json_bytes(self.subject.read_bytes()))
        self.selections = [{'seeds': [self.imported['records'][0]['record']['id']], 'budget_records': None}]
        case = gate.bridge.closure_certificate(self.imported, [0])
        self.views = self.root / 'views.json'
        self.views.write_bytes(reuse.canonical([gate.graphify_view(self.imported, case, self.selections[0])]))
        self.request = {'schema': 'a_c.formal-gate.request/1',
                        'input': {'format': 'model', 'path': str(self.subject), 'raw_sha256': reuse.sha(self.subject.read_bytes())},
                        'selections': self.selections,
                        'supplied_views': {'path': str(self.views), 'raw_sha256': reuse.sha(self.views.read_bytes())},
                        'context_binding': {'rendered_sha256': 'a' * 64, 'activation_identity': {'id': 'unit-only'}}}
        self.counter = 0
        reuse.init_origin()

    def identity(self):
        pins = {'scripts/formal_gate.py': '1' * 64, 'scripts/formal_reuse.py': '2' * 64,
                'profiles/proof-support-v1.json': '3' * 64}
        selected = reuse.selection()
        if selected is not None:
            pins[reuse.ORIGIN_SELECTION_PIN] = selected[1]
        return {'pins': pins, 'sha256': reuse.sha(reuse.canonical(pins))}

    def proof_stub(self, command, *, cwd, env, stdout, timeout):
        """Only controlled orchestration; these bytes are not a Lean proof."""
        directory = Path(stdout.name).parent
        if '-o' in command:
            target = Path(command[command.index('-o') + 1])
            target.write_bytes(b'UNIT-STUB-NOT-LEAN:' + target.name.encode())
            source = Path(command[-1]).read_text()
            names = re.findall(r'#print axioms ([A-Za-z0-9_.]+)', source)
            stdout.write(''.join("'AC.GateData." + name + "' does not depend on any axioms\n" for name in names).encode())
        elif '--run' in command:
            cases = gate.read_json_bytes((directory / 'certificates.json').read_bytes())
            raw_sha = reuse.sha((directory / 'input.json').read_bytes())
            actual = {'model': gate.model_output(self.imported, raw_sha), 'views': [
                {'status': 'refused', 'reason': 'insufficient record budget; required closure is not truncated'}
                if case['effective_budget'] < case['required_count'] else
                {'status': 'verified', 'projection': gate.projection_output(self.imported, case, raw_sha)} for case in cases]}
            stdout.write(reuse.canonical(actual))
        else:
            stdout.write(b'UNIT STUB: no kernel executed\n')
        return subprocess.CompletedProcess(command, 0)

    def output(self):
        self.counter += 1
        return self.root / ('bundle-' + str(self.counter))

    def cold(self, request=None):
        out = self.output()
        result = gate.verify(deepcopy(request or self.request), out)
        self.assertEqual(result['status'], 'verified', result.get('reason'))
        self.assertEqual(self.process.call_count % 9, 0)
        return out, result

    def refresh(self, out):
        manifest = reuse.decode((out / 'manifest.json').read_bytes())
        manifest['members'] = {name: reuse.sha((out / name).read_bytes()) for name in manifest['members']}
        (out / 'manifest.json').write_bytes(reuse.canonical(manifest))
        result = reuse.decode((out / 'result.json').read_bytes())
        result['evidence'] = {'manifest_sha256': reuse.sha((out / 'manifest.json').read_bytes()), 'members': manifest['members']}
        (out / 'result.json').write_bytes(reuse.canonical(result))

    def test_exact_reuse_and_reuse_of_reuse_preserve_original_cost_and_artifacts(self):
        old, cold = self.cold()
        self.process.reset_mock(); self.support.reset_mock()
        out = self.output(); result = gate.check_evidence(old, out)
        self.assertEqual(result['status'], 'verified', result.get('reason'))
        self.assertEqual(result['observations']['reuse'], 'local-origin')
        self.process.assert_not_called(); self.assertEqual(self.support.call_count, 2)
        self.assertEqual(reuse.decode((out / 'origin-result.json').read_bytes()), cold)
        for field in ('current_dynamic_proof_invocations', 'current_kernel_replay_invocations', 'current_runtime_invocations'):
            self.assertEqual(result['observations'][field], 0)
        again = self.output(); newest = gate.check_evidence(out, again)
        self.assertEqual(newest['status'], 'verified', newest.get('reason'))
        self.process.assert_not_called()
        self.assertEqual((again / 'origin-result.json').read_bytes(), (old / 'result.json').read_bytes())
        self.assertEqual(reuse.decode((again / 'local-origin.json').read_bytes())['entry_id'], reuse.decode((old / 'local-origin.json').read_bytes())['entry_id'])
        key = (self.checker / reuse.STORE_RELATIVE / 'origin.key').read_bytes()
        self.assertTrue(all(key not in path.read_bytes() for path in again.iterdir()))

    def test_foreign_and_absent_origin_only_identity_execute_cold(self):
        old, _ = self.cold()
        for selected in (False, True):
            checker = self.root / ('foreign-' + str(selected)); checker.mkdir()
            with patch.object(reuse, 'ROOT', checker), patch.object(gate, 'ROOT', checker):
                if selected: reuse.init_origin()
                self.process.reset_mock()
                out = self.output(); result = gate.check_evidence(old, out)
                self.assertEqual(result['status'], 'verified', result.get('reason'))
                self.assertEqual(result['runtime_identity'], self.identity())
                self.assertEqual(self.process.call_count, 9)
                self.assertNotEqual(result['observations']['reuse'], 'local-origin')

    def test_nonorigin_pin_drift_extra_pin_and_bad_aggregate_refuse(self):
        old, _ = self.cold()
        for mode in ('changed', 'extra', 'aggregate'):
            identity = self.identity()
            if mode == 'changed': identity['pins']['scripts/formal_reuse.py'] = '4' * 64
            if mode == 'extra': identity['pins']['caller-labelled-origin.json'] = '5' * 64
            identity['sha256'] = reuse.sha(reuse.canonical(identity['pins'])) if mode != 'aggregate' else '0' * 64
            self.process.reset_mock()
            with patch.object(gate, 'runtime_identity', return_value=identity):
                result = gate.check_evidence(old, self.output())
            self.assertEqual(result['status'], 'refused'); self.process.assert_not_called()

    def test_public_manifest_refresh_cannot_forge_exact_origin(self):
        old, _ = self.cold()
        for name in ('input.json', 'model.json', 'supplied-views.json', 'certificates.json', 'GateModel.lean',
                     'GateModel.olean', 'GateModel.log', 'actual-runtime.log', 'view-comparison.json', 'result.json'):
            with self.subTest(name=name):
                changed = self.output(); shutil.copytree(old, changed)
                (changed / name).write_bytes((changed / name).read_bytes() + b' ')
                self.refresh(changed)
                self.process.reset_mock()
                result = gate.check_evidence(changed, self.output())
                self.assertEqual(result['status'], 'refused', result)
                self.process.assert_not_called()

    def test_exact_request_and_limits_cannot_be_refreshed_by_caller(self):
        old, _ = self.cold()
        modifications = [lambda r: r['selections'][0].update(budget_records=100),
                         lambda r: r['selections'][0]['seeds'].append(self.imported['records'][1]['record']['id']),
                         lambda r: r['context_binding']['activation_identity'].update(id='different'),
                         lambda r: r['context_binding'].update(rendered_sha256='b' * 64)]
        for modify in modifications:
            changed = self.output(); shutil.copytree(old, changed)
            original = reuse.decode((changed / 'request.json').read_bytes()); modify(original)
            replay = deepcopy(original); replay['input']['path'] = 'input.json'; replay['supplied_views']['path'] = 'supplied-views.json'
            for name, value in (('request.json', original), ('replay-request.json', replay)):
                (changed / name).write_bytes(reuse.canonical(value))
            result = reuse.decode((changed / 'result.json').read_bytes()); result['request_sha256'] = gate.digest(original)
            (changed / 'result.json').write_bytes(reuse.canonical(result)); self.refresh(changed)
            self.assertEqual(gate.check_evidence(changed, self.output())['status'], 'refused')
        self.assertEqual(gate.check_evidence(old, self.output(), {'max_selections': 1})['status'], 'refused')

    def test_current_reused_request_is_type_exact_against_original_establishment(self):
        request = deepcopy(self.request); request['context_binding']['activation_identity']['flag'] = True
        old, _ = self.cold(request)
        reused = self.output(); self.assertEqual(gate.check_evidence(old, reused)['status'], 'verified')
        for name in ('request.json', 'replay-request.json'):
            value = reuse.decode((reused / name).read_bytes())
            value['context_binding']['activation_identity']['flag'] = 1
            (reused / name).write_bytes(reuse.canonical(value))
        value = reuse.decode((reused / 'result.json').read_bytes())
        value['request_sha256'] = reuse.sha(reuse.canonical(reuse.decode((reused / 'request.json').read_bytes())))
        (reused / 'result.json').write_bytes(reuse.canonical(value)); self.refresh(reused)
        self.process.reset_mock()
        self.assertEqual(gate.check_evidence(reused, self.output())['status'], 'refused')
        self.process.assert_not_called()

    def test_failed_cold_stages_never_publish(self):
        for failing in range(1, 10):
            with self.subTest(stage=failing):
                count = 0
                def fail_one(*args, **kwargs):
                    nonlocal count
                    count += 1
                    return subprocess.CompletedProcess(args[0], 1) if count == failing else self.proof_stub(*args, **kwargs)
                with patch.object(gate.runtime_process, 'run', side_effect=fail_one):
                    out = self.output(); result = gate.verify(self.request, out)
                self.assertEqual(result['status'], 'incomplete')
                self.assertFalse((out / 'local-origin.json').exists())
                self.assertEqual(list((self.checker / reuse.STORE_RELATIVE / 'entries').iterdir()), [])
        for calls in ([ValueError('support drift')], [{'unit_stub': 'no proof/support qualification'}, ValueError('post-support drift')]):
            with patch.object(gate.support, 'check', side_effect=calls):
                out = self.output(); self.assertEqual(gate.verify(self.request, out)['status'], 'refused')
            self.assertFalse((out / 'local-origin.json').exists())
        under = deepcopy(self.request); under['selections'][0]['budget_records'] = 0
        out = self.output(); self.assertEqual(gate.verify(under, out)['status'], 'refused')
        self.assertFalse((out / 'local-origin.json').exists())

    def test_pending_and_hint_never_commit_but_postcommit_is_established(self):
        install = reuse._install
        for boundary in ('before-hint', 'before-private', 'after-private'):
            with self.subTest(boundary=boundary):
                def interrupted(pending, final, raw, *, private):
                    if (boundary == 'before-hint' and not private) or (boundary == 'before-private' and private):
                        raise OSError('UNIT controlled precommit interruption')
                    install(pending, final, raw, private=private)
                    if boundary == 'after-private' and private:
                        raise OSError('UNIT controlled transport interruption')
                with patch.object(reuse, '_install', side_effect=interrupted):
                    out = self.output(); result = gate.verify(self.request, out)
                self.assertEqual(result['status'], 'incomplete')
                if not (out / 'local-origin.json').exists():
                    origin, _ = reuse._origin(); body = reuse.binding(out, 'cold', origin[0], origin[1])
                    reuse.publish_hint(out, origin[0]['origin_id'], reuse.sha(reuse.canonical(body)), 'cold')
                self.process.reset_mock(); replay = gate.check_evidence(out, self.output())
                self.assertEqual(replay['status'], 'verified', replay.get('reason'))
                self.assertEqual(self.process.call_count, 0 if boundary == 'after-private' else 9)
                self.assertEqual(list((self.checker / reuse.STORE_RELATIVE / 'pending').iterdir()), [])

    def test_bad_seal_or_key_refuses_and_missing_key_cold_falls_back(self):
        old, _ = self.cold(); store = self.checker / reuse.STORE_RELATIVE
        hint = reuse.decode((old / 'local-origin.json').read_bytes()); entry = store / 'entries' / (hint['entry_id'] + '.json')
        original = entry.read_bytes(); value = reuse.decode(original); value['hmac_sha256'] = '0' * 64; entry.write_bytes(reuse.canonical(value))
        self.assertEqual(gate.check_evidence(old, self.output())['status'], 'refused'); entry.write_bytes(original)
        key = store / 'origin.key'; raw = key.read_bytes(); key.write_bytes(b'0' * 32)
        self.assertEqual(gate.check_evidence(old, self.output())['status'], 'refused'); key.write_bytes(raw)
        key.unlink(); self.process.reset_mock()
        self.assertEqual(gate.check_evidence(old, self.output())['status'], 'verified'); self.assertEqual(self.process.call_count, 9)
        self.assertFalse(key.exists())

    def test_duplicate_nonfinite_and_immutable_entry_controls(self):
        for raw in (b'{"a":1,"a":2}', b'{"a":NaN}', b'{"a":1e999}'):
            with self.assertRaises(reuse.OriginError): reuse.decode(raw)
        old, _ = self.cold(); origin, _ = reuse._origin()
        entry_id = reuse._establish(old, origin)
        entry = self.checker / reuse.STORE_RELATIVE / 'entries' / (entry_id + '.json')
        entry.write_bytes(b'controlled conflicting existing entry')
        with self.assertRaises(reuse.OriginError): reuse._establish(old, origin)
        self.assertEqual(entry.read_bytes(), b'controlled conflicting existing entry')
        with self.assertRaises(FileExistsError): reuse.init_origin()

    def test_ordinary_paths_never_read_or_retain_origin_material(self):
        secret = self.checker / reuse.STORE_RELATIVE / 'origin.key'
        request = deepcopy(self.request); request['input']['path'] = str(secret)
        out = self.output()
        with patch.object(reuse, '_read_regular', side_effect=AssertionError('protected bytes acquired')):
            self.assertEqual(gate.verify(request, out)['status'], 'refused')
            self.assertEqual(gate.check_evidence(secret.parent, self.output())['status'], 'refused')
            with patch.object(sys, 'argv', ['formal_gate.py', 'verify', '--request', str(secret), '--output', str(self.output())]):
                with self.assertRaises(reuse.OriginError): gate.main()
        self.assertFalse(out.exists())
        for destination in (secret, secret.parent / 'output', self.checker):
            self.assertEqual(gate.verify(self.request, destination)['status'], 'refused')
        alias = self.root / 'hardlink.json'; os.link(secret, alias)
        request['input']['path'] = str(alias)
        self.assertEqual(gate.verify(request, self.output())['status'], 'refused'); alias.unlink()
        alias = self.root / 'alias'; alias.symlink_to(secret.parent, target_is_directory=True)
        request['input']['path'] = str(alias / 'origin.key')
        self.assertEqual(gate.verify(request, self.output())['status'], 'refused')

    def test_current_correspondence_and_final_support_are_not_skipped(self):
        old, _ = self.cold(); self.process.reset_mock()
        with patch.object(gate, 'model_output', return_value={'changed': True}):
            self.assertEqual(gate.check_evidence(old, self.output())['status'], 'refused')
        with patch.object(gate.support, 'check', side_effect=[{'unit_stub': 'no proof/support qualification'}, ValueError('late drift')]):
            self.assertEqual(gate.check_evidence(old, self.output())['status'], 'refused')
        self.process.assert_not_called()

    def test_missing_hint_never_uses_saved_status_or_objects(self):
        old, _ = self.cold()
        (old / 'local-origin.json').unlink()
        (old / 'GateModel.olean').write_bytes(b'caller-forged proof object')
        self.refresh(old)
        self.process.reset_mock(); out = self.output()
        result = gate.check_evidence(old, out)
        self.assertEqual(result['status'], 'verified', result.get('reason'))
        self.assertEqual(self.process.call_count, 9)
        self.assertNotEqual((out / 'GateModel.olean').read_bytes(), (old / 'GateModel.olean').read_bytes())
        self.assertNotEqual(result['observations']['reuse'], 'local-origin')

    def test_distinct_failures_and_final_source_drift_cannot_establish(self):
        for status, change in (('unsupported', lambda r: r.update(schema='future/99')),
                               ('refused', lambda r: r.update(origin={'key': 'caller-selected'}))):
            request = deepcopy(self.request); change(request)
            out = self.output(); result = gate.verify(request, out)
            self.assertEqual(result['status'], status); self.assertFalse(out.exists())
        out = self.output()
        with patch.object(gate, 'runtime_identity', side_effect=[self.identity(), {'changed': True}]):
            result = gate.verify(self.request, out)
        self.assertEqual(result['status'], 'refused'); self.assertFalse((out / 'local-origin.json').exists())
        with patch.object(gate.support, 'check', side_effect=FileNotFoundError('unit support unavailable')):
            self.assertEqual(gate.verify(self.request, self.output())['status'], 'incomplete')
        self.assertEqual(list((self.checker / reuse.STORE_RELATIVE / 'entries').iterdir()), [])

    def test_flat_helper_namespace_is_still_exact_with_reuse_helper(self):
        scripts = self.checker / 'scripts'; scripts.mkdir()
        for name in gate.SCRIPT_FILES:(scripts / name).write_bytes(b'# unit namespace only')
        gate._script_namespace()
        self.assertIn('formal_reuse.py', gate.SCRIPT_FILES)
        (scripts / 'unselected.py').write_bytes(b'# never imported')
        with self.assertRaises(gate.ScriptNamespaceError):gate._script_namespace()

    def test_case_aliases_refuse_before_read_and_output_creation(self):
        secret = self.checker / reuse.STORE_RELATIVE / 'origin.key'
        aliases = [Path(str(secret).replace('/.cache/', '/.CACHE/')),
                   self.checker.with_name(self.checker.name.upper()) / reuse.STORE_RELATIVE / 'origin.key']
        if not all(path.exists() and path.samefile(secret) for path in aliases):
            self.skipTest('selected filesystem has no case aliases; absent reserved suffix still separately tested')
        with patch.object(reuse, '_read_regular', side_effect=AssertionError('case alias acquired protected bytes')):
            for alias in aliases:
                request = deepcopy(self.request); request['input']['path'] = str(alias)
                self.assertEqual(gate.verify(request, self.output())['status'], 'refused')
                self.assertEqual(gate.check_evidence(alias.parent, self.output())['status'], 'refused')
                with self.assertRaises(reuse.OriginError):reuse.guard(alias.parent / 'new-output', output=True)
            with self.assertRaises(reuse.OriginError):reuse.guard(self.checker.with_name(self.checker.name.upper()), output=True)
        old, _ = self.cold()
        overlapping = old.with_name(old.name.upper()) / 'new-output'
        self.assertEqual(gate.check_evidence(old, overlapping)['status'], 'refused')
        self.assertFalse(overlapping.exists())

    def test_absent_origin_suffix_is_reserved_before_setup(self):
        checker = self.root / 'unselected-checker'; checker.mkdir()
        with patch.object(reuse, 'ROOT', checker):
            for suffix in ('.cache/formal-origin-v1/out', '.CACHE/FORMAL-ORIGIN-V1/out'):
                with self.assertRaises(reuse.OriginError):reuse.guard(checker / suffix, output=True)
        self.assertEqual(list(checker.iterdir()), [])

    def test_malformed_retained_original_result_refuses_with_four_state_api(self):
        old, _ = self.cold(); out = self.output()
        self.assertEqual(gate.check_evidence(old, out)['status'], 'verified')
        for value in (None, [], 1, 'verified'):
            changed = self.output(); shutil.copytree(out, changed)
            (changed / 'origin-result.json').write_bytes(reuse.canonical(value)); self.refresh(changed)
            result = gate.check_evidence(changed, self.output())
            self.assertEqual(result['status'], 'refused', result)

    def test_setup_material_is_owner_only_and_ordinary_calls_do_not_repair_it(self):
        store = self.checker / reuse.STORE_RELATIVE
        for path in (store, store / 'entries', store / 'pending', store / 'origin.key', store / 'selection.json'):
            self.assertEqual(path.stat().st_mode & 0o077, 0)
        key = store / 'origin.key'; key.chmod(0o644)
        with self.assertRaises(reuse.OriginError):reuse._origin()
        self.assertEqual(key.stat().st_mode & 0o077, 0o044)


if __name__ == '__main__':
    unittest.main()
