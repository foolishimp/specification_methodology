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
    require(inventory_before['all_product_sources_match_input_commit'], 'source bytes differ from frozen input commit')
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
    report['index_semantics'] = 'Named roots plus transitive dependency closure; no direct-index completeness requirement asserted'

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
    # Include the owner/context preceding F1-F6, avoiding unresolved "above".
    premise_text = foundation_text.split('## Interpretation and representation', 1)[0]
    core_text = '## Result algebra' + foundation_text.split('## Result algebra', 1)[1]
    selected_core = premise_text + '\n' + core_text
    (ROOT / 'CORE_SOURCE_EXCERPTS.md').write_text(selected_core)
    source_scope = (ROOT / 'SOURCE.md').read_text()
    baseline = (TENANT / 'successor/standards/STDO_REFERENCE_FRAME_BASELINE.md').read_text()
    profile_text = '## Executive Attention, Evaluation, And Action' + baseline.split(
        '## Executive Attention, Evaluation, And Action', 1)[1].split('### Event-Driven Executive Attention', 1)[0]
    old_program = json.loads((ROOT / 'pre-r1-r10-repair/program.json').read_text())
    old_clauses = {c['uri']: c for c in old_program['clauses']}
    changed = [c for c in program['clauses'] if old_clauses.get(c['uri']) != c]
    consumption = [c for c in program['clauses'] if ':family-' in c['uri'] or ':consumer-' in c['uri']]
    require(len(consumption) == 18 and all(c['operator'].endswith('#consumes') for c in consumption),
            'family consumption was represented as outcome refinement')
    require(all(next(a['literal'] for a in c['arguments'] if a['role'].endswith('#standing')) in
                {'premise', 'source-owned method law', 'additional domain policy'} for c in program['clauses']),
            'standing outside declared vocabulary')
    family_index = next(i for i in program['frame_indexes'] if i['uri'].endswith(':material-families'))
    require(set(family_index['clause_refs']) == {c['uri'] for c in consumption}, 'family index omitted consumption clause')
    require(all(old_clauses[c['uri']] == c for c in consumption), 'textual repair expanded family scope')
    delta = {'kind': 'R1-R10-selected-interpretation-repair',
             'source_commit': inventory_before['input_commit'],
             'exact_changed_clauses': changed,
             'exact_grant_identity_symbols': [v for v in program['symbols'] if v['uri'].endswith((':grant', ':identity'))],
             'exact_residuals': program['residuals'],
             'scope': 'Only R1-R10 textual repairs and N1 finite refinement repair are reassessed. A1-A7 and other finite findings were settled or truthfully narrowed by preceding review. No family clause changed; all eighteen family-source fidelity claims remain unresolved. N1 code and its oracle are provided separately. Structural closure and these textual clauses prove no whole-core acceptance.'}
    write('SOURCE_DELTA.json', delta)
    prior_review = (ROOT / 'pre-r1-r10-repair/SOURCE_RECHECK.md').read_text()
    counterexamples = '## 4. Remaining counterexamples and altered meaning' + prior_review.split(
        '## 4. Remaining counterexamples and altered meaning', 1)[1].split('## 5. Still unresolved', 1)[0]
    selected_recheck_source = premise_text + '\n' + core_text.split('## Core contract derivations', 1)[0]
    selected_scope = source_scope.split('## Results', 1)[0] + '\n## Residual scope\n' + source_scope.split('## Residual scope', 1)[1]
    finite_review = (ROOT / 'pre-n1-repair/FINITE_RECHECK.md').read_text()
    n1_findings = '## New finding' + finite_review.split('## New finding', 1)[1].split('## Mutant count check', 1)[0]
    code = (ROOT / 'model.py').read_text()
    n1_code = 'REFINEMENTS = ' + code.split('REFINEMENTS = ', 1)[1].split('def observe_effect', 1)[0]
    checks = (ROOT / 'finite_check.py').read_text()
    n1_checks = '    reason_oracle = ' + checks.split('    reason_oracle = ', 1)[1].split("    for row in expected['effect_observations']:", 1)[0]
    oracle = json.loads((ROOT / 'ORACLE.json').read_text())
    n1_oracle = {key: oracle[key] for key in ('refinement', 'unsupported_predicate_substitutions', 'n1_counterexamples')}
    sections = [
        {'label': 'Bounded final reassessment and limits', 'text': selected_scope},
        {'label': 'Exact unchanged deciding source', 'text': selected_recheck_source},
        {'label': 'Prior R1-R10 counterexamples; settled A findings omitted', 'text': counterexamples},
        {'label': 'Prior N1 counterexample and minor finite-claim qualifications', 'text': n1_findings},
        {'label': 'Interpretation vocabulary', 'text': (ROOT / 'SIGNATURE.md').read_text()},
        {'label': 'Exact corrected clauses, premise links and residual links', 'text': json.dumps(delta, separators=(',', ':'), ensure_ascii=False)},
        {'label': 'Exact finite refinement code and its called helpers', 'text': n1_code},
        {'label': 'Exact N1 finite oracle rows', 'text': json.dumps(n1_oracle, separators=(',', ':'), ensure_ascii=False)},
        {'label': 'Exact refinement and N1 enumeration checks; require raises on false', 'text': n1_checks},
        {'label': 'Source-first final reassessment task', 'text': 'No tools. Assess only R1-R10 textual repairs and N1 finite refinement against their exact deciding source. Check every R counterexample, the new separate-support boundary, mapped-failure retention, positive/nonindependent claim rejection, predicate/provenance/admissibility guards, performance preservation and declared limits. For R6, separate positive evaluation needs its own record; this finite model intentionally does not combine positive separate support. Unknown original undertaking is never upgraded. Do not infer family fidelity or complete executable coverage from clauses or structural checks. Recovery covers five stipulated rows; mutants are faulty functions versus expected outputs, not module-replacement suite runs. Settled A findings and unrelated finite domains are outside this final delta. Return remaining concrete counterexamples or confirm the bounded repairs; no acceptance or release is requested.'},
    ]
    joined_text = '\n\n'.join(s['label'] + '\n' + s['text'] for s in sections)
    require(len(joined_text.encode()) <= 120000, 'selected review request exceeds native assessment input cap: ' + str(len(joined_text.encode())))
    write('sections.json', sections)
    joined = invoke([TOOL, 'join', '--input', ROOT / 'sections.json', '--output', ROOT / 'REQUEST.txt'])
    require(joined.returncode == 0 and (ROOT / 'REQUEST.txt').read_text() == joined_text, 'exact join mismatch')
    report['joined_input_bytes'] = len(joined_text.encode())
    report['selected_input_cap_bytes'] = 120000

    # Earlier independent finite review consumed this exact packet. Preserve it;
    # its N1 counterexample is repaired only in the combined final REQUEST.
    require((ROOT / 'FINITE_REQUEST.txt').read_bytes() == (ROOT / 'pre-n1-repair/FINITE_REQUEST.txt').read_bytes(),
            'historical independent finite packet changed')
    report['finite_review_input_bytes'] = len((ROOT / 'FINITE_REQUEST.txt').read_bytes())
    report['finite_review_input_standing'] = 'Historical pre-N1 review input; superseded by current combined REQUEST.txt'
    report['combined_final_review'] = True

    finite = invoke([ROOT / 'finite_check.py'])
    require(finite.returncode == 0, finite.stdout + finite.stderr)
    report['finite'] = json.loads(finite.stdout)
    # All source observations still match: later edits require reinspection and rerun.
    for row in inventory_before['members']:
        require(sha((TENANT / row['path']).read_bytes()) == row['sha256'], 'source changed during run: ' + row['path'])
    report['source_observations_stable'] = True
    report['input_commit'] = inventory_before['input_commit']
    report['historical_exclusions'] = ['pre-9982/', 'pre-146e6ad/', 'pre-independent-review-repair/', 'pre-r1-r10-repair/', 'pre-n1-repair/']
    for dirname in ('pre-9982', 'pre-146e6ad', 'pre-independent-review-repair', 'pre-r1-r10-repair', 'pre-n1-repair'):
        archive = ROOT / dirname
        historical = json.loads((archive / 'HISTORICAL.json').read_text())
        for item in historical['members']:
            require(sha((archive / item['path']).read_bytes()) == item['sha256'], 'historical archive changed')
    report['historical_archive_unchanged'] = True
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
