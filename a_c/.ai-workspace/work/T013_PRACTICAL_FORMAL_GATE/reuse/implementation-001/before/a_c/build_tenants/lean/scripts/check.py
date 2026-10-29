#!/usr/bin/env python3
"""Run the source/import, kernel, proof-contract, axiom and actual-output checks.

Exit zero establishes this finite mechanical fragment, never semantic acceptance.
Run scripts/bootstrap.py first. Logs default to ignored .lake/check/.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import time

from import_fixture import (FIXTURE_DIR, RAW_SHA256, canonical, closure_certificate,
                            import_model, load_checked, verify_fixture, TOY_FIXTURE_DIR, TOY_RAW_SHA256)

ROOT = Path(__file__).resolve().parents[1]
GENERIC_THEOREMS = [
    'checkModel_sound', 'certificate_seed_inclusion', 'certificate_closed',
    'certificate_exact_reachability', 'certificate_least', 'certificate_fixed_point',
    'certificate_unique', 'project_ok_properties', 'project_ok_exact_reachability',
    'insufficient_budget_refuses', 'projection_record_conservation',
    'projection_authority_basis_conservation', 'projection_parent_conservation',
    'projection_external_exact', 'projection_ordinary_exact', 'projection_residual_conservation',
    'projection_excluded_residual_exact', 'projection_all_residuals_accounted',
]
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}


def run(command, label, outdir, env, timeout=180):
    start = time.monotonic()
    result = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True, timeout=timeout)
    (outdir / f'{label}.log').write_text(result.stdout + result.stderr)
    if result.returncode:
        raise RuntimeError(f'{label} failed with exit {result.returncode}; see {outdir / (label + ".log")}')
    print(f'{label}: pass ({time.monotonic()-start:.2f}s)', flush=True)
    return result.stdout


def code_only(source):
    # Nested Lean block comments and strings are removed before checking prohibited
    # admission/unchecked-code tokens. This scan supplements the actual axiom audit.
    out, i, depth, string = [], 0, 0, False
    while i < len(source):
        if depth:
            if source.startswith('/-', i): depth += 1; i += 2
            elif source.startswith('-/', i): depth -= 1; i += 2
            else: i += 1
        elif string:
            if source[i] == '\\': i += 2
            elif source[i] == '"': string = False; out.append(' '); i += 1
            else: i += 1
        elif source.startswith('/-', i): depth = 1; i += 2
        elif source.startswith('--', i):
            end = source.find('\n', i); i = len(source) if end < 0 else end
        elif source[i] == '"': string = True; i += 1
        else: out.append(source[i]); i += 1
    return ''.join(out)


def record_output(entry):
    r = entry['record']
    return {'key':entry['index'],'identity':r['id'],'family':entry['family'],
            'context':r['context'],'owner':r['owner'],'scope':canonical(r['scope']),
            'basis':r['basis'],'payload':canonical(r)}


def reference_output(ref):
    return {'owner':ref['owner'],
            'path':[{'index':v} if type(v) is int else {'field':v} for v in ref['path']],
            'target':{'local':ref['target']} if type(ref['target']) is int else {'external':ref['target']},
            'governing':ref['governing'],'domain':ref['domain']}


def expected_runtime(imported, raw_sha):
    result=[]
    for seed in range(len(imported['records'])):
        cert=closure_certificate(imported,[seed])
        boundary=cert['boundary']
        p={'parentIdentity':imported['envelope']['id'], 'parentRawSha256':raw_sha,
           'parentCanonicalSha256':imported['model_sha256'], 'parentEnvelope':canonical(imported['envelope']),
           'seeds':[seed], 'included':cert['included'], 'excluded':cert['excluded'],
           'records':[record_output(r) for r in cert['records']],
           'external':[{'identity':e['external_identity'],'payload':canonical(e)} for e in boundary['external']],
           'ordinary':[reference_output(r) for r in boundary['non_governing_references']],
           'unresolved':[record_output(r) for r in boundary['unresolved_residual_records']],
           'excludedResiduals':[record_output(r) for r in boundary['excluded_residual_records']],
           'invalidation':canonical(boundary['invalidation'])}
        result.append({'budget':cert['required_count'],
                       'underbudgetRefusal':'insufficient record budget; required closure is not truncated',
                       'projection':p})
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'.lake/check')
    args=parser.parse_args()
    outdir=args.output.resolve();outdir.mkdir(parents=True,exist_ok=True)
    lock=json.loads((ROOT/'toolchain-lock.json').read_text())
    archive=lock['lean']['archives'][f'{platform.system()}-{platform.machine()}']['name']
    prefix=ROOT/'.toolchain'/archive.removesuffix('.tar.zst')
    if not (prefix/'bin/lean').exists(): raise RuntimeError('Run python3 scripts/bootstrap.py first')
    env=os.environ|{'PATH':str(prefix/'bin')+os.pathsep+os.environ.get('PATH',''),
                    'MATHLIB_CACHE_DIR':str(ROOT/'.cache/mathlib'),'MATHLIB_NO_CACHE_ON_UPDATE':'1'}
    lake=str(prefix/'bin/lake')
    actual_commit=subprocess.check_output([str(prefix/'bin/lean'),'--githash'],text=True).strip()
    if actual_commit!=lock['lean']['commit']: raise RuntimeError('Compiler pin mismatch')
    manifest=json.loads((ROOT/'lake-manifest.json').read_text())
    for package in manifest['packages']:
        actual=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT/'.lake/packages'/package['name'],text=True).strip()
        if actual!=package['rev']:raise RuntimeError(f'Dependency pin mismatch: {package["name"]}')
    if next(p['rev'] for p in manifest['packages'] if p['name']=='mathlib')!=lock['mathlib']['commit']:
        raise RuntimeError('Mathlib manifest pin mismatch')
    for path in [ROOT/'AC.lean',*(ROOT/'AC').glob('*.lean')]:
        code=code_only(path.read_text())
        if re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b|\bdecide\s*\+native|skipKernelTC\s+true',code):
            raise RuntimeError(f'Prohibited unchecked/admission token in {path}')
    custody=verify_fixture()
    run([sys.executable,'scripts/generate_fixture.py','--check'],'source-import',outdir,env)
    run([sys.executable,'-m','unittest','discover','-s','tests','-p','test_*.py','-v'],'adapter-tests',outdir,env)
    run([lake,'build'],'lake-build',outdir,env)
    audit=run([lake,'env','lean','AC/Audit.lean'],'axiom-audit',outdir,env)
    observed={name:set(a.strip() for a in axioms.split(',') if a.strip())
              for name,axioms in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]",audit)}
    expected={'AC.'+name for name in GENERIC_THEOREMS}|{'AC.Fixture.model_checked'}|{
        f'AC.Fixture.{name}{i}' for i in range(32) for name in ('checked','reachability','success','budget_refusal')}
    expected |= {'AC.Toy.model_checked'} | {
        f'AC.Toy.{name}{i}' for i in range(14) for name in ('checked','reachability','success','budget_refusal')}
    if set(observed)!=expected: raise RuntimeError('Axiom audit theorem coverage mismatch')
    if any(not axioms<=ALLOWED_AXIOMS for axioms in observed.values()): raise RuntimeError('Unexpected proof axiom')
    run([lake,'env','leanchecker','--fresh','AC'],'kernel-replay',outdir,env,timeout=300)
    actual_text=run([lake,'env','lean','--run','AC/Run.lean'],'actual-lean-output',outdir,env)
    actual=json.loads(actual_text)
    imported=import_model(load_checked(FIXTURE_DIR/'MODEL.json'))
    toy=import_model(load_checked(TOY_FIXTURE_DIR/'MODEL.json'))
    expected_output={'stdo302':expected_runtime(imported,RAW_SHA256['MODEL.json']),
                     'toy':expected_runtime(toy,TOY_RAW_SHA256)}
    if actual!=expected_output: raise RuntimeError('Actual Lean output disagrees with independently recovered source/model/projection')
    negative=outdir/'RejectedCertificate.lean'
    negative.write_text('import AC.Fixture\nset_option debug.skipKernelTC false\nexample : AC.checkCertificate AC.Fixture.model.dependencies AC.Fixture.model.localKeys AC.Fixture.seeds0 [] = true := by decide +kernel\n')
    negative_result=subprocess.run([lake,'env','lean',str(negative)],cwd=ROOT,env=env,capture_output=True,text=True,timeout=60)
    negative_log=negative_result.stdout+negative_result.stderr
    (outdir/'rejected-certificate.log').write_text(negative_log)
    if negative_result.returncode==0 or 'error:' not in negative_log or 'false' not in negative_log:
        raise RuntimeError('Kernel did not reject the false truncated closure claim for the expected reason')
    print('tampered-certificate-kernel-rejection: pass',flush=True)
    report={'status':'passed','claim':'bounded mechanical formalisation; no semantic acceptance',
            'lean':lock['lean']['version'],'lean_commit':actual_commit,'mathlib_commit':lock['mathlib']['commit'],
            'fixture':custody,'axiom_checked_theorems':len(observed),'allowed_axioms':sorted(ALLOWED_AXIOMS),
            'kernel_replay':'fresh AC including both fixtures and selected imports',
            'actual_projection_outputs':len(actual['stdo302'])+len(actual['toy']),
            'actual_underbudget_refusals':len(actual['stdo302'])+len(actual['toy']),
            'toy':{'records':len(toy['records']),'references':len(toy['references']),
                   'edges':len(toy['edges']),'model_sha256':toy['model_sha256'],
                   'raw_sha256':TOY_RAW_SHA256},
            'actual_output_sha256':hashlib.sha256(actual_text.encode()).hexdigest(),
            'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in sorted([ROOT/'AC.lean',*(ROOT/'AC').glob('*.lean'),*(ROOT/'scripts').glob('*.py')])}}
    (outdir/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'passed','report':str(outdir/'report.json'),'axiom_checked_theorems':len(observed),
                      'actual_projections':len(actual['stdo302'])+len(actual['toy'])},sort_keys=True))

if __name__=='__main__':
    try:main()
    except (RuntimeError,subprocess.SubprocessError,ValueError,KeyError) as exc:
        print(f'CHECK FAILED: {exc}',file=sys.stderr);raise SystemExit(1)
