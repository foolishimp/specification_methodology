#!/usr/bin/env python3
"""Exact-subject reusable formal gate. Result labels are evidence, never authority."""
from __future__ import annotations
import sys

# The CLI selects CPython's isolated, no-site startup before importing deciding
# helpers. Python initialization before this re-exec remains a trusted-host
# boundary; supervisors should invoke the selected interpreter with -I -S -B.
if __name__ == '__main__' and not (sys.flags.isolated and sys.flags.no_site):
    import os
    os.execv(sys.executable, [sys.executable, '-I', '-S', '-B', __file__, *sys.argv[1:]])

import argparse,copy,hashlib,json,os,re,subprocess,time,resource,types
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SCRIPT_FILES=frozenset(name+'.py' for name in (
    'bootstrap','check','check_gate','formal_gate','formal_support','gate_codegen',
    'generate_fixture','generation_profile','import_fixture','runtime_process'))
RESULT_LIMITS=[
    'Finite declared structural model/closure/projection only; no semantic acceptance.',
    'Whole-model-source-correspondence covers only supplied or carrier-recovered model JSON; original prose/corpus-to-model F_P fidelity remains opaque and unproved.',
    'Python profile/parser/generator and runtime serialization remain tested trusted bridges.',
    'Python API imports and interpreter initialization remain trusted-host responsibilities; the CLI isolates helper loading after startup.',
    'Context binding is metadata; consumer must check actual delivered bytes.',
    'Crossing relations are checked source-derived metadata, not a Lean theorem.']

class ScriptNamespaceError(ValueError):
    pass

def _script_namespace():
    """Reject importable alternatives before loading any deciding helper."""
    entries={p.name:p for p in (ROOT/'scripts').iterdir()}
    if set(entries)-{'__pycache__'} != SCRIPT_FILES:
        raise ScriptNamespaceError('Selected scripts namespace differs from the exact flat source population')
    for name,p in entries.items():
        if p.is_symlink():raise ScriptNamespaceError('Selected scripts namespace contains a symlink: '+name)
        if name=='__pycache__':
            if not p.is_dir() or any(c.is_symlink() or not c.is_file() or c.suffix!='.pyc' for c in p.iterdir()):
                raise ScriptNamespaceError('Selected scripts bytecode cache is not inert regular .pyc files')
        elif not p.is_file():raise ScriptNamespaceError('Selected helper is not a regular source file: '+name)

_CLI_HELPER_SOURCES={}
def _load_cli_helpers():
    # Dependency order closes all sibling imports, including the importer's
    # deferred generation-profile import. Compile exact source bytes rather than
    # SourceFileLoader, which may consume a cached .pyc instead of the pinned .py.
    for name in ('generation_profile','import_fixture','runtime_process',
                 'formal_support','generate_fixture','check','gate_codegen'):
        path=ROOT/'scripts'/(name+'.py');raw=path.read_bytes()
        module=types.ModuleType(name);module.__file__=str(path);module.__package__=''
        sys.modules[name]=module
        exec(compile(raw,str(path),'exec',dont_inherit=True),module.__dict__)
        _CLI_HELPER_SOURCES[str(path.relative_to(ROOT))]=hashlib.sha256(raw).hexdigest()

try:
    _script_namespace()
    if __name__=='__main__':_load_cli_helpers()
except (OSError,ScriptNamespaceError) as exc:
    if __name__!='__main__':raise
    status='refused' if isinstance(exc,ScriptNamespaceError) else 'incomplete'
    print(json.dumps({'schema':'a_c.formal-gate.result/1','status':status,
                     'reason':str(exc),'checked_claims':[],'limits':RESULT_LIMITS},sort_keys=True))
    sys.exit(2 if status=='refused' else 4)

# API users own their host module namespace. The public CLI populated these
# aliases above from the exact selected files under isolated interpreter search.
import import_fixture as bridge
from generation_profile import ProfileError,validate_generation_profile
import formal_support as support
import runtime_process
from gate_codegen import (data_source,name_source,name_contract_names,identities_source,
                          bounds_source,model_proof,identity_contract_names,views_source,RUNNER)
from check import record_output,reference_output

EXIT={'verified':0,'refused':2,'unsupported':3,'incomplete':4}
DEFAULT_LIMITS={'timeout_seconds':90,'memory_mb':4096,'max_input_bytes':32*1024*1024,'max_selections':64}
AXIOMS={'propext','Classical.choice','Quot.sound'}
class GateError(Exception):
    def __init__(self,status,reason):super().__init__(reason);self.status=status;self.reason=reason

def fail(status,reason):raise GateError(status,reason)
def digest(value):return bridge.digest(value)
def read_json_bytes(raw):
    try:
        value=json.loads(raw.decode('utf-8'),object_pairs_hook=bridge._pairs);bridge._grammar(value);return value
    except (ValueError,UnicodeError,RecursionError) as e:fail('refused','Malformed JSON: '+str(e))
def read_evidence_json(path):
    # Timing observations are ordinary finite JSON numbers. They are not part
    # of the integer-only subject grammar imported into Lean.
    def invalid_constant(value):raise ValueError('nonfinite evidence number: '+value)
    return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=bridge._pairs,parse_constant=invalid_constant)
def write_json(path,value):
    with Path(path).open('x',encoding='utf-8') as f:f.write(json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2)+'\n')

def runtime_identity():
    _script_namespace()
    paths={ROOT/'toolchain-lock.json',ROOT/'lake-manifest.json',ROOT/'lakefile.toml',ROOT/'lean-toolchain'}
    paths.update((ROOT/'scripts').glob('*.py'));paths.update((ROOT/'profiles').glob('*.json'))
    paths.update(ROOT/f'AC/{name}.lean' for name in support.CORE)
    pins={str(p.relative_to(ROOT)):support.sha(p) for p in sorted(paths)}
    if any(pins.get(path)!=h for path,h in _CLI_HELPER_SOURCES.items()):
        raise ScriptNamespaceError('Selected helper source changed after exact-file loading')
    return {'sha256':digest(pins),'pins':pins}

def validate_request(request):
    if type(request) is not dict or set(request)!={'schema','input','selections','supplied_views','context_binding'}:fail('refused','Malformed gate request fields')
    if request['schema']!='a_c.formal-gate.request/1':fail('unsupported','Unsupported gate request schema')
    inp=request['input']
    if type(inp) is not dict or set(inp)!={'format','path','raw_sha256'}:fail('refused','Malformed input binding')
    if inp['format'] not in ('model','carrier'):fail('unsupported','Unsupported input format')
    for entry in (inp,request['supplied_views']):
        if entry is None:continue
        if type(entry) is not dict or type(entry.get('path')) is not str or not entry['path'] or not re.fullmatch('[0-9a-f]{64}',str(entry.get('raw_sha256',''))):fail('refused','Malformed raw input coordinate')
    if request['supplied_views'] is not None and set(request['supplied_views'])!={'path','raw_sha256'}:fail('refused','Malformed supplied views binding')
    selections=request['selections']
    if type(selections) is not list:fail('refused','Selections must be an ordered list')
    if request['supplied_views'] is not None and not selections:fail('refused','Supplied views require nonempty matching selections')
    for s in selections:
        if type(s) is not dict or set(s)!={'seeds','budget_records'} or type(s['seeds']) is not list or not s['seeds']:fail('refused','Malformed selection')
        if any(type(x) is not str or not x for x in s['seeds']) or len(set(s['seeds']))!=len(s['seeds']):fail('refused','Seeds must be unique exact source identities')
        if s['budget_records'] is not None and (type(s['budget_records']) is not int or s['budget_records']<0):fail('refused','Budget must be a nonnegative record count or null')
    ctx=request['context_binding']
    if ctx is not None and (type(ctx) is not dict or set(ctx)!={'rendered_sha256','activation_identity'} or type(ctx['activation_identity']) is not dict or not re.fullmatch('[0-9a-f]{64}',str(ctx['rendered_sha256']))):fail('refused','Malformed context binding')

def model_output(imported,raw_sha):
    e=imported['envelope']
    return {'identity':e['id'],'rawSha256':raw_sha,'canonicalSha256':imported['model_sha256'],
      'envelope':bridge.canonical(e),'records':[record_output(r) for r in imported['records']],
      'references':[reference_output(r) for r in imported['references']],
      'externalResolutions':[{'identity':v['external_identity'],'payload':bridge.canonical(v)} for v in e['external_resolutions']],
      'edges':imported['edges'],'invalidation':bridge.canonical(e['interpretation']['invalidation'])}

def projection_output(imported,cert,raw_sha):
    e,b=imported['envelope'],cert['boundary']
    return {'parentIdentity':e['id'],'parentRawSha256':raw_sha,'parentCanonicalSha256':imported['model_sha256'],
      'parentEnvelope':bridge.canonical(e),'seeds':sorted(cert['seeds']),'included':cert['included'],'excluded':cert['excluded'],
      'records':[record_output(r) for r in cert['records']],
      'external':[{'identity':v['external_identity'],'payload':bridge.canonical(v)} for v in b['external']],
      'ordinary':[reference_output(v) for v in b['non_governing_references']],
      'unresolved':[record_output(v) for v in b['unresolved_residual_records']],
      'excludedResiduals':[record_output(v) for v in b['excluded_residual_records']],
      'invalidation':bridge.canonical(b['invalidation'])}

def graphify_view(imported,cert,selection):
    """Declared boundary mapping to the actual existing Graphify view schema."""
    ids={r['index']:r['record']['id'] for r in imported['records']};b=cert['boundary']
    populations={f:[r['record'] for r in cert['records'] if r['family']==f] for f in bridge.FAMILIES}
    return {'profile':'a_c.graphify.projection/1','parent':{'id':imported['envelope']['id'],'sha256':imported['model_sha256'],'profile':imported['envelope']['profile']},
      'selection':{'seeds':selection['seeds'],'dependency_contract':imported['envelope']['dependency_contract'],'budget_records':selection['budget_records']},
      'included':sorted(ids[i] for i in cert['included']),'excluded':sorted(ids[i] for i in cert['excluded']),
      'populations':populations,'boundary':{
        'external':sorted(b['external'],key=lambda e:e['external_identity']),
        'unresolved_residuals':sorted(ids[i] for i in b['retained_residuals']),
        'crossing_relations':[{k:r['record'][k] for k in ('id','kind','source','target')} for r in b['crossing_relations']],
        'non_governing_references':[{'owner':ids[r['owner']],'path':[str(x) for x in r['path']],'target':ids[r['target']],'domain':r['domain']} for r in b['non_governing_references']],
        'invalidation':b['invalidation']},
      'claim':'view of exact parent; not a replacement complete model or semantic acceptance'}

def _audit(log,expected):
    found={n:set(x.strip() for x in a.split(',') if x.strip()) for n,a in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]",log)}
    found.update({n:set() for n in re.findall(r"'([^']+)' does not depend on any axioms",log)})
    if set(found)!=set(expected) or any(a-AXIOMS for a in found.values()):fail('incomplete','Dynamic theorem coverage/axiom audit failed')
    return found

def verify(request,output_dir,limits=None,*,base_dir=None):
    started=time.monotonic();limits=DEFAULT_LIMITS|dict(limits or {});out=Path(output_dir).absolute();created=False
    result={'schema':'a_c.formal-gate.result/1','status':'incomplete','reason':None,'model':None,
      'request_sha256':digest(request),'inputs':{},'selections':request.get('selections') if isinstance(request,dict) else None,
      'context_binding':request.get('context_binding') if isinstance(request,dict) else None,
      'runtime_identity':None,'requested_claims':[],'checked_claims':[],
      'evidence':{'manifest_sha256':None,'members':{}},'observations':{'stages':[]},
      'limits':list(RESULT_LIMITS)}
    try:
        validate_request(request)
        base=Path(base_dir or Path.cwd())
        def source_path(binding):
            p=Path(binding['path']);return p if p.is_absolute() else base/p
        sources=[source_path(request['input']).absolute()]+([source_path(request['supplied_views']).absolute()] if request['supplied_views'] else [])
        if out.exists() or out.is_symlink():fail('refused','Evidence output already exists; no overwrite')
        for p in sources:
            if out.resolve()==p.resolve() or p.resolve().is_relative_to(out.resolve()):fail('refused','Evidence output overlaps an input')
            if p.is_symlink():fail('refused','Input symlinks are unsupported')
        out.mkdir(parents=True,exist_ok=False);created=True
        write_json(out/'request.json',request)
        replay=copy.deepcopy(request)
        for key,name in (('input','input.json'),('supplied_views','supplied-views.json')):
            binding=request[key]
            if binding is None:continue
            p=source_path(binding)
            try:
                if p.stat().st_size>limits['max_input_bytes']:fail('incomplete','Input exceeds selected byte resource limit')
                raw=p.read_bytes()
            except OSError as e:fail('incomplete','Required input unavailable: '+str(e))
            if hashlib.sha256(raw).hexdigest()!=binding['raw_sha256']:fail('refused','Raw input digest mismatch: '+key)
            (out/name).write_bytes(raw);replay[key]['path']=name
            result['inputs'][key]={'raw_sha256':binding['raw_sha256'],'bytes':len(raw),'retained_path':name}
        write_json(out/'replay-request.json',replay)
        if len(request['selections'])>limits['max_selections']:fail('incomplete','Selection count exceeds selected resource limit')
        parsed=read_json_bytes((out/'input.json').read_bytes())
        if request['input']['format']=='carrier':
            model=bridge.recover_carrier(parsed)
        else:
            model=parsed
        if not isinstance(model,dict):fail('refused','Model must be an object')
        if model.get('profile')!=bridge.MODEL_PROFILE:fail('unsupported','Unsupported model profile')
        sig=bridge._exact(model.get('signature'),('id','sha256','definition'),'signature')
        if (type(sig['id']) is not str or not sig['id'] or type(sig['sha256']) is not str
            or not re.fullmatch('[0-9a-f]{64}',sig['sha256']) or type(sig['definition']) is not dict):
            fail('refused','Malformed model signature fields')
        if sig.get('sha256') not in (bridge.SIGNATURE_SHA256,bridge.TOY_SIGNATURE_SHA256):
            try:validate_generation_profile(model)
            except ProfileError as e:fail('unsupported' if e.unsupported else 'refused',str(e))
        imported=bridge.import_model(model)
        if bridge.reconstruct(imported)!=model:fail('refused','Whole-source reconstruction mismatch')
        write_json(out/'model.json',model)
        raw_model_sha=support.sha(out/'input.json') if request['input']['format']=='model' else support.sha(out/'model.json')
        result['model']={'id':model['id'],'sha256':imported['model_sha256']}
        result['inputs']['model']={'raw_sha256':raw_model_sha,'canonical_sha256':imported['model_sha256'],'retained_path':'input.json' if request['input']['format']=='model' else 'model.json'}
        result['requested_claims']=['imported-model-well-formedness','whole-model-source-correspondence']
        if request['selections']:result['requested_claims']+=['declared-closure-and-projection','record-budget-result']
        if request['supplied_views']:result['requested_claims']+=['supplied-graphify-view-correspondence']
        result['observations'].update(records=len(imported['records']),references=len(imported['references']),edges=len(imported['edges']),reuse='none; fresh dynamic obligations; pinned established base support',
            execution='projectWithProof with exact freshly checked model/closure premises; per-selection equality to unchanged project is kernel-replayed; the raw checker is not reevaluated')
        initial=runtime_identity();result['runtime_identity']=initial
        t=time.monotonic()
        try:result['observations']['support']=support.check()
        except OSError as e:fail('incomplete','Selected proof support unavailable: '+str(e))
        except (ValueError,KeyError) as e:fail('refused','Selected proof support changed: '+str(e))
        result['observations']['stages'].append({'stage':'support-pins','seconds':time.monotonic()-t})
        names={r['record']['id']:r['index'] for r in imported['records']};cases=[]
        for selection in request['selections']:
            if any(s not in names for s in selection['seeds']):fail('refused','Selection names a nonlocal seed')
            c=bridge.closure_certificate(imported,[names[s] for s in selection['seeds']])
            c['effective_budget']=c['required_count'] if selection['budget_records'] is None else selection['budget_records'];cases.append(c)
        write_json(out/'certificates.json',cases)
        for name,source in {'GateData':data_source(imported,raw_model_sha),
                            'GateLocalNames':name_source(imported),'GateExternalNames':name_source(imported,True),
                            'GateIdentities':identities_source(imported),'GateBounds':bounds_source(imported),
                            'GateModel':model_proof(imported),'GateViews':views_source(cases),'GateRun':RUNNER}.items():(out/(name+'.lean')).write_text(source)
        prefix,env,_=support.proof_environment(out)
        def run(command,label):
            start=time.monotonic();log=out/(label+'.log')
            with log.open('wb') as f:
                try:r=runtime_process.run(command,cwd=ROOT,env=env,stdout=f,timeout=limits['timeout_seconds'])
                except subprocess.TimeoutExpired:fail('incomplete',label+' exceeded selected time limit')
                except (runtime_process.CleanupUnresolved,InterruptedError) as e:fail('incomplete',label+': '+str(e))
            elapsed=time.monotonic()-start
            result['observations']['stages'].append({'stage':label,'seconds':elapsed,'exit_code':r.returncode})
            if r.returncode:fail('incomplete',label+' did not complete successfully; diagnostic retained')
            return log.read_text()
        for name in ('GateData','GateLocalNames','GateExternalNames','GateIdentities','GateBounds','GateModel','GateViews'):
            log=run([str(prefix/'bin/lean'),'-j','1','-M',str(limits['memory_mb']),'-R',str(out),'-o',str(out/(name+'.olean')),str(out/(name+'.lean'))],name)
            if name=='GateLocalNames':_audit(log,name_contract_names(imported,False))
            elif name=='GateExternalNames':_audit(log,name_contract_names(imported,True))
            elif name=='GateIdentities':_audit(log,identity_contract_names(imported))
            elif name=='GateBounds':_audit(log,['AC.GateData.edgeBounds','AC.GateData.refBounds'] if len(imported['records'])>256 else [])
            elif name=='GateModel':_audit(log,['AC.GateData.model_checked'])
            elif name=='GateViews':_audit(log,[f'AC.GateData.{p}{i}' for i in range(len(cases)) for p in ('checked','set','reachability','result','execution_matches_project')])
        # Newly elaborated generated declarations are already kernel-checked with
        # skipKernelTC=false. Replay only this request's proof declarations.
        run([str(prefix/'bin/leanchecker'),'GateLocalNames','GateExternalNames','GateIdentities','GateBounds','GateModel','GateViews'],'dynamic-kernel-replay')
        log=run([str(prefix/'bin/lean'),'-j','1','-M',str(limits['memory_mb']),'--run',str(out/'GateRun.lean')],'actual-runtime')
        actual=read_json_bytes(log.encode())
        if actual.get('model')!=model_output(imported,raw_model_sha):fail('refused','Actual Lean whole-model output differs from imported source')
        expected_views=[]
        for c in cases:
            if c['effective_budget']<c['required_count']:expected_views.append({'status':'refused','reason':'insufficient record budget; required closure is not truncated'})
            else:expected_views.append({'status':'verified','projection':projection_output(imported,c,raw_model_sha)})
        if actual.get('views')!=expected_views:fail('refused','Actual Lean selected output differs from exact source/certificate')
        result['checked_claims']=['imported-model-well-formedness','whole-model-source-correspondence']
        if cases:result['checked_claims']+=['declared-closure-and-projection','record-budget-result']
        if request['supplied_views']:
            supplied=read_json_bytes((out/'supplied-views.json').read_bytes())
            expected=[graphify_view(imported,c,s) for c,s in zip(cases,request['selections'])]
            if supplied!=expected:fail('refused','Supplied Graphify view differs from actual formal result/boundary mapping')
            result['checked_claims'].append('supplied-graphify-view-correspondence')
            write_json(out/'view-comparison.json',{'status':'equal','supplied_sha256':request['supplied_views']['raw_sha256'],'formal_runtime_sha256':support.sha(out/'actual-runtime.log'),'boundary_mapping':'a_c.lean.graphify-view/1'})
        if runtime_identity()!=initial:fail('refused','Deciding verifier/profile/proof source changed during verification')
        t=time.monotonic()
        try:support.check()
        except OSError as e:fail('incomplete','Proof support unavailable during verification: '+str(e))
        except (ValueError,KeyError) as e:fail('refused','Proof support changed during verification: '+str(e))
        result['observations']['stages'].append({'stage':'support-pins-after','seconds':time.monotonic()-t})
        if any(c['effective_budget']<c['required_count'] for c in cases):fail('refused','Insufficient record budget; verified refusal, no truncated projection')
        result['status']='verified'
    except GateError as e:result.update(status=e.status,reason=e.reason)
    except ScriptNamespaceError as e:result.update(status='refused',reason=str(e))
    except bridge.Refusal as e:result.update(status='refused',reason=str(e))
    except (OSError,ValueError,KeyError,TypeError,subprocess.SubprocessError,RecursionError) as e:result.update(status='incomplete',reason=type(e).__name__+': '+str(e))
    result['observations']['elapsed_seconds']=time.monotonic()-started
    result['observations']['limits']=limits
    result['observations']['child_maxrss_native_units']=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    if created:
        members={p.name:support.sha(p) for p in sorted(out.iterdir()) if p.is_file() and p.name not in ('manifest.json','result.json')}
        manifest={'schema':'a_c.formal-gate.bundle/1','members':members}
        write_json(out/'manifest.json',manifest)
        result['evidence']={'manifest_sha256':support.sha(out/'manifest.json'),'members':members}
        write_json(out/'result.json',result)
    return result

def check_evidence(bundle,output_dir,limits=None):
    old=Path(bundle).resolve();out=Path(output_dir).resolve()
    if out==old or out.is_relative_to(old) or old.is_relative_to(out):return _recheck_failure('Evidence output overlaps prior bundle')
    try:
        manifest=read_evidence_json(old/'manifest.json');saved=read_evidence_json(old/'result.json')
        if manifest.get('schema')!='a_c.formal-gate.bundle/1' or saved.get('evidence',{}).get('manifest_sha256')!=support.sha(old/'manifest.json'):return _recheck_failure('Evidence manifest binding mismatch')
        for name,h in manifest['members'].items():
            if Path(name).name!=name or (old/name).is_symlink() or support.sha(old/name)!=h:return _recheck_failure('Retained evidence member missing/changed: '+name)
        if saved.get('runtime_identity')!=runtime_identity():return _recheck_failure('Evidence verifier/proof/profile pins are stale')
        original=bridge.read_json(old/'request.json');replay=bridge.read_json(old/'replay-request.json')
        if digest(original)!=saved.get('request_sha256'):return _recheck_failure('Original request digest changed')
        expected=copy.deepcopy(original)
        expected['input']['path']='input.json'
        if expected['supplied_views']:expected['supplied_views']['path']='supplied-views.json'
        if replay!=expected:return _recheck_failure('Retained replay request differs from original selections/bindings')
        result=verify(replay,out,limits,base_dir=old)
        return result
    except (OSError,ValueError,KeyError,TypeError) as e:return _recheck_failure('Evidence unavailable/malformed: '+str(e))

def _recheck_failure(reason):
    return {'schema':'a_c.formal-gate.result/1','status':'refused','reason':reason,'checked_claims':[],'evidence':None,'limits':list(RESULT_LIMITS)}

def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='command',required=True)
    sub.add_parser('identity')
    p=sub.add_parser('verify');p.add_argument('--request',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    p=sub.add_parser('check-evidence');p.add_argument('--bundle',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.command=='identity':print(json.dumps(runtime_identity(),sort_keys=True));return 0
    if args.command=='verify':
        req=bridge.read_json(args.request)
        result=verify(req,args.output,base_dir=args.request.resolve().parent)
    else:result=check_evidence(args.bundle,args.output)
    print(json.dumps(result,ensure_ascii=False,sort_keys=True));return EXIT[result['status']]
if __name__=='__main__':
    try:sys.exit(main())
    except Exception as e:
        print(json.dumps({'schema':'a_c.formal-gate.result/1','status':'incomplete','reason':type(e).__name__+': '+str(e),'limits':list(RESULT_LIMITS)},sort_keys=True));sys.exit(4)
