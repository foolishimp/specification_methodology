"""Bounded-layout dynamic Lean imports and concrete obligations; never native proof."""
from import_fixture import canonical
from generate_fixture import lean_string, numbers
HEADER='module\npublic import AC.GateProof\n@[expose] public section\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\nset_option debug.skipKernelTC false\nnamespace AC.GateData\n'

def data_source(imported,raw_sha):
    strings={};decls=[]
    def string(value):
        if value not in strings:
            name='str'+str(len(strings));strings[value]=name
            decls.append('def '+name+' : String := '+lean_string(value)+'\n')
        return strings[value]
    def chunked(name,typ,values):
        names=[]
        for offset in range(0,len(values),128):
            n=name+str(offset//128);names.append(n)
            decls.append(f'def {n} : List {typ} := [\n'+',\n'.join(values[offset:offset+128])+'\n]\n')
        decls.append(f'def {name} : List {typ} := ['+', '.join(names)+'].flatten\n')
    records=[]
    for entry in imported['records']:
        r=entry['record'];name='record'+str(entry['index'])
        fields={'identity':r['id'],'context':r['context'],'owner':r['owner'],'scope':canonical(r['scope']),'basis':r['basis'],'payload':canonical(r)}
        values=[f'{key} := {string(value)}' for key,value in fields.items()]
        decls.append(f'def {name} : Record := {{ key := {entry["index"]}, family := .{entry["family"]}, '+', '.join(values)+' }\n')
        records.append(name)
    chunked('records','Record',records)
    decls.append('def nameTable : Array String := #['+', '.join(strings[r['record']['id']] for r in imported['records'])+']\n')
    decls.append('def lookupName (i : Nat) : String := nameTable[i]?.getD ""\n')
    decls.append('def nameOrder : List Nat := '+numbers(sorted(range(len(imported['records'])),key=lambda i:imported['records'][i]['record']['id']))+'\n')
    refs=[]
    for ref in imported['references']:
        path='['+', '.join(f'.index {x}' if type(x) is int else '.field '+string(x) for x in ref['path'])+']'
        target=f'.localRecord {ref["target"]}' if type(ref['target']) is int else '.external '+string(ref['target'])
        refs.append(f'{{ owner := {ref["owner"]}, path := {path}, target := {target}, governing := {str(ref["governing"]).lower()}, domain := {string(ref["domain"])} }}')
    chunked('references','Reference',refs)
    ext=[f'{{ identity := {string(e["external_identity"])}, payload := {string(canonical(e))} }}' for e in imported['envelope']['external_resolutions']]
    chunked('externals','External',ext)
    chunked('edges','(Nat × Nat)',[f'({a},{b})' for a,b in imported['edges']])
    env=imported['envelope']
    data={'identity':env['id'],'rawSha256':raw_sha,'canonicalSha256':imported['model_sha256'],
          'envelope':canonical(env),'invalidation':canonical(env['interpretation']['invalidation'])}
    fields=[f'  {k} := {string(v)}' for k,v in data.items()]
    decls.append('def model : Model := {\n'+'\n'.join(fields)+'\n  records := records\n  references := references\n  externalResolutions := externals\n  edges := edges\n}\n')
    return HEADER+'\n'.join(decls)+'\nend AC.GateData\n'

def model_proof(imported):
    n=len(imported['records'])
    text='module\npublic import GateData\npublic import AC.Structure\n@[expose] public section\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\nset_option debug.skipKernelTC false\nnamespace AC.GateData\n'
    text+=f'theorem keys_exact : model.records.map Record.key = List.range {n} := by rfl\n'
    if n <= 256:
        return text+'theorem model_checked : checkModel model = true := by decide +kernel\n#print axioms model_checked\nend AC.GateData\n'
    text+=f'theorem names_checked : (model.records.map Record.identity).Nodup := by\n apply names_nodup_of_order _ lookupName nameOrder {n} {n.bit_length()}\n · rfl\n · decide +kernel\n · decide +kernel\n'
    text+='theorem external_checked : (model.externalResolutions.map External.identity).Nodup := by decide +kernel\n'
    entries=[('records','separate','fun r : Record => r.identity ∉ model.externalResolutions.map External.identity',len(imported['records'])),
        ('edges','edgeBounds',f'fun e : Nat × Nat => e.1 < {n} ∧ e.2 < {n}',len(imported['edges'])),
        ('references','refBounds',f'fun r : Reference => r.owner < {n} ∧ targetBound {n} (model.externalResolutions.map External.identity) r.target',len(imported['references']))]
    for base,proof,prop,count in entries:
        blocks=[base+str(i) for i in range((count+127)//128)]
        for i,block in enumerate(blocks):
            text+=f'theorem {proof}{i} : ∀ x ∈ {block}, ({prop}) x := by decide +kernel\n'
        text+=f'theorem {proof} : ∀ x ∈ model.{base}, ({prop}) x := by\n'
        text+=f' change ∀ x ∈ '+('['+', '.join(blocks)+'].flatten')+f', ({prop}) x\n'
        text+=' apply all_flatten\n intro block member\n'
        if not blocks:text+=' simp only [List.not_mem_nil] at member\n'
        else:
            text+=' simp only [List.mem_cons, List.not_mem_nil, or_false] at member\n'
            text+=' rcases member with '+' | '.join('rfl' for _ in blocks)+'\n'
            for i in range(len(blocks)):text+=f' · exact {proof}{i}\n'
    text+=f'theorem model_checked : checkModel model = true :=\n checked_of_wellFormed model (wellFormed_of_range model {n} keys_exact names_checked external_checked separate edgeBounds refBounds)\n'
    text+='#print axioms model_checked\nend AC.GateData\n'
    return text

def views_source(cases):
    text='module\npublic import GateModel\n@[expose] public section\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\nset_option debug.skipKernelTC false\nnamespace AC.GateData\n'
    for i,c in enumerate(cases):
        budget=c['effective_budget'];size=c['required_count']
        text+=f'def seeds{i} : Finset Nat := ({numbers(c["seeds"])} : List Nat).toFinset\n'
        text+=f'def trace{i} : List Nat := {numbers(c["order"])}\ndef included{i} : Finset Nat := ({numbers(c["included"])} : List Nat).toFinset\n'
        text+=f'theorem checked{i} : checkCertificate model.dependencies model.localKeys seeds{i} trace{i} = true := by\n rw [localKeys_range model _ keys_exact]\n decide +kernel\n'
        text+=f'theorem set{i} : traceSet seeds{i} trace{i} = included{i} := by decide +kernel\n'
        text+=f'theorem reachability{i} (x : Nat) : x ∈ included{i} ↔ Reachable model.dependencies seeds{i} x := by\n rw [← set{i}]\n exact certificate_exact_reachability model.dependencies model.localKeys seeds{i} trace{i} checked{i} x\n'
        if budget>=size:
            text+=f'theorem result{i} : project model seeds{i} trace{i} {budget} = .ok (makeProjection model seeds{i} included{i}) := by\n rw [← set{i}]\n exact projection_success model seeds{i} trace{i} {budget} model_checked checked{i} (by decide +kernel)\n'
        else:
            text+=f'theorem result{i} : project model seeds{i} trace{i} {budget} = .error "insufficient record budget; required closure is not truncated" :=\n insufficient_budget_refuses model seeds{i} trace{i} {budget} model_checked checked{i} (by decide +kernel)\n'
        for prefix in ('checked','set','reachability','result'):text+=f'#print axioms {prefix}{i}\n'
    text+='def selections : List (Finset Nat × List Nat × Nat) := ['+', '.join(f'(seeds{i},trace{i},{c["effective_budget"]})' for i,c in enumerate(cases))+']\nend AC.GateData\n'
    return text

RUNNER='''module
import GateViews
meta import GateViews
import AC.GateRuntime
meta import AC.GateRuntime
public import Lean.Data.Json.Basic
public section
def main : IO UInt32 := do
 let m := AC.GateData.model
 let result := Lean.Json.mkObj [("model", AC.GateRuntime.modelJson m),
   ("views", Lean.Json.arr (AC.GateData.selections.map (AC.GateRuntime.gateSelectionJson m)).toArray)]
 IO.println result.compress
 return 0
'''
