#!/usr/bin/env python3
"""Bind the actual RC2 source, native cut, companion members and annotated refs."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile

VERSION = '3.1.0-rc.3'
DEFINITIONS = {
 'specification_methodology':'specification_methodology/v3/stdo_3.json',
 'purpose_context':'purpose_context/stdo_purpose_context.json',
 'stdo_skills':'stdo_skills/stdo_skills.json',
 'a_c':'a_c/stdo_a_c.json',
 'stdo_representation':'stdo_representation/stdo_representation.json',
 'axiom_indexer':'axiom_indexer/stdo_default.json',
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['root','work','plan','out']:
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--carrier',required=True)
    p.add_argument('--identity-assessment',type=Path)
    p.add_argument('--identity-execution',type=Path)
    args=p.parse_args();root=args.root.resolve();work=args.work.resolve()
    if args.out.exists(): raise FileExistsError(args.out)
    def read(path): return json.loads(path.read_text())
    def git(*argv): return subprocess.check_output(['git','-C',str(root),*argv],text=True).strip()
    def committed(path):
        relative=path.relative_to(root).as_posix()
        raw=subprocess.check_output(['git','-C',str(root),'show',args.carrier+':'+relative])
        if raw!=path.read_bytes(): raise ValueError('Working/committed evidence differs: '+relative)
        return {'commit':args.carrier,'path':relative,'sha256':sha(raw)}
    selection=read(root/f'releases/{VERSION}/COHORT_INPUTS.json')
    binding=read(work/'NATIVE_BINDING.json');native=binding['native'];plan=read(args.plan)
    manifest=read(work/f'assets/stdo-v{VERSION}-manifest.json')
    if manifest['release']['commit']!=native['native_commit']: raise ValueError('Native subject differs')
    if sha((work/f'assets/stdo-v{VERSION}-manifest.json').read_bytes())!=binding['manifest_sha256']:
        raise ValueError('Native manifest changed')
    if selection['version']!=VERSION or plan['version']!=VERSION: raise ValueError('Wrong version')
    archive=work/f'assets/stdo-products-v{VERSION}.zip'
    extraction=read(work/'PRODUCT_EXTRACTION.json')
    if sha(archive.read_bytes())!=extraction['archive_sha256']: raise ValueError('Changed archive')
    with zipfile.ZipFile(archive) as z:
        inventory=json.loads(z.read('PRODUCTS.json'))
        expected={f'{name}/{row["path"]}' for name,product in inventory['products'].items() for row in product['members']}
        if set(z.namelist())!=expected|{'PRODUCTS.json','INSTALLATION.md'}: raise ValueError('Archive population differs')
        for name,product in inventory['products'].items():
            for row in product['members']:
                data=z.read(name+'/'+row['path'])
                if len(data)!=row['bytes'] or sha(data)!=row['sha256']:raise ValueError('Archive member differs')
    if inventory['native_method']!={'uri':f'stdo://releases/v{VERSION}/','manifest_sha256':binding['manifest_sha256']}:
        raise ValueError('Companion native dependency differs')
    products=[]
    for item in plan['products']:
        definition=root/DEFINITIONS[item['namespace']]
        record={**item,'definition':committed(definition)}
        basis=read(definition)['constitution']['stdo']['basis']
        if basis['manifest_sha256']!='102817a3f4bea4dca1d6fa0fc634b94404dd2ba82ba6d8c38b273402dda9f95b':
            raise ValueError('Construction basis differs')
        record['definition']['construction_basis']=basis
        if git('rev-parse',item['commit']+':'+item['root'])!=item['subtree_tree']:raise ValueError('Product tree differs')
        if item['namespace']=='specification_methodology':
            record['distribution']={'asset':f'stdo-v{VERSION}-manifest.json','manifest_sha256':binding['manifest_sha256'],'native_members':native['file_count']}
        else:
            record['distribution']={'asset':archive.name,'root':item['namespace'],**inventory['products'][item['namespace']]}
            record['source_public_identity']=committed(root/item['root']/('specification/composition/DEPENDENCIES.json' if item['namespace']=='stdo_skills' else 'PUBLIC_MANIFEST.json'))
        products.append(record)
    old=read(root/'.ai-workspace/work/STDO_3_1_RELEASE_2026-11-15/COHORT_DRAFT.json')
    replacements={
      '3.1.0-rc.2':VERSION,
      'ddbd3910981a63f41c17879551f93ef58f369848bae81cc9726d77df55dc7faa':binding['manifest_sha256'],
      'c1e0faaa8437c169031a476343c764614135cd93':native['native_commit'],
      'fca8d5e97cf2e945196aecdc33908bb190efdca5':native['tag_object'],
      'c93e1a34fc59b7bc8cc385d3caece3b224616670ef627371f60171b9fdf0a537':inventory['products']['purpose_context']['identity_sha256'],
      '396ffa87ca05f6a621e0b0e556d641284e88fe9488b5c5b5b15038a790d810e7':sha((root/'purpose_context/PUBLIC_MANIFEST.json').read_bytes()),
      '40b6e19214f40ba10ed38d90b11f98f0e62ecad6ef2e9b2ccf758ed9607f74af':inventory['products']['a_c']['identity_sha256'],
      '9d9bbe03ebd31ea7d114ef4c56dd1929e9107cd12ceb12dd4ecaa4fbc9f5dbed':inventory['products']['axiom_indexer']['identity_sha256'],
    }
    edges=json.dumps(old['dependency_edges'])
    for before,after in replacements.items():edges=edges.replace(before,after)
    evidence_paths=['ACTIVATION.md','PREPUBLICATION.md','PREDECESSOR_DISPOSITIONS.json','NATIVE_BINDING.json',
      'method/SOURCE_DELTA.json','method/GUIDE_FINDINGS.json','context/RESULT.json','context/FINAL_FREEZE.json',
      'visual/RESULT.json','visual/PREDECESSOR_COMPARISON.json','manager-checks/RESULT.json','ref-tests-01/RESULT.json',
      'assessment/SOURCE_FIRST.json','assessment/semantic-01/ASSESSMENT.md','assessment/semantic-01/VERDICT.json']
    evidence=[committed(work/name) for name in evidence_paths]
    assessments=[]
    for path in sorted((work/'assessment/semantic-01/assessments').glob('*.json')):
        envelope=read(path)
        if envelope['status']!='supported':raise ValueError('Unexpected supported-envelope directory status')
        assessments.append({'name':path.stem,**committed(path),'assessment':envelope})
    assets=[]
    for name in selection['assets']:
        if name.startswith('cohort-release-'):continue
        path=work/'assets'/name
        assets.append({'name':name,'bytes':path.stat().st_size,'sha256':sha(path.read_bytes())})
    graph={k:plan[k] for k in ['products','refs','protected_predecessor_refs']}
    qualification={'declared_prepublication_claims':'Supported within the attached exact-subject assessment and retained limits.',
      'evidence':evidence,'exact_query_assessments':assessments,
      'post_tag_review':'pending; this draft is not the final publishable cohort',
      'public_verification':'Separate postpublication acquisition/install result; unperformed until actually observed.'}
    if args.identity_assessment:
        if not args.identity_execution:raise ValueError('Actual identity execution required')
        report=args.identity_assessment.read_bytes(); execution=read(args.identity_execution)
        if execution['invocation']['exit_code']!=0 or execution['result']['subtype']!='success':
            raise ValueError('Identity assessment did not complete successfully')
        qualification['post_tag_review']={'report':report.decode(),'sha256':sha(report),
          'standing':'Read the actual independent conclusions and residuals below; publication is still unperformed.',
          'execution':{'model':execution['init'].get('model'),'session_id':execution['init'].get('session_id'),
                       'result_subtype':execution['result']['subtype'],'exit_code':execution['invocation']['exit_code'],
                       'observed_tool_uses':len(execution['observed_tool_uses']),
                       'raw_stdout_sha256':execution['invocation']['stdout_sha256']}}
    value={'kind':'stdo.release-cohort/1','profile':'rc-six-product-v1','version':VERSION,'public_version':'3.1.0',
      'repository':selection['repository'],'native':manifest['release'],
      'native_manifest_sha256':binding['manifest_sha256'],
      'predecessor':{'version':'3.1.0-rc.2','native_commit':selection['native_predecessor'],'source_carrier':selection['source_predecessor']},
      'source':{'checkpoint':native['source_commit'],'carrier':args.carrier,'native_source_subtree':native['source_path'],'native_source_tree':native['source_tree']},
      'products':products,'assets':assets,
      'asset_digest_policy':'This asset is excluded from its own hash inventory; final expected-assets and GitHub advertised digest bind it.',
      'refs':plan['refs'],'protected_predecessor_refs':plan['protected_predecessor_refs'],
      'ref_graph_sha256':sha(canonical(graph)),'ref_graph_hash_scope':'Canonical JSON of products, refs and protected_predecessor_refs; excludes external qualification-file references.',
      'qualification':qualification,
      'publication_contract':{'authority':'Owner instruction to fix issues and cut RC2; ACTIVATION and RELEASE in source carrier.',
        'atomic_refs':25,'immutable_tags_create_only':True,'mutable_destinations_explicit_leases':True,'github_normal_release':True,'existing_consumers_adopted':False},
      'dependency_edges':json.loads(edges),'constructor_basis':old['constructor_basis'],
      'inactive_historical_dependency':old['inactive_historical_dependency']}
    args.out.write_text(json.dumps(value,indent=2)+'\n')
    print(json.dumps({'out':str(args.out),'sha256':sha(args.out.read_bytes()),'products':len(products),'companion_members':len(expected),'ref_graph_sha256':value['ref_graph_sha256']}))


if __name__=='__main__':
    main()
