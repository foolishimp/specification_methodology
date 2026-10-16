"""Inspect selected source/model pairs and cold binding; not semantic acceptance."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

BASE=Path('/tmp/stdo-i4-review-20261015T160637Z')
REL=Path('specification_methodology/v3/build_tenants')
C=BASE/'claude'/REL/'claude'
X=BASE/'codex'/REL/'codex'/'successor'
OUT=BASE/'interpretation-review-checks'
THEORY=Path('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2')
sha=lambda b:hashlib.sha256(b).hexdigest()
account=json.loads((X/'interpretation/source-account.json').read_text())
rows={r['id']:r for r in account['determinations']}
report={'codex_projection_scope':[], 'claude_mapping_shape':{}, 'cold_binding':[]}
for case in ['current-surface-writing','good-prose','evaluate-conjoin','work-recovery']:
    path=OUT/('codex-'+case+'-materialized.json')
    p=json.loads(path.read_text())
    clause_ids=[c['uri'].split(':clause:')[-1] for c in p['clauses']]
    source_bytes=0
    for identifier in clause_ids:
        if identifier not in rows:
            continue
        owner=rows[identifier]['owner']
        body=(X/owner['path']).read_bytes().splitlines(keepends=True)
        source_bytes += sum(map(len,body[owner['start_line']-1:owner['end_line']]))
    report['codex_projection_scope'].append({'case':case,'clause_ids':clause_ids,
        'materialized_bytes':path.stat().st_size,'source_section_byte_sum':source_bytes,
        'boundary':'Inclusive source owner line ranges, summed per selected row; not actual actor acquisition, deduplicated context or an efficiency comparison.'})
p=json.loads((C/'a_c/i3/axiomatic-program.json').read_text())
maps=[c for c in p['clauses'] if c['operator'].endswith(':maps-to')]
for c in maps:
    parts={suffix:[a for a in c['arguments'] if a['role'].endswith(':'+suffix)] for suffix in ['refined-value','predicate','core-value']}
    assert all(len(v)==1 for v in parts.values())
report['claude_mapping_shape']={'maps':len(maps),'each_has_one_value_predicate_and_core':True,
    'limit':'Shape checked on every encoded maps-to relation; complete domain coverage and semantic correctness not established.'}
report['source_model_samples']={identifier:{key:rows[identifier].get(key) for key in ['owner','predicate','applicability','obligations','permissions_exceptions','result_mapping','dependency_relations']}
    for identifier in ['WRITING_GUIDE.good-prose','WRITING_GUIDE.current-surface-writing','TRANSFORMATION_LIBRARY.evaluate','TRANSFORMATION_LIBRARY.conjoin','FOUNDATIONS.workspace-and-context']}
with tempfile.TemporaryDirectory(prefix='i4-review-cold-') as td:
    cold=Path(td)/'package'
    shutil.copytree(X,cold)
    command=[sys.executable,'-B',str(cold/'interpretation/bindings.py'),'--theory-root',str(THEORY)]
    for label in ['unchanged','source-drift']:
        if label=='source-drift':
            member=cold/'standards/WRITING_GUIDE.md'
            member.write_bytes(member.read_bytes()+b'\nReview-only source-drift probe.\n')
        run=subprocess.run(command,capture_output=True,text=True,cwd=Path(td))
        report['cold_binding'].append({'case':label,'argv':command,'exit_code':run.returncode,
            'stdout':run.stdout,'stderr':run.stderr})
    assert report['cold_binding'][0]['exit_code']==0
    assert report['cold_binding'][1]['exit_code']!=0
(OUT/'static-probes.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'claude_mapping_shape':report['claude_mapping_shape'],'cold_binding':report['cold_binding'],
    'codex_projection_scope':report['codex_projection_scope']},indent=2))
