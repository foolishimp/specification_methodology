"""Actual selected RC source materialization and mapped-page readiness."""
from pathlib import Path
import json
import run_observed as o
HERE=Path(__file__).absolute().parent
h=json.loads((HERE/'SELECTED_HANDOFF.json').read_bytes())
b=Path(h['workspace']);native=Path(h['native_root'])
assert h['version']=='3.0.5-rc.1'
argv=[str(b/'manager/bin/python'),'-I','-B',str(native/'standards/tooling/materialize.py'),'materialize','--destination',str(b/'source-tools')]
record,result=o.run('source-materialization',argv,'specification_methodology/v3/build_tenants/common-tools/tooling_materialize.py',inputs=[native/'standards/tooling/TOOLING.json',native/'standards/tooling/sources.zip'])
assert record['execution']['returncode']==0 and result['status']=='materialized' and result['source_files']==243
tooling=json.loads((native/'standards/tooling/TOOLING.json').read_bytes())
root=b/'source-tools';expected={row['archive_path']:row for row in tooling['sources']}
observed={p.relative_to(root).as_posix():p for p in root.rglob('*') if p.is_file()}
assert set(observed)==set(expected)
for name,row in expected.items():
    p=observed[name]
    assert not p.is_symlink() and o.sha(p)==row['sha256'] and p.stat().st_size==row['bytes']
    assert ('100755' if p.stat().st_mode&0o111 else '100644')==row['git_mode']
pages=[root/'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5-rc.1/explorer.html',native/'standards/documentation/index.html',native/'standards/documentation/proofs/index.html']
value={'kind':'stdo.rc-reset.mapped-page-readiness/1','status':'materialized_and_exact_inventory_checked','source_member_count':len(expected),'sources':list(expected.values()),'tooling':o.ref(native/'standards/tooling/TOOLING.json'),'execution':o.ref(HERE/'executions/source-materialization/execution.json'),'pages':[{'path':str(p),'sha256':o.sha(p),'bytes':p.stat().st_size} for p in pages],'scope':'Actual source custody and page readiness; browser, runtime and installed qualification are separate.'}
(HERE/'MATERIALIZATION_CHECK.json').write_bytes(o.encoded(value))
print(json.dumps({'materialization':o.ref(HERE/'MATERIALIZATION_CHECK.json'),'pages':value['pages']}),flush=True)
