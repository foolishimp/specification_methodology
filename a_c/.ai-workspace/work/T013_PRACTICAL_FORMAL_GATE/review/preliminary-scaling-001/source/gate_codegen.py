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

def _identity_code(value):
    # Exact byte-derived witness; the Lean equality is checked independently.
    # Distinct projected values are sufficient, with no injectivity assumption.
    result=1
    for byte in value.encode('utf-8'):result=result*257+byte+1
    return result


def _flatten_proof(base,proof,prop,count,model_field=None):
    blocks=[base+str(i) for i in range((count+127)//128)]
    text=f'theorem {proof} : ∀ x ∈ model.{model_field or base}, ({prop}) x := by\n'
    text+=f' change ∀ x ∈ ['+', '.join(blocks)+f'].flatten, ({prop}) x\n'
    text+=' apply all_flatten\n intro block member\n'
    if not blocks:text+=' simp only [List.not_mem_nil] at member\n'
    else:
        text+=' simp only [List.mem_cons, List.not_mem_nil, or_false] at member\n'
        text+=' rcases member with '+' | '.join('rfl' for _ in blocks)+'\n'
        for i in range(len(blocks)):text+=f' · exact {proof}{i}\n'
    return text


def _identities_proof(imported):
    text='';values=[];all_codes=[]
    specs=[('records','Record.identity',[r['record']['id'] for r in imported['records']],'localCodes'),
           ('externals','External.identity',[r['external_identity'] for r in imported['envelope']['external_resolutions']],'externalCodes')]
    for base,project,names,joined in specs:
        code_names=[];checks=[]
        for i,start in enumerate(range(0,len(names),128)):
            codes=[_identity_code(v) for v in names[start:start+128]];all_codes.extend(codes)
            name=base+'Codes'+str(i);check=name+'_exact';code_names.append(name);checks.append(check)
            text+=f'def {name} : List Nat := '+numbers(codes)+'\n'
            text+=f'theorem {check} : {base}{i}.map (fun r => identityCode ({project} r)) = {name} := by decide +kernel\n'
        text+=f'def {joined} : List Nat := ['+', '.join(code_names)+'].flatten\n'
        field='records' if base=='records' else 'externalResolutions'
        text+=f'theorem {joined}_exact : (model.{field}.map {project}).map identityCode = {joined} := by\n'
        text+=f' change ((['+', '.join(base+str(i) for i in range(len(code_names)))+f'].flatten).map {project}).map identityCode = {joined}\n'
        text+=' simp only [List.map_map, List.map_flatten, List.map_cons, List.map_nil, Function.comp_def, '+', '.join(checks+[joined])+']\n'
    text+='def allCodes : List Nat := localCodes ++ externalCodes\n'
    text+='def sortedCodes : List Nat := '+numbers(sorted(all_codes))+'\n'
    text+='theorem allCodes_exact : ((model.records.map Record.identity) ++ (model.externalResolutions.map External.identity)).map identityCode = allCodes := by\n rw [List.map_append, localCodes_exact, externalCodes_exact]\n rfl\n'
    text+=f'theorem identities_checked : ((model.records.map Record.identity) ++ (model.externalResolutions.map External.identity)).Nodup :=\n nodup_of_codes identityCode _ allCodes sortedCodes {len(all_codes).bit_length()} allCodes_exact (by decide +kernel) (by decide +kernel)\n'
    text+='theorem names_checked : (model.records.map Record.identity).Nodup := (List.nodup_append.mp identities_checked).1\n'
    text+='theorem external_checked : (model.externalResolutions.map External.identity).Nodup := (List.nodup_append.mp identities_checked).2.1\n'
    text+='theorem separate : ∀ r ∈ model.records, r.identity ∉ model.externalResolutions.map External.identity := separated_of_nodup _ _ identities_checked\n'
    return text


def _references_proof(imported,n):
    externals=imported['envelope']['external_resolutions']
    blocks=['externals'+str(i) for i in range((len(externals)+127)//128)]
    text=''
    for i,block in enumerate(blocks):
        table='externalTable'+str(i)
        text+=f'def {table} : Array String := ({block}.map External.identity).toArray\n'
        member='Or.inl rfl' if i<len(blocks)-1 else 'Or.inl rfl'
        for _ in range(i):member='Or.inr ('+member+')'
        text+=f'theorem externalInside{i} : ∀ x ∈ {table}.toList, x ∈ model.externalResolutions.map External.identity := by\n'
        text+=f' change ∀ x ∈ {table}.toList, x ∈ ['+', '.join(blocks)+'].flatten.map External.identity\n'
        text+=f' simpa only [{table}, List.toList_toArray] using mapped_block_inside External.identity ['+', '.join(blocks)+f'] {block} ({member})\n'
    external_index={e['external_identity']:i for i,e in enumerate(externals)}
    # Each external membership is proved once by an exact bounded block index.
    for i,entry in enumerate(externals):
        text+=f'theorem externalAt{i} : {lean_string(entry["external_identity"])} ∈ model.externalResolutions.map External.identity :=\n member_of_block_index _ externalTable{i//128} {i%128} _ externalInside{i//128} (by rfl)\n'
    prop=f'fun r : Reference => r.owner < {n} ∧ targetBound {n} (model.externalResolutions.map External.identity) r.target'
    refs=imported['references']
    for i,start in enumerate(range(0,len(refs),128)):
        term='List.forall_mem_nil _'
        for ref in reversed(refs[start:start+128]):
            witness='(by decide +kernel)' if type(ref['target']) is int else f'⟨by decide +kernel, externalAt{external_index[ref["target"]]}⟩'
            term='List.forall_mem_cons.mpr ⟨'+witness+', '+term+'⟩'
        text+=f'theorem refBounds{i} : ∀ x ∈ references{i}, ({prop}) x :=\n {term}\n'
    return text+_flatten_proof('references','refBounds',prop,len(refs))


def model_proof(imported):
    n=len(imported['records'])
    text='module\npublic import GateData\npublic import AC.Structure\n@[expose] public section\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\nset_option debug.skipKernelTC false\nnamespace AC.GateData\n'
    text+=f'theorem keys_exact : model.records.map Record.key = List.range {n} := by rfl\n'
    if n <= 256:
        return text+'theorem model_checked : checkModel model = true := by decide +kernel\n#print axioms model_checked\nend AC.GateData\n'
    text+=f'theorem names_array : model.records.map Record.identity = nameTable.toList := by rfl\ntheorem nameTable_size : nameTable.size = {n} := by rfl\n'
    text+=f'theorem names_exact : model.records.map Record.identity = (List.range {n}).map lookupName := by\n rw [names_array]\n change nameTable.toList = (List.range {n}).map (fun i => nameTable[i]?.getD "")\n simpa only [nameTable_size] using array_reconstruct nameTable ""\n'
    text+=_identities_proof(imported)
    prop=f'fun e : Nat × Nat => e.1 < {n} ∧ e.2 < {n}'
    for i in range((len(imported['edges'])+127)//128):
        text+=f'theorem edgeBounds{i} : ∀ x ∈ edges{i}, ({prop}) x := by decide +kernel\n'
    text+=_flatten_proof('edges','edgeBounds',prop,len(imported['edges']))
    text+=_references_proof(imported,n)
    text+=f'theorem model_checked : checkModel model = true :=\n checked_of_wellFormed model (wellFormed_of_range model {n} keys_exact names_checked external_checked separate edgeBounds refBounds)\n'
    return text+'#print axioms model_checked\nend AC.GateData\n'

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
