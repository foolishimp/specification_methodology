"""Generator inconsistency must retain an incomplete result before proof effects."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import formal_gate as gate


class GateCodegenTests(unittest.TestCase):
    def test_later_parent_in_internal_trace_is_retained_as_incomplete(self):
        model = gate.bridge.load_checked(gate.bridge.TOY_FIXTURE_DIR / 'MODEL.json')
        imported = gate.bridge.import_model(model)
        edges = {tuple(edge) for edge in imported['edges']}
        # Use a real reachable child that requires a previously discovered
        # parent. Only the internal producer's discovery order is corrupted.
        for seed in range(len(imported['records'])):
            certificate = gate.bridge.closure_certificate(imported, [seed])
            child = next((x for x in certificate['order'] if (seed, x) not in edges), None)
            if child is not None:
                break
        self.assertIsNotNone(child)
        broken = deepcopy(certificate)
        broken['order'] = [child] + [x for x in certificate['order'] if x != child]
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            checker = temporary / 'checker'; checker.mkdir()
            source = temporary / 'model.json'
            source.write_bytes(gate.reuse.canonical(model))
            output = temporary / 'evidence'
            request = {'schema': 'a_c.formal-gate.request/1',
                       'input': {'format': 'model', 'path': str(source),
                                 'raw_sha256': hashlib.sha256(source.read_bytes()).hexdigest()},
                       'selections': [{'seeds': [imported['records'][seed]['record']['id']],
                                       'budget_records': None}],
                       'supplied_views': None, 'context_binding': None}
            with patch.object(gate, 'ROOT', checker), patch.object(gate.reuse, 'ROOT', checker), \
                 patch.object(gate, 'runtime_identity', return_value={'unit_control': 'no live origin'}), \
                 patch.object(gate.support, 'check', return_value={'unit_control': 'no proof support'}), \
                 patch.object(gate.bridge, 'closure_certificate', return_value=broken), \
                 patch.object(gate.runtime_process, 'run', side_effect=AssertionError('proof invoked')) as process:
                result = gate.verify(request, output)
            process.assert_not_called()
            self.assertEqual(result['status'], 'incomplete')
            self.assertIn('ValueError: Closure trace has no earlier parent', result['reason'])
            self.assertEqual(result['checked_claims'], [])
            self.assertEqual(json.loads((output / 'result.json').read_bytes()), result)
            self.assertEqual((output / 'input.json').read_bytes(), source.read_bytes())
            self.assertEqual(hashlib.sha256((output / 'manifest.json').read_bytes()).hexdigest(),
                             result['evidence']['manifest_sha256'])
            for name, digest in result['evidence']['members'].items():
                self.assertEqual(hashlib.sha256((output / name).read_bytes()).hexdigest(), digest)


if __name__ == '__main__':
    unittest.main()
