"""Freeze bounded source-first review inputs and execute fresh nonauthor checks."""
from pathlib import Path
import argparse, concurrent.futures, json, subprocess, sys

q = Path(__file__).resolve().parent
tenant = q.parents[2]
repo = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=tenant, text=True).strip())
product = tenant / 'successor'
prefix = str(product.relative_to(repo))
parser = argparse.ArgumentParser()
parser.add_argument('--run', action='store_true')
parser.add_argument('--after', default='5b4aebb')
parser.add_argument('--label', default='final')
args = parser.parse_args()
cut = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip()
common = (tenant.parents[1] / 'specification/requirements/README.md').read_text()
foundations = (product / 'standards/FOUNDATIONS.md').read_text()
core = foundations[foundations.index('## Result algebra'):]
groups = {
    'work': ['standards/SPEC_METHOD.md', 'standards/TICKET_METHOD.md', 'standards/RELEASE_METHOD.md'],
    'frames': ['standards/REFERENCE_FRAME_METHOD.md', 'standards/STDO_REFERENCE_FRAME_BASELINE.md'],
    'formal': ['standards/AXIOMATIC_CALCULUS.md', 'standards/DESIGN_MODULE_METHOD.md', 'standards/TRAVERSAL_OCCURRENCE_PROFILE.md'],
    'profiles': ['standards/ODD_METHOD.md', 'standards/WORLD_MODEL_METHOD.md', 'standards/UX_METHOD.md', 'standards/IDENTITY_METHOD.md'],
    'entry': ['README.md', 'standards/README.md', 'standards/GLOSSARY_GUIDE.md', 'standards/POSTING_GUIDE.md', 'standards/WRITING_GUIDE.md', 'plugins', 'templates', 'compressions'],
}
jobs = []
for name, members in groups.items():
    diff = subprocess.check_output(['git', 'diff', '--unified=15', args.after, cut, '--', *[prefix + '/' + m for m in members]], cwd=repo, text=True)
    prompt = '''Independent source-first integration review. You did not author these changes. Read common requirements and the core before the consumer source changes. Seek concrete contradictions, lost predecessor obligations, wrong result maps, authority or recovery defects at actual producer-consumer joins. Report counterexamples, exact headings and the smallest repair. Do not add optional mechanisms or style preferences. A refinement may keep its domain choices. Changes and 15 lines of boundary context are provided, not complete omitted bodies: disclose that coverage. This is a working source check, not per-member acceptance or approval of the source-port review policy. No tools or source changes.\n'''
    prompt += '\nCANDIDATE ' + cut + '; OWN PREIMAGE ' + args.after + '\nCOMMON\n' + common + '\nCORE\n' + core + '\nSOURCE DIFF\n' + diff
    path = q / 'prompts' / (args.label+'-integration-' + name + '.txt')
    if len(prompt.encode()) > 120000:
        raise ValueError((name, len(prompt.encode())))
    path.write_text(prompt)
    jobs.append((name, path, q / 'runs' / (args.label+'-integration-' + name)))

prompt = '''Independent source-first re-review of the repaired shared core. You did not author it. Judge concrete material counterexamples against the common requirements; no style requests or universal new mechanisms. In particular exercise: aborted suite with authenticated failure; no concluded procedure and independently observed invalid basis; deployment then rollback then reapplication on the same effect part; an absent dispatched effect; complete irreversible external effects alongside local rollback; unknown or conflicting supersession; OR/negation with known failed joins; overlapping/incomplete operator declarations; admission relation versus evaluated join. Verify the conditions on the associativity claim. Report any remaining contradiction and its minimal counterexample, or state the bounded checks that hold. Source-port acceptance and complete-corpus acceptance are separate.\n'''
prompt += '\nCANDIDATE ' + cut + '\nCOMMON\n' + common + '\nFOUNDATIONS\n' + foundations + '\nLIBRARY\n' + (product / 'standards/TRANSFORMATION_LIBRARY.md').read_text()
path = q / 'prompts' / (args.label+'-core.txt')
if len(prompt.encode()) > 120000:
    raise ValueError(('core', len(prompt.encode())))
path.write_text(prompt)
jobs.append(('core', path, q / 'runs' / (args.label+'-core')))
for name, path, _ in jobs:
    print(json.dumps({'review': name, 'input_bytes': path.stat().st_size, 'cut': cut}), flush=True)
if args.run:
    def run(job):
        name, path, destination = job
        proc = subprocess.run([sys.executable, str(q / 'run_actor.py'), str(path), str(destination)], capture_output=True, text=True)
        result = {'review': name, 'host_exit': proc.returncode, 'summary': proc.stdout.strip(), 'stderr': proc.stderr}
        print(json.dumps(result), flush=True)
        return result
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(run, jobs))
    (q / (args.label.upper()+'_INTEGRATION_EXECUTION.json')).write_text(json.dumps(results, indent=2) + '\n')
    raise SystemExit(0 if all(r['host_exit'] == 0 for r in results) else 1)
