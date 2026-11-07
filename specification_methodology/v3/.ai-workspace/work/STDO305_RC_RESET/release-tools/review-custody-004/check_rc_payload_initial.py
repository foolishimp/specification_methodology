from pathlib import Path
import hashlib,io,json,re,stat,subprocess,sys,zipfile
ROOT=Path('/Users/jim/src/apps/specification_methodology')
BASE=ROOT/'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET/release-tools'
P=BASE/'packaging-001';COMMON=ROOT/'specification_methodology/v3/build_tenants/common'
OUT=Path(__file__).parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def raw(ref):
 b=(ROOT/ref['path']).read_bytes();assert sha(b)==ref['sha256'],ref['path']
 if 'bytes' in ref:assert len(b)==ref['bytes'],ref['path']
 return b
def load(ref):return json.loads(raw(ref))
def git(commit,path):return subprocess.check_output(['git','--no-optional-locks','-C',str(ROOT),'show',commit+':'+path])
fraw=(P/'FREEZE.json').read_bytes();f=json.loads(fraw);assert sha(fraw)=='211225aa054f0557faee8b6fa96eed3631fe239d1643caed7cd6dea3c5d7fb40'
refs=f['references']+[f[k] for k in ('manager_build','materializer_freeze','materializer_review_custody','source_freeze','source_review_custody')]
for r in refs:raw(r)
report={'subject_sha256':sha(fraw),'source_checkpoint':f['source_checkpoint'],'direct_refs':len(refs)}
# Exact current native bytes, modes, population, and before-copy delta.
rows=json.loads((P/'NATIVE_INPUT_INVENTORY.json').read_bytes())['files'];actual={}
for row in rows:
 q=COMMON/row['path'];assert q.is_file() and not q.is_symlink();b=q.read_bytes()
 assert sha(b)==row['sha256'] and len(b)==row['bytes'] and stat.S_IMODE(q.stat().st_mode)==(int(row['git_mode'],8)&0o777),row['path'];actual[row['path']]=row
assert {p.relative_to(COMMON).as_posix() for p in COMMON.rglob('*') if p.is_file()}==set(actual)
delta=json.loads((P/'PRE_COPY_DELTA.json').read_bytes());pre={r['path']:r for r in load(delta['source_preimage'])['files']};changes={r['after']['path']:r for r in delta['changed']}
assert set(pre)==set(actual)
for path,row in actual.items():
 if path in changes:assert changes[path]=={'before':pre[path],'after':row}
 else:assert row==pre[path]
assert set(json.loads((P/'COPY_RESULT.json').read_bytes())['changed_paths'])==set(changes)
s=load(f['source_freeze']);semantic=s['members']+s['native_contracts']
for row in semantic:assert actual[row['path']]['sha256']==row['sha256']
report['native']={'members':len(actual),'bytes':sum(r['bytes'] for r in rows),'exact_delta':len(changes),'unchanged':len(actual)-len(changes),'source_members':len(semantic),'all_match':True}
# Manager source, wheel, and closed runtime artifact set.
build=load(f['manager_build']);selection=load(build['source_selection'])
for row in selection['source_members']:
 b=raw(row);assert git(selection['source_commit'],row['path'])==b
wheel_raw=raw(build['wheel']);wheel=zipfile.ZipFile(io.BytesIO(wheel_raw));package=[r for r in selection['source_members'] if '/src/' in r['path']]
for row in package:assert wheel.read(row['path'].split('/src/',1)[1])==raw(row)
assert {n for n in wheel.namelist() if n.startswith('stdo_toolchain/')}=={r['path'].split('/src/',1)[1] for r in package}
metadata=wheel.read('stdo_toolchain-3.0.5rc1.dist-info/METADATA').decode();assert '\nVersion: 3.0.5rc1\n' in metadata
runtime=zipfile.ZipFile(io.BytesIO(raw(build['runtime_archive'])));wheels=json.loads(runtime.read('WHEELS.json'))
for row in wheels['members']:
 b=runtime.read(row['path']);assert sha(b)==row['sha256'] and len(b)==row['bytes']
assert set(runtime.namelist())=={'README.md','WHEELS.json','constraints-python313.txt','requirements-macos-arm64-cp313.txt'}|{r['path'] for r in wheels['members']}
assert runtime.read('wheels/'+Path(build['wheel']['path']).name)==wheel_raw
assert runtime.read('constraints-python313.txt')==raw(build['constraints'])
report['manager']={'source_commit':selection['source_commit'],'source_members':len(selection['source_members']),'package_sources':len(package),'wheel_version':'3.0.5rc1','release_version':selection['release_version'],'runtime_wheels':len(wheels['members']),'runtime_members':len(runtime.namelist()),'all_match':True,'acquisition':build['acquisition']}
# The actual shipped tool archive is consumed by the corrected standalone source checker.
sys.path.insert(0,str(ROOT/'specification_methodology/v3/build_tenants/common-tools'))
import tooling_materialize as tool
meta,sources=tool.source_bytes(tool.read_bundle(COMMON/'standards/tooling'))
sel=json.loads((COMMON/'standards/tooling/SELECTION.json').read_bytes())
for owner,unit in sel['owners'].items():
 assert unit['version']=='3.0.5-rc.1'
 for row in unit['members']:
  b=raw(row);assert sources[row['path']]==b
assert meta['source_identity_sha256']==s['source_identity_sha256']
assert (COMMON/'standards/tooling/materialize.py').read_bytes()==Path(tool.__file__).read_bytes()
report['tooling']={'members':len(sources),'owners':{k:{'version':v['version'],'members':len(v['members'])} for k,v in sel['owners'].items()},'actual_source_archive_current':True,'corrected_materializer_sha256':sha(Path(tool.__file__).read_bytes())}
# F3: actual rendered projection, retained exact source, five immutable target objects.
import proof_reader_current as proof
proofroot=COMMON/'standards/documentation/proofs';selected=json.loads((proofroot/'SELECTION.json').read_bytes())
files={'SELECTION.json':(proofroot/'SELECTION.json').read_bytes()}
for name in proof.DOCUMENT_LINKS:
 files[name]=(proofroot/'source-documents'/ (name+'.txt')).read_bytes()
proof.validate_document_sources(ROOT,files)
profile=proof.document_profile(files);links=[]
for name,one in profile.items():
 presentation=(proofroot/name).read_bytes();assert proof.project_document(name,files[name],profile)==presentation
 assert git(one['commit'],one['source']['path'])==files[name]
 for relative,target in one['links']:
  path,_,fragment=target.partition('#');b=git(one['commit'],path);assert b
  if fragment:
   assert '# '+fragment.replace('-',' ').lower() in b.decode().lower() or fragment in {re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in re.findall(r'^#{1,6}\s+(.+?)\s*#*\s*$',b.decode(),re.M)}
  links.append({'document':name,'commit':one['commit'],'path':path,'fragment':fragment,'sha256':sha(b)})
assert len(links)==5
report['document_links']={'source_custody_and_projection_exact':True,'actual_git_targets':links,'current_checkpoint':selected['document_source_commit'],'historical_library_checkpoint':proof.DOCUMENT_SOURCE_COMMIT,'network_use':'None; target objects checked in Git. Browser offline observation remains separate.'}
# Exact multipart archive and each retained member, with no extraction or Lean run.
transport_root=P/'archives/transport';t=json.loads((transport_root/'TRANSPORT.json').read_bytes());parts=[]
for row in t['parts']:
 b=(transport_root/row['path']).read_bytes();assert len(b)==row['bytes']<=64*1024*1024 and sha(b)==row['sha256'];parts.append(b)
joined=b''.join(parts);assert len(joined)==t['archive_bytes'] and sha(joined)==t['archive_sha256'];archive=zipfile.ZipFile(io.BytesIO(joined));assert set(archive.namelist())==set(t['members']) and len(archive.infolist())==len(t['members'])
for name,row in t['members'].items():
 b=archive.read(name);assert len(b)==row['bytes'] and sha(b)==row['sha256'],name
manifest_raw=archive.read('manifest.json');manifest=json.loads(manifest_raw);result_raw=archive.read('result.json');result=json.loads(result_raw)
assert sha(manifest_raw)==t['manifest_sha256'] and sha(result_raw)==t['result_sha256']==selected['result']['sha256']
assert result_raw==(proofroot/'evidence/result.json').read_bytes()
assert result['status']=='verified' and result['inputs']['model']['raw_sha256']==selected['model']['sha256']
assert [result['observations'][k] for k in ('current_dynamic_proof_invocations','current_kernel_replay_invocations','current_runtime_invocations')]==[7,1,1]
assert len(result['checked_claims'])==5 and all(set(v)<={'Classical.choice','Quot.sound','propext'} for v in result['observations']['theorem_audit'].values())
for name,digest in manifest.items():
 assert name in t['members'] and t['members'][name]['sha256']==digest
catalog=json.loads((proofroot/'PROOFS.json').read_bytes());doc=json.loads((COMMON/'standards/documentation/DOCUMENTATION.json').read_bytes())
assert catalog['result_sha256']==sha(result_raw) and catalog['runtime_identity']==result['runtime_identity'] and catalog['model']['sha256']==result['model']['sha256']
assert doc['model']==catalog['model'] and doc['source']['source_identity_sha256']==s['source_identity_sha256'] and doc['proof_catalog_sha256']==sha((proofroot/'PROOFS.json').read_bytes())
assert doc['viewer_sha256']==sha((COMMON/'standards/documentation/constraint-explorer/index.html').read_bytes())
report['proof_transport']={'archive_sha256':t['archive_sha256'],'members':len(t['members']),'manifest_members':len(manifest),'parts':len(parts),'exact_members_checked':True,'result_sha256':sha(result_raw),'runtime_sha256':result['runtime_identity']['sha256'],'model':result['model'],'five_claims':result['checked_claims'],'observed_counts':[7,1,1],'limits':result['limits'],'source_scope':'Fresh dynamic construction obligations with pinned existing support; no installed proof claimed.'}
report['documentation_join']={'model':doc['model'],'source':doc['source'],'viewer_sha256':doc['viewer_sha256'],'proof_catalog_sha256':doc['proof_catalog_sha256'],'proof_reader_sha256':sha((proofroot/'index.html').read_bytes()),'landing_sha256':sha((COMMON/'standards/documentation/index.html').read_bytes())}
for r in refs:raw(r)
report['final_direct_refs_unchanged']=True
(OUT/'RC_PAYLOAD_CHECK.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'checked','report':str(OUT/'RC_PAYLOAD_CHECK.json'),'sha256':sha((OUT/'RC_PAYLOAD_CHECK.json').read_bytes()),'native':report['native'],'manager':report['manager'],'tooling':len(sources),'archive_members':len(t['members'])}))
