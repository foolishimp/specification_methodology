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
# expected digests are read from the common dependency contract, not from a constant
DEP = '../../specification/requirements/A_C_DEPENDENCY.md'
import re as _re
dep = open(DEP, encoding='utf-8').read()
expected = {k: _re.search(rf'\| {k} SHA256 \| ([0-9a-f]{{64}}) \|', dep).group(1) for k in ('Executable', 'Schema', 'Output-contract')}
files = {'Executable': AC, 'Schema': os.path.join(AI, 'skills/axiomatize-corpus/references/program.schema.json'), 'Output-contract': os.path.join(AI, 'skills/axiomatize-corpus/references/output-contract.md')}
def identity_check(paths):
    """The identity check: every named member's digest equals the contract's; returns (ok, mismatches)."""
    mism = [k for k, p in paths.items() if sha(p) != expected[k]]
    return (not mism), mism
ok, mism = identity_check(files)
ctl('identity-positive', 'the materialised executable, schema and output contract match the digests in A_C_DEPENDENCY.md', ok, {'expected': expected, 'mismatches': mism})
tampered = dict(files); tam = os.path.join(SP, 'program.schema.tampered.json'); shutil.copy(files['Schema'], tam); open(tam, 'ab').write(b'\n'); tampered['Schema'] = tam
ok2, mism2 = identity_check(tampered)
ctl('identity-adverse', 'the same identity check refuses when one member is tampered (one byte appended to the schema)', (not ok2) and mism2 == ['Schema'], {'mismatches': mism2})
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
        rc, so, se = run(['project', '--program', PROG, '--map', mp, '--bindings', BIND, '--frame-index', fi['uri'], '--mode', mode, '--output', o])  # the fresh map of the positive validate
        f = f'a_c/i3/projections/projection-{ix}-{mode}.json'; same.append((ix, mode, rc, os.path.exists(o) and os.path.exists(f) and sha(o) == sha(f), se[-120:] if rc else ''))
ctl('project-positive', 'all 8 projections from the fresh map exit 0 and are byte-identical to a_c/i3/projections', all(rc == 0 and s for _, _, rc, s, _ in same), same)
m3 = json.loads(json.dumps(prog)); fi0 = m3['frame_indexes'][0]; dropped = fi0['clause_refs'].pop(); p3 = os.path.join(SP, 'prog-dropped.json'); json.dump(m3, open(p3, 'w'), indent=1)
rc3, st3, diag3, rep3, mp3, se3 = validate(p3, 'dropped')
o3 = os.path.join(SP, 'proj', 'dropped.json'); rc, so, se = run(['project', '--program', p3, '--map', mp3 if os.path.exists(mp3) else 'a_c/i3/logical-constraint-map.json', '--bindings', BIND, '--frame-index', fi0['uri'], '--mode', 'materialized', '--output', o3])
ix0 = fi0['uri'].rsplit(':', 1)[-1]; f0 = f'a_c/i3/projections/projection-{ix0}-materialized.json'
base = os.path.join(SP, 'proj', f'projection-{ix0}-materialized.json')  # the fresh positive projection of the same index
ctl('project-adverse-dropped-clause', 'a program with one clause dropped from a frame index validates, and its projection differs from the fresh positive projection of that index (the passing baseline), and from the frozen one', st3 == 'valid' and os.path.exists(o3) and os.path.exists(base) and sha(o3) != sha(base) and sha(o3) != sha(f0), {'dropped': dropped, 'exit': rc, 'validate_status': st3, 'baseline_exists': os.path.exists(base), 'differs_from_fresh': os.path.exists(o3) and os.path.exists(base) and sha(o3) != sha(base), 'stderr': se[-160:]})
rec['elapsed_seconds'] = round(time.time() - t0, 1); rec['holds_all'] = all(c['holds'] for c in rec['controls'])
json.dump(rec, open('qualification/C3-ITER4/returns/ac_controls.json', 'w'), indent=1)
for c in rec['controls']: print(('HOLDS ' if c['holds'] else 'FAILS '), c['control'], json.dumps(c['detail'])[:200])
print('all hold:', rec['holds_all'], 'elapsed', rec['elapsed_seconds'])
