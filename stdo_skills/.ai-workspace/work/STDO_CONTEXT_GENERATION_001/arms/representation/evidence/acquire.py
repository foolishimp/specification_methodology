#!/usr/bin/env python3
"""Bounded representation reader; writes evidence only inside this arm."""
import hashlib, importlib.util, json, pathlib, sys
BASE=pathlib.Path('/Users/jim/src/apps/specification_methodology/stdo_skills/.ai-workspace/work/STDO_CONTEXT_GENERATION_001/arms/representation/evidence')
MODEL=pathlib.Path('/Users/jim/.local/share/stdo-qualification/v3.0.5-rc.1/public-001/formal/current-full/model.json')
IMPL=pathlib.Path('/Users/jim/.local/share/stdo-qualification/v3.0.5-rc.1/public-001/runtime/a_c/build_tenants/graphify/code/ac_graph.py')
EXPECTED='b40ecc595d1a58ad96a9ba0be4942e015123224adee1832a58a6c3b53f21eeb7'
def encoded(x): return (json.dumps(x,ensure_ascii=False,indent=2)+'\n').encode()
def semantic_record(r):
    r=json.loads(json.dumps(r))
    for k in ('basis','context','owner','scope','kind','sort','judgment_kind'): r.pop(k,None)
    for field in (r.get('value',{}),r.get('predicate',{}),r):
        for g in field.get('grounding',[]): g.pop('quote',None)
    return r
def save(name,x):
    p=BASE/name
    if p.exists(): raise ValueError('Evidence output already exists: '+str(p))
    p.write_bytes(encoded(x)); return p
b=MODEL.read_bytes()
assert hashlib.sha256(b).hexdigest()==EXPECTED
spec=importlib.util.spec_from_file_location('stdo_graph_installed',IMPL)
graph=importlib.util.module_from_spec(spec); sys.modules[spec.name]=graph; spec.loader.exec_module(graph)
model=graph.validate(json.loads(b))
mode, tag = sys.argv[1:3]
items=json.loads(sys.argv[3])
if not tag.replace('-','').replace('_','').isalnum(): raise ValueError('Unsafe evidence tag')
if mode=='find':
    raw=[graph.find(model,q) for q in items]
    visible=[{'query':x['query'],'matches':x['matches'],'scope':x['scope']} for x in raw]
elif mode=='inspect':
    raw=[graph.inspect(model,rid) for rid in items]
    visible=[{'family':x['family'],'record':semantic_record(x['record']),'typed_references':[r for r in x['references'] if r['path'][0] not in ('basis','context','owner','scope','kind','sort','judgment_kind') and 'grounding' not in r['path']]} for x in raw]
elif mode=='project':
    raw=graph.project(model,items)
    visible={'seeds':items,'included_count':len(raw['included']),'population_counts':{k:len(v) for k,v in raw['populations'].items()},'unresolved_residual_count':len(raw['boundary']['unresolved_residuals']),'crossing_relation_count':len(raw['boundary']['crossing_relations']),'claim':raw['claim']}
else: raise ValueError('Unsupported mode')
raw_path=save(tag+'.raw.json',raw)
visible_path=save(tag+'.display.json',visible)
event={'operation':mode,'installed_public_function':'ac_graph.'+mode,'implementation':str(IMPL),'implementation_sha256':hashlib.sha256(IMPL.read_bytes()).hexdigest(),'model':str(MODEL),'raw_model_sha256':EXPECTED,'raw_model_bytes':len(b),'inputs':items,'raw_output':str(raw_path),'raw_output_bytes':raw_path.stat().st_size,'selected_display':str(visible_path),'displayed_bytes':visible_path.stat().st_size,'transport_envelope_excluded':True,'display_transform':'omit parent audit envelope and repeated coordinate metadata; preserve exact semantic fields and grounding path/section/lines; embedded duplicate source quotes retained in raw only','claim_limit':'typed structure and declared closure are not semantic fidelity, admission, or task completeness'}
with (BASE/'events.jsonl').open('a') as f: f.write(json.dumps(event)+'\n')
sys.stdout.write(encoded(visible).decode())
