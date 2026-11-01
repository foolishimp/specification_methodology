"""Project-front-door origin controls; synthetic material, no Lean invocation."""
from contextlib import redirect_stderr
import io
import json
import os
from pathlib import Path
import unittest
from unittest.mock import patch

import test_ac_formal_gate as controls
import test_ac_formal_origin_paths as origin_controls
from test_ac_generate import SOURCE, fixture_answer
import ac_generate as gen
import ac_project as project

formal = gen.ac_formal_gate


class ProjectOriginControls(unittest.TestCase):
    identity = controls.FormalGateControls.identity
    retain_control = controls.FormalGateControls.retain_control
    secret = origin_controls.FormalOriginPathControls.secret
    no_secret_read = origin_controls.FormalOriginPathControls.no_secret_read

    def setUp(self):
        controls.FormalGateControls.setUp(self)
        self.source = self.root / 'specification/RULES.md'
        self.source.parent.mkdir()
        self.source.write_text(SOURCE)
        self.definition = self.root / 'stdo_subject.json'
        gen.save(self.definition, {'kind': 'stdo.product-definition', 'product': {
            'definition_id': 'urn:example:origin-control', 'name': 'Origin control', 'source_project': './'},
            'constitution': {'stdo': {'basis': {'uri': 'stdo://releases/v3.0.2/', 'manifest_sha256': 'a' * 64}}},
            'what': {'intent': 'specification/RULES.md', 'product': 'specification/RULES.md',
                     'specification': ['specification']}})
        self.manager = patch.object(project, 'verify_definition', side_effect=lambda p, m, checker=None:
                                    (gen._decode(project.regular(p, checker)), {'valid': True, 'test_fixture': True}))
        self.manager.start()
        self.addCleanup(self.manager.stop)

    def prepare(self, selected=True, **kwargs):
        run = self.root / ('run-' + str(len(list(self.root.glob('run-*')))))
        project.prepare(self.root, self.definition, run, formal_checker=self.config if selected else None, **kwargs)
        return run

    def answer(self, run):
        chunk = gen.load(run / 'generation/chunks.json')[0]
        answer = run / 'draft.json'
        gen.save(answer, fixture_answer(chunk))
        return chunk['id'], answer

    def test_selected_source_and_broad_directory_refuse_before_read_or_run_creation(self):
        secret = self.secret()
        for selections in ([str(secret.relative_to(self.root))], ['checker']):
            output = self.root / 'refused-source-run'
            with self.subTest(selections=selections), self.no_secret_read(secret):
                with self.assertRaisesRegex(formal.GateError, 'protected formal origin'):
                    project.prepare(self.root, self.definition, output, selections=selections, formal_checker=self.config)
            self.assertFalse(output.exists())

    def test_selected_output_refuses_before_definition_read_and_directory_creation(self):
        secret = self.secret()
        output = secret.parent / 'new-project-run'
        with patch.object(project, 'verify_definition', side_effect=AssertionError('definition acquired before output reservation')):
            with self.assertRaisesRegex(formal.GateError, 'protected formal origin'):
                project.prepare(self.root, self.definition, output, formal_checker=self.config)
        self.assertFalse(output.exists())
        # Reserve a missing origin as well as an already established one.
        parent = self.root / 'new-checker-parent'
        config = dict(self.config, root=str(parent / 'checker'))
        with self.assertRaisesRegex(formal.GateError, 'protected formal origin'):
            project.prepare(self.root, self.definition, parent, formal_checker=config)
        self.assertFalse(parent.exists())

    def test_selected_definition_refuses_before_its_bytes_or_manager_are_used(self):
        definition = self.secret().with_name('stdo_subject.json')
        definition.write_bytes(self.definition.read_bytes())
        with self.no_secret_read(definition), patch.object(project, 'verify_definition', side_effect=AssertionError('manager invoked')):
            with self.assertRaisesRegex(formal.GateError, 'protected formal origin'):
                project.prepare(self.root, definition, self.root / 'definition-run', formal_checker=self.config)
        self.assertFalse((self.root / 'definition-run').exists())

    def test_selected_prepare_task_submit_and_status_need_no_checker_execution(self):
        with patch.object(formal, 'current', side_effect=AssertionError('path inspection ran checker')):
            run = self.prepare()
            self.assertEqual(project.task(run)['status'], 'authoring_required')
            chunk, answer = self.answer(run)
            self.assertEqual(project.submit(run, chunk, answer, 'controlled-author')['status'], 'submitted')
            self.assertEqual(project.task(run), {'status': 'ready_to_build'})
            self.assertEqual(project.status(run)['status'], 'ready_to_build')

    def test_unselected_workflow_performs_no_origin_lookup(self):
        secret = self.secret()
        secret.write_text(SOURCE)
        with patch.object(formal, 'guard_path', side_effect=AssertionError('unselected operation consulted origin')):
            run = self.prepare(False, selections=[str(secret.relative_to(self.root))])
            self.assertEqual(project.task(run)['status'], 'authoring_required')
            chunk, answer = self.answer(run)
            self.assertEqual(project.submit(run, chunk, answer, 'controlled-author')['status'], 'submitted')
            self.assertEqual(project.build(run)['status'], 'built')
            self.assertEqual(project.build(run)['status'], 'reused')
            self.assertEqual(project.status(run)['status'], 'built')

    def test_resume_guards_project_metadata_and_original_source_before_read(self):
        secret = self.secret()
        for member in ('PROJECT.json', 'source-manifest.json', 'product-definition.json', 'original-definition', 'original-source'):
            run = self.prepare()
            target = (self.definition if member == 'original-definition' else self.source if member == 'original-source'
                      else run / member)
            original = target.read_bytes()
            target.unlink(); os.link(secret, target)
            try:
                for caller in (project.task, project.status, project.build):
                    with self.subTest(member=member, caller=caller.__name__), self.no_secret_read(secret):
                        with self.assertRaises(formal.GateError):
                            caller(run)
            finally:
                target.unlink(); target.write_bytes(original)

    def test_resume_refuses_a_protected_source_path_named_by_project_record(self):
        run = self.prepare()
        secret = self.secret()
        record = gen.load(run / 'PROJECT.json')
        record['selection'] = [str(secret.relative_to(self.root))]
        gen.save(run / 'PROJECT.json', record)
        with self.no_secret_read(secret), self.assertRaisesRegex(formal.GateError, 'protected formal origin'):
            project.status(run)

    def test_submission_guards_external_answer_and_retained_answer_before_read(self):
        run = self.prepare()
        chunk, answer = self.answer(run)
        protected = self.secret().with_name('answer.json')
        protected.write_bytes(answer.read_bytes())
        alias = self.root / 'answer-alias.json'; os.link(protected, alias)
        for source in (protected, alias):
            with self.subTest(source=source.name), self.no_secret_read(protected), self.assertRaises(formal.GateError):
                project.submit(run, chunk, source, 'controlled-author')
        self.assertFalse((run / 'answers').exists())
        alias.unlink()
        project.submit(run, chunk, answer, 'controlled-author')
        retained = run / 'answers' / (chunk + '.json')
        retained.unlink(); os.link(protected, retained)
        with self.no_secret_read(protected), self.assertRaises(formal.GateError):
            project.status(run)

    def test_completed_status_guards_build_receipt_before_read(self):
        run = self.prepare()
        chunk, answer = self.answer(run)
        project.submit(run, chunk, answer, 'controlled-author')
        secret = self.secret()
        os.link(secret, run / 'BUILD.json')
        with self.no_secret_read(secret), self.assertRaises(formal.GateError):
            project.status(run)

    def test_public_cli_catches_selected_guard_refusal_with_shared_adapter(self):
        self.assertIs(project.ac_formal_gate, gen.ac_formal_gate)
        config = self.root / 'checker-config.json'
        config.write_bytes(formal.canonical(self.config))
        output = self.secret().parent / 'cli-run'
        error = io.StringIO()
        with redirect_stderr(error):
            code = project.main(['prepare', '--project', str(self.root), '--definition', str(self.definition),
                                 '--out', str(output), '--formal-checker', str(config),
                                 '--formal-checker-sha256', formal.sha(config.read_bytes())])
        self.assertEqual(code, 2)
        self.assertEqual(json.loads(error.getvalue())['status'], 'refused')
        self.assertFalse(output.exists())


if __name__ == '__main__':
    unittest.main()
