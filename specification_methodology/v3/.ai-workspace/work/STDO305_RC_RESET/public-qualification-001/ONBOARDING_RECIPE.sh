set -eu
STDO_CUT='v3.0.5-rc.1'
STDO_ASSETS='https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology%2Fv3.0.5-rc.1'
STDO_MANAGER_ENV="$HOME/.local/share/stdo-toolchain-3.0.5-rc.1"
STDO_STORE_ROOT="$HOME/.local/share/stdo-store-3.0.5-rc.1"
STDO_DOWNLOAD_DIR="$(mktemp -d)"
curl --fail --location --output "$STDO_DOWNLOAD_DIR/release.json" \
  'https://api.github.com/repos/foolishimp/specification_methodology/releases/tags/specification_methodology%2Fv3.0.5-rc.1'
for asset in stdo_toolchain-3.0.5rc1-py3-none-any.whl stdo-v3.0.5-rc.1-manifest.json stdo-manager-runtime-v3.0.5-rc.1-macos-arm64-cp313.zip stdo-manager-constraints-v3.0.5-rc.1-python313.txt stack-release-v3.0.5-rc.1.json; do
  curl --fail --location --output "$STDO_DOWNLOAD_DIR/$asset" "$STDO_ASSETS/$asset"
done
python3.13 - "$STDO_DOWNLOAD_DIR" <<'PYVERIFY'
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
PYVERIFY
test ! -e "$STDO_MANAGER_ENV"
python3.13 -m zipfile -e "$STDO_DOWNLOAD_DIR/stdo-manager-runtime-v3.0.5-rc.1-macos-arm64-cp313.zip" "$STDO_DOWNLOAD_DIR/runtime"
python3.13 -m venv "$STDO_MANAGER_ENV"
"$STDO_MANAGER_ENV/bin/python" -m pip install --no-index --find-links "$STDO_DOWNLOAD_DIR/runtime/wheels" --require-hashes --no-deps -r "$STDO_DOWNLOAD_DIR/runtime/requirements-macos-arm64-cp313.txt"
"$STDO_MANAGER_ENV/bin/python" -m pip check
stdo() { "$STDO_MANAGER_ENV/bin/stdo" --store "$STDO_STORE_ROOT" "$@"; }
stdo --version
STDO_MANIFEST="$(python3.13 -c 'import hashlib,sys; print(hashlib.sha256(open(sys.argv[1],"rb").read()).hexdigest())' "$STDO_DOWNLOAD_DIR/stdo-v3.0.5-rc.1-manifest.json")"
stdo install "$STDO_CUT" --repository https://github.com/foolishimp/specification_methodology.git --manifest-sha256 "$STDO_MANIFEST"
stdo verify "$STDO_CUT" --manifest-sha256 "$STDO_MANIFEST"
