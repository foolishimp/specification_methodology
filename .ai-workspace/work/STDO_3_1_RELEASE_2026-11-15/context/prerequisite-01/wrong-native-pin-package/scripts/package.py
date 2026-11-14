#!/usr/bin/env python3
"""Create an exact development or explicitly native-release-matched Skills package."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil

ROOT=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--version')
    parser.add_argument('--method-root',type=Path)
    parser.add_argument('--method-manifest-sha256')
    args=parser.parse_args()
    release=None
    if any((args.version,args.method_root,args.method_manifest_sha256)):
        if not all((args.version,args.method_root,args.method_manifest_sha256)):
            parser.error('Release packaging requires version, method-root and selected method-manifest-sha256')
        if not re.fullmatch(r'\d+\.\d+\.\d+(?:-rc\.\d+)?',args.version):
            parser.error('Invalid exact release version')
        native_path=args.method_root.absolute()/'manifest.json'
        if not native_path.is_file() or any(p.is_symlink() for p in (native_path,*native_path.parents)):
            parser.error('Native manifest must be a physical regular file')
        raw=native_path.read_bytes();native=json.loads(raw)
        if hashlib.sha256(raw).hexdigest()!=args.method_manifest_sha256 or native.get('kind')!='stdo.installed-release-manifest' or native['release']['cut']!='v'+args.version:
            parser.error('Actual native cut or manifest differs from the selected release')
        release={'version':args.version,'native_method':{'uri':'stdo://releases/v'+args.version+'/',
                 'manifest_sha256':args.method_manifest_sha256}}
    out=args.out.absolute()
    if out.exists() or out.is_symlink() or out.resolve().is_relative_to(ROOT/'release'):
        parser.error('Select a fresh package directory outside release/')
    paths=[ROOT/x for x in ['README.md','GETTING_STARTED.md','RELEASE.md','AGENTS.md','CLAUDE.md','stdo_skills.json','build_tenants/README.md',*[f'build_tenants/{h}/README.md' for h in ['codex','claude']]]]
    for base in [ROOT/'scripts',ROOT/'specification',ROOT/'skills',*(ROOT/'build_tenants'/h/'current' for h in ['codex','claude'])]:
        paths.extend(p for p in base.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    files=[]
    for p in sorted(paths):
        if p.is_symlink():raise ValueError('Package source must not be a symlink')
        b=p.read_bytes();files.append({'path':p.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
    manifest={'kind':'stdo-skills.development-package/1','product_definition_id':'urn:stdo:product-definition:stdo-skills','standing':'unversioned source development package; not a released cut','files':files}
    if release:
        manifest.update(kind='stdo-skills.release-package/1',release=release,
                        standing='Exact release-matched candidate package; publication and qualification are external records.')
    out.mkdir(parents=True,exist_ok=False)
    for row in files:
        dest=out/row['path'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/row['path'],dest)
    (out/'INVENTORY.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'packaged','path':str(out),'files':len(files),'inventory_sha256':hashlib.sha256((out/'INVENTORY.json').read_bytes()).hexdigest()}))


if __name__=='__main__':main()
