from pathlib import Path
import hashlib,json,os,subprocess,sys,time
proof=Path(__file__).resolve().parent
a=json.loads((proof/"ACTIVATION.json").read_bytes()); temporary=Path(a["temporary_root"])
root=Path(a["checkout"])
stage=sys.argv[1]; output=proof/stage; output.mkdir()
python=root/".venv/bin/python"
owned=list(a["source_preimages"])
dependencies=owned+["build_tenants/graphify/code/ac_support.py","build_tenants/graphify/code/ac_support_effects.py","build_tenants/graphify/code/ac_graph.py","build_tenants/graphify/design/fd-support.md","build_tenants/graphify/design/fd-method-claude-rc9.json"]
pins=lambda:{name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in dependencies}
env=dict(os.environ)
for key in list(env):
 if (key.startswith("AC_") and key.endswith("_TEST_EVIDENCE")) or key in ("AC_SUPPORT_EFFECTS_PROOF_ROOT","A_C_CORE_QUALIFICATION_CUSTODY"): env.pop(key)
env.update({"PYTHONDONTWRITEBYTECODE":"1","PYTHONPATH":str(root/"build_tenants/graphify/code")+os.pathsep+str(root/"build_tenants/graphify/test_env"),"MYPYPATH":str(root/"build_tenants/graphify/code")+os.pathsep+str(root/"build_tenants/graphify/test_env"),"TMPDIR":str(temporary),"TMP":str(temporary),"TEMP":str(temporary),"PYTHONPYCACHEPREFIX":str(temporary/"bytecode"),"MYPY_CACHE_DIR":str(temporary/"mypy"),"XDG_CACHE_HOME":str(temporary/"cache")})
if stage=="focused-after":
 command=[str(python),"-B","-m","unittest","-v","test_ac_support_core.CoreTests","test_ac_support_interfaces.PublicJudgmentIngressTests"]
 env.update({"AC_JUDGMENT_INGRESS_TEST_EVIDENCE":str(output/"public"),"A_C_CORE_QUALIFICATION_CUSTODY":str(output/"core-fixtures")})
elif stage=="typing":
 command=[str(python),"-B","-m","mypy","--strict","--cache-dir",str(temporary/"mypy"),*[str(root/name) for name in owned]]
else: raise ValueError(stage)
record={"stage":stage,"command":command,"cwd":str(root/"build_tenants/graphify"),"environment_overrides":{key:value for key,value in env.items() if key in ("PYTHONDONTWRITEBYTECODE","PYTHONPATH","MYPYPATH","TMPDIR","PYTHONPYCACHEPREFIX","MYPY_CACHE_DIR","XDG_CACHE_HOME","AC_JUDGMENT_INGRESS_TEST_EVIDENCE","A_C_CORE_QUALIFICATION_CUSTODY")},"started_ns":time.time_ns(),"source_before":pins(),"scope":"Focused judgment ingress and affected core consumers; no provider, network, native actor, full suite, semantic acceptance or release claim."}
(output/"command.json").write_text(json.dumps(record,indent=2)+"\n")
run=subprocess.run(command,cwd=root/"build_tenants/graphify",env=env,capture_output=True,check=False,timeout=90)
(output/"stdout").write_bytes(run.stdout); (output/"stderr").write_bytes(run.stderr)
record.update({"ended_ns":time.time_ns(),"exit":run.returncode,"source_after":pins()})
record["owned_sources_unchanged"]=all(record["source_before"][name]==record["source_after"][name] for name in owned)
(output/"execution.json").write_text(json.dumps(record,indent=2)+"\n")
with (proof/"commands.jsonl").open("a") as stream:stream.write(json.dumps(record)+"\n")
print(run.stdout.decode()); print(run.stderr.decode()); print("retained_exit",run.returncode,"owned_sources_unchanged",record["owned_sources_unchanged"])
raise SystemExit(run.returncode)
