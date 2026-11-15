#!/usr/bin/env python3
"""Read an exact public GitHub release and verify every downloaded asset byte."""
import argparse
import hashlib
import json
from pathlib import Path
import time
import urllib.error
import urllib.request


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--release-id', type=int, required=True)
    parser.add_argument('--expected', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    attempts = []

    def get(url):
        for attempt in range(1, 4):
            try:
                request = urllib.request.Request(url, headers={'User-Agent': 'STDO-exact-public-readback/3.1',
                                                               'Accept': 'application/octet-stream' if '/download/' in url else 'application/vnd.github+json'})
                with urllib.request.urlopen(request, timeout=120) as response:
                    data = response.read()
                    attempts.append({'url': url, 'attempt': attempt, 'status': response.status,
                                     'bytes': len(data), 'final_url': response.url})
                    return data
            except (urllib.error.URLError, TimeoutError) as error:
                attempts.append({'url': url, 'attempt': attempt, 'error': str(error)})
                if attempt == 3:
                    raise
                time.sleep(attempt * 2)
            finally:
                (args.out / 'ACQUISITION.json').write_text(json.dumps(attempts, indent=2) + '\n')

    raw = get(f'https://api.github.com/repos/foolishimp/specification_methodology/releases/{args.release_id}')
    (args.out / 'RELEASE_API.json').write_bytes(raw)
    release = json.loads(raw)
    if release['id'] != args.release_id or release['tag_name'] != 'specification_methodology/v3.1.0-rc.2' or release['draft'] or release['prerelease']:
        raise ValueError('Wrong release identity or public status')
    expected = {row['name']: row for row in json.loads(args.expected.read_text())['assets']}
    assets = {asset['name']: asset for asset in release['assets']}
    if len(assets) != len(release['assets']) or set(assets) != set(expected):
        raise ValueError('Unexpected asset set')
    rows = []
    downloads = args.out / 'assets'
    downloads.mkdir()
    for name, asset in sorted(assets.items()):
        data = get(asset['browser_download_url'])
        digest = hashlib.sha256(data).hexdigest()
        if len(data) != expected[name]['bytes'] or digest != expected[name]['sha256']:
            raise ValueError('Downloaded asset differs: ' + name)
        if len(data) != asset['size'] or asset.get('digest') != 'sha256:' + digest:
            raise ValueError('GitHub asset metadata differs: ' + name)
        (downloads / name).write_bytes(data)
        rows.append({'name': name, 'id': asset['id'], 'bytes': len(data), 'sha256': digest,
                     'url': asset['browser_download_url']})
    result = {'kind': 'stdo.public-asset-readback/1', 'release_id': release['id'],
              'url': release['html_url'], 'tag': release['tag_name'],
              'authentication': 'none; public HTTPS GET', 'assets': rows, 'valid': True}
    (args.out / 'ASSET_READBACK.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'valid': True, 'release_id': release['id'], 'assets': len(rows), 'url': release['html_url']}))


if __name__ == '__main__':
    main()
