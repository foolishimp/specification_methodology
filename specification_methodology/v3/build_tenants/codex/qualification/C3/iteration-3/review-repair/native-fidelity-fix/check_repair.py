"""Source-selected regressions for conditional acquisition and pointer scopes.

No native process, task trial or acceptance decision is implied by this audit.
Run before generation, and again with --generated to check the shipped program.
"""
import argparse
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
Q = HERE.parents[1]
sys.path.insert(0, str(Q))
import build_interpretation as build

PREIMAGE = 'aa063bd918267ff88f4c31fd24229e8198363f8d'
UNIT = 'TRANSFORMATION_LIBRARY.composition-law'
DOMAINS = {
    'design_declarations': ('design composition', [
        'DESIGN_MODULE_METHOD.transformation-admission-completeness-stdo-up-016',
        'DESIGN_MODULE_METHOD.bounded-frame-conservation-stdo-up-017']),
    'complete_transition_admission_and_semantic_commit': ('consequential admission', [
        'SPEC_METHOD.complete-enclosing-relation-admission-stdo-up-021']),
    'frame_relations': ('frame-governed composition', ['REFERENCE_FRAME_METHOD.using-frames-in-conjunction']),
    'typed_calculus_paths': ('a_c composition', ['AXIOMATIC_CALCULUS.ac-016-typed-composition']),
}


def require(value, message):
    if not value:
        raise ValueError(message)


def check_domains(current):
    row = next(r for r in current['determinations'] if r['id'] == UNIT)
    domains = row['definition']['clauses'][0]['conditional_domain_owners']
    for domain, (when, owners) in DOMAINS.items():
        require(domains[domain] == {'required_when': when, 'owners': owners}, 'Missing explicit condition: ' + domain)
    edges = build.acquisition_edges(row, {r['id'] for r in current['determinations']}, current['semantic_contracts'], row)
    for _, (when, owners) in DOMAINS.items():
        for owner in owners:
            occurrences = [e for e in edges if e['target'] == build.clause_id(owner)
                           and e['acquisition'] not in {'typed-duplicate', 'provenance'}]
            require(occurrences and all(e['acquisition'] == 'conditional' and e['qualification']['required_when'] == when
                    for e in occurrences), 'Repeated occurrence became unconditional: ' + owner)


def audit_occurrences(program):
    """Separate traversal of all declared bases, including transitions outward."""
    counts = {'references': 0, 'routes': 0, 'inline_uses': 0, 'clauses': 0, 'outer_after_inline': 0}
    for clause in program['clauses']:
        bases = {}
        inline_seen = False
        for index, arg in enumerate(clause['arguments']):
            role = arg['role'].rsplit('#', 1)[-1]
            if role == 'semantic-record':
                require(index == 0, 'More than one semantic record')
                bases['semantic-record'] = json.loads(arg['literal'])
                continue
            if role not in {'reference-location', 'inlined-contract', 'acquisition-route'}:
                continue
            record = json.loads(arg['literal'])
            value = bases[record['scope']]
            for encoded in record['pointer'].split('/')[1:]:
                key = encoded.replace('~1', '/').replace('~0', '~')
                value = value[int(key)] if isinstance(value, list) else value[key]
            if role == 'inlined-contract':
                require(record['identity'] == build.NS + 'contract:' + value, 'Inline use identifies another definition')
                bases[record['identity']] = record['definition']
                inline_seen = True
                counts['inline_uses'] += 1
                continue
            target = clause['arguments'][index + 1]['ref'] if role == 'reference-location' else record['target']
            relation = clause['arguments'][index + 1]['role'].rsplit('#', 1)[-1] if role == 'reference-location' else record['relation']
            expected = build.NS + ('contract:' if relation == 'shared-contract' else 'clause:') + value
            if relation == 'foundation-premise-owner':
                require(value in {'F1', 'F2', 'F3', 'F4', 'F5', 'F6'}, 'Unknown foundation premise')
                expected = build.NS + 'clause:FOUNDATIONS.foundational-commitments'
            require(target == expected, 'Resolved occurrence points to another target')
            counts['references' if role == 'reference-location' else 'routes'] += 1
            if inline_seen and record['scope'] == 'semantic-record':
                counts['outer_after_inline'] += 1
        counts['clauses'] += 1
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--generated', action='store_true')
    args = parser.parse_args()
    current, _ = build.semantic_projection(build.read(build.ACCOUNT))
    build.validate_account(current)
    check_domains(current)
    program, _, _ = build.build_program(current)
    if args.generated:
        require(program == build.read(build.OUTPUT / 'program.json'), 'Generated program drift')
    checks = build.validate_occurrences(program, current['semantic_contracts'])
    independent = audit_occurrences(program)
    repo = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=HERE, text=True).strip())
    old = json.loads(subprocess.check_output(['git', 'show', PREIMAGE + ':' + str((build.OUTPUT / 'source-account.json').relative_to(repo))], cwd=repo))
    changed = [r['id'] for r in current['determinations'] if r != next(v for v in old['determinations'] if v['id'] == r['id'])]
    require(changed == [UNIT], 'A determination outside the repair changed')
    require(current['semantic_contracts'] == old['semantic_contracts'], 'Shared meanings changed')
    ux = next(c for c in program['clauses'] if c['uri'] == build.clause_id('UX_METHOD.1-position'))
    locations = [json.loads(a['literal']) for a in ux['arguments'] if a['role'] == build.VOCAB + 'reference-location']
    require(any(r['pointer'] == '/premises/0' and r['scope'] != 'semantic-record' for r in locations), 'Inline premise scope absent')
    require(any(r == {'scope': 'semantic-record', 'pointer': '/argument/premise_owner'} for r in locations), 'Outer return scope absent')
    controls = []

    def rejects(label, action):
        try:
            action()
        except (ValueError, KeyError, TypeError) as error:
            controls.append({'case': label, 'result': 'rejected', 'reason': str(error)})
        else:
            raise ValueError('Adverse control escaped: ' + label)

    rejects('original unqualified composition occurrences', lambda: check_domains(old))
    unqualified = copy.deepcopy(current)
    row = next(r for r in unqualified['determinations'] if r['id'] == UNIT)
    del row['definition']['clauses'][0]['conditional_domain_owners']['frame_relations']['required_when']
    rejects('one repeated frame occurrence loses condition', lambda: check_domains(unqualified))
    old_program = json.loads(subprocess.check_output(['git', 'show', PREIMAGE + ':' + str((build.OUTPUT / 'program.json').relative_to(repo))], cwd=repo))
    rejects('original unscoped program', lambda: build.validate_occurrences(old_program, old['semantic_contracts']))
    for label, mutation in [
        ('inline pointer incorrectly uses outer base', lambda r: r.update(scope='semantic-record')),
        ('undefined pointer base', lambda r: r.update(scope='missing')),
        ('pointer resolves but names another target', lambda r: r.update(scope='semantic-record', pointer='/id')),
        ('invalid pointer escape', lambda r: r.update(pointer='/premises/~2')),
        ('negative array index', lambda r: r.update(pointer='/premises/-1')),
    ]:
        mutant = copy.deepcopy(ux)
        arg = next(a for a in mutant['arguments'] if a['role'] == build.VOCAB + 'reference-location'
                   and json.loads(a['literal'])['pointer'] == '/premises/0')
        record = json.loads(arg['literal']); mutation(record)
        arg['literal'] = build.text(record)
        rejects(label, lambda: build.validate_occurrences({'clauses': [mutant]}, current['semantic_contracts']))
    mutant = copy.deepcopy(ux)
    arg = next(a for a in mutant['arguments'] if a['role'] == build.VOCAB + 'reference-location'
               and json.loads(a['literal'])['pointer'] == '/argument/premise_owner')
    record = json.loads(arg['literal'])
    record['scope'] = next(r['scope'] for r in locations if r['scope'] != 'semantic-record')
    arg['literal'] = build.text(record)
    rejects('outer occurrence retains the preceding inline base',
            lambda: build.validate_occurrences({'clauses': [mutant]}, current['semantic_contracts']))
    mutant = copy.deepcopy(ux)
    index = next(i for i, a in enumerate(mutant['arguments']) if a['role'] == build.VOCAB + 'reference-location')
    del mutant['arguments'][index + 1]
    rejects('missing adjacent typed target', lambda: build.validate_occurrences({'clauses': [mutant]}, current['semantic_contracts']))
    mutant = copy.deepcopy(ux)
    arg = next(a for a in mutant['arguments'] if a['role'] == build.VOCAB + 'inlined-contract')
    record = json.loads(arg['literal']); record['definition']['premises'] = []
    arg['literal'] = build.text(record)
    rejects('inline definition differs from its identity', lambda: build.validate_occurrences({'clauses': [mutant]}, current['semantic_contracts']))

    # Exercise actual compiler recursion with nested and repeated abbreviations,
    # escaped property names, and a subsequent occurrence in the outer record.
    nested = copy.deepcopy(current)
    nested['semantic_contracts']['test/outer~'] = {'contract_ref': 'test/inner~'}
    nested['semantic_contracts']['test/inner~'] = {'a/b~': 'FOUNDATIONS.result-algebra'}
    row = next(r for r in nested['determinations'] if r['id'] == UNIT)
    row['definition']['scope_regression'] = [{'contract_ref': 'test/outer~'}, {'contract_ref': 'test/outer~'}]
    nested_program, _, _ = build.build_program(nested)
    nested_audit = audit_occurrences(nested_program)
    require(nested_audit['references'] == independent['references'] + 2, 'Nested references omitted')

    # Retain the previous ODD fix without rewriting its historical task export.
    spec = importlib.util.spec_from_file_location('odd_fix', HERE.parent / 'odd-binding-fix/check_repair.py')
    odd = importlib.util.module_from_spec(spec); spec.loader.exec_module(odd)
    odd.check_binding(next(r for r in current['determinations'] if r['id'] == odd.UNIT))
    report = {'valid': True, 'preimage_commit': PREIMAGE, 'generated_program_checked': args.generated,
              'account_sha256': build.sha(build.ACCOUNT.read_bytes()), 'program_sha256': build.sha(build.json_bytes(program)),
              'checker_sha256': build.sha(Path(__file__).read_bytes()), 'changed_determinations': changed,
              'compiler_occurrences': checks, 'separate_occurrence_traversal': independent,
              'nested_and_repeated_scopes': 'passed', 'previous_ODD_binding': 'preserved', 'controls': controls,
              'limits': ['Author checks; independent semantic review and C3 acceptance remain open.',
                         'Applicability is retained, not evaluated; no fresh task-use evidence.']}
    (HERE / ('CHECK.json' if args.generated else 'PREGENERATION_CHECK.json')).write_bytes(build.json_bytes(report))
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
