"""Capture the exact RC2 identity gate; no Product or Git mutation."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import re
import subprocess
import zipfile

BASE = Path(__file__).resolve().parent
WORK = BASE.parent
ROOT = WORK.parents[2]
VERSION = '3.1.0-rc.2'
NATIVE = '21a9d4b93c5adef1e84a369360a99176b98793c5'
SEMANTIC_REPORT = 'e7636ededbad4e5cd1cc48cee0b39e1120518a84cf416a806464648e941a33c6'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()


def read(path):
    return json.loads(path.read_text())


def git(*argv):
    return subprocess.check_output(['git', '-C', str(ROOT), *argv], stderr=subprocess.PIPE)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--carrier', required=True)
    p.add_argument('--plan', type=Path, required=True)
    p.add_argument('--cohort', type=Path, required=True)
    p.add_argument('--packaged-checks', type=Path, required=True)
    p.add_argument('--extra', type=Path, action='append', default=[])
    p.add_argument('--stage', default='identity-01')
    args = p.parse_args()
    stage = BASE / args.stage
    assert not stage.exists(), 'Preserve prior stages.'
    plan = read(args.plan); cohort = read(args.cohort)
    assert cohort['version'] == plan['version'] == VERSION
    assert cohort['source']['carrier'] == args.carrier
    assert cohort['native']['commit'] == NATIVE
    graph = {k: plan[k] for k in ['products', 'refs', 'protected_predecessor_refs']}
    graph_sha = sha(canonical(graph))
    assert graph_sha == cohort['ref_graph_sha256']
    assert len(plan['refs']) == len({x['destination'] for x in plan['refs']}) == 25
    assert len(plan['products']) == len({x['namespace'] for x in plan['products']}) == 6
    assert len(plan['protected_predecessor_refs']) == 12
    assert sha((BASE/'semantic-01/ASSESSMENT.md').read_bytes()) == SEMANTIC_REPORT
    observations = {'kind': 'stdo.rc2.independent-operator-identity-readback/1',
        'performed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'source_carrier': args.carrier, 'native': NATIVE, 'ref_graph_sha256': graph_sha,
        'standing': 'Mechanical readback by the separate Codex assessment operator; not the independent semantic verdict.',
        'committed_evidence': [], 'refs': [], 'products': [], 'qualified_files': [],
        'companion_members': [], 'asset_digests': [], 'assessed_contexts': []}
    remote_raw = git('ls-remote', 'origin')
    remote = {line.split('\t')[1]: line.split('\t')[0] for line in remote_raw.decode().splitlines()}
    for product in plan['products']:
        prefix = r'^refs/tags/' + re.escape(product['namespace']) + r'/v3\.1\.0-rc\.(\d+)$'
        assert not any((m := re.match(prefix, ref)) and int(m[1]) >= 2 for ref in remote)
    for row in plan['refs']:
        assert git('rev-parse', row['source']).decode().strip() == row['object']
        assert git('rev-parse', row['source']+'^{commit}').decode().strip() == row['commit']
        assert remote.get(row['destination'], '') == row['expected_remote']
        tag = row['destination'].startswith('refs/tags/')
        if tag:
            assert git('cat-file', '-t', row['object']).decode().strip() == 'tag'
        observations['refs'].append({**row, 'annotated_tag_verified': tag,
                                     'remote_expected_object_verified': True})
    for ref, oid in plan['protected_predecessor_refs'].items():
        assert remote.get(ref) == oid
    for row in plan['products']:
        assert git('rev-parse', row['commit']+':'+row['root']).decode().strip() == row['subtree_tree']
        observations['products'].append({**row, 'subtree_verified': True})
    for product in cohort['products']:
        definition = product['definition']
        assert definition['commit'] == args.carrier
        data = git('show', args.carrier+':'+definition['path'])
        assert sha(data) == definition['sha256']
        assert json.loads(data)['constitution']['stdo']['basis'] == definition['construction_basis']
    for item in plan['qualified_files']:
        path = Path(item['path'])
        assert sha(path.read_bytes()) == item['sha256']
        observations['qualified_files'].append(item)
    for row in cohort['qualification']['evidence'] + cohort['qualification']['exact_query_assessments']:
        assert row['commit'] == args.carrier
        committed = git('show', args.carrier+':'+row['path'])
        assert sha(committed) == row['sha256']
        assert (ROOT/row['path']).read_bytes() == committed
        observations['committed_evidence'].append({k: row[k] for k in ['commit', 'path', 'sha256']})
    archive = WORK/'assets'/f'stdo-products-v{VERSION}.zip'
    with zipfile.ZipFile(archive) as z:
        inventory = json.loads(z.read('PRODUCTS.json'))
        expected = {'PRODUCTS.json', 'INSTALLATION.md'}
        for name, product in inventory['products'].items():
            declared = next(p for p in cohort['products'] if p['namespace'] == name)['distribution']
            assert all(declared[k] == value for k,value in product.items())
            assert len(product['members']) == product['member_count']
            assert sha(z.read(name+'/'+product['identity_path'])) == product['identity_sha256']
            for row in product['members']:
                member = name+'/'+row['path']; expected.add(member)
                data = z.read(member)
                assert len(data) == row['bytes'] and sha(data) == row['sha256']
                try:
                    source = git('show', args.carrier+':'+member)
                except subprocess.CalledProcessError:
                    source = None
                observations['companion_members'].append({**row, 'product': name,
                    'source_identical': data == source, 'source_sha256': sha(source) if source is not None else None})
        assert len(observations['companion_members']) == 225
        assert set(z.namelist()) == expected
        observations['companion_archive_sha256'] = sha(archive.read_bytes())
        observations['companion_inventory'] = inventory
    for row in cohort['assets']:
        data = (WORK/'assets'/row['name']).read_bytes()
        assert len(data) == row['bytes'] and sha(data) == row['sha256']
        observations['asset_digests'].append(row)
    checks = read(args.packaged_checks)
    allowed_change = {'covered', 'semantic_coverage', 'trial_binding', 'use'}
    for host, details in checks['hosts'].items():
        for row in details.get('contexts', []) + details.get('boundary_controls', []):
            name = row.get('purpose', row.get('case'))
            if not row.get('delivery'):
                assert not row['covered']
                observations['assessed_contexts'].append({'host':host,'name':name,'covered':False,'delivery':None})
                continue
            body = read(Path(row['delivery'])/'CONTEXT.json')['payload']
            frozen_suffix = name+'-delivery' if name in ['python', 'sdlc'] else name+'-boundary'
            frozen = read(WORK/'context/distribution-checks-01'/('codex-'+frozen_suffix)/'CONTEXT.json')['payload']
            different = sorted(k for k in set(body)|set(frozen) if body.get(k)!=frozen.get(k))
            assert set(different) <= allowed_change, (name,different)
            assert body['covered'] is True and row['covered'] is True
            envelope = read(BASE/'semantic-01/assessments'/(name+'.json'))
            assert all(body[k] == envelope[k] for k in ['index_sha256','corpus_sha256','query_sha256'])
            observations['assessed_contexts'].append({'host':host,'name':name,'covered':True,
                'query_sha256':body['query_sha256'],'index_sha256':body['index_sha256'],
                'corpus_sha256':body['corpus_sha256'], 'semantic_payload_fields_unchanged':True,
                'assessment_annotation_changes':different,'selected_rules':len(body['selected'])})
    assert sum(x['covered'] for x in observations['assessed_contexts']) == 12
    stage.mkdir()
    (stage/'REMOTE_BEFORE.txt').write_bytes(remote_raw)
    (stage/'OPERATOR_READBACK.json').write_text(json.dumps(observations,indent=2)+'\n')
    parts = []; manifest = []; seen = set()
    def append(label, path):
        path=path.resolve()
        if path in seen: return
        seen.add(path); data=path.read_bytes()
        manifest.append({'label':label,'path':str(path),'bytes':len(data),'sha256':sha(data)})
        parts.append('\n\n## '+label+'\nSource: '+str(path)+'\nSHA256: '+sha(data)+'\n\n'+data.decode())
    preface = f'''# RC2 final identity / pre-push assessment

You are the independently activated Claude-family assessor, not the Codex Writers or the operator. Judge this exact local post-tag subject: native {NATIVE}, source B {args.carrier}, canonical graph {graph_sha}. Actual publication has NOT happened. Your report may establish bounded prepublication identity/qualification and the applicable reuse of the prior actual assessment; it cannot invent public acquisition, acceptance or adoption. Return findings and evidence gaps, with affected claim only withheld where appropriate.

The prior actual Claude semantic result is fixed and retained. Reuse only its demonstrated unchanged subject, applicability, residuals and exact six query bindings; do not relabel old assessments or conduct another unconditional review. Final source/package checks map its bytes into the release. The changed PC/Skills distribution manifests represent an explicit portable projection, not necessarily byte-equal source manifests. Assess the declared transformations and dependency identities rather than assuming every archive member equals its source path. The three unknown-boundary queries remain refused and uncovered.

The operator readback is mechanical evidence, author records are claims, and prior actual Claude reports are independent evidence with their native limits. Complete deciding RELEASE, EVALUATION and FOUNDATIONS source owners are supplied below. Generic role authority is fixed in the admitted ACTIVATION. Preserved source-first expectations and the already performed semantic report remain explicit. This packet measures UTF-8 bytes only; no enforced clean room, hidden host fit or adequate attention is asserted.

Please assess Product/member/dependency/version identities; native A/source B distinction; assessment-to-packaged-context mapping; current release claims and predecessor conservation applicability; annotated tag objects/peels/exact25-ref graph/remote expectations; guarded atomic publication and RC1 preservation; external cohort self-digest avoidance. Inspect the new release helper and its finite tests proportionately. Distinguish local construction/qualification from required future public checks and human exact-cut acceptance. Any prospective native release-note claim remains conditional on actual publication evidence.

After prose reasoning, provide one JSON fenced object with keys: subject (native_commit, source_carrier, ref_graph_sha256), status (supported/falsified/unknown for bounded prepublication identity), claim_results, semantic_reuse, findings, residuals, unperformed, publication_conditions. Do not authorize publication or manufacture a published status. The Root remains owner of the already-authorized effect and its final result. No tools are available or needed.
'''
    append('Admitted role, exact work scope and closure requirements',WORK/'ACTIVATION.md')
    installed = WORK/'native-store/releases/v3.1.0-rc.2'
    basis = Path('/Users/jim/Library/Application Support/STDO/releases/v3.0.4')
    for owner in ['RELEASE','EVALUATION','FOUNDATIONS']:
        a=basis/'standards'/(owner+'.md'); b=installed/'standards'/(owner+'.md')
        append('Construction-basis complete '+owner+' owner',a)
        if a.read_bytes()!=b.read_bytes():append('Current native complete '+owner+' owner',b)
        else:parts.append('\n\nCurrent native '+str(b)+' is byte-identical to the complete construction-basis owner above; SHA256 '+sha(b.read_bytes())+'.')
    inputs = [
        ('Fixed source-first expectations 1',BASE/'source-first-01/EXPECTATIONS.md'),
        ('Fixed source-first expectations 2',BASE/'source-first-02/EXPECTATIONS.md'),
        ('Prior actual semantic assessment',BASE/'semantic-01/ASSESSMENT.md'),
        ('Actual assessment serialization and provenance',BASE/'semantic-01/SERIALIZATION.json'),
        ('Actual semantic host events and limits',BASE/'semantic-01/HOST_EVENTS.json'),
        ('Source/package semantic unchanged mapping',BASE/'FINAL_PACKAGE_SEMANTIC_READBACK_02.json'),
        ('Independent current identity mechanical readback',stage/'OPERATOR_READBACK.json'),
        ('Final local ref graph',args.plan),('Draft cohort',args.cohort),
        ('Actual extracted-ZIP assessed host checks',args.packaged_checks),
        ('Root prepublication claims',WORK/'PREPUBLICATION.md'),
        ('Claim-level predecessor dispositions proposed by Root',WORK/'PREDECESSOR_DISPOSITIONS.json'),
        ('Native identity',WORK/'NATIVE_BINDING.json'),
        ('Native source delta',WORK/'method/SOURCE_DELTA.json'),
        ('Native release-scoped record',installed/'release/release-note.md'),
        ('Manager finite installed checks',WORK/'manager-checks/RESULT.json'),
        ('Ref-helper real Git fixture results',WORK/'ref-tests-01/RESULT.json'),
        ('Exact ref publication helper',ROOT/f'releases/{VERSION}/tools/ref_transaction.py'),
        ('Ref-helper fixture implementation',ROOT/f'releases/{VERSION}/tools/test_ref_transaction.py'),
        ('Exact cohort construction helper',ROOT/f'releases/{VERSION}/tools/cohort_record.py'),
        ('Release cohort contract inputs',ROOT/f'releases/{VERSION}/COHORT_INPUTS.json'),
        ('Purpose Context Product authority',ROOT/'purpose_context/specification/PRODUCT.md'),
        ('Purpose Context release contract',ROOT/'purpose_context/RELEASE.md'),
        ('Purpose Context portable source relation',WORK/'packaged-products/purpose_context/SOURCE_RELATION.json'),
        ('Skills portable inventory',WORK/'packaged-products/stdo_skills/INVENTORY.json'),
        ('Skills portable dependencies',WORK/'packaged-products/stdo_skills/specification/composition/DEPENDENCIES.json'),
        ('PC and Skills construction return',WORK/'context/RESULT.json'),
        ('PC and Skills final source freeze',WORK/'context/FINAL_FREEZE.json'),
        ('Visual construction return',WORK/'visual/RESULT.json'),
        ('Visual exact predecessor comparison',WORK/'visual/PREDECESSOR_COMPARISON.json'),
        ('Verified asset extraction',WORK/'PRODUCT_EXTRACTION.json')]
    for label,path in inputs:append(label,path)
    for product in cohort['products']:
        append('Product Definition: '+product['namespace'],ROOT/product['definition']['path'])
    for path in args.extra:append('Root supplied final gate evidence: '+path.name,path)
    packet=(preface+''.join(parts)+'\n').encode()
    (stage/'PACKET.md').write_bytes(packet)
    (stage/'INPUT_MANIFEST.json').write_text(json.dumps({'inputs':manifest,'packet_bytes':len(packet),'packet_sha256':sha(packet)},indent=2)+'\n')
    print(json.dumps({'stage':str(stage),'packet_bytes':len(packet),'packet_sha256':sha(packet),'inputs':len(manifest),'source_carrier':args.carrier,'ref_graph_sha256':graph_sha}))


if __name__ == '__main__':
    main()
