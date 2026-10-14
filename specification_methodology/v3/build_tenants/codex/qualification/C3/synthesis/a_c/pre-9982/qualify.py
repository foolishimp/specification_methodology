"""Verify pinned mechanics, validate, project, join and run bounded checks.

Every write stays in this qualification directory. Source hashes are checked
again at exit. A changed source requires semantic reinspection before refresh.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
TENANT = ROOT.parents[3]
INSTALL = TENANT / 'a_c/install/axiom_indexer-v2.5.1-rc.2'
TOOL = INSTALL / 'build_tenants/core/code/ac.py'
TAG = 'refs/tags/axiom_indexer/v2.5.1-rc.2'
COMMIT = '9a9c479776ffd974fbcafcf48341980918209aef'
THEORY = Path('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md')


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write(name, value):
    (ROOT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def git(*args):
    return subprocess.check_output(['git', *args], cwd=TENANT)


def invoke(args):
    return subprocess.run([sys.executable, '-B'] + [str(s) for s in args],
                          cwd=INSTALL, text=True, capture_output=True)


def main():
    started = time.perf_counter()
    report = {'started_utc': datetime.now(timezone.utc).isoformat(), 'operations': []}
    expected_identity = {
        'tag': '9bff233c3f0e7d80f63307fa3b12800dd3db681c',
        'commit': COMMIT, 'tree': '3a553ceb8db2e8de4ac779abdc2a2ceae5708c7d',
        'subtree': '6dae168d0a258ca506f4d6b9d5cd0a0c835fb546'}
    observed_identity = {
        'tag': git('rev-parse', TAG).decode().strip(),
        'commit': git('rev-parse', TAG + '^{commit}').decode().strip(),
        'tree': git('rev-parse', COMMIT + '^{tree}').decode().strip(),
        'subtree': git('rev-parse', COMMIT + ':axiom_indexer').decode().strip()}
    require(expected_identity == observed_identity, 'fixed tool identity changed')
    note = git('show', COMMIT + ':axiom_indexer/releases/v2.5.1.md')
    require(sha(note) == 'ae59529d285cd4bcbee1f3fb65807d66a3774fca14d76f8edad826a0aaa2d9c9', 'release inventory owner changed')
    receipt = json.loads((TENANT / 'a_c/INSTALL_RECEIPT.json').read_text())
    members = []
    for pin in receipt['members']:
        path = INSTALL / pin['path']
        require(path.is_symlink() == (pin['type'] == 'symlink'), 'wrong member type: ' + pin['path'])
        data = os.readlink(path).encode() if path.is_symlink() else path.read_bytes()
        original = git('show', COMMIT + ':axiom_indexer/' + pin['path'])
        require(data == original and sha(data) == pin['sha256'], 'member changed: ' + pin['path'])
        require(pin['path'].encode() in note and pin['sha256'].encode() in note, 'unowned inventory entry')
        if path.is_symlink():
            require(path.resolve().is_relative_to(INSTALL.resolve()), 'link escapes pinned installation')
        members.append({'path': pin['path'], 'type': pin['type'], 'bytes': len(data), 'sha256': sha(data)})
    discovered = set()
    for folder, dirs, files in os.walk(INSTALL, followlinks=False):
        for name in files + [n for n in dirs if (Path(folder) / n).is_symlink()]:
            discovered.add(str((Path(folder) / name).relative_to(INSTALL)))
    require(discovered == {m['path'] for m in members}, 'installed member set differs')
    stream = ''.join(m['sha256'] + '  ' + m['type'] + '  ' + m['path'] + '\n'
                     for m in sorted(members, key=lambda row: row['path']))
    inventory = sha(stream.encode())
    require(inventory == '55a2061bd55ca29e349318a2869bc13518374ef2fa764a73b1688e76d35a63c1', 'wrong inventory digest')
    require(sha(TOOL.read_bytes()) == '5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8', 'wrong ac.py')
    require(sha(THEORY.read_bytes()) == 'cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d', 'wrong theory')
    write('INSTALL_VERIFICATION.json', {'valid': True, 'identity': observed_identity,
          'inventory_sha256': inventory, 'member_count': len(members), 'members': members,
          'theory_sha256': sha(THEORY.read_bytes()), 'checked_utc': datetime.now(timezone.utc).isoformat()})

    build = invoke([ROOT / 'build_program.py'])
    require(build.returncode == 0, build.stderr)
    report['program_counts'] = json.loads(build.stdout)
    inventory_before = json.loads((ROOT / 'SOURCE_INVENTORY.json').read_text())
    command = [TOOL, 'validate', '--program', ROOT / 'program.json', '--bindings', ROOT / 'bindings.json',
               '--output', ROOT / 'validation.json', '--emit-map', ROOT / 'map.json']
    result = invoke(command)
    require(result.returncode == 0, result.stdout + result.stderr + (ROOT / 'validation.json').read_text())
    report['operations'].append({'operation': 'validate', 'exit': result.returncode})

    program = json.loads((ROOT / 'program.json').read_text())
    select = [piece for index in program['frame_indexes'] for piece in ('--frame-index', index['uri'])]
    common = [TOOL, 'project', '--program', ROOT / 'program.json', '--map', ROOT / 'map.json',
              '--bindings', ROOT / 'bindings.json']
    projections = []
    for mode in ('reference-only', 'materialized'):
        target = ROOT / ('projection-' + mode + '.json')
        result = invoke(common + ['--mode', mode, '--output', target] + select)
        require(result.returncode == 0, result.stdout + result.stderr)
        write('project-' + mode + '.report.json', json.loads(result.stdout))
        projections.append(json.loads(target.read_text()))
        report['operations'].append({'operation': 'project', 'mode': mode, 'exit': result.returncode})
    for key in ('closure', 'clause_relations', 'residual_routes', 'source_routes'):
        require(projections[0][key] == projections[1][key], 'projection parity failed: ' + key)
    require(set(projections[0]['closure']['clauses']) == {c['uri'] for c in program['clauses']}, 'selected union omitted authored clauses')
    report['projection_parity'] = True

    # A real closure test starts with a single source-owned configuration root.
    result = invoke(common + ['--mode', 'reference-only', '--output', ROOT / 'projection-configuration.json',
                             '--frame-index', 'urn:codex-stdo3:synthesis:index:configuration'])
    require(result.returncode == 0, result.stdout + result.stderr)
    partial = json.loads((ROOT / 'projection-configuration.json').read_text())
    roots = next(i['clause_refs'] for i in program['frame_indexes'] if i['uri'].endswith(':configuration'))
    require(set(roots) < set(partial['closure']['clauses']), 'transitive dependency closure was not demonstrated')
    report['configuration_closure_clauses'] = len(partial['closure']['clauses'])

    empty = invoke(common + ['--mode', 'reference-only'])
    empty_report = json.loads(empty.stdout)
    require(empty.returncode != 0 and any(d['code'] == 'empty_selection' for d in empty_report['diagnostics']), 'empty selection did not refuse')
    write('EMPTY_SELECTION_REFUSAL.json', empty_report)
    mutant = json.loads((ROOT / 'program.json').read_text())
    mutant['clauses'][0]['statement'] += ' Changed observation for map-drift check.'
    write('program-map-drift-mutant.json', mutant)
    wrong = invoke([TOOL, 'project', '--program', ROOT / 'program-map-drift-mutant.json', '--map', ROOT / 'map.json',
                    '--bindings', ROOT / 'bindings.json', '--mode', 'reference-only'] + select)
    wrong_report = json.loads(wrong.stdout)
    require(wrong.returncode != 0 and any(d['code'] == 'map_mismatch' for d in wrong_report['diagnostics']), 'stale map did not refuse')
    write('MAP_DRIFT_REFUSAL.json', wrong_report)

    foundation_text = (TENANT / 'successor/standards/FOUNDATIONS.md').read_text()
    premise_text = '## Foundational commitments' + foundation_text.split('## Foundational commitments', 1)[1].split('## Interpretation and representation', 1)[0]
    core_text = '## Result algebra' + foundation_text.split('## Result algebra', 1)[1]
    selected_core = premise_text + '\n' + core_text
    (ROOT / 'CORE_SOURCE_EXCERPTS.md').write_text(selected_core)
    source_scope = (ROOT / 'SOURCE.md').read_text()
    program_scope = source_scope.split('## Finite oracle', 1)[0] + '## Residual scope' + source_scope.split('## Residual scope', 1)[1]
    sections = [
        {'label': 'Selected source frames and residual scope', 'text': program_scope},
        {'label': 'Core owner selected unchanged sections', 'text': selected_core},
        {'label': 'Interpretation vocabulary', 'text': (ROOT / 'SIGNATURE.md').read_text()},
        {'label': 'Exact source-linked program value with insignificant whitespace removed', 'text': json.dumps(program, separators=(',', ':'), ensure_ascii=False)},
        {'label': 'Review task', 'text': 'Judge this selected source/model fidelity before semantic acceptance. The material-family clauses retain unmodelled fine policy. Structure and finite checks do not establish fidelity. Re-enter exact domain owners when their policy is material; do not infer it from family labels.'},
    ]
    joined_text = '\n\n'.join(s['label'] + '\n' + s['text'] for s in sections)
    require(len(joined_text.encode()) <= 120000, 'selected review request exceeds native assessment input cap')
    write('sections.json', sections)
    joined = invoke([TOOL, 'join', '--input', ROOT / 'sections.json', '--output', ROOT / 'REQUEST.txt'])
    require(joined.returncode == 0 and (ROOT / 'REQUEST.txt').read_text() == joined_text, 'exact join mismatch')
    report['joined_input_bytes'] = len(joined_text.encode())
    report['selected_input_cap_bytes'] = 120000

    finite_sections = [
        {'label': 'Selected source and proof boundary', 'text': source_scope},
        {'label': 'Exact core owner selected sections', 'text': selected_core},
        {'label': 'Fixed oracle expectations', 'text': (ROOT / 'ORACLE.json').read_text()},
        {'label': 'Executable interpretation', 'text': (ROOT / 'model.py').read_text()},
        {'label': 'Executable finite checks and separate oracle algorithm', 'text': (ROOT / 'finite_check.py').read_text()},
        {'label': 'Independent assessment task', 'text': 'Read the method source first. Judge whether the fixed oracle, executable interpretation, legal-coordinate cases, effect joins, and actual faulty-function counterexamples preserve its selected semantics. Distinguish same-Writer algorithmic separation from your independent fidelity judgment. No whole-corpus, native-agent, real-transport or release claim follows.'},
    ]
    finite_request = '\n\n'.join(s['label'] + '\n' + s['text'] for s in finite_sections)
    require(len(finite_request.encode()) <= 120000, 'finite source review request exceeds cap')
    write('sections-finite.json', finite_sections)
    finite_joined = invoke([TOOL, 'join', '--input', ROOT / 'sections-finite.json', '--output', ROOT / 'FINITE_REQUEST.txt'])
    require(finite_joined.returncode == 0 and (ROOT / 'FINITE_REQUEST.txt').read_text() == finite_request, 'finite exact join mismatch')
    report['finite_review_input_bytes'] = len(finite_request.encode())

    finite = invoke([ROOT / 'finite_check.py'])
    require(finite.returncode == 0, finite.stdout + finite.stderr)
    report['finite'] = json.loads(finite.stdout)
    # All source observations still match: later edits require reinspection and rerun.
    for row in inventory_before['members']:
        require(sha((TENANT / row['path']).read_bytes()) == row['sha256'], 'source changed during run: ' + row['path'])
    report['source_observations_stable'] = True
    report['operations'] += [{'operation': 'exact-join', 'exit': joined.returncode},
                             {'operation': 'finite-interpretation', 'exit': finite.returncode}]
    report['pins'] = {p.name: sha(p.read_bytes()) for p in ROOT.iterdir()
                      if p.is_file() and p.name not in {'MECHANICAL_RESULT.json'}}
    report['elapsed_seconds'] = time.perf_counter() - started
    report['finished_utc'] = datetime.now(timezone.utc).isoformat()
    report['valid'] = True
    report['limits'] = ['Author-owned bounded interpretation, not complete-corpus fidelity or acceptance',
                        'Fixed ac.py verifies structure and source relations only',
                        'Finite oracle is algorithmically separate, same Writer; independent source-first assessment remains required']
    write('MECHANICAL_RESULT.json', report)
    print(json.dumps({k: report[k] for k in ('valid', 'program_counts', 'joined_input_bytes', 'elapsed_seconds')}))


if __name__ == '__main__':
    main()
