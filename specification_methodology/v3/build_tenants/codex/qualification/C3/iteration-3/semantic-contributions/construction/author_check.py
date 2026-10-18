#!/usr/bin/env python3
"""Bounded author checks, not an independent fidelity or runtime oracle.

Read only frozen Git objects and this contribution. The finite behavioral
fixtures exercise selected deciding relationships with positive, adverse and
unknown cases. They neither execute an adopting runtime nor establish every
possible semantic instance. No project generator or oracle is used or changed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / '.git').exists())
SOURCE = 'f2cb3e593757d094d008102551925e871a0204ff'
ACCOUNT_SHA = 'ae5169eea86204a0d5d27915c6935604bb09d8d9a4feeb6cc403706a0ac42b12'
ACCOUNT = 'specification_methodology/v3/build_tenants/codex/qualification/C3/iteration-3/DETERMINATIONS.json'
SOURCE_ROOT = 'specification_methodology/v3/build_tenants/codex/successor/'
VERDICTS = {'satisfied', 'falsified', 'indeterminate', 'out_of_frame', 'invalid_basis'}


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def frozen(revision: str, path: str) -> bytes:
    return subprocess.check_output(['git', 'show', f'{revision}:{path}'], cwd=ROOT)


def conjoin(values: list[bool | None], interpretable: bool = True,
            capable: bool = True) -> str:
    if not interpretable:
        return 'invalid_basis'
    if any(v is False for v in values):
        return 'falsified'
    if not capable:
        return 'out_of_frame'
    if any(v is None for v in values):
        return 'indeterminate'
    return 'satisfied'


def effect_join(parts: list[str]) -> str:
    """Parts are already reconciled at one disjoint observation boundary."""
    assert parts
    p = set(parts)
    if 'unknown' in p:
        return 'unknown'
    if p <= {'not_requested'}:
        return 'not_requested'
    if p <= {'completed', 'not_requested'}:
        return 'completed'
    if p <= {'not_started', 'not_requested'}:
        return 'not_started'
    if p <= {'reverted', 'not_started', 'not_requested'}:
        return 'reverted'
    return 'partial'


def acyclic(edges: list[list[str]]) -> bool:
    graph: dict[str, set[str]] = {}
    for a, b in edges:
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set())
    visiting: set[str] = set()
    done: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return False
        if node in done:
            return True
        visiting.add(node)
        if any(not visit(child) for child in graph[node]):
            return False
        visiting.remove(node)
        done.add(node)
        return True

    return all(visit(n) for n in graph)


def evaluate(case: dict[str, Any], rows: dict[str, dict[str, Any]]) -> dict[str, Any]:
    d = case['input']
    kind = case['kind']
    row = rows[case['binding']]
    if kind == 'co_evolution':
        fields = row['decision_rule']['conditions']
        verdict = conjoin([d.get(f) for f in fields])
        return {'verdict': verdict, 'co_evolution_permitted': verdict == 'satisfied'}
    if kind == 'reconstruction':
        reconstruction = conjoin([d.get(f) for f in row['decision_rule']['reconstruction_conditions']])
        action = d['action']
        if action == row['decision_rule']['unlawful_action']:
            lawful = 'falsified'
        else:
            conditions = row['decision_rule']['lawful_actions'][action]
            lawful = conjoin([d.get(c) for c in conditions])
        return {'reconstruction': reconstruction, 'lawfulness': lawful}
    if kind == 'cut':
        members = row['semantic_cut']['members']
        shape = set(d['members']) == set(members) and len(d['members']) == len(members)
        # A demonstrated incomplete cut is false; missing judgment evidence alone
        # remains unknown. j_a is deliberately not an input to cut assessment.
        values: list[bool | None] = [shape, d.get('claim_admitted'), d.get('event_admitted'),
                                   d.get('joins_equal'), d.get('frontier_current')]
        verdict = conjoin(values, d.get('basis_interpretable', True), d.get('capable', True))
        downstream = verdict == 'satisfied' and d.get('cut_judgment_admitted') is True
        return {'verdict': verdict, 'downstream_admitted': downstream}
    if kind == 'next_function':
        f = next(f for f in row['function_contracts'] if f['name'] == d['function'])
        if d['operation'] in f['forbidden']:
            return {'verdict': 'falsified', 'selected': False}
        if d.get('post_reprice') and not d.get('new_basis_admitted'):
            return {'verdict': 'satisfied', 'selected': False}
        result = conjoin([d.get('published'), d.get('target_bound'), d.get('authority')])
        return {'verdict': result, 'selected': result == 'satisfied'}
    if kind == 'compute':
        c = row['compute_predicates'][d['means']]
        verdict = conjoin([d.get(f) for f in c['requires']])
        return {'verdict': verdict, 'fitness': d.get('fitness', 'unassessed'),
                'acceptance': d.get('acceptance', 'unassessed')}
    if kind == 'effect':
        # Effect observations cannot be inferred from a request/authority label.
        if d.get('observed_parts'):
            effect = effect_join(d['observed_parts'])
        elif d.get('effect_free_scope_established'):
            effect = 'not_requested'
        elif d.get('authenticated_no_start'):
            effect = 'not_started'
        else:
            effect = 'unknown'
        readiness = conjoin([d.get('grant_matches'), d.get('pre_observation_current')])
        return {'readiness': readiness, 'effect': effect}
    if kind == 'typed_causality':
        types = ['identity', 'occurrence_cause', 'event_cause']
        return {'verdict': 'satisfied' if all(acyclic(d.get(k, [])) for k in types) else 'falsified'}
    if kind == 'schema':
        required = row['definition']['sorts'][d['sort']]
        valid = set(d['fields']) == set(required) and len(d['fields']) == len(required)
        return {'verdict': 'satisfied' if valid else 'falsified'}
    if kind == 'event_scope':
        if d.get('scope_supported') is None:
            return {'verdict': 'indeterminate', 'decision': 'hold'}
        if not d['scope_supported']:
            return {'verdict': 'falsified', 'decision': 'out_of_scope'}
        if d.get('capable') is False:
            return {'verdict': 'out_of_frame', 'decision': 'hold'}
        return {'verdict': 'satisfied', 'decision': 'admitted'}
    raise AssertionError(f'Unknown finite fixture kind: {kind}')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    raw = (HERE / 'bindings.json').read_bytes()
    package: dict[str, Any] = json.loads(raw)
    account_raw = frozen('fe4fcbe', ACCOUNT)
    assert digest(account_raw) == ACCOUNT_SHA
    account: dict[str, Any] = json.loads(account_raw)
    assert package['schema_version'] == 'stdo.semantic-contribution.v1'
    assert package['source_commit'] == SOURCE
    assert package['input_account_sha256'] == ACCOUNT_SHA
    owners = set(package['owner_paths'])
    assigned = {r['id']: r for r in account['determinations'] if r['owner']['path'] in owners}
    rows = {r['id']: r for r in package['bindings']}
    assert len(rows) == len(package['bindings']) == 141
    assert set(rows) == set(assigned)
    assert not package['unfinished_ids'] and not package['unchanged_ready_ids']
    source_members: list[dict[str, Any]] = []
    contents: dict[str, bytes] = {}
    for member in package['source_members']:
        body = frozen(SOURCE, SOURCE_ROOT + member['path'])
        assert digest(body) == member['sha256']
        assert len(body) == member['bytes']
        contents[member['path']] = body
        source_members.append({'path': member['path'], 'sha256': digest(body), 'bytes': len(body)})
    all_ids = {r['id'] for r in account['determinations']}
    for rid, row in rows.items():
        o = assigned[rid]['owner']
        lines = contents[o['path']].splitlines(keepends=True)
        assert digest(b''.join(lines[o['start_line'] - 1:o['end_line']])) == o['body_sha256'], rid
        assert row['owner_body_sha256'] == o['body_sha256'], rid
        assert row['applicability']['when'] and row['applicability']['unknown']
        assert row['argument']['conditional_consequence'] and row['argument']['policy_choices']
        assert set(row['dependencies']) <= all_ids, rid
        assert set(row['dependencies']) == {d['id'] for d in row['dependency_relations']}, rid
        assert all(d['kind'] for d in row['dependency_relations'])
        assert VERDICTS <= set(row['result_mapping']), rid
        if row['representation_kind'] in {'definition_data', 'non_deciding_locator'}:
            assert row['predicate'] is None and row['definition'], rid
        elif row['representation_kind'] == 'constraint':
            assert row['predicate'] and row['obligations'] and row['inputs'], rid
        else:
            assert row['representation_kind'] == 'consumer_binding'
            assert row['definition'] and row['dependencies'], rid
        assert all(i['description'] and i['required_when'] and i['standing'] == 'external_required'
                   for i in row['inputs']), rid
    # Finite population and inherited-field checks catch omitted table rows and
    # accidental promotion of commentary into a field, independent of examples.
    prefix = 'TRAVERSAL_OCCURRENCE_PROFILE.'
    sorts = rows[prefix + 'closed-semantic-object-sorts']['definition']['sorts']
    assert len(sorts) == 19
    assert sorts['SubjectBinding'] == ['subject_ref', 'authority_ref', 'invalidation_ref']
    assert all(all(';' not in f and ' ' not in f for f in fields) for fields in sorts.values())
    domains = rows[prefix + 'finite-reference-domain-table']['definition']
    assert len(domains['rows']) == 144
    assert len({r['qualified_field'] for r in domains['rows']}) == 144
    assert len(domains['judgment_fields']) == 19
    assert len(rows[prefix + 'closed-relation-families']['definition']['relations']) == 24
    kinds = rows[prefix + 'closed-constraint-judgment-residual-and-stop-kinds']['definition']
    assert [len(kinds[k]) for k in ['constraints', 'judgments', 'residuals', 'stops']] == [11, 8, 8, 6]
    assert rows['ODD_METHOD.probabilistic-compute']['compute_predicates']['F_D']['concept_identity'] not in kinds['functor_kinds']
    fixtures = json.loads((HERE / 'semantic_cases.json').read_text())
    results: list[dict[str, Any]] = []
    for case in fixtures['cases']:
        actual = evaluate(case, rows)
        assert actual == case['expected'], (case['id'], actual, case['expected'])
        results.append({'id': case['id'], 'binding': case['binding'], 'actual': actual, 'passed': True})
    installed = json.loads(subprocess.check_output([
        'stdo', 'verify', 'v2.5.1-rc.2', '--manifest-sha256',
        '3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782'
    ], cwd=ROOT))
    assert installed['valid'] is True and not installed['failures']
    result = {
        'standing': 'bounded reproducible author check; no independent fidelity, acceptance or runtime claim',
        'bindings_sha256': digest(raw), 'account_sha256': digest(account_raw),
        'source_commit': SOURCE, 'source_members': source_members,
        'coverage': {'assigned': len(assigned), 'represented': len(rows), 'unfinished': [],
                     'previous_standing': dict(Counter(r['interpretation_standing'] for r in assigned.values()))},
        'installed_builder': {'cut': installed['cut'], 'valid': installed['valid'],
                              'manifest_sha256': installed['manifest_sha256']},
        'behavioral_cases': results,
        'limitations': ['Finite authored case models, not live adopting runtime execution.',
                       'Pins and population checks do not prove all-row semantic fidelity.',
                       'No independent assessor, external grant, current world truth or release acceptance is established.']
    }
    if args.output:
        output = args.output.resolve()
        assert output.parent == HERE, 'Output must remain in the construction grant'
        output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'passed': True, 'rows': len(rows), 'behavioral_cases': len(results),
                      'bindings_sha256': digest(raw), 'installed_valid': True}))


if __name__ == '__main__':
    main()
