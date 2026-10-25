"""Independent bounded probes. Synthetic release identities; no Git effects."""
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import copy
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tarfile
import tempfile

HERE = Path(__file__).resolve().parent
WORK = HERE.parent.parent
REPO = WORK.parents[4]

def module(name):
    path = WORK / 'native-release' / (name + '.py')
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value

n, s = module('native_release'), module('supplement')
cases = []

def refused(name, call):
    try:
        call()
    except (ValueError, FileExistsError) as error:
        cases.append({'case': name, 'result': 'refused', 'reason': str(error)})
    else:
        raise AssertionError('unexpected acceptance: ' + name)

with tempfile.TemporaryDirectory(prefix='synthetic-', dir=HERE) as temp:
    root = Path(temp)
    n.BASE = s.BASE = root
    rep = WORK / 'representation'
    plan = s.read(rep / 'PLAN.json')
    rows = [{'path': row['path'], 'sha256': row['sha256']} for row in plan['files']]
    rows.append({'path': 'LICENSE', 'sha256': s.sha((REPO / 'specification_methodology/v3/build_tenants/common/LICENSE').read_bytes())})
    native = dict(cut='v3.0.2', commit='1'*40, tag_object='2'*40, tree='3'*40,
                  standards_tree='4'*40, qualified_ref=n.TAG, package_path=n.PREFIX,
                  package_tree='5'*40)
    release = {k: native[k] for k in ('cut', 'commit', 'tag_object', 'tree', 'standards_tree', 'qualified_ref')}
    release.update(profile='stable-v1', project_subtree_root=n.PREFIX, project_subtree_tree=native['package_tree'])
    manifest = s.canonical({'release': release, 'standards': {'members': [
        {'path': row['path'].removeprefix('standards/'), 'sha256': row['sha256']}
        for row in rows if row['path'].startswith('standards/')]}})
    native['manifest_sha256'] = s.sha(manifest)
    selection = s.canonical({'kind': 'a_c.stdo302.native-source-selection/1', 'native': native,
                            'files': rows, 'fixture': 'synthetic identity; never a release receipt'})
    (root / 'SOURCE_SELECTION.json').write_bytes(selection)
    (root / n.MANIFEST_NAME).write_bytes(manifest)
    args = SimpleNamespace(repo=REPO, representation=rep, selection=root/'SOURCE_SELECTION.json',
                           selection_sha256=s.sha(selection), bundle=root/'bundle', archive=root/'bundle.tar.gz')
    refused('archive output inside bundle', lambda: s.build(SimpleNamespace(**{**vars(args), 'archive': args.bundle/'nested.tar.gz'})))
    assert not args.bundle.exists()
    result = s.build(args)
    extracted = root / 'extracted'
    with tarfile.open(args.archive) as archive:
        archive.extractall(extracted, filter='data')
    bundle = extracted / s.PREFIX
    command = [sys.executable, '-I', '-S', '-B', str(bundle/'supplement.py'), 'verify', '--bundle', str(bundle)]
    environment = {**os.environ, 'PYTHONPATH': '/nonexistent-reviewer-poison'}
    result = subprocess.run(command, cwd='/', env=environment, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr + result.stdout
    cases.append({'case': 'portable extracted bundle with poisoned PYTHONPATH', 'result': 'passed',
                  'exit': result.returncode, 'verification': json.loads(result.stdout)})
    refused('existing bundle preserved', lambda: s.build(args))
    payload = s.files(args.bundle)
    bad = copy.deepcopy(payload)
    bad['source/standards/RELEASE.md'] += b'\nindependent probe\n'
    refused('native source mismatch', lambda: s.check_binding(bad))
    bad = copy.deepcopy(payload)
    changed = json.loads(bad['NATIVE_MANIFEST.json'])
    changed['release']['qualified_ref'] = 'refs/tags/specification_methodology/v3.0.2-rc.1'
    bad['NATIVE_MANIFEST.json'] = s.canonical(changed)
    changed_selection = json.loads(bad['SOURCE_SELECTION.json'])
    changed_selection['native']['manifest_sha256'] = s.sha(bad['NATIVE_MANIFEST.json'])
    bad['SOURCE_SELECTION.json'] = s.canonical(changed_selection)
    refused('ref contradiction despite refreshed manifest hash', lambda: s.check_binding(bad))

    # The actual publication planner, with read-only Git observations substituted.
    # All objects below are synthetic; no Git command or real tag is used.
    run = root / 'publication'; run.mkdir()
    data = {'standards/README.md': b'synthetic payload\n'}
    selected = {'source_candidate': {'commit': '6'*40}, 'native': native,
                'files': [{'path': p, 'bytes': len(raw), 'sha256': n.sha(raw)} for p, raw in data.items()]}
    selected_raw = n.canonical(selected); selection_sha = n.sha(selected_raw)
    (run/'SOURCE_SELECTION.json').write_bytes(selected_raw)
    (run/n.MANIFEST_NAME).write_bytes(manifest)
    store = run/'store'; installed = store/'releases'/n.CUT
    for name, raw in {**data, 'manifest.json': manifest}.items():
        target=installed/name; target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
    (run/'installed-local.json').write_bytes(n.canonical({'selection_sha256': selection_sha,
        'exact_payload_and_manifest': True, 'store': str(store)}))
    wheel = run/n.MANAGER_WHEEL;wheel.write_bytes(b'synthetic wheel; not executable')
    supplement = run/'supplement.tar.gz'; supplement.write_bytes(b'synthetic supplement; not an archive')
    asset_result=n.assets(SimpleNamespace(run=run,selection_sha256=selection_sha,
        file=[run/n.MANIFEST_NAME,wheel,supplement]))
    refs={'refs/heads/main':'7'*40, 'refs/tags/specification_methodology/v3.0.1-rc.1':'8'*40,
          'refs/tags/specification_methodology/v3.0.1-rc.1^{}':n.PREDECESSOR}
    publication_args=SimpleNamespace(run=run,repo=REPO,selection_sha256=selection_sha,
        assets_sha256=asset_result['sha256'],carrier_commit='9'*40)
    facts={k:v for k,v in native.items() if k!='manifest_sha256'}
    def observed_text(repo,*args):
        if args==('rev-parse',n.TAG):return native['tag_object']
        if args==('rev-parse','refs/heads/release/specification_methodology/3.0.2'):return native['commit']
        raise AssertionError(args)
    with patch.object(n,'commit',side_effect=lambda repo,value:value), patch.object(n,'git',return_value=b''), \
         patch.object(n,'native_facts',return_value=facts), patch.object(n,'text_git',side_effect=observed_text), \
         patch.object(n,'remote_refs',return_value=refs):
        publication=n.publication_plan(publication_args)
    proof=json.loads(Path(publication['path']).read_text())
    assert set(proof['sources'])=={'refs/heads/main',n.TAG,'refs/heads/release/specification_methodology/3.0.2'}
    assert '--atomic' in proof['push_argv']
    assert '--force-with-lease='+n.TAG+':' in proof['push_argv']
    cases.append({'case':'publication planner exact destination and lease scope','result':'passed',
                  'sources':proof['sources'],'argv':proof['push_argv']})
    for ref in ['refs/tags/v3.0.2','refs/tags/specification_methodology/v3.0.2-rc.1']:
        refused('legacy collision '+ref,lambda ref=ref:n.stable_line_available({**refs,ref:'a'*40}))
    after={**refs,**proof['sources'],n.TAG+'^{}':native['commit']}
    with patch.object(n,'remote_refs',return_value={**after,'refs/heads/unrelated':'b'*40}):
        refused('public readback preserves unrelated-ref claim',lambda:n.published(SimpleNamespace(
            run=run,repo=REPO,plan_sha256=publication['sha256'])))

record={'scope':'Bounded independent source/packager probes; synthetic native identities; no Git effects, actual release or manager proof',
        'candidate':{'native_tools_sha256':'3f9dee1ba83d882d3aa97bd9d86032f2688cba000c8b804f0f7660583ac1adc3',
                     'representation_sha256':'827ad7ec3b76b6416381f6415065817e85d425fb6819172110f58f66093e0b41'},
        'cases':cases}
with (HERE/'RESULTS.json').open('x') as output:json.dump(record,output,indent=2);output.write('\n')
print(json.dumps({'cases':len(cases),'passed':True,'record':str(HERE/'RESULTS.json')}))
