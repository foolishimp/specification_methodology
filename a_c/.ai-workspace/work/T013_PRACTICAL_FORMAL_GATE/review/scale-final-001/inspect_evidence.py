"""Read-only independent comparison of the three retained full-size runs.

Uses standard library only; invokes no tenant module, compiler or gate.
"""
from pathlib import Path
from collections import deque
import ast
import copy
import hashlib
import json
import re

ROOT = Path('/Users/jim/src/apps/specification_methodology/a_c')
LEAN = ROOT / 'build_tenants/lean'
WORK = ROOT / '.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE/lean'


def sha(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def load(path):
    return json.loads(path.read_bytes())


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':'))


constants = {}
for node in ast.parse((LEAN / 'scripts/import_fixture.py').read_text()).body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in ('FAMILIES', 'VARIANTS'):
                constants[target.id] = ast.literal_eval(node.value)
families, variants = constants['FAMILIES'], constants['VARIANTS']
source_path = ROOT / 'applications/stdo-v3-common-35fb4824/run/repaired-proposal/model.json'
assert sha(source_path) == '70feb48cf657bcb20231dbfffe0c2076e5e69b24aeb0f226a001a22957b7f56a'
source = load(source_path)
flat = [(family, record) for family in families for record in source['populations'][family]]
indices = {record['id']: i for i, (_, record) in enumerate(flat)}
records = [dict(key=i, identity=r['id'], family=f, context=r['context'], owner=r['owner'],
                scope=canonical(r['scope']), basis=r['basis'], payload=canonical(r))
           for i, (f, r) in enumerate(flat)]
refs = []


def scan(value, schema, owner, path):
    kind = schema['type']
    if kind == 'ref':
        refs.append(dict(owner=owner,
                         path=[{'index' if type(x) is int else 'field': x} for x in path],
                         target={'local': indices[value]} if value in indices else {'external': value},
                         governing=schema['governing'], domain=schema['domain']))
    elif kind == 'array':
        for i, item in enumerate(value):
            scan(item, schema['items'], owner, path + [i])
    elif kind == 'object':
        for key in sorted(schema['fields']):
            scan(value[key], schema['fields'][key], owner, path + [key])


definition = source['signature']['definition']
for identity in sorted(indices):
    owner = indices[identity]
    family, record = flat[owner]
    fields = dict(definition['fields'][family])
    if family in variants:
        group, selector = variants[family]
        fields.update(definition[group][record[selector]])
    for field in sorted(fields):
        scan(record[field], fields[field], owner, [field])
edges = {(r['owner'], r['target']['local']) for r in refs if r['governing'] and 'local' in r['target']}
dependency = source['dependency_contract']
for i, (family, record) in enumerate(flat):
    if family == 'relations' and record['kind'] in dependency['required_relation_kinds']:
        if record['source'] in indices:
            edges.update(((indices[record['source']], i), (i, indices[record['source']])))
        if record['target'] in indices:
            edges.add((i, indices[record['target']]))
    if family in dependency['attachment_families']:
        for name in ([record['subject']] if family == 'residuals' else record['applies_to']):
            if name in indices:
                edges.add((indices[name], i))
envelope = {key: value for key, value in source.items() if key != 'populations'}
source_canonical = hashlib.sha256(canonical(source).encode()).hexdigest()
externals = [dict(identity=e['external_identity'], payload=canonical(e)) for e in source['external_resolutions']]
expected_model = dict(identity=source['id'], rawSha256=sha(source_path), canonicalSha256=source_canonical,
                      envelope=canonical(envelope), records=records, references=refs,
                      externalResolutions=externals, edges=[list(e) for e in sorted(edges)],
                      invalidation=canonical(source['interpretation']['invalidation']))

expectations = load(WORK / 'view-expectations-001/EXPECTATIONS.json')
selection = expectations['selection']
seeds = [indices[name] for name in selection['seeds']]
seen = set(seeds)
pending = deque(seeds)
trace = []
adjacency = {i: [] for i in range(len(records))}
for a, b in sorted(edges):
    adjacency[a].append(b)
while pending:
    for target in adjacency[pending.popleft()]:
        if target not in seen:
            seen.add(target)
            pending.append(target)
            trace.append(target)
included = sorted(seen)
excluded = sorted(set(range(len(records))) - seen)
assert included == expectations['required_indices']
selected_refs = [r for r in refs if r['owner'] in seen]
external_ids = {r['target']['external'] for r in selected_refs if 'external' in r['target']}
external = [e for e in externals if e['identity'] in external_ids]
ordinary = [r for r in selected_refs if 'local' in r['target'] and r['target']['local'] not in seen]
residuals = [records[i] for i in included if flat[i][0] == 'residuals']
excluded_residuals = [records[i] for i in excluded if flat[i][0] == 'residuals']
projection = dict(parentIdentity=source['id'], parentRawSha256=sha(source_path),
                  parentCanonicalSha256=source_canonical, parentEnvelope=canonical(envelope),
                  seeds=seeds, included=included, excluded=excluded,
                  records=[records[i] for i in included], external=external, ordinary=ordinary,
                  unresolved=residuals, excludedResiduals=excluded_residuals,
                  invalidation=canonical(source['interpretation']['invalidation']))
crossing = [r for i, (f, r) in enumerate(flat) if f == 'relations' and i not in seen
            and (indices.get(r['source']) in seen or indices.get(r['target']) in seen)]
expected_view = dict(profile='a_c.graphify.projection/1',
    parent=dict(id=source['id'], sha256=source_canonical, profile=source['profile']),
    selection=dict(seeds=selection['seeds'], dependency_contract=dependency, budget_records=9),
    included=sorted(flat[i][1]['id'] for i in included), excluded=sorted(flat[i][1]['id'] for i in excluded),
    populations={f: [flat[i][1] for i in included if flat[i][0] == f] for f in families},
    boundary=dict(external=sorted((e for e in source['external_resolutions'] if e['external_identity'] in external_ids), key=lambda e:e['external_identity']),
        unresolved_residuals=sorted(r['identity'] for r in residuals),
        crossing_relations=[{k:r[k] for k in ('id','kind','source','target')} for r in crossing],
        non_governing_references=[dict(owner=flat[r['owner']][1]['id'],
            path=[str(next(iter(s.values()))) for s in r['path']], target=flat[r['target']['local']][1]['id'], domain=r['domain']) for r in ordinary],
        invalidation=source['interpretation']['invalidation']),
    claim='view of exact parent; not a replacement complete model or semantic acceptance')
source_closure = load(WORK / 'scale-closure-001/SOURCE.json')
assert all(sha(LEAN / k) == v for k, v in source_closure['runtime_identity']['pins'].items())
assert all(sha(LEAN / k) == v for k, v in source_closure['additional_reviewed_source'].items())
closure = load(WORK / 'scale-closure-001/CLOSED.json')
assert all(sha(WORK / k) == v for k, v in closure['source_and_evidence_pins'].items())
runs = load(WORK / 'scale-closure-001/RUNS.json')['runs']
summary = []
allowed_axioms = {'propext', 'Classical.choice', 'Quot.sound'}
audits = {
 'GateLocalNames': [f'localCharsBlock{i}_source' for i in range(16)] + ['localChars_source','names_exact'],
 'GateExternalNames': [f'externalCharsBlock{i}_source' for i in range(8)] + ['externalChars_source'],
 'GateIdentities': [f'orderedPairsChecked{i}' for i in range(24)] + ['chars_reconstructed','ordered_chain','identities_checked'],
 'GateBounds':['edgeBounds','refBounds'], 'GateModel':['model_checked'],
 'GateViews':['checked0','set0','reachability0','result0','execution_matches_project0']}
for run in runs:
    path = WORK / run['name']
    result, manifest, request = (load(path / n) for n in ('result.json','manifest.json','request.json'))
    assert sha(path/'result.json') == run['result_sha256']
    assert sha(path/'manifest.json') == run['manifest_sha256'] == result['evidence']['manifest_sha256']
    assert manifest['members'] == result['evidence']['members']
    assert all(Path(k).name == k and not (path/k).is_symlink() and sha(path/k) == v for k,v in manifest['members'].items())
    assert sha(WORK/(run['name']+'.public-result.json')) == run['outer_observation_sha256']
    outer = load(WORK/(run['name']+'.public-result.json'))
    assert outer['command'][1:4] == ['-I','-S','-B'] and outer['outer_seconds'] == 600
    assert outer['external_elapsed_seconds'] == run['external_seconds'] < 600
    assert all(s['seconds'] < 90 and s.get('exit_code',0) == 0 for s in result['observations']['stages'])
    assert result['runtime_identity'] == source_closure['runtime_identity']
    assert hashlib.sha256(canonical(request).encode()).hexdigest() == result['request_sha256']
    assert sha(path/'input.json') == sha(source_path)
    actual = load(path/'actual-runtime.log')
    assert actual['model'] == expected_model
    for name, expected_names in audits.items():
        log = (path/(name+'.log')).read_text()
        found = {n:set(a.strip() for a in values.split(',') if a.strip()) for n,values in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]",log)}
        found.update({n:set() for n in re.findall(r"'([^']+)' does not depend on any axioms",log)})
        assert set(found) == {'AC.GateData.'+n for n in expected_names}
        assert all(values <= allowed_axioms for values in found.values())
    if run['name'] == 'public-underbudget-001':
        assert request['selections'][0] == dict(seeds=selection['seeds'],budget_records=8)
        assert actual['views'] == [dict(status='refused',reason='insufficient record budget; required closure is not truncated')]
        assert result['status'] == 'refused'
    else:
        assert actual['views'] == [dict(status='verified',projection=projection)]
        view = load(path/'supplied-views.json')
        assert sha(path/'supplied-views.json') == request['supplied_views']['raw_sha256']
        if run['name'] == 'public-positive-002':
            assert view == [expected_view]
            assert result['status'] == 'verified' and result['checked_claims'] == result['requested_claims']
        else:
            altered = copy.deepcopy(expected_view)
            altered['populations']['residuals'] = []
            assert view == [altered] and view != [expected_view]
            assert result['status'] == 'refused' and 'supplied-graphify-view-correspondence' not in result['checked_claims']
    summary.append(dict(name=run['name'],status=result['status'],members=len(manifest['members']),
                        external_seconds=outer['external_elapsed_seconds'],complete_model_equal=True,
                        proof_audit_names=sum(map(len,audits.values())),all_member_hashes_equal=True))
print(json.dumps(dict(source_identity=source_closure['runtime_identity']['sha256'],
    complete_source_records=len(records),complete_reference_occurrences=len(refs),complete_edges=len(edges),
    complete_externals=len(externals),included=included,trace=trace,external_boundary=len(external),
    retained_residuals=len(residuals),excluded_residuals=len(excluded_residuals),crossing_relations=len(crossing),
    source_reconstruction_and_actual_projection='exact',runs=summary,
    method='Standard-library read-only independent reconstruction; no tenant module, proof or runtime invocation'),indent=2))
