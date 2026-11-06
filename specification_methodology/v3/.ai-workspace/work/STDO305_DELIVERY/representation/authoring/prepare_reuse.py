"""Work-local candidate assembly, never a semantic author or provider build replacement."""
import json,pathlib,hashlib,collections,sys
ROOT=pathlib.Path(__file__).resolve().parents[7]
# Resolve repository from the fixed work scope, not the user's environment.
while not (ROOT/'stdo_representation').is_dir(): ROOT=ROOT.parent
WORK=pathlib.Path(__file__).parent
RUN=ROOT/'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5/run'
PREFIX='build_tenants/a_c/representation/stdo-v3.0.5/source/'
old=json.loads((ROOT/'a_c/applications/stdo-v3-common-35fb4824/run/repaired-proposal/model.json').read_text())
oldchunks=json.loads((ROOT/'a_c/applications/stdo-v3-common-35fb4824/run/chunks.json').read_text())
oldsegments={s['id']:s for c in oldchunks for s in c['segments']}
chunks=json.loads((RUN/'generation/chunks.json').read_text());
if '--coherent-draft' in sys.argv:
 chunks=[{'id':'draft-coherent-not-a-public-task','segments':[s for c in chunks for s in c['segments']]}]
segments={};chunkof={}
for chunk in chunks:
 for segment in chunk['segments']:
  segments[(segment['path'].removeprefix(PREFIX),segment['heading'])]=segment
  chunkof[segment['id']]=chunk['id']
# These meanings are explicitly superseded by the current F_D/import/review/release owners.
REAUTHOR={'cc99c053f518c955c093894ab174b704','aeb3b76829c62d92d2421634121dbe87','d95615227f8fdfe4b3e7141e3ba237e3','d9237cdda330747e7521d91a94f9903d','c36742969202896443796eebdfd9412a','2bbbd963f7f6d5d24101d2e46322aece','26c627c4204c2f1f3b1820e20d788928','49318086a847f97f92e8b24ef9e83d81','6df41135c9856299bf9ef53e0ecba6bb'}
FAMILY={'objects':'concepts','relations':'relations','constraints':'constraints','latitude':'latitude','residuals':'residuals'}
BODY={'objects':'value','relations':'qualifiers','constraints':'predicate','latitude':'allowed_variation','residuals':'uncertainty'}
keyof=lambda value:'prior_'+value.rsplit(':',1)[-1]
selected={};ledger=[]
for family,rows in old['populations'].items():
 for row in rows:
  ident=row['id'];body=row[BODY[family]];checked=[];grounds=[];reason=None
  if ident.rsplit(':',1)[-1] in REAUTHOR:reason='changed normative meaning explicitly selected for fresh authoring'
  for ground in body['grounding']:
   prior=oldsegments.get(ground['section']);target=segments.get((ground['path'],prior['heading'])) if prior else None
   if not target or ground['quote'] not in target['text']:
    reason=reason or 'source member/section/quote changed or outside selected current corpus';continue
   index=target['text'].index(ground['quote']);start=target['start_line']+target['text'][:index].count('\n');end=start+ground['quote'].count('\n')-(1 if ground['quote'].endswith('\n') else 0)
   grounds.append({'section_id':target['id'],'start_line':start,'end_line':end,'quote':ground['quote']});checked.append(prior['text']==target['text'])
  chunkids={chunkof[g['section_id']] for g in grounds}
  if len(chunkids)!=1:reason=reason or 'grounded record crosses public task boundary; requires fresh local authoring'
  record={'key':keyof(ident),'grounding':grounds}
  if family=='objects':record.update({k:body[k] for k in ['label','definition','conditions','exceptions']})
  elif family=='relations':record.update({k:body[k] for k in ['kind','meaning','conditions','exceptions']});record.update(source_key=keyof(row['source']),target_key=keyof(row['target']),governing=':governing:' in row['kind'])
  elif family=='constraints':record.update({k:body[k] for k in ['statement','uncertainty','conditions','exceptions']});record['applies_to_keys']=[keyof(x) for x in row['applies_to']]
  elif family=='latitude':record.update(applies_to_keys=[keyof(x) for x in row['applies_to']],allowed=row['allowed_variation']['statements'],forbidden=row['forbidden_variation']['statements'])
  else:record.update(subject_key=keyof(row['subject']),uncertainty=body['statement'],consequence=row['consequence'])
  entry={'old_record':ident,'family':FAMILY[family],'key':keyof(ident),'all_ground_sections_equal':bool(checked) and all(checked),'chunk':next(iter(chunkids)) if len(chunkids)==1 else None,'reason':reason,'standing':'not selected' if reason else 'candidate only; LLM conservation decision required'};ledger.append(entry)
  if not reason:selected[record['key']]={'record':record,'family':FAMILY[family],'chunk':entry['chunk'],'ledger':entry}
# Preserve dependency closure in each public task; no hidden cross-task author refs.
changed=True
while changed:
 changed=False
 for key,item in list(selected.items()):
  r=item['record'];deps=([r['source_key'],r['target_key']] if item['family']=='relations' else r.get('applies_to_keys',[r['subject_key']] if item['family']=='residuals' else []))
  if any(dep not in selected or selected[dep]['chunk']!=item['chunk'] for dep in deps):
   item['ledger']['reason']='local supporting identity absent in this task; fresh local authoring required';item['ledger']['standing']='not selected';del selected[key];changed=True
answers={c['id']:{**{f:[] for f in FAMILY.values()},'dispositions':[],'limitations':['Source-local semantic proposal; processing coverage and mechanical checks do not establish semantic completeness or acceptance.']} for c in chunks}
for item in selected.values():answers[item['chunk']][item['family']].append(item['record'])
for chunk in chunks:
 answer=answers[chunk['id']]
 for seg in chunk['segments']:
  refs=[r['key'] for fam in FAMILY.values() for r in answer[fam] if any(g['section_id']==seg['id'] for g in r['grounding'])]
  answer['dispositions'].append({'section_id':seg['id'],'decision':'retained' if refs else 'omitted','keys':refs,'reason':'Candidate prior semantics with exact refreshed grounds; pending LLM current-cone conservation judgment.' if refs else 'Pending bounded LLM current-source authoring or explicit source-role disposition.'})
 (WORK/(chunk['id']+'.candidate.json')).write_text(json.dumps(answer,ensure_ascii=False,indent=2)+'\n')
(WORK/'reuse-ledger.prepared.json').write_text(json.dumps(ledger,indent=2)+'\n')
print({'chunks':len(chunks),'retained_candidates':len(selected),'unselected':len(ledger)-len(selected),'reasons':dict(collections.Counter(x['reason'] for x in ledger if x['reason']))})
for chunk in chunks:
 a=answers[chunk['id']];print(chunk['id'],len(chunk['segments']),sum(len(a[f]) for f in FAMILY.values()),sum(d['decision']=='omitted' for d in a['dispositions']),sorted({s['path'].removeprefix(PREFIX) for s in chunk['segments']}))
