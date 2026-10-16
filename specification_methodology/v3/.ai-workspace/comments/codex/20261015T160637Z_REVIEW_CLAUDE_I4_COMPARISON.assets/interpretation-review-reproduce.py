"""Read-only replay over frozen subjects; all runtime outputs go to /tmp.

Run with python3 -B. This checks structural/projection behavior, not semantics.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

BASE = Path('/tmp/stdo-i4-review-20261015T160637Z')
REPO = Path('/Users/jim/src/apps/specification_methodology')
REL = Path('specification_methodology/v3/build_tenants')
C = BASE / 'claude' / REL / 'claude'
X = BASE / 'codex' / REL / 'codex'
THEORY = Path('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2')
INSTALL = X / 'a_c/install/axiom_indexer-v2.5.1-rc.2'
TOOL = INSTALL / 'build_tenants/core/code/ac.py'
OUT = BASE / 'interpretation-review-checks'
OUT.mkdir(exist_ok=True)
REPORT = {'purpose': 'Read-only mechanical reproduction; not fresh-use qualification', 'commands': [], 'tool_verification': [], 'projections': []}

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def run(args, cwd, stdout_file=None):
    started = time.monotonic()
    p = subprocess.run(args, cwd=cwd, capture_output=True)
    row = {'argv': [str(a) for a in args], 'cwd': str(cwd), 'exit_code': p.returncode,
           'stdout': p.stdout.decode(errors='replace'), 'stderr': p.stderr.decode(errors='replace'),
           'elapsed_seconds': time.monotonic()-started}
    REPORT['commands'].append(row)
    if stdout_file is not None:
        stdout_file.write_bytes(p.stdout)
    return p

receipt = json.loads((X / 'a_c/INSTALL_RECEIPT.json').read_text())
for row in receipt['members']:
    path = INSTALL / row['path']
    expected = subprocess.check_output(['git', 'show', '9a9c479776ffd974fbcafcf48341980918209aef:axiom_indexer/' + row['path']], cwd=REPO)
    actual = str(path.readlink()).encode() if path.is_symlink() else path.read_bytes()
    check = {'path': row['path'], 'sha256': sha(actual), 'bytes': len(actual),
             'matches_immutable_git': actual == expected, 'matches_release_inventory': sha(actual) == row['sha256']}
    REPORT['tool_verification'].append(check)
    assert check['matches_immutable_git'] and check['matches_release_inventory'], check
assert sha((THEORY/'manifest.json').read_bytes()) == '3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782'
assert sha((THEORY/'standards/AXIOMATIC_CALCULUS.md').read_bytes()) == 'cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d'
REPORT['theory_verified'] = True

run([sys.executable,'-I','-B','a_c/i3/tools/assemble.py','--check'], C)
binding = OUT/'codex-bindings.json'
bound = run([sys.executable,'-B','interpretation/bindings.py','--theory-root',str(THEORY)], X/'successor', binding)
assert bound.returncode == 0

for who, root, program, source_map, bindings, cases in [
    ('claude', C, C/'a_c/i3/axiomatic-program.json', C/'a_c/i3/logical-constraint-map.json', C/'a_c/i3/bindings.json',
     {n:['urn:stdo-3:claude:i3:frame-index:'+n] for n in ['result-algebra-and-conjunction','authority-kinds','reuse-and-invalidation','promotion-block']}),
    ('codex', X/'successor', X/'successor/interpretation/program.json', X/'successor/interpretation/map.json', binding,
     {n:['urn:codex-stdo3:iteration-3-r2:index:'+i for i in ids] for n,ids in {
         'current-surface-writing':['WRITING_GUIDE.current-surface-writing'],
         'good-prose':['WRITING_GUIDE.good-prose'],
         'evaluate-conjoin':['TRANSFORMATION_LIBRARY.evaluate','TRANSFORMATION_LIBRARY.conjoin'],
         'work-recovery':['TRANSFORMATION_LIBRARY.workrecovery-specialization']}.items()})]:
    run([sys.executable,'-B',str(TOOL),'validate','--program',str(program),'--bindings',str(bindings),
         '--output',str(OUT/(who+'-validation.json')),'--emit-map',str(OUT/(who+'-new-map.json'))],root)
    for name, indexes in cases.items():
        for mode in ['reference-only','materialized']:
            output=OUT/(who+'-'+name+'-'+mode+'.json')
            command=[sys.executable,'-B',str(TOOL),'project','--program',str(program),'--map',str(source_map),
                     '--bindings',str(bindings),'--mode',mode,'--output',str(output)]
            for index in indexes:
                command += ['--frame-index',index]
            proc=run(command, root)
            if output.exists():
                raw=output.read_bytes()
                value=json.loads(raw)
                counts={k:len(v) for k,v in value.items() if isinstance(v,(list,dict))}
                clauses=value.get('clauses',value.get('clause_relations',[]))
                REPORT['projections'].append({'candidate':who,'case':name,'mode':mode,'exit_code':proc.returncode,
                    'bytes':len(raw),'sha256':sha(raw),'fields':sorted(value),'counts':counts,'file':str(output)})

(OUT/'results.json').write_text(json.dumps(REPORT,indent=2)+'\n')
print(json.dumps({'report':str(OUT/'results.json'),'tool_members_verified':len(REPORT['tool_verification']),
    'commands':len(REPORT['commands']), 'exits':[r['exit_code'] for r in REPORT['commands']],
    'projections':REPORT['projections']},indent=2))
