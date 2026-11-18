#!/usr/bin/env python3
"""Exercise RC3 advancement and refusal against a disposable real Git remote."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

TOOL = Path(__file__).with_name('ref_transaction.py')
NAMES = ['specification_methodology','purpose_context','stdo_skills','a_c','stdo_representation','axiom_indexer']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    commands = []
    checks = []
    def run(name, argv, expected=0, cwd=None):
        p = subprocess.run([str(x) for x in argv], cwd=cwd, capture_output=True, text=True)
        (args.out/(name+'.stdout')).write_text(p.stdout)
        (args.out/(name+'.stderr')).write_text(p.stderr)
        commands.append({'name':name,'argv':[str(x) for x in argv],'exit':p.returncode,'expected':expected})
        (args.out/'COMMANDS.json').write_text(json.dumps(commands,indent=2)+'\n')
        assert (p.returncode == 0) == (expected == 0), name + ': ' + p.stderr
        return p.stdout.strip()
    with tempfile.TemporaryDirectory(prefix='stdo-rc3-ref-fixture-') as temporary:
        base=Path(temporary).resolve(); repo=base/'repo'; remote=base/'remote.git'; repo.mkdir()
        def git(*argv): return subprocess.check_output(['git','-C',str(repo),*argv],text=True,stderr=subprocess.DEVNULL).strip()
        subprocess.run(['git','init','--bare','-q',str(remote)],check=True)
        git('init','-q','-b','main'); git('config','user.name','STDO test fixture'); git('config','user.email','fixture@example.invalid')
        for name in NAMES:
            (repo/name).mkdir(); (repo/name/'README.md').write_text('predecessor fixture\n')
        git('add','.');git('commit','-q','-m','fixture predecessor'); old=git('rev-parse','HEAD')
        for name in NAMES:
            for tag in [f'{name}/v3.1.0-rc.2',f'{name}/v3.1.0']:
                git('tag','-a',tag,'-m','test fixture predecessor')
            for kind in ['rc','release']: git('branch',f'{kind}/{name}/3.1.0')
        git('remote','add','origin',str(remote));git('push','--mirror','origin')
        descriptor=repo/'releases/3.1.0-rc.3/COHORT_INPUTS.json'; descriptor.parent.mkdir(parents=True)
        descriptor.write_text(json.dumps({'version':'3.1.0-rc.3','native_predecessor':old,'source_predecessor':old,
          'products':[{'namespace':n,'root':n,'commit_role':'native-A' if n=='specification_methodology' else 'source-B'} for n in NAMES]}))
        (repo/'specification_methodology/README.md').write_text('native fixture RC3\n')
        git('add','.');git('commit','-q','-m','fixture native'); native=git('rev-parse','HEAD')
        git('tag','-a','specification_methodology/v3.1.0-rc.3',native,'-m','fixture native cut')
        (repo/'purpose_context/README.md').write_text('derived fixture RC3\n')
        git('add','.');git('commit','-q','-m','fixture carrier');carrier=git('rev-parse','HEAD')
        evidence=base/'evidence.txt';evidence.write_text('qualified fixture only\n')
        qualification=base/'qualification.json'
        qualification.write_text(json.dumps({'kind':'test-fixture-only','status':'qualified-for-declared-prepublication-claims',
          'carrier':carrier,'native':native,'expected_remote_main':old,
          'qualified_files':[{'path':str(evidence),'sha256':hashlib.sha256(evidence.read_bytes()).hexdigest()}]}))
        plan=base/'plan.json'
        def cli(mode):
            command=['python3','-B',str(TOOL),mode,'--root',str(repo),'--plan',str(plan),'--result',str(base/(mode+'.json'))]
            if mode=='prepare': command+=['--native',native,'--carrier',carrier,'--qualification',str(qualification)]
            return command
        def refs(): return {s.split('\t')[1]:s.split('\t')[0] for s in git('ls-remote','origin').splitlines()}
        initial=refs()
        future='refs/tags/a_c/v3.1.0-rc.3'
        subprocess.run(['git','--git-dir',str(remote),'update-ref',future,initial['refs/tags/a_c/v3.1.0-rc.2']],check=True)
        run('01-higher-ordinal-refused',cli('prepare'),expected=1); assert not plan.exists()
        subprocess.run(['git','--git-dir',str(remote),'update-ref','-d',future],check=True)
        checks.append('higher ordinal refuses before ref mutation')
        missing='refs/heads/release/a_c/3.1.0'
        subprocess.run(['git','--git-dir',str(remote),'update-ref','-d',missing,old],check=True)
        run('02-missing-predecessor-refused',cli('prepare'),expected=1);assert not plan.exists()
        subprocess.run(['git','--git-dir',str(remote),'update-ref',missing,old],check=True)
        checks.append('missing predecessor destination refuses')
        run('03-prepare',cli('prepare')); run('04-check',cli('check'))
        assert len(json.loads(plan.read_text())['refs'])==25
        checks.append('complete 25-ref advancement prepares and checks')
        saved=plan.read_bytes(); bad=json.loads(saved);bad['refs'].pop();plan.write_text(json.dumps(bad))
        run('05-incomplete-graph-refused',cli('check'),expected=1);plan.write_bytes(saved)
        checks.append('incomplete ref graph refuses')
        evidence.write_text('changed fixture\n');run('06-evidence-drift-refused',cli('check'),expected=1)
        evidence.write_text('qualified fixture only\n');checks.append('qualified evidence drift refuses')
        raced='refs/heads/rc/a_c/3.1.0'
        # Carrier commit exists only locally; copy objects before changing the remote fixture ref.
        git('push','origin',carrier+':refs/heads/fixture-object-transfer')
        subprocess.run(['git','--git-dir',str(remote),'update-ref',raced,carrier,old],check=True)
        run('07-remote-drift-refused',cli('publish'),expected=1)
        assert not any(f'refs/tags/{n}/v3.1.0-rc.3' in refs() for n in NAMES)
        subprocess.run(['git','--git-dir',str(remote),'update-ref',raced,old,carrier],check=True)
        subprocess.run(['git','--git-dir',str(remote),'update-ref','-d','refs/heads/fixture-object-transfer'],check=True)
        checks.append('remote lease drift refuses with no partial RC3')
        hook=remote/'hooks/pre-receive'
        hook.write_text('#!/bin/sh\nwhile read old new ref; do\n  case \"$ref\" in refs/tags/a_c/v3.1.0-rc.3) exit 1;; esac\ndone\nexit 0\n')
        hook.chmod(0o755)
        run('08-server-rejection',cli('publish'),expected=1);assert refs()==initial
        hook.unlink();checks.append('atomic server rejection leaves all prior remote refs unchanged')
        run('09-publish',cli('publish'))
        result=json.loads((base/'publish.json').read_text());assert result['remote_readback_valid']
        actual=refs();p=json.loads(plan.read_text())
        for row in p['refs']: assert actual[row['destination']]==row['object']
        for ref,obj in p['protected_predecessor_refs'].items(): assert actual[ref]==obj
        checks.append('atomic success publishes 25 exact refs and preserves all RC2 tag objects and peels')
    result={'kind':'stdo.rc3-ref-transaction-fixture/1','checks':checks,'passed':True,
      'tool_sha256':hashlib.sha256(TOOL.read_bytes()).hexdigest(),
      'limit':'Real local Git transport fixture only; no production publication or semantic qualification.'}
    (args.out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'checks':len(checks)}))


if __name__=='__main__':
    main()
