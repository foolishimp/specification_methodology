"""Execute each installed guide's project route with an unrelated ambient manager.

Manager/native cuts and authored answers are controlled fixtures, not nativeA
installation or F_P authoring qualification. The provider and CLI calls are real.
"""
from pathlib import Path
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import unittest

import test_install_305 as installation

REPO = installation.REPO
sys.path.insert(0, str(REPO / 'a_c/build_tenants/graphify/test_env'))
from test_ac_generate import SOURCE, fixture_answer


class ProjectManagerRouteTests(unittest.TestCase):
    def test_both_installed_guides_forward_manager_through_complete_public_flow(self):
        fixture = installation.Install305Tests('test_plan_has_no_effect'); fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        root = fixture.root; log = root / 'calls'; log.mkdir(); counter = 0
        launcher, contract = fixture.selected_store_launcher()
        anchor = json.loads(fixture.definition.read_text())
        anchor.update(kind='stdo.product-definition', product={'definition_id': 'urn:fixture:runtime-anchor', 'source_project': './'})
        fixture.definition.write_bytes(installation.m.encode(anchor))
        manager_log = root / 'manager-calls.jsonl'
        fixture.manager.write_text('#!/usr/bin/env python3\nimport sys,json,pathlib\n'
            + 'assert sys.argv[1:3] == ' + repr(['--store', contract['store']]) + '\n'
            + 'with open(' + repr(str(manager_log)) + ',"a") as f:f.write(json.dumps(sys.argv)+"\\n")\n'
            + 'p=pathlib.Path(sys.argv[sys.argv.index("--definition")+1]);d=json.loads(p.read_text());b=d["constitution"]["stdo"]["basis"]\n'
            + 'print(json.dumps({"basis":b["uri"],"manifest_sha256":b["manifest_sha256"],"installed":True,"valid":True,"failures":[],"path":'
            + repr(str(fixture.method)) + ',"definition":str(p),"definition_id":d["product"]["definition_id"]}))\n')
        contract['manager_sha256'] = installation.m.sha(fixture.manager.read_bytes())
        owner = REPO / 'specification_methodology/v3/build_tenants/common-tools/tooling_setup.py'
        spec = importlib.util.spec_from_file_location('route_setup', owner)
        setup = importlib.util.module_from_spec(spec); spec.loader.exec_module(setup)
        launcher.write_bytes(setup.launcher_source(contract))
        fixture.args.ac_root = REPO / 'a_c'
        wrong = root / 'wrong-bin'; wrong.mkdir(); marker = root / 'wrong-manager-called'
        (wrong / 'stdo').write_text('#!/usr/bin/env python3\nfrom pathlib import Path\nPath(' + repr(str(marker)) + ').write_text("wrong ambient invoked")\nraise SystemExit(77)\n')
        (wrong / 'stdo').chmod(0o755)
        project = root / 'project'; project.mkdir(); (project / 'RULES.md').write_text(SOURCE)
        definition = {'kind': 'stdo.product-definition', 'product': {'definition_id': 'urn:fixture:nominated', 'name': 'Nominated fixture', 'source_project': './'},
                      'constitution': {'stdo': {'basis': {'uri': 'stdo://releases/v3.0.4/', 'manifest_sha256': 'a' * 64}}},
                      'what': {'intent': 'RULES.md', 'product': 'RULES.md', 'specification': ['RULES.md']}}
        product = project / 'Product.json'; product.write_bytes(installation.m.encode(definition)); original = product.read_bytes()

        def call(label, argv, environment, expected=0):
            nonlocal counter
            counter += 1; directory = log / (str(counter).zfill(2) + '-' + label); directory.mkdir()
            process = subprocess.run(argv, cwd=root, env=environment, capture_output=True, text=True)
            (directory / 'stdout.txt').write_text(process.stdout); (directory / 'stderr.txt').write_text(process.stderr)
            (directory / 'execution.json').write_bytes(installation.m.encode({'argv': argv, 'cwd': str(root), 'returncode': process.returncode,
                'PATH': environment['PATH'], 'STDO_STORE': environment.get('STDO_STORE')}))
            self.assertEqual(process.returncode, expected, process.stdout + process.stderr)
            return json.loads(process.stdout) if process.stdout else None

        try:
            for host in ('codex', 'claude'):
                fixture.args.host = host; installation.m.install(fixture.args)
                base, bundle, _ = installation.m.paths(fixture.workspace, host)
                guide = (base / 'skills/stdo-project/references/project.md').read_text()
                template = next(text for text in re.findall(r'`([^`]+)`', guide) if text.startswith('prepare --')).split(' [')[0].split()
                entry = (base / 'skills/stdo-project/SKILL.md').read_text()
                self.assertIn('`python`, `ac_root` and `stdo`', entry)
                for ambient in ('unset', 'wrong'):
                    environment = dict(os.environ, PATH='/usr/local/bin:/usr/bin:/bin'); environment.pop('STDO_STORE', None)
                    if ambient == 'wrong': environment.update(PATH=str(wrong) + ':' + environment['PATH'], STDO_STORE=str(root / 'unselected-store'))
                    config = call(host + '-' + ambient + '-runtime', [sys.executable, '-B', str(bundle / 'manage_skills.py'), 'check-runtime', '--configuration', str(bundle / 'CONFIG.json')], environment)['configuration']
                    prefix = [config['python'], '-B', str(Path(config['ac_root']) / 'scripts/ac.py'), 'project']
                    run = root / (host + '-' + ambient + '-run')
                    values = {'ROOT': str(project), 'FILE': 'Product.json', 'NEW_RUN': str(run), 'STDO': config['stdo']}
                    prepare = [values.get(token, token) for token in template] + ['--source', 'RULES.md']
                    self.assertIn('--stdo', prepare)
                    # Preserve the review's failing counterfactual on a separate output.
                    old = prepare[:]; i = old.index('--stdo'); del old[i:i + 2]
                    old[old.index('--out') + 1] += '-missing-manager'
                    call(host + '-' + ambient + '-omitted-manager', prefix + old, environment, 2)
                    marker_before = marker.read_bytes() if marker.exists() else None
                    call(host + '-' + ambient + '-prepare', prefix + prepare, environment)
                    task = call(host + '-' + ambient + '-task', prefix + ['task', '--run', str(run)], environment)
                    self.assertEqual(task['status'], 'authoring_required')
                    chunk = json.loads((run / 'generation/chunks.json').read_text())[0]
                    answer = root / (host + '-' + ambient + '-answer.json'); answer.write_bytes(installation.m.encode(fixture_answer(chunk)))
                    call(host + '-' + ambient + '-submit', prefix + ['submit', '--run', str(run), '--chunk', chunk['id'], '--answer', str(answer), '--author', 'controlled-guide-regression-fixture'], environment)
                    built = call(host + '-' + ambient + '-build', prefix + ['build', '--run', str(run)], environment)
                    self.assertEqual(built['status'], 'built'); self.assertEqual(built['method'], definition['constitution']['stdo']['basis'])
                    status = call(host + '-' + ambient + '-status', prefix + ['status', '--run', str(run)], environment)
                    self.assertEqual(status['status'], 'built')
                    self.assertEqual(json.loads((run / 'PROJECT.json').read_text())['manager'], config['stdo'])
                    self.assertEqual(product.read_bytes(), original)
                    self.assertEqual(marker.read_bytes() if marker.exists() else None, marker_before)
        finally:
            custody = os.environ.get('STDO_SKILLS_ROUTE_CUSTODY')
            if custody:
                target = Path(custody).absolute(); shutil.copytree(root, target)
                (target / 'CUSTODY.json').write_bytes(installation.m.encode({'original_root': str(root), 'public_calls': counter,
                    'standing': 'Actual installed-guide/public-provider route against synthetic manager/native cuts and authored fixture answers; no nativeA or F_P qualification.'}))


if __name__ == '__main__': unittest.main()
