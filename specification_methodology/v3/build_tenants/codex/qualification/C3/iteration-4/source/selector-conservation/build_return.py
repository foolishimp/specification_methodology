"""Construct an author proposal only; never write source or current conservation."""
import copy, hashlib, json, re, subprocess
from pathlib import Path
ROOT=Path('/Users/jim/src/apps/specification_methodology-codex')
BASE='specification_methodology/v3/build_tenants/codex/'
OUT=ROOT/BASE/'qualification/C3/iteration-4/source/selector-conservation'
OLD='199c6d29bc02590a8b7f252043fc43223c09808d'
COMMON='3c4c503d291e7cb19ba21333ba6caf6167be77c9'
CURRENT='0db93e415060dbc7beac9857edbb49c44b7ab04f'
KEY='IDENTITY_METHOD.md#release-version-boundary'
sha=lambda b:hashlib.sha256(b).hexdigest()
def frozen(commit,path): return subprocess.check_output(['git','show',commit+':'+path],cwd=ROOT)
def canonical(o): return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def write(name,o): (OUT/name).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def section(raw,anchor):
 matches=list(re.finditer(rb'^#{1,6} (.+)\n',raw,re.M))
 for i,m in enumerate(matches):
  label=m.group(1).decode().strip().lower()
  slug=re.sub(r'[^\w\s-]','',label).replace(' ','-')
  if '#'+slug==anchor:
   end=matches[i+1].start() if i+1<len(matches) else len(raw)
   return raw[m.start():end], {'start_line':raw[:m.start()].count(b'\n')+1,'end_line':raw[:end].count(b'\n')}
 raise ValueError(anchor)
old_path=BASE+'qualification/C3/iteration-3/CONSERVATION.json'
old_bytes=frozen(OLD,old_path)
old=json.loads(old_bytes)
original=next(x for x in old['rows'] if x['id']==KEY)
assert original['disposition']=='conserved'
common_path='specification_methodology/v3/specification/requirements/PREDECESSOR_CLAIMS.md'
common=frozen(COMMON,common_path)
common_row=next(x for x in common.decode().splitlines() if x.startswith('| Release Version Boundary |') and 'latest-accepted' in x)
installed=Path('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2')
predecessor=(installed/'standards/IDENTITY_METHOD.md').read_bytes()
predecessor_body,_=section(predecessor,'#release-version-boundary')
assert sha(predecessor_body)=='fb43da187d10d07b00f100b906762057e90977ab65858359bf642c6d8e8a8bce'
replacement_loci=['standards/IDENTITY_METHOD.md#release-version-boundary','standards/RELEASE_METHOD.md#release-identities','standards/RELEASE_METHOD.md#selector-and-consumer-adoption']
all_loci=list(dict.fromkeys(original['successor_loci']+replacement_loci))
pins={}
for route in all_loci:
 member,anchor=route.split('#',1)
 raw=frozen(CURRENT,BASE+'successor/'+member)
 body,lines=section(raw,'#'+anchor)
 pins[route]={'source_commit':CURRENT,'member_sha256':sha(raw),'body_sha256':sha(body),'bytes':len(body),'hash_scope':'whole heading inclusive through the byte before the next heading of any level',**lines}
 assert (ROOT/BASE/'successor'/member).read_bytes()==raw, 'current owner drift: '+member
assert pins[replacement_loci[0]]['body_sha256']=='10a881e60c38299128fad514d07e91a9ef9d2d87fb2d06b339dcf8d98eb5498e'
reason=('The predecessor Identity section projects the mutable version selector as latest-accepted, while its cited Release owner already requires highest-ordinal published RC independently of acceptance. On the same project/version case with accepted rc.1 and published unaccepted rc.2, the local predecessor projection selects rc.1 and the corrected projection selects rc.2. The predecessor sources are internally contradictory; this is not a claim that their combined law coherently required rc.1. Correcting the contradictory projection changes the Identity determination and cannot be carried as conserved by a fresh pin. Canonical Release policy and consumer adoption remain unchanged.')
replacement=('The Identity boundary derives mutable v<version> selection from Release Identities and Selector And Consumer Adoption: select the highest-ordinal published immutable RC for the project/version line independently of acceptance. Selector movement does not change the consumer exact operative basis; its governing authority must explicitly adopt another cut.')
row=copy.deepcopy(original)
row.update(disposition='superseded',disposition_standing='author_proposal',acceptance='owner_decision_and_current_independent_review_pending',reason=reason,successor_loci=all_loci,successor_sha256=pins[replacement_loci[0]]['member_sha256'])
row['successor_relation']={'id':'I4-SELECTOR-CONSERVATION-R001','predecessor_claim_id':KEY,'changed_meaning':reason,'replacement_determination':replacement,'replacement_loci':replacement_loci,'standing':'proposed_pending_owner_decision','owner_decision':None,'remaining_condition':'Product owner recorded acceptance of this named replacement relation and independent semantic assessment of the frozen candidate are required before dependent member acceptance.'}
row['semantic_review']={'result':'indeterminate','scope':'Bounded author same-case comparison rejects unqualified conservation of the local selector projection; proposed supersession and complete carrying relation await independent assessment and owner decision.','remaining_obligations':['Independent review must assess the exact predecessor contradiction, modal force, triggers, exceptions, canonical owner, and complete replacement carrying relation.','Product owner must record a decision accepting or rejecting I4-SELECTOR-CONSERVATION-R001 under Construction Authority.','Dependent Identity member acceptance and integrated C3 qualification cannot treat this proposed row or refreshed hashes as accepted conservation.']}
row['author_comparison']={'predecessor_basis':'v2.5.1-rc.2','candidate_assessed_commit':CURRENT,'candidate_locus':replacement_loci[0],'granularity':'inventory section ends at next heading of any level; whole heading included in reported body hashes','predecessor_section_sha256':sha(predecessor_body),'candidate_section_sha256':pins[replacement_loci[0]]['body_sha256'],'predecessor_section_bytes':len(predecessor_body),'candidate_section_bytes':pins[replacement_loci[0]]['bytes'],'local_bytes_equal':False,'meaning_assessment':reason,'standing':'bounded_author_assessment_not_independent_acceptance'}
row['author_comparison_history']=copy.deepcopy(original.get('author_comparison_history',[]))
if original.get('author_comparison'): row['author_comparison_history'].append(copy.deepcopy(original['author_comparison']))
row['disposition_history']=copy.deepcopy(original.get('disposition_history',[]))+[{'source_commit':OLD,'account_path':old_path,'standing':'historical_author_proposal_preserved_not_current_acceptance','row':copy.deepcopy(original)}]
row['shared_replacement_dependencies']=copy.deepcopy(original.get('shared_replacement_dependencies',[]))
row['replacement_owner_dependencies']=[{'locus':x,'standing':'existing canonical owner retained; no Release policy change proposed','acquire_when':'evaluating this selector replacement or its applicability'} for x in replacement_loci[1:]]
row['review_repair']={'activation':'I4-SELECTOR-CONSERVATION','document_source_commit':CURRENT,'inspection_population':'single inherited Identity release-version-boundary claim and necessary canonical Release owners','assessment':reason,'carrying_condition':'Acquire these loci where material to this claim and selected selector/adoption operation; provenance route membership creates no new general acquisition or authority.'}
patch={'schema_version':1,'kind':'proposed_conservation_row_amendment','activation':'I4-SELECTOR-CONSERVATION','standing':'author_proposal_owner_decision_pending','source_commit':CURRENT,'common_input_commit':COMMON,'account_preimage':{'commit':OLD,'path':old_path,'sha256':sha(old_bytes)},'claim_id':KEY,'preconditions':{'original_row_canonical_sha256':sha(canonical(original)),'claim_identity_and_source_coordinates_must_be_unchanged':True,'expected_old_disposition':'conserved'},'original_row':original,'proposed_row':row,'apply_contract':{'target':'iteration-4/tools/carry_conservation.py in-memory rows copied from exact I3 account','operation':'Replace only the matching row after validating the expected original row canonical hash and identity, before successor-locus pinning, changed-locus computation, frontier generation, and replacement-question grouping.','script_change_required':'The current carry script has no patch-input parameter; the integrating owner must explicitly add this guarded application or equivalent input handling. This return does not modify or run it.','preserve':'Retain all 691 claim IDs, common source coordinates, original evidence, historical rows and all unrelated row fields. Include new Release routes in successor_loci for pinning and changed-locus review.','standing':'The proposed_row disposition is a construction proposal, not an accepted classification. Do not convert owner_decision:null or review pending into acceptance.','new_source_guard':'If candidate source changes, re-assess and repin; the named frozen comparison is not automatically applicable.'},'canonical_json_hash_format':'UTF-8 json.dumps(sort_keys=True,separators=(comma,colon),ensure_ascii=False), no trailing newline','replacement_locus_pins':pins,'preserved_determinations':['Immutable v<version>-rc.<n> cut identities remain separate from mutable version selectors.','Version remains a release process fact rather than object identity.','Path and ordinary reference equality remain governed by object identity and authority law.','Consumer adoption remains explicit, separate from publication and selector movement.'],'permitted_change_explanation':'The source repair authorization permits constructing a consistent candidate under the unchanged canonical Release owner. It does not accept a changed predecessor determination. Same-case modal comparison requires the explicit proposed replacement relation; Product owner acceptance remains reserved.','dependent_acceptance':['Identity member semantic acceptance for this predecessor claim','Any C3 integrated qualification or later acceptance whose sufficiency relies on this claim'],'owner_decision':{'authority':'Product owner under common Construction Authority','status':'pending','record':None,'decision_needed':'Accept or reject the named replacement of the contradictory latest-accepted Identity projection by the existing Release selector law.'}}
patch['accepted_disposition']=None
patch['accepted_coverage']='unresolved pending Product owner decision and independent assessment; superseded is the author proposal only'
write('ROW_AMENDMENT.json',patch)
write('EVIDENCE.json',{'source_commit':CURRENT,'common_input_commit':COMMON,'frozen_common_claim':{'path':common_path,'row':common_row,'standing':'historical Claude tenant report only; supplies neither Codex disposition nor acceptance'},'predecessor':{'release':'v2.5.1-rc.2','manifest_sha256':'3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782','member':'standards/IDENTITY_METHOD.md','member_sha256':sha(predecessor),'body_sha256':sha(predecessor_body),'bytes':len(predecessor_body)},'counterexample':{'kind':'hypothetical author comparison case, not observed publication or independent test','fixed_case':{'project':'same project','version_line':'same version line','rc1':'published and accepted','rc2':'published with higher ordinal; not accepted','consumer_basis':'exact rc.1'},'predecessor_local_identity_projection':'v<version> selects rc.1','predecessor_canonical_release_owner':'v<version> selects rc.2','corrected_identity_and_release':'v<version> selects rc.2','consumer_basis_after_selector_movement':'exact rc.1 until explicit adoption','conclusion':'Local Identity determination changes on the same case; unqualified conservation is not established. Proposed supersession resolves the contradiction without changing canonical Release law.'},'replacement_locus_pins':pins})
assert row['id']==original['id'] and row['source_member']==original['source_member'] and row['source_anchor']==original['source_anchor']
assert all(x in row['successor_loci'] for x in row['successor_relation']['replacement_loci'])
assert row['successor_relation']['owner_decision'] is None
assert (ROOT/old_path).read_bytes()==old_bytes,'I3 historical account changed'
write('CHECKS.json',{'standing':'author mechanical checks; not independent semantic acceptance','source_commit':CURRENT,'checks':{'exact_original_claim_and_coordinates_preserved':True,'historical_row_and_evidence_preserved':True,'all_replacement_routes_resolve':True,'whole_heading_inclusive_hashes':True,'candidate_owner_bytes_match_frozen_source':True,'I3_account_unchanged':True,'owner_decision_pending':True,'current_conservation_not_written':True,'source_not_written':True,'all_writes_limited_to_new_return_directory':True},'remaining_work':patch['proposed_row']['semantic_review']['remaining_obligations']})
for name in ['ROW_AMENDMENT.json','EVIDENCE.json','CHECKS.json']:
 p=OUT/name; print(name,len(p.read_bytes()),sha(p.read_bytes()))
