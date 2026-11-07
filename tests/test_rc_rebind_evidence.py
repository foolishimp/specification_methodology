"""The real RC coordinate consumer accepts its actual run, not arbitrary edits."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import check_stack_release as api
import rc_rebind_evidence as rebind
import stable_release_evidence as evidence

INPUTS = ROOT / 'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET/release-tools/rebind-adapter-001/ACTUAL.json'


class RebindEvidenceTests(unittest.TestCase):
    def setUp(self):
        selected = json.loads(INPUTS.read_bytes())
        self.manifest = selected['manifest']
        self.record = json.loads((ROOT / selected['record']['path']).read_bytes())
        self.view = api.View(ROOT)

    @property
    def facts(self):
        return self.manifest['components']['representation']['facts']

    def check(self):
        evidence.representation(self.view, self.record, 'source_current_model', self.manifest, api)

    def test_actual_recorded_rebind_and_current_provider_outputs_pass(self):
        self.check()

    def test_arbitrary_predecessor_cannot_borrow_published_assessment(self):
        self.facts['rebind']['predecessor_manifest'] = self.facts['model']
        with self.assertRaisesRegex(ValueError, 'original published cohort'):
            self.check()

    def test_unselected_prefix_refuses(self):
        self.facts['rebind']['new_source_prefix'] = 'another-source/'
        with self.assertRaisesRegex(ValueError, 'unselected source-coordinate'):
            self.check()

    def test_source_copy_mode_change_refuses(self):
        original = api.git
        def changed(root, *args, **kwargs):
            result = original(root, *args, **kwargs)
            if args[:3] == ('ls-tree', '-r', rebind.PREDECESSOR_CARRIER):
                return SimpleNamespace(stdout=result.stdout.replace('100644 ', '100755 ', 1))
            return result
        with patch.object(api, 'git', changed), self.assertRaisesRegex(ValueError, 'source copy modes'):
            self.check()

    def test_normative_source_delta_refuses_even_with_rehashed_selection(self):
        old_read = self.view.read_bytes
        name = self.manifest['source']['path']
        source = json.loads(old_read(name)); source['members'][0]['sha256'] = 'f' * 64
        raw = api.canonical_json_bytes(source)
        self.manifest['source'].update(sha256=api.sha256(raw), bytes=len(raw))
        with patch.object(self.view, 'read_bytes', side_effect=lambda p: raw if p == name else old_read(p)):
            with self.assertRaisesRegex(ValueError, 'normative source population'):
                self.check()

    def test_coherently_rehashed_semantic_edit_and_open_ledger_refuse(self):
        # These are deliberately counterfactual receipts in a disposable test
        # directory. Original observed files and current model never change.
        for edit in ('residual', 'ledger'):
            with self.subTest(edit=edit), tempfile.TemporaryDirectory(prefix='control-', dir=INPUTS.parent) as temporary:
                self.setUp()
                directory = Path(temporary)
                def put(name, value):
                    raw = api.canonical_json_bytes(value); p = directory / name; p.write_bytes(raw)
                    return {'path': p.relative_to(ROOT).as_posix(), 'sha256': api.sha256(raw), 'bytes': len(raw)}
                def replace(old, new):
                    run = self.record['execution']
                    run['argv'] = [str(ROOT / new['path']) if arg == str(ROOT / old['path']) else arg for arg in run['argv']]
                    for key in ('inputs', 'outputs'):
                        run[key] = [new if row['path'] == old['path'] else row for row in run[key]]
                selected = self.facts['rebind']
                report = json.loads((ROOT / selected['report']['path']).read_bytes())
                if edit == 'residual':
                    model = json.loads((ROOT / self.facts['model']['path']).read_bytes())
                    model['populations']['residuals'][0]['consequence'] += ' Unsupported changed meaning.'
                    model_ref = put('model.json', model)
                    replace(selected['emitted_model'], model_ref)
                    self.facts.update(model=model_ref, model_sha256=model_ref['sha256'], model_canonical_sha256=api.canonical_value_sha256(model))
                    selected['emitted_model'] = model_ref
                    report['current_model'].update(sha256=self.facts['model_canonical_sha256'], raw_sha256=model_ref['sha256'])
                else:
                    report['coordinates'].append({'path': '/populations/residuals/0/consequence', 'old': 'meaning', 'new': 'changed'})
                report_ref = put('report.json', report); replace(selected['report'], report_ref); selected['report'] = report_ref
                result = {key: report[key] for key in ('kind', 'status', 'current_model', 'coordinate_map_sha256', 'source_members_equal', 'inverse_equal')}
                result_ref = put('result.json', result); replace(self.record['result'], result_ref)
                self.record['result'] = result_ref; self.record['execution']['stdout'] = result_ref
                with self.assertRaisesRegex(ValueError, 'reproduced closed coordinate transform'):
                    self.check()


if __name__ == '__main__':
    unittest.main()
