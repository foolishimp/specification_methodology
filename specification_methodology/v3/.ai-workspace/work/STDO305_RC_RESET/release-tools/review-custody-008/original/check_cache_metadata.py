from pathlib import Path
import json,hashlib,posixpath
r=Path('/Users/jim/src/apps/specification_methodology');q=r/'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET/tools-skills/installed-qualification-002';out=Path(__file__).parent
p=q/'cache-clone-001/INVENTORY_JOIN.json';assert hashlib.sha256(p.read_bytes()).hexdigest()=='d8500c948eba4617b102e06e9917eae8dc82b9a9f154423c552599e6c5539ff5';d=json.loads(p.read_bytes())
def path(ref):
 x=Path(ref['path']);return x if x.is_absolute() else r/x
def check(ref):
 x=path(ref);h=hashlib.sha256();total=0
 with x.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b);total+=len(b)
 assert h.hexdigest()==ref['sha256'] and total==ref['bytes'];return x
profile=json.loads(check(d['source_profile']).read_bytes());prefixes=('.toolchain/','.lake/packages/','.cache/mathlib/');roots={p.rstrip('/') for p in prefixes};expected={k:v for k,v in profile['members'].items() if k.startswith(prefixes)}
ledger={}
with check(d['clone_ledger']).open() as f:
 for line in f:
  x=json.loads(line);key=x['path'];assert key not in ledger and (key.startswith(prefixes) or key in roots)
  if x['kind']=='file':
   assert x['clone']['returncode']==0 and x['clone']['copy_fallback'] is False
   a,b=x['source_identity'],x['destination_identity'];assert (a['device'],a['inode'])!=(b['device'],b['inode']);ledger[key]=('file',x['sha256'])
  elif x['kind']=='symlink':ledger[key]=('symlink',x['link'])
  else:assert x['kind']=='directory';ledger[key]=(x['kind'],None)
joined={}
with check(d['join']).open() as f:
 for line in f:
  x=json.loads(line);key=x['path'];assert key not in joined and expected[key]==x['expected_sha256']==x['observed_sha256'];target=key;seen=set()
  while ledger[target][0]=='symlink':
   assert target not in seen;seen.add(target);target=posixpath.normpath(posixpath.join(posixpath.dirname(target),ledger[target][1]));assert target.startswith(prefixes)
  assert target==x['ledger_file'] and ledger[target]==('file',x['observed_sha256']);joined[key]=True
assert set(joined)==set(expected) and len(joined)==d['joined_members']==30369
extras=set()
with check(d['unprofiled_paths']).open() as f:
 for line in f:
  x=json.loads(line);assert x['path'] not in extras;extras.add(x['path'])
assert extras==set(ledger)-set(expected) and len(extras)==d['unprofiled_entries']==19705
for x in d['package_revisions']:
 for o in x['observations']:assert o['returncode']==0 and o['stdout'].strip()==x['expected_revision']
a=d['archive'];assert ledger[a['path']]==('file',a['sha256'])
record={'kind':'stdo.independent-cache-metadata-join-check/1','status':'consistent','join_sha256':'d8500c948eba4617b102e06e9917eae8dc82b9a9f154423c552599e6c5539ff5','source_profile_sha256':d['source_profile']['sha256'],'clone_ledger_sha256':d['clone_ledger']['sha256'],'profile_members_matched':len(expected),'unprofiled_entries_separate':len(extras),'package_revisions':len(d['package_revisions']),'limitations':'Pure retained metadata reconstruction only; no live source/cache/runtime file-tree scan, no proof standing from the clone, no success claim for active model proof.','reviewer_probe_correction':'Initial scratch assertion assumed all ledger paths have a slash-suffixed prefix; the declared root directory .toolchain is a legitimate ledger entry. Corrected scratch-only check explicitly includes the three declared roots.'}
(out/'CACHE_METADATA_CHECK.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record));print(hashlib.sha256((out/'CACHE_METADATA_CHECK.json').read_bytes()).hexdigest())
