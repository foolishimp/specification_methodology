#!/usr/bin/env python3
"""One bounded metadata derivation; no installed scans, gate runs or Git writes."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import time

ROOT = Path('/Users/jim/src/apps/specification_methodology')
DELIVERY = ROOT / 'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY'
OUT = DELIVERY / 'cohort-binding-003'
C3 = 'ec0c09474a1d42084ddd1ba2b97c9479affb0220'
C2 = '327bb14af2ee5c1673a5f66bca6a6ec1bfcde402'
A3 = 'ef1af5c6f2aab90c7042266e4d5f6047029c2827'
TAG = 'd40a147f5b2e5f5cd638c71646232e0d4df95249'
PACKAGE = 'specification_methodology/v3/build_tenants/common'
NOW = time.time_ns()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return sha(json.dumps(value, ensure_ascii=False, allow_nan=False,
                          separators=(',', ':'), sort_keys=True).encode())


def ref(path, expected=None):
    path = Path(path)
    raw = path.read_bytes()
    value = {'path': str(path.relative_to(ROOT)), 'bytes': len(raw), 'sha256': sha(raw)}
    if expected:
        assert value['sha256'] == expected, value
    return value


def read(path, expected=None):
    selected = ref(path, expected)
    return json.loads((ROOT / selected['path']).read_bytes()), selected


def write(name, value):
    path = OUT / name
    assert not path.exists(), path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')
    return ref(path)


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, check=True,
                          capture_output=True).stdout


def tree_rows(revision, paths):
    raw = git('ls-tree', '-rz', revision, '--', *paths)
    rows = {}
    for entry in raw.split(b'\0'):
        if not entry:
            continue
        identity, name = entry.split(b'\t', 1)
        mode, kind, blob = identity.decode().split()
        assert kind == 'blob' and mode in ('100644', '100755')
        rows[name.decode()] = {'git_mode': mode, 'git_blob': blob}
    assert set(rows) == set(paths)
    return rows


def subject(rows):
    rows = sorted(rows, key=lambda row: row['path'])
    assert len(rows) == len({row['path'] for row in rows})
    return {'scope': [row['path'] for row in rows], 'member_count': len(rows),
            'members': rows, 'sha256': canonical(rows)}


manifest, root_preimage = read(ROOT / 'stack_release.json')
assert git('show', C3 + ':stack_release.json') == (ROOT / 'stack_release.json').read_bytes()
prior, prior_ref = read(DELIVERY / 'native-recovery-018/SUBJECTS.json',
    '8a897d49184f98f78771a58eae83921c8fe4053dc2a43b06c8ef51155dc1155b')
handoff, handoff_ref = read(DELIVERY / 'native-recovery-execution-019/HANDOFF.json',
    '8fbbefa09eb50d4de5e45a678d5f734acb80c23366913fae4ee924465a678b17')
native, native_ref = read(DELIVERY / 'cohort-recovery-019/NATIVE_INPUT_INVENTORY.json',
    'ce5b5dd36440a3460b54ee05a39600bbf1d76fa43a8c9e41e36c51165f87e9df')
portable, portable_ref = read(DELIVERY / 'tools-skills/a_c-portable-016.json',
    '258d1b662dc67f33312b86342d70a996f12adfe9f46bfc05d862a23ce410daaf')
staged, staged_ref = read(DELIVERY / 'cohort-recovery-019/PATHS.json',
    'bc7845fef173eae52f198a966ac7d9d06641002757b506e320952a84e52a26c8')
formal, formal_ref = read(DELIVERY / 'tools-skills/current-formal-016/CURRENT_FORMAL.json',
    '9c4f8c0071bf055916f753332c6733e50fa473faa60cd2fac8e985c4bd92c104')
assert handoff['source_checkpoint'] == C3 and handoff['native_commit'] == A3
assert handoff['native_tag_object'] == TAG
assert git('rev-parse', 'HEAD').decode().strip() == C3
assert git('rev-parse', 'refs/tags/specification_methodology/v3.0.5').decode().strip() == TAG
assert git('rev-parse', TAG + '^{}').decode().strip() == A3
assert git('rev-parse', C3 + ':' + PACKAGE).decode().strip() == handoff['source_package_tree']
assert git('rev-parse', A3 + '^{tree}').decode().strip() == handoff['native_root_tree']
assert git('show', '-s', '--format=%P', C3).decode().strip() == C2
assert git('show', '-s', '--format=%P', A3).decode().strip() == '16bc30d215915a4b7b3ed2f13e52e14510ae1c9d'
assert all(manifest['products'][name]['subject'] == value for name, value in prior['products'].items())

products = copy.deepcopy(prior['products'])
products['a_c'] = subject([{k: row[k] for k in ('path', 'bytes', 'sha256')} for row in portable['files']])
manager_rows = [row for row in products['specification_methodology']['members']
                if not row['path'].startswith(PACKAGE + '/')]
assert len(manager_rows) == 13
native_rows = [{'path': PACKAGE + '/' + row['path'], 'bytes': row['bytes'], 'sha256': row['sha256']}
               for row in native['files']]
products['specification_methodology'] = subject(manager_rows + native_rows)
assert len(native_rows) == 171 and products['a_c']['scope'] == prior['products']['a_c']['scope']
current_rows = {row['path']: row for item in products.values() for row in item['members']}
old_rows = {row['path']: row for item in prior['products'].values() for row in item['members']}
assert set(current_rows) == set(old_rows) and len(current_rows) == 424
changed = sorted(name for name in current_rows if current_rows[name] != old_rows[name])
assert len(changed) == 18 and sum(name.startswith(PACKAGE + '/') for name in changed) == 14
selected_rows = {row['path']: row['selected'] for row in staged['members']}
before_git = tree_rows(C2, sorted(current_rows))
after_git = tree_rows(C3, sorted(current_rows))
for name in current_rows:
    expected = ({key: selected_rows[name][key] for key in ('git_mode', 'git_blob')}
                if name in changed else before_git[name])
    assert after_git[name] == expected, name
    if name in changed:
        assert all(selected_rows[name][key] == current_rows[name][key] for key in ('bytes', 'sha256'))
for row in native['files']:
    assert after_git[PACKAGE + '/' + row['path']] == {key: row[key] for key in ('git_mode', 'git_blob')}
components = {name: subject([current_rows[row['path']] for row in value['members']])
              for name, value in prior['components'].items()}
changed_products = [name for name in products if products[name] != prior['products'][name]]
changed_components = [name for name in components if components[name] != prior['components'][name]]
subjects_ref = write('SUBJECTS.json', {'kind': 'stdo.cohort-subject-succession/1',
    'status': 'exact_committed_subjects_pending_complete_qualification',
    'source_checkpoint': C3, 'native_commit': A3, 'native_tag_object': TAG,
    'prior_subjects': prior_ref, 'products': products, 'components': components,
    'changed_products': changed_products, 'changed_components': changed_components,
    'delta': [{'before': old_rows[name], 'after': current_rows[name]} for name in changed],
    'basis': {'native_input_inventory': native_ref, 'a_c_portable_inventory': portable_ref,
             'checkpoint_inventory': staged_ref, 'native_handoff': handoff_ref},
    'limits': 'Derived from accepted retained byte inventories and exact selected C2/C3 Git blob/mode joins. No archive, support tree, installed tree or live source content scan was performed by this derivation. Existing required live gate checks remain mandatory.'})
git_ref = write('COMMITTED_SUBJECT_JOIN.json', {'kind': 'stdo.selected-git-object-join/1',
    'observed_ns': NOW, 'source_checkpoint': C3, 'parent': C2,
    'native_commit': A3, 'native_tag_object': TAG, 'member_count': 424,
    'changed_member_count': len(changed), 'unchanged_member_count': 424 - len(changed),
    'files': [{'path': name, **after_git[name]} for name in sorted(after_git)],
    'commands': ['git ls-tree -rz C2 -- <424 explicit member paths>',
                 'git ls-tree -rz C3 -- <same 424 explicit member paths>',
                 'git rev-parse <explicit commit/tree/tag expressions>', 'git show -s --format=%P <C3/A3>'],
    'limits': 'Read-only selected Git metadata, not a new whole-tree byte qualification.'})

runtime_ref = write('construction-runtime-identity.json', formal['runtime_identity'])
manifest['cohort']['status'] = 'assembling'
manifest['native'] = {'manifest': handoff['native_manifest'], 'source_selection': handoff['source_selection']}
for name, value in manifest['products'].items():
    value['subject'] = products[name]
    value['qualification'] = []
for name, value in manifest['components'].items():
    value['subject'] = components[name]
    value['evidence'] = {}
for edge in manifest['dependency_edges']:
    edge['provider_subject_sha256'] = products[edge['provider']]['sha256']
lean = manifest['components']['lean']['facts']
lean['bundle'] = str((DELIVERY / 'tools-skills/current-formal-016/cold').relative_to(ROOT))
lean['bundle_manifest'] = formal['bundle_manifest']
lean['bundle_archive'] = ref(DELIVERY / 'cohort-recovery-019/archives/cold016-transport/TRANSPORT.json',
    'ceffee95e35a737c4bed1fb5b2595f0b089c6571fe6718f0765dd15877e3466a')
lean['runtime_identity'] = runtime_ref
for key in ('request', 'selections', 'supplied_views'):
    if key in formal:
        assert lean[key] == formal[key]
for asset in manifest['publication']['assets']:
    if asset['name'] == 'stdo-v3.0.5-manifest.json':
        asset.update(handoff['native_manifest'])
manifest['qualification']['evidence'] = {}
source_claims = {}
for component, claim in [('representation', 'source_current_model'), ('representation', 'source_current_map'),
                         ('axiom_indexer', 'current_index_validation'), ('representation', 'independent_semantic_review')]:
    record, selected = read(DELIVERY / ('cohort-binding-001/evidence/' + claim + '.json'))
    assert 'installation' not in record
    assert record['source_identity_sha256'] == manifest['source']['source_identity_sha256']
    assert all(products[name]['sha256'] == digest for name, digest in record['subjects'].items())
    if record.get('producer'):
        producer = record['producer']; assert current_rows[producer['path']]['sha256'] == producer['sha256']
    manifest['components'][component]['evidence'][claim] = selected
    source_claims[claim] = selected
candidate_ref = write('CANDIDATE.json', manifest)
write('SOURCE_RELATIONS.json', {'kind': 'stdo.current-source-claim-selection/1',
    'status': 'retained_exact_source_only_evidence_selected_for_later_live_gate',
    'source_identity_sha256': manifest['source']['source_identity_sha256'],
    'subjects': subjects_ref, 'claims': source_claims,
    'producer_and_subject_join': git_ref,
    'limits': 'These unchanged original records describe their actual source build readback, map write, index validation and bounded semantic assessment. They have no installation field. No A1/A2 runtime observation or verdict is relabelled as A3. Live owner predicates will run within refs(D). Semantic assessment remains the attributed Executive transcription with its targeted scope; it is not a newly signed original report or whole-model semantic qualification.'})
write('NATIVE_BINDING.json', {'kind': 'stdo.cohort-native-binding-succession/1',
    'status': 'actual_local_native_installation_accepted_runtime_pending',
    'current': manifest['native'], 'handoff': handoff_ref, 'source_subjects': subjects_ref,
    'committed_subject_join': git_ref, 'construction_proof': formal_ref,
    'review_custody': ref(OUT / 'original-recovery-review/CUSTODY.json'),
    'previous': {'native': json.loads((ROOT / 'stack_release.json').read_bytes())['native'],
                 'subjects': prior_ref, 'preserved': True},
    'pending': ['fresh local003 support/runtime binding and installed full-model proof',
                'current Context path and both native host sessions',
                'complete installed aggregate and final independent assessment',
                'atomic public transport and fresh public readback']})
write('CONSTRUCTION_PROOF_BINDING.json', {'kind': 'stdo.current-construction-proof-binding/1',
    'status': 'actual_verified_construction_result_and_owner_inspection',
    'result': formal['result'], 'execution': formal['execution'], 'inspection': formal['inspection'],
    'inspection_execution': formal['inspection_execution'], 'current_formal': formal_ref,
    'runtime_identity': runtime_ref, 'bundle_archive': lean['bundle_archive'],
    'native_manifest': handoff['native_manifest'], 'subject_inventory': subjects_ref,
    'limits': 'Actual construction016 result/runtime bound to reviewed payload019 and actual A3. The exact_candidate_lean_result gate still requires the separately successful installed verification; that claim is not completed here. Mathematical 59-member equality preserves bytes, not prior execution verdicts.'})
browser = ref(OUT / 'browser/observation-portable.json')
for claim in ('current_3d_2d_layered', 'source_files_navigation'):
    write('claim-preparation/' + claim + '.json', {'kind': 'stdo.cohort-claim-preparation/1',
        'status': 'actual_observation_retained_installation_adapter_binding_pending',
        'claim': claim, 'subjects': {'stdo_representation': products['stdo_representation']['sha256']},
        'source_identity_sha256': manifest['source']['source_identity_sha256'],
        'category': 'browser_observation', 'assessor': '/root/stdo305_integration_review',
        'authors': ['/root/stdo305_representation', '/root/stdo305_tools_skills', '/root/stdo305_release_tools'],
        'result': browser, 'report': ref(OUT / 'original-recovery-review/BROWSER_REVIEW.json'),
        'original_custody': ref(OUT / 'original-recovery-review/CUSTODY.json'),
        'native_handoff': handoff_ref, 'installation': None,
        'limits': 'Fresh actual local003 offline browser observation accepted by Root. Only screenshot/driver references relocated; original bytes and actual page paths retained. Gate-consumable wrapper awaits the actual completed runtime installation binding. No repeated browser observation is selected.'})
write('FRONTIER.json', {'kind': 'stdo.complete-cohort-frontier/1', 'observed_ns': NOW,
    'status': 'assembling_not_release_ready', 'candidate': candidate_ref,
    'root_manifest_preimage': root_preimage, 'root_manifest_unchanged': True,
    'completed': ['C3 exact checkpoint', 'A3 native cut and local-only method tag',
                  'fresh exact offline manager and initial172-member native installation',
                  'independent actual A3 native/browser observation',
                  'current construction016 full-model proof and owner inspection',
                  'reviewed source/model/package relations'],
    'pending': ['fresh local003 runtime/support', 'installed Graphify/Skills/MCP capability wrappers',
                'fresh local003 installed full-model proof and exact transport',
                'one current native-work21 Context path', 'Codex and Claude actual native sessions',
                'final independent complete-subject assessment', 'final candidate D and four peer tags',
                'refs(D), including ready/content predicates', 'atomic six-ref publication',
                'five public assets and anonymous fresh public installation/required fixed capability checks',
                'public installed full-model proof and browser observation', 'public gate and Latest readback'],
    'heavy_slot': 'Tools Writer owns local003 support/proof operations. This preparation performed only retained small metadata and selected Git-object joins.',
    'limits': 'No Git/index/ref, source/native payload, store, public or root manifest effects. Pending fields are explicit and cannot satisfy schema2 readiness.'})
print(json.dumps({'subjects': subjects_ref, 'candidate': candidate_ref,
                  'changed_products': changed_products, 'changed_components': changed_components,
                  'product_sha256': {k: v['sha256'] for k, v in products.items()},
                  'members': len(current_rows), 'changed': len(changed)}, indent=2))
