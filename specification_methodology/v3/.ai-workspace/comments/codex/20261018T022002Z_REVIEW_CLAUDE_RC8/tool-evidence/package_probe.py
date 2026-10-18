"""Independently verify RC8 local package identity, then reproduce its builder.

No installer, remote query, Git mutation, adoption or release operation occurs.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import jsonschema

REPO=Path('/Users/jim/src/apps/specification_methodology')
EVIDENCE=Path(__file__).resolve().parent
A='9aee01ffa76cfbde1a6b8f1153a25bd6d71c216e'
B='1db13bfeb0675fc95de04aceccb214f5b76873fc'
TAG='08555a3b6f09df0a0297e59932dc7b6a967582bd'
PREFIX='specification_methodology/v3/build_tenants/claude/'
mechanical_bytes=0

def git(*args):
    return subprocess.check_output(['git','-C',str(REPO),*args])

def blob(path,commit=A):
    global mechanical_bytes
    b=git('show',commit+':'+PREFIX+path)
    mechanical_bytes+=len(b)
    return b

def sha(b): return hashlib.sha256(b).hexdigest()

mb=blob('release/manifest.json',B)
m=json.loads(mb);r=m['release']
assert r['cut']=='v3.0.0-rc.8'
assert r['commit']==A and r['tag_object']==TAG
assert r['project_release_namespace']=='specification_methodology-claude'
assert r['project_subtree_root']==PREFIX.rstrip('/')
assert r['qualified_ref']=='refs/tags/specification_methodology-claude/v3.0.0-rc.8'
assert git('cat-file','-t',TAG).decode().strip()=='tag'
assert git('rev-parse',r['qualified_ref']).decode().strip()==TAG
assert git('rev-parse',TAG+'^{}').decode().strip()==A
tag=git('cat-file','-p',TAG).decode()
assert '\ntag '+r['qualified_ref'].removeprefix('refs/tags/')+'\n' in tag
for key,ref in [('tree',A+'^{tree}'),('standards_tree',A+':'+PREFIX+'standards'),
                ('project_subtree_tree',A+':'+PREFIX.rstrip('/'))]:
    assert r[key]==git('rev-parse',ref).decode().strip()
assert git('merge-base','--is-ancestor',A,B)==b''
assert git('rev-parse',B+'^').decode().strip()==A
changed=git('diff','--name-only',A,B,'--',PREFIX).decode().splitlines()
assert not git('diff','--name-only',A,B,'--',*[PREFIX+p for p in ('standards','plugins','a_c','LICENSE','release/release-note.md','release/build_manifest.py')])
groups={}
member_records=[]
for label,group,root in [('standards',m['standards'],'standards'),('plugin',m['auxiliary']['plugin'],'plugins/spec')]:
    members=group['members']
    names=[x['path'] for x in members]
    tree_names=git('ls-tree','-r','--name-only',A,'--',PREFIX+root).decode().splitlines()
    expected=[p.removeprefix(PREFIX+root+'/') for p in tree_names]
    assert len(names)==group['member_count'] and len(names)==len(set(names))
    assert names==sorted(expected)
    assert all(not n.startswith('/') and '..' not in Path(n).parts for n in names)
    for entry in members:
        data=blob(root+'/'+entry['path'])
        assert sha(data)==entry['sha256']
        member_records.append({'path':root+'/'+entry['path'],'sha256':entry['sha256'],'bytes':len(data)})
    groups[label]={'members':len(members),'bytes':sum(x['bytes'] for x in member_records if x['path'].startswith(root+'/'))}
aggregate=sha(''.join(x['sha256']+'  '+x['path']+'\n' for x in m['standards']['members']).encode())
assert aggregate==m['standards']['member_set_sha256']
assert sha(blob('LICENSE'))==m['auxiliary']['license']['sha256']
assert sha(blob('release/release-note.md'))==m['auxiliary']['release_note']['sha256']
schema=json.loads(blob('standards/schemas/installed-release-manifest.schema.json'))
jsonschema.validators.validator_for(schema)(schema).validate(m)
plugin_versions={p:json.loads(blob('plugins/spec/'+p))['version'] for p in ['.claude-plugin/plugin.json','.codex-plugin/plugin.json']}
assert set(plugin_versions.values())=={'3.0.0-rc.8'}
scratch=Path(tempfile.mkdtemp(prefix='stdo-rc8-manifest-',dir='/private/tmp'))
(scratch/'release').mkdir()
script=scratch/'release/build_manifest.py';script.write_bytes(blob('release/build_manifest.py'))
cmd=[sys.executable,'-I',str(script),A,TAG]
run=subprocess.run(cmd,cwd=scratch,env=dict(os.environ,GIT_DIR=str(REPO/'.git'),PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True)
rebuilt=(scratch/'release/manifest.json').read_bytes() if run.returncode==0 else b''
assert run.returncode==0 and rebuilt==mb
(EVIDENCE/'manifest-reproduced.json').write_bytes(rebuilt)
receipt={'source_A':A,'records_B':B,'tag_object':TAG,'manifest_sha256':sha(mb),
         'manifest_release':r,'direct_A_parent_of_B':True,'tag_peels_to_A':True,
         'local_qualified_ref_matches_tag_object':True,'tag_annotation':tag,
         'A_to_B_changed_paths':changed,'package_and_interpretation_A_to_B':'byte-identical',
         'membership':groups,'standards_member_set_sha256':aggregate,
         'manifest_schema_valid':True,'plugin_versions':plugin_versions,
         'builder_command':cmd,'builder_exit':run.returncode,'builder_stdout':run.stdout,
         'builder_stderr':run.stderr,'builder_reproduces_B_manifest_bytes':rebuilt==mb,
         'scratch':str(scratch),'mechanically_acquired_blob_bytes':mechanical_bytes,
         'member_evidence':member_records,'external_paid_calls':0,
         'limits':['Local tag identity only; no remote-publication verification or publication claim.',
                   'Membership and hashes do not establish semantic completeness, acceptance or qualification.',
                   'No native installation or activated consumer was exercised.']}
(EVIDENCE/'package-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in ('member_evidence','tag_annotation','A_to_B_changed_paths','builder_command')},indent=2))
