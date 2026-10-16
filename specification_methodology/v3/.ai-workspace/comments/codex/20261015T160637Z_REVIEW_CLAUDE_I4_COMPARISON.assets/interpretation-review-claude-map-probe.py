"""Isolate published Claude map staleness from extraction or binding layout."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

BASE=Path('/tmp/stdo-i4-review-20261015T160637Z')
REL='specification_methodology/v3/build_tenants/'
C=BASE/'claude'/REL/'claude'
X=BASE/'codex'/REL/'codex'
OUT=BASE/'interpretation-review-checks'
OUT.mkdir(exist_ok=True)
THEORY=Path('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2')
TOOL=X/'a_c/install/axiom_indexer-v2.5.1-rc.2/build_tenants/core/code/ac.py'
REPO=Path('/Users/jim/src/apps/specification_methodology')
sha=lambda raw:hashlib.sha256(raw).hexdigest()
report={'subject':'8a0ea226e8662695f8c0a79e56be7416a21549b0','frozen_files':[],'commands':[]}
for name in ['axiomatic-program.json','logical-constraint-map.json','bindings.json']:
    relative=REL+'claude/a_c/i3/'+name
    frozen=(C/'a_c/i3'/name).read_bytes()
    git=subprocess.check_output(['git','show',report['subject']+':'+relative],cwd=REPO)
    report['frozen_files'].append({'path':relative,'sha256':sha(frozen),'matches_exact_git_object':frozen==git})
    assert frozen==git
old=json.loads((C/'a_c/i3/logical-constraint-map.json').read_text())
program=json.loads((C/'a_c/i3/axiomatic-program.json').read_text())
report['published_map_program_sha256']=old['program_sha256']
bindings=OUT/'claude-absolute-bindings.json'
bindings.write_text(json.dumps({'kind':'axiom-indexer.binding-set','schema_version':1,'bindings':[
    {'uri_prefix':'stdo-3://build_tenants/claude/standards/','path':str(C/'standards')},
    {'uri_prefix':'stdo://releases/v2.5.1-rc.2/standards/','path':str(THEORY/'standards')}]},indent=2)+'\n')
def run(args):
    p=subprocess.run([str(a) for a in args],cwd=C,capture_output=True,text=True)
    report['commands'].append({'argv':[str(a) for a in args],'cwd':str(C),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
    return p
run([sys.executable,'-B',TOOL,'validate','--program',C/'a_c/i3/axiomatic-program.json','--bindings',bindings,
     '--output',OUT/'claude-absolute-validation.json','--emit-map',OUT/'claude-absolute-map.json'])
fresh=json.loads((OUT/'claude-absolute-map.json').read_text())
report['actual_program_sha256']=fresh['program_sha256']
report['observations_changed']=[{'before':a,'after':b} for a,b in zip(old['resolved_sources'],fresh['resolved_sources']) if a!=b]
for label,map_path in [('published',C/'a_c/i3/logical-constraint-map.json'),('regenerated',OUT/'claude-absolute-map.json')]:
    for mode in ['reference-only','materialized']:
        output=OUT/('claude-'+label+'-absolute-result-'+mode+'.json')
        run([sys.executable,'-B',TOOL,'project','--program',C/'a_c/i3/axiomatic-program.json','--map',map_path,
             '--bindings',bindings,'--frame-index','urn:stdo-3:claude:i3:frame-index:result-algebra-and-conjunction',
             '--mode',mode,'--output',output])
        if output.exists():
            raw=output.read_bytes(); parsed=json.loads(raw)
            report.setdefault('outputs',[]).append({'name':output.name,'bytes':len(raw),'sha256':sha(raw),
                'clause_count':len(parsed.get('clauses',parsed.get('clause_relations',[])))})
(OUT/'claude-map-probe.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
