from pathlib import Path
import hashlib, json, sys
root = Path(sys.argv[1])
release = json.loads((root / 'release.json').read_bytes())
if release.get('tag_name') != 'specification_methodology/v3.0.5-rc.1' or release.get('draft') is not False or release.get('prerelease') is not False:
    raise SystemExit('wrong fixed RC release or publication status')
names = {'stdo_toolchain-3.0.5rc1-py3-none-any.whl', 'stdo-v3.0.5-rc.1-manifest.json',
         'stdo-manager-runtime-v3.0.5-rc.1-macos-arm64-cp313.zip',
         'stdo-manager-constraints-v3.0.5-rc.1-python313.txt', 'stack-release-v3.0.5-rc.1.json'}
assets = release.get('assets', [])
if len(assets) != len(names) or {a['name'] for a in assets} != names:
    raise SystemExit('release asset population differs')
for asset in assets:
    raw = (root / asset['name']).read_bytes()
    if len(raw) != asset['size'] or asset.get('digest') != 'sha256:' + hashlib.sha256(raw).hexdigest():
        raise SystemExit('release asset checksum mismatch: ' + asset['name'])
