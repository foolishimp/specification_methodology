from pathlib import Path,PurePosixPath
import hashlib,io,json,stat,subprocess,time,zipfile
R=Path('/Users/jim/src/apps/specification_methodology')
B=R/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/cohort-recovery-020'
C=R/'specification_methodology/v3/build_tenants/common'
OUT=Path(__file__).parent
START=time.monotonic()
def sha(raw):return hashlib.sha256(raw).hexdigest()
def read(p):return json.loads(p.read_bytes())
def save(n,v):(OUT/n).write_text(json.dumps(v,indent=2,sort_keys=True)+'\n')
def check_ref(row,base=R):
 p=base/row['path'];st=p.lstat();assert stat.S_ISREG(st.st_mode),str(p)
 raw=p.read_bytes();assert sha(raw)==row['sha256'],str(p)
 if 'bytes' in row:assert len(raw)==row['bytes'],str(p)
 return {'path':str(p),'sha256':sha(raw),'bytes':len(raw),'mode':stat.S_IMODE(st.st_mode),'mtime_ns':st.st_mtime_ns}
def oldraw(rel):return subprocess.check_output(['git','show','ec0c09474a1d42084ddd1ba2b97c9479affb0220:'+rel],cwd=R)
F=read(B/'PAYLOAD_REVIEW_FREEZE.json')
assert sha((B/'PAYLOAD_REVIEW_FREEZE.json').read_bytes())=='aabf49204294cfee9ff9c040f2ce83178721f116a34f628b771228c47430e64b'
refs=[F['subject'],*F['references'],*F['transport_parts']]
before={r['path']:check_ref(r) for r in refs}
subject=read(R/F['subject']['path'])
inv=read(B/'NATIVE_INPUT_INVENTORY.json')['files'];assert inv==F['native_members'] and len(inv)==171
native={r['path']:check_ref(r,C) for r in inv}
paths=list(C.rglob('*'));assert all(not p.is_symlink() for p in paths)
assert {p.relative_to(C).as_posix() for p in paths if p.is_file()}==set(native)
for r in inv:
 raw=(C/r['path']).read_bytes();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==r['git_blob']
 assert ('100755' if native[r['path']]['mode']&0o111 else '100644')==r['git_mode']
assert sum(x['bytes'] for x in native.values())==subject['native_bytes']==290062273
oldinv={r['path']:r for r in read(B.parent/'cohort-recovery-019/NATIVE_INPUT_INVENTORY.json')['files']}
assert set(oldinv)==set(native)
changed=[r['path'] for r in inv if r!=oldinv[r['path']]]
assert len(changed)==16 and set(changed)=={r['path'].removeprefix(C.relative_to(R).as_posix()+'/') for r in subject['changed_native_files']}
newinv={r['path']:r for r in inv}
for row in read(B/'PRE_COPY_DELTA.json')['changed']:
 assert row['before']==oldinv[row['after']['path']]
 assert row['after']==newinv[row['after']['path']]
for path in changed:
 root=B/('current-documentation' if path.startswith('standards/documentation/') else 'current-tooling')
 relative=path.removeprefix('standards/documentation/').removeprefix('standards/tooling/')
 assert (root/relative).read_bytes()==(C/path).read_bytes()
save('NATIVE_CHECK.json',{'frozen_refs':before,'native_before':native,'changed':changed,'unchanged':155,'bytes':sum(x['bytes'] for x in native.values())})
P=C/'standards/documentation/proofs';T=read(P/'transport/TRANSPORT.json')
archive=b''.join((P/'transport'/x['path']).read_bytes() for x in T['parts'])
assert len(archive)==T['archive_bytes']==124504542 and sha(archive)==T['archive_sha256']==subject['transport']['archive_sha256']
for row in T['parts']:check_ref(row,P/'transport');assert row['bytes']<=64*1024*1024
with zipfile.ZipFile(io.BytesIO(archive)) as z:
 assert len(z.infolist())==len(set(z.namelist()))==61
 assert set(z.namelist())==set(T['members']) and 'local-origin.json' not in z.namelist()
 got={}
 for info in z.infolist():
  assert not info.is_dir() and not stat.S_ISLNK(info.external_attr>>16)
  path=PurePosixPath(info.filename);assert not path.is_absolute() and '..' not in path.parts
  h=hashlib.sha256();total=0
  with z.open(info) as fp:
   for chunk in iter(lambda:fp.read(1048576),b''):h.update(chunk);total+=len(chunk)
  got[info.filename]={'bytes':total,'sha256':h.hexdigest()}
 assert got==T['members'] and sum(v['bytes'] for v in got.values())==T['expanded_bytes']==579468245
 manifest=z.read('manifest.json');result=z.read('result.json')
 assert sha(manifest)==T['manifest_sha256'] and sha(result)==T['result_sha256']
 assert manifest==(B.parent/'tools-skills/current-formal-016/cold/manifest.json').read_bytes()
 assert result==(P/'evidence/result.json').read_bytes()==(B.parent/'tools-skills/current-formal-021/cold/result.json').read_bytes()
 map59=json.loads(manifest)['members'];assert len(map59)==59
 assert {k:v['sha256'] for k,v in got.items() if k not in ['manifest.json','result.json']}==map59
save('TRANSPORT_CHECK.json',{'archive_sha256':sha(archive),'archive_bytes':len(archive),'members':got,'mathematical_manifest_sha256':sha(manifest),'mathematical_59_equal_016':True,'result_sha256':sha(result)})
del archive
U=C/'standards/tooling';tooling=read(U/'TOOLING.json');selection=read(U/'SELECTION.json')
assert sha((U/'SELECTION.json').read_bytes())==tooling['selection_sha256']
owner={x['path']:x for v in selection['owners'].values() for x in v['members']};assert len(owner)==240
with zipfile.ZipFile(U/'sources.zip') as new,zipfile.ZipFile(io.BytesIO(oldraw((U/'sources.zip').relative_to(R).as_posix()))) as old:
 assert len(new.namelist())==len(set(new.namelist()))==240 and set(new.namelist())==set(old.namelist())==set(owner)
 source_changes=[]
 for row in tooling['sources']:
  name=row['archive_path'];raw=new.read(name);prev=old.read(name)
  assert sha(raw)==row['sha256']==owner[name]['sha256'] and len(raw)==row['bytes']==owner[name]['bytes']
  assert raw==(R/name).read_bytes()
  if raw!=prev:source_changes.append({'path':name,'before':sha(prev),'after':sha(raw)})
 declared=[{'path':row['after']['path'],'before':row['before']['sha256'],'after':row['after']['sha256']} for row in read(B/'UNCHANGED_RELATIONS.json')['changed_tooling_members']]
 assert sorted(source_changes,key=lambda x:x['path'])==sorted(declared,key=lambda x:x['path']) and len(source_changes)==7
save('SOURCE_ARCHIVE_CHECK.json',{'members':240,'changed':source_changes,'other_233_exact_A3':True})
print(json.dumps({'status':'native_transport_sources_passed','native_changed':16,'proof_members':61,'source_members':240,'source_changes':source_changes,'elapsed_seconds':time.monotonic()-START}))
