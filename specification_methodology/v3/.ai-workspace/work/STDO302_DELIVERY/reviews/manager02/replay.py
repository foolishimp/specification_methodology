"""Bounded installed-wheel and source CLI review; no release refs are created."""
from pathlib import Path
from unittest.mock import patch
import hashlib
import importlib.metadata
import json
import os
import subprocess
import sys
import tempfile
import zipfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[6]
WORK=ROOT/'specification_methodology/v3/.ai-workspace/work/STDO302_DELIVERY/manager'
FREEZE='e3c5302012ac9cfdc2413096976a9ba2ae49e408b0d01f47320edd21ae1fd50d'
raw=(WORK/'CANDIDATE-repair1.json').read_bytes();assert hashlib.sha256(raw).hexdigest()==FREEZE
index=json.loads(raw);assert all(hashlib.sha256((ROOT/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in index['files'])
package=json.loads((WORK/'package-03/PACKAGE.json').read_text());wheel=ROOT/package['wheel']['path']
assert hashlib.sha256(wheel.read_bytes()).hexdigest()=='ef726f780220a4be93c8ce014e2838d140851ec0e3d47902ea2ddd36a26c3242'
import stdo_toolchain
from stdo_toolchain import git_source as g
from stdo_toolchain.errors import StdoError
assert 'site-packages' in Path(stdo_toolchain.__file__).parts
assert stdo_toolchain.__version__==importlib.metadata.version('stdo-toolchain')=='0.1.6'
checked=[]
with zipfile.ZipFile(wheel) as z:
    for x in index['files']:
        prefix='specification_methodology/v2/src/'
        if x['path'].startswith(prefix):
            name=x['path'].removeprefix(prefix);data=z.read(name)
            assert hashlib.sha256(data).hexdigest()==x['sha256']
            assert (Path(stdo_toolchain.__file__).parent/name.removeprefix('stdo_toolchain/')).read_bytes()==data
            checked.append(name)
record={'freeze_sha256':FREEZE,'wheel_sha256':package['wheel']['sha256'],'runtime_python':sys.executable,
        'import':stdo_toolchain.__file__,'version':stdo_toolchain.__version__,'wheel_source_installed_members':checked,'cases':[]}

def refused(name,fn):
    try:fn()
    except StdoError as error:record['cases'].append({'case':name,'result':'refused','reason':str(error)})
    else:raise AssertionError('unexpected acceptance: '+name)

for invalid in ['v03.0.2','v3.0','v3.0.2+build','v3.0.2-beta']:
    refused('nonstable syntax '+invalid,lambda value=invalid:g.normalize_cut(value))
assert g.normalize_cut('v3.0.2')=='v3.0.2' and g.cut_coordinates('v3.0.2')==('3.0.2',None)
refused('same-line stable-to-RC channel regression',lambda:g.ensure_channel_not_downgrade('v3.0.2','v3.0.2-rc.1'))
TAG='refs/tags/specification_methodology/v3.0.2';OID='1'*40;COMMIT='2'*40
refs={TAG:OID,TAG+'^{}':COMMIT}
with patch.object(g,'_remote_tag_refs',return_value=refs):assert g._resolve_stable_ref('synthetic','v3.0.2')==TAG
for collision in ['refs/tags/v3.0.2','refs/tags/specification_methodology/v3.0.2-rc.1']:
    with patch.object(g,'_remote_tag_refs',return_value={**refs,collision:'3'*40}):
        refused('stable fresh-line collision '+collision,lambda:g._resolve_stable_ref('synthetic','v3.0.2'))

def snapshot_probe(message,kind='commit',tag='specification_methodology/v3.0.2'):
    annotation='object '+COMMIT+'\ntype '+kind+'\ntag '+tag+'\ntagger fixture\n\n'+message+'\n'
    def text(self,args):
        if args==['cat-file','-t',TAG]:return 'tag'
        if args==['cat-file','tag',OID]:return annotation
        if args==['rev-parse',TAG]:return OID
        if args==['rev-parse',TAG+'^{commit}']:return COMMIT
        if args[0]=='rev-parse':return '4'*40
        raise AssertionError(args)
    remote=''.join(oid+'\t'+ref+'\n' for ref,oid in refs.items())
    def transport(args,**kwargs):
        if args[0]=='ls-remote':return remote
        return ''  # No Git invocation: synthetic object-observation boundary.
    with patch.object(g,'_remote_tag_refs',return_value=refs),patch.object(g,'_git',side_effect=transport), \
         patch.object(g.GitSnapshot,'_text',text),patch.object(g.GitSnapshot,'_repository_object_type',lambda self,p:'tree' if p=='specification_methodology/v3/standards' else None):
        result=g.resolve_channel('synthetic','3.0.2')
        assert result.cut=='v3.0.2' and result.cut_ordinal is None and result.cut_ref==result.selector_ref==TAG
        return result

snapshot_probe(g.STABLE_TAG_MARKER)
record['cases'].append({'case':'stable object/profile and channel path with synthetic read-only Git observations','result':'passed'})
for name,message,kind,tag in [
    ('missing marker','release','commit','specification_methodology/v3.0.2'),
    ('duplicate marker',g.STABLE_TAG_MARKER+'\n'+g.STABLE_TAG_MARKER,'commit','specification_methodology/v3.0.2'),
    ('indented marker',' '+g.STABLE_TAG_MARKER,'commit','specification_methodology/v3.0.2'),
    ('indirect tag target',g.STABLE_TAG_MARKER,'tag','specification_methodology/v3.0.2'),
    ('wrong embedded tag identity',g.STABLE_TAG_MARKER,'commit','v3.0.2')]:
    refused(name,lambda message=message,kind=kind,tag=tag:snapshot_probe(message,kind,tag))

sys.path.insert(0,str(ROOT/'specification_methodology/v2/tests'))
from test_toolchain import definition_document
STORE=Path('/Users/jim/Library/Application Support/STDO')
LEGACY='60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8'
with tempfile.TemporaryDirectory(prefix='cli-',dir=HERE) as tmp:
    root=Path(tmp);env={**os.environ,'PYTHONPATH':'/nonexistent-reviewer-poison','PYTHONDONTWRITEBYTECODE':'1','TMPDIR':str(root)}
    env.pop('PYTHONHOME',None)
    argv=[sys.executable,'-I','-B','-m','stdo_toolchain.cli','manifest','v3.0.1-rc.1','--repository',str(ROOT)]
    completed=subprocess.run(argv,cwd='/',env=env,capture_output=True,text=True,timeout=30)
    assert completed.returncode==0,completed.stderr
    legacy=json.loads(completed.stdout);assert legacy['manifest_sha256']==LEGACY
    assert 'profile' not in legacy['manifest']['release']
    record['cases'].append({'case':'actual legacy native tag manifest through isolated wheel CLI','result':'passed','argv':argv,'report':legacy})
    for name in ['a','b']:
        directory=root/name;directory.mkdir();doc=definition_document(ROOT,'stdo://releases/v3.0.1-rc.1/',LEGACY)
        doc.pop('unrelated',None);doc['product']['definition_id']='urn:test:composition:'+name
        doc['$schema']='stdo://releases/v3.0.1-rc.1/standards/schemas/product-definition.schema.json'
        doc['constitution']['stdo']['selector']='stdo://channels/3.0.1'
        doc['reference_frame_bases'][0]['applies_to']=[doc['product']['definition_id']]
        if name=='a':doc['composition']=[{'product_definition':'../b/stdo_b.json','target_definition_id':'urn:test:composition:b','relation':'relation.md#support','contracts':['../b/contract.md#contract']}]
        (directory/('stdo_'+name+'.json')).write_text(json.dumps(doc,indent=2)+'\n')
        (directory/'contract.md').write_text('# Contract\n')
    cases=[('list fence','- ```markdown\n  # Support\n  <a id="support"></a>\n  ```\n',False),
      ('unfinished comment','<!-- unfinished\n# Support\n<a id="support"></a>\n',False),
      ('escaped HTML','\\<a id="support"></a>\n',False),
      ('multiline inline code','`code\n<a id="support"></a>\ncode`\n',False),
      ('plain heading','# Support\n',True),
      ('genuine after list fence','- ```markdown\n  # Hidden\n  ```\n\n# Support\n',True),
      ('genuine after comment','<!-- hidden -->\n<a id="support"></a>\n',True),
      ('quote-list HTML','> - <a id="support"></a>\n',True)]
    observations=[]
    for name,body,valid in cases:
        (root/'a/relation.md').write_text(body)
        for mode in ['wheel','source']:
            command=[sys.executable,*(['-I'] if mode=='wheel' else []),'-B','-m','stdo_toolchain.cli','--store',str(STORE),'fleet','verify','--root',str(root/'a/stdo_a.json'),'--resolver-root',str(root)]
            environment=dict(env)
            if mode=='source':environment['PYTHONPATH']=str(ROOT/'specification_methodology/v2/src')
            result=subprocess.run(command,cwd='/',env=environment,capture_output=True,text=True,timeout=30)
            response=json.loads(result.stdout)
            assert result.returncode==(0 if valid else 1),(name,mode,result.returncode,response,result.stderr)
            assert response['valid'] is valid
            if not valid:assert 'missing_fragment' in json.dumps(response),(name,mode,response,result.stderr)
            observations.append({'case':name,'mode':mode,'argv':command,'exit':result.returncode,'report':response})
    record['cases'].append({'case':'actual source and installed-wheel composition CLI fragment discriminators','result':'passed','observations':observations})

assert all(hashlib.sha256((ROOT/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in index['files'])
with (HERE/'RESULTS.json').open('x') as output:json.dump(record,output,indent=2);output.write('\n')
print(json.dumps({'groups':len(record['cases']),'passed':True,'output':str(HERE/'RESULTS.json')}))
