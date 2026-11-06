INSPECTION_LIMITS = [
    'Read-only retained-evidence consistency and currentness, not a new execution verdict.',
    'Process transcripts and actual cold/fresh kernel execution remain separate required evidence.',
    *RESULT_LIMITS]
PROOF_MODULES = ('GateData','GateLocalNames','GateExternalNames','GateIdentities','GateBounds','GateModel','GateViews','GateRun')


def inspect_evidence(bundle, request, *, base_dir=None):
    """Reconstruct retained obligations against an externally selected request."""
    answer = {'schema':'a_c.formal-gate.inspection/1','status':'incomplete','reason':None,
              'checks':[], 'limits':list(INSPECTION_LIMITS)}
    try:
        validate_request(request)
        directory = reuse.guard(bundle, directory=True)
        saved, manifest = reuse.bundle(directory)
        if saved.get('schema') != 'a_c.formal-gate.result/1' or saved.get('status') != 'verified' or saved.get('reason') is not None:
            fail('refused', 'Inspection requires an established verified gate result')
        members = manifest['members']
        actual_names = {p.name for p in directory.iterdir()}
        permitted = set(members) | {'manifest.json','result.json'}
        if 'local-origin.json' in actual_names:
            reuse.decode(reuse.read(directory/'local-origin.json'))
            permitted.add('local-origin.json')  # inert lookup hint, never proof authority
        if actual_names != permitted:
            fail('refused', 'Bundle population differs from complete retained inventory')
        initial = runtime_identity()
        if not reuse.compatible(saved.get('runtime_identity'), initial):
            fail('refused', 'Retained verifier/profile/proof source pins are stale')
        current_support = support.check()
        observations = saved.get('observations')
        if not isinstance(observations, dict) or observations.get('support') != current_support:
            fail('refused', 'Retained proof support differs from actual selected support')
        original = read_json_bytes(reuse.read(directory/'request.json'))
        replay = read_json_bytes(reuse.read(directory/'replay-request.json'))
        validate_request(original); validate_request(replay)
        if digest(original) != saved.get('request_sha256'):
            fail('refused', 'Retained original request digest differs')
        def normalized(value):
            value = copy.deepcopy(value); value['input']['path'] = 'input.json'
            if value['supplied_views'] is not None: value['supplied_views']['path'] = 'supplied-views.json'
            return value
        if replay != normalized(original) or normalized(request) != replay:
            fail('refused', 'Current selected request, selections, views or context differ')
        base = Path(base_dir or Path.cwd())
        for key, name in (('input','input.json'),('supplied_views','supplied-views.json')):
            binding = request[key]
            if binding is None: continue
            path = Path(binding['path']); path = path if path.is_absolute() else base/path
            raw = reuse.read(path)
            if reuse.sha(raw) != binding['raw_sha256'] or raw != reuse.read(directory/name):
                fail('refused', 'Current selected input bytes differ: '+key)
        parsed = read_json_bytes(reuse.read(directory/'input.json'))
        model = bridge.recover_carrier(parsed) if request['input']['format']=='carrier' else parsed
        if not isinstance(model,dict) or model.get('profile')!=bridge.MODEL_PROFILE:
            fail('refused','Unsupported retained model profile')
        if model.get('signature',{}).get('sha256') not in (bridge.SIGNATURE_SHA256,bridge.TOY_SIGNATURE_SHA256):
            validate_generation_profile(model)
        imported = bridge.import_model(model)
        if bridge.reconstruct(imported) != model or read_json_bytes(reuse.read(directory/'model.json')) != model:
            fail('refused','Retained model reconstruction differs from selected current source')
        raw_sha = request['input']['raw_sha256'] if request['input']['format']=='model' else support.sha(directory/'model.json')
        model_identity = {'id':model['id'],'sha256':imported['model_sha256']}
        expected_inputs = {'input':{'raw_sha256':request['input']['raw_sha256'],'bytes':len(reuse.read(directory/'input.json')),'retained_path':'input.json'},
                           'model':{'raw_sha256':raw_sha,'canonical_sha256':imported['model_sha256'],'retained_path':'input.json' if request['input']['format']=='model' else 'model.json'}}
        if request['supplied_views'] is not None:
            expected_inputs['supplied_views'] = {'raw_sha256':request['supplied_views']['raw_sha256'],'bytes':len(reuse.read(directory/'supplied-views.json')),'retained_path':'supplied-views.json'}
        claims = ['imported-model-well-formedness','whole-model-source-correspondence']
        if request['selections']: claims += ['declared-closure-and-projection','record-budget-result']
        if request['supplied_views']: claims += ['supplied-graphify-view-correspondence']
        if (saved.get('model') != model_identity or saved.get('inputs') != expected_inputs
                or saved.get('selections') != request['selections'] or saved.get('context_binding') != request['context_binding']
                or saved.get('requested_claims') != claims or saved.get('checked_claims') != claims):
            fail('refused','Retained result does not discharge exact required current obligations')
        names = {r['record']['id']:r['index'] for r in imported['records']}; cases = []
        for selection in request['selections']:
            if any(seed not in names for seed in selection['seeds']): fail('refused','Nonlocal seed')
            case = bridge.closure_certificate(imported,[names[seed] for seed in selection['seeds']])
            case['effective_budget'] = case['required_count'] if selection['budget_records'] is None else selection['budget_records']
            if case['effective_budget'] < case['required_count']: fail('refused','Verified result cannot discharge insufficient-budget request')
            cases.append(case)
        if read_json_bytes(reuse.read(directory/'certificates.json')) != cases:
            fail('refused','Retained certificates differ from current declared closure')
        sources = {'GateData':data_source(imported,raw_sha), 'GateLocalNames':name_source(imported),
                   'GateExternalNames':name_source(imported,True), 'GateIdentities':identities_source(imported),
                   'GateBounds':bounds_source(imported), 'GateModel':model_proof(imported),
                   'GateViews':views_source(imported,cases), 'GateRun':RUNNER}
        required = {'request.json','replay-request.json','input.json','model.json','certificates.json','dynamic-kernel-replay.log','actual-runtime.log'}
        required.update(name+'.lean' for name in PROOF_MODULES)
        required.update(name+suffix for name in PROOF_MODULES[:-1] for suffix in ('.olean','.log'))
        if request['supplied_views']: required.update(('supplied-views.json','view-comparison.json'))
        if not required <= set(members) or observations.get('proof_modules') != list(PROOF_MODULES):
            fail('refused','Required proof source/object/log population is incomplete')
        lock = read_evidence_json(ROOT/'toolchain-lock.json')
        for name, source in sources.items():
            if reuse.read(directory/(name+'.lean')) != source.encode(): fail('refused','Retained generated proof source differs: '+name)
            if name != 'GateRun':
                raw = reuse.read(directory/(name+'.olean'))
                if len(raw)<128 or not raw.startswith(b'olean') or lock['lean']['commit'].encode() not in raw[:128]:
                    fail('refused','Retained object is not selected-compiler Lean object: '+name)
        audit_expected = {'GateLocalNames':name_contract_names(imported,False), 'GateExternalNames':name_contract_names(imported,True),
                          'GateIdentities':identity_contract_names(imported), 'GateBounds':['AC.GateData.edgeBounds','AC.GateData.refBounds'] if len(imported['records'])>256 else [],
                          'GateModel':['AC.GateData.model_checked'], 'GateViews':[f'AC.GateData.{p}{i}' for i in range(len(cases)) for p in ('checked','set','reachability','result','execution_matches_project')]}
        audit = {}
        for name, expected in audit_expected.items():
            audit.update({k:sorted(v) for k,v in _audit(reuse.read(directory/(name+'.log')).decode(),expected).items()})
        if observations.get('theorem_audit') != audit:
            fail('refused','Retained theorem audit differs from complete actual logs')
        counts = {'current_dynamic_proof_invocations':7,'current_kernel_replay_invocations':1,'current_runtime_invocations':1}
        if any(type(observations.get(k)) is not int or observations[k]!=v for k,v in counts.items()):
            fail('refused','Inspector requires a cold proof with7 elaborations,1 kernel replay and1 runtime execution')
        stages = observations.get('stages',[])
        for name in (*PROOF_MODULES[:-1],'dynamic-kernel-replay','actual-runtime'):
            selected = [stage for stage in stages if isinstance(stage,dict) and stage.get('stage')==name]
            if len(selected)!=1 or type(selected[0].get('exit_code')) is not int or selected[0]['exit_code']!=0:
                fail('refused','Missing successful cold execution stage: '+name)
        actual = read_json_bytes(reuse.read(directory/'actual-runtime.log'))
        expected_views = [{'status':'verified','projection':projection_output(imported,c,raw_sha)} for c in cases]
        if actual != {'model':model_output(imported,raw_sha),'views':expected_views}:
            fail('refused','Retained runtime output differs from exact current source and selections')
        if request['supplied_views']:
            expected_views = [graphify_view(imported,c,s) for c,s in zip(cases,request['selections'])]
            comparison = {'status':'equal','supplied_sha256':request['supplied_views']['raw_sha256'],'formal_runtime_sha256':support.sha(directory/'actual-runtime.log'),'boundary_mapping':'a_c.lean.graphify-view/1'}
            if read_json_bytes(reuse.read(directory/'supplied-views.json')) != expected_views or read_evidence_json(directory/'view-comparison.json') != comparison:
                fail('refused','Supplied views or retained correspondence differ')
        if any(observations.get(key)!=len(imported[key]) for key in ('records','references','edges')):
            fail('refused','Retained population observations differ')
        if runtime_identity()!=initial or support.check()!=current_support or reuse.bundle(directory)!=(saved,manifest):
            fail('refused','Runtime, support or evidence changed during inspection')
        answer.update(status='consistent', model=model_identity, inputs=expected_inputs, selections=request['selections'],
                      context_binding=request['context_binding'], required_claims=claims, runtime_identity=initial,
                      selected_request_sha256=digest(request), retained_request_sha256=saved['request_sha256'],
                      evidence={'result_sha256':support.sha(directory/'result.json'),'manifest_sha256':support.sha(directory/'manifest.json'),'members':members},
                      observations={'proof_modules':list(PROOF_MODULES),'theorem_count':len(audit),**counts},
                      checks=['complete-member-integrity','current-runtime-and-support','exact-current-request-inputs',
                              'known-required-obligations','regenerated-proof-sources','complete-theorem-axiom-audit',
                              'cold-stage-consistency','current-runtime-output-correspondence','supplied-view-correspondence'])
    except (GateError,reuse.OriginError) as exc: answer.update(status=exc.status,reason=str(exc))
    except (OSError,ValueError,KeyError,TypeError,RecursionError) as exc: answer.update(status='incomplete',reason=type(exc).__name__+': '+str(exc))
    return answer


