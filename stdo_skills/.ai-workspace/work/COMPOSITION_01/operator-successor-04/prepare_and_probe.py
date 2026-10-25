"""One selected real T-002 read/context activation; no dispatch or work grant."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import sys

REPO=Path(__file__).resolve().parents[5]
SKILLS=REPO/'stdo_skills'
TOOL=REPO/'a_c'
OUT=Path(__file__).resolve().parent
WORK=OUT.parent

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text())
def save(p,value):
    if p.exists(): raise RuntimeError('Preserve prior artifact: '+str(p))
    p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def ref(root,path):
    base={'product':SKILLS,'tool':TOOL}[root]
    return {'engine':'workspace-regular-file','root':root,'path':path,'object':None,'sha256':sha(base/path),'selector':None}

provider_path=REPO/'a_c/.ai-workspace/work/PRODUCT_COMPOSITION_01/source-freeze-04.json'
manager_path=REPO/'specification_methodology/v3/.ai-workspace/work/PRODUCT_COMPOSITION_IMPLEMENTATION_01/manager/CANDIDATE-repair1.json'
provider=load(provider_path);manager=load(manager_path)
for path,expected in provider['files'].items(): assert sha(REPO/path)==expected,path
for row in manager['files']: assert sha(REPO/row['path'])==row['sha256'],row['path']
production=load(REPO/'a_c/.ai-workspace/work/PRODUCT_COMPOSITION_01/provider-files-04.json')
for path,expected in production['files'].items(): assert sha(REPO/path)==expected,path
selected=set(production['files'])|{row['path'] for row in manager['files'] if '/tests/' not in row['path']}
selected.update(str(p.relative_to(REPO)) for p in (REPO/'specification_methodology/v2/src/stdo_toolchain').glob('*.py'))
selected.update('a_c/'+p for p in ['stdo_a_c.json','specification/requirements/fd-stdo-3.0.1-binding.md','build_tenants/graphify/code/ac_graph.py','build_tenants/graphify/design/fd-method-stdo-3.0.1.json','build_tenants/graphify/design/fd-support.md','build_tenants/graphify/design/fd-support-stdo-3.0.1.md'])
manifest={'schema':'stdo-skills.selected-support-sources/1','standing':'Selected development source bytes for T-002 construction; no Product or release acceptance','repository_base_head':'0ec4b6c94f6255f6057416fec9d4c77feddf1b06','path_base':'repository containing the sibling stdo_skills and a_c Products; paths are not acquisition grants','consumer_basis':{'uri':'stdo://releases/v3.0.1-rc.1/','manifest_sha256':'60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8'},'provider_builder':'stdo://releases/v2.5.1-rc.2/','native_profile':'urn:a-c:fd-support:method:stdo-3.0.1-rc.1:executive:1','provider_freeze':{'path':str(provider_path.relative_to(REPO)),'sha256':sha(provider_path)},'manager_freeze':{'path':str(manager_path.relative_to(REPO)),'sha256':sha(manager_path)},'runtime':{'interpreter':str(Path(sys.executable).resolve()),'interpreter_sha256':sha(Path(sys.executable).resolve()),'python':sys.version},'files':[{'path':p,'sha256':sha(REPO/p),'bytes':(REPO/p).stat().st_size} for p in sorted(selected)],'limits':['Native results.conjoin unsupported.','Global installed manager remains unchanged; select this source invocation explicitly.','Installed 3.0.1 remains the consumer method; mutable successor standards are not a dependency.','No OS confinement, complete actor-knowledge or solved Claude Q05 claim.']}
manifest['qualification_sources']='Provider and manager freeze records retain their test-source subjects separately; files above are runtime/contract dependencies.'
manifest_path=SKILLS/'specification/composition/SOURCE_MANIFEST.json'
history=load(WORK/'HISTORY-freeze02.json')
expected=next(row['sha256'] for row in history['files'] if row['path']=='stdo_skills/specification/composition/SOURCE_MANIFEST.json')
assert sha(manifest_path)==expected,'Current manifest changed since archived operation02'
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
owner=load(OUT/'OWNER.json')
owner['authority_sources'][1]=ref('product','.ai-workspace/work/COMPOSITION_01/operator-successor-04/OPERATOR_SELECTION.md')
owner['mechanism']['source']=ref('tool','build_tenants/graphify/code/ac_support_core.py')
owner['mechanism']['implementation_sha256']=owner['mechanism']['source']['sha256']
(OUT/'OWNER.json').write_text(json.dumps(owner,indent=2)+'\n')
owner_ref=ref('product','.ai-workspace/work/COMPOSITION_01/operator-successor-04/OWNER.json')
selection_ref=ref('product','.ai-workspace/work/COMPOSITION_01/operator-successor-04/OPERATOR_SELECTION.md')
return_contract={'schema':'a_c.fd-support.return-contract/1','id':'urn:stdo-skills:T002:read-context-return:1','authority_source':owner_ref,'carrier':'a_c.fd-support.closed-return/1','output_slot':'final_stdout_object','required_evaluations':[],'role':'Worker','proof':{'transition_sources':[selection_ref],'predicate_ids':[]}}
save(OUT/'RETURN_CONTRACT.json',return_contract)
definition=load(SKILLS/'stdo_skills.json')
assert definition['reference_frame_bases'][0]['authority'][1]=='./.ai-workspace/work/COMPOSITION_01/operator/OWNER.json'
definition['reference_frame_bases'][0]['authority'][1]='./.ai-workspace/work/COMPOSITION_01/operator-successor-04/OWNER.json'
(SKILLS/'stdo_skills.json').write_text(json.dumps(definition,indent=2)+'\n')
product_id=definition['product']['definition_id'];provider_id='urn:stdo:product-definition:a-c-implementations'
refs={
 'definition':ref('product','stdo_skills.json'),
 'owner':owner_ref,'selection':selection_ref,
 'ticket':ref('product','.ai-workspace/tickets/active/T-002-composition-support.md'),
 'frame':ref('product','specification/REFERENCE_FRAME_BASIS.md'),
 'requirements':ref('product','specification/requirements/README.md'),
 'return':ref('product','.ai-workspace/work/COMPOSITION_01/operator-successor-04/RETURN_CONTRACT.json'),
 'relation':ref('product','specification/composition/A_C_SUPPORT.md'),
 'manifest':ref('product','specification/composition/SOURCE_MANIFEST.json'),
 'provider-definition':ref('tool','stdo_a_c.json'),
 'profile':ref('tool','build_tenants/graphify/design/fd-method-stdo-3.0.1.json'),
 'mechanism':ref('tool','build_tenants/graphify/code/ac_support_core.py'),
 'requirements-native':ref('tool','specification/requirements/fd-stdo-3.0.1-binding.md'),
 'support-native':ref('tool','build_tenants/graphify/design/fd-support-stdo-3.0.1.md'),
 'support':ref('tool','build_tenants/graphify/design/fd-support.md'),
 'composition':ref('tool','build_tenants/graphify/design/fd-composition.md'),
 'outside-selection':ref('tool','specification/GOALS.md'),
}
prior=load(WORK/'operator/COMPOSITION.json')
resources=json.loads(json.dumps(prior['resources']))
allowed=list(prior['bindings']['writer']['allow'])
for key,source in refs.items():
    current=key if key in resources and resources[key]['source']==source else key+'-04'
    resources[current]={'source':source,'owner':product_id if source['root']=='product' else provider_id,'complete':False,'parents':[]}
    if key!='outside-selection' and current not in allowed: allowed.append(current)
operations=['tools.describe','composition.inspect','source.read','context.assemble']
actor='/root/composition_proposal_writer'
binding={'engagement':'urn:stdo-skills:T002:composition-proof:2','purpose':'Actual current Writer acquiring selected Skills support and constructing its bounded read-only Context','route':['skills-ac-support'],'operations':operations,'allow':allowed,'exclude':[],'exports':[],'require_complete':False,'clean_room':False,'host_isolation':False,'output':{'complete':False,'sources':[]}}
declaration={'schema':'a_c.fd-support.composition/1','id':'urn:stdo-skills:T002:composition-binding:2','authority_sources':[owner_ref,selection_ref],'edges':{'skills-ac-support':{'source_definition':refs['definition'],'source_id':product_id,'index':0,'target_definition':refs['provider-definition'],'target_id':provider_id,'relation':refs['relation'],'contracts':[refs[k] for k in ('requirements-native','support-native','support','composition','manifest')]}},'resources':resources,'bindings':{'writer':binding}}
save(OUT/'COMPOSITION.json',declaration)
sources={root:{'path':str(base),'kind':'workspace','writable':False,'read_scope':[{'path':p,'kind':'file'} for p in sorted({v['source']['path'] for v in resources.values() if v['source']['root']==root}|({'.ai-workspace/work/COMPOSITION_01/operator-successor-04/COMPOSITION.json','.ai-workspace/work/COMPOSITION_01/operator-successor-04/COMPOSITION-strict.json'} if root=='product' else set()))]} for root,base in [('product',SKILLS),('tool',TOOL)]}
policy={'schema':'a_c.fd-support.policy/1','id':'urn:stdo-skills:T002:native-read-context:2','product':{'definition_id':product_id,'definition':refs['definition'],'authority_binding':{'definition_locator':'/reference_frame_bases/0/authority/1','owner_record':owner_ref,'mechanism':owner['mechanism'],'result_surface':owner['result_surface'],'scope':owner['scope']}},'method_profile':{'id':'urn:a-c:fd-support:method:stdo-3.0.1-rc.1:executive:1','sha256':refs['profile']['sha256'],'source':refs['profile']},'sources':sources,'principals':{'writer':{'actor_id':actor,'role':'Worker','family':'Codex','authorship':'Actual current separately delegated Writer; no nested actor','operations':operations,'role_binding':selection_ref,'role_transition':None}},'grants':{},'predicates':{},'operators':{},'executors':{},'event_sinks':{},'independence_policy':None,'evidence_root':owner['result_surface']['root'],'limits':{'max_message_bytes':8000000,'max_files':1000,'max_bytes':16000000,'max_history_records':10000,'max_wait_ms':1000},'authority_sources':[owner_ref,selection_ref],'composition':ref('product','.ai-workspace/work/COMPOSITION_01/operator-successor-04/COMPOSITION.json')}
save(OUT/'POLICY.json',policy)
subject={'id':'urn:stdo-skills:T002:source-selection','sha256':refs['manifest']['sha256']}
packet={'activation':{'id':'urn:stdo-skills:T002:read-context:2','revision':'2','configuration':selection_ref},'frame':{'id':'urn:stdo-skills:T002:read-context-frame','revision':'2','declaration':refs['frame'],'evaluation':selection_ref,'result_algebra':refs['frame']},'subject_basis':{'subject':subject,'method_profile':{k:policy['method_profile'][k] for k in ('id','sha256')},'product':{'id':product_id,'definition':refs['definition']},'observations':[],'dependencies':[refs['relation'],refs['manifest'],refs['composition']],'time_basis':'Exact local development source selection; no currentness inference from the base commit'},'attention':{'material_relations':[refs['relation']],'invariants':[selection_ref],'semantic_sources':[refs['requirements'],refs['composition']],'exclusions':[],'prohibited_assumptions':['Prior actor knowledge is not fully recorded.','No acceptance, dispatch, write or isolation authority follows from this Context.']},'actor_authority':{'actor_id':actor,'role':'Worker','capability':selection_ref,'semantic':None,'evaluation':None,'operation':owner_ref,'decision':None,'acceptance':None,'publication':None,'territory':[],'tools':operations},'evidence_relations':{'admissible_evidence':[owner_ref],'acquisition':[selection_ref],'dependencies':[refs['manifest']],'conjunction':None,'translation':None,'consumer':'/root','return_contract':refs['return']},'stop_change':{'invalidators':['Selected source or mechanism changed'],'stop_conditions':['Missing required authority or deciding source'],'residuals':['Prior actor context and complete output provenance unknown'],'re_entry':['Preserve original evidence and select affected current sources'],'reconfiguration':[]},'profile_additions':{'worker':{'operation_grant_id':owner['id'],'mutation_subject':subject,'territory':[]}}}
save(OUT/'PACKET.json',packet)
checks=[]
def call(name,operation,arguments,policy_file,expect):
 folder=OUT/'calls'/name;folder.mkdir(parents=True)
 request={'schema':'a_c.fd-support.request/1','id':'t002-04-'+name,'operation':operation,'arguments':arguments}
 save(folder/'request.json',request)
 argv=[sys.executable,'-B',str(TOOL/'build_tenants/graphify/code/ac_support.py'),'--policy',str(policy_file),'--policy-sha256',sha(policy_file),'--principal','writer','call','--request',str(folder/'request.json')]
 run=subprocess.run(argv,capture_output=True,text=True,timeout=30,cwd=SKILLS)
 (folder/'stdout.json').write_text(run.stdout);(folder/'stderr.txt').write_text(run.stderr)
 response=json.loads(run.stdout);entry={'name':name,'operation':operation,'argv':argv,'exit':run.returncode,'status':response['status'],'evidence':response.get('evidence'),'expected':expect,'refusal':response.get('refusal')}
 save(folder/'EXECUTION.json',entry);checks.append(entry)
 assert response['status']==expect,entry
 return response
call('describe','tools.describe',{},OUT/'POLICY.json','ok')
call('inspect','composition.inspect',{},OUT/'POLICY.json','ok')
call('read-contract','source.read',{'source':refs['composition'],'encoding':'utf8'},OUT/'POLICY.json','ok')
call('denied-outside-selection','source.read',{'source':refs['outside-selection'],'encoding':'utf8'},OUT/'POLICY.json','refused')
arguments={'packet':packet,'models':[],'sources':[],'late_acquisition':[],'envelope':{'capacity_bytes':None,'boundary':'executor-stdin-utf8','host_context':{'state':'unknown','bytes':None,'evidence':None}}}
context=call('ordinary-context','context.assemble',arguments,OUT/'POLICY.json','ok')
assert context['result']['value']['boundaries']['declared_input_provenance_complete'] is False
strict=json.loads(json.dumps(declaration));strict['id']='urn:stdo-skills:T002:composition-binding:strict';strict['bindings']['writer']['require_complete']=True
save(OUT/'COMPOSITION-strict.json',strict)
strict_policy=json.loads(json.dumps(policy));strict_policy['id']='urn:stdo-skills:T002:native-read-context:strict';strict_policy['composition']=ref('product','.ai-workspace/work/COMPOSITION_01/operator-successor-04/COMPOSITION-strict.json')
save(OUT/'POLICY-strict.json',strict_policy)
call('strict-context','context.assemble',arguments,OUT/'POLICY-strict.json','refused')
save(OUT/'CHECKS.json',{'status':'passed bounded actual public operations','source_manifest_sha256':refs['manifest']['sha256'],'checks':checks,'ordinary_context_boundaries':context['result']['value']['boundaries'],'actor':actor,'dispatches':0,'executors':0,'effect_grants':0,'claims':'Actual local native inspect/read/context and refusal paths only; no semantic adequacy, independent review, clean-room or host qualification.'})
print(json.dumps({'status':'passed','operations':len(checks),'ordinary_context_unknown_provenance_retained':True,'evidence':str(OUT/'CHECKS.json')}))
