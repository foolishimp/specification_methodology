#!/usr/bin/env python3
"""Replay bounded checks against an actual extracted PC/Skills distribution."""
from pathlib import Path
import argparse, copy, hashlib, json, re, shlex, shutil, subprocess, sys


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['products-root','native-root','stdo','fixture-root','queries-root','out']:
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--store',type=Path)
    p.add_argument('--python',type=Path,default=Path(sys.executable))
    p.add_argument('--predecessor-assessment',type=Path)
    p.add_argument('--assessment-python',type=Path)
    p.add_argument('--assessment-sdlc',type=Path)
    p.add_argument('--assessment-boundaries',type=Path)
    p.add_argument('--remove',action='store_true')
    args=p.parse_args();out=args.out.absolute();out.mkdir(parents=True,exist_ok=False)
    pc=args.products_root.absolute()/'purpose_context';sk=args.products_root.absolute()/'stdo_skills'
    native=args.native_root.absolute();public=json.loads((pc/'PUBLIC_MANIFEST.json').read_text());pin=sha(pc/'PUBLIC_MANIFEST.json')
    inventory=json.loads((sk/'INVENTORY.json').read_text());selected=inventory['release']['native_method']
    assert selected==public['release']['native_method'] and sha(native/'manifest.json')==selected['manifest_sha256']
    assert inventory['release']['version']=='3.1.0-rc.2'
    manager=args.stdo.absolute()
    if args.store:
        manager=out/'stdo'
        manager.write_text('#!/bin/sh\nexec '+shlex.quote(str(args.stdo.absolute()))+' --store '+shlex.quote(str(args.store.absolute()))+' "$@"\n');manager.chmod(0o755)
    logs=out/'operations';logs.mkdir();operations=[];hosts={};trial='STDO_3_1_RC2_2026-11-15 approved bounded context and successor-boundary trial'
    def retain():
        result={'kind':'stdo-3.1.distribution-checks/1','standing':'Finite local installed-path checks; not native actor decisions, automatic pickup or semantic assessment.',
                'products_root':str(args.products_root.absolute()),'native_root':str(native),'method':selected,'manager':str(manager),'python':str(args.python),
                'public_manifest_sha256':pin,'skills_inventory_sha256':sha(sk/'INVENTORY.json'),'operations':operations,'hosts':hosts,
                'negative_predecessor_assessment':str(args.predecessor_assessment) if args.predecessor_assessment else 'unperformed: not supplied'}
        (out/'RESULT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    def run(name,argv,expected=0,cwd=None):
        argv=[str(x) for x in argv];r=subprocess.run(argv,cwd=cwd,capture_output=True,text=True)
        (logs/(name+'.stdout')).write_text(r.stdout);(logs/(name+'.stderr')).write_text(r.stderr)
        passed=r.returncode==expected if isinstance(expected,int) else r.returncode in expected
        operations.append({'name':name,'argv':argv,'cwd':str(cwd) if cwd else None,'expected_returncode':expected,'returncode':r.returncode,'passed':passed,
                           'stdout_sha256':sha(logs/(name+'.stdout')),'stderr_sha256':sha(logs/(name+'.stderr'))});retain()
        assert passed,(name,r.stdout,r.stderr)
        try:return json.loads(r.stdout)
        except json.JSONDecodeError:return r.stdout
    for host in ['codex','claude']:
        workspace=out/host;shutil.copytree(args.fixture_root,workspace)
        for forbidden in ['.agents','.claude','__pycache__']:
            assert not (workspace/forbidden).exists(),'Select the frozen pre-actor fixture'
        (workspace/'unrelated.txt').write_text('retain across exact installation removal\n')
        definition=workspace/'stdo_trial.json';basis=json.loads(definition.read_text())['constitution']['stdo']['basis'];assert basis==selected
        verify=run(host+'-native-status',[manager,'status','--definition',definition,'--verify'])
        assert verify['installed'] is True and verify['valid'] is True and not verify['failures']
        manage=[args.python,'-B',sk/'scripts/manage_skills.py']
        inputs=['--package',sk,'--workspace',workspace,'--host',host,'--definition',definition,'--method-root',native,'--stdo',manager,'--python',args.python,'--purpose-context',pc]
        run(host+'-plan',manage+['plan']+inputs)
        receipt=run(host+'-install',manage+['install']+inputs)
        owned=['--workspace',workspace,'--host',host,'--receipt-sha256',receipt['receipt_sha256']]
        run(host+'-verify',manage+['verify']+owned)
        base=workspace/('.agents' if host=='codex' else '.claude');adapter=base/'skills/stdo-context/scripts/provider.py'
        run(host+'-runtime',manage+['check-runtime','--configuration',base/'stdo-skills/CONFIG.json'])
        description=run(host+'-describe',[args.python,'-B',adapter,'describe']);assert description['manifest_sha256']==pin
        command=[args.python,'-B',adapter,'context','--']
        listed=run(host+'-indexes',command+['indexes','--public-manifest-sha256',pin])
        observations=[]
        for name,suffix in [('python','python-pure-refactor-v2'),('sdlc','sdlc-workflow-v1')]:
            index_id='stdo-3.1.0-rc.2-'+suffix;query=args.queries_root/(name+'.json');bundle=out/(host+'-'+name+'-bundle');delivery=out/(host+'-'+name+'-delivery')
            run(host+'-'+name+'-bind',command+['bind','--index-id',index_id,'--source-root',native,'--method-uri',selected['uri'],'--method-manifest-sha256',selected['manifest_sha256'],'--public-manifest-sha256',pin,'--out',bundle])
            select=['select','--bundle',bundle,'--query',query,'--index-id',index_id,'--public-manifest-sha256',pin]
            entry=run(host+'-'+name+'-select',command+select)
            assessment=getattr(args,'assessment_'+name)
            support=['--assessment',assessment] if assessment else ['--trial-binding',trial]
            consume=['consume','--bundle',bundle,'--query',query,'--index-id',index_id,'--public-manifest-sha256',pin,*support,'--byte-budget','262144','--out',delivery]
            run(host+'-'+name+'-consume',command+consume)
            check=run(host+'-'+name+'-check',command+['check','--bundle',bundle,'--index',entry['index_path'],'--query',query,*support,'--byte-budget','262144','--context',delivery/'CONTEXT.json','--markdown',delivery/'CONTEXT.md'])
            body=json.loads((delivery/'CONTEXT.json').read_text())['payload'];assert not body['gaps']
            observations.append({'purpose':name,'index_id':index_id,'query':str(query.absolute()),'bundle':str(bundle),'delivery':str(delivery),'context_sha256':sha(delivery/'CONTEXT.json'),'markdown_sha256':sha(delivery/'CONTEXT.md'),'context_bytes':check['context_bytes'],'selected_rules':len(body['selected']),'covered':body['covered'],'assessment':str(assessment) if assessment else None})
            small=out/(host+'-'+name+'-overflow')
            overflow=['consume','--bundle',bundle,'--query',query,'--index-id',index_id,'--public-manifest-sha256',pin,*support,'--byte-budget','1','--out',small]
            run(host+'-'+name+'-overflow-refused',command+overflow,2);assert not small.exists()
            changed=json.loads(query.read_text());changed['facts'].pop('pure_local' if name=='python' else 'adopted_defaults')
            missing=out/(host+'-'+name+'-missing.json');missing.write_text(json.dumps(changed))
            run(host+'-'+name+'-unknown-family',command+['select','--bundle',bundle,'--query',missing,'--index-id',index_id,'--public-manifest-sha256',pin],3)
            other=args.queries_root/('sdlc.json' if name=='python' else 'python.json')
            run(host+'-'+name+'-wrong-purpose',command+['select','--bundle',bundle,'--query',other,'--index-id',index_id,'--public-manifest-sha256',pin],2)
            if name=='python' and args.predecessor_assessment:
                refused=out/(host+'-old-assessment-delivery')
                run(host+'-predecessor-assessment-refused',command+['consume','--bundle',bundle,'--query',query,'--index-id',index_id,'--public-manifest-sha256',pin,'--assessment',args.predecessor_assessment,'--byte-budget','262144','--out',refused],2);assert not refused.exists()
        boundary_observations=[]
        for name in ['acceptance','qualification','release','work','missing-boundary','null-boundary','ill-typed-boundary']:
            query=args.queries_root/(name+'.json')
            if not query.is_file():
                continue
            index_id='stdo-3.1.0-rc.2-sdlc-workflow-v1';bundle=out/(host+'-sdlc-bundle')
            delivery=out/(host+'-'+name+'-boundary')
            assessment=args.assessment_boundaries/(name+'.json') if args.assessment_boundaries else None
            if assessment is not None and not assessment.is_file():
                assessment=None
            support=['--assessment',assessment] if assessment else ['--trial-binding',trial]
            if name in ['missing-boundary','null-boundary','ill-typed-boundary']:
                refused=run(host+'-'+name+'-boundary-refused',command+['consume','--bundle',bundle,'--query',query,'--index-id',index_id,'--public-manifest-sha256',pin,*support,'--byte-budget','262144','--out',delivery],3)
                assert refused['status']=='incomplete' and refused['matches']['family']=='unknown' and not delivery.exists()
                boundary_observations.append({'case':name,'query':str(query.absolute()),'delivery':None,'selection_status':'incomplete','covered':False,'W35':'unperformed: family unknown','W26':'unperformed: family unknown','gaps':'family applicability unknown; no context delivery','context_sha256':None,'markdown_sha256':None,'selection_sha256':sha(logs/(host+'-'+name+'-boundary-refused.stdout')),'assessment':None})
                continue
            run(host+'-'+name+'-boundary-consume',command+['consume','--bundle',bundle,'--query',query,'--index-id',index_id,'--public-manifest-sha256',pin,*support,'--byte-budget','262144','--out',delivery])
            run(host+'-'+name+'-boundary-check',command+['check','--bundle',bundle,'--index',pc/'skills/stdo-context/indexes'/index_id/'INDEX.json','--query',query,*support,'--byte-budget','262144','--context',delivery/'CONTEXT.json','--markdown',delivery/'CONTEXT.md'])
            body=json.loads((delivery/'CONTEXT.json').read_text())['payload']
            states={x['rule']['id']:x['applicability'] for x in body['selected']}
            if name in ['acceptance','qualification','release']:
                assert states['W35']=='true' and body['selection_status']=='ready' and not body['gaps']
                assert states['W26']==('true' if name=='release' else 'false')
            elif name=='work':
                assert 'W35' not in states and body['selection_status']=='ready'
            else:
                assert states['W35']=='unknown' and body['selection_status']=='incomplete' and not body['covered']
            boundary_observations.append({'case':name,'query':str(query.absolute()),'delivery':str(delivery),'selection_status':body['selection_status'],'covered':body['covered'],'W35':states.get('W35','excluded'),'W26':states.get('W26','excluded'),'gaps':body['gaps'],'context_sha256':sha(delivery/'CONTEXT.json'),'markdown_sha256':sha(delivery/'CONTEXT.md'),'assessment':str(assessment) if assessment else None})
        run(host+'-wrong-public-pin',command+['indexes','--public-manifest-sha256','0'*64],2)
        run(host+'-wrong-native-selection',command+['bind','--index-id','stdo-3.1.0-rc.2-python-pure-refactor-v2','--source-root',native,'--method-uri','stdo://releases/v3.0.4/','--method-manifest-sha256',selected['manifest_sha256'],'--public-manifest-sha256',pin,'--out',out/(host+'-wrong-native')],2)
        run(host+'-collision',manage+['install']+inputs,2)
        guide=base/'stdo-skills/GETTING_STARTED.md';before=guide.read_bytes();guide.write_bytes(before+b'changed owned member\n')
        run(host+'-changed-owned-refused',manage+['verify']+owned,2)
        run(host+'-changed-remove-refused',manage+['remove']+owned,2)
        guide.write_bytes(before);run(host+'-restored-verify',manage+['verify']+owned)
        # Actual wrapper/native relation, independently checked from installed bytes.
        wrapper_results=[]
        for name in ['stdo-work','stdo-review','stdo-ticket','stdo-status','stdo-help']+(['stdo-refresh'] if host=='claude' else []):
            relative='claude-skills/refresh/SKILL.md' if name=='stdo-refresh' else 'skills/'+name+'/SKILL.md'
            target=native/'plugins/spec'/relative;wrapper=base/'skills'/name/'SKILL.md'
            original_header=re.match(r'\A---\r?\n.*?\r?\n---(?:\r?\n|\Z)',target.read_text(),re.S).group(0)
            expected=re.sub(r'^name:[^\r\n]*','name: '+name,original_header,count=1,flags=re.M)
            assert wrapper.read_text().startswith(expected) and target.as_uri() in wrapper.read_text()
            wrapper_results.append({'name':name,'wrapper_sha256':sha(wrapper),'native_sha256':sha(target),'frontmatter_equal_except_refresh_name':True})
        if args.remove:
            run(host+'-remove',manage+['remove']+owned)
            assert (workspace/'unrelated.txt').read_text()=='retain across exact installation removal\n'
        hosts[host]={'workspace':str(workspace),'definition':str(definition),'adapter':str(adapter),'receipt':receipt,'contexts':observations,'boundary_controls':boundary_observations,'native_wrappers':wrapper_results,'removed':args.remove};retain()
    for left,right in zip(hosts['codex']['contexts'],hosts['claude']['contexts'],strict=True):
        assert left['context_sha256']==right['context_sha256'] and left['markdown_sha256']==right['markdown_sha256']
    for left,right in zip(hosts['codex']['boundary_controls'],hosts['claude']['boundary_controls'],strict=True):
        assert left['context_sha256']==right['context_sha256'] and left['markdown_sha256']==right['markdown_sha256']
    retain();print(json.dumps({'status':'passed','operations':len(operations),'hosts':list(hosts),'result':str(out/'RESULT.json'),'public_manifest_sha256':pin,'skills_inventory_sha256':sha(sk/'INVENTORY.json')}))


if __name__=='__main__':main()
