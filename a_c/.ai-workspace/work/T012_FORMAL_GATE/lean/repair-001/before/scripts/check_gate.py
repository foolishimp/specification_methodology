#!/usr/bin/env python3
"""Retained real-kernel qualification of reusable gate inputs, runtime and refusal controls."""
from __future__ import annotations
import argparse,copy,json,os,subprocess,sys,time
from pathlib import Path
import formal_gate as gate
import formal_support as support
import gate_codegen
import import_fixture as bridge
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tests'))
from test_formal_gate import new_subject,request_for,ac_graph


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--large-model',type=Path);args=parser.parse_args()
    out=args.output.resolve();out.mkdir(parents=True,exist_ok=False);start=time.monotonic();records=[]
    def run(label,request,expected):
        result=gate.verify(request,out/label)
        row={'case':label,'status':result['status'],'expected':expected,'reason':result['reason'],'seconds':result['observations']['elapsed_seconds'],'evidence':result['evidence']['manifest_sha256']}
        records.append(row);print(json.dumps(row),flush=True)
        if result['status']!=expected:raise RuntimeError('unexpected gate status for '+label)
        return result
    try:
        r=subprocess.run([sys.executable,'-m','unittest','discover','-s',str(ROOT/'tests'),'-p','test_*.py','-v'],cwd=ROOT,capture_output=True,text=True,timeout=120)
        (out/'unit-tests.log').write_text(r.stdout+r.stderr)
        if r.returncode:raise RuntimeError('unit controls failed')
        payload='Exact "quotes", \\slashes, newline\n tab\t NUL\x00 unit\x1f DEL\x7f Unicode λ雪😀.\nend Injected\naxiom forged : False\n'
        model=new_subject(out/'subject-alpha','repo://formal-gate/new-alpha/',payload)
        model_path=out/'subject-alpha/model.json';imported=bridge.import_model(model)
        run('new-model-only',request_for(model_path),'verified')
        seed=imported['records'][0]['record']['id'];selection={'seeds':[seed],'budget_records':None}
        views=ac_graph.project_many(ac_graph.validate(model),[([seed],None)])
        gate.write_json(out/'actual-views.json',views)
        carrier=ac_graph.materialize(ac_graph.validate(model)).document;gate.write_json(out/'carrier.json',carrier)
        req=request_for(out/'carrier.json',[selection],{'path':str(out/'actual-views.json'),'raw_sha256':support.sha(out/'actual-views.json')})
        req['input']['format']='carrier';req['context_binding']={'rendered_sha256':'a'*64,'activation_identity':{'id':'qualification-only','sha256':'b'*64}}
        run('carrier-with-actual-view',req,'verified')
        replay=gate.check_evidence(out/'carrier-with-actual-view',out/'fresh-evidence-replay')
        records.append({'case':'fresh-evidence-replay','status':replay['status'],'expected':'verified','seconds':replay.get('observations',{}).get('elapsed_seconds')})
        if replay['status']!='verified':raise RuntimeError('fresh evidence replay failed: '+str(replay))
        altered=copy.deepcopy(views);altered[0]['populations']['objects'][0]['value']['definition']='ALTERED'
        gate.write_json(out/'altered-views.json',altered)
        bad=copy.deepcopy(req);bad['supplied_views']={'path':str(out/'altered-views.json'),'raw_sha256':support.sha(out/'altered-views.json')}
        run('changed-view-refuses',bad,'refused')
        budget=request_for(model_path,[{'seeds':[seed],'budget_records':0}]);run('budget-refuses',budget,'refused')
        second=new_subject(out/'subject-beta','repo://formal-gate/new-beta/')
        run('second-unseen-subject',request_for(out/'subject-beta/model.json'),'verified')
        # Negative kernel control imports the actual successful concrete model.
        negative=out/'kernel-negative';negative.mkdir()
        source='module\nimport GateViews\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\nset_option debug.skipKernelTC false\nexample : AC.checkCertificate AC.GateData.model.dependencies AC.GateData.model.localKeys AC.GateData.seeds0 [] = true := by decide +kernel\n'
        (negative/'Rejected.lean').write_text(source)
        prefix,env,_=support.tools();env['LEAN_PATH']=str(out/'carrier-with-actual-view')+os.pathsep+subprocess.check_output([str(prefix/'bin/lake'),'env','printenv','LEAN_PATH'],cwd=ROOT,env=env,text=True,timeout=10).strip()
        r=subprocess.run([str(prefix/'bin/lean'),'-j','1','-M','4096',str(negative/'Rejected.lean')],cwd=ROOT,env=env,capture_output=True,text=True,timeout=90)
        (negative/'rejection.log').write_text(r.stdout+r.stderr)
        if r.returncode==0 or 'decide' not in r.stdout:raise RuntimeError('false certificate was not rejected by kernel decision')
        records.append({'case':'false-closure-kernel-control','status':'rejected','expected':'rejected'})
        if args.large_model:run('large-model-only',request_for(args.large_model.resolve()),'verified')
        report={'status':'passed','cases':records,'runtime_identity':gate.runtime_identity(),'seconds':time.monotonic()-start,
                'limits':['Test-authored semantics only; no LLM or semantic acceptance claim.','Large model claim only if explicitly requested and passed.']}
    except Exception as e:
        report={'status':'incomplete','reason':str(e),'cases':records,'seconds':time.monotonic()-start}
    gate.write_json(out/'qualification.json',report);print(json.dumps(report,ensure_ascii=False,sort_keys=True))
    return 0 if report['status']=='passed' else 1
if __name__=='__main__':sys.exit(main())
