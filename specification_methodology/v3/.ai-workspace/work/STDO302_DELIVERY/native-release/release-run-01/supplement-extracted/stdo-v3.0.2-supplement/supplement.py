#!/usr/bin/env python3
"""Build a bounded native-source-bound supplement; verify an extracted bundle."""
from pathlib import Path
import argparse
import hashlib
import io
import json
import subprocess
import sys
import tarfile
import tempfile

BASE = Path(__file__).resolve().parent
CUT = 'v3.0.2'
PREFIX = 'stdo-v3.0.2-supplement'


def require(value, message):
    if not value:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()


def read(path):
    return json.loads(Path(path).read_bytes())


def files(root):
    root = Path(root)
    require(root.is_dir() and not root.is_symlink(), 'bundle root missing or redirected')
    result = {}
    for p in sorted(root.rglob('*')):
        require(not p.is_symlink(), 'redirected member')
        if p.is_dir():
            continue
        require(p.is_file(), 'nonregular member')
        result[p.relative_to(root).as_posix()] = p.read_bytes()
    return result


def check_binding(payload):
    selection = json.loads(payload['SOURCE_SELECTION.json'])
    manifest = json.loads(payload['NATIVE_MANIFEST.json'])
    require(selection['kind'] == 'a_c.stdo302.native-source-selection/1', 'wrong native selection kind')
    native = selection['native']
    require(native['cut'] == CUT and manifest['release']['cut'] == CUT, 'wrong native cut')
    require(manifest['release']['profile'] == 'stable-v1', 'wrong release profile')
    require(sha(payload['NATIVE_MANIFEST.json']) == native['manifest_sha256'], 'native manifest digest mismatch')
    for key in ('cut', 'commit', 'tag_object', 'tree', 'standards_tree', 'qualified_ref'):
        require(manifest['release'][key] == native[key], 'native identity mismatch: ' + key)
    require(native['qualified_ref'] == 'refs/tags/specification_methodology/' + CUT, 'wrong native ref')
    require(manifest['release']['project_subtree_root'] == native['package_path'], 'native package root mismatch')
    require(manifest['release']['project_subtree_tree'] == native['package_tree'], 'native package tree mismatch')
    chosen = {v['path']: v for v in selection['files']}
    installed = {'standards/' + v['path']: v for v in manifest['standards']['members']}
    require(sha(payload['source/LICENSE']) == chosen['LICENSE']['sha256'], 'native source license mismatch')
    plan = json.loads(payload['PLAN.json'])
    for row in plan['files']:
        path = row['path']; source = payload['source/' + path]
        require(sha(source) == row['sha256'] == chosen[path]['sha256'] == installed[path]['sha256'], 'representation/native source mismatch: ' + path)
    for section in json.loads(payload['SOURCE_SECTIONS.json'])['segments']:
        lines = payload['source/' + section['path']].decode().splitlines(keepends=True)
        exact = ''.join(lines[section['start_line']-1:section['end_line']])
        require(exact == section['text'] and sha(exact.encode()) == section['sha256'], 'section grounding mismatch')
    return selection


def verify(bundle):
    payload = files(bundle)
    inventory = json.loads(payload.pop('BUNDLE_MANIFEST.json'))
    expected = {row['path']: row for row in inventory['files']}
    require(set(payload) == set(expected), 'bundle membership mismatch')
    for name, raw in payload.items():
        require(len(raw) == expected[name]['bytes'] and sha(raw) == expected[name]['sha256'], 'bundle bytes mismatch: ' + name)
    require(sha(payload['SOURCE_SELECTION.json']) == inventory['selection_sha256'], 'selection digest mismatch')
    check_binding(payload)
    model = json.loads(payload['MODEL.json']); commands = []
    with tempfile.TemporaryDirectory(prefix='stdo302-supplement-verify-') as tmp:
        for carrier in ('CARRIER.json', 'GRAPHIFY_EXTRACTION.json'):
            out = Path(tmp) / (carrier + '.recovered.json')
            argv = [sys.executable, '-I', '-B', str(Path(bundle)/'tools/ac_graph.py'), 'decode', str(Path(bundle)/carrier), '--out', str(out)]
            p = subprocess.run(argv, capture_output=True, text=True)
            require(p.returncode == 0, 'carrier decode refused: ' + p.stderr + p.stdout)
            require(read(out) == model, 'carrier recovery differs')
            commands.append({'argv': argv, 'exit': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr})
    return {'kind':'stdo302.supplement-verification/1','files':len(payload),'selection_sha256':inventory['selection_sha256'],
            'recovery':'equal JSON values; raw serialization equality not claimed','commands':commands,
            'limits':'Source custody and carrier recovery; no independent semantic acceptance or whole-method coverage'}


def build(args):
    bundle, archive = Path(args.bundle).absolute(), Path(args.archive).absolute()
    for p in (bundle, archive):
        require('..' not in p.parts and p.is_relative_to(BASE), 'build output outside native-release territory')
        require(not any(x.is_symlink() for x in (p, *p.parents)), 'redirected output path')
        require(not p.exists(), 'preserve existing output')
    require(not archive.is_relative_to(bundle) and not bundle.is_relative_to(archive), 'overlapping archive/bundle output paths')
    selection = Path(args.selection).read_bytes()
    require(sha(selection) == args.selection_sha256, 'selection pin mismatch')
    payload = files(args.representation)
    payload['SOURCE_SELECTION.json'] = selection
    payload['NATIVE_MANIFEST.json'] = (Path(args.selection).parent/'stdo-v3.0.2-manifest.json').read_bytes()
    repo = Path(args.repo)
    decoder = repo/'a_c/build_tenants/graphify/code/ac_graph.py'
    pins = json.loads(payload['TOOL_PINS.json'])
    require(sha(decoder.read_bytes()) == pins['a_c/build_tenants/graphify/code/ac_graph.py'], 'decoder pin mismatch')
    payload['tools/ac_graph.py'] = decoder.read_bytes()
    payload['source/LICENSE'] = (repo/'specification_methodology/v3/build_tenants/common/LICENSE').read_bytes()
    payload['DISTRIBUTION.md'] = b'Native source/LICENSE retains its native-source scope. The pinned a_c decoder, authored interpretation and packaging keep their source ownership; this bundle assigns them no new license. Distribution is selected by the Product owner; see the exact release record.\n'
    payload['supplement.py'] = Path(__file__).read_bytes()
    check_binding(payload)
    rows = [{'path':p,'bytes':len(raw),'sha256':sha(raw)} for p,raw in sorted(payload.items())]
    payload['BUNDLE_MANIFEST.json'] = canonical({'kind':'stdo302.supplement-inventory/1','selection_sha256':args.selection_sha256,'files':rows})
    bundle.mkdir(parents=True)
    for name, raw in payload.items():
        p = bundle/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
    result = verify(bundle)
    archive.parent.mkdir(parents=True,exist_ok=True)
    # Enumerate fixed verified bytes before opening the output; output overlap is refused above.
    with archive.open('xb') as output, tarfile.open(fileobj=output,mode='w:gz') as tar:
        for name, raw in sorted(payload.items()):
            info=tarfile.TarInfo(PREFIX+'/'+name);info.size=len(raw);info.mtime=0;info.mode=0o644
            tar.addfile(info,io.BytesIO(raw))
    return {'kind':'stdo302.supplement-build/1','archive':str(archive),'sha256':sha(archive.read_bytes()),'bundle':str(bundle),'verification':result}


def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='command',required=True)
    p=sub.add_parser('verify');p.add_argument('--bundle',required=True,type=Path)
    p=sub.add_parser('build')
    for name in ('repo','representation','selection','bundle','archive'):p.add_argument('--'+name,required=True,type=Path)
    p.add_argument('--selection-sha256',required=True)
    args=parser.parse_args()
    try:
        print(json.dumps(verify(args.bundle) if args.command=='verify' else build(args),sort_keys=True))
    except (ValueError,OSError,KeyError,json.JSONDecodeError) as error:
        parser.exit(1,'refused: '+str(error)+'\n')


if __name__=='__main__':main()
