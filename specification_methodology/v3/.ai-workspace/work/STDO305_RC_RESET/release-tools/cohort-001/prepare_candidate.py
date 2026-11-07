"""Derive current cohort subjects from closed inventories and committed Git objects."""
import copy, hashlib, json, subprocess
from pathlib import Path
R = Path.cwd()
Q = R / 'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET'
W, T = Q / 'release-tools', Q / 'tools-skills'
O = Path(__file__).resolve().parent
D = R / 'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY'
V = '3.0.5-rc.1'
COMMON = 'specification_methodology/v3/build_tenants/common/'
sha = lambda b: hashlib.sha256(b).hexdigest()
def load(p): return json.loads(p.read_bytes())
def ref(p):
    b = p.read_bytes()
    return {'path': p.relative_to(R).as_posix(), 'sha256': sha(b), 'bytes': len(b)}
def save(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x') as f:
        json.dump(x, f, indent=2, sort_keys=True)
        f.write('\n')
    return ref(p)
def canonical(x): return sha(json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode())
def subject(rows):
    rows = sorted([{k: row[k] for k in ('path', 'bytes', 'sha256')} for row in rows], key=lambda row: row['path'])
    assert len(rows) == len({row['path'] for row in rows})
    return {'scope': [row['path'] for row in rows], 'member_count': len(rows), 'members': rows, 'sha256': canonical(rows)}

old = load(R / 'scripts/fixtures/stack_release-v3.0.5.json')
assert ref(R / 'stack_release.json')['sha256'] == '84a0c3747f8915592a2a1628fa8227f6891d8389737fdc0c5a0e8c806d5c3c4f'
handoff = load(W / 'native-transaction-001/HANDOFF.json')
assert handoff['source_checkpoint'] == 'a3f74053b300bdcffd4aba90daaa16e764de5468'
selection = load(W / 'packaging-001/tooling-selection.json')
native = load(R / handoff['source_selection']['path'])
manager = load(W / 'manager-001/BUILD.json')
manager_selection = load(W / 'manager-001/SELECTION.json')
manager_rows = [row for row in manager_selection['source_members'] if row['path'].startswith('specification_methodology/v2/src/stdo_toolchain/')]
assert len(manager_rows) == 13
products = {owner: subject(unit['members']) for owner, unit in selection['owners'].items()}
products['specification_methodology'] = subject(manager_rows + [{**row, 'path': COMMON + row['path']} for row in native['files']])
rows = {row['path']: row for value in products.values() for row in value['members']}
assert len(rows) == 429
committed = {}
for p in (W / 'source-checkpoint-002/PATHS.json', W / 'native-transaction-001/PATHS.json'):
    committed.update({row['path']: row for row in load(p)['files']})
old_rows = {row['path']: row for value in old['products'].values() for row in value['subject']['members']}
old_git = {row['path']: row for row in load(D / 'cohort-binding-004/COMMITTED_SUBJECT_JOIN.json')['files']}
expected = {}
for name, row in rows.items():
    if name in committed:
        known = committed[name]
        assert (known['sha256'], known['bytes']) == (row['sha256'], row['bytes'])
    else:
        assert old_rows[name] == row, name
        known = old_git[name]
    expected[name] = {key: known[key] for key in ('git_mode', 'git_blob')}
raw = subprocess.check_output(['git', '--no-optional-locks', 'ls-tree', '-r', '-z', handoff['source_checkpoint'], '--', *sorted(rows)], cwd=R)
actual = {}
for item in raw.split(b'\0'):
    if item:
        metadata, name = item.split(b'\t', 1)
        mode, kind, oid = metadata.decode().split()
        assert kind == 'blob'
        actual[name.decode()] = {'git_mode': mode, 'git_blob': oid}
assert actual == expected
components = {}
for name, value in old['components'].items():
    owner = value['owner']
    if name == 'representation':
        chosen = products[owner]['members']
    elif name == 'documentation':
        chosen = [row for path, row in rows.items() if path.startswith(COMMON + 'standards/documentation/')]
    elif name == 'proof_reader':
        chosen = [row for path, row in rows.items() if path.startswith(COMMON + 'standards/documentation/proofs/')]
    elif name in ('codex_skills', 'claude_skills'):
        other = 'claude' if name == 'codex_skills' else 'codex'
        chosen = [row for row in products[owner]['members'] if '/build_tenants/' + other + '/' not in row['path']]
    else:
        paths = [path.replace('stdo-v3.0.5/', 'stdo-v' + V + '/').replace('stdo-3.0.5.', 'stdo-' + V + '.') for path in value['subject']['scope']]
        chosen = [rows[path] for path in paths]
    components[name] = subject(chosen)
subjects = save(O / 'SUBJECTS.json', {'kind': 'stdo.rc-cohort-subjects/1', 'source_checkpoint': handoff['source_checkpoint'],
    'native_commit': handoff['native_commit'], 'native_manifest': handoff['native_manifest'], 'products': products, 'components': components,
    'member_count': len(rows), 'git_join': [{'path': name, **actual[name]} for name in sorted(actual)],
    'basis': [ref(W / 'packaging-001/tooling-selection.json'), handoff['source_selection'], ref(W / 'manager-001/SELECTION.json')],
    'limits': 'Exact retained byte inventories joined to current committed Git blob/mode identities. No fresh runtime/support scan or qualification claim.'})

candidate = copy.deepcopy(old)
candidate['profile'] = 'rc-five-product-v1'
candidate['cohort'].update(version=V, cut='v' + V, version_line='3.0.5', status='assembling')
source = load(W / 'source-freeze-rc1.json')
candidate['source'] = {**ref(W / 'source-freeze-rc1.json'), 'source_identity_sha256': source['source_identity_sha256']}
for name, product in candidate['products'].items():
    product.update(version=V, release_ref='refs/tags/' + name + '/v' + V, selector_ref='refs/tags/' + name + '/v3.0.5', subject=products[name], qualification=[])
for name, component in candidate['components'].items():
    component.update(version=V, subject=components[name], evidence={})
for edge in candidate['dependency_edges']:
    edge['provider_subject_sha256'] = products[edge['provider']]['sha256']
candidate['native'] = {'manifest': handoff['native_manifest'], 'source_selection': handoff['source_selection']}
config = load(W / 'packaging-001/native-configuration.json')
candidate['native_preparation'] = {**config['native_preparation'], 'configuration': ref(W / 'packaging-001/native-configuration.json')}
facts = copy.deepcopy(load(W / 'rebind-adapter-001/ACTUAL.json')['manifest']['components']['representation']['facts'])
historical = {}
for key in ('build_run', 'generated_model', 'generation_plan', 'project', 'retained_definition', 'source_manifest'):
    historical[key] = facts.pop(key)
facts['historical_generation'] = {'scope': 'Original authored 3.0.5 generation/provenance; not current RC generation.', **historical}
for key in ('program', 'bindings', 'map', 'preservation', 'source_corpus'):
    path = facts[key]['path'].replace('stdo-v3.0.5/', 'stdo-v' + V + '/')
    facts[key] = rows[path]
facts['source_identity_sha256'] = source['source_identity_sha256']
candidate['components']['representation']['facts'] = facts
candidate['components']['axiom_indexer']['facts'] = {'bindings': facts['bindings'], 'source_corpus': facts['source_corpus'], 'validation_program': facts['program']}
page = 'stdo_representation/build_tenants/a_c/representation/stdo-v' + V + '/explorer.html'
candidate['components']['unified_explorer']['facts'] = {'page': rows[page]}
for host in ('codex', 'claude'):
    candidate['components'][host + '_skills']['facts'] = {'package_manifest': rows['stdo_skills/release/' + V + '/manifest.json']}
candidate['components']['manager']['facts'] = {'source_root': 'specification_methodology/v2/src/stdo_toolchain', 'wheel': manager['wheel'],
    'build_selection': ref(W / 'manager-001/SELECTION.json'), 'portable_setup': ref(W / 'manager-001/BUILD.json'), 'python_distribution_version': '3.0.5rc1'}
candidate['components']['manager']['public_assets'] = [{**manager[key], 'name': Path(manager[key]['path']).name} for key in ('runtime_archive', 'constraints')]
formal = load(T / 'construction-proof-001/CURRENT_FORMAL.json')
runtime = save(O / 'construction-runtime-identity.json', formal['runtime_identity'])
lean = candidate['components']['lean']['facts']
lean.update(bundle=(T / 'construction-proof-001/cold').relative_to(R).as_posix(), bundle_manifest=formal['manifest'],
    bundle_archive=ref(W / 'packaging-001/archives/transport/TRANSPORT.json'), runtime_identity=runtime,
    request=formal['request'], selections=formal['selections'], supplied_views=formal['supplied_views'])
for name, reference in lean['runtime_auxiliary'].items():
    assert formal['runtime_identity']['pins'][name] == reference['sha256']
preimages = load(W / 'PREIMAGES.json')
candidate['publication']['reset'] = ref(W / 'RESET_CONTRACT.json')
expectations = {'refs/heads/main': preimages['head']}
for row in preimages['tag_objects']:
    expectations[row['ref']] = row['object']
    expectations[row['archive_ref']] = None
for product in candidate['products'].values():
    expectations[product['release_ref']] = None
candidate['publication']['expected_remote'] = expectations
url = 'https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology%2Fv' + V + '/'
candidate['publication']['assets'] = sorted([{**value, 'name': Path(value['path']).name, 'url': url + Path(value['path']).name}
    for value in (manager['wheel'], manager['runtime_archive'], manager['constraints'], handoff['native_manifest'])], key=lambda row: row['name'])
candidate['publication']['external_manifest_asset'] = {'name': 'stack-release-v' + V + '.json', 'url': url + 'stack-release-v' + V + '.json'}
candidate['qualification']['evidence'] = {}
candidate_ref = save(O / 'CANDIDATE.json', candidate)
save(O / 'FRONTIER.json', {'status': 'assembling_not_release_ready', 'candidate': candidate_ref, 'subjects': subjects,
    'completed': ['Reviewed source checkpoint and deterministic coordinate rebind', 'Fresh current construction Lean proof and inspection', 'Current source Graphify and Axiom validation/map operations', 'Reviewed native package and exact fresh manager/native installation'],
    'pending': ['Installed fixed interfaces and fresh supported-runtime full proof', 'Independent actual native/browser final record', 'Source-side/installed claim wrappers and final independent cohort review', 'Final carrier and checked atomic16-ref reset publication', 'Fresh public installation/qualification and normal Latest readback'],
    'historical_only': 'Original 3.0.5 LLM/Context trials retain original subjects/limits. No duplicate actor trials or automatic adoption selected.',
    'root_manifest_unchanged_sha256': ref(R / 'stack_release.json')['sha256']})
print(json.dumps({'subjects': subjects, 'candidate': candidate_ref, 'members': len(rows), 'products': {name: value['sha256'] for name, value in products.items()}}, indent=2))
