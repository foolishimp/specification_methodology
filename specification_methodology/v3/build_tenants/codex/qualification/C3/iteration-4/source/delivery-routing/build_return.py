"""Author scoped delivery argument routing. Writes only this return directory."""
import copy, hashlib, json, re, subprocess
from pathlib import Path
ROOT=Path('/Users/jim/src/apps/specification_methodology-codex')
BASE=ROOT/'specification_methodology/v3/build_tenants/codex'
OUT=Path(__file__).resolve().parent
ACCOUNT=BASE/'qualification/C3/iteration-4/DETERMINATIONS.json'
DIRECT=BASE/'qualification/C3/iteration-4/source/delivery/ACCOUNT_PATCH.json'
SOURCE='feac24710c843ff3bece10004b6bc5499cc84f6e'
HELD='b8c43489311b387045de129db459ef1bf29c1334724fcccc36474ea9565fedcd'
sha=lambda b:hashlib.sha256(b).hexdigest()
def canonical(o):return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def write(name,obj):(OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
account_raw=ACCOUNT.read_bytes(); assert sha(account_raw)==HELD,'held account changed'
account=json.loads(account_raw); units={u['id']:u for u in account['determinations']}
direct_raw=DIRECT.read_bytes(); direct=json.loads(direct_raw)
assert sha(direct_raw)=='84a52481f50710a06da4c77dcba1a6248b082c0485698c1fd809a46e5042fc1d'
source={}; sections={}; row_tables={}
for member,anchor in [('SPEC_METHOD','method-families'),('TICKET_METHOD','carrier-families')]:
 path='specification_methodology/v3/build_tenants/codex/successor/standards/'+member+'.md'
 raw=subprocess.check_output(['git','show',SOURCE+':'+path],cwd=ROOT)
 assert (ROOT/path).read_bytes()==raw,'source member drift'
 source[member]=raw
 heads=list(re.finditer(rb'^(#{1,6}) (.+)\n',raw,re.M)); stack=[]
 for i,h in enumerate(heads):
  title=h[2].decode().strip(); slug=re.sub(r'[^\w\s-]','',title.lower()).replace(' ','-')
  level=len(h[1]); end=heads[i+1].start() if i+1<len(heads) else len(raw)
  while stack and stack[-1][0]>=level:stack.pop()
  sections.setdefault(member+'.'+slug,{'body':raw[h.start():end],'path':'standards/'+member+'.md','anchor':slug,'ancestors':copy.deepcopy(stack),'line':raw[:h.start()].count(b'\n')+1})
  stack.append((level,slug))
 body=sections[member+'.'+anchor]['body']; rows=[]
 for lineno,line in enumerate(raw.splitlines(keepends=True),1):
  if line in body.splitlines(keepends=True) and line.startswith(b'| ['):
   cells=[v.strip() for v in line.decode().strip().strip('|').split('|')]
   assert len(cells)==4
   rows.append({'cells':cells,'line':lineno,'sha256':sha(line),'bytes':len(line),'path':'standards/'+member+'.md','anchor':anchor})
 assert len(rows)==8
 row_tables[member]=rows
WHEN='Only when assessing this family argument, its applicability, consequence, conservation, coverage or fidelity against this consumer. This is not an unconditional operational dependency.'
def provenance(path,anchor):return {'path':path,'anchor':anchor,'role':'provenance','required_when':WHEN}
OWNED=[{'path':'standards/SPEC_METHOD.md','anchor':'method-families'},{'path':'standards/TICKET_METHOD.md','anchor':'carrier-families'}]
LEGACY=['SPEC_METHOD.method-families','TICKET_METHOD.carrier-families']
def owned(f):
 r=f.get('source_row',{})
 return any(r.get('path')==x['path'] and r.get('anchor')==x['anchor'] for x in OWNED) or any(x in LEGACY for x in f.get('source_refs',[]) if isinstance(x,str))
def premises(s):
 out=set(int(x) for x in re.findall(r'F([1-6])',s))
 for a,b in re.findall(r'F([1-6])[–-]F?([1-6])',s):out.update(range(int(a),int(b)+1))
 return ['F'+str(x) for x in sorted(out)]
# Seven clauses have a specific source-supported scope; four data/locator units do not.
BINDINGS={
'SPEC_METHOD.adr-folder-convention':(3,'adr-conventions','scoped_heading_descendant','ADR Folder Convention is the child of the explicitly named ADR Conventions consumer. Apply the current row to decision ownership, retained decision support and the convention status of ADR layout. The row does not derive a mandatory adrs directory, migration, numeric ID or registry.', 'Spec chooses ADR location and filename conventions at the owning design surface. Product bindings govern actual locations; alternative tenant paths remain conformant and the registry remains optional.'),
'TICKET_METHOD.goals':(0,'core-model','scoped_heading_descendant','Goals is a Core Model child defining the epic carrier role. The family is relevant only when assessing which existing carrier retains the selected work-wave facts beyond an activation. It does not turn Goals into durable execution tracking, prescribe a physical filename or create a new goal-admission decision.', 'Ticket distinguishes the current Goals epic layer from durable execution tracking; the Product Definition locates it and GOALS.md is the default.'),
'TICKET_METHOD.comments':(0,'core-model','scoped_heading_descendant','Comments is a Core Model child defining the discussion/publication carrier role. Apply the continuation argument only to facts actually required after the local boundary and lawfully recorded there. It neither requires a new comment for every task nor grants task-status authority; Posting Guide retains publication ownership.', 'Ticket assigns comments to discussion and publication, not task-status authority. The Product Definition locates the carrier and Posting Guide owns its publication rules.'),
'TICKET_METHOD.tickets':(0,'core-model','scoped_heading_descendant','Tickets is a Core Model child that gives enduring work identity a recoverable authoritative carrier. The premise applies when work needs independent state beyond the local boundary; a ticket or particular physical file is not required for every execution.', 'Ticket chooses one enduring source of truth for the work identity. A Markdown file is the default carrier; other lawfully bound carriers remain permitted.'),
'TICKET_METHOD.sprints':(0,'core-model','scoped_heading_descendant','Sprints is a Core Model child defining a bounded batch lifetime. The family explains why surviving obligations need a carrier beyond close. It does not grant escrow, replace sprint-close review, authorize debt retention or supply constitutional authority.', 'Ticket chooses a bounded manifest and explicit close review. A sprint may contain durable tickets, local entries or both; independently surviving debt requires the lawful durable follow-up already specified.'),
'TICKET_METHOD.execution-contracts':(0,'core-model','scoped_heading_descendant','Execution Contracts is a Core Model child distinguishing one run from ticket and sprint lifetimes. The family explains selection of a surviving source carrier and recoverable run result. Admission and closure keep their separately owned conditions; contract presence supplies neither.', 'Ticket chooses one run-scoped admitted contract derived from the smallest lawful source carrier. Draft, admit and execute may share one invocation; a run contract does not become a rival backlog or planning surface.'),
'TICKET_METHOD.evaluation-criteria-and-non-closure-conditions':(5,'condition-based-closure-and-reuse','explicit_consumed_condition_surface','The named Condition-Based Closure And Reuse consumer evaluates every applicable declared obligation and absence of active non-closure conditions. This clause supplies those same evaluation_criteria and non_closure_conditions and their migration examples. The binding covers those consumed conditions, not every Ticket Rules sibling or a new acceptance requirement.', 'Ticket chooses visible evaluation criteria and non-closure conditions for the admitted contract. Spec owns path-relative residual-debt authority; debt outside the claimed acceptance path is not by itself a non-closure condition.')}
NO_FAMILY={
'TICKET_METHOD.default-layout':'This unit supplies a starter layout and locator/rebinding data. The current family table names Authority as a deciding consumer, but does not make this layout an independent family-law predicate. The default paths do not follow from F1–F6; the explicit permission to bind other resources and the governing installed-basis obligation remain unchanged.',
'TICKET_METHOD.required-fields':'This unit supplies the ticket/contract field schema, recommendation distinctions and conditional migration fields. The field names are chosen carrier policy, not a new family-law inference. Its required, recommended and conditional requirements remain intact and are consumed by the separately owned carrier/admission/migration decisions. No family argument is asserted for each schema entry.',
'TICKET_METHOD.sprint-manifest-required-fields':'This unit supplies manifest schema data and field meanings, including the explicit paydown link to Sprint Close Review. The current family argues at the named escrow/close consumers; it does not derive these literal keys or create a standalone schema acceptance decision. All required fields and their paydown binding remain unchanged.',
'TICKET_METHOD.future-extensions':'This unit lists optional future extensions and preserves the selected local-file model and existing authority/refusal laws. It is not an implementation migration or a new deciding consumer named in the current migration row. Optionality and the obligations on any selected alternative remain unchanged; no migration-family derivation or new adoption duty is assigned here.'}
IDS=['SPEC_METHOD.adr-folder-convention','TICKET_METHOD.comments','TICKET_METHOD.default-layout','TICKET_METHOD.evaluation-criteria-and-non-closure-conditions','TICKET_METHOD.execution-contracts','TICKET_METHOD.future-extensions','TICKET_METHOD.goals','TICKET_METHOD.required-fields','TICKET_METHOD.sprint-manifest-required-fields','TICKET_METHOD.sprints','TICKET_METHOD.tickets']
patches=[]; audit=[]; old_hashes=[]
for id in IDS:
 unit=units[id]; member=id.split('.')[0]; sec=sections[id]
 old_families=unit['argument']['source_family_arguments']; foreign=[copy.deepcopy(x) for x in old_families if not owned(x)]; retiring=[x for x in old_families if owned(x)]
 assert len(retiring)==1
 refresh=next(x for x in direct['dependent_argument_refresh'] if x['id']==id)
 assert refresh['new_direct_family_arguments']==[]
 old_hashes.extend(x['source_row']['sha256'] for x in retiring)
 new=[]
 if id in BINDINGS:
  number,root,kind,scope,policy=BINDINGS[id]; row=row_tables[member][number]; cells=row['cells']
  if kind=='scoped_heading_descendant':assert any(x[1]==root for x in sec['ancestors'])
  else:
   body=sections[member+'.'+root]['body']; assert b'non-closure condition' in body and b'non_closure_conditions' in sec['body']
  root_ref=provenance(sec['path'],root)
  binding={'declared_root':root_ref,'binding_kind':kind,'scope_condition':scope,'source_evidence':'Current source table explicitly names '+root+'; the exact consumer body and the owning body establish the limited relation described here.','role':'provenance','required_when':WHEN}
  new=[{'family':cells[0],'declared_consumer_scope':cells[0],'premises':premises(cells[1]),'premise_and_pillar_argument':cells[1],'conditional_consequence':cells[2],'additional_policy_and_owner':cells[3],'source_row':{k:row[k] for k in ['path','anchor','line','sha256']}|{'source_commit':SOURCE,'member_sha256':sha(source[member]),'hash_boundary':'Exact Markdown row including terminal newline.'},'source_refs':[provenance(row['path'],row['anchor'])],'required_when':WHEN,'audit_consumer_loci':[provenance(sec['path'],sec['anchor'])],'consumer_scope_bindings':[binding]}]
  app={'standing':'scoped_source_match','binding_kind':kind,'scope_condition':scope,'source_refs':[root_ref,provenance(sec['path'],sec['anchor'])],'required_when':WHEN,'operational_dependency_effect':'No change to local applicability, dependencies, admission, closure, permissions or result predicates.'}
  new_premises=premises(cells[1])
  if root=='core-model':
   # The explicit Core Model preamble retains F6 for authority even though its carrier-row lifetime argument uses F1/F3/F5.
   new_premises=sorted(set(new_premises+['F6']))
   app['local_premise_support']={'premise':'F6','source':root_ref,'reason':'The unchanged Core Model preamble explicitly adopts F1, F3, F5 and F6 and preserves Product/ticket-state authority. This local premise is retained separately from the table row.'}
  summary={'argument.premises':new_premises,'argument.conditional_consequence':cells[2]+' Scope for this unit: '+scope,'argument.policy_choices':[policy]}
 else:
  reason=NO_FAMILY[id]
  app={'standing':'no_family_law_argument_for_this_data_surface','binding_kind':'schema_locator_or_optional_extension_data','reason':reason,'source_refs':[provenance(sec['path'],sec['anchor'])],'required_when':WHEN,'operational_dependency_effect':'No decision, requirement, recommendation, permission, refusal law or consumer dependency is added or removed.'}
  summary={'argument.premises':[],'argument.conditional_consequence':reason,'argument.policy_choices':[]}
 values={'argument.source_family_arguments':foreign+new,'argument.source_family_applicability':app,**summary}
 guards={}
 for field,value in summary.items():
  key=field.split('.')[1]
  guards[field]={'held_preimage':copy.deepcopy(unit['argument'][key]),'held_preimage_canonical_sha256':sha(canonical(unit['argument'][key])),'integration_rule':'This is a stale family-derived wrapper, not a replacement for a more-specific local argument. Apply the supplied value only when the current field equals this held preimage and no foreign family contribution would be lost. Preserve any later local argument. If foreign families exist, retain their premise/policy contributions and merge the owned replacement by origin; if provenance is insufficient, retain the current field and return an explicit conflict for author review.'}
 patch={'id':id,'set':values,'scoped_replacements':{'argument.source_family_arguments':{'mode':'replace_owned_source_rows_preserving_current_other_entries','owned_source_rows':OWNED,'legacy_source_refs':LEGACY,'incoming_entries':'Use only entries in this dotted set value whose source_row path/anchor matches an owned source row. The unowned entries in the set value document the held-preimage result only.','application':'At application time, retain every current array entry outside the owned source rows (including entries added by earlier integration patches), then append the incoming owned entries in supplied order. Legacy exact source_refs naming an owned table also identify an owned entry. Do not blindly replace this array after another patch adds unowned families.','preserve_unowned_entries':True}},'generated_summary_preimages':guards,'changed_nested_fields':list(values),'preserve':'All unmentioned semantic fields, local definitions, predicates, obligations, permissions/exceptions, dependencies, source applicability, result/effect mappings, consumers and proof standing remain byte-equivalent JSON values. Only the exact obsolete family-derived summary wrapper may change under its guard.','source_binding':{'source_commit':SOURCE,'path':sec['path'],'anchor':sec['anchor'],'whole_heading_inclusive_body_sha256':sha(sec['body']),'body_bytes':len(sec['body']),'start_line':sec['line']},'direct_refresh_preimage':refresh}
 patches.append(patch)
 audit.append({'id':id,'retired_owned_family_rows':retiring,'incoming_owned_family_rows':len(new),'disposition':app['standing'],'source_owner_support':app,'local_semantics':'preserved; schema obligations and preferences are not weakened by absence of a family-law derivation'})
patch={'schema_version':'stdo.authored-semantic-fields-patch.v1','activation':'I4-DELIVERY-ACCOUNT-ROUTES','standing':'Authored account integration input; no source, account, generated artifact or independent fidelity judgment is changed by this patch.','source_commit':SOURCE,'receiving_account':{'path':'qualification/C3/iteration-4/DETERMINATIONS.json','sha256':HELD,'standing':'Parent-held provisional integration shape, not an accepted account.'},'direct_delivery_patch':{'path':'qualification/C3/iteration-4/source/delivery/ACCOUNT_PATCH.json','sha256':sha(direct_raw),'relationship':'Completes exactly the eleven named empty dependent_argument_refresh proposals; the closed direct patch remains unchanged.'},'integration':'Apply dotted set fields to the existing determination. scoped_replacements is normative for family arrays and preserves all current foreign families. Generated summaries are guarded by generated_summary_preimages; preserve later local/foreign contributions, reporting a conflict instead of blindly overwriting. Do not replace whole argument or definition objects.','acquisition':'source_refs, audit_consumer_loci, source_row, consumer_scope_bindings and applicability support are provenance. required_when limits family acquisition to the exact argument/applicability/fidelity assessment. No operational dependency or deciding predicate is added.','patches':patches,'unresolved_source_bindings':[],'source_members':[{'path':'standards/'+m+'.md','sha256':sha(b)} for m,b in source.items()],'scope_counts':{'existing_determinations':11,'scoped_current_family_bindings':7,'explicit_no_family_law_data_surfaces':4,'current_family_rows_used':3}}
write('ACCOUNT_PATCH.json',patch);write('COVERAGE.json',{'activation':patch['activation'],'standing':'author route audit; not independent fidelity evidence','source_commit':SOURCE,'rows':audit})
# In-memory checks only; no generated account or source is written.
changed=set(); hash_checks=0
for p in patches:
 before=units[p['id']]; after=copy.deepcopy(before)
 for field,value in p['set'].items(): after['argument'][field.split('.')[1]]=copy.deepcopy(value)
 for key in before:
  if key!='argument':assert after[key]==before[key]
 for key in before['argument']:
  if 'argument.'+key not in p['set']:assert after['argument'][key]==before['argument'][key]
 for f in after['argument']['source_family_arguments']:
  if owned(f):
   r=f['source_row']; raw=source[Path(r['path']).stem].splitlines(keepends=True)[r['line']-1]
   assert sha(raw)==r['sha256']; assert r['sha256'] not in old_hashes; assert f['required_when']==WHEN; hash_checks+=1
   assert all(x['role']=='provenance' for x in f['source_refs'])
 # Deliberately inject a foreign family and verify the normative replacement preserves it.
 foreign_probe={'family':'foreign-family-preservation-probe','premises':['F2'],'source_row':{'path':'standards/FOUNDATIONS.md','anchor':'core-contract-derivations','sha256':'probe'}}
 current=copy.deepcopy(before['argument']['source_family_arguments'])+[foreign_probe]
 incoming=[x for x in p['set']['argument.source_family_arguments'] if owned(x)]
 merged=[x for x in current if not owned(x)]+incoming
 assert foreign_probe in merged and all(x not in merged for x in current if owned(x))
 changed.add(p['id'])
assert changed==set(IDS);assert hash_checks==7
assert sha(ACCOUNT.read_bytes())==HELD and DIRECT.read_bytes()==direct_raw
checks={'activation':patch['activation'],'standing':'author mechanical checks; not independent semantic acceptance','checks':{'exact_held_account_preimage':True,'eleven_empty_direct_refresh_proposals_bound':True,'current_row_hashes_verified':hash_checks,'retired_coarse_hashes_removed_from_current_incoming_entries':True,'all_non_argument_semantics_preserved':True,'more_specific_local_argument_and_foreign_summary_guards_present':True,'foreign_current_family_preservation_probe_passes':11,'no_new_mandatory_acquisition':True,'all_incoming_family_refs_marked_provenance_and_conditional':True,'four_no_family_rationales_preserve_schema_and_optional_policy':True,'source_and_held_account_and_closed_direct_return_unchanged':True},'remaining_work':['Parent integrates guarded dotted fields and scoped replacements.','Parent checks any wrapper conflict against later local or foreign contributions rather than overwriting it.','Independent readback assesses actual scope support and integrated interpretation/fidelity; author checks supply no acceptance.']}
write('CHECKS.json',checks)
for name in ['ACCOUNT_PATCH.json','COVERAGE.json','CHECKS.json']:
 p=OUT/name;print(name,len(p.read_bytes()),sha(p.read_bytes()))
