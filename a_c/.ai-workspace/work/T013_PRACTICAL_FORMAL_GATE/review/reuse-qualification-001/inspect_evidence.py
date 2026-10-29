"""Independent public-evidence inspection. Standard library; no product imports.

No proof, compiler, actor, private origin, key, cache or Git operations.
Writes only CHECKS.json alongside this Reviewer artifact.
"""
from pathlib import Path
from collections import deque
from datetime import datetime
import ast
import copy
import hashlib
import json
import re

AC = Path('/Users/jim/src/apps/specification_methodology/a_c')
W = AC / '.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE'
Q = W / 'reuse/qualification-001'
OUT = Path(__file__).resolve().parent
LEAN = AC / 'build_tenants/lean'
ORIGIN = '.cache/formal-origin-v1/selection.json'


def load(path):
    assert 'formal-origin-v1' not in path.parts, 'Private origin is outside review grant'
    return json.loads(path.read_bytes())


def sha(path):
    assert 'formal-origin-v1' not in path.parts, 'Private origin is outside review grant'
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':'), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


public = load(OUT / 'PUBLIC_HASHES.json')['members']


def retained_hash(path):
    return public[path.relative_to(Q).as_posix()]['sha256']


integration = load(W / 'reuse/integration-001/SOURCE-PINS.json')
source_pins = integration['after'] | integration['conserved_source_pins']
assert all(sha(AC / name) == expected for name, expected in source_pins.items())
identity = load(Q / 'RUNTIME-IDENTITY.json')
baseline = load(Q / 'BASELINE.json')
assert digest(identity['pins']) == identity['sha256'] == '065648e6cc971be7edc75c1fa7b0428351357fe312146059b71fb788842313a7'
portable = {k: v for k, v in identity['pins'].items() if k != ORIGIN}
assert portable == baseline['runtime_identity']['pins'] == integration['runtime_identity']['pins']
assert digest(portable) == '07f423004952338c7ce4273e2fe1f17556b0c96803caa4a355859762750e9601'
assert all(sha(LEAN / name) == expected for name, expected in portable.items())
support_pin = identity['pins']['profiles/proof-support-v1.json']
assert support_pin == '7198879c3dfefe52ee4c980b33990197cd338eb19ac4e84cce3dd26a4cd66363'
checker = load(Q / 'checker.json')
assert checker['runtime_identity'] == identity
assert sha(Path(checker['python']['path'])) == checker['python']['sha256']
assert checker['adapter_sha256'] == sha(AC / 'build_tenants/graphify/code/ac_formal_gate.py')
assert checker['entry_sha256'] == sha(LEAN / 'scripts/formal_gate.py')
prior_scale = load(W / 'lean/scale-closure-001/SOURCE.json')['runtime_identity']['pins']
changed_from_scale = sorted(k for k in set(prior_scale) | set(portable) if prior_scale.get(k) != portable.get(k))
assert changed_from_scale == ['scripts/formal_gate.py', 'scripts/formal_reuse.py']

constants = {}
for node in ast.parse((LEAN / 'scripts/import_fixture.py').read_text()).body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in ('FAMILIES', 'VARIANTS'):
                constants[target.id] = ast.literal_eval(node.value)
families, variants = constants['FAMILIES'], constants['VARIANTS']


def independently_reconstruct(directory):
    """Reconstruct every retained record/reference and the selected view."""
    request, source, actual = (load(directory / n) for n in ('request.json', 'model.json', 'actual-runtime.log'))
    if request['input']['format'] == 'carrier':
        carrier = load(directory / 'input.json')
        metadata = [n['ac_payload'] for n in carrier['nodes'] if n['ac_role'] == 'metadata']
        assert len(metadata) == 1
        recovered = copy.deepcopy(metadata[0]['envelope'])
        records = [n['ac_payload'] for n in carrier['nodes'] if n['ac_role'] == 'record']
        recovered['populations'] = {f: [x['record'] for x in sorted(records, key=lambda x: x['ordinal']) if x['family'] == f] for f in families}
        assert recovered == source
        raw = retained_hash(directory / 'model.json')
    else:
        assert load(directory / 'input.json') == source
        raw = retained_hash(directory / 'input.json')
    flat = [(family, record) for family in families for record in source['populations'][family]]
    indices = {r['id']: i for i, (_, r) in enumerate(flat)}
    records = [dict(key=i, identity=r['id'], family=f, context=r['context'], owner=r['owner'], scope=canonical(r['scope']), basis=r['basis'], payload=canonical(r)) for i, (f, r) in enumerate(flat)]
    refs = []

    def scan(value, schema, owner, path):
        if schema['type'] == 'ref':
            refs.append(dict(owner=owner, path=[{'index' if type(x) is int else 'field': x} for x in path], target={'local': indices[value]} if value in indices else {'external': value}, governing=schema['governing'], domain=schema['domain']))
        elif schema['type'] == 'array':
            for i, item in enumerate(value):
                scan(item, schema['items'], owner, path + [i])
        elif schema['type'] == 'object':
            for key in sorted(schema['fields']):
                scan(value[key], schema['fields'][key], owner, path + [key])

    definition = source['signature']['definition']
    for record_id in sorted(indices):
        i = indices[record_id]
        family, record = flat[i]
        fields = dict(definition['fields'][family])
        if family in variants:
            group, selector = variants[family]
            fields.update(definition[group][record[selector]])
        for field in sorted(fields):
            scan(record[field], fields[field], i, [field])
    edges = {(r['owner'], r['target']['local']) for r in refs if r['governing'] and 'local' in r['target']}
    contract = source['dependency_contract']
    for i, (family, record) in enumerate(flat):
        if family == 'relations' and record['kind'] in contract['required_relation_kinds']:
            if record['source'] in indices:
                edges.update(((indices[record['source']], i), (i, indices[record['source']])))
            if record['target'] in indices:
                edges.add((i, indices[record['target']]))
        if family in contract['attachment_families']:
            for name in ([record['subject']] if family == 'residuals' else record['applies_to']):
                if name in indices:
                    edges.add((indices[name], i))
    envelope = {k: v for k, v in source.items() if k != 'populations'}
    externals = [dict(identity=e['external_identity'], payload=canonical(e)) for e in source['external_resolutions']]
    expected_model = dict(identity=source['id'], rawSha256=raw, canonicalSha256=digest(source), envelope=canonical(envelope), records=records, references=refs, externalResolutions=externals, edges=[list(e) for e in sorted(edges)], invalidation=canonical(source['interpretation']['invalidation']))
    assert actual['model'] == expected_model
    selection, = request['selections']
    seeds = [indices[x] for x in selection['seeds']]
    selected = set(seeds)
    queue = deque(seeds)
    adjacency = {i: [] for i in range(len(records))}
    for a, b in sorted(edges):
        adjacency[a].append(b)
    while queue:
        for target in adjacency[queue.popleft()]:
            if target not in selected:
                selected.add(target)
                queue.append(target)
    included, excluded = sorted(selected), sorted(set(range(len(records))) - selected)
    selected_refs = [r for r in refs if r['owner'] in selected]
    external_ids = {r['target']['external'] for r in selected_refs if 'external' in r['target']}
    external = [e for e in externals if e['identity'] in external_ids]
    ordinary = [r for r in selected_refs if 'local' in r['target'] and r['target']['local'] not in selected]
    unresolved = [records[i] for i in included if flat[i][0] == 'residuals']
    projection = dict(parentIdentity=source['id'], parentRawSha256=raw, parentCanonicalSha256=digest(source), parentEnvelope=canonical(envelope), seeds=seeds, included=included, excluded=excluded, records=[records[i] for i in included], external=external, ordinary=ordinary, unresolved=unresolved, excludedResiduals=[records[i] for i in excluded if flat[i][0] == 'residuals'], invalidation=canonical(source['interpretation']['invalidation']))
    assert actual['views'] == [dict(status='verified', projection=projection)]
    crossing = [r for i, (f, r) in enumerate(flat) if f == 'relations' and i not in selected and (indices.get(r['source']) in selected or indices.get(r['target']) in selected)]
    expected_view = dict(profile='a_c.graphify.projection/1', parent=dict(id=source['id'], sha256=digest(source), profile=source['profile']), selection=dict(seeds=selection['seeds'], dependency_contract=contract, budget_records=selection['budget_records']), included=sorted(flat[i][1]['id'] for i in included), excluded=sorted(flat[i][1]['id'] for i in excluded), populations={f: [flat[i][1] for i in included if flat[i][0] == f] for f in families}, boundary=dict(external=sorted((e for e in source['external_resolutions'] if e['external_identity'] in external_ids), key=lambda e: e['external_identity']), unresolved_residuals=sorted(r['identity'] for r in unresolved), crossing_relations=[{k:r[k] for k in ('id','kind','source','target')} for r in crossing], non_governing_references=[dict(owner=flat[r['owner']][1]['id'], path=[str(next(iter(s.values()))) for s in r['path']], target=flat[r['target']['local']][1]['id'], domain=r['domain']) for r in ordinary], invalidation=source['interpretation']['invalidation']), claim='view of exact parent; not a replacement complete model or semantic acceptance')
    assert load(directory / 'supplied-views.json') == [expected_view]
    return dict(records=len(records), references=len(refs), edges=len(edges), external_resolutions=len(externals), selected_indices=included, retained_unresolved=len(unresolved), view_external=len(external))


subject_counts = {label: independently_reconstruct(Q / label) for label in ('small-cold', 'full-cold')}
assert subject_counts['full-cold'] == dict(records=1987, references=16498, edges=3995, external_resolutions=1021, selected_indices=[0,9,10,664,666,866,867,869,1825], retained_unresolved=1, view_external=18)
prior_bundle = W / 'lean/public-positive-002'
conserved_prior_artifacts = ['GateData.lean','GateLocalNames.lean','GateExternalNames.lean','GateIdentities.lean','GateBounds.lean','GateModel.lean','GateViews.lean','GateRun.lean','actual-runtime.log','input.json','model.json','certificates.json','supplied-views.json']
for name in conserved_prior_artifacts:
    assert sha(prior_bundle / name) == retained_hash(Q / 'full-cold' / name), name

allowed_axioms = {'propext', 'Classical.choice', 'Quot.sound'}
labels = ['small-cold', 'small-reuse-1', 'small-reuse-2', 'full-cold', 'full-reuse']
run_summaries = []
measurement = load(Q / 'MEASUREMENTS.json')
origin_selection = load(Q / 'ORIGIN-SELECTION.json')
assert identity['pins'][ORIGIN] == origin_selection['origin_selection_pin']
init = load(Q / 'init-origin.external.json')
assert init['origin_before']['present'] is False and init['origin_after'] == origin_selection['origin_counts']
assert init['origin_after']['entry_count'] == init['origin_after']['pending_count'] == 0
assert init['returned'] == origin_selection['public_setup_response']
assert init['expected_argv'][-1] == 'init-origin' and init['returncode'] == 0
previous_time = datetime.fromisoformat(init['finished_utc'])
for label in labels:
    directory = Q / label
    result, manifest, request = (load(directory / n) for n in ('result.json','manifest.json','request.json'))
    external = load(Q / (label + '.external.json'))
    hint = load(directory / 'local-origin.json')
    obs = result['observations']
    assert result == external['returned'] == load(Q / (label + '.stdout'))
    assert result['status'] == 'verified' and external['returncode'] == 0
    assert external['stdout_sha256'] == retained_hash(Q / (label + '.stdout'))
    assert external['stderr_sha256'] == retained_hash(Q / (label + '.stderr'))
    assert result['runtime_identity'] == identity and result['checked_claims'] == result['requested_claims']
    assert result['request_sha256'] == digest(request)
    assert result['evidence']['members'] == manifest['members']
    assert result['evidence']['manifest_sha256'] == retained_hash(directory / 'manifest.json')
    assert all(Path(name).name == name and retained_hash(directory / name) == expected for name, expected in manifest['members'].items())
    assert {p.name for p in directory.iterdir()} == set(manifest['members']) | {'result.json','manifest.json','local-origin.json'}
    for key, filename in [('input','input.json'),('supplied_views','supplied-views.json')]:
        assert result['inputs'][key]['raw_sha256'] == request[key]['raw_sha256'] == retained_hash(directory / filename)
    assert obs['support'] == dict(manifest_sha256=support_pin, members=30405, platform='Darwin-arm64')
    assert obs['limits'] == dict(max_input_bytes=33554432, max_selections=64, memory_mb=4096, timeout_seconds=90)
    assert external['outer_seconds'] == 600 and external['checking_seconds'] == 90 and external['lean_memory_mb'] == 4096
    assert external['physical_rss_cap'] is False
    assert obs['elapsed_seconds'] <= external['external_invocation_seconds'] < 600
    assert datetime.fromisoformat(external['started_utc']) >= previous_time
    previous_time = datetime.fromisoformat(external['finished_utc'])
    assert external['expected_argv'][:7] == [checker['python']['path'],'-I','-S','-B','-X','pycache_prefix=/dev/null',str(LEAN / 'scripts/formal_gate.py')]
    measured = next(x for x in measurement['runs'] if x['label'] == label)
    assert measured['external_seconds'] == external['external_invocation_seconds']
    assert measured['external_child_high_water_rss_bytes'] == external['child_high_water_rss_bytes']
    assert measured['stages'] == obs['stages']
    cold = label.endswith('-cold')
    expected_counts = (7,1,1) if cold else (0,0,0)
    assert tuple(obs[k] for k in ('current_dynamic_proof_invocations','current_kernel_replay_invocations','current_runtime_invocations')) == expected_counts
    assert all(s['seconds'] < 90 and s.get('exit_code', 0) == 0 for s in obs['stages'])
    stage_names = [s['stage'] for s in obs['stages']]
    assert stage_names[:3] == ['acquire-import-reconstruct','support-pins','current-certificates']
    assert stage_names[-3:] == ['output-view-correspondence','support-pins-after','origin-currentness']
    found_audits = {}
    for name in ['GateLocalNames','GateExternalNames','GateIdentities','GateBounds','GateModel','GateViews']:
        log = (directory / (name + '.log')).read_text()
        found_audits.update({n: sorted(a.strip() for a in values.split(',') if a.strip()) for n, values in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log)})
        found_audits.update({n: [] for n in re.findall(r"'([^']+)' does not depend on any axioms", log)})
    assert found_audits == obs['theorem_audit']
    assert all(set(v) <= allowed_axioms for v in found_audits.values())
    assert len(found_audits) == (62 if label.startswith('full') else 6)
    if cold:
        assert hint['layout'] == 'cold' and 'original_establishment' not in obs
        assert external['expected_argv'][7] == 'verify'
        assert stage_names[3:-3] == ['GateData','GateLocalNames','GateExternalNames','GateIdentities','GateBounds','GateModel','GateViews','dynamic-kernel-replay','actual-runtime']
        assert external['origin_after']['entry_count'] == external['origin_before']['entry_count'] + 1
    else:
        original_dir = Q / ('small-cold' if label.startswith('small') else 'full-cold')
        original = load(original_dir / 'result.json')
        original_hint = load(original_dir / 'local-origin.json')
        assert hint == original_hint | {'layout': 'reuse'}
        assert stage_names[3:-3] == ['authenticated-artifacts']
        assert obs['reuse'] == 'local-origin' and 'retained authenticated cold runtime' in obs['execution']
        assert external['origin_before'] == external['origin_after']
        for name in ('result.json','manifest.json','request.json','replay-request.json'):
            assert retained_hash(directory / ('origin-' + name)) == retained_hash(original_dir / name)
        for name, expected in original['evidence']['members'].items():
            mapped = 'origin-' + name if name in ('request.json','replay-request.json') else name
            assert retained_hash(directory / mapped) == expected
        for key in ('checked_claims','requested_claims','model','inputs','selections','context_binding','limits'):
            assert result[key] == original[key]
        assert obs['original_establishment']['result_sha256'] == retained_hash(original_dir / 'result.json')
        assert obs['original_establishment']['manifest_sha256'] == retained_hash(original_dir / 'manifest.json')
        expected_parent = Q / ('small-reuse-1' if label == 'small-reuse-2' else original_dir.name)
        assert external['expected_argv'][7:10] == ['check-evidence','--bundle',str(expected_parent)]
    assert hint['origin_id'] == init['returned']['origin_id']
    assert external['origin_before']['pending_count'] == external['origin_after']['pending_count'] == 0
    run_summaries.append(dict(label=label, result_sha256=retained_hash(directory / 'result.json'), entry_id=hint['entry_id'], current_invocations=expected_counts, audit_count=len(found_audits), external_seconds=external['external_invocation_seconds'], internal_seconds=obs['elapsed_seconds'], child_high_water_rss_bytes=external['child_high_water_rss_bytes']))

prepared = load(Q / 'CONTROLS-PREPARED.json')
original_dir = Q / 'small-cold'
assert all(retained_hash(original_dir / name) == expected for name, expected in prepared['original_bundle_members'].items())
control_summaries = []
for case in prepared['controls']:
    name = case['control']
    external = load(Q / ('control-' + name + '.external.json'))
    assert external['returned'] == load(Q / ('control-' + name + '.stdout'))
    assert external['returncode'] == case['expected_exit'] == 2
    assert external['returned']['status'] == case['expected_status'] == 'refused'
    assert external['returned']['reason'] == case['expected_reason']
    assert external['origin_before'] == external['origin_after']
    assert external['origin_after']['entry_count'] == 2 and external['origin_after']['pending_count'] == 0
    assert not (Q / ('control-' + name)).exists()
    assert datetime.fromisoformat(external['started_utc']) >= previous_time
    previous_time = datetime.fromisoformat(external['finished_utc'])
    if name != 'boolean-budget':
        directory = Q / 'controls' / name
        manifest, result = load(directory / 'manifest.json'), load(directory / 'result.json')
        assert all(retained_hash(directory / k) == v for k, v in manifest['members'].items())
        assert manifest['members'] == result['evidence']['members']
        assert result['evidence']['manifest_sha256'] == retained_hash(directory / 'manifest.json')
        changed = {k: {'before': v, 'after': retained_hash(directory / k)} for k, v in prepared['original_bundle_members'].items() if retained_hash(directory / k) != v}
        assert changed == case['changed_public_files']
        for k in prepared['original_bundle_members']:
            assert (directory / k).stat().st_ino != (original_dir / k).stat().st_ino
    if name == 'typed-context':
        changed_context = load(Q / 'controls/typed-context/request.json')['context_binding']
        original_context = load(original_dir / 'request.json')['context_binding']
        assert changed_context == original_context and canonical(changed_context) != canonical(original_context)
        assert type(changed_context['activation_identity']['trial_ordinal']) is bool
        assert type(original_context['activation_identity']['trial_ordinal']) is int
    elif name == 'boolean-budget':
        assert type(load(Q / 'controls/boolean-budget-request.json')['selections'][0]['budget_records']) is bool
    elif name == 'stale-pin':
        changed_identity = load(Q / 'controls/stale-pin/result.json')['runtime_identity']
        assert digest(changed_identity['pins']) == changed_identity['sha256']
        assert [k for k in identity['pins'] if identity['pins'][k] != changed_identity['pins'][k]] == ['scripts/gate_codegen.py']
    elif name == 'omitted-residual':
        old_view, = load(original_dir / 'supplied-views.json')
        changed_view, = load(Q / 'controls/omitted-residual/supplied-views.json')
        missing = case['omitted_identity']
        assert len(old_view['populations']['residuals']) == 1 and changed_view['populations']['residuals'] == []
        assert old_view['boundary']['unresolved_residuals'] == [missing] and changed_view['boundary']['unresolved_residuals'] == []
        assert set(old_view['included']) - set(changed_view['included']) == {missing}
    elif name == 'runtime-tamper':
        altered = load(Q / 'controls/runtime-tamper/actual-runtime.log')
        original = load(original_dir / 'actual-runtime.log')
        assert altered['model'] == original['model']
        payload = json.loads(altered['views'][0]['projection']['records'][0]['payload'])
        assert payload.pop('qualification_tamper') is True
        assert payload == json.loads(original['views'][0]['projection']['records'][0]['payload'])
    control_summaries.append(dict(control=name, reason=external['returned']['reason'], early_no_output=True, public_hashes_refreshed=name != 'boolean-budget', external_seconds=external['external_invocation_seconds']))

report = dict(status='passed', scope='Read-only public source/evidence comparisons; no product execution, proof, private origin or key read', source_pin_count=len(source_pins), portable_runtime_pins=len(portable), full_runtime_identity=identity['sha256'], support_manifest_sha256=support_pin, prior_scale_changed_runtime_paths=changed_from_scale, exact_prior_full_artifacts_conserved=conserved_prior_artifacts, reconstructed_subjects=subject_counts, runs=run_summaries, controls=control_summaries, full_ratio=run_summaries[3]['external_seconds']/run_summaries[4]['external_seconds'], actual_worker_delivery_or_benefit_established=False, origin_free_installed_fallback_established=False)
(OUT / 'CHECKS.json').write_text(json.dumps(report, sort_keys=True, indent=2) + '\n')
print(json.dumps({k: report[k] for k in ('status','source_pin_count','portable_runtime_pins','reconstructed_subjects','full_ratio')}, sort_keys=True))
