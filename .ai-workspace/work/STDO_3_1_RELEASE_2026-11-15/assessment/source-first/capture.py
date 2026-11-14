from pathlib import Path
import json, hashlib, subprocess, datetime, uuid
repo=Path('/Users/jim/src/apps/specification_methodology')
out=repo/'.ai-workspace/work/STDO_3_1_RELEASE_2026-11-15/assessment/source-first'
installed=Path('/Users/jim/Library/Application Support/STDO/releases/v3.0.4')
sha=lambda b:hashlib.sha256(b).hexdigest()
manifest=json.loads((installed/'manifest.json').read_text())
assert sha((installed/'manifest.json').read_bytes())=='102817a3f4bea4dca1d6fa0fc634b94404dd2ba82ba6d8c38b273402dda9f95b'
entries=[]
chunks=[]
def add(label,path,ranges=None):
 data=path.read_bytes(); lines=data.decode().splitlines(keepends=True)
 if ranges is None:ranges=[(1,len(lines))]
 body=''.join(f'\n[Original lines {a}-{b}]\n'+''.join(lines[a-1:b]) for a,b in ranges)
 entry={'label':label,'origin':str(path),'source_sha256':sha(data),'selected_lines':ranges,'selected_body_sha256':sha(body.encode())}
 entries.append(entry)
 chunks.append(f'\n\n===== VERBATIM GOVERNING SOURCE: {label} =====\nSource SHA-256: {entry["source_sha256"]}\n{body}\n===== END SOURCE =====\n')
 assert sha(path.read_bytes())==entry['source_sha256'],'source changed during capture'
add('release activation',repo/'.ai-workspace/work/STDO_3_1_RELEASE_2026-11-15/ACTIVATION.md')
add('root AGENTS.md',repo/'AGENTS.md')
roots=[('specification_methodology/v3','stdo_3.json'),('purpose_context','stdo_purpose_context.json'),('stdo_skills','stdo_skills.json'),('a_c','stdo_a_c.json'),('stdo_representation','stdo_representation.json'),('axiom_indexer','stdo_default.json')]
statuses=[]
for root,definition in roots:
 p=repo/root
 status=json.loads(subprocess.check_output(['/Users/jim/.local/bin/stdo','status','--definition',str(p/definition),'--verify']))
 assert status['valid'] and status['installed'] and not status['failures']
 assert status['manifest_sha256']==sha((installed/'manifest.json').read_bytes())
 compact={k:status[k] for k in ['definition','definition_id','basis','manifest_sha256','installed','valid','failures','path','release']}
 statuses.append(compact)
 for filename in [definition,'AGENTS.md','README.md','specification/GOALS.md','specification/INTENT.md','specification/PRODUCT.md','specification/REFERENCE_FRAME_BASIS.md']:
  ranges=None
  if root=='specification_methodology/v3' and filename=='specification/GOALS.md':ranges=[(1,82),(231,240)]
  if root=='specification_methodology/v3' and filename=='specification/PRODUCT.md':ranges=[(1,278),(302,407),(501,511)]
  if root=='specification_methodology/v3' and filename=='specification/REFERENCE_FRAME_BASIS.md':ranges=[(1,99),(151,164)]
  add(root+'/'+filename,p/filename,ranges)
 reqs=sorted((p/'specification/requirements').glob('*.md'))
 if root=='specification_methodology/v3':
  selected={'README.md','SDLC_DEFAULTS.md','COMPLETE_RELEASE.md','INSTALLED_TOOLING.md','INSTALLED_DOCUMENTATION.md','COORDINATED_SKILLS.md','REVIEW_FLOW.md','A_C_DEPENDENCY.md','PRODUCT_COMPOSITION.md','ASSURANCE.md'}
  reqs=[r for r in reqs if r.name in selected]
 for f in reqs:add(str(f.relative_to(repo)),f)
installed_selections={
 'standards/RELEASE.md':[(1,81),(144,820)],
 'standards/EVALUATION.md':[(1,58),(141,444),(616,776)],
 'standards/ACTIVATION.md':[(353,618),(619,692),(693,937),(1114,1163),(1370,1518),(1627,1771)],
 'standards/TICKETS.md':[(1,100),(148,178),(536,592),(672,795),(1088,1336)],
 'plugins/spec/skills/stdo-review/SKILL.md':None,
 'plugins/spec/skills/stdo-work/SKILL.md':None,
 'plugins/spec/references/PRODUCT_BASIS.md':None,
 'plugins/spec/references/COORDINATED_HANDOFF.md':None,
}
for filename,ranges in installed_selections.items():add('installed-3.0.4/'+filename,installed/filename,ranges)
packet='''# Source-first independent release expectation intake\n\nTask: derive a finite qualification matrix for the authorized STDO 3.1.0-rc.1 release from the governing sources below BEFORE receiving candidate implementations, indexes, test outputs, author expectations or verdicts. This is expectation derivation only; no candidate result is sought at this stage. Root's exact activation is included verbatim.\n\nRequested review relation: six separately owned Products coordinated by the release activation. Every Product has its own definition and verified installed 3.0.4 construction basis; there is no synthetic seventh Product or implicit adoption. Product/status bindings below are mechanical source verification, not semantic verdicts.\n\nAuthority: the Root release activation explicitly permits review operators to retain actual independent-family Claude results and write only their reports. You return through this print session; the authorized assessment recorder persists stdout unchanged. No candidate or other writes are permitted. Use the installed stdo-review instructions below in this source-first stage. Final exact candidate identities will be supplied in a later stage.\n\nAcquisition: this packet contains verbatim governing-source projections with exact original line ranges and digests. No candidate implementation, generated index body, previous expected response, or candidate test result is included. Source Product documents may refer to historic standing; such source prose is not supplied evidence of a later candidate. All tools are disabled for this expectation stage; request any genuinely missing material source by exact path/section in your return. The packet is sufficient for expectation derivation only, not a candidate verdict. No hostile-code or clean-room isolation claim is made.\n\nAuthorship and host: the operator is Codex and a release assessment recorder, not the Product source author. You are a separate Claude first-party model family, selected through a fresh CLI print session with safe mode, no tools, no inherited conversation, and no session persistence. CLI metadata supplies actual model/session, not this request's assertion. No semantic actor-family waiver is selected. Do not infer independence solely from fresh context; declare the available authorship/evidence conditions and residuals.\n\nOutput: (1) source-derived minimal release predicates with source citations, exact observation boundary and finite falsifier; (2) semantic/behavior/migration case matrix for the changed Purpose Context/default SDLC/ticket-context/Skills/visual-only path, preserving cross-Product interactions; (3) prior-evidence applicability criteria, mandatory reruns and allowed reuse; (4) gaps or ambiguous governing obligations requiring a declared disposition before final claims; (5) exact evidence needed for your later candidate assessment. Keep historical duties on their historical subjects. Do not add universal review rounds, require a general whole-method reliability proof for bounded release claims, revive retired runtime requirements without governing authority, or invent supported coverage. Those are source interpretation questions for your independent judgment, not expected answers. Return observations, scope and limits; do not authorize publication, assign Product priority or supply a release verdict.\n\nVerified selected Product/basis identities:\n'''+json.dumps(statuses,indent=2)+'\n'+''.join(chunks)
(out/'SOURCE_PACKET.md').write_text(packet)
(out/'SOURCE_MANIFEST.json').write_text(json.dumps({'captured_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_packet_sha256':sha(packet.encode()),'source_packet_bytes':len(packet.encode()),'sources':entries,'verified_products':statuses,'candidate_exposure':'none; public source requirements/control only'},indent=2)+'\n')
session=str(uuid.uuid4())
(out/'SESSION_ID').write_text(session+'\n')
print(json.dumps({'files':len(entries),'packet_bytes':len(packet.encode()),'packet_sha256':sha(packet.encode()),'session_id':session},indent=2))
