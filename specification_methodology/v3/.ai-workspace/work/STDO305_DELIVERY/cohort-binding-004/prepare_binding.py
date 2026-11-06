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
OUT = DELIVERY / 'cohort-binding-004'
C4 = '2ee0147ad06b58dbdf6dad4b874c363a035aab9e'
C3 = 'ec0c09474a1d42084ddd1ba2b97c9479affb0220'
A4 = 'd1f13c53ab733a73993615498f66251041a74073'
TAG = '8eccce113086a15a042580c4c4158eea96ec17e2'
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


_, root_preimage = read(ROOT / 'stack_release.json')
manifest, prior_candidate = read(DELIVERY / 'cohort-binding-003/CANDIDATE.json')
assert git('show', C4 + ':stack_release.json') == (ROOT / 'stack_release.json').read_bytes()
prior, prior_ref = read(DELIVERY / 'cohort-binding-003/SUBJECTS.json',
    'bb8efc45d207232ab6522510cfb5966d025c6372e74556f6b5ae7403bde450bf')
handoff, handoff_ref = read(DELIVERY / 'native-recovery-execution-020/HANDOFF.json',
    '26659c43b6367b15747c51bf21f629ecaac072b01c7e78900a8a338d4904e307')
native, native_ref = read(DELIVERY / 'cohort-recovery-020/NATIVE_INPUT_INVENTORY.json',
    'a99238f4bd8e70fbb9ba187ef040953262dab7ee873d6551c5cd4e370e8499ce')
portable, portable_ref = read(DELIVERY / 'tools-skills/formal-budget-repair-021/PORTABLE.json',
    '2c3749b0babbe50eb1eae6da251493d58ecb9c80afab6e7b3b91238e3cb2aaa2')
staged, staged_ref = read(DELIVERY / 'cohort-recovery-020/PATHS.json',
    'a5ad23ad24f3e31fe7a6ba28b70c2edeb1b7b0b32b59d41f6e9c2f270a2388b4')
formal, formal_ref = read(DELIVERY / 'tools-skills/current-formal-021/CURRENT_FORMAL.json',
    'f338afeec12b7d1c07451cb7927e30f2f384d8a96c3647f4478065daf0cd6a70')
assert handoff['source_checkpoint'] == C4 and handoff['native_commit'] == A4
assert handoff['native_tag_object'] == TAG
assert git('rev-parse', 'HEAD').decode().strip() == C4
assert git('rev-parse', 'refs/tags/specification_methodology/v3.0.5').decode().strip() == TAG
assert git('rev-parse', TAG + '^{}').decode().strip() == A4
assert git('rev-parse', C4 + ':' + PACKAGE).decode().strip() == handoff['source_package_tree']
assert git('rev-parse', A4 + '^{tree}').decode().strip() == handoff['native_root_tree']
assert git('show', '-s', '--format=%P', C4).decode().strip() == C3
assert git('show', '-s', '--format=%P', A4).decode().strip() == '16bc30d215915a4b7b3ed2f13e52e14510ae1c9d'
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
assert len(changed) == 23 and sum(name.startswith(PACKAGE + '/') for name in changed) == 16
selected_rows = {row['path']: row['selected'] for row in staged['members']}
before_git = tree_rows(C3, sorted(current_rows))
after_git = tree_rows(C4, sorted(current_rows))
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
    'source_checkpoint': C4, 'native_commit': A4, 'native_tag_object': TAG,
    'prior_subjects': prior_ref, 'products': products, 'components': components,
    'changed_products': changed_products, 'changed_components': changed_components,
    'delta': [{'before': old_rows[name], 'after': current_rows[name]} for name in changed],
    'basis': {'native_input_inventory': native_ref, 'a_c_portable_inventory': portable_ref,
             'checkpoint_inventory': staged_ref, 'native_handoff': handoff_ref},
    'limits': 'Derived from accepted retained byte inventories and exact selected C3/C4 Git blob/mode joins. No archive, support tree, installed tree or live source content scan was performed by this derivation. Existing required live gate checks remain mandatory.'})
git_ref = write('COMMITTED_SUBJECT_JOIN.json', {'kind': 'stdo.selected-git-object-join/1',
    'observed_ns': NOW, 'source_checkpoint': C4, 'parent': C3,
    'native_commit': A4, 'native_tag_object': TAG, 'member_count': 424,
    'changed_member_count': len(changed), 'unchanged_member_count': 424 - len(changed),
    'files': [{'path': name, **after_git[name]} for name in sorted(after_git)],
    'commands': ['git ls-tree -rz C3 -- <424 explicit member paths>',
                 'git ls-tree -rz C4 -- <same 424 explicit member paths>',
                 'git rev-parse <explicit commit/tree/tag expressions>', 'git show -s --format=%P <C4/A4>'],
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
lean['bundle'] = str((DELIVERY / 'tools-skills/current-formal-021/cold').relative_to(ROOT))
lean['bundle_manifest'] = formal['bundle_manifest']
lean['bundle_archive'] = ref(DELIVERY / 'cohort-recovery-020/archives/current-transport/TRANSPORT.json',
    '442c29433b39c0ec95846305b6de16d4a01286d0c8eb92c9e739b5b85455004c')
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
    'limits': 'These unchanged original records describe their actual source build readback, map write, index validation and bounded semantic assessment. They have no installation field. No A1/A2/A3 runtime observation or verdict is relabelled as A4. Live owner predicates will run within refs(D). Semantic assessment remains the attributed Executive transcription with its targeted scope; it is not a newly signed original report or whole-model semantic qualification.'})
write('NATIVE_BINDING.json', {'kind': 'stdo.cohort-native-binding-succession/1',
    'status': 'actual_local_native_installation_accepted_runtime_pending',
    'current': manifest['native'], 'handoff': handoff_ref, 'source_subjects': subjects_ref,
    'committed_subject_join': git_ref, 'construction_proof': formal_ref,
    'review_custody': ref(OUT / 'original-native-review/CUSTODY.json'),
    'previous': {'native': json.loads((DELIVERY / 'cohort-binding-003/CANDIDATE.json').read_bytes())['native'],
                 'subjects': prior_ref, 'preserved': True},
    'pending': ['fresh local004 support/runtime binding and installed full-model proof',
                'current Context path and both native host sessions',
                'complete installed aggregate and final independent assessment',
                'atomic public transport and fresh public readback']})
write('CONSTRUCTION_PROOF_BINDING.json', {'kind': 'stdo.current-construction-proof-binding/1',
    'status': 'actual_verified_construction_result_and_owner_inspection',
    'result': formal['result'], 'execution': formal['execution'], 'inspection': formal['inspection'],
    'inspection_execution': formal['inspection_execution'], 'current_formal': formal_ref,
    'runtime_identity': runtime_ref, 'bundle_archive': lean['bundle_archive'],
    'native_manifest': handoff['native_manifest'], 'subject_inventory': subjects_ref,
    'limits': 'Actual construction021 result/runtime bound to reviewed payload020 and actual A4. The exact_candidate_lean_result gate still requires the separately successful installed verification; that claim is not completed here. Mathematical 59-member equality preserves bytes, not prior execution verdicts.'})
write('FRONTIER.json', {'kind': 'stdo.complete-cohort-frontier/1', 'observed_ns': NOW,
    'status': 'assembling_not_release_ready', 'candidate': candidate_ref,
    'root_manifest_preimage': root_preimage, 'root_manifest_unchanged': True,
    'completed': ['C4 exact checkpoint', 'A4 native cut and local-only method tag',
                  'fresh exact offline manager and initial172-member native installation',
                  'independent actual A4 native observation',
                  'current construction021 full-model proof and owner inspection',
                  'reviewed source/model/package relations'],
    'pending': ['fresh local004 mapped browser observation', 'fresh local004 runtime/support', 'installed Graphify/Skills/MCP capability wrappers',
                'fresh local004 installed full-model proof and exact transport',
                'one current native-work21 Context path', 'Codex and Claude actual native sessions',
                'final independent complete-subject assessment', 'final candidate D and four peer tags',
                'refs(D), including ready/content predicates', 'atomic six-ref publication',
                'five public assets and anonymous fresh public installation/required fixed capability checks',
                'public installed full-model proof and browser observation', 'public gate and Latest readback'],
    'heavy_slot': 'Tools Writer owns local004 runtime operations after actual mapped browser closure. This preparation performed only retained small metadata and selected Git-object joins.',
    'limits': 'No Git/index/ref, source/native payload, store, public or root manifest effects. Pending fields are explicit and cannot satisfy schema2 readiness.'})
print(json.dumps({'subjects': subjects_ref, 'candidate': candidate_ref,
                  'changed_products': changed_products, 'changed_components': changed_components,
                  'product_sha256': {k: v['sha256'] for k, v in products.items()},
                  'members': len(current_rows), 'changed': len(changed)}, indent=2))
