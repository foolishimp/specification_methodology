from pathlib import Path
import hashlib,json,re
ROOT=Path('/Users/jim/src/apps/specification_methodology/stdo_skills/.ai-workspace/work/STDO_CONTEXT_GENERATION_001')
ARM=ROOT/'arms/representation'; EVIDENCE=ARM/'evidence'
MODEL='/Users/jim/.local/share/stdo-qualification/v3.0.5-rc.1/public-001/formal/current-full/model.json'
MODEL_ID='urn:a-c:coordinate-rebind:model:25c5d17918e649e4866d0f0981475ee4377616593cd8c14363b62e30fae5af27'
MODEL_SHA='b40ecc595d1a58ad96a9ba0be4942e015123224adee1832a58a6c3b53f21eeb7'
RECORD='urn:a-c:generation:ba37e2825e4e3c758a5cfaec:record:'
METHOD='/Users/jim/.local/share/stdo-qualification/v3.0.5-rc.1/public-001/store/releases/v3.0.5-rc.1'
MANIFEST='64c026667abba933d289317793dbe80b5f9ab822a9870307795584402e460e1c'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def scenario_ref(case,fid): return f'{ROOT}/inputs/{case}.md@sha256:{sha(ROOT/"inputs"/(case+".md"))}#{fid}'
def rref(rid): return f'{MODEL}@sha256:{MODEL_SHA}#{RECORD}{rid}'
def source_block(case, rules):
    lines=[f'Fixture: `{ROOT}/inputs/{case}.md`, SHA-256 `{sha(ROOT/"inputs"/(case+".md"))}`. `{case}-nn` denotes its numbered facts. All project coordinates are fictional, not accessed files or measured hashes.',f'Method: `stdo://releases/v3.0.5-rc.1/`, manifest SHA-256 `{MANIFEST}`. Method selection/current installation is supplied by `inputs/BASIS.json`; no new full installation verification is claimed. The source Product builder remains on v3.0.4.',f'Representation G: `{MODEL}`, model identity `{MODEL_ID}`, raw SHA-256 `{MODEL_SHA}` (checked). In this document, `R(x)` means the exact record `{RECORD}x` in G. Grounding below is the representation\'s source locator under `build_tenants/a_c/representation/stdo-v3.0.5-rc.1/source/`; it is not a separate prose read.', 'Released skills actually read: `'+METHOD+'/plugins/spec/skills/stdo-work/SKILL.md`, SHA-256 `9dc06e03fd6f64483fa485ed55f35e414fefae472bb69aa930ecef9335585b35`; and `'+METHOD+'/plugins/spec/skills/stdo-review/SKILL.md`, SHA-256 `b90b3a2014d7891e25b40c11e5f3638accb9f3408cb3f0cf3922d26f17bc57df`.']
    lines+=['','| Rule alias | Exact representation record and grounding |','|---|---|']
    lines += [f'| {alias} | R({rid}); {grounding} |' for alias,rid,grounding in rules]
    return '\n\n'.join(lines[:4])+'\n'+'\n'.join(lines[4:])+'\n'
def build_map(case,method_nodes,extra_nodes,edges):
    text=(ROOT/'inputs'/f'{case}.md').read_text()
    chunks=re.split(r'^## ('+case+r'-\d+)\s*$',text,flags=re.M)
    nodes=[]
    for i in range(1,len(chunks),2):
        fid=chunks[i]; nodes.append({'id':fid,'kind':'scenario_fact','text':chunks[i+1].strip(),'source_refs':[scenario_ref(case,fid)]})
    for nid,txt,refs in method_nodes: nodes.append({'id':nid,'kind':'method_fact','text':txt,'source_refs':[rref(x) for x in refs]})
    for nid,kind,txt,refs in extra_nodes:
        nodes.append({'id':nid,'kind':kind,'text':txt,'source_refs':[scenario_ref(case,x) if x.startswith(case+'-') else rref(x) for x in refs]})
    es=[]
    for fr,to,typ,reason,refs in edges:
        es.append({'from':fr,'to':to,'type':typ,'reason':reason,'source_refs':[scenario_ref(case,x) if x.startswith(case+'-') else rref(x) for x in refs]})
    return {'schema':'stdo.context-generation.constraint-map/1','scenario':case,'nodes':nodes,'edges':es,'limitations':['Explanatory graph of proposed contexts, not formal verification, admission, execution, review, acceptance or dispatch.','Model projection conserves only declared governing closure; no semantic-fidelity or complete-method guarantee follows, and absent edges do not remove obligations.','Scenario coordinates are fictional fixture facts; no fictional paths were accessed.','All cases share this generator session in S1, S2, S3 order; later cases have carryover. Host context and general shell are not isolated by an enforced acquisition gate.']}
def write_case(case,executive,worker,reviewer,map_data,event_tags,reused_tags=[]):
    folder=ARM/case; folder.mkdir(exist_ok=True)
    for name,body in [('executive.md',executive),('worker.md',worker),('reviewer.md',reviewer)]: (folder/name).write_text(body.rstrip()+'\n')
    (folder/'constraint-map.json').write_text(json.dumps(map_data,ensure_ascii=False,indent=2)+'\n')
    basis=json.loads((ROOT/'inputs/BASIS.json').read_text())
    common=json.loads((EVIDENCE/'common-intake.json').read_text())
    evs=[json.loads(line) for line in (EVIDENCE/'events.jsonl').read_text().splitlines()]
    selected=[e for e in evs if Path(e['raw_output']).name.removesuffix('.raw.json') in event_tags]
    reused=[e for e in evs if Path(e['raw_output']).name.removesuffix('.raw.json') in reused_tags]
    common_reads=[]
    for rel in ['inputs/COMMON.md','inputs/OUTPUT_CONTRACT.md','inputs/BASIS.json','preparation/FREEZE.json']:
        p=ROOT/rel; common_reads.append({'category':'common_input','tool':'exec_command cat; then byte/hash verification','source_path':str(p),'sha256':sha(p),'range':'complete file','selected_source_bytes':p.stat().st_size,'displayed_source_bytes':p.stat().st_size,'purpose':'shared instructions, contract, supplied basis and frozen selection','cost_allocation':'once in session; reused after S1'})
    p=ROOT/'inputs'/f'{case}.md'
    case_read={'category':'scenario_input','tool':'exec_command cat','source_path':str(p),'sha256':sha(p),'range':'complete file','selected_source_bytes':p.stat().st_size,'displayed_source_bytes':p.stat().st_size,'purpose':'supplied fictional scenario facts'}
    acqs=[]
    if case=='S1':
        acqs += [dict(category='common_skill',tool='exec_command cat',purpose='required released skill/control-reference guidance',**e) for e in common['common_skill_acquisition']]
        acqs += [{'category':'tool_guidance','tool':'exec_command help/rg/sed','source_path':'/Users/jim/.local/share/stdo-qualification/v3.0.5-rc.1/public-001/runtime/a_c/scripts/ac.py','ranges':['graph --help','graph find --help','graph inspect --help','graph project --help','dispatch imports matching graph'], 'selected_source_bytes':None,'purpose':'discover permitted public operations; byte total unavailable for earlier tool returns'},{'category':'tool_guidance','tool':'exec_command rg/sed','source_path':'/Users/jim/.local/share/stdo-qualification/v3.0.5-rc.1/public-001/runtime/a_c/build_tenants/graphify/code/ac_graph.py','ranges':['lines 680-860','lines 1-95','function-name search'],'selected_source_bytes':None,'purpose':'public pure API and projection closure mechanics, no model semantic admission'},{'category':'representation_identity','tool':'Python hashlib/json metadata extraction','source_path':MODEL,'raw_sha256':MODEL_SHA,'file_bytes_read':8568341,'display':'identity and top-level type/count metadata only','displayed_bytes':None,'purpose':'confirm exact supplied model; no complete model display'}]
        acqs += common_reads
    else:
        acqs += [{'category':'session_reuse','source_path':str(EVIDENCE/'common-intake.json'),'purpose':'previously acquired common skills/references/input binding; no additive reread or token claim','reused_common_inputs':[x['source_path'] for x in common_reads]}]
    acqs += [case_read]
    acqs += [dict(category='representation_method',**e) for e in selected]
    if case=='S1':
        p=EVIDENCE/'s1-projection-catalog.display.json'
        acqs += [{'category':'representation_discovery_display','tool':'Python field selection from retained projection','source_path':str(EVIDENCE/'s1-project.raw.json'),'selected_display':str(p),'displayed_bytes':p.stat().st_size,'purpose':'discover exact included identities/grounding; 140-character statement prefixes are discovery only and not normative substitutes'}]
    acqs += [{'category':'session_reuse','source_path':e['selected_display'],'record_ids':e['inputs'],'purpose':'reuse acquired exact method meaning; not new acquisition'} for e in reused]
    out={'schema':'stdo.context-generation.acquisition/1','scenario':case,'assigned_mode':'current-representation-first','actual_skill':basis['skill'],'review_skill':basis['review_skill'],'method':basis['experiment_method'],'representation':basis['representation'],'acquisitions':acqs,'source_fallbacks':[],'failed_reads':[],'query_misses':[{'query':q['query'],'meaning':'literal find had no matches; no absence-of-obligation inference'} for e in selected if e['operation']=='find' for q in json.loads(Path(e['raw_output']).read_text()) if not q['matches']],'supplied_preverified_identity':{'basis_json':str(ROOT/'inputs/BASIS.json'),'installation_and_manifest':'supplied prior public-001 verification only; not re-executed','freeze_sha256':'ef89677365e8caeba649242e40b464db35bca8c388cbe5668dc57d28257944d2'},'checks_actually_performed':['Raw model SHA-256 matched exact granted value.','Installed public validate(model) succeeded before find/inspect/project; this checks declared fragment structure only.','Common skill SHA-256 values matched BASIS.json.','Named common and scenario file hashes matched the selected freeze; no private checklist was read.'],'actual_execution':'Only these context/evidence artifacts written; no fictional work, native Skill UI activation, real admission, dispatch, provider, Git, network, build or proof execution.','host_and_order_limits':common['host_exposure']|{'scenario_order':['S1','S2','S3'],'current_case':case,'independence':'one generator session; no independent assessment performed'},'metrics':{'new_scenario_input_bytes':case_read['selected_source_bytes'],'common_skill_reference_source_bytes_once':sum(e['selected_bytes'] for e in common['common_skill_acquisition']) if case=='S1' else 0,'common_input_source_bytes_once':sum(e['selected_source_bytes'] for e in common_reads) if case=='S1' else 0,'method_raw_output_bytes':sum(e['raw_output_bytes'] for e in selected),'method_displayed_bytes':sum(e['displayed_bytes'] for e in selected),'model_file_bytes_per_load':8568341,'model_load_count_for_recorded_operations':len(selected),'public_operation_calls':sum(len(e['inputs']) if e['operation'] in ['find','inspect'] else 1 for e in selected),'tool_batches_for_recorded_operations':len(selected),'full_input_file_display_count':len(common_reads)+1 if case=='S1' else 1,'generated_output_file_bytes':{},'observed_elapsed_time':None,'token_count':None,'monetary_cost':None,'attention':None,'unavailable':['Whole-turn elapsed time was not instrumented.','No tokenizer, model cost or reader attention measurement was exposed.','Early help/implementation reads have no retained exact source-byte measurement; known byte totals are bounded partial totals.'],'interpretation':'Source bytes, repeated raw model loads, mechanical returned bytes, selected display bytes and generated output bytes are separate proxies; none measures actual Worker attention or execution efficiency.'}}
    for _ in range(5):
        (folder/'acquisition.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
        sizes={p.name:p.stat().st_size for p in folder.iterdir() if p.is_file()}
        if sizes==out['metrics']['generated_output_file_bytes']:break
        out['metrics']['generated_output_file_bytes']=sizes
    print(json.dumps({'scenario':case,'files':sizes,'total_output_bytes':sum(sizes.values())}))
