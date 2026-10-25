"""One exact read-only Codex MCP capability control; preparation only."""
import copy, hashlib, importlib.util, json, subprocess, sys, urllib.request
from pathlib import Path
HERE=Path(__file__).resolve().parent
REVIEW=HERE.parent
PRODUCT=REVIEW.parents[3]
REPO=PRODUCT.parent
PREVIOUS=REVIEW.parent/'operator/successor-1'
CONTROL=HERE/'mcp-capability-3'
spec=importlib.util.spec_from_file_location('q05_previous',PREVIOUS/'prepare.py')
old=importlib.util.module_from_spec(spec);sys.modules[spec.name]=old;spec.loader.exec_module(old)
save,sha,pin=old.save,old.sha,old.pin
if CONTROL.exists():raise RuntimeError('Preserve prior capability control')
CONTROL.mkdir();(CONTROL/'workspace').mkdir();(CONTROL/'tmp').mkdir()
base=json.loads((PREVIOUS/'executive-policy.json').read_text())
base['sources']['control']={'path':str(CONTROL),'kind':'workspace','writable':False,'read_scope':[{'path':name,'kind':'directory' if name in ('actor-output','docs') else 'file'} for name in ['TASK.md','MCP-POLICY.json','actor-plan.json','ordinary-prompt.txt','launch.json','RETURN-CONTRACT.json','executive-policy.json','SOURCE-NOTES.json','actor-output','docs']]}
for root in base['sources'].values():root['writable']=False
def ref(root,path,selector=None):
 return {'engine':'workspace-regular-file','root':root,'path':path,'object':None,'sha256':sha(Path(base['sources'][root]['path'])/path),'selector':selector}
docs=[]
for name,url in [('official-mcp.md','https://learn.chatgpt.com/docs/extend/mcp.md'),('official-config.md','https://learn.chatgpt.com/docs/config-file/config-reference.md')]:
 raw=(HERE/'mcp-capability-2/docs'/name).read_bytes()
 path=CONTROL/'docs'/name;path.parent.mkdir(exist_ok=True);path.write_bytes(raw)
 docs.append({'url':url,**pin(path)})
save(CONTROL/'SOURCE-NOTES.json',{'selected_by':'Root explicitly selected one read-only MCP capability control before Q05; dispatch remains unselected','source_docs':docs,'host':pin(Path(json.loads((PREVIOUS/'codex/actor-plan.json').read_text())['executable']['path'])),'known_prior':'Original Codex ordinary/recovery MCP calls refused under never; no successful current MCP assumption','local_readback':'Actual previous control ignored the quoted dotted CLI key before refusing MCP approval. Local features-list probes accept valid table-valued override and reject an invalid enum in that exact field; this establishes parsing only.', 'parser_controls':pin(HERE/'mcp-capability-2/config-recognition-1/RESULT.json'), 'predecessor_result':pin(HERE/'mcp-capability-2/CONTROL-RESULT.json'),'control_change':'Recognized table-valued CLI form for per-tool tools.describe approval_mode=approve only, with policy operations=[tools.describe] and enabled_tools=[tools.describe]. No default server approval, network enablement, sandbox bypass, global config or model override.','claim':'Observe one actual MCP metadata call or its refusal; no dispatch capability or Q05 qualification inferred'})
save(CONTROL/'TASK.md','''# Read-only Codex MCP capability control

Root explicitly selected preparation of one minimal current-host MCP control.
Actual launch is selected separately from this readiness. The only host tool
operation authorized is a_c tools.describe, once. It may describe dispatch.start
metadata but cannot dispatch: the MCP policy exposes and permits only tools.describe.
No files, source/candidate bytes, credentials, shell, model delegation, Git or
global configuration may be changed. Native tool evidence and pinned physical
capture are the only declared record effects. The configured model and effort,
workspace-write sandbox and inherited global approval policy remain unchanged.
Per-tool approval_mode=approve is selected for this read-only metadata operation
only; no broad server approval is installed. Retain a refusal as the control result.
The fixed launcher reports physical observations, never semantic MCP success.
''')
task=ref('control','TASK.md')
identity='urn:stdo-skills:T001:q05:mcp-capability:2'
probe={'actor_id':identity+':host','role':'Worker','family':'openai-codex','authorship':'Actual current native Codex MCP read-only capability control; resolved model remains raw','operations':['tools.describe'],'role_binding':task,'role_transition':None}
mcp=copy.deepcopy(base);mcp.update({'id':identity+':mcp-policy','principals':{'probe':probe},'grants':{},'executors':{},'event_sinks':{},'predicates':{},'operators':{},'independence_policy':None})
mcp['authority_sources']=base['authority_sources']+[task]
save(CONTROL/'MCP-POLICY.json',mcp)
prompt='Call the exposed stdo_q05_probe tools.describe MCP tool exactly once with this full envelope: '+json.dumps({'schema':'a_c.fd-support.request/1','id':'q05-codex-mcp-control-describe-2','operation':'tools.describe','arguments':{'operation':'dispatch.start'}})+'. Do not use shell, source reads or any other tool. If unavailable or refused, report that exact fact and stop; no retry or bypass. Otherwise report that a structured tools.describe response arrived and quote its status. This is a read-only host capability control, not permission to dispatch anything.'
save(CONTROL/'ordinary-prompt.txt',prompt+'\n')
plan=json.loads((PREVIOUS/'codex/actor-plan.json').read_text())
mcp_args=['-B',str(old.CLI),'--policy',str(CONTROL/'MCP-POLICY.json'),'--policy-sha256',sha(CONTROL/'MCP-POLICY.json'),'--principal','probe','mcp']
plan.update({'id':identity+':host-plan','cwd':str(CONTROL/'workspace'),'evidence_directory':str(CONTROL/'actor-output')})
plan['argv']=[plan['executable']['path'],'exec','--json','--color','never','--sandbox','workspace-write','--skip-git-repo-check','--cd',str(CONTROL/'workspace'),'-c','mcp_servers.stdo_q05_probe.command='+json.dumps(str(old.PYTHON)),'-c','mcp_servers.stdo_q05_probe.args='+json.dumps(mcp_args),'-c','mcp_servers.stdo_q05_probe.enabled_tools=["tools.describe"]','-c','mcp_servers.stdo_q05_probe.tools={"tools.describe"={approval_mode="approve"}}','-']
plan['dependencies']=[x for x in plan['dependencies'] if Path(x['path']).is_relative_to(old.TOOL)]+[pin(CONTROL/'MCP-POLICY.json')]
plan['limits'].update({'timeout_ms':120000,'max_output_bytes':524288})
plan['environment']['TMPDIR']=str(CONTROL/'tmp')
plan['settings'].update({'host_scope':'One tools.describe MCP metadata operation only; no shell/candidate/credential/global mutation','control':'read-only per-tool binding probe; no inferred Q05 dispatch support'})
save(CONTROL/'actor-plan.json',plan)
actor={'id':identity+':physical-launcher','family':'fixed-local-qualification-executor','authorship':'Existing pinned projection/capture executable; not a semantic host result'}
launch_path=REVIEW.parent/'qualification/launch_fixture.py'
config={'schema':'stdo_skills.qualification-launch/1','transport':pin(old.ADAPTER),'actor_plan':pin(CONTROL/'actor-plan.json'),'ordinary_prompt':pin(CONTROL/'ordinary-prompt.txt'),'max_outer_bytes':4194304,'activation_id':identity+':launch','case':'q05-codex-mcp-readonly-capability-2','package':{'kind':'no skill package, isolated metadata capability control'},'return_actor':actor}
save(CONTROL/'launch.json',config)
root=copy.deepcopy(base);root['id']=identity+':root-policy';root['authority_sources']=base['authority_sources']+[task]
root['principals']={'executive':copy.deepcopy(base['principals']['executive']),'launcher':{'actor_id':actor['id'],'role':'Worker','family':actor['family'],'authorship':actor['authorship'],'operations':['tools.describe'],'role_binding':task,'role_transition':None}}
root['principals']['executive']['role_binding']=task
root['sources']['fixture_code']={'path':str(launch_path.parent),'kind':'workspace','writable':False,'read_scope':[{'path':'launch_fixture.py','kind':'file'}]}
authority=root['product']['authority_binding'];tools=['native-host-readonly-capability','a_c.tools.describe']
executor={'id':'mcp-probe','executable':pin(old.PYTHON),'argv':[str(old.PYTHON),'-B',str(launch_path),'--config',str(CONTROL/'launch.json'),'--config-sha256',sha(CONTROL/'launch.json')],'dependencies':[ref('tool','build_tenants/graphify/code/ac_support_core.py'),ref('tool','build_tenants/graphify/code/ac_support.py'),ref('tool','build_tenants/graphify/examples/fd-support/actor_cli.py'),{'engine':'workspace-regular-file','root':'fixture_code','path':'launch_fixture.py','object':None,'sha256':sha(launch_path),'selector':None}]+[ref('control',n) for n in ['MCP-POLICY.json','actor-plan.json','ordinary-prompt.txt','launch.json']],'cwd':str(CONTROL/'workspace'),'environment':copy.deepcopy(plan['environment']),'actor_id':actor['id'],'settings':{'timeout_ms':130000,'termination_grace_ms':3000,'max_output_bytes':1048576},'tools':tools,'effect_scope':{'read_only_host_tool':'tools.describe','physical_capture':str(CONTROL/'actor-output'),'public_evidence':root['evidence_root'],'hidden_host_effects':'unknown; no OS confinement claim'},'stdin_mode':'context-utf8','stdout_decoder':{'format':'json','pointer':None,'decode_json_string':False},'observers':[{'kind':'process-end'}]}
grant_id=identity+':grant'
root['executors']={'mcp-probe':executor};root['grants']={grant_id:{'id':grant_id,'authority_sources':root['authority_sources'],'outcome':{'id':identity,'source':task},'principals':['executive'],'targets':['launcher'],'operations':['contract.preflight','dispatch.start'],'tools':tools,'executors':['mcp-probe'],'territory':[],'preconditions':[task],'admission':{'mechanism_id':authority['mechanism']['id'],'mechanism_source':authority['mechanism']['source'],'authority_source':authority['owner_record'],'required_predicates':[],'allowed_override_sources':[]},'notification_sink':'root-events'}}
root['predicates']={};root['operators']={};root['independence_policy']=None
save(CONTROL/'executive-policy.json',root)
contract={'schema':'a_c.fd-support.return-contract/1','id':identity+':observations','authority_source':task,'carrier':'a_c.fd-support.closed-return/1','output_slot':'final_stdout_object','required_evaluations':[],'role':'Worker','proof':{'transition_sources':[],'predicate_ids':[]}}
save(CONTROL/'RETURN-CONTRACT.json',contract)
def call(name,op,args):
 req={'schema':'a_c.fd-support.request/1','id':'q05-mcp-probe2-'+name,'operation':op,'arguments':args}
 save(CONTROL/'requests'/(name+'.json'),req)
 argv=[str(old.PYTHON),'-B',str(old.CLI),'--policy',str(CONTROL/'executive-policy.json'),'--policy-sha256',sha(CONTROL/'executive-policy.json'),'--principal','executive','call','--request','-']
 run=subprocess.run(argv,input=json.dumps(req).encode(),capture_output=True,timeout=60)
 save(CONTROL/'responses'/(name+'.json'),run.stdout.decode());save(CONTROL/'responses'/(name+'.stderr'),run.stderr.decode())
 result=json.loads(run.stdout)
 if run.returncode or result['status']!='ok':raise RuntimeError('Public preparation refusal: '+name)
 return result
stable=[task,root['product']['definition'],root['method_profile']['source']]+[ref('control',n) for n in ['MCP-POLICY.json','actor-plan.json','ordinary-prompt.txt','launch.json','RETURN-CONTRACT.json','SOURCE-NOTES.json']]
observation=call('observe','workspace.observe',{'scope':[{'root':x['root'],'path':x['path'],'kind':'file'} for x in stable]})['result']['artifact']
subject={'id':identity,'sha256':sha(CONTROL/'ordinary-prompt.txt')}
packet={'activation':{'id':identity+':launch','revision':'1','configuration':task},'frame':{'id':'qualification.physical-executor/1','revision':'1','declaration':task,'evaluation':task,'result_algebra':ref('method','standards/ACTIVATION.md',{'lines':[1004,1055]})},'subject_basis':{'subject':subject,'method_profile':{k:root['method_profile'][k] for k in ('id','sha256')},'product':{'id':root['product']['definition_id'],'definition':root['product']['definition']},'observations':[observation],'dependencies':stable,'time_basis':'Stable exact control inputs only'},'attention':{'material_relations':stable,'invariants':[task],'semantic_sources':[task],'exclusions':['any dispatch capability through host MCP','any host shell/source mutation','Q05 behavioral qualification'],'prohibited_assumptions':['mcp get accepted key proves runtime support']},'actor_authority':{'actor_id':actor['id'],'role':'Worker','capability':task,'semantic':None,'evaluation':None,'operation':task,'decision':None,'acceptance':None,'publication':None,'territory':[],'tools':tools},'evidence_relations':{'admissible_evidence':stable,'acquisition':stable,'dependencies':[],'conjunction':None,'translation':None,'consumer':'root-executive','return_contract':ref('control','RETURN-CONTRACT.json')},'stop_change':{'invalidators':['selected source/config drift'],'stop_conditions':['120 seconds','any refusal'],'residuals':['nested dispatch unestablished','hidden effects and full host input unknown'],'re_entry':['Root chooses any supported successor'],'reconfiguration':[]},'profile_additions':{'worker':{'operation_grant_id':grant_id,'mutation_subject':subject,'territory':[]}}}
context=call('assemble','context.assemble',{'packet':packet,'models':[],'sources':[],'late_acquisition':[],'envelope':{'capacity_bytes':None,'boundary':'executor-stdin-utf8','host_context':{'state':'unknown','bytes':None,'evidence':None}}})['result']['artifact']
preflight=call('preflight','contract.preflight',{'context':context,'grant_id':grant_id,'executor_id':'mcp-probe','result_key':identity,'observations':[observation]})
result={'standing':'One read-only control ready; Root launch selection required','policy':pin(CONTROL/'executive-policy.json'),'plan':pin(CONTROL/'actor-plan.json'),'mcp_policy':pin(CONTROL/'MCP-POLICY.json'),'context':context,'preflight':preflight['result']['artifact'],'contract_sha256':preflight['result']['value']['contract_sha256'],'decision':preflight['result']['value']['decision'],'gaps':preflight['result']['value']['gaps'],'observation':observation,'no_dispatch':True}
save(CONTROL/'READINESS.json',result);print(json.dumps(result,indent=2))
