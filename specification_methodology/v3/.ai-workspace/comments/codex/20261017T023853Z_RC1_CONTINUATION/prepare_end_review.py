#!/usr/bin/env python3
"""Prepare exact read-only inputs for one consolidated working review."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--package', required=True)
p.add_argument('--evidence', required=True)
a = p.parse_args()
s = json.loads(Path('/tmp/stdo_rc1_current.json').read_text())
repo, out = Path(s['root']), Path(s['out'])
base = Path('/tmp') / ('stdo-rc1-end-review-' + a.package[:10])
base.mkdir(exist_ok=False)
prefix = 'specification_methodology/v3/build_tenants/codex/'
inputs = []

def export(revision, prefix, dest):
    names = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', revision, '--', prefix], cwd=repo, text=True).splitlines()
    for name in names:
        target = dest / name[len(prefix):].lstrip('/')
        b = subprocess.check_output(['git', 'show', revision + ':' + name], cwd=repo)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b)
        inputs.append({'path': str(target.relative_to(base)), 'commit': revision, 'source_path': name, 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()})

export(s['common'], 'specification_methodology/v3/specification/', base / 'basis')
export(a.package, prefix + 'successor/', base / 'candidate')
for part in ('iteration-5', 'rc1'):
    export(a.evidence, prefix + 'qualification/C3/' + part + '/', base / 'evidence' / part)
installed = Path('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2')
for path in sorted((installed / 'standards').rglob('*')):
    if path.is_file():
        b = path.read_bytes()
        rel = path.relative_to(installed)
        target = base / 'predecessor' / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b)
        inputs.append({'path': str(target.relative_to(base)), 'source': 'installed:' + str(rel), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()})

account = json.loads((base / 'evidence/rc1/integration/DETERMINATIONS.json').read_text())
view = base / 'account-by-owner'
view.mkdir()
groups = {}
for row in account['determinations']:
    groups.setdefault(row['owner']['path'], []).append(row)
for owner, rows in groups.items():
    (view / (owner.replace('/', '__') + '.json')).write_text(json.dumps({'owner': owner, 'standing': 'Exact authored rows, not a judgment; raw source governs', 'rows': rows}, indent=2) + '\n')
conservation = json.loads((base / 'evidence/iteration-5/CONSERVATION.json').read_text())
view = base / 'conservation-by-source'
view.mkdir()
groups = {}
for row in conservation['rows']:
    groups.setdefault(row['source_member'], []).append(row)
for owner, rows in groups.items():
    (view / (owner.replace('/', '__') + '.json')).write_text(json.dumps(rows, indent=2) + '\n')

closed = base / 'prior-closed-reviews'
closed.mkdir()
for name in ('20261016T154154Z_I5_CORE_REVIEW.md', '20261016T160600Z_I5_DERIVED_REVIEW.md', '20261016T161900Z_I5_CONSERVATION_REVIEW.md'):
    source = 'specification_methodology/v3/.ai-workspace/comments/codex/' + name
    b = subprocess.check_output(['git', 'show', s['consumer_disposition_commit'] + ':' + source], cwd=repo)
    (closed / name).write_bytes(b)

scopes = {
    'SOURCE': 'Primary members: FOUNDATIONS, AXIOMATIC_CALCULUS, TRANSFORMATION_LIBRARY, REFERENCE_FRAME_METHOD, SPEC_METHOD, TICKET_METHOD, DESIGN_MODULE_METHOD, IDENTITY_METHOD, RELEASE_METHOD. Assess current shared law and material deciding paths, generic human/software/mixed assessment, preservation/assurance/diagnosis/recovery, and predecessor conservation/replacement claims. Acquire mandatory dependencies across members; read current source before its author account. Compare required/permitted/prohibited choices and exceptions. Distinguish proposed replacement from accepted replacement. Group equivalent claims only with a shared argument and exact membership.',
    'DOMAIN': 'Primary members: STDO_REFERENCE_FRAME_BASELINE, ODD_METHOD, WORLD_MODEL_METHOD, TRAVERSAL_OCCURRENCE_PROFILE, UX_METHOD, GLOSSARY_GUIDE, WRITING_GUIDE, POSTING_GUIDE, standards README, templates and schemas. Acquire shared Foundations and other owners as necessary. Assess current decisions, exceptions, executor/profile optionality, result/composition semantics and predecessor conservation. This is the source/domain partition of one review. Identify actual member and predecessor-row coverage.',
    'REPRESENTATION': 'Primary members: interpretation, compressions, seven frames, root entries and all plugin carriers. Assess source-to-account-to-view fidelity and ordinary acquisition. Read raw source owners first. Generated JSON is large: use exact owner groups in account-by-owner and targeted searches. Focus first on changed generic assessment and five conditional procedure dependencies, preserved optionality, citations, provenance versus operative dependencies, and current qualification/entry coordinates. Assess broader fidelity risks explicitly. Native generation/checks support only mechanical claims; do not run the old full sweep. Distinguish release preparation and the review archive from selected/tagged/released acceptance.'
}
for name, scope in scopes.items():
    prompt = f'''You are a fresh nonauthor cross-family working Reviewer of the completed Codex STDO v3 document product. Read/Glob/Grep only; no mutation, shell, Git, repair, external calls or subagents. Read only this scratch directory. Candidate: {a.package}; common: {s['common']}; predecessor: installed v2.5.1-rc.2. Do not assume software-only realization or mandatory optional profiles.

FIRST, before opening candidate/account/conservation/evidence/prior-review material: read basis/INTENT.md, basis/PRODUCT.md, basis/requirements/README.md, basis/conformance/README.md and applicable requirement and predecessor source (predecessor/standards/). Derive concrete expectations independently, then output an EXPECTATIONS message. It must precede any candidate opening in the durable ordered stream.

SECOND: {scope}

Read complete relevant sections and conditions; page through Read limits or disclose unread ranges. account-by-owner and conservation-by-source contain exact frozen author claims, not proof. Source first; only then use prior-closed-reviews/ for justified retention of exact unchanged predicates. Do not repeat supported tests because a hash changed. Current changed scope: generic assessment, five carrier dependencies, inverse consumer metadata. evidence/rc1/ contains the construction receipts. Eleven unmatched positive consumer relations remain unresolved. Empty consumer fields alone are not source defects. This review is not the shared held actual-use trial, which remains unperformed.

Return FINAL REVIEW: scoped candidate-readiness judgment; confirmed defects with severity, file/line, trigger, consequence and smallest owner repair; disputed claims separately; exact coverage/unassessed scope; justified reuse; contributions to the six criteria (disposition completeness, conservation, accepted replacements, actual use/context fit, fidelity/conformance, governing reduction); resource limits. Never mark unread scope satisfied. No winner, acceptance, release or universal proof follows. Seek material counterexamples, not stylistic preferences. Whole completeness requires actual complete coverage.

Local allowances: USD6, 45 minutes. Relevant source is available; report acquisition actually performed. Provider context capacity and per-request input/cache plus whole-call output are captured by the parent. Do not claim unmeasured context fit. On exhaustion return retained work and remainder, without a restart. Elapsed/usage fields unavailable to you should say unavailable; parent joins measured values. Be detailed enough to make findings actionable.
'''
    (base / (name + '_PROMPT.txt')).write_text(prompt)
receipt = {'candidate_commit': a.package, 'evidence_commit': a.evidence, 'common_commit': s['common'], 'predecessor_manifest_sha256': '3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782', 'scratch': str(base), 'scopes': scopes, 'inputs': inputs}
(out / 'END_REVIEW_INPUTS.json').write_text(json.dumps(receipt, indent=2) + '\n')
s['review_scratch'], s['review_package_commit'] = str(base), a.package
Path('/tmp/stdo_rc1_current.json').write_text(json.dumps(s, indent=2) + '\n')
print(json.dumps({'scratch': str(base), 'members': len(inputs), 'candidate': a.package}))
