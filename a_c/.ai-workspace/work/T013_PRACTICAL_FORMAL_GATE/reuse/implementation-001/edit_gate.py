from pathlib import Path
stage=Path(__file__).resolve().parent
p=stage/'candidate/a_c/build_tenants/lean/scripts/formal_gate.py'
s=p.read_text()
def replace(a,b):
    global s
    assert a in s,a[:100]
    s=s.replace(a,b,1)
replace("'bootstrap','check','check_gate','formal_gate','formal_support','gate_codegen',", "'bootstrap','check','check_gate','formal_gate','formal_reuse','formal_support','gate_codegen',")
replace("'formal_support','generate_fixture','check','gate_codegen'):", "'formal_reuse','formal_support','generate_fixture','check','gate_codegen'):")
replace('import formal_support as support','import formal_support as support\nimport formal_reuse as reuse')
replace("    return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=bridge._pairs,parse_constant=invalid_constant)","    return reuse.decode(reuse.read(path))")
replace("    pins={str(p.relative_to(ROOT)):support.sha(p) for p in sorted(paths)}", "    selected=reuse.selection()\n    if selected is not None:paths.add(ROOT/reuse.ORIGIN_SELECTION_PIN)\n    pins={str(p.relative_to(ROOT)):support.sha(p) for p in sorted(paths)}")
replace("def verify(request,output_dir,limits=None,*,base_dir=None):\n", '''def verify(request,output_dir,limits=None,*,base_dir=None):
    """Always cold; optional local establishment follows complete actual success."""
    return _verify(request,output_dir,limits,base_dir=base_dir)

def _verify(request,output_dir,limits=None,*,base_dir=None,established=None,reuse_unavailable=None):
''')
replace("started=time.monotonic();limits=DEFAULT_LIMITS|dict(limits or {});out=Path(output_dir).absolute();created=False", "started=time.monotonic();limits=DEFAULT_LIMITS|dict(limits or {});out=Path(output_dir).absolute();created=False;origin=None;completed=False")
replace("        validate_request(request)\n        base=", "        validate_request(request)\n        if set(limits)!=set(DEFAULT_LIMITS) or any(type(v) is not int or v<1 for v in limits.values()):fail('refused','Malformed resource limits')\n        reuse.guard(out,output=True)\n        base=")
replace("            if p.is_symlink():fail('refused','Input symlinks are unsupported')", "            reuse.guard(p)")
replace("                if p.stat().st_size>limits['max_input_bytes']:fail('incomplete','Input exceeds selected byte resource limit')\n                raw=p.read_bytes()", "                raw=reuse.read(p,max_bytes=limits['max_input_bytes'])")
replace("        initial=runtime_identity();result['runtime_identity']=initial", "        initial=runtime_identity();result['runtime_identity']=initial\n        if reuse_unavailable is not None:result['observations']['reuse_unavailable']=reuse_unavailable")
start=s.index("        for name,source in {'GateData':data_source")
end=s.index("        actual=read_json_bytes(log.encode())",start)
cold=s[start:end]
# Keep all current scaling generator, theorem coverage, and compiler ordering.
cold=cold.replace("        prefix,env,_=support.proof_environment(out)","        result['observations']['proof_modules']=['GateData','GateLocalNames','GateExternalNames','GateIdentities','GateBounds','GateModel','GateViews','GateRun']\n        result['observations']['theorem_audit']={}\n        def audit(log,expected):\n            found=_audit(log,expected)\n            result['observations']['theorem_audit'].update({k:sorted(v) for k,v in found.items()})\n        prefix,env,_=support.proof_environment(out)")
cold=cold.replace(':_audit(log,', ':audit(log,')
cold=cold.replace("        log=run([str(prefix/'bin/lean'),'-j','1','-M',str(limits['memory_mb']),'--run',str(out/'GateRun.lean')],'actual-runtime')", "        log=run([str(prefix/'bin/lean'),'-j','1','-M',str(limits['memory_mb']),'--run',str(out/'GateRun.lean')],'actual-runtime')\n        result['observations'].update(current_dynamic_proof_invocations=7,current_kernel_replay_invocations=1,current_runtime_invocations=1)")
reuse_branch='''        else:
            t=time.monotonic();body=established['body'];old=established['directory'];layout=established['hint']['layout']
            if (body['replay_request']!=replay or body['resource_limits']!=limits or body['runtime_identity']!=initial
                    or any(body[k]!=result[k] for k in ('model','inputs','requested_claims'))
                    or body['support']!=result['observations']['support']):
                fail('refused','Current request, input, model, support or limits differ from the original establishment')
            # Copy only authenticated artifacts. Saved objects are inert bytes,
            # never imported by a compiler and never a source of current truth.
            for name,expected in body['members'].items():
                raw=reuse.read(old/reuse.origin_name(name,layout))
                if reuse.sha(raw)!=expected:fail('refused','Original artifact changed before retention')
                if name in ('request.json','replay-request.json'):
                    (out/('origin-'+name)).write_bytes(raw)
                elif name=='view-comparison.json':
                    pass  # rebuilt after current output/view correspondence below
                elif (out/name).exists():
                    if reuse.sha(reuse.read(out/name))!=expected:fail('refused','Current reconstructed artifact differs: '+name)
                else:(out/name).write_bytes(raw)
            for name in ('result.json','manifest.json'):
                raw=reuse.read(old/reuse.origin_name(name,layout))
                if reuse.sha(raw)!=body[name.replace('.json','_sha256')]:fail('refused','Original metadata changed before retention')
                (out/('origin-'+name)).write_bytes(raw)
            log=reuse.read(out/'actual-runtime.log').decode('utf-8')
            result['observations'].update(reuse='local-origin',
                original_establishment={'origin_id':body['origin_id'],'entry_id':established['hint']['entry_id'],
                    'result_sha256':body['result_sha256'],'manifest_sha256':body['manifest_sha256'],
                    'result_path':'origin-result.json','caller_return':'not established by local origin'},
                execution='retained authenticated cold runtime; current source/import/certificate/output correspondence checked',
                proof_modules=body['proof_modules'],theorem_audit=body['theorem_audit'],
                current_dynamic_proof_invocations=0,current_kernel_replay_invocations=0,current_runtime_invocations=0)
            result['observations']['stages'].append({'stage':'authenticated-artifacts','seconds':time.monotonic()-t})
'''
s=s[:start]+"        if established is None:\n"+''.join('    '+line if line.strip() else line for line in cold.splitlines(keepends=True))+reuse_branch+s[end:]
replace("        result['status']='verified'", """        if established is not None:
            for name in ('model.json','certificates.json','view-comparison.json'):
                if name in established['body']['members'] and reuse.sha(reuse.read(out/name))!=established['body']['members'][name]:
                    fail('refused','Current correspondence artifact differs from cold establishment')
            current,reason=reuse.lookup(established['directory'],initial,limits)
            if current!=established:fail('refused','Local establishment changed during reuse')
        else:
            origin,reason=reuse._origin()
            if reason is not None:result['observations']['origin_unavailable']=reason
        if result['requested_claims']!=result['checked_claims']:fail('incomplete','Requested claims were not completely checked')
        result['status']='verified';completed=True""")
replace("    except GateError as e:result.update(status=e.status,reason=e.reason)", "    except GateError as e:result.update(status=e.status,reason=e.reason)\n    except reuse.OriginError as e:result.update(status=e.status,reason=str(e))")
replace("    result['observations']['elapsed_seconds']=time.monotonic()-started", "    result['observations']['elapsed_seconds']=time.monotonic()-started\n    result['observations']['elapsed_scope']='checking only; excludes final bundle/origin publication; complete wall requires external process measurement'")
replace("        write_json(out/'result.json',result)\n    return result", """        write_json(out/'result.json',result)
        if completed:
            try:
                if established is not None:
                    reuse.publish_hint(out,established['body']['origin_id'],established['hint']['entry_id'],'reuse')
                elif origin is not None:reuse._establish(out,origin)
            except (OSError,reuse.OriginError) as exc:
                # The sealed result is immutable. A committed establishment may
                # exist even if publication/return observation is incomplete.
                result=copy.deepcopy(result)
                result.update(status='incomplete',reason='Local origin publication did not complete: '+str(exc))
    return result""")
start=s.index('def check_evidence(')
end=s.index('def _recheck_failure(',start)
s=s[:start]+'''def check_evidence(bundle,output_dir,limits=None):
    try:
        old=reuse.guard(bundle,directory=True);out=reuse.guard(output_dir,output=True)
        if out==old or out.is_relative_to(old) or old.is_relative_to(out):return _recheck_failure('Evidence output overlaps prior bundle')
        saved,manifest=reuse.bundle(old)
        initial=runtime_identity()
        if not reuse.compatible(saved.get('runtime_identity'),initial):return _recheck_failure('Evidence verifier/proof/profile pins are stale')
        original=read_json_bytes(reuse.read(old/'request.json'));replay=read_json_bytes(reuse.read(old/'replay-request.json'))
        validate_request(original);validate_request(replay)
        if digest(original)!=saved.get('request_sha256'):return _recheck_failure('Original request digest changed')
        expected=copy.deepcopy(original)
        expected['input']['path']='input.json'
        if expected['supplied_views']:expected['supplied_views']['path']='supplied-views.json'
        if replay!=expected:return _recheck_failure('Retained replay request differs from original selections/bindings')
        effective=DEFAULT_LIMITS|dict(limits or {})
        if saved['runtime_identity']==initial:
            established,reason=reuse.lookup(old,initial,effective)
        else:
            established,reason=None,'different or absent origin selection; standalone cold verification required'
        return _verify(replay,out,limits,base_dir=old,established=established,reuse_unavailable=reason)
    except reuse.OriginError as e:return _recheck_failure(str(e),e.status)
    except ScriptNamespaceError as e:return _recheck_failure(str(e))
    except GateError as e:return _recheck_failure(e.reason,e.status)
    except (OSError,ValueError,KeyError,TypeError,RecursionError) as e:return _recheck_failure('Evidence unavailable/malformed: '+str(e))

''' +s[end:]
replace("def _recheck_failure(reason):\n    return {'schema':'a_c.formal-gate.result/1','status':'refused'", "def _recheck_failure(reason,status='refused'):\n    return {'schema':'a_c.formal-gate.result/1','status':status")
replace("    sub.add_parser('identity')", "    sub.add_parser('identity')\n    sub.add_parser('init-origin')")
replace("    if args.command=='identity':print(json.dumps(runtime_identity(),sort_keys=True));return 0", "    if args.command=='identity':print(json.dumps(runtime_identity(),sort_keys=True));return 0\n    if args.command=='init-origin':print(json.dumps(reuse.init_origin(),sort_keys=True));return 0")
replace("        req=bridge.read_json(args.request)", "        reuse.guard(args.output,output=True)\n        req=read_json_bytes(reuse.read(args.request))")
replace("    except Exception as e:\n        print(json.dumps(", "    except (GateError,reuse.OriginError) as e:\n        print(json.dumps(_recheck_failure(str(e),e.status),sort_keys=True));sys.exit(EXIT[e.status])\n    except Exception as e:\n        print(json.dumps(")
p.write_text(s)
print('Updated staged formal_gate.py; scaling code retained within the cold branch.')
