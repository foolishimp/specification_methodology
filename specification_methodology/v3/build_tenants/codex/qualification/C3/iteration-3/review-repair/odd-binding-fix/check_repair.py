"""Replay the two repair counterexamples without evaluating prose predicates."""
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
Q = HERE.parents[1]
TENANT = Q.parents[2]
PACKAGE = TENANT / 'successor'
PREIMAGE = 'c29b2be37f9a12e050478be97793927d99c01781'
UNIT = 'ODD_METHOD.19-ramp-up-checklist'
CLAUSE = 'urn:codex-stdo3:iteration-3-r2:clause:' + UNIT
RESULTS = {'satisfied', 'falsified', 'indeterminate', 'out_of_frame', 'invalid_basis'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_binding(row):
    require(row['result_mapping']['bound_predicate'] == row['predicate'], 'entry predicate and result differ')
    bindings = {b['name']: b for b in row['contract_bindings']}
    recommendation, entry = bindings['ramp_up_recommendation'], bindings['entry_sufficiency']
    require(recommendation['modality'] == 'should', 'recommendation was made mandatory')
    require(entry['modality'] == 'required_for_claim', 'sufficiency lost its claim condition')
    require(recommendation['result_mapping']['bound_predicate'] == recommendation['predicate'], 'recommendation result binds another predicate')
    require(recommendation['predicate'] != row['predicate'], 'distinct source questions collapsed')
    for field in ('predicate', 'applicability', 'result_mapping'):
        require(entry[field + '_ref'] == '/' + field, 'entry binding does not resolve its own ' + field)
    for mapping in (row['result_mapping'], recommendation['result_mapping']):
        require(RESULTS <= mapping.keys(), 'a required core result is missing')
        require(mapping['kind'] == 'predicate_bound_five_result', 'parallel result mapping introduced')
    source = (PACKAGE / row['owner']['path']).read_bytes()
    blocks = {b['id']: b for b in row['source_clauses']}
    for binding in (recommendation, entry):
        for identifier in binding['source_clause_ids']:
            block = blocks[identifier]
            require(sha(source[block['byte_start']:block['byte_end']]) == block['sha256'], 'binding source span drift')


def semantic_record(clause):
    argument = next(a for a in clause['arguments'] if a['role'].endswith('#semantic-record'))
    return json.loads(argument['literal'])


def main():
    account = json.loads((PACKAGE / 'interpretation/source-account.json').read_bytes())
    row = next(r for r in account['determinations'] if r['id'] == UNIT)
    check_binding(row)
    repo = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=TENANT, text=True).strip())
    path = str((PACKAGE / 'interpretation/source-account.json').relative_to(repo))
    old = json.loads(subprocess.check_output(['git', 'show', PREIMAGE + ':' + path], cwd=repo))
    old_row = next(r for r in old['determinations'] if r['id'] == UNIT)
    swapped = copy.deepcopy(row)
    swapped['contract_bindings'][0]['result_mapping']['bound_predicate'] = row['predicate']
    mandatory = copy.deepcopy(row)
    mandatory['contract_bindings'][0]['modality'] = 'required_for_claim'
    controls = []
    for label, mutant in [('original mixed predicate', old_row), ('recommendation result rebound to entry', swapped), ('should promoted to required', mandatory)]:
        try:
            check_binding(mutant)
        except (ValueError, KeyError) as error:
            controls.append({'case': label, 'result': 'rejected', 'reason': str(error)})
        else:
            raise ValueError('Counterexample escaped: ' + label)

    guide = HERE.parent / 'interpretation/PROJECTION_USE.md'
    script = re.search(r'```sh\n(.*?)\n```', guide.read_text(), re.S)[1]
    tool = TENANT / 'a_c/install/axiom_indexer-v2.5.1-rc.2/build_tenants/core/code/ac.py'
    with tempfile.TemporaryDirectory(prefix='codex-i3-repair-check-') as directory:
        # Run the published recipe literally; only TMPDIR selects isolated outputs.
        result = subprocess.run(['sh', '-c', script], cwd=TENANT,
                                env={**os.environ, 'TMPDIR': directory}, capture_output=True, text=True)
        require(result.returncode == 0, result.stderr + result.stdout)
        lines = result.stdout.strip().splitlines()
        report = json.loads(lines[0])
        require(report['status'] == 'valid' and not report['diagnostics'], 'published projection recipe failed')
        output = Path(lines[-1])
        require(output.is_relative_to(Path(directory)), 'recipe output escaped temporary boundary')
        export = json.loads(output.read_bytes())
        recorded = json.loads((HERE.parent / 'interpretation/T1_EVALUATE_CONJOIN.materialized.json').read_bytes())
        preserved = ['clauses', 'clause_relations', 'closure', 'residuals', 'symbols', 'source_routes', 'residual_routes']
        for field in preserved:
            require(export[field] == recorded[field], 'T1 acquired meaning changed: ' + field)
        command = {'valid': True, 'guide_sha256': sha(guide.read_bytes()), 'script_sha256': sha(script.encode()),
                   'output_bytes': output.stat().st_size, 'output_sha256': sha(output.read_bytes()),
                   'historical_T1_selected_fields_unchanged': preserved, 'native_report': report}
        projections = []
        for mode in ('reference-only', 'materialized'):
            target = Path(directory) / (mode + '.json')
            invocation = subprocess.run([sys.executable, '-B', str(tool), 'project',
                '--program', str(PACKAGE / 'interpretation/program.json'), '--map', str(PACKAGE / 'interpretation/map.json'),
                '--bindings', str(output.parent / 'bindings.json'), '--frame-index',
                'urn:codex-stdo3:iteration-3-r2:index:' + UNIT, '--mode', mode, '--output', str(target)],
                cwd=TENANT, capture_output=True, text=True)
            require(invocation.returncode == 0, invocation.stderr + invocation.stdout)
            projection = json.loads(target.read_bytes())
            clauses = projection['clauses'].values() if isinstance(projection['clauses'], dict) else projection['clauses']
            native = semantic_record(next(c for c in clauses if c['uri'] == CLAUSE))
            check_binding(native)
            require(native == row, 'native view changes the source-bound record')
            projections.append({'mode': mode, 'bytes': target.stat().st_size, 'sha256': sha(target.read_bytes()),
                                'closure_clauses': len(projection['closure']['clauses']), 'both_bindings_preserved': True})
    result = {'valid': True, 'counterexample_preimage': PREIMAGE,
              'program_sha256': sha((PACKAGE / 'interpretation/program.json').read_bytes()),
              'map_sha256': sha((PACKAGE / 'interpretation/map.json').read_bytes()),
              'source_account_sha256': sha((PACKAGE / 'interpretation/source-account.json').read_bytes()),
              'mechanical_predicate_binding': 'passed', 'negative_controls': controls,
              'published_command': command, 'odd_projections': projections,
              'limits': ['Checks field relations, source pins and native carrier preservation; does not execute prose predicates.',
                         'Semantic fidelity and adequate/adverse/unresolved source cases require the separate nonauthor readback.',
                         'Historical T1 meaning is compared; changed package identity is not a new actor run.']}
    (HERE / 'CHECK.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'valid': True, 'negative_controls': len(controls), 'odd_modes': len(projections), 'published_command': 'passed',
                      'T1_selected_meaning': 'unchanged'}))


if __name__ == '__main__':
    main()
