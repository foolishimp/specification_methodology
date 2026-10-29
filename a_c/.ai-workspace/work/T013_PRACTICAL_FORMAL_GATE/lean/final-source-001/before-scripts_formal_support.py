"""Establish/recheck a selected exact base-proof support manifest.

The manifest is trusted selected tenant HOW, not request/caller evidence. Creating
one explicitly performs fresh kernel replay. Ordinary gates only compare it.
"""
from __future__ import annotations
import argparse,hashlib,json,os,platform,re,subprocess,tempfile,time
from pathlib import Path
import runtime_process
ROOT=Path(__file__).resolve().parents[1]
SUPPORT=ROOT/'profiles/proof-support-v1.json'
CORE=('Model','Closure','Projection','Structure','GateProof','GateRuntime')
SELECTED_PRIOR={
    'manifest':'c2bdfe7ce5bfd0c95ea71316708a93d738e8f8385086195c720e859e14968009',
    'log':'45e3ed7310936c9e3676e76c66fb911a7545c85a019f8e44614c63aa7d4b5a7e',
    'root':'fb9d1e9815990adc213899ab1b51f02ddc4bddd3e0163066ef17123042cc4bf2'}
SCALE_PRIOR_MANIFEST='3ee283ef53a47cd966ad6c47479fe57c2c793003a88590469c2289ea8b2621a2'
SCALE_MODULES=('Structure','GateProof','GateRuntime')
GENERIC_CONTRACTS={'AC.'+n for n in ('checkModel_sound','certificate_exact_reachability','certificate_unique','project_ok_properties','projection_all_residuals_accounted','names_nodup_of_order','array_reconstruct','nodup_of_codes','separated_of_nodup','member_of_block_index','mapped_block_inside','wellFormed_of_range','checked_of_wellFormed')}

def sha(path):
    with Path(path).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()

def canonical(value):return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'))

def tools():
    lock=json.loads((ROOT/'toolchain-lock.json').read_text())
    key=f'{platform.system()}-{platform.machine()}'
    prefix=ROOT/'.toolchain'/lock['lean']['archives'][key]['name'].removesuffix('.tar.zst')
    # No caller-controlled module root, dynamic loader, or Lake override participates
    # in the selected proof basis. The dynamic request directory is added later.
    env={k:v for k,v in os.environ.items() if not (k.startswith(('LEAN','LAKE','DYLD_','LD_','MATHLIB_')) or k in ('PYTHONPATH','PYTHONHOME'))}
    env.update({'PATH':str(prefix/'bin')+os.pathsep+'/usr/bin:/bin:/usr/sbin:/sbin',
                    'MATHLIB_CACHE_DIR':str(ROOT/'.cache/mathlib'),'MATHLIB_NO_CACHE_ON_UPDATE':'1'}
    )
    return prefix,env,lock

def proof_environment(extra=None):
    prefix,env,lock=tools()
    manifest=json.loads((ROOT/'lake-manifest.json').read_text())
    paths=[ROOT/'.lake/build/lib/lean']
    paths.extend(ROOT/'.lake/packages'/entry['name']/'.lake/build/lib/lean' for entry in reversed(manifest['packages']))
    if extra is not None:paths.insert(0,Path(extra).resolve())
    env['LEAN_PATH']=os.pathsep.join(str(p) for p in paths)
    return prefix,env,lock

def audit_contracts(prefix,env):
    with tempfile.TemporaryFile(dir=ROOT/'.cache') as log:
        runtime_process.run([str(prefix/'bin/lean'),'-j','1','-M','4096',str(ROOT/'AC/GateProof.lean')],cwd=ROOT,env=env,stdout=log,check=True,timeout=90)
        log.seek(0);text=log.read().decode()
    print(text,end='',flush=True)
    found={n:set(x.strip() for x in a.split(',') if x.strip()) for n,a in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]",text)}
    found.update({n:set() for n in re.findall(r"'([^']+)' does not depend on any axioms",text)})
    if set(found)!=GENERIC_CONTRACTS or any(a-{'propext','Classical.choice','Quot.sound'} for a in found.values()):
        raise ValueError('fixed generic theorem coverage/axiom audit failed')
    return text

def members():
    prefix,_,_=tools();paths=set()
    for name in CORE:
        paths.add(ROOT/f'AC/{name}.lean')
        for p in (ROOT/'.lake/build/lib/lean/AC').glob(name+'.*'):
            if any(p.name.endswith(s) for s in ('.olean','.olean.private','.olean.server','.ir','.ir.sig')):paths.add(p)
    # Superset of all deciding cached imports: source and loaded object/IR bytes.
    for base in (ROOT/'.lake/packages',prefix/'src/lean',prefix/'lib/lean'):
        for p in base.rglob('*'):
            if p.is_file() and '.git' not in p.parts and any(p.name.endswith(s) for s in ('.lean','.olean','.olean.private','.olean.server','.ir','.ir.sig','.dylib','.so')):
                paths.add(p)
    for n in ('lean','leanchecker','lake'):paths.add(prefix/'bin'/n)
    return {str(p.relative_to(ROOT)):sha(p) for p in sorted(paths)}

def establish(output):
    output=Path(output)
    if output.exists():raise ValueError('support output already exists; explicit new selection required')
    prefix,env,lock=tools();start=time.monotonic()
    runtime_process.run([str(prefix/'bin/lake'),'build','AC.GateRuntime','AC.GateProof'],cwd=ROOT,env=env,stdout=None,check=True,timeout=90)
    prefix,env,lock=proof_environment()
    runtime_process.run([str(prefix/'bin/leanchecker'),'--fresh','AC.GateProof'],cwd=ROOT,env=env,stdout=None,check=True,timeout=300)
    audit=audit_contracts(prefix,env)
    result={'schema':'a_c.lean.proof-support/1','platform':f'{platform.system()}-{platform.machine()}',
            'lean':lock['lean'],'mathlib':lock['mathlib'],'kernel_replay':'leanchecker --fresh AC.GateProof',
            'runtime_boundary':'AC.GateRuntime/Lean.Data.Json serialization is compiled/pinned and output-tested, outside the generic proof replay root',
            'generic_contract_audit':audit,'members':members(),'established_seconds':time.monotonic()-start}
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open('x') as f:f.write(json.dumps(result,sort_keys=True,indent=2)+'\n')
    return result

def extend_selected(output,prior_path,log_path,root_path):
    """Explicit setup-only extension of the independently selected historical base.

    Ordinary requests cannot choose these inputs. Exact historical origin hashes
    are tenant configuration, not values supplied by the evidence producer.
    """
    output=Path(output)
    if output.exists():raise ValueError('support output already exists')
    start=time.monotonic()
    texts={key:Path(path).read_text() for key,path in [('manifest',prior_path),('log',log_path),('root',root_path)]}
    if any(hashlib.sha256(texts[key].encode()).hexdigest()!=value for key,value in SELECTED_PRIOR.items()):
        raise ValueError('prior support origin is not the explicitly selected successful establishment')
    prior=json.loads(texts['manifest'])
    if prior['kernel_replay']!='leanchecker --fresh AC.GateRuntime':raise ValueError('wrong prior replay root')
    current=members()
    changed=sorted(n for n,h in prior['members'].items() if n in current and current[n]!=h)
    removed=sorted(set(prior['members'])-set(current));added=sorted(set(current)-set(prior['members']))
    allowed_changed={'AC/GateRuntime.lean'}|{'.lake/build/lib/lean/AC/GateRuntime'+suffix for suffix in ('.olean','.olean.private','.olean.server','.ir','.ir.sig')}
    if removed or set(changed)-allowed_changed:raise ValueError('prior imported support changed outside selected tenant delta')
    prefix,env,lock=proof_environment()
    allowed_new={str((prefix/'bin/lake').relative_to(ROOT))}
    for module in ('Structure','GateProof'):
        allowed_new.add('AC/'+module+'.lean')
        allowed_new.update('.lake/build/lib/lean/AC/'+module+suffix for suffix in ('.olean','.olean.private','.olean.server','.ir','.ir.sig'))
    if set(added)-allowed_new:raise ValueError('unexpected new external support member')
    expected_imports={'Structure':['AC.Model'],'GateProof':['AC.Projection','AC.Structure'],
                      'GateRuntime':['AC.Projection','AC.Structure','Lean.Data.Json.Basic']}
    for module,expected in expected_imports.items():
        actual=re.findall(r'^public import ([A-Za-z0-9_.]+)$',(ROOT/f'AC/{module}.lean').read_text(),re.M)
        if actual!=expected:raise ValueError('new module imports escape conserved dependency closure: '+module)
    runtime_process.run([str(prefix/'bin/leanchecker'),'AC.Structure','AC.GateProof','AC.GateRuntime'],cwd=ROOT,env=env,stdout=None,check=True,timeout=90)
    # Audit the fixed generic contracts in the selected GateProof source itself.
    audit=audit_contracts(prefix,env)
    after=members()
    if after!=current:raise ValueError('support changed during bounded extension')
    result={'schema':'a_c.lean.proof-support/1','platform':prior['platform'],'lean':lock['lean'],'mathlib':lock['mathlib'],
        'kernel_replay':'leanchecker AC.Structure AC.GateProof AC.GateRuntime against exact prior fresh-checked imports',
        'generic_contract_audit':audit,'members':current,'established_seconds':time.monotonic()-start,
        'runtime_boundary':'Serialization remains a tested source/output bridge; no JSON semantic interpretation theorem.',
        'origin':{'selected_sha256':SELECTED_PRIOR,'retained_text':texts,
                  'prior_fresh_command':prior['kernel_replay'],'prior_success_seconds':prior['established_seconds'],
                  'unchanged_members':len(prior['members'])-len(changed),'changed':changed,'new':added,'removed':removed,
                  'new_direct_imports':expected_imports,'new_external_proof_imports':[]}}
    with output.open('x') as f:f.write(json.dumps(result,sort_keys=True,indent=2)+'\n')
    return result

def _scale_delta(prior,current):
    """Only the selected tenant proof additions may differ from exact T012."""
    allowed={'AC/Structure.lean','AC/GateProof.lean'}
    allowed.update('.lake/build/lib/lean/AC/'+module+suffix
        for module in SCALE_MODULES
        for suffix in ('.olean','.olean.private','.olean.server','.ir','.ir.sig'))
    if set(current)!=set(prior['members']):raise ValueError('scale extension changed the support population')
    changed=sorted(n for n,h in prior['members'].items() if current[n]!=h)
    if set(changed)-allowed:raise ValueError('scale extension changed conserved external/core support')
    return changed

def extend_scale(output,prior_path):
    """Setup-only replay of the T013 tenant delta over the exact checked T012 base.

    This is support establishment, not reuse of a request verdict or generated
    dynamic theorem. Every public request continues to prove and replay its data.
    """
    output=Path(output)
    if output.exists():raise ValueError('support output already exists')
    start=time.monotonic();prior_text=Path(prior_path).read_text()
    if hashlib.sha256(prior_text.encode()).hexdigest()!=SCALE_PRIOR_MANIFEST:
        raise ValueError('scale extension requires the exact established T012 support')
    prior=json.loads(prior_text)
    origin=prior['origin']
    if origin['selected_sha256']!=SELECTED_PRIOR or any(hashlib.sha256(origin['retained_text'][k].encode()).hexdigest()!=h for k,h in SELECTED_PRIOR.items()):
        raise ValueError('T012 historical fresh-proof origin changed')
    expected_imports={'Structure':['AC.Model'],'GateProof':['AC.Projection','AC.Structure'],
                      'GateRuntime':['AC.Projection','AC.Structure','Lean.Data.Json.Basic']}
    for module,expected in expected_imports.items():
        actual=re.findall(r'^public import ([A-Za-z0-9_.]+)$',(ROOT/f'AC/{module}.lean').read_text(),re.M)
        if actual!=expected:raise ValueError('scale extension escapes conserved import closure: '+module)
    prefix,env,lock=proof_environment()
    # Compile only affected tenant roots. Core Model/Closure/Projection and all
    # external source/object bytes must match the historical manifest exactly.
    _scale_delta(prior,members())
    for module in SCALE_MODULES:
        runtime_process.run([str(prefix/'bin/lean'),'-j','1','-M','4096','-R',str(ROOT),
            '-o',str(ROOT/f'.lake/build/lib/lean/AC/{module}.olean'),str(ROOT/f'AC/{module}.lean')],
            cwd=ROOT,env=env,stdout=None,check=True,timeout=90)
    current=members();changed=_scale_delta(prior,current)
    runtime_process.run([str(prefix/'bin/leanchecker'),*[f'AC.{m}' for m in SCALE_MODULES]],
        cwd=ROOT,env=env,stdout=None,check=True,timeout=90)
    audit=audit_contracts(prefix,env)
    if members()!=current:raise ValueError('support changed during scale extension')
    result={'schema':'a_c.lean.proof-support/1','platform':prior['platform'],
        'lean':lock['lean'],'mathlib':lock['mathlib'],
        'kernel_replay':'leanchecker AC.Structure AC.GateProof AC.GateRuntime against exact established T012 imports',
        'generic_contract_audit':audit,'members':current,'established_seconds':time.monotonic()-start,
        'runtime_boundary':prior['runtime_boundary'],'origin':origin,
        'scale_extension':{'selected_manifest_sha256':SCALE_PRIOR_MANIFEST,'retained_manifest':prior_text,
            'changed':changed,'unchanged_members':len(current)-len(changed),
            'direct_imports':expected_imports,'new_external_proof_imports':[],
            'replayed_modules':list(SCALE_MODULES)}}
    with output.open('x') as f:f.write(json.dumps(result,sort_keys=True,indent=2)+'\n')
    return result

def check():
    basis=json.loads(SUPPORT.read_text())
    if basis.get('schema')!='a_c.lean.proof-support/1':raise ValueError('unsupported selected proof support')
    if 'origin' in basis:
        origin=basis['origin']
        if origin['selected_sha256']!=SELECTED_PRIOR or any(hashlib.sha256(origin['retained_text'][k].encode()).hexdigest()!=h for k,h in SELECTED_PRIOR.items()):
            raise ValueError('selected prior support origin changed')
    if 'scale_extension' in basis:
        extension=basis['scale_extension']
        if extension['selected_manifest_sha256']!=SCALE_PRIOR_MANIFEST or hashlib.sha256(extension['retained_manifest'].encode()).hexdigest()!=SCALE_PRIOR_MANIFEST:
            raise ValueError('selected scale support origin changed')
        changed=_scale_delta(json.loads(extension['retained_manifest']),basis['members'])
        if extension['changed']!=changed or extension['replayed_modules']!=list(SCALE_MODULES):
            raise ValueError('scale support delta/replay declaration changed')
    # Newly installed irrelevant modules do not affect the selected import basis;
    # every selected source/object/runtime member must still match exactly.
    for name,digest in basis['members'].items():
        p=ROOT/name
        if not p.is_file():raise FileNotFoundError('selected proof support unavailable: '+name)
        if Path(name).is_absolute() or '..' in Path(name).parts or p.is_symlink() or not p.resolve().is_relative_to(ROOT) or sha(p)!=digest:raise ValueError('selected proof support changed: '+name)
    # A newly added object at an earlier search root could otherwise shadow an
    # unchanged pinned import. Refuse any unselected object/IR in loaded roots.
    _,env,_=proof_environment()
    for directory in env['LEAN_PATH'].split(os.pathsep):
        for p in Path(directory).rglob('*'):
            if p.is_file() and any(p.name.endswith(s) for s in ('.olean','.olean.private','.olean.server','.ir','.ir.sig')):
                relative=str(p.relative_to(ROOT))
                umbrella=relative in {'.lake/build/lib/lean/AC'+suffix for suffix in ('.olean','.olean.private','.olean.server','.ir','.ir.sig')}
                if relative not in basis['members'] and not relative.startswith('.lake/build/lib/lean/AC/') and not umbrella:
                    raise ValueError('unselected import object in search root: '+relative)
                if relative.startswith('.lake/build/lib/lean/AC/') and p.stem.split('.')[0] in CORE and relative not in basis['members']:
                    raise ValueError('unselected deciding AC object: '+relative)
    return {'manifest_sha256':sha(SUPPORT),'members':len(basis['members']),'platform':basis['platform']}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True)
    selection=parser.add_mutually_exclusive_group()
    selection.add_argument('--extend-selected',type=Path);selection.add_argument('--extend-scale',type=Path)
    parser.add_argument('--prior-log',type=Path);parser.add_argument('--prior-root',type=Path);args=parser.parse_args()
    result=extend_scale(args.output,args.extend_scale) if args.extend_scale else extend_selected(args.output,args.extend_selected,args.prior_log,args.prior_root) if args.extend_selected else establish(args.output)
    print(json.dumps({'status':'established','members':len(result['members']),'seconds':result['established_seconds']}))
