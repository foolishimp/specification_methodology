"""Conserved independent reconstruction function from prior closed Reviewer; no product imports."""
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
