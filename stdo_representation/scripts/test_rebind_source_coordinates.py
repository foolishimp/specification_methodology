"""Closed coordinate policy against the actual preserved authored model."""
import copy
import json
from pathlib import Path
import unittest
import rebind_source_coordinates as rebind

ROOT = Path(__file__).resolve().parents[1]
OLD = 'build_tenants/a_c/representation/stdo-v3.0.5/source/'
NEW = 'build_tenants/a_c/representation/stdo-v3.0.5-rc.1/source/'


class CoordinateRebindTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = json.loads((ROOT / OLD / '../model.json').read_bytes())
        cls.current = json.loads((ROOT / NEW / '../model.json').read_bytes())
        cls.inventory = json.loads((ROOT / NEW / '../source-inventory.json').read_bytes())
        cls.freeze = json.loads((ROOT / NEW / '../source-freeze.json').read_bytes())

    def test_exact_current_transform_and_unchanged_record_order(self):
        ledger, identity = rebind.verify_transform(self.original, self.current, OLD, NEW, self.inventory, self.freeze['source_identity_sha256'])
        self.assertEqual(len(ledger), 9292)
        self.assertEqual(self.current['id'], 'urn:a-c:coordinate-rebind:model:' + identity)
        for family in self.original['populations']:
            self.assertEqual([r['id'] for r in self.original['populations'][family]], [r['id'] for r in self.current['populations'][family]])
        self.assertEqual(self.current['basis']['calculus'], self.original['basis']['calculus'])
        for field in ('authority', 'interpreter', 'provenance'):
            self.assertEqual(self.current['interpretation'][field], self.original['interpretation'][field])

    def test_extra_semantic_change_is_not_an_allowed_rebind(self):
        for variant in ('statement', 'edge', 'residual'):
            with self.subTest(variant=variant):
                changed = copy.deepcopy(self.current)
                if variant == 'statement':
                    changed['populations']['constraints'][0]['predicate']['statement'] += ' changed obligation'
                elif variant == 'edge':
                    changed['populations']['relations'][0]['target'] = changed['populations']['objects'][0]['id']
                else:
                    changed['populations']['residuals'][0]['uncertainty']['statement'] += ' erased uncertainty'
                with self.assertRaisesRegex(ValueError, 'permitted coordinate transform'):
                    rebind.verify_transform(self.original, changed, OLD, NEW, self.inventory, self.freeze['source_identity_sha256'])

    def test_missing_mapping_and_dangling_grounding_refuse(self):
        for variant in ('missing', 'dangling'):
            with self.subTest(variant=variant):
                changed = copy.deepcopy(self.current)
                ground = changed['populations']['constraints'][0]['predicate']['grounding'][0]
                if variant == 'missing':
                    ground['section'] = self.original['populations']['constraints'][0]['predicate']['grounding'][0]['section']
                else:
                    ground['section'] += '-unbound'
                with self.assertRaises(ValueError):
                    rebind.verify_transform(self.original, changed, OLD, NEW, self.inventory, self.freeze['source_identity_sha256'])
        broken = copy.deepcopy(self.original)
        broken['populations']['constraints'][0]['predicate']['grounding'][0]['section'] += '-unbound'
        with self.assertRaisesRegex(ValueError, 'unbound source section'):
            rebind.transform(broken, OLD, NEW, self.inventory, self.freeze['source_identity_sha256'])

    def test_no_version_substitution_in_authored_statement(self):
        changed = copy.deepcopy(self.original)
        changed['populations']['constraints'][0]['predicate']['statement'] += OLD
        with self.assertRaisesRegex(ValueError, 'outside declared coordinate'):
            rebind.transform(changed, OLD, NEW, self.inventory, self.freeze['source_identity_sha256'])

    def test_numeric_and_boolean_type_changes_are_not_equal_coordinates(self):
        for variant in ('float', 'boolean'):
            with self.subTest(variant=variant):
                changed = copy.deepcopy(self.current)
                ground = changed['populations']['constraints'][0]['predicate']['grounding'][0]
                ground['start_line'] = float(ground['start_line']) if variant == 'float' else True
                with self.assertRaisesRegex(ValueError, 'permitted coordinate transform'):
                    rebind.verify_transform(self.original, changed, OLD, NEW, self.inventory, self.freeze['source_identity_sha256'])


if __name__ == '__main__':
    unittest.main()
