"""Prospective exact RC reset operations; this script performs no Git/network effects."""
from pathlib import Path
import hashlib
import json

R = Path('/Users/jim/src/apps/specification_methodology')
Q = R / 'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET'
W = Q / 'release-tools'
O = W / 'cohort-001/publication'
PY = '/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/bin/python3.13'
GIT = ['git', '-c', 'gc.auto=0', '-c', 'maintenance.auto=false']


def read(p):
    return json.loads(p.read_bytes())


def ref(p):
    raw = p.read_bytes()
    return {'path': p.relative_to(R).as_posix(), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def save(name, value):
    p = O / name
    assert not p.exists(), p
    p.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n')
    return ref(p)


def main():
    assert not O.exists()
    O.mkdir()
    candidate = read(W / 'cohort-001/CANDIDATE.json')
    h = read(W / 'native-transaction-001/HANDOFF.json')
    pre = read(W / 'PREIMAGES.json')
    old = read(R / pre['release']['path'])
    remote = dict(line.split('\t')[::-1] for line in (R / pre['remote']['path']).read_text().splitlines())
    products = candidate['products']
    assert all(not any(k.startswith('refs/tags/' + p + '/v3.0.5-rc.') for k in remote) for p in products)
    version_lines = {p: [] for p in sorted(products)}
    version_binding = save('VERSION_LINES.json', {
        'kind': 'stdo.rc-version-line-preimage/1', 'source': pre['remote'],
        'expected_version_lines': version_lines,
        'limitation': 'This is the retained initial preimage. The actual refs gate must reobserve the exact complete remote set immediately before the atomic transaction.',
    })
    annotations = {}
    selectors = {}
    for name, product in sorted(products.items()):
        target = h['native_commit'] if name == 'specification_methodology' else 'FINAL_CARRIER_COMMIT'
        lines = [f'{name} v3.0.5-rc.1', f'STDO-Product: {name}', 'STDO-Version: 3.0.5-rc.1',
                 'STDO-Version-Line: 3.0.5', 'STDO-Source-Identity: ' + candidate['source']['source_identity_sha256'],
                 'STDO-Product-Subject: ' + product['subject']['sha256'], 'STDO-Native-Commit: ' + h['native_commit']]
        if name != 'specification_methodology':
            annotations[name] = {'ref': product['release_ref'], 'target': target, 'annotation_lines': lines}
        selectors[name] = {'ref': product['selector_ref'], 'target': target,
                           'expected_old_object': candidate['publication']['expected_remote'][product['selector_ref']],
                           'annotation_lines': [f'{name} v3.0.5', 'Moving version-line selector for the immutable v3.0.5-rc.1 cut.', *lines[1:]]}
    new_tag = 'specification_methodology/v3.0.5-rc.1'
    old_archive = next(x['archive_ref'].removeprefix('refs/tags/') for x in pre['tag_objects'] if x['ref'] == 'refs/tags/specification_methodology/v3.0.5')
    archive_patch = save('archive-previous-release.json', {
        'tag_name': old_archive, 'name': 'STDO 3.0.5 — superseded stable candidate (archived)',
        'body': 'Superseded by the owner-authorized unadopted-line reset. Use the normal STDO 3.0.5 release at the immutable `specification_methodology/v3.0.5-rc.1` tag. This historical release preserves its original five asset identities and original native tag object under the archive ref. Old v3.0.5 URI continuity is not promised.\n\n---\n\n' + (old.get('body') or ''),
        'draft': False, 'prerelease': False, 'make_latest': 'false',
    })
    latest = save('make-latest.json', {'make_latest': 'true'})
    assets = candidate['publication']['assets']
    external = O / 'assets/stack-release-v3.0.5-rc.1.json'
    gate = [PY, '-B', str(R / 'scripts/check_stack_release.py')]
    commands = [
        {'id': 'checkpoint', 'argv': [*GIT, 'commit', '-m', 'Release STDO 3.0.5 RC1 cohort and reset unadopted selectors'],
         'precondition': 'Exact final accepted B/evidence/path/index and HEAD a3f74053b300bdcffd4aba90daaa16e764de5468. One final carrier commit; no source or native changes.'},
        {'id': 'annotated-tag-objects', 'argv': [*GIT, 'mktag'],
         'stdin': 'Exact object/type/tag/tagger headers and the per-Product cut/selector annotation below, binding actual D or native64cf9cc8. Existing native RC tag0c0ee702 remains unchanged.'},
        {'id': 'local-atomic-reset-refs', 'argv': [*GIT, 'update-ref', '--stdin'],
         'stdin': 'start\ncreate each of four absent peer RC refs with its actual tag object\ncreate each of five absent archive refs with its exact former tag object\nupdate each of five selectors with new actual annotated object and exact former object precondition\nprepare\ncommit\n',
         'precondition': 'Actual complete remote/main/old selectors/absent RC+archive preimages match; no other ref is selected.'},
        {'id': 'refs', 'argv': [*gate, '--phase', 'refs', '--revision', 'FINAL_CARRIER_COMMIT'],
         'coverage': 'ready/content predicates executed within refs(D)'},
        {'id': 'atomic-push', 'argv_source': 'Use only the successful refs(D) emitted push_argv, qualified_push_sha256 and exact 16-ref vector: main, five RC cuts, five leased selectors and five create-only archives. No sequential or unguarded-force fallback.',
         'environment': {'GIT_CONFIG_COUNT': '2', 'GIT_CONFIG_KEY_0': 'gc.auto', 'GIT_CONFIG_VALUE_0': '0', 'GIT_CONFIG_KEY_1': 'maintenance.auto', 'GIT_CONFIG_VALUE_1': 'false'}},
        {'id': 'published', 'argv': [*gate, '--phase', 'published', '--revision', 'FINAL_CARRIER_COMMIT']},
        {'id': 'archive-previous-release', 'argv': ['gh', 'api', '--method', 'PATCH', 'repos/foolishimp/specification_methodology/releases/437012396', '--input', str(R / archive_patch['path'])],
         'precondition': 'Exact existing release437012396 and all five asset IDs/digests/sizes match retained preimage; archive ref now publicly names the exact original annotated tag. Preserve assets, release ID and original body in custody. Read back the same five identities after metadata-only patch.'},
        {'id': 'new-release-absence', 'argv': ['gh', 'api', 'repos/foolishimp/specification_methodology/releases/tags/specification_methodology%2Fv3.0.5-rc.1'], 'expected_http_status': 404},
        {'id': 'release-create', 'argv': ['gh', 'release', 'create', new_tag, *[str(R / a['path']) for a in assets], str(external), '--repo', 'foolishimp/specification_methodology', '--verify-tag', '--title', 'STDO 3.0.5', '--notes-file', str(O / 'RELEASE_NOTES.md'), '--latest=false'],
         'preconditions': ['All selected current local claims and independent review accepted.', 'External B asset is exact git show D:stack_release.json; its digest is outside B.', 'Normal release: draft=false, prerelease=false; exactly five selected assets; Latest remains deferred to actual public qualification.']},
        {'id': 'public-gate', 'argv': [*gate, '--phase', 'public', '--revision', 'FINAL_CARRIER_COMMIT', '--public-receipt', str((Q / 'public-qualification-001/PUBLIC_READBACK.json').relative_to(R)), '--public-receipt-sha256', 'ACTUAL_PUBLIC_RECEIPT_SHA256']},
        {'id': 'latest-after-public-pass', 'argv': ['gh', 'api', '--method', 'PATCH', 'repos/foolishimp/specification_methodology/releases/ACTUAL_NEW_RELEASE_ID', '--input', str(R / latest['path'])],
         'precondition': 'Exact public gate passed; same new fixedRC release ID/tag/five assets and normal flags reobserved; then anonymous Latest endpoint must return that same ID and five identities.'},
    ]
    value = {
        'kind': 'stdo.rc-reset-publication-operation-templates/1', 'status': 'prepared_unexecuted',
        'candidate': ref(W / 'cohort-001/CANDIDATE.json'), 'native_handoff': ref(W / 'native-transaction-001/HANDOFF.json'),
        'reset_contract': candidate['publication']['reset'], 'version_line_binding': version_binding,
        'expected_version_lines': version_lines,
        'expected_remote': candidate['publication']['expected_remote'],
        'preserved_immutable_refs': candidate['publication']['preserved_immutable_refs'],
        'selected_ref_count': 16, 'cut_annotations': annotations, 'selector_annotations': selectors,
        'archive_refs': {x['archive_ref']: x['object'] for x in pre['tag_objects']},
        'assets': assets, 'external_manifest_asset': candidate['publication']['external_manifest_asset'],
        'commands': commands,
        'phase_consolidation': {'wording': 'ready/content predicates executed within refs(D)',
                               'basis': 'Existing schema2 dispatch executes content before refs. The prior Executive-authorized operator consolidation is continued explicitly; no ready-only predicate or separate successful invocation is claimed.',
                               'limits': 'Mutable installation/currentness checks are unchanged. Published and public phases remain separate. Drift or a failed/uncertain effect stops the sequence.'},
        'public_installation': {'workspace': '/Users/jim/.local/share/stdo-qualification/v3.0.5-rc.1/public-001',
                                'handoff': str((Q / 'public-qualification-001/HANDOFF.json').relative_to(R)),
                                'transport': 'Anonymous TLS-verified acquisition using the exact fixed RC tag API, exact five names/digests/sizes and normal flags before executing the downloaded manager recipe.',
                                'native_manifest_sha256': h['native_manifest']['sha256'],
                                'method': 'Fresh manager/native/source installation; fixed interfaces, Graphify, full proof, owner inspection, documentation checks and independent browser. No new model-agent or Context sessions.',
                                'cache': 'Only the explicitly selected, independently cloned third-party toolchain/packages/Mathlib cache may be acquired from retained bytes. Fresh support/origin/proof and runtime identities are mandatory; no verdict, own build, profile or venv transfer.'},
        'remaining_actual_bindings': ['Final complete accepted B and carrier D', 'Actual local installed runtime/proof and complete qualification aggregate', 'New GH release ID and anonymous acquisitions', 'Fresh public installation/runtime/proof/aggregate and public gate', 'Actual same-ID Latest readback'],
    }
    result = save('OPERATION_TEMPLATES.json', value)
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
