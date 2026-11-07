"""Native305 byte transport accepts empty members without weakening integrity."""
from pathlib import Path
import copy
import hashlib
import json
import subprocess
import unittest
from unittest.mock import patch

import test_ac_support_native305 as native

c = native.c


class EmptyNativeMembersTests(unittest.TestCase):
    setUp = native.Native305PublicTests.setUp
    tearDown = native.Native305PublicTests.tearDown
    _select_policy = native.Native305PublicTests._select_policy
    bind_manifest = native.Native305PublicTests.bind_manifest

    def empty_member(self):
        relative = 'documentation/empty-proof.log'
        target = self.installation / 'standards' / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b'')
        self.manifest['standards']['members'].append({'path': relative, 'sha256': hashlib.sha256(b'').hexdigest()})
        self.manifest['standards']['member_count'] += 1
        definition = json.loads((self.f.workspace / 'Product.json').read_bytes())
        definition['product'] = {'definition_id': self.f.policy['product']['definition_id']}
        self.f.definition = self.f.write('Product.json', definition)
        self.f.policy['product']['definition'] = self.f.definition
        self.bind_manifest()
        return target

    @staticmethod
    def tree(root):
        if not root.exists():
            return None
        return {p.relative_to(root).as_posix(): p.read_bytes() if p.is_file() else None for p in root.rglob('*')}

    def command(self, label, argv, *, stdin=None):
        self.sequence += 1
        directory = self.root / 'calls' / (str(self.sequence).zfill(3) + '-' + label)
        directory.mkdir(parents=True)
        result = subprocess.run([str(x) for x in argv], cwd=self.root, input=stdin, capture_output=True, timeout=30)
        (directory / 'stdout.bin').write_bytes(result.stdout)
        (directory / 'stderr.bin').write_bytes(result.stderr)
        (directory / 'execution.json').write_bytes(c.canonical({'argv': [str(x) for x in argv], 'returncode': result.returncode}))
        if stdin is not None:
            (directory / 'stdin.bin').write_bytes(stdin)
        return result

    def public_startup(self):
        request = self.root / ('request-' + str(self.sequence) + '.json')
        request.write_bytes(c.canonical({'schema': c.REQUEST, 'id': 'empty-member-startup', 'operation': 'tools.describe', 'arguments': {}}))
        result = self.command('startup', [self.python, '-B', self.code / 'ac_support.py', '--policy', self.policy_path,
            '--policy-sha256', self.policy_sha, '--principal', 'executive', 'call', '--request', request])
        return result, json.loads(result.stdout)

    def test_empty_member_public_startup_and_initializer(self):
        self.empty_member()
        before = self.tree(self.installation)
        result, response = self.public_startup()
        self.assertEqual(result.returncode, 0, response)
        self.assertEqual(response['status'], 'ok')
        # This unit fixture supplies a declared manager response; the retained
        # complete-A1 integration witness separately uses the actual manager.
        manager = self.root / 'fixture-manager'
        manager.write_text('#!' + str(self.python) + '\nimport json\nfrom pathlib import Path\n'
            + 'p=Path(' + repr(str(self.f.workspace / 'Product.json')) + ')\nv=json.loads(p.read_bytes())\n'
            + 'print(json.dumps({"basis":v["constitution"]["stdo"]["basis"]["uri"],'
            + '"manifest_sha256":v["constitution"]["stdo"]["basis"]["manifest_sha256"],'
            + '"definition_id":v["product"]["definition_id"],"valid":True,"installed":True,"failures":[],"path":'
            + repr(str(self.installation)) + '}))\n')
        manager.chmod(0o755)
        output = self.root / 'initialized'
        initialized = self.command('initializer', [self.python, '-B', self.code.parent / 'examples/fd-support/prepare_readonly.py',
            '--out', output, '--profile', 'stdo-3.0.5', '--product-root', self.f.workspace,
            '--definition-name', 'Product.json', '--method-installation', self.installation, '--stdo', manager])
        self.assertEqual(initialized.returncode, 0, initialized.stderr.decode())
        setup = json.loads(initialized.stdout)
        served = self.command('mcp', [self.python, '-B', self.code / 'ac_support.py', '--policy', output / 'policy.json',
            '--policy-sha256', setup['policy_sha256'], '--principal', 'executive', 'mcp'], stdin=(output / 'mcp-session.jsonl').read_bytes())
        self.assertEqual(served.returncode, 0, served.stderr.decode())
        responses = [json.loads(line) for line in served.stdout.splitlines()]
        self.assertEqual([value['id'] for value in responses], [1, 2, 3])
        self.assertEqual(responses[-1]['result']['structuredContent']['status'], 'ok')
        self.assertEqual(self.tree(self.installation), before)

    def test_empty_member_integrity_and_population_refuse_before_effects(self):
        target = self.empty_member()
        valid = copy.deepcopy(self.manifest)
        for variant in ('changed_digest', 'changed_bytes', 'omitted', 'extra'):
            with self.subTest(variant=variant):
                self.manifest = copy.deepcopy(valid)
                target.write_bytes(b'')
                extra = self.installation / 'standards/unselected-empty.log'
                if extra.exists(): extra.unlink()
                if variant == 'changed_digest': self.manifest['standards']['members'][-1]['sha256'] = '0' * 64
                elif variant == 'changed_bytes': target.write_bytes(b'changed')
                elif variant == 'omitted': target.unlink()
                else: extra.write_bytes(b'')
                self.bind_manifest()
                native_before = self.tree(self.installation)
                evidence = Path(self.f.policy['evidence_root'])
                evidence_before = self.tree(evidence)
                result, response = self.public_startup()
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(response['status'], 'refused', response)
                self.assertIn(response['refusal']['code'], ('digest_mismatch', 'basis_stale'))
                self.assertIsNone(response['evidence'])
                self.assertEqual(self.tree(self.installation), native_before)
                self.assertEqual(self.tree(evidence), evidence_before)

    def test_encoded_member_response_is_strict_at_internal_boundary(self):
        target = self.empty_member()
        actual_read = c.read_source
        # Filesystem read_source always creates valid base64. These are explicit
        # internal fault injections, not caller-reachable encoded responses.
        for encoded in (None, 7, b'', [], '!', 'a', '\n', 'é'):
            with self.subTest(encoded=encoded):
                def injected(runtime, reference):
                    value = actual_read(runtime, reference)
                    if reference['path'] == target.relative_to(self.installation).as_posix():
                        value['content_base64'] = encoded
                    return value
                with patch.object(c, 'read_source', side_effect=injected):
                    with self.assertRaises(c.SupportError) as caught:
                        c.Runtime.from_policy(self.policy_path, self.policy_sha, 'executive')
                    self.assertEqual(caught.exception.code, 'contract_violation')
        with self.assertRaises(c.SupportError):
            c.text('')


if __name__ == '__main__':
    unittest.main()
