#!/usr/bin/env python3
"""Inspect emitted acquisition routes without loading full projections into chat."""
import collections
import hashlib
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
replay = json.loads((OUT / 'projection_reproduction.json').read_text())
frames = json.loads((OUT / 'frame_reproduction.json').read_text())
package = Path(frames['subjects']['codex']['scratch_archive_root']) / 'specification_methodology/v3/build_tenants/codex/successor'
account = json.loads((package / 'interpretation/source-account.json').read_bytes())
owners = {r['id']: r['owner'] for r in account['determinations']}
def sha(b):
    return hashlib.sha256(b).hexdigest()
def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()
def decoded(value):
    return json.loads(value) if isinstance(value, str) else value
def pointer(base, address):
    for term in address.lstrip('/').split('/') if address else []:
        term = term.replace('~1', '/').replace('~0', '~')
        base = base[int(term)] if isinstance(base, list) else base[term]
    return base

out = []
for replayed in replay['projections']:
    data = (Path(replay['scratch_output_root']) / (replayed['id'] + '.json')).read_bytes()
    assert sha(data) == replayed['output_sha256']
    doc = json.loads(data)
    clause = next(c for c in doc['clauses'] if c['uri'].endswith(replayed['id']))
    semantic = decoded(next(a['literal'] for a in clause['arguments'] if a['role'].endswith('#semantic-record')))
    routes = [decoded(a['literal']) for a in clause['arguments'] if a['role'].endswith('#acquisition-route')]
    qualification_checks, pin_checks, details = [], [], []
    for route in routes:
        q = route.get('qualification_ref')
        if q:
            assert q['scope'] == 'semantic-record', 'Uncovered inline scope needs separate analysis'
            value = pointer(semantic, q['pointer'])
            qualification_checks.append({'pointer': q['pointer'], 'digest_matches': sha(canonical(value)) == q['sha256'], 'required_when_matches': route.get('required_when') == value.get('required_when')})
        target_id = route['target'].rsplit(':', 1)[-1]
        owner = owners[target_id]
        raw = (package / owner['path']).read_bytes()
        selected = b''.join(raw.splitlines(keepends=True)[owner['start_line']-1:owner['end_line']])
        pin_checks.append({'target': target_id, 'member_matches': sha(raw) == route['source_member_sha256'], 'body_matches': sha(selected) == route['source_body_sha256'], 'source_account_body_matches': sha(selected) == owner['body_sha256']})
        if route['relation'] != 'foundation-premise-owner':
            details.append({'acquisition': route['acquisition'], 'target': target_id, 'required_when': route.get('required_when'), 'in_native_closure': route['target'] in doc['closure']['clauses']})
    out.append({'id': replayed['id'], 'materialized_output_bytes': len(data), 'native_clause_count': len(doc['clauses']), 'native_clauses': doc['closure']['clauses'], 'root_route_counts': dict(collections.Counter(r['acquisition'] for r in routes)), 'qualification_checks': qualification_checks, 'source_pin_checks': pin_checks, 'non_premise_routes': details})
(OUT / 'projection_route_checks.json').write_text(json.dumps(out, indent=2) + '\n')
for row in out:
    print(json.dumps({'id': row['id'], 'clauses': row['native_clause_count'], 'route_kinds': row['root_route_counts'], 'qualifications_valid': all(x['digest_matches'] and x['required_when_matches'] for x in row['qualification_checks']), 'all_source_pins_valid': all(all(x[k] for k in ('member_matches', 'body_matches', 'source_account_body_matches')) for x in row['source_pin_checks']), 'non_premise_routes': row['non_premise_routes']}))
