from pathlib import Path
import hashlib,json,sys
TEMP=Path(__file__).resolve().parent
REPORT=Path('/Users/jim/src/apps/specification_methodology/a_c/.ai-workspace/qualification/t008/review-fixes-001/reviews/generation')
sys.path.insert(0,str(TEMP/'code'))
import ac_generate as g
output=TEMP/'cases/missing-result.json/run'
plan,chunks=g.checkpoint(output); chunk=chunks[0]
selection=g.successful_attempt(output,'author',chunk)
assert selection is None,'Missing result must not be selected'
try:
 g.assemble(output)
except g.GenerationError as exc:
 assembly={'status':'refused','reason':str(exc)}
else:
 raise AssertionError('Ordinary assembly unexpectedly used missing-result attempt')
assert not (output/'proposal').exists()
stage=g.stage(output,'author',execute=False)
assert stage['status']=='incomplete' and stage['completed_chunks']==[]
result={'profile':'a_c.review.control-resolution/1','case':'missing-result.json','status':'passed','original_controls_preserved':'CONTROLS.json retains first-run 41 passed and one overly narrow reviewer assertion.','reason':'The reviewer first required successful_attempt to throw for missing result; its declared selection API lawfully returns None for unfinished attempts. The governing expectation is no reuse/fallback and ordinary assembly refusal, not an exception from this internal selector.','selection':None,'ordinary_assembly':assembly,'prepared_stage_status':stage['status'],'new_model_or_provider_calls':0,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
with (REPORT/'CONTROLS-RESOLUTION.json').open('x') as f:json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps(result,sort_keys=True))
