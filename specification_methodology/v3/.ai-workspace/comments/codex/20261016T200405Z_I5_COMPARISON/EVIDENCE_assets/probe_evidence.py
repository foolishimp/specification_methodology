#!/usr/bin/env python3
"""Independent frozen-object accounting. No candidate code is executed or written."""
import collections
import hashlib
import json
import re
import subprocess
from pathlib import Path
from acquire import ASSETS, REPO, blob, record

COMMON = '4c340f7adec9f3c893e3e267b23e4cadeb357854'
CODEX = '99f932cfece1a7c9ba6f85c44c47d2403a486aa7'
CLAUDE = '5da6bdec6ca383b4a9c91fe5b45a293aa03d8ff2'
CX = 'specification_methodology/v3/build_tenants/codex/'
CL = 'specification_methodology/v3/build_tenants/claude/'
I5 = CX + 'qualification/C3/iteration-5/'

def sha(data):
    return hashlib.sha256(data.encode() if isinstance(data, str) else data).hexdigest()

def read(commit,path):
    return json.loads(blob(commit,path))

def sections(text):
    # Exact Claude frontier hashing convention, independently applied to Git blobs.
    out, seen, current, buf, code = {}, {}, None, [], False
    for line in text.splitlines(keepends=True):
        if line.startswith('```'): code = not code
        match = None if code else re.match(r'^(#{1,6})\s+(.*)', line)
        if match:
            if current is not None: out[current] = ''.join(buf)
            slug = re.sub(r'[^\w\- ]', '', match.group(2).strip().lower().replace('`','')).replace(' ', '-')
            n = seen.get(slug, 0); seen[slug] = n + 1
            current = slug if n == 0 else f'{slug}-{n}'
            buf = []
        else:
            buf.append(line)
    if current is not None: out[current] = ''.join(buf)
    return out

def main():
    result = {'subjects': {'common':COMMON,'codex':CODEX,'claude':CLAUDE}}
    cx=read(CODEX,I5+'CONSERVATION.json')
    cl=read(CLAUDE,CL+'frontier/REVIEW.json')
    result['codex']={
        'frontier_rows':len(cx['rows']),
        'unique_rows':len({r['id'] for r in cx['rows']}),
        'dispositions':dict(collections.Counter(r['disposition'] for r in cx['rows'])),
        'acceptance':dict(collections.Counter(r['acceptance'] for r in cx['rows'])),
        'current_review':dict(collections.Counter(r['current_review']['standing'] for r in cx['rows'])),
        'changed_carrying_loci_rows':sum(bool(r['current_review']['changed_carrying_loci']) for r in cx['rows'])}
    inventory=read(CODEX,I5+'CANDIDATE.json')
    paths=subprocess.check_output(['git','ls-tree','-r','--name-only',CODEX,CX+'successor/'],cwd=REPO).decode().splitlines()
    expected={m['path'] for m in inventory['members']}
    actual={p[len(CX+'successor/'):] for p in paths}
    mismatches=[]
    for m in inventory['members']:
        raw=subprocess.check_output(['git','show',CODEX+':'+CX+'successor/'+m['path']],cwd=REPO)
        if len(raw)!=m['bytes'] or sha(raw)!=m['sha256']:
            mismatches.append(m['path'])
    result['codex']['package_inventory']={'declared':len(expected),'actual':len(actual),'missing':sorted(expected-actual),'unlisted':sorted(actual-expected),'byte_or_digest_mismatches':mismatches}
    cases=read(CODEX,I5+'CONFORMANCE.json')['rows']
    result['codex']['conformance']={'cases':len(cases),'assessments':dict(collections.Counter(str(r['assessment']) for r in cases))}
    cache={}
    mismatches=[]
    for row in cl['rows']:
        for locus in row['successor_loci']:
            member,anchor=locus['locus'].split('#',1)
            if member not in cache: cache[member]=sections(blob(CLAUDE,CL+'standards/'+member))
            body=cache[member].get(anchor)
            actual_hash=sha(body) if body is not None else None
            if actual_hash != locus['sha256']:
                mismatches.append({'row':row['id'],'locus':locus['locus'],'pinned_sha256':locus['sha256'],'actual_sha256':actual_hash,'semantic_result':row['semantic_review']['result'],'record':row['semantic_review'].get('record')})
    assessed=[r for r in cl['rows'] if r['semantic_review']['result']!='indeterminate']
    result['claude']={
        'review_rows':len(cl['rows']),
        'review_dispositions':dict(collections.Counter(r['disposition'] for r in cl['rows'])),
        'semantic_results':dict(collections.Counter(r['semantic_review']['result'] for r in cl['rows'])),
        'all_rows_pending_ticket':all(r['acceptance']=='ticket_decision_pending' for r in cl['rows']),
        'unresolved_predecessor_anchors':sum(r['predecessor_sha256'] is None for r in cl['rows']),
        'total_locus_occurrences':sum(len(r['successor_loci']) for r in cl['rows']),
        'stale_locus_occurrences':len(mismatches),
        'stale_rows':len({r['row'] for r in mismatches}),
        'stale_assessed_rows':len({r['row'] for r in mismatches if r['semantic_result']!='indeterminate'}),
        'stale_assessed_loci':[r for r in mismatches if r['semantic_result']!='indeterminate'],
        'stale_unassessed_sample':[r for r in mismatches if r['semantic_result']=='indeterminate'][:5],
        'assessment_scope_counts':dict(collections.Counter(r['semantic_review'].get('scope') for r in assessed))}
    output=json.dumps(result,indent=2)+'\n'
    (ASSETS/'probe_evidence.json').write_text(output)
    record('independent frozen object probe',output,{'common':COMMON,'codex':CODEX,'claude':CLAUDE})

if __name__=='__main__': main()
