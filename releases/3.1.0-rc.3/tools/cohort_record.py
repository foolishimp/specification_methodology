#!/usr/bin/env python3
"""Bind actual six-Product RC3 subjects and evidence without predecessor hash substitution."""
from pathlib import Path
import argparse, hashlib, json, subprocess, zipfile
VERSION='3.1.0-rc.3'
DEFINITIONS={'specification_methodology':'specification_methodology/v3/stdo_3.json','purpose_context':'purpose_context/stdo_purpose_context.json','stdo_skills':'stdo_skills/stdo_skills.json','a_c':'a_c/stdo_a_c.json','stdo_representation':'stdo_representation/stdo_representation.json','axiom_indexer':'axiom_indexer/stdo_default.json'}

def sha(data):return hashlib.sha256(data).hexdigest()
def canonical(value):return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def read(path):return json.loads(path.read_text())

def main():
 p=argparse.ArgumentParser(description=__doc__)
 for name in ['root','work','plan','qualification','out']:p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--carrier',required=True);args=p.parse_args();root=args.root.resolve();w=args.work.resolve()
 if args.out.exists():raise FileExistsError(args.out)
 def git(*argv):return subprocess.check_output(['git','-C',str(root),*argv],text=True).strip()
 def committed(path):
  rel=path.relative_to(root).as_posix();b=subprocess.check_output(['git','-C',str(root),'show',args.carrier+':'+rel]);assert b==path.read_bytes(),rel
  return {'commit':args.carrier,'path':rel,'sha256':sha(b)}
 binding=read(w/'NATIVE_BINDING.json');native=binding['native'];manifest=read(w/f'assets/stdo-v{VERSION}-manifest.json');plan=read(args.plan);selection=read(root/f'releases/{VERSION}/COHORT_INPUTS.json')
 assert manifest['release']['commit']==native['native_commit']
 assert sha((w/f'assets/stdo-v{VERSION}-manifest.json').read_bytes())==binding['manifest_sha256']
 assert plan['version']==selection['version']==VERSION and len(plan['refs'])==25
 with zipfile.ZipFile(w/f'assets/stdo-products-v{VERSION}.zip') as z:
  inventory=json.loads(z.read('PRODUCTS.json'));expected={name+'/'+x['path'] for name,product in inventory['products'].items() for x in product['members']}
  assert set(z.namelist())==expected|{'PRODUCTS.json','INSTALLATION.md'}
  for name,product in inventory['products'].items():
   for row in product['members']:
    b=z.read(name+'/'+row['path']);assert len(b)==row['bytes'] and sha(b)==row['sha256']
 method={'uri':f'stdo://releases/v{VERSION}/','manifest_sha256':binding['manifest_sha256']};assert inventory['native_method']==method
 products=[];bases={}
 for item in plan['products']:
  name=item['namespace'];definition=root/DEFINITIONS[name];basis=read(definition)['constitution']['stdo']['basis'];assert basis['uri']=='stdo://releases/v3.0.4/' and basis['manifest_sha256']=='102817a3f4bea4dca1d6fa0fc634b94404dd2ba82ba6d8c38b273402dda9f95b'
  bases[name]=basis;assert git('rev-parse',item['commit']+':'+item['root'])==item['subtree_tree']
  record={**item,'definition':{**committed(definition),'construction_basis':basis}}
  if name=='specification_methodology':record['distribution']={'asset':f'stdo-v{VERSION}-manifest.json','manifest_sha256':binding['manifest_sha256'],'native_members':native['file_count']}
  else:
   record['distribution']={'asset':f'stdo-products-v{VERSION}.zip','root':name,**inventory['products'][name]}
   identity=root/item['root']/('specification/composition/DEPENDENCIES.json' if name=='stdo_skills' else 'PUBLIC_MANIFEST.json');record['source_public_identity']=committed(identity)
  products.append(record)
 edges=[{'consumer':'purpose_context','provider':'specification_methodology','relation':'Two exact native-source purpose indexes; no implicit method adoption','selected':method},
 {'consumer':'stdo_skills','provider':'specification_methodology','relation':'Exact native workflow host bindings','selected':method},
 {'consumer':'stdo_skills','provider':'purpose_context','relation':'Required single context runtime and catalog','distribution_manifest_sha256':inventory['products']['purpose_context']['identity_sha256']},
 {'consumer':'stdo_skills','provider':'a_c','relation':'Optional visual documentation; not needed for context','distribution_manifest_sha256':inventory['products']['a_c']['identity_sha256']},
 {'consumer':'stdo_representation','provider':'specification_methodology','relation':'Selected exact native sources for bounded visual documentation','selected':method},
 {'consumer':'stdo_representation','provider':'a_c','relation':'Public visual generation/model/carrier/explorer','distribution_manifest_sha256':inventory['products']['a_c']['identity_sha256']},
 {'consumer':'stdo_representation','provider':'axiom_indexer','relation':'Optional mechanical conversion and projection','distribution_manifest_sha256':inventory['products']['axiom_indexer']['identity_sha256']}]
 assets=[]
 for name in selection['assets']:
  if name.startswith('cohort-release-'):continue
  b=(w/'assets'/name).read_bytes();assets.append({'name':name,'bytes':len(b),'sha256':sha(b)})
 q=read(args.qualification);assert q['carrier']==args.carrier and q['native']==native['native_commit'] and q['status']=='qualified-for-declared-prepublication-claims'
 for row in q['qualified_files']:assert sha(Path(row['path']).read_bytes())==row['sha256']
 graph={k:plan[k] for k in ['products','refs','protected_predecessor_refs']}
 value={'kind':'stdo.release-cohort/1','profile':'rc-six-product-v1','version':VERSION,'public_version':'3.1.0','repository':selection['repository'],'native':manifest['release'],'native_manifest_sha256':binding['manifest_sha256'],
 'predecessor':{'version':'3.1.0-rc.2','native_commit':selection['native_predecessor'],'source_carrier':selection['source_predecessor']},
 'source':{'checkpoint':native['source_commit'],'carrier':args.carrier,'native_source_subtree':native['source_path'],'native_source_tree':native['source_tree']},'products':products,'dependency_edges':edges,'constructor_basis':bases,'assets':assets,
 'asset_digest_policy':'This asset is excluded from its own digest inventory; expected assets and public GitHub metadata bind its final bytes.',
 'refs':plan['refs'],'protected_predecessor_refs':plan['protected_predecessor_refs'],'ref_graph_sha256':sha(canonical(graph)),'ref_graph_hash_scope':'Canonical JSON of products, refs and protected_predecessor_refs; external evidence hashes excluded.',
 'qualification':{'prepublication':q,'record_sha256':sha(args.qualification.read_bytes()),'public_verification':'Recorded separately after actual public acquisition and fresh installation; not supplied by this asset.'},
 'publication_contract':{'authority':'Owner approval and RC3 release instruction in source ACTIVATION.md.','atomic_refs':25,'immutable_tags_create_only':True,'mutable_destinations_explicit_leases':True,'github_normal_release':True,'existing_consumers_adopted':False},
 'limits':['Finite declared claims only; no whole-method qualification or arbitrary-query coverage.','Source assessment is cross-family to Codex construction, not independent of earlier Claude-family architectural advice.','Automatic host discovery, wider usefulness, human exact-cut acceptance and consumer adoption remain separate.','Earlier immutable cuts, index assets, models and judgments retain their original subjects.']}
 args.out.write_text(json.dumps(value,indent=2)+'\n');print(json.dumps({'out':str(args.out),'sha256':sha(args.out.read_bytes()),'products':len(products),'companion_members':len(expected),'ref_graph_sha256':value['ref_graph_sha256']}))
if __name__=='__main__':main()
