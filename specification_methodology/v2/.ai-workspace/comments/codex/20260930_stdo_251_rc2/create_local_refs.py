"""Construct the exact locally qualified RC2 cohort ref set in one compare-and-swap transaction."""
from pathlib import Path
import json
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
load = lambda p: json.loads(p.read_text())

def git(*argv, body=None):
    return subprocess.check_output(['git', *argv], cwd=ROOT, input=body, text=True).strip()

b = git('rev-parse', 'HEAD')
content = load(OUT / 'cohort-content-commit-b.json')
assert content['status'] == 'valid' and not content['failures'] and content['checked_revision'] == b
cohort = json.loads(git('show', b + ':stack_release.json'))
assert cohort['cohort']['version'] == '2.5.1-rc.2'
source = cohort['products']['specification_methodology']
assert git('rev-parse', source['release_ref']) == source['freeze']['tag_object']
assert load(OUT / 'companion-review.json')['status'] == 'satisfied'
tagger = git('var', 'GIT_COMMITTER_IDENT')
changes = []
for name, product in cohort['products'].items():
    commit = source['freeze']['commit'] if name == 'specification_methodology' else b
    refs = [(product['selector_ref'], True), (product['rc_branch'], False), (product['release_branch'], False)]
    if name != 'specification_methodology': refs.insert(0, (product['release_ref'], True))
    for ref, annotated in refs:
        actual = subprocess.run(['git','show-ref','--verify','--hash',ref], cwd=ROOT,capture_output=True,text=True)
        before = actual.stdout.strip() if actual.returncode == 0 else None
        expected = cohort['publication']['expected_remote'][ref]
        assert before == expected, f'Local ref differs from frozen predecessor: {ref}'
        if annotated:
            body = f"object {commit}\ntype commit\ntag {ref.removeprefix('refs/tags/')}\ntagger {tagger}\n\nSTDO 2.5.1 RC2 matched cohort; bounded triage clarification.\n"
            oid = git('mktag', body=body)
        else: oid = commit
        changes.append({'ref':ref,'before':before,'object':oid,'commit':commit,'annotated':annotated})
transaction = 'start\n' + ''.join((f"update {x['ref']} {x['object']} {x['before']}\n" if x['before'] else f"create {x['ref']} {x['object']}\n") for x in changes) + 'prepare\ncommit\n'
result = git('update-ref', '--stdin', body=transaction)
(OUT/'local-ref-construction.json').write_text(json.dumps({'commit_b':b,'changes':changes,'transaction_receipt':result,'published':False},indent=2)+'\n')
print(json.dumps({'commit_b':b,'local_refs':len(changes),'published':False}))
