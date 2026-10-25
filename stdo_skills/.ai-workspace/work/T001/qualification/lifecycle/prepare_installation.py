"""Exercise shipped scoped update recipes before an actual post-update host trial.

Only disposable fixtures are mutated. No host is launched here. The original
candidate is copied unchanged; the compatible successor is explicitly a local
metadata-only test derivative, not an accepted Product revision.
"""
import argparse
import copy
import json
from pathlib import Path
import shutil
import subprocess
from prepare_lifecycle import QUAL, HERE, PRODUCT, PYTHON, common, pin, save, sha, inventory


def run(argv, records, expect=0):
    p=subprocess.run([str(a) for a in argv],capture_output=True,text=True)
    records.append({'argv':[str(a) for a in argv],'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
    if (expect==0 and p.returncode!=0) or (expect!=0 and p.returncode==0):
        raise ValueError('Unexpected recipe outcome: '+json.dumps(records[-1]))
    return p


def refresh(package, tenant):
    if tenant=='codex':
        p=package/'inventory.json';d=json.loads(p.read_text());d['activation']='qualification-compatible-update-only'
        d['files']=[{'path':x['path'],'sha256':x['sha256'],'bytes':x['bytes']} for x in inventory(package) if x['path']!='inventory.json']
        p.write_text(json.dumps(d,indent=2)+'\n')
    else:
        rows=['# Claude compatible-update fixture inventory','', 'This is a local metadata-only test derivative, not a Product release.','', '| Path | SHA256 |','| --- | --- |']
        rows += ['| '+x['path']+' | '+x['sha256']+' |' for x in inventory(package) if x['path']!='INVENTORY.md']
        (package/'INVENTORY.md').write_text('\n'.join(rows)+'\n')


def create(tenant,base):
    lane='installation-update';w=base/tenant/'workspace';c=base/tenant/'control';c.mkdir(parents=True)
    artifacts=['outputs/greeting.txt']
    common(w,'installed-update','# R1\nProduce Hello, <name>. and exactly one newline for inputs/name.txt. Preserve all installed skills, unrelated files and host configuration.\n',
        '# D1\nUse the current installed skill and exact method. Read the name, acquire current output, and make the single declared native Writer correction. Installation/update mechanics have already run; do not repeat them or remove a skill in this host activation.\n',
        '# Authorized post-update invocation\nThe owner authorizes only outputs/greeting.txt correction using the existing sources. Preserve the actual current installed package and receipts, both host configurations and unrelated contents. Read/compute and native Writer are permitted. No package update/removal, Git mutation, network, new actors or global configuration in this actor task.\n',artifacts)
    save(w/'inputs/name.txt','Ada\n');save(w/'outputs/greeting.txt','Hello, Grace.\n')
    save(w/'.agents/skills/unrelated-tool/SKILL.md','---\nname: unrelated-tool\ndescription: Only for an unrelated fixture operation.\n---\nKEEP\n')
    save(w/'.claude/skills/unrelated-tool/SKILL.md','---\nname: unrelated-tool\ndescription: Only for an unrelated fixture operation.\n---\nKEEP\n')
    save(w/'.codex/config.toml','# Existing local configuration; retain unchanged.\n')
    save(w/'.claude/settings.json',{})
    original=PRODUCT/'build_tenants'/tenant;old=c/'source-old';new=c/'source-compatible-update';shutil.copytree(original,old);shutil.copytree(original,new)
    oldinv=old/('inventory.json' if tenant=='codex' else 'INVENTORY.md')
    assert sha(oldinv)==('337d274efde96147c8e9a2db3e3b25f7631731fc8486562c9022ad087833aa36' if tenant=='codex' else '42d246cbe2fcf1414b0fd7ed094be74d6f2607595525555caa52618d8999f79a')
    if tenant=='codex':
        p=new/'skills/stdo-work/source-routes.json';d=json.loads(p.read_text());d['fixture_update']={'revision':2,'standing':'metadata-only controlled compatible update; no method or instructions changed'};p.write_text(json.dumps(d,indent=2)+'\n')
        package_root=new/'skills/stdo-work';dest=w/'.agents/skills/stdo-work';oldcheck=old/'tests/verify_package.py';newcheck=new/'tests/verify_package.py'
    else:
        p=new/'skills/stdo-release-install/references/maintenance.md';p.write_text(p.read_text()+'\n<!-- Controlled compatible metadata update 2; method and behavioral instructions unchanged. -->\n')
        package_root=new/'skills';dest=w/'.claude/skills';helper_rel='skills/stdo-release-install/scripts/manage_install.py';oldhelper=old/helper_rel;newhelper=new/helper_rel
    refresh(new,tenant)
    records=[]
    preserved={str(p.relative_to(w)):sha(p) for p in sorted(w.rglob('*')) if p.is_file()}
    if tenant=='codex':
        run([PYTHON,'-B',oldcheck,old,'--destination',dest],records)
        run(['/bin/cp','-R',old/'skills/stdo-work',dest],records)
        run([PYTHON,'-B',oldcheck,old,'--installed',dest],records)
    else:
        first=run([PYTHON,'-I','-B',oldhelper,'install','--package',old,'--workspace',w],records)
        receipt_sha=json.loads(first.stdout)['receipt_sha256']
    initial=inventory(w)
    negatives=[]
    for mutation in ['extra','modified','foreign']:
        nw=base/tenant/'negative'/mutation;shutil.copytree(w,nw)
        unit=nw/('.agents/skills/stdo-work' if tenant=='codex' else '.claude/skills/stdo-workspace-change')
        if mutation=='extra':(unit/'local-note.txt').write_text('KEEP local user content\n')
        elif mutation=='modified':(unit/'SKILL.md').write_text((unit/'SKILL.md').read_text()+'\nLOCAL CHANGE\n')
        else:
            shutil.rmtree(unit);unit.mkdir();(unit/'foreign.txt').write_text('KEEP foreign same-name unit\n')
        before=inventory(nw);calls=[]
        if tenant=='codex':
            # The documented update/remove both require this successful custody
            # step before any destructive instruction. Its real refusal stops them.
            for action in ['update','remove']:
                run([PYTHON,'-B',oldcheck,old,'--installed',unit],calls,expect=1)
        else:
            run([PYTHON,'-I','-B',newhelper,'update','--package',new,'--workspace',nw,'--receipt-sha256',receipt_sha],calls,expect=1)
            run([PYTHON,'-I','-B',oldhelper,'remove','--workspace',nw,'--receipt-sha256',receipt_sha],calls,expect=1)
        after=inventory(nw);assert before==after
        negatives.append({'mutation':mutation,'workspace':str(nw),'before':before,'calls':calls,'after':after,'standing':'Actual shipped refusal before any replacement/removal; all bytes preserved'})
    if tenant=='codex':
        run([PYTHON,'-B',oldcheck,old,'--installed',dest],records)
        run([PYTHON,'-B',newcheck,new],records)
        retired=c/'retired-old-install';run(['/bin/mv',dest,retired],records)
        run([PYTHON,'-B',newcheck,new,'--destination',dest],records)
        run(['/bin/cp','-R',new/'skills/stdo-work',dest],records)
        run([PYTHON,'-B',newcheck,new,'--installed',dest],records)
    else:
        result=run([PYTHON,'-I','-B',newhelper,'update','--package',new,'--workspace',w,'--receipt-sha256',receipt_sha],records)
        new_receipt_sha=json.loads(result.stdout)['receipt_sha256']
    for rel,h in preserved.items():assert sha(w/rel)==h
    freeze=HERE/'installations'/tenant
    custody={'schema':'stdo_skills.actual-installation-lifecycle/1','tenant':tenant,'workspace':str(w),'old_inventory':pin(oldinv),
        'new_inventory':pin(new/('inventory.json' if tenant=='codex' else 'INVENTORY.md')),
        'compatibility':'Controlled metadata-only derivative; no algorithm/skill instructions, method pin, host roster or tool binding changed. Not an accepted Product revision.',
        'initial':initial,'records':records,'negative_cases':negatives,'post_update':inventory(w),'preserved_original_files':preserved,'removal':'Not yet performed; wait actual post-update invocation and evidence capture'}
    save(freeze/'UPDATE-CUSTODY.json',custody)
    save(control_prompt:=c/'ordinary-prompt.base.txt','Please correct outputs/greeting.txt for inputs/name.txt under the existing requirement and design, using the current installed skill. Preserve unrelated files and both host configurations. I authorize the bounded task in TASK.md.\n')
    stable=[str(p.relative_to(w)) for p in sorted(w.rglob('*')) if p.is_file() and str(p.relative_to(w)) not in artifacts + ['.claude/stdo-skills-claude.receipt.json'] and not str(p.relative_to(w)).startswith(('.agents/skills/','.claude/skills/'))]
    save(freeze/'INPUTS.json',{'schema':'stdo_skills.fixture-inputs/1','workspace':str(w),'files':inventory(w)})
    fixture={'schema':'stdo_skills.qualification-fixture/1','tenant':tenant,'lane':lane,'workspace':str(w),'control':str(c),'artifact_paths':artifacts,'stable_input_paths':stable,'input_manifest':pin(freeze/'INPUTS.json')}
    save(freeze/'fixture.json',fixture)
    template=QUAL/'selections'/('codex-recovery-histories.json' if tenant=='codex' else 'claude-basis-tool-diagnostics.json')
    selected=json.loads(template.read_text());selected.update({'lane':lane,'standing':'Actual shipped installation/update done in this isolated fixture; Root selects actual post-update invocation separately',
        'candidate_record':custody['new_inventory'],'tenant_root':str(new),'install_documentation':pin(new/('README.md' if tenant=='codex' else 'INSTALL.md')),'package_root':str(package_root),
        'package_files':[{'path':str(p.relative_to(package_root)),'sha256':sha(p)} for p in sorted(package_root.rglob('*')) if p.is_file()],
        'fixture_record':pin(freeze/'fixture.json'),'timeout_ms':600000,'install_checks':{'before':[],'after':[]}})
    if tenant=='codex':selected['install_binding']={'kind':'codex-existing-package/1','verifier':pin(newcheck),'custody':pin(freeze/'UPDATE-CUSTODY.json')}
    else:selected['install_binding']={'kind':'claude-bundle-installer/1','action':'verified-existing','helper':pin(newhelper),'receipt_sha256':new_receipt_sha,'custody':pin(freeze/'UPDATE-CUSTODY.json')}
    path=QUAL/'selections'/(tenant+'-'+lane+'.json');save(path,selected)
    print(json.dumps({'selection':pin(path),'custody':pin(freeze/'UPDATE-CUSTODY.json'),'fixture':pin(freeze/'fixture.json')}))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--tenant',choices=['codex','claude'],required=True);p.add_argument('--base',type=Path,required=True);a=p.parse_args();create(a.tenant,a.base.resolve())
