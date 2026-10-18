"""Regression expectations authored from the deciding source relationships.

These checks assess compiler decisions, not task truth or whole-source fidelity.
Native projection and fresh-actor use remain separate checks on a frozen package.
"""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
Q = HERE.parents[1]
spec = importlib.util.spec_from_file_location('build_interpretation', Q / 'build_interpretation.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

PREIMAGE = '0517eb2771b18a7369c69e52570a3db3e36f8229'
ACCOUNT = 'specification_methodology/v3/build_tenants/codex/successor/interpretation/source-account.json'


def check(condition, detail):
    if not condition:
        raise ValueError(detail)


def relations(account, identifier):
    rows = {r['id']: r for r in account['determinations']}
    row = rows[identifier]
    return build.acquisition_edges(row, set(rows), account['semantic_contracts'], row)


def required(account, identifier):
    return {e['target'].removeprefix(build.NS + 'clause:')
            for e in relations(account, identifier) if e['acquisition'] == 'required'}


def oracle(account):
    """Specific source expectations, independent of classifier branching."""
    prose = required(account, 'WRITING_GUIDE.good-prose')
    check({'FOUNDATIONS.result-algebra', 'FOUNDATIONS.result-conjunction',
           'WRITING_GUIDE.method-alignment'} <= prose, 'Prose lost a material predicate owner')
    evaluate = relations(account, 'TRANSFORMATION_LIBRARY.evaluate')
    target = build.clause_id('STDO_REFERENCE_FRAME_BASELINE.derived-reviewer-frame')
    check(not any(e['target'] == target and e['acquisition'] == 'required' for e in evaluate),
          'The optional Baseline Reviewer became an unconditional requirement')
    check(any(e['target'] == target and e['acquisition'] == 'conditional'
              and e['qualification']['required_when'] == 'Baseline Reviewer is adopted and lawfully activated'
              for e in evaluate), 'Baseline adoption/activation condition was erased')
    conjunction = relations(account, 'FOUNDATIONS.result-conjunction')
    for suffix in ('transformation-admission-completeness-stdo-up-016', 'bounded-frame-conservation-stdo-up-017'):
        target = build.clause_id('DESIGN_MODULE_METHOD.' + suffix)
        check(not any(e['target'] == target and e['acquisition'] == 'required' for e in conjunction),
              'Design-only composition became universal')
        check(any(e['target'] == target and e['acquisition'] == 'conditional'
                  and e['qualification']['required_when'] == 'design composition is selected' for e in conjunction),
              'Design applicability was lost')
    recovery = required(account, 'TRANSFORMATION_LIBRARY.workrecovery-specialization')
    check({'FOUNDATIONS.workspace-and-context', 'FOUNDATIONS.result-conjunction',
           'REFERENCE_FRAME_METHOD.rf-005-exact-basis-and-coordinates',
           'TICKET_METHOD.work-carrier-to-execution-rule'} <= recovery,
          'Recovery lost currentness, exact basis, failed/missing results or work continuity')
    target = build.clause_id('TRANSFORMATION_LIBRARY.workrecovery-specialization')
    foundation = relations(account, 'FOUNDATIONS.foundational-commitments')
    check(any(e['target'] == target and e['acquisition'] == 'provenance' for e in foundation),
          'The recoverable specialization example disappeared')
    check(not any(e['target'] == target and e['acquisition'] == 'required' for e in foundation),
          'A specialization example became mandatory foundational acquisition')


def main():
    account = json.loads(subprocess.check_output(['git', 'show', PREIMAGE + ':' + ACCOUNT], cwd=Q))
    oracle(account)
    controls = []
    def rejected(name, mutate):
        changed = copy.deepcopy(account)
        rows = {r['id']: r for r in changed['determinations']}
        mutate(rows)
        try:
            oracle(changed)
        except ValueError as error:
            controls.append({'case': name, 'refusal': str(error)})
        else:
            raise ValueError(name + ': unsafe interpretation escaped the independent oracle')
    rejected('Omitted prose result owner', lambda rows: rows['WRITING_GUIDE.good-prose']['result_mapping'].update(owner_refs=[]))
    def demote_recovery(rows):
        row = rows['TRANSFORMATION_LIBRARY.workrecovery-specialization']
        for rel in row['dependency_relations']:
            if rel['id'] == 'FOUNDATIONS.workspace-and-context':
                rel['kind'] = 'source_provenance'
        step = row['argument']['clause_arguments'][0]['conditional_steps'][3]
        step['contracts'] = [v for v in step['contracts'] if v != 'FOUNDATIONS.workspace-and-context']
    rejected('Required recovery support relabelled provenance', demote_recovery)
    def erase_condition(rows):
        for rel in rows['TRANSFORMATION_LIBRARY.evaluate']['dependency_relations']:
            if rel['id'] == 'STDO_REFERENCE_FRAME_BASELINE.derived-reviewer-frame':
                rel.pop('required_when')
    rejected('Adoption condition erased', erase_condition)
    def unconditional_duplicate(rows):
        rows['TRANSFORMATION_LIBRARY.evaluate']['dependency_relations'].append({
            'id': 'STDO_REFERENCE_FRAME_BASELINE.derived-reviewer-frame', 'kind': 'contract_application'})
    rejected('Unconditional alternate edge defeats profile scope', unconditional_duplicate)
    sample = {'id': 'A', 'dependency_relations': [{'id': 'B', 'kind': 'previously-unclassified'}]}
    check(build.acquisition_edges(sample, {'A', 'B'}, {}, sample)[0]['acquisition'] == 'required',
          'Unknown relationship kind was silently dropped')
    unknown = {'id': 'A', 'dependency_relations': [{'id': 'B', 'kind': 'contract_application', 'required_when': 'condition is not yet known'}]}
    routed = build.acquisition_edges(unknown, {'A', 'B'}, {}, unknown)[0]
    check(routed['acquisition'] == 'conditional' and routed['qualification'] == unknown['dependency_relations'][0],
          'Unknown applicability became false or disappeared')
    owners = build.source_contract_owners(account)
    check(owners['core.shared_contracts.core_evaluation'] == ['FOUNDATIONS.result-algebra', 'FOUNDATIONS.result-conjunction'],
          'The existing result owners changed')
    check(owners['core.shared_contracts.definition_data'] == [], 'Consumers became authority for a shared abbreviation')
    print(json.dumps({'valid': True, 'preimage': PREIMAGE, 'controls': controls,
                      'limits': ['Authored relation oracle, not independent source fidelity.',
                                 'No task predicate was executed; native/use proofs follow the source freeze.']}, indent=2))


if __name__ == '__main__':
    main()
