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


def _references_proof(imported,n):
    externals=imported['envelope']['external_resolutions']
    blocks=['externals'+str(i) for i in range((len(externals)+127)//128)]
    text=''
    for i,block in enumerate(blocks):
        table='externalTable'+str(i)
        text+=f'def {table} : Array String := ({block}.map External.identity).toArray\n'
        member='List.mem_cons.mpr (Or.inl rfl)'
        for _ in range(i):member='List.mem_cons.mpr (Or.inr ('+member+'))'
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


def _proof_header(imports):
    return 'module\n'+''.join('public import '+name+'\n' for name in imports)+'@[expose] public section\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\nset_option debug.skipKernelTC false\nnamespace AC.GateData\n'


def _char_literal(value):
    return "'"+lean_string(value)[1:-1].replace("'", "\\'")+"'"


def _name_rows(imported,external):
    return [e['external_identity'] for e in imported['envelope']['external_resolutions']] if external else [e['record']['id'] for e in imported['records']]


def name_contract_names(imported,external):
    if len(imported['records'])<=256:return []
    base='external' if external else 'local'
    return ['AC.GateData.'+base+'CharsBlock'+str(i)+'_source' for i in range((len(_name_rows(imported,external))+127)//128)]+['AC.GateData.'+base+'Chars_source']+([] if external else ['AC.GateData.names_exact'])


def name_source(imported,external=False):
    n=len(imported['records']);text=_proof_header(['GateData','AC.Structure'])
    if not external:text+=f'theorem keys_exact : model.records.map Record.key = List.range {n} := by rfl\n'
    if n<=256:return text+'end AC.GateData\n'
    if not external:
        text+=f'theorem names_array : model.records.map Record.identity = nameTable.toList := by rfl\ntheorem nameTable_size : nameTable.size = {n} := by rfl\n'
        text+=f'theorem names_exact : model.records.map Record.identity = (List.range {n}).map lookupName := by\n rw [names_array]\n change nameTable.toList = (List.range {n}).map (fun i => nameTable[i]?.getD "")\n simpa only [nameTable_size] using array_reconstruct nameTable ""\n#print axioms names_exact\n'
    base='external' if external else 'local';letter='E' if external else 'L';records='externals' if external else 'records';project='External.identity' if external else 'Record.identity';field='externalResolutions' if external else 'records'
    rows=_name_rows(imported,external)
    for i,value in enumerate(rows):text+=f'def chars{letter}{i} : List Char := ['+', '.join(_char_literal(c) for c in value)+']\n'
    blocks=[];checks=[]
    for i,start in enumerate(range(0,len(rows),128)):
        block=base+'CharsBlock'+str(i);blocks.append(block);checks.append(block+'_source')
        text+=f'def {block} : List (List Char) := ['+', '.join(f'chars{letter}{j}' for j in range(start,min(start+128,len(rows))))+']\n'
        text+=f'theorem {block}_source : {block}.map String.ofList = {records}{i}.map {project} := by rfl\n#print axioms {block}_source\n'
    text+=f'def {base}Chars : List (List Char) := ['+', '.join(blocks)+'].flatten\n'
    text+=f'theorem {base}Chars_source : {base}Chars.map String.ofList = model.{field}.map {project} := by\n'
    text+=' change (['+', '.join(blocks)+'].flatten).map String.ofList = (['+', '.join(records+str(i) for i in range(len(blocks)))+f'].flatten).map {project}\n'
    text+=' simp only [List.map_flatten, List.map_cons, List.map_nil'+(' ,'+', '.join(checks) if checks else '')+']\n'
    return text+f'#print axioms {base}Chars_source\nend AC.GateData\n'


def identity_contract_names(imported):
    if len(imported['records'])<=256:return []
    count=len(imported['records'])+len(imported['envelope']['external_resolutions'])
    return ['AC.GateData.orderedPairsChecked'+str(i) for i in range((max(0,count-1)+127)//128)]+['AC.GateData.chars_reconstructed','AC.GateData.ordered_chain','AC.GateData.identities_checked']


def identities_source(imported):
    text=_proof_header(['GateLocalNames','GateExternalNames'])
    if len(imported['records'])<=256:return text+'end AC.GateData\n'
    rows=[(value,'charsL'+str(i)) for i,value in enumerate(_name_rows(imported,False))]+[(value,'charsE'+str(i)) for i,value in enumerate(_name_rows(imported,True))]
    ordered=sorted(enumerate(rows),key=lambda p:p[1][0]);names=[entry[1][1] for entry in ordered];count=len(rows);fuel=count.bit_length()
    text+='def labeledChars : List (Nat × List Char) := ['+', '.join(f'({i},{row[1]})' for i,row in ordered)+']\n'
    text+='def orderedChars : List (List Char) := ['+', '.join(names)+']\n'
    text+=f'theorem chars_reconstructed : (sortLabeled {fuel} labeledChars).map Prod.snd = localChars ++ externalChars := by rfl\n#print axioms chars_reconstructed\n'
    blocks=[]
    for i,start in enumerate(range(0,max(0,count-1),128)):
        block='orderedPairs'+str(i);blocks.append(block)
        text+=f'def {block} : List (List Char × List Char) := ['+', '.join(f'({names[j]},{names[j+1]})' for j in range(start,min(start+128,count-1)))+']\n'
        text+=f'theorem orderedPairsChecked{i} : ∀ p ∈ {block}, p.1 < p.2 := by decide +kernel\n#print axioms orderedPairsChecked{i}\n'
    text+='theorem orderedPairs_exact : orderedChars.zip orderedChars.tail = ['+', '.join(blocks)+'].flatten := by rfl\n'
    text+='theorem ordered_chain : orderedChars.IsChain (· < ·) := by\n apply isChain_of_pairs\n rw [orderedPairs_exact]\n apply all_flatten\n intro block member\n'
    if blocks:
        text+=' simp only [List.mem_cons, List.not_mem_nil, or_false] at member\n rcases member with '+' | '.join('rfl' for _ in blocks)+'\n'
        for i in range(len(blocks)):text+=f' · exact orderedPairsChecked{i}\n'
    else:text+=' simp only [List.not_mem_nil] at member\n'
    text+=f'theorem identitySource : (sortLabeled {fuel} labeledChars).map (fun p => String.ofList p.2) = model.records.map Record.identity ++ model.externalResolutions.map External.identity :=\n rendered_labeled_source _ _ localChars externalChars labeledChars {fuel} chars_reconstructed localChars_source externalChars_source\n'
    text+=f'theorem identities_checked : ((model.records.map Record.identity) ++ (model.externalResolutions.map External.identity)).Nodup :=\n nodup_of_labeled_characters _ labeledChars {fuel} identitySource ordered_chain\n'
    text+='theorem names_checked : (model.records.map Record.identity).Nodup := (List.nodup_append.mp identities_checked).1\n'
    text+='theorem external_checked : (model.externalResolutions.map External.identity).Nodup := (List.nodup_append.mp identities_checked).2.1\n'
    text+='theorem separate : ∀ r ∈ model.records, r.identity ∉ model.externalResolutions.map External.identity := separated_of_nodup _ _ identities_checked\n'
    return text+'#print axioms ordered_chain\n#print axioms identities_checked\nend AC.GateData\n'

def bounds_source(imported):
    n=len(imported['records']);text=_proof_header(['GateData','AC.Structure'])
    if n>256:
        prop=f'fun e : Nat × Nat => e.1 < {n} ∧ e.2 < {n}'
        for i in range((len(imported['edges'])+127)//128):
            text+=f'theorem edgeBounds{i} : ∀ x ∈ edges{i}, ({prop}) x := by decide +kernel\n'
        text+=_flatten_proof('edges','edgeBounds',prop,len(imported['edges']))
        text+=_references_proof(imported,n)
        text+='#print axioms edgeBounds\n#print axioms refBounds\n'
    return text+'end AC.GateData\n'


def model_proof(imported):
    n=len(imported['records']);text=_proof_header(['GateIdentities','GateBounds'])
    if n<=256:text+='theorem model_checked : checkModel model = true := by decide +kernel\n'
    else:text+=f'theorem model_checked : checkModel model = true :=\n checked_of_wellFormed model (wellFormed_of_range model {n} keys_exact names_checked external_checked separate edgeBounds refBounds)\n'
    return text+'#print axioms model_checked\nend AC.GateData\n'

def views_source(imported,cases):
    text='module\npublic import GateModel\n@[expose] public section\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\nset_option debug.skipKernelTC false\nnamespace AC.GateData\n'
    for i,c in enumerate(cases):
        budget=c['effective_budget'];size=c['required_count']
        text+=f'def seeds{i} : Finset Nat := ({numbers(c["seeds"])} : List Nat).toFinset\n'
        text+=f'def trace{i} : List Nat := {numbers(c["order"])}\ndef included{i} : Finset Nat := ({numbers(c["included"])} : List Nat).toFinset\n'
        known=set(c['seeds']);parents=[]
        for step,child in enumerate(c['order']):
            parent=min((a for a,b in imported['edges'] if b==child and a in known),default=None)
            if parent is None:
                raise ValueError(f'Closure trace has no earlier parent at selection {i}, step {step}')
            parents.append(parent);known.add(child)
            text+=f'theorem witness_edge{i}_{step} : {child} ∈ model.dependencies {parent} := by decide +kernel\n'
        # Python supplies only witnesses. Both the original model edge and the
        # parent's membership in the preceding known set remain kernel checked.
        text+=f'theorem witness{i} : Witness model.dependencies seeds{i} trace{i} := by\n exact\n'
        for step,parent in enumerate(parents):
            text+='  '+' '*step+f'⟨⟨{parent}, by decide +kernel, witness_edge{i}_{step}⟩,\n'
        text+='  '+' '*len(parents)+'True.intro'+'⟩'*len(parents)+'\n'
        n=len(imported['records'])
        text+=f'theorem seed_nonempty{i} : seeds{i}.Nonempty := by decide +kernel\n'
        text+=f'theorem seed_universe{i} : seeds{i} ⊆ Finset.range {n} := by decide +kernel\n'
        text+=f'theorem trace_universe{i} : traceSet seeds{i} trace{i} ⊆ Finset.range {n} := by decide +kernel\n'
        text+=f'theorem closed{i} : Closed model.dependencies (traceSet seeds{i} trace{i}) := by decide +kernel\n'
        text+=f'theorem checked{i} : checkCertificate model.dependencies model.localKeys seeds{i} trace{i} = true := by\n rw [localKeys_range model _ keys_exact]\n exact decide_eq_true ⟨seed_nonempty{i}, seed_universe{i}, trace_universe{i}, witness{i}, closed{i}⟩\n'
        text+=f'theorem set{i} : traceSet seeds{i} trace{i} = included{i} := by decide +kernel\n'
        text+=f'theorem reachability{i} (x : Nat) : x ∈ included{i} ↔ Reachable model.dependencies seeds{i} x := by\n rw [← set{i}]\n exact certificate_exact_reachability model.dependencies model.localKeys seeds{i} trace{i} checked{i} x\n'
        if budget>=size:
            text+=f'theorem result{i} : project model seeds{i} trace{i} {budget} = .ok (makeProjection model seeds{i} included{i}) := by\n rw [← set{i}]\n exact projection_success model seeds{i} trace{i} {budget} model_checked checked{i} (by decide +kernel)\n'
        else:
            text+=f'theorem result{i} : project model seeds{i} trace{i} {budget} = .error "insufficient record budget; required closure is not truncated" :=\n insufficient_budget_refuses model seeds{i} trace{i} {budget} model_checked checked{i} (by decide +kernel)\n'
        text+=f'def execution{i} : Except String Projection := projectWithProof model seeds{i} trace{i} {budget} model_checked checked{i}\n'
        text+=f'theorem execution_matches_project{i} : execution{i} = project model seeds{i} trace{i} {budget} :=\n projectWithProof_eq_project model seeds{i} trace{i} {budget} model_checked checked{i}\n'
        for prefix in ('checked','set','reachability','result','execution_matches_project'):text+=f'#print axioms {prefix}{i}\n'
    text+='def selections : List (Finset Nat × List Nat × Nat) := ['+', '.join(f'(seeds{i},trace{i},{c["effective_budget"]})' for i,c in enumerate(cases))+']\n'
    text+='def executions : List (Except String Projection) := ['+', '.join(f'execution{i}' for i in range(len(cases)))+']\nend AC.GateData\n'
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
   ("views", Lean.Json.arr (AC.GateData.executions.map (AC.GateRuntime.selectionResultJson m)).toArray)]
 IO.println result.compress
 return 0
'''
