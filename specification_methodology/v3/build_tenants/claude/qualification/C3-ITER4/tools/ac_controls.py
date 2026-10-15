"""Port C5, adapted: positive checker run with adverse controls.
Usage, from the tenant root: python3 -I qualification/C3-ITER4/tools/ac_controls.py <scratch dir>
Writes qualification/C3-ITER4/returns/ac_controls.json. Every control states what it expects and what happened.
"""
import hashlib, json, os, shutil, subprocess, sys, time
SP = sys.argv[1]; os.makedirs(SP, exist_ok=True)
t0 = time.time()
rec = {'kind': 'claude-ac-controls', 'controls': []}
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def ctl(name, expect, holds, detail): rec['controls'].append({'control': name, 'expects': expect, 'holds': bool(holds), 'detail': detail})
# 1. materialise and identify the checker
out = subprocess.run(['bash', 'qualification/C3-ITER3/tools/verify_ai.sh', SP], capture_output=True, text=True)
AI = out.stdout.strip().splitlines()[-1]; AC = os.path.join(AI, 'build_tenants/core/code/ac.py')
rec['checker'] = {'ids': out.stdout.strip().splitlines()[0], 'ac_py_sha256': sha(AC)}
RECORDED_AC = '5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8'
ctl('identity-positive', 'materialised ac.py digest equals the recorded digest', sha(AC) == RECORDED_AC, sha(AC))
tam = os.path.join(SP, 'ac_tampered.py'); shutil.copy(AC, tam); open(tam, 'ab').write(b'\n# tampered\n')
ctl('identity-adverse', 'a tampered copy fails the same digest comparison', sha(tam) != RECORDED_AC, sha(tam))
PROG = 'a_c/i3/axiomatic-program.json'; BIND = 'a_c/i3/bindings.json'
def run(args):
    r = subprocess.run(['python3', '-I', AC] + args, capture_output=True, text=True); return r.returncode, r.stdout[-300:], r.stderr[-300:]
def validate(prog, tag):
    rep = os.path.join(SP, f'report-{tag}.json'); mp = os.path.join(SP, f'map-{tag}.json')
    rc, so, se = run(['validate', '--program', prog, '--bindings', BIND, '--output', rep, '--emit-map', mp])
    st = json.load(open(rep))['status'] if os.path.exists(rep) else None
    diag = len(json.load(open(rep)).get('diagnostics', [])) if os.path.exists(rep) else None
    return rc, st, diag, rep, mp, se
# 2. positive validation reproduces the frozen report
rc, st, diag, rep, mp, se = validate(PROG, 'positive')
ctl('validate-positive', 'exit 0, status valid, 0 diagnostics, report and map byte-identical to a_c/i3', rc == 0 and st == 'valid' and diag == 0 and sha(rep) == sha('a_c/i3/validation-report.json') and sha(mp) == sha('a_c/i3/logical-constraint-map.json'), {'exit': rc, 'status': st, 'diagnostics': diag, 'report_identical': sha(rep) == sha('a_c/i3/validation-report.json'), 'map_identical': sha(mp) == sha('a_c/i3/logical-constraint-map.json')})
# 3. adverse programs
prog = json.load(open(PROG))
m1 = dict(prog); m1['clauses'] = prog['clauses'] + [prog['clauses'][0]]; p1 = os.path.join(SP, 'prog-dup.json'); json.dump(m1, open(p1, 'w'), indent=1)
rc, st, diag, *_ , se = validate(p1, 'dup')
ctl('validate-adverse-duplicate-clause', 'a program with a duplicated clause uri is not valid', st != 'valid' or (diag or 0) > 0 or rc != 0, {'exit': rc, 'status': st, 'diagnostics': diag, 'stderr': se[-160:]})
m2 = json.loads(json.dumps(prog)); m2['clauses'][0]['source_refs'] = ['stdo-3://build_tenants/claude/standards/AXIOMATIC_CALCULUS.md#no-such-anchor-i4-control']; p2 = os.path.join(SP, 'prog-dangling.json'); json.dump(m2, open(p2, 'w'), indent=1)
rc, st, diag, *_ , se = validate(p2, 'dangling')
ctl('validate-adverse-dangling-source', 'a program whose clause cites a missing anchor is not valid', st != 'valid' or (diag or 0) > 0 or rc != 0, {'exit': rc, 'status': st, 'diagnostics': diag, 'stderr': se[-160:]})
# 4. projections reproduce byte for byte; a mutated index projects differently
os.makedirs(os.path.join(SP, 'proj'), exist_ok=True); same = []; 
for fi in prog['frame_indexes']:
    ix = fi['uri'].rsplit(':', 1)[-1]
    for mode in ('reference-only', 'materialized'):
        o = os.path.join(SP, 'proj', f'projection-{ix}-{mode}.json')
        rc, so, se = run(['project', '--program', PROG, '--map', 'a_c/i3/logical-constraint-map.json', '--bindings', BIND, '--frame-index', fi['uri'], '--mode', mode, '--output', o])
        f = f'a_c/i3/projections/projection-{ix}-{mode}.json'; same.append((ix, mode, rc, os.path.exists(o) and os.path.exists(f) and sha(o) == sha(f), se[-120:] if rc else ''))
ctl('project-positive', 'all 8 projections exit 0 and are byte-identical to a_c/i3/projections', all(rc == 0 and s for _, _, rc, s, _ in same), same)
m3 = json.loads(json.dumps(prog)); fi0 = m3['frame_indexes'][0]; dropped = fi0['clause_refs'].pop(); p3 = os.path.join(SP, 'prog-dropped.json'); json.dump(m3, open(p3, 'w'), indent=1)
rc3, st3, diag3, rep3, mp3, se3 = validate(p3, 'dropped')
o3 = os.path.join(SP, 'proj', 'dropped.json'); rc, so, se = run(['project', '--program', p3, '--map', mp3 if os.path.exists(mp3) else 'a_c/i3/logical-constraint-map.json', '--bindings', BIND, '--frame-index', fi0['uri'], '--mode', 'materialized', '--output', o3])
ix0 = fi0['uri'].rsplit(':', 1)[-1]; f0 = f'a_c/i3/projections/projection-{ix0}-materialized.json'
ctl('project-adverse-dropped-clause', 'a program with one clause dropped from a frame index projects differently from the frozen projection', (not os.path.exists(o3)) or sha(o3) != sha(f0), {'dropped': dropped, 'exit': rc, 'validate_status': st3, 'exists': os.path.exists(o3), 'stderr': se[-160:]})
rec['elapsed_seconds'] = round(time.time() - t0, 1); rec['holds_all'] = all(c['holds'] for c in rec['controls'])
json.dump(rec, open('qualification/C3-ITER4/returns/ac_controls.json', 'w'), indent=1)
for c in rec['controls']: print(('HOLDS ' if c['holds'] else 'FAILS '), c['control'], json.dumps(c['detail'])[:200])
print('all hold:', rec['holds_all'], 'elapsed', rec['elapsed_seconds'])
