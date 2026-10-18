import copy, importlib.util, json, sys, time
from pathlib import Path
root=Path('/Users/jim/src/apps/specification_methodology/a_c/dogfood')
spec=importlib.util.spec_from_file_location('v3artifactreview',root/'v3_graphify.py');v=importlib.util.module_from_spec(spec);sys.modules[spec.name]=v;spec.loader.exec_module(v)
for tenant in ('claude','codex'):
 path=root/('stdo-v3-i5-'+tenant)/'artifacts/manifest.json'
 if not path.exists(): print(json.dumps({'tenant':tenant,'status':'artifacts-not-yet-present'}),flush=True);continue
 t=time.monotonic(); s,m,manifest=v.load_representation(tenant)
 selections=[s.program['frame_indexes'][0]['uri']]
 selection=v.select(s,m,selections)
 # Mutate carrier-owned native payload directly, keeping identity/structure; exact decoder must reject.
 graph=v.read_document(path.parent/'graph.json.gz'); victim=next(n for n in graph['nodes'] if n['ac_role']=='record'); victim['ac_payload']['record']['value']['native_json']+=' '
 try:v.ac.decode(v.ac.GraphCarrier(graph))
 except v.ac.Refusal: tamper=True
 else:raise AssertionError('native payload tamper accepted')
 print(json.dumps({'tenant':tenant,'status':'passed','final_artifact_full_validation':True,'canonical_builder_sha256':manifest['builder_sha256'],'canonical_carrier_sha256':manifest['carrier_sha256'],'selectors':manifest['selector_check'],'counts':manifest['counts'],'direct_payload_tamper_refused':tamper,'first_selector_native_counts':{k:len(x) for k,x in selection['native'].items()},'elapsed_seconds':round(time.monotonic()-t,3)}),flush=True)
