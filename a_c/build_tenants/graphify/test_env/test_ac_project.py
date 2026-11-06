"""Public project workflow controls; fixture authoring is not LLM-quality evidence."""
import copy
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))
import ac_project as project
import ac_generate as gen
import ac_graph
from test_ac_generate import SOURCE, fixture_answer


class ProjectBuildTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name).resolve()
        self.subject = self.root / "user project"
        self.subject.mkdir()
        self.source = self.subject / "specification"
        self.source.mkdir()
        (self.source / "RULES.md").write_text(SOURCE)
        self.definition = self.subject / "stdo_sample.json"
        self.product = {"kind": "stdo.product-definition", "product": {
            "definition_id": "urn:example:project", "name": "User project", "source_project": "./"},
            "constitution": {"stdo": {"basis": {"uri": "stdo://releases/v3.0.2/", "manifest_sha256": "a" * 64}}},
            "what": {"intent": "specification/RULES.md", "product": "specification/RULES.md", "specification": ["specification"]}}
        gen.save(self.definition, self.product)
        self.run = self.root / "representation"
        self.manager = patch.object(project, "verify_definition", side_effect=lambda p, m, checker=None:
                                    (gen._decode(project.regular(p, checker)), {"valid": True, "test_fixture": True}))
        self.manager.start()

    def tearDown(self):
        self.manager.stop()
        self.tmp.cleanup()

    def prepare(self, **kwargs):
        return project.prepare(self.subject, self.definition, self.run, **kwargs)

    def answer(self):
        chunk = gen.load(self.run / "generation/chunks.json")[0]
        path = self.run / "host-answer.json"
        gen.save(path, fixture_answer(chunk))
        return chunk, path

    def complete(self):
        self.prepare()
        chunk, path = self.answer()
        project.submit(self.run, chunk['id'], path, 'controlled-fixture-author')
        return project.build(self.run)

    def test_new_project_full_path_and_matching_reuse(self):
        before = (self.source / 'RULES.md').read_bytes()
        definition_before = self.definition.read_bytes()
        prepared = self.prepare()
        self.assertEqual(prepared['source_files'], 1)
        task = project.task(self.run)
        self.assertEqual(task['status'], 'authoring_required')
        self.assertIn('SOURCE_DATA_JSON', task['prompt'])
        self.assertIn('host-session', task['prompt'])
        chunk, path = self.answer()
        submitted = project.submit(self.run, chunk['id'], path, 'controlled-fixture-author')
        self.assertEqual(submitted['status'], 'submitted')
        self.assertEqual(project.submit(self.run, chunk['id'], path, 'controlled-fixture-author')['status'], 'already_submitted')
        self.assertEqual(project.task(self.run), {'status': 'ready_to_build'})
        built = project.build(self.run)
        self.assertEqual(built['status'], 'built')
        self.assertEqual(built['method'], self.product['constitution']['stdo']['basis'])
        self.assertEqual(self.definition.read_bytes(), definition_before)
        self.assertEqual(built['formal_gate']['status'], 'not_performed')
        model = gen.load(Path(built['artifacts']['model']))
        carrier = gen.load(Path(built['artifacts']['carrier']))
        self.assertEqual(ac_graph.decode(ac_graph.GraphCarrier(carrier)).document, model)
        self.assertIn('User project', Path(built['artifacts']['explorer']).read_text())
        page = Path(built['artifacts']['explorer']).read_text()
        self.assertIn('data-renderer="unified"', page)
        self.assertIn('id="mode-layered"', page)
        self.assertEqual(page.count('<script id="explorer-data"'), 1)
        self.assertNotIn('layered', built['artifacts'])
        self.assertEqual(project.build(self.run)['status'], 'reused')
        self.assertEqual(project.status(self.run)['status'], 'built')
        self.assertEqual((self.source / 'RULES.md').read_bytes(), before)

    def test_explicit_coherent_transaction_retains_full_source_and_public_build(self):
        # A bounded fixture exceeds the prior 500k cap. This tests mechanics,
        # not whether an LLM can acquire or faithfully interpret this corpus.
        source = SOURCE + ("Retained fixture context.\n" * 25000)
        self.assertGreater(len(source), 500_000)
        (self.source / 'RULES.md').write_text(source)
        self.prepare(chunk_chars=3_000_000)
        chunks = gen.load(self.run / 'generation/chunks.json')
        self.assertEqual(len(chunks), 1)
        task = project.task(self.run)
        self.assertIn(source.splitlines()[-1], task['prompt'])
        chunk, path = self.answer()
        project.submit(self.run, chunk['id'], path, 'controlled-large-transaction-fixture')
        built = project.build(self.run)
        self.assertEqual(built['status'], 'built')
        self.assertEqual(project.status(self.run)['status'], 'built')
        self.assertEqual((self.run / 'generation/corpus/specification/RULES.md').read_text(), source)
        self.assertEqual(gen.load(self.run / 'generation/plan.json')['chunk_chars'], 3_000_000)

    def test_transaction_envelope_over_limit_is_refused(self):
        with self.assertRaisesRegex(gen.GenerationError, 'outside supported range'):
            self.prepare(chunk_chars=3_000_001)
        self.assertFalse((self.run / 'generation').exists())

    def test_missing_authoring_does_not_build(self):
        self.prepare()
        with self.assertRaisesRegex(gen.GenerationError, 'missing authored chunks'):
            project.build(self.run)
        self.assertFalse((self.run / 'BUILD.json').exists())

    def test_false_grounding_and_changed_submission_refuse(self):
        self.prepare()
        chunk, path = self.answer()
        good = gen.load(path)
        bad = copy.deepcopy(good)
        bad['constraints'][0]['grounding'][0]['quote'] = 'invented quotation'
        gen.save(path, bad)
        with self.assertRaisesRegex(gen.GenerationError, 'grounding quote'):
            project.submit(self.run, chunk['id'], path, 'fixture')
        self.assertFalse((self.run / 'answers').exists())
        gen.save(path, good)
        project.submit(self.run, chunk['id'], path, 'fixture')
        good['limitations'].append('Changed interpretation')
        gen.save(path, good)
        with self.assertRaisesRegex(gen.GenerationError, 'submission exists'):
            project.submit(self.run, chunk['id'], path, 'fixture')

    def test_source_content_and_membership_invalidate(self):
        self.prepare()
        added = self.source / 'NEW.md'
        added.write_text('New obligation\n')
        with self.assertRaisesRegex(gen.GenerationError, 'selected source changed'):
            project.task(self.run)
        added.unlink()
        (self.source / 'RULES.md').write_text(SOURCE + 'Changed.\n')
        with self.assertRaisesRegex(gen.GenerationError, 'selected source changed'):
            project.build(self.run)

    def test_definition_and_machinery_invalidate(self):
        self.prepare()
        saved = self.definition.read_bytes()
        self.definition.write_bytes(saved + b'\n')
        with self.assertRaisesRegex(gen.GenerationError, 'definition changed'):
            project.status(self.run)
        self.definition.write_bytes(saved)
        with patch.object(project, 'machinery', return_value={}):
            with self.assertRaisesRegex(gen.GenerationError, 'machinery changed'):
                project.status(self.run)

    def test_output_inside_source_and_existing_run_refuse(self):
        with self.assertRaisesRegex(gen.GenerationError, 'inside a selected source tree'):
            project.prepare(self.subject, self.definition, self.source / 'output')
        self.prepare()
        with self.assertRaisesRegex(gen.GenerationError, 'already exists'):
            self.prepare()

    def test_escape_and_symlink_sources_refuse(self):
        with self.assertRaises(gen.GenerationError):
            self.prepare(selections=['../outside'])
        (self.subject / 'alias.md').symlink_to(self.source / 'RULES.md')
        with self.assertRaisesRegex(gen.GenerationError, 'symlink'):
            self.prepare(selections=['alias.md'])

    def test_built_document_tamper_and_missing_member_refuse(self):
        built = self.complete()
        page = Path(built['artifacts']['explorer'])
        page.write_bytes(page.read_bytes() + b'changed')
        with self.assertRaisesRegex(gen.GenerationError, 'artifact changed'):
            project.build(self.run)
        page.unlink()
        with self.assertRaisesRegex(gen.GenerationError, 'inventory changed'):
            project.status(self.run)

    def test_refreshed_submission_digest_does_not_reuse_old_model(self):
        self.complete()
        path = next((self.run / 'answers').glob('*.json'))
        receipt = gen.load(path)
        receipt['answer']['limitations'].append('Changed')
        receipt['answer_sha256'] = gen.digest(receipt['answer'])
        gen.save(path, receipt)
        with self.assertRaisesRegex(gen.GenerationError, 'authored submissions'):
            project.build(self.run)

    def test_partial_output_is_preserved(self):
        self.prepare()
        chunk, path = self.answer()
        project.submit(self.run, chunk['id'], path, 'fixture')
        folder = self.run / 'generation/proposal'
        folder.mkdir()
        (folder / 'partial.txt').write_text('retain')
        with self.assertRaisesRegex(gen.GenerationError, 'already exists'):
            project.build(self.run)
        self.assertEqual((folder / 'partial.txt').read_text(), 'retain')

    def test_trailing_directory_and_nested_definition_use_declared_source(self):
        nested = self.subject / 'governance'
        nested.mkdir()
        (nested / 'specification').mkdir()
        (nested / 'specification/RULES.md').write_text(SOURCE + 'A nested source.\n')
        product = copy.deepcopy(self.product)
        product['product']['source_project'] = '../'
        product['what']['specification'] = ['./specification/']
        self.definition = nested / 'stdo_sample.json'
        gen.save(self.definition, product)
        self.prepare()
        record = gen.load(self.run / 'PROJECT.json')
        self.assertEqual([row['path'] for row in record['files']], ['governance/specification/RULES.md'])
        self.assertEqual((self.run / 'generation/corpus/governance/specification/RULES.md').read_text(), SOURCE + 'A nested source.\n')

    def test_wrong_source_project_refuses(self):
        self.product['product']['source_project'] = '../'
        gen.save(self.definition, self.product)
        with self.assertRaisesRegex(gen.GenerationError, 'source_project differs'):
            self.prepare()

    def test_build_metadata_cannot_invent_method_source_or_formal_verdict(self):
        self.complete()
        path = self.run / 'BUILD.json'
        original = gen.load(path)
        for field, value in [('method', {'uri': 'stdo://releases/v3.0.99/'}),
                             ('source_manifest_sha256', '0' * 64),
                             ('formal_gate', {'required': True, 'status': 'verified', 'runs': []})]:
            changed = copy.deepcopy(original)
            changed[field] = value
            gen.save(path, changed)
            with self.subTest(field=field), self.assertRaises(gen.GenerationError):
                project.status(self.run)
        gen.save(path, original)
        self.assertEqual(project.status(self.run)['status'], 'built')

    @unittest.skipUnless(os.environ.get('AC_GRAPHIFY_UPSTREAM'), 'pinned upstream required for actual boundary trial')
    def test_actual_graphify_project_path(self):
        self.prepare(mode='graphify-ac', upstream=os.environ['AC_GRAPHIFY_UPSTREAM'])
        self.assertIn('GRAPHIFY_DISCOVERY_DATA_JSON', project.task(self.run)['prompt'])
        chunk, path = self.answer()
        project.submit(self.run, chunk['id'], path, 'controlled-upstream-fixture')
        result = project.build(self.run)
        self.assertEqual(result['mode'], 'graphify-ac')
        self.assertEqual(result['upstream_trial']['commit'], gen.UPSTREAM_COMMIT)
        self.assertEqual(project.build(self.run)['status'], 'reused')


if __name__ == '__main__':
    unittest.main()
