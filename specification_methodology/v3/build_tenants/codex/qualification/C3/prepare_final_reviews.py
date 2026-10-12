"""Assemble exact frozen source-first reviewer inputs in this tenant only."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

base = Path(__file__).resolve().parents[2]
checkout = base.parents[3]
commit = subprocess.check_output(['git', 'rev-parse', '804b396'], cwd=checkout, text=True).strip()
installed = Path('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2')
records = {}


def pinned(label, data):
    return '\n'+label+' full_sha256 '+hashlib.sha256(data).hexdigest()+'\n'+data.decode()


def candidate(path):
    rel = (base/'successor'/path).relative_to(checkout)
    data = subprocess.check_output(['git', 'show', commit+':'+str(rel)], cwd=checkout)
    records[str(rel)] = {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}
    return pinned('CANDIDATE '+path, data)


def owner(name):
    return pinned('SOURCE OWNER '+name, (installed/'standards'/name).read_bytes())


def owner_sections(name, needles):
    data = (installed/'standards'/name).read_bytes()
    text = data.decode()
    headings = list(re.finditer(r'^#{1,6} .+$', text, re.M))
    selected = []
    for i, heading in enumerate(headings):
        if not any(needle in heading[0].lower() for needle in needles):
            continue
        level = len(heading[0].split()[0])
        end = next((h.start() for h in headings[i+1:] if len(h[0].split()[0]) <= level), len(text))
        selected.append(text[heading.start():end])
    if len(selected) != len(needles):
        raise ValueError('Missing/ambiguous owner section '+name)
    return '\nEXACT SELECTED SOURCE '+name+' full_member_sha256 '+hashlib.sha256(data).hexdigest()+'\n'+'\n'.join(selected)


def intro(name):
    text = candidate('standards/'+name).split('\n', 2)[2]
    if '<!-- STDO3_PROFILE_BINDING_START -->' in text:
        text = text.split('<!-- STDO3_PROFILE_BINDING_START -->', 1)[1].split('<!-- STDO3_PROFILE_BINDING_END -->', 1)[0]
    elif name == 'REFERENCE_FRAME_METHOD.md':
        text = text[text.index('The [foundations]'):text.index('This is an engagement meta-method.')]
    elif name == 'AXIOMATIC_CALCULUS.md':
        text = text[text.index('The [foundations]'):text.index('Its stable concept identity')]
    elif name == 'SPEC_METHOD.md':
        text = text.split('## Canonical Compression', 1)[0]
    return '\nCANDIDATE EXPLANATORY INTRO '+name+'\n'+text


common = '''You are a fresh author-independent Reviewer. Use only supplied source and candidate bytes. No tools, peer tenant, filesystem or mutation. Frozen subject commit: '''+commit+'''. Host Writer resolved Git bytes and computed the supplied full-member SHA256; retain your inability to reacquire/hash. No acceptance/disposition grant. Return source-linked RF results and literal counterexamples for the selected predicates. Distinguish owning obligations, non-deciding correspondence and unsupported wider claims. Assessor labels are evidence, not owner disposition.\n'''


def save(relative, prompt):
    target = base/'qualification/C3'/relative
    target.mkdir(parents=True, exist_ok=False)
    data = (prompt.rstrip()+'\n').encode()
    if len(data) > 600000:
        raise ValueError('Context envelope exceeded')
    (target/'PROMPT.txt').write_bytes(data)
    print(relative, len(data), 'bytes')


prompt = common+'''Selected predicate: introduced explanation conserves owner dependencies, scopes, result/decision algebras, source standing, ownership and authority without a rival universal signature or hierarchy. Mathematical equivalence, empirical adequacy and release are out of scope. SOURCE FIRST.\n'''
for name in ['SPEC_METHOD.md', 'REFERENCE_FRAME_METHOD.md', 'AXIOMATIC_CALCULUS.md', 'ODD_METHOD.md']:
    prompt += owner(name)
prompt += owner_sections('DESIGN_MODULE_METHOD.md', ['bounded frame conservation'])
prompt += owner_sections('STDO_REFERENCE_FRAME_BASELINE.md', ['status and authority boundary', 'complete engagement transition'])
for name in ['FOUNDATIONS.md', 'TRANSFORMATION_LIBRARY.md', 'README.md']:
    prompt += candidate('standards/'+name)
for name in ['SPEC_METHOD.md', 'AXIOMATIC_CALCULUS.md', 'REFERENCE_FRAME_METHOD.md', 'ODD_METHOD.md', 'WORLD_MODEL_METHOD.md', 'UX_METHOD.md']:
    prompt += intro(name)
save('reviews/owner-conservation-closed', prompt)

prompt = common+'''Selected predicate: existing manifest namespaces, source-to-installed distribution, full bootstrap/aggregate routing, digest discovery, historical-label standing in plugin-only use, exact-coordinate guide and view discovery. Full files below are full bytes. Tenant source needs future canonical materialization; no actual marketplace, native host or v3 cohort qualification is supplied. Separate that release residual from artifact fidelity.\n'''
for name in ['standards/README.md', 'standards/FOUNDATIONS.md', 'standards/TRANSFORMATION_LIBRARY.md', 'standards/schemas/installed-release-manifest.schema.json', 'standards/authority_compressions/README.md', 'standards/authority_compressions/stdo_bootstrap.md', 'standards/authority_compressions/stdo_compressed.md', 'plugins/spec/references/GETTING_STARTED.md', 'plugins/spec/references/REFRESH.md', 'plugins/spec/references/provenance/README.md', 'plugins/spec/references/provenance/predecessor-release-note.txt', 'plugins/spec/claude-skills/refresh/SKILL.md', 'plugins/spec/.claude-plugin/plugin.json', 'plugins/spec/.codex-plugin/plugin.json', 'release/release-note.md']:
    prompt += candidate(name)
for name in ['WORK_RECOVERY', 'EVALUATION_CONJUNCTION', 'CONSTITUTIONAL_DERIVATION', 'DOMAIN_BINDING', 'RELEASE_ADOPTION']:
    prompt += candidate('standards/frames/'+name+'.md')
save('reviews/distribution-closed', prompt)

prompt = common+'''Selected predicate: finite/qualitative SOURCE fidelity, complete indexes/closure, missing and unauthenticated slot exceptions, explicit encoding latitude, executable/model correspondence and receipt binding. Alpha is permission-mutant; Beta intended-faithful; judge independently. Separately judge the matching label-permission executable mutant and token scope. Structural and finite success supplies no wider claim.\n'''
for name in ['SOURCE.md', 'ENCODING.md', 'program.json', 'program-mutant.json', 'finite_check.py', 'qualify.py', 'FINITE_RESULT.json', 'MECHANICAL_RESULT.json']:
    relative = (base/'qualification/C3/a_c'/name).relative_to(checkout)
    data = subprocess.check_output(['git', 'show', commit+':'+str(relative)], cwd=checkout)
    prompt += pinned('FROZEN MODEL MEMBER '+name, data)
prompt += candidate('standards/TRANSFORMATION_LIBRARY.md')+candidate('standards/FOUNDATIONS.md')
save('a_c/closed', prompt)
(base/'qualification/C3/REVIEW_DISPATCH_PINS.json').write_text(json.dumps({
    'subject_commit': commit, 'members': records,
    'transport': 'Frozen git-show bytes; tool-free reviewers cannot reacquire/hash',
    'standing': 'Acquisition evidence, not acceptance'
}, indent=2)+'\n')
