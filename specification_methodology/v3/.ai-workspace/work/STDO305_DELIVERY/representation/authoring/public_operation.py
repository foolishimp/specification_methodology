"""Record exact public-provider invocation and observed local process costs."""
import hashlib,json,pathlib,resource,subprocess,sys,time
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE
while not (ROOT/'stdo_representation').is_dir():ROOT=ROOT.parent
PINS=json.loads((HERE.parent.parent/'tools-skills/project-provider-305.json').read_text())
ENTRY=pathlib.Path(PINS['entrypoint'])
for path,digest in PINS['files'].items():
    assert hashlib.sha256((ENTRY.parent/path).read_bytes()).hexdigest()==digest,path
RUN=ROOT/'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5/run-coherent-003'
name=sys.argv[1]
argv=[PINS['python'],'-B',str(ENTRY),name,'--run',str(RUN)]+sys.argv[2:]
prefix=HERE/('public-'+name)
assert not prefix.with_suffix('.receipt.json').exists(),'retain each actual invocation; choose a distinct receipt name before retry'
start=time.monotonic();before=resource.getrusage(resource.RUSAGE_CHILDREN)
result=subprocess.run(argv,capture_output=True,text=True)
after=resource.getrusage(resource.RUSAGE_CHILDREN)
prefix.with_suffix('.stdout.json').write_text(result.stdout)
prefix.with_suffix('.stderr.txt').write_text(result.stderr)
receipt={'kind':'stdo305.public-provider-invocation/1','argv':argv,'returncode':result.returncode,
         'elapsed_seconds':time.monotonic()-start,'user_cpu_seconds':after.ru_utime-before.ru_utime,
         'system_cpu_seconds':after.ru_stime-before.ru_stime,'max_rss_bytes_macos':after.ru_maxrss,
         'stdout_sha256':hashlib.sha256(result.stdout.encode()).hexdigest(),
         'stderr_sha256':hashlib.sha256(result.stderr.encode()).hexdigest(),
         'standing':'actual public API execution; costs cover this subprocess, not LLM authoring/context or independent acceptance'}
prefix.with_suffix('.receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(result.stdout);print(result.stderr);print(json.dumps(receipt,indent=2));sys.exit(result.returncode)
