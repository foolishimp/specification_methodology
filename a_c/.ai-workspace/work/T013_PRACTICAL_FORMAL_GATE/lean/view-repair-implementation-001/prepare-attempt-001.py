"""Generate bounded proof controls from exact frozen actual input; no gate call."""
from pathlib import Path
import copy
import hashlib
import json
import sys
import types

OUT=Path(__file__).resolve().parent
BASELINE=json.loads((OUT/'BASELINE.json').read_bytes())
BUNDLE=Path(BASELINE['frozen_bundle'])
ROOT=OUT.parents[4]/'build_tenants/lean'
sys.path.insert(0,str(ROOT/'scripts'))
import gate_codegen as codegen
import import_fixture as bridge

sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
model=bridge.read_json(BUNDLE/'model.json')
imported=bridge.import_model(model)
cases=bridge.read_json(BUNDLE/'certificates.json')
assert len(imported['records'])==1987 and len(imported['edges'])==3995
assert cases[0]['seeds']==[182,278] and cases[0]['required_count']==29
assert sha(BUNDLE/'model.json')=='70feb48cf657bcb20231dbfffe0c2076e5e69b24aeb0f226a001a22957b7f56a'
source=codegen.views_source(imported,cases)
actual=OUT/'actual-29';actual.mkdir()
(actual/'GateViews.lean').write_text(source)
original=(BUNDLE/'GateViews.lean').read_text()
assert source[:source.index('theorem witness_edge0_0')]==original[:original.index('theorem checked0')]
assert source[source.index('theorem set0'):]==original[original.index('theorem set0'):]
proposal=(OUT.parent/'view-repair-001/PROPOSED_GateViews.lean').read_text().replace('-- PROPOSAL ONLY: not compiled or qualified in this activation.\n','')
assert source==proposal
old=types.ModuleType('old_view_codegen')
old_source=OUT/'before/build_tenants/lean/scripts/gate_codegen.py'
exec(compile(old_source.read_bytes(),str(old_source),'exec'),old.__dict__)
low=copy.deepcopy(cases);low[0]['effective_budget']=28
old_low=old.views_source(low);new_low=codegen.views_source(imported,low)
assert new_low[new_low.index('theorem set0'):]==old_low[old_low.index('theorem set0'):]
(OUT/'budget-28-old.lean').write_text(old_low)
(OUT/'budget-28-new.lean').write_text(new_low)
header=source[:source.index('theorem witness_edge0_0')]
negative=OUT/'negatives';negative.mkdir()
assert (181,1122) in {tuple(x) for x in imported['edges']} and 181 not in cases[0]['seeds']
text=header+'''theorem real_edge : 1122 ∈ model.dependencies 181 := by decide +kernel
#print axioms real_edge
theorem rejected_parent : ∃ parent ∈ seeds0, 1122 ∈ model.dependencies parent := by
 exact ⟨181, by decide +kernel, real_edge⟩
end AC.GateData
'''
(negative/'UnknownParent.lean').write_text(text)
assert (278,1122) not in {tuple(x) for x in imported['edges']} and 278 in cases[0]['seeds']
text=header+'''theorem known_parent : 278 ∈ seeds0 := by decide +kernel
#print axioms known_parent
theorem rejected_edge : ∃ parent ∈ seeds0, 1122 ∈ model.dependencies parent := by
 exact ⟨278, known_parent, by decide +kernel⟩
end AC.GateData
'''
(negative/'MissingEdge.lean').write_text(text)
parents=json.loads((OUT.parent/'view-repair-001/PARENT-WITNESSES.json').read_bytes())
assert all(row['parent']!=1867 for row in parents['rows'])
short=copy.deepcopy(cases[0]);short['order'].remove(1867);short['included'].remove(1867)
short_source=codegen.views_source(imported,[short])
text=short_source[:short_source.index('theorem witness_edge0_0')]+'''theorem rejected_closed : Closed model.dependencies (traceSet seeds0 trace0) := by
 decide +kernel
end AC.GateData
'''
(negative/'OmittedResidual.lean').write_text(text)
record={'schema':'a_c.T013.view-repair-generated-controls/1','positive_source_sha256':sha(actual/'GateViews.lean'),'reviewed_concrete_proposal_matched':True,'actual_prefix_and_downstream_suffix_byte_identical':True,'budget_28_downstream_suffix_byte_identical':True,'model_raw_sha256':sha(BUNDLE/'model.json'),'certificates_sha256':sha(BUNDLE/'certificates.json'),'imported_records':1987,'imported_edges':3995,'parents':27,'negative_sources':{p.name:sha(p) for p in negative.iterdir()},'omitted_1867_not_a_later_selected_parent':True,'evidence_kind':'Generated component controls, not public-path qualification'}
(OUT/'GENERATED.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
