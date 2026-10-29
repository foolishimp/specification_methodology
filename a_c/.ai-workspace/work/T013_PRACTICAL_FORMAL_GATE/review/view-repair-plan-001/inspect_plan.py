"""Source/data inspection only; no live source, compiler or product imports."""
from pathlib import Path
import hashlib
import json
import re
import tarfile

W = Path('/Users/jim/src/apps/specification_methodology/a_c/.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE')
P = W / 'lean/view-repair-001'
F = W / 'real-use/runtime-preparation-002/execution-001'
OUT = Path(__file__).resolve().parent


def sha(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def load(path):
    return json.loads(path.read_bytes())


assert sha(P / 'CLOSED.json') == 'a914ec6d639073b1bfd3d56f5db2bb6da6079b2d77d77b0d505d03d67ff84d25'
assert sha(P / 'PINS.json') == '42e8ef18414ed186f5477e9b61a38319a9e25d4dd7e90b4c25ddc6278bdeaa1f'
pins = load(P / 'PINS.json')['members']
assert all(Path(n).name == n and not (P/n).is_symlink() and sha(P/n) == h for n,h in pins.items())
assert {p.name for p in P.iterdir() if p.is_file()} == set(pins) | {'PINS.json','CLOSED.json'}
assert sha(F / 'CLOSED.json') == '2b791df7a0cb172f569606534c27dc6d55eb619caae4444be566bab13e652f9b'
failure_pins = load(F / 'PINS.json')['members']
for name in ('FAILURE.json','PUBLIC-EVIDENCE-CUSTODY.json','RETURN.md'):
    assert sha(F/name) == failure_pins[name]
subject = load(P / 'SUBJECT.json')
bundle = Path(subject['frozen_bundle'])
assert bundle.is_relative_to(W / 'real-use/runtime-preparation-001/execution/evidence/formal')
custody = load(F / 'PUBLIC-EVIDENCE-CUSTODY.json')
for name in ('GateData.lean','GateViews.lean','GateViews.log','request.json','certificates.json','input.json','supplied-views.json'):
    expected = custody['members'][str((bundle/name).relative_to(Path(custody['root'])))]['sha256']
    assert sha(bundle/name) == expected == subject['frozen_members'][name]
old = (bundle/'GateViews.lean').read_text()
new = (P/'PROPOSED_GateViews.lean').read_text()
assert old.split('theorem checked0')[0] == new.split('-- PROPOSAL ONLY:')[0]
assert old[old.index('theorem set0'):] == new[new.index('theorem set0'):]
assert 'set_option debug.skipKernelTC false' in new
assert not re.search(r'\b(?:sorry|native_decide|axiom)\b', new)
assert 'theorem checked0 : checkCertificate model.dependencies model.localKeys seeds0 trace0 = true := by' in new
assert 'exact decide_eq_true ⟨seed_nonempty0, seed_universe0, trace_universe0, witness0, closed0⟩' in new
assert 'theorem witness0 : Witness model.dependencies seeds0 trace0 := by' in new
assert 'theorem closed0 : Closed model.dependencies (traceSet seeds0 trace0) := by decide +kernel' in new

data = (bundle/'GateData.lean').read_text()
blocks = re.findall(r'^def edges(\d+) : List \(Nat × Nat\) := \[\n(.*?)\n\]', data, re.M | re.S)
assert [int(i) for i,_ in blocks] == list(range(32))
names = re.search(r'^def edges : List \(Nat × Nat\) := \[(.*?)\]\.flatten$', data, re.M).group(1)
assert names.split(', ') == ['edges'+str(i) for i in range(32)]
edges = [tuple(map(int,p)) for _,block in blocks for p in re.findall(r'\((\d+),\s*(\d+)\)',block)]
assert len(edges) == len(set(edges)) == 3995
parents = load(P/'PARENT-WITNESSES.json')
assert parents['full_edge_source_sha256'] == sha(bundle/'GateData.lean')
assert parents['model_raw_sha256'] == sha(bundle/'input.json') == '70feb48cf657bcb20231dbfffe0c2076e5e69b24aeb0f226a001a22957b7f56a'
assert parents['seeds'] == [182,278] and parents['budget'] == 29
request = load(bundle/'request.json')
assert request['selections'][0]['budget_records'] == 29
assert request['supplied_views']['raw_sha256'] == sha(bundle/'supplied-views.json') == '70bfa0148bcb3bc10111a99a60fa42c2e87f5b99352ed446fe4c09178f419768'
source_trace = json.loads(re.search(r'^def trace0 : List Nat := (\[.*\])$',new,re.M).group(1))
assert source_trace == parents['trace']
known = set(parents['seeds'])
candidate_count = 0
for ordinal,row in enumerate(parents['rows']):
    assert row['ordinal'] == ordinal and row['target'] == source_trace[ordinal]
    assert row['known_before'] == sorted(known)
    eligible = sorted(p for p,t in edges if t == row['target'] and p in known)
    assert eligible == row['eligible_parents'] and row['parent'] == min(eligible)
    expected = f"theorem witness_edge0_{ordinal} : {row['target']} ∈ model.dependencies {row['parent']} := by decide +kernel"
    assert expected in new
    candidate_count += len(known)
    known.add(row['target'])
assert len(parents['rows']) == len(source_trace) == 27
assert sorted(known) == parents['included'] and len(known) == 29
assert len({r['parent'] for r in parents['rows']}) == 14
assert candidate_count == parents['known_parent_candidates_upper_bound'] == 405
constructor_refs = re.findall(r'⟨⟨(\d+), by decide \+kernel, witness_edge0_(\d+)⟩', new)
assert [(int(parent),int(ordinal)) for parent,ordinal in constructor_refs] == [(r['parent'],r['ordinal']) for r in parents['rows']]
assert (181,1122) in edges and 181 not in parents['seeds']
assert (278,1122) not in edges and 278 in parents['seeds']

probe_summary = []
results = load(P/'RESULTS.json')
for name,expected_exit in [('ProbeWitness',-6),('ProbeClosed',1),('ProbeDecomposed',0)]:
    external = load(P/(name+'.external.json'))
    assert external['source_sha256'] == sha(P/(name+'.lean'))
    assert external['log_sha256'] == sha(P/(name+'.log'))
    assert external['returncode'] == results['probes'][name]['returncode'] == expected_exit
    assert external['external_seconds'] == results['probes'][name]['external_seconds'] < 90
    assert external['argv'][1:5] == ['-j','1','-M','4096'] and external['timeout_seconds'] == 90
    assert external['retained_compiled_inputs'] == str(bundle)
    assert external['LEAN_PATH'].split(':')[0] == str(bundle)
    probe_summary.append(dict(name=name,exit=expected_exit,seconds=external['external_seconds']))
assert 'Type mismatch' in (P/'ProbeWitness.log').read_text()
closed_log = (P/'ProbeClosed.log').read_text()
assert 'Type mismatch' in closed_log and "'AC.GateData.ClosedProbe.closed_checked' depends on axioms: [propext, Classical.choice, Quot.sound]" in closed_log
range_log = (P/'ProbeDecomposed.log').read_text()
assert 'PASS original trace-range subset decision' in range_log and 'error:' not in range_log
assert 'memory_exception' in (bundle/'GateViews.log').read_text()

archive = W/'package/delivery-001/source-package.tar'
with tarfile.open(archive,'r:') as tar:
    manifest = json.loads(tar.extractfile('SOURCE_PACKAGE.json').read())
    assert subject['public_runtime_pins'] == manifest['portable_runtime_identity']['pins']
    frozen_core_pins = {name: hashlib.sha256(tar.extractfile('a_c/build_tenants/lean/'+name).read()).hexdigest() for name in ['AC/Closure.lean','AC/GateProof.lean','AC/Projection.lean','AC/Model.lean']}
    calls = []
    for member in tar:
        if member.name.endswith('.py'):
            for i,line in enumerate(tar.extractfile(member).read().decode().splitlines(),1):
                if 'views_source' in line:
                    calls.append(dict(path=member.name,line=i,text=line.strip()))
assert len(calls) == 3  # import, definition and one call in the frozen package
report = dict(status='passed',scope='closed proposal and frozen source/data only; no compiler/product/model/actor invocation or live source read',proposal_files_checked=len(pins),proposal_sha256=sha(P/'PROPOSAL.md'),concrete_proposal_sha256=sha(P/'PROPOSED_GateViews.lean'),frozen_core_pins=frozen_core_pins,parent_steps=27,valid_exact_parent_memberships=True,original_model_edges=3995,exact_prefix_and_downstream_suffix_preserved=True,unchanged_final_audit_names=True,uncompiled_proposal=True,witness_cause_uniquely_established=False,range_only_cause_supported=False,probe_summary=probe_summary,expected_future_parent_negative=dict(step=0,parent=181,target=1122,real_edge=True,parent_in_known=False),expected_missing_edge_negative=dict(step=0,parent=278,target=1122,parent_in_known=True,real_edge=False),frozen_views_source_references=calls,actual_same_model_29_view_public_success_required=True,affected_negative_required=True,repair_discharged=False)
(OUT/'CHECKS.json').write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['status','proposal_files_checked','parent_steps','original_model_edges','exact_prefix_and_downstream_suffix_preserved','uncompiled_proposal','repair_discharged']},sort_keys=True))
