#!/usr/bin/env python3
"""Read-only author checks; stdout is the receipt. No semantic-fidelity oracle."""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / '.git').exists())
TENANT = 'specification_methodology/v3/build_tenants/codex/'
PATH = TENANT + 'qualification/C3/iteration-3/DETERMINATIONS.json'
OBSERVED = 'a6d5f00c484e4366e2efed35dc76c1b13ee5620a'
OBSERVED_SHA = '74b4140f328446ae60fd5a4a3ec17483264c1cef30086e391ebf8310e3d46044'
D1 = 'f2cb3e593757d094d008102551925e871a0204ff'
D2 = '6bcc4126efd54c41e412affc29e3801dc9deeb5b'

def sha(b):
    return hashlib.sha256(b).hexdigest()

def frozen(commit, path):
    return subprocess.check_output(['git','show',commit+':'+path], cwd=REPO)

def at_pointer(row, pointer):
    assert pointer.startswith('/')
    value = row
    for field in pointer[1:].split('/'):
        field = field.replace('~1','/').replace('~0','~')
        value = value[int(field)] if isinstance(value,list) else value[field]
    return value

account_bytes = frozen(OBSERVED, PATH)
assert sha(account_bytes) == OBSERVED_SHA
account = json.loads(account_bytes)
originals = {r['id']:r for r in account['determinations']}
selected = {r['id'] for r in account['determinations'] if r.get('unrepresented_scope')}
assert len(selected) == 25
binding_bytes = (HERE/'bindings.json').read_bytes()
j = json.loads(binding_bytes)
rows = j['bindings']
assert j['schema'] == 'stdo.semantic-contribution.v1'
assert j['input_account_sha256'] == 'ae5169eea86204a0d5d27915c6935604bb09d8d9a4feeb6cc403706a0ac42b12'
assert j['source_commit'] == D1 and j['documentary_source_commit'] == D2
assert j['observed_preimage_account']['sha256'] == OBSERVED_SHA
assert j['observed_preimage_account']['commit'] == OBSERVED
assert {r['id'] for r in rows} == selected and len(rows) == 25
assert j['completion']['completed_ids'] == sorted(selected)
assert j['completion']['unfinished_ids'] == j['unfinished_units'] == []
contracts = set(account['semantic_contracts'])
required = {'id','owner_body_sha256','source_member_sha256','owner',
            'representation_kind','interpretation_standing','applicability',
            'predicate','definition','obligations','permissions_exceptions',
            'dependencies','dependency_relations','inputs','result_mapping',
            'argument','source_clause_ids','source_clause_roles','unrepresented_scope'}
cache = {}
clause_count = 0
pointer_count = 0
for r in rows:
    assert required <= r.keys(), r['id']
    original = originals[r['id']]
    o = original['owner']
    path = TENANT+'successor/'+o['path']
    if path not in cache:
        cache[path] = frozen(D2,path)
        assert cache[path] == frozen(D1,path)
    source = cache[path]
    body = b''.join(source.splitlines(keepends=True)[o['start_line']-1:o['end_line']])
    assert r['owner'] == o
    assert sha(body) == r['owner_body_sha256'] == o['body_sha256']
    assert sha(source) == r['source_member_sha256']
    assert r['unrepresented_scope'] == []
    assert r['applicability'] and r['inputs'] and r['obligations']
    assert r['applicability'] != original['applicability']
    assert r['predicate'] is None or isinstance(r['predicate'],str) and r['predicate']
    if r['predicate'] is None:
        assert r['representation_kind'] == 'definition_data'
        assert isinstance(r['definition'],dict) and r['definition']['clauses']
        assert r['result_mapping']['contract_ref'] == 'core.shared_contracts.definition_data'
    assert r['result_mapping']['contract_ref'] in contracts
    assert r['result_mapping']['evaluation_contract_ref'] in contracts
    assert set(r['dependencies']) == {d['id'] for d in r['dependency_relations']}
    assert all(d in originals for d in r['dependencies'])
    assert all(d.get('kind') and d.get('binding') and d.get('required_when') for d in r['dependency_relations'])
    assert all(i.get('description') and i.get('required_when') and i.get('standing') == 'external_required_at_instance_not_missing_source' for i in r['inputs'])
    expected = [r['id']+'#'+c['id'] for c in original['source_clauses']]
    assert r['source_clause_ids'] == expected
    assert [m['source_clause_id'] for m in r['source_clause_roles']] == expected
    for c,m in zip(original['source_clauses'],r['source_clause_roles']):
        assert c['sha256'] == m['source_block_sha256'] == sha(source[c['byte_start']:c['byte_end']])
        assert c['byte_start'] == m['source_byte_start'] and c['byte_end'] == m['source_byte_end']
        assert m['source_block_id'] == c['id'] and m['source_roles'] == c['roles']
        assert m['represented_at']
        for target in m['represented_at']:
            assert target['role'] in {'D','O','P','A','R'}
            assert at_pointer(r,target['pointer'])
            pointer_count += 1
        clause_count += 1
comparison = json.loads((HERE/'COMPARISON.json').read_text())
assert {r['id'] for r in comparison['rows']} == selected
assert all(r['source_comparison_findings_and_repairs'] and r['remaining_material_source_omissions'] == [] for r in comparison['rows'])
scope = json.loads((HERE/'SOURCE_SCOPE.json').read_text())
assert {r['id'] for r in scope['selected_source_units']} == selected
assert scope['selected_owner_members_identical_D1_D2'] is True
print(json.dumps({
    'schema':'stdo.scoped-author-checks.v1',
    'result':'satisfied', 'scope':'Exact-source identity, selected-row structure and source-to-field pointer integrity only.',
    'bindings_sha256':sha(binding_bytes), 'observed_account_sha256':OBSERVED_SHA,
    'selected_rows':len(rows), 'source_blocks':clause_count, 'resolved_semantic_field_pointers':pointer_count,
    'definition_rows':sum(r['predicate'] is None for r in rows),
    'declared_unfinished_source_ids':[],
    'checks':['Frozen preimage digest and exact nonempty-unrepresented-scope selection',
              'Integration-base identity plus D2 source and observed-preimage binding',
              'Stable IDs, exact owner/body/member hashes and D1/D2 equality',
              'Every original source block mapped exactly once with its exact hash and byte coordinates',
              'Every block-to-field pointer resolves to nonempty authored semantic content',
              'Explicit definition/predicate distinction, actual instance inputs and typed dependency resolution',
              'Shared result-contract references resolve in the observed account',
              'All 25 comparisons and declared completion/unfinished sets agree'],
    'limitations':['Author checks are not independent fidelity, mathematical entailment or task-use qualification.',
                   'Pointer coverage does not prove that an authored statement preserves every source meaning.',
                   'No account/compiler/package generation, acceptance, release or paid actor execution was performed.']
},ensure_ascii=False,indent=2))
