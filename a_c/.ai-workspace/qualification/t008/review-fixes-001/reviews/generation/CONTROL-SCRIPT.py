from pathlib import Path
import copy, hashlib, json, os, sys, traceback
from unittest.mock import patch

TEMP = Path(__file__).resolve().parent
REPORT = Path('/Users/jim/src/apps/specification_methodology/a_c/.ai-workspace/qualification/t008/review-fixes-001/reviews/generation')
sys.path.insert(0, str(TEMP/'code'))
import ac_generate as g
import ac_grounding as h
import ac_repair as r

rows = []
module_calls = []
forbidden_calls = []
SOURCE = '# Contract\nPublication requires a reviewed plan.\n'
SETTINGS = {'model':'synthetic-review-fixture','model_reasoning_effort':'high'}
VERSION = 'synthetic-review-fixture-no-actor'
UPSTREAM = TEMP/'synthetic-upstream'
(UPSTREAM/Path(g.UPSTREAM_PROMPT).parent).mkdir(parents=True)
(UPSTREAM/g.UPSTREAM_PROMPT).write_text('Synthetic host reference\n```\nRead FILE_LIST for CHUNK_NUM of TOTAL_CHUNKS; DEEP_MODE.\n```\n')
CONFIG = TEMP/'synthetic-config.toml'
CONFIG.write_text('model="synthetic-review-fixture"\nmodel_reasoning_effort="high"\n')


def forbidden(*args, **kwargs):
    forbidden_calls.append('actor/provider operation attempted')
    raise AssertionError('No actor/provider operation is permitted in these controls')


def module_fixture(path):
    from types import SimpleNamespace
    def validate(value):
        module_calls.append(str(path))
        return []
    return {'semantic_cleanup':SimpleNamespace(validate_semantic_fragment=validate)}


def check(name, fn):
    try:
        detail = fn()
        rows.append({'case':name,'status':'passed','detail':detail})
    except Exception as exc:
        rows.append({'case':name,'status':'failed','error':type(exc).__name__+': '+str(exc),'traceback':traceback.format_exc()})


def refused(fn):
    try:
        fn()
    except (ValueError, OSError) as exc:
        return type(exc).__name__+': '+str(exc)
    raise AssertionError('Expected refusal, operation succeeded')


def answer_for(chunk):
    seg = chunk['segments'][0]
    index = next(i for i,line in enumerate(seg['text'].splitlines()) if 'Publication requires a reviewed plan.' in line)
    ground = {'section_id':seg['id'],'start_line':seg['start_line']+index,'end_line':seg['start_line']+index,'quote':'Publication requires a reviewed plan.'}
    return {'concepts':[{'key':'reviewed_plan','label':'Reviewed plan','definition':'A reviewed plan is required for publication.','conditions':[],'exceptions':[],'grounding':[copy.deepcopy(ground)]}],
            'constraints':[{'key':'publication_requires_plan','applies_to_keys':['reviewed_plan'],'statement':'Publication requires a reviewed plan.','conditions':[],'exceptions':[],'uncertainty':'','grounding':[copy.deepcopy(ground)]}],
            'relations':[],'latitude':[],'residuals':[],
            'dispositions':[{'section_id':seg['id'],'decision':'retained','keys':['reviewed_plan','publication_requires_plan'],'reason':'Retain the stated publication prerequisite.'}],
            'limitations':['Synthetic mechanical fixture; no semantic acceptance.']}


def attempt(output, plan, chunk, stage, answer, number=1, failed=False):
    target = output/'actors'/stage/chunk['id']/f'attempt-{number:03d}'
    target.mkdir(parents=True)
    work = target/'empty-workspace'; work.mkdir()
    schema = g.ASSETS/('extraction.schema.json' if stage=='extract' else 'author.schema.json')
    prompt = g.extraction_prompt(plan,chunk,output) if stage=='extract' else g.author_prompt(plan,chunk,output)
    (target/'prompt.txt').write_text(prompt)
    g.save(target/'answer.json',answer)
    overrides = {**SETTINGS,'features.shell_tool':False,'features.apps':False,'features.multi_agent':False,'features.memories':False,'features.js_repl':False,'web_search':'disabled','project_doc_max_bytes':0}
    command = ['/synthetic-review/codex','exec','--json','--ephemeral','--sandbox','read-only','--skip-git-repo-check','--color','never','--output-schema',str(schema.resolve()),'--output-last-message',str((target/'answer.json').resolve()),'--cd',str(work.resolve())]
    for key,value in overrides.items(): command.extend(['-c',key+'='+json.dumps(value,ensure_ascii=False)])
    command.append('-')
    invocation = {'profile':'ac.generation.actor-invocation/1','settings':SETTINGS,'cli_version':VERSION,'config_path':str(CONFIG),'config_sha256':g.sha(CONFIG.read_bytes()),'command':command,'inline_overrides':overrides,'cwd':str(work),'prompt_sha256':g.sha(prompt.encode()),'schema_sha256':g.sha(schema.read_bytes()),'timeout_seconds':30,'effective_mcp_inventory':[]}
    g.save(target/'invocation.json',invocation)
    usage = [{'input_tokens':100,'cached_input_tokens':0,'output_tokens':20}]
    events = [{'type':'item.completed','item':{'type':'agent_message','text':'Synthetic fixture'}},{'type':'turn.completed','usage':usage[0]}]
    (target/'events.jsonl').write_text(''.join(json.dumps(e)+'\n' for e in events))
    (target/'stderr.txt').write_text('')
    g.save(target/'usage.json',{'usage_events':usage,'claim':'Synthetic protocol fixture, not actual backend usage.'})
    error = None
    try:
        if stage=='author': g.author_check(answer,chunk)
        else: g.semantic_check(answer,chunk,output,module_fixture(UPSTREAM))
    except g.GenerationError as exc: error = str(exc)
    result = {'profile':'ac.generation.actor-result/1','status':'failed' if failed else 'completed','failures':['source_or_semantic_fragment_validation'] if failed else [],'cli_exit_code':0,'timed_out':False,'user_config_unchanged':True,'schema_errors':[],'unexpected_item_types':[],'answer_sha256':g.sha((target/'answer.json').read_bytes()),'events_sha256':g.sha((target/'events.jsonl').read_bytes()),'stderr_sha256':g.sha((target/'stderr.txt').read_bytes()),'settings':SETTINGS,'cli_version':VERSION,'usage_events':usage,'elapsed_seconds':0.1}
    if failed:
        if error is None: raise AssertionError('Source-failed fixture has no actual source failure')
        result['validation_error'] = error
    else:
        if error is not None: raise AssertionError(error)
        g.save(target/'validation.json',{'status':'structurally_valid_proposal','answer_sha256':result['answer_sha256'],'chunk_sha256':g.digest(chunk),'claim':'Synthetic mechanical validation only.'})
    g.save(target/'result.json',result)
    return target


def build(name, mode='direct', source=SOURCE, failed=False):
    folder=TEMP/'cases'/name; folder.mkdir(parents=True)
    corpus=folder/'input'; corpus.mkdir(); (corpus/'source.md').write_text(source)
    manifest=folder/'manifest.json'
    g.save(manifest,{'subject_id':'repo://independent-review/'+name+'/','files':[{'path':'source.md','sha256':g.sha(source.encode()),'bytes':len(source.encode())}]})
    output=folder/'run'
    record={'root':str(UPSTREAM),'commit':g.UPSTREAM_COMMIT,'prompt_path':g.UPSTREAM_PROMPT,'prompt_sha256':g.sha((UPSTREAM/g.UPSTREAM_PROMPT).read_bytes())}
    with patch.object(g,'verify_upstream',return_value=record):
        g.prepare(corpus,manifest,output,mode,UPSTREAM if mode!='direct' else None,1000)
    plan,chunks=g.checkpoint(output); chunk=chunks[0]
    g.save(output/'actor-settings.json',{'settings':SETTINGS,'cli_version':VERSION})
    extract=None
    if mode=='graphify':
        source_path=str((output/'corpus/source.md').resolve())
        extraction={'nodes':[{'id':'reviewed_plan','label':'Reviewed plan','file_type':'concept','source_file':source_path,'source_location':'L2','source_url':None,'captured_at':None,'author':None,'contributor':None,'rationale':None}],'edges':[],'hyperedges':[],'input_tokens':0,'output_tokens':0}
        extract=attempt(output,plan,chunk,'extract',extraction)
    if mode in g.GRAPH_MODES:
        discovery=output/'discovery'; discovery.mkdir()
        g.save(discovery/'graph.json',{'nodes':[],'links':[]})
        g.save(discovery/'structural.json',{'synthetic_fixture':True,'nodes':[],'edges':[]})
        entry={'id':chunk['id']}
        if extract: entry.update(attempt=str(extract.relative_to(output)),answer_sha256=g.sha((extract/'answer.json').read_bytes()))
        g.save(discovery/'coverage.json',{'chunks':[entry],'claim':'Synthetic discovery custody; no upstream trial.'})
        g.save(discovery/'result.json',{'status':'completed','mode':mode,'files':{p:g.sha((discovery/p).read_bytes()) for p in ('graph.json','structural.json','coverage.json')}})
    answer=answer_for(chunk)
    if failed:
        for family in ('concepts','constraints'):
            answer[family][0]['grounding'][0]['quote']='Publication requires a reviewed\nplan.'
    author=attempt(output,plan,chunk,'author',answer,failed=failed)
    return output,plan,chunk,author,extract


def edit_json(path, fn):
    value=g.load(path); fn(value); g.save(path,value)


def ordinary_positive():
    output,plan,chunk,author,_=build('ordinary-positive')
    assert g.successful_attempt(output,'author',chunk)==author
    model=g.assemble(output)
    assert model['status']=='proposed' and model['processing_complete'] is True
    return {'status':model['status'],'processing_complete':True,'claim':model['claim']}


def custody_case(name, mutation):
    output,plan,chunk,author,_=build(name)
    assert g.successful_attempt(output,'author',chunk)==author
    mutation(output,author)
    selection=refused(lambda:g.successful_attempt(output,'author',chunk))
    assembly=refused(lambda:g.assemble(output))
    assert not (output/'proposal').exists()
    return {'selection':selection,'assembly':assembly}


def failed_retry_case(name, unfinished):
    output,plan,chunk,author,_=build(name)
    if unfinished: (author.parent/'attempt-002').mkdir()
    else:
        value=answer_for(chunk)
        for family in ('concepts','constraints'): value[family][0]['grounding'][0]['quote']='Missing actual source support.'
        attempt(output,plan,chunk,'author',value,2,failed=True)
    assert g.successful_attempt(output,'author',chunk) is None
    message=refused(lambda:g.assemble(output))
    prepared=g.stage(output,'author',execute=False)
    assert prepared['status']=='incomplete' and prepared['completed_chunks']==[]
    assert author.exists() and not (output/'proposal').exists()
    return {'assembly':message,'prepared_stage':prepared['status'],'older_attempt_retained':True}


def grounding_failure_separation():
    output,plan,chunk,author,_=build('source-failure-separation',failed=True)
    before={p.name:p.read_bytes() for p in author.iterdir() if p.is_file()}
    assert g.successful_attempt(output,'author',chunk) is None
    ordinary=refused(lambda:g.assemble(output))
    original,proof=h.evidence(output,plan,chunk,author)
    assert proof['original_status']=='failed'
    normalized=h.normalize(output)
    assert normalized['chunks'][0]['status']=='derived_validated'
    assembled=h.assemble(output)
    assert assembled['status']=='proposed'
    repair_request=r.prepare(output,chunk['id'])
    assert (repair_request/'request.json').is_file() and not (repair_request/'actor').exists()
    assert all((author/name).read_bytes()==data for name,data in before.items())
    return {'ordinary':ordinary,'grounded':assembled['status'],'original_status':g.load(author/'result.json')['status'],'repair_preparation_model_calls':0}


def graph_stage_case(mode):
    output,plan,chunk,author,extract=build('stage-'+mode,mode)
    calls_before=len(module_calls)
    assert g.successful_attempt(output,'author',chunk)==author
    if extract:
        assert g.successful_attempt(output,'extract',chunk)==extract
        assert len(module_calls)>calls_before
        edit_json(extract/'answer.json',lambda a:a['nodes'][0].update(source_file='outside-exact-chunk'))
        ah=g.sha((extract/'answer.json').read_bytes())
        edit_json(extract/'result.json',lambda a:a.update(answer_sha256=ah))
        edit_json(extract/'validation.json',lambda a:a.update(answer_sha256=ah))
        message=refused(lambda:g.successful_attempt(output,'extract',chunk))
        assert 'source_file' in message
        return {'exact_author_and_extract_custody':True,'refreshed_hash_wrong_source':message,'actual_upstream_execution':False}
    edit_json(author/'invocation.json',lambda a:a.update(schema_sha256='f'*64))
    return {'exact_author_custody':True,'wrong_schema':refused(lambda:g.successful_attempt(output,'author',chunk)),'actual_upstream_execution':False}


def fence_case(name, body, expected):
    values=g.sections('source.md',body,'repo://independent-fence/')
    headings=[v['heading'] for v in values]
    assert headings==expected,(headings,expected)
    assert ''.join(v['text'] for v in values)==body
    assert ''.join(s['text'] for c in g.make_chunks(values,1000) for s in c['segments'])==body
    return {'headings':headings,'characters_conserved':True}


def unicode_case(label, separator):
    source='# Contract\nPreamble'+separator+'Publication requires a reviewed plan.'+separator+'End.\n'
    output,plan,chunk,author,_=build('unicode-'+label,source=source)
    answer=g.load(author/'answer.json')
    g.author_check(answer,chunk)
    noop,changes=h.normalize_answer(answer,chunk)
    assert changes==[] and noop==answer
    for family in ('concepts','constraints'):
        answer[family][0]['grounding'][0].update(start_line=500,end_line=500)
    derived,changes=h.normalize_answer(answer,chunk)
    g.author_check(derived,chunk)
    assert len(changes)==2
    assert g.canonical(h.nongrounding(answer))==g.canonical(h.nongrounding(derived))
    coords=[(derived[f][0]['grounding'][0]['start_line'],derived[f][0]['grounding'][0]['end_line']) for f in ('concepts','constraints')]
    assert coords==[(3,3),(3,3)],coords
    return {'strict_noop':True,'recovered_ranges':coords,'non_grounding_equal':True}


def ambiguity_refusal():
    section={'id':'repo://same-section','path':'x.md','start_line':10,'end_line':11,'text':'A requires evidence.\nA  requires evidence.\n','sha256':g.sha(b'A requires evidence.\nA  requires evidence.\n')}
    raw={'section_id':section['id'],'start_line':500,'end_line':500,'quote':'A requires evidence.'}
    return refused(lambda:h.recover_anchor(raw,section))


with patch.object(g,'run_actor',side_effect=forbidden), patch.object(g,'actor_settings',side_effect=forbidden), patch.object(g,'upstream_modules',side_effect=module_fixture):
    check('ordinary-complete-direct-proposal',ordinary_positive)
    for filename in ('answer.json','result.json','invocation.json','prompt.txt','events.jsonl','stderr.txt','usage.json'):
        check('missing-'+filename,lambda filename=filename:custody_case('missing-'+filename,lambda output,author:(author/filename).unlink()))
    check('append-prompt-and-refresh-self-hash',lambda:custody_case('prompt-refreshed',lambda output,author:((author/'prompt.txt').write_text((author/'prompt.txt').read_text()+'\nAdditional repair directions.\n'),edit_json(author/'invocation.json',lambda v:v.update(prompt_sha256=g.sha((author/'prompt.txt').read_bytes()))))))
    check('wrong-schema',lambda:custody_case('wrong-schema',lambda output,author:edit_json(author/'invocation.json',lambda v:v.update(schema_sha256='0'*64))))
    check('wrong-settings',lambda:custody_case('wrong-settings',lambda output,author:edit_json(author/'invocation.json',lambda v:v['settings'].update(model='other-model'))))
    check('wrong-actual-argv',lambda:custody_case('wrong-argv',lambda output,author:edit_json(author/'invocation.json',lambda v:v['command'].insert(2,'--dangerously-bypass-approvals-and-sandbox'))))
    check('changed-events-with-stale-result-hash',lambda:custody_case('events-stale',lambda output,author:(author/'events.jsonl').write_text('{}\n')))
    check('usage-contradiction',lambda:custody_case('usage-bad',lambda output,author:edit_json(author/'usage.json',lambda v:v.update(usage_events=[{'input_tokens':1}]))))
    def tool_event(output,author):
        events=[{'type':'item.completed','item':{'type':'mcp_tool_call'}},{'type':'turn.completed','usage':{'input_tokens':100,'cached_input_tokens':0,'output_tokens':20}}]
        (author/'events.jsonl').write_text(''.join(json.dumps(e)+'\n' for e in events))
        edit_json(author/'result.json',lambda v:v.update(events_sha256=g.sha((author/'events.jsonl').read_bytes())))
    check('tool-event-despite-refreshed-event-hash',lambda:custody_case('tool-event',tool_event))
    def failed_event(output,author):
        with (author/'events.jsonl').open('a') as f:f.write(json.dumps({'type':'turn.failed','error':{'message':'synthetic'}})+'\n')
        edit_json(author/'result.json',lambda v:v.update(events_sha256=g.sha((author/'events.jsonl').read_bytes())))
    check('failed-turn-despite-refreshed-event-hash',lambda:custody_case('turn-failed',failed_event))
    check('retained-workspace-not-empty',lambda:custody_case('workspace-content',lambda output,author:(author/'empty-workspace'/'unexpected').write_text('unadmitted context')))
    check('newer-unfinished-no-fallback',lambda:failed_retry_case('newer-unfinished',True))
    check('newer-failed-no-fallback',lambda:failed_retry_case('newer-failed',False))
    check('ordinary-vs-grounding-source-failure',grounding_failure_separation)
    check('graphify-ac-stage-custody',lambda:graph_stage_case('graphify-ac'))
    check('graphify-extract-stage-custody-and-source-revalidation',lambda:graph_stage_case('graphify'))
    fence_cases=[
      ('simple3','# Before\n```md\n# Hidden\n```\n# Actual\n',['Before','Actual']),
      ('wider-with-short-inner','# Before\n````md\n```\n# Hidden\n````\n# Actual\n',['Before','Actual']),
      ('wider-with-longer-close','# Before\n````md\n# Hidden\n`````\n# Actual\n',['Before','Actual']),
      ('tilde-marker','# Before\n~~~~md\n~~~\n# Hidden\n~~~~\n# Actual\n',['Before','Actual']),
      ('other-marker-not-close','# Before\n````md\n~~~~\n# Hidden\n````\n# Actual\n',['Before','Actual']),
      ('closing-content-not-close','# Before\n```md\n``` trailing\n# Hidden\n```\n# Actual\n',['Before','Actual']),
      ('three-space-indent','# Before\n   ```md\n# Hidden\n   ```\n# Actual\n',['Before','Actual']),
      ('four-space-not-close','# Before\n```md\n    ```\n# Hidden\n```\n# Actual\n',['Before','Actual']),
      ('closing-horizontal-space','# Before\n```md\n# Hidden\n``` \t\n# Actual\n',['Before','Actual']),
      ('invalid-backtick-info','# Before\n```bad`info\n# Visible\n',['Before','Visible'])]
    for name,body,expected in fence_cases:
        check('fence-'+name,lambda name=name,body=body,expected=expected:fence_case(name,body,expected))
    for label,separator in [('lf','\n'),('vt','\v'),('ff','\f'),('fs','\x1c'),('gs','\x1d'),('rs','\x1e'),('nel','\x85'),('ls','\u2028'),('ps','\u2029')]:
        check('line-convention-'+label,lambda label=label,separator=separator:unicode_case(label,separator))
    check('normalized-ambiguity-remains-refused',ambiguity_refusal)

assert not forbidden_calls,forbidden_calls
result={'profile':'a_c.review.generation-fixes.controls/1','cases':rows,'passed':sum(x['status']=='passed' for x in rows),'failed':sum(x['status']=='failed' for x in rows),'actual_actor_or_provider_calls':0,'actual_upstream_execution':False,'scope':'Independent synthetic controls over exact owned code copies; no full suite or model-quality assessment.','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
with (REPORT/'CONTROLS.json').open('x') as f:json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps({'passed':result['passed'],'failed':result['failed'],'failed_cases':[x for x in rows if x['status']=='failed'],'script_sha256':result['script_sha256'],'controls_sha256':hashlib.sha256((REPORT/'CONTROLS.json').read_bytes()).hexdigest()},sort_keys=True))
sys.exit(1 if result['failed'] else 0)
