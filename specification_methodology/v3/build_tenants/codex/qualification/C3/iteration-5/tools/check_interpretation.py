"""Exercise the current native acquisition path and source-bound refusal.

These are author-selected mechanical probes. They are not the shared actual-use
protocol and supply no fresh-actor or whole-source fidelity judgment.
"""
import argparse
import build_interpretation as build
import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
from context import HERE, PACKAGE, INPUTS, encoded, library, read, sha, write


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--theory-root', type=Path, required=True)
    args = parser.parse_args()
    oracle = library('iteration-3/review-repair/interpretation/check_acquisition_policy.py')
    raw = (PACKAGE/'interpretation/source-account.json').read_bytes()
    account = json.loads(raw)
    build.validate_account(account)
    oracle.oracle(account)
    program = read(PACKAGE/'interpretation/program.json')
    expanded, _, _ = build.build_program(account, compact_qualifications=False)
    equivalence = build.qualification_equivalence(program, expanded)
    build.validate_occurrences(program, account['semantic_contracts'])
    refusals = []
    def refuse(name, action):
        try:
            action()
        except (ValueError, KeyError) as error:
            refusals.append({'case': name, 'reason': str(error)})
        else:
            raise ValueError('Unsafe alteration escaped: '+name)
    changed = copy.deepcopy(account)
    row = next(r for r in changed['determinations'] if r['id']=='TRANSFORMATION_LIBRARY.evaluate')
    for relation in row['dependency_relations']:
        if relation['id']=='STDO_REFERENCE_FRAME_BASELINE.derived-reviewer-frame':
            relation.pop('required_when', None)
    refuse('Optional profile promoted to unconditional input', lambda: oracle.oracle(changed))
    changed = copy.deepcopy(account)
    row = next(r for r in changed['determinations'] if r['id']=='WRITING_GUIDE.good-prose')
    row['result_mapping']['owner_refs'] = []
    refuse('Material result owner omitted', lambda: oracle.oracle(changed))
    for name, alteration in [('Broken qualification pointer', lambda r: r['qualification_ref'].update(pointer='/not-present')),
                             ('Changed qualification condition', lambda r: r.update(required_when='unconditional permission')),
                             ('Changed acquisition classification', lambda r: r.update(acquisition='required'))]:
        damaged = copy.deepcopy(program)
        route = next(a for c in damaged['clauses'] for a in c['arguments']
                     if a['role'] == build.VOCAB + 'acquisition-route' and 'qualification_ref' in json.loads(a['literal']))
        value = json.loads(route['literal']); alteration(value); route['literal'] = build.text(value)
        refuse(name, lambda: build.qualification_equivalence(damaged, expanded))
    odd = next(r for r in account['determinations'] if r['id']=='ODD_METHOD.118-cumulative-environment-law-is-mandatory')
    if odd['result_mapping']['bound_predicate'] != odd['predicate']:
        raise ValueError('ODD predicate/result binding differs')
    cases = {
        'evaluate-conjoin': ['TRANSFORMATION_LIBRARY.evaluate','TRANSFORMATION_LIBRARY.conjoin'],
        'good-prose': ['WRITING_GUIDE.good-prose'],
        'work-recovery': ['TRANSFORMATION_LIBRARY.workrecovery-specialization'],
    }
    for identifier in ('construction-assurance', 'preservation-obligations', 'assertions-and-observations',
                       'parallel-assurance-and-provenance', 'risk-and-assurance-selection',
                       'change-impact-and-evidence-retention'):
        key = 'FOUNDATIONS.' + identifier
        if key not in {r['id'] for r in account['determinations']}:
            raise ValueError('Required I5 owner is absent: ' + key)
        cases[identifier] = [key]
    observations=[]
    with tempfile.TemporaryDirectory(prefix='codex-i5-native-') as temporary:
        root=Path(temporary)
        bindings=root/'bindings.json'
        invocation=[sys.executable,'-B',str(PACKAGE/'interpretation/bindings.py'),
                    '--theory-root',str(args.theory_root.resolve())]
        run=subprocess.run(invocation,capture_output=True)
        if run.returncode:
            raise RuntimeError(run.stderr.decode())
        bindings.write_bytes(run.stdout)
        for name, identifiers in cases.items():
            for mode in ('reference-only','materialized'):
                output=root/(name+'-'+mode+'.json')
                command=[sys.executable,'-B',str(build.TOOL),'project',
                    '--program',str(PACKAGE/'interpretation/program.json'),
                    '--map',str(PACKAGE/'interpretation/map.json'),
                    '--bindings',str(bindings),'--mode',mode,'--output',str(output)]
                for identifier in identifiers:
                    command += ['--frame-index',build.NS+'index:'+identifier]
                started=time.monotonic()
                projected=subprocess.run(command,capture_output=True,text=True)
                if projected.returncode:
                    raise RuntimeError(projected.stdout+projected.stderr)
                value=output.read_bytes()
                parsed=json.loads(value)
                observations.append({'case':name,'mode':mode,'bytes':len(value),
                    'sha256':sha(value),'elapsed_seconds':time.monotonic()-started,
                    'top_level_fields':sorted(parsed),'exit_code':projected.returncode})
        cold=root/'cold'
        shutil.copytree(PACKAGE,cold)
        cold_command=[sys.executable,'-B',str(cold/'interpretation/bindings.py'),
                      '--theory-root',str(args.theory_root.resolve())]
        good=subprocess.run(cold_command,capture_output=True,text=True)
        if good.returncode:
            raise RuntimeError('Cold package binding failed: '+good.stderr)
        path=cold/'standards/ODD_METHOD.md'
        path.write_bytes(path.read_bytes()+b'\nChanged source without a successor pin.\n')
        bad=subprocess.run(cold_command,capture_output=True,text=True)
        if bad.returncode==0:
            raise ValueError('Changed source passed native bindings')
        refusals.append({'case':'Source changed behind frozen documentary inventory',
                         'exit_code':bad.returncode,'reason':bad.stderr.strip()})
    paired=subprocess.run([sys.executable,'-B',str(HERE/'tools/source_pair.py'),
                          '--id',odd['id']],capture_output=True)
    if paired.returncode:
        raise RuntimeError(paired.stderr.decode())
    pair=json.loads(paired.stdout)
    if sha(pair['source_utf8'].encode())!=odd['owner']['body_sha256']:
        raise ValueError('Paired source body changed')
    result={'valid':True,'source_commit':read(PACKAGE/'interpretation/SOURCE_INVENTORY.json')['document_source_input_commit'],
        'common_input':INPUTS['common_input'],'semantic_account_sha256':sha(raw),
        'program_sha256':sha((PACKAGE/'interpretation/program.json').read_bytes()),
        'map_sha256':sha((PACKAGE/'interpretation/map.json').read_bytes()),
        'checker_sha256':sha(Path(__file__).read_bytes()),
        'acquisition_oracle_sha256':INPUTS['libraries']['iteration-3/review-repair/interpretation/check_acquisition_policy.py'],
        'native_projections':observations,'negative_controls':refusals,
        'qualification_equivalence':equivalence, 'compiler_sha256':sha(Path(build.__file__).read_bytes()),
        'cold_binding':'passed','paired_source':{'id':odd['id'],'body_sha256':odd['owner']['body_sha256']},
        'limits':['Authored mechanical checks, not shared trials or semantic acceptance.',
                  'Projection bytes are emitted artifact sizes, not retained actor context or efficiency gains.']}
    write(HERE/'interpretation/NATIVE_CHECK.json',result)
    print({'valid':True,'projections':len(observations),'negative_controls':len(refusals)})


if __name__=='__main__':
    main()
