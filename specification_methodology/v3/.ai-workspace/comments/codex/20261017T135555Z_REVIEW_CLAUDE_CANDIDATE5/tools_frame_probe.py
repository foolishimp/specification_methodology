"""Reproduce changed-frame pin checks; reads frozen Git blobs only.
Run: python3 -B tools_frame_probe.py /path/to/specification_methodology
"""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

REPO = Path(sys.argv[1]).resolve()
A = '4a63c9293ddaa568803b81f1ed5dcc1d3dc19cec'
OLD = '9e901690e9f9b66917cafd917fff9ad755efa2a6'
PREFIX = 'specification_methodology/v3/build_tenants/claude/'


def blob(path, ref=A):
    return subprocess.check_output(['git', '-C', str(REPO), 'show', ref + ':' + PREFIX + path])


def sha(value):
    return hashlib.sha256(value).hexdigest()


current = json.loads(blob('standards/frames/FRAME_INPUTS.json'))
prior = {f['id']: f for f in json.loads(blob('standards/frames/FRAME_INPUTS.json', OLD))['frames']}
rows = []
for frame in current['frames']:
    if frame['id'] not in ('bootstrap', 'binding', 'dm-task-d'):
        continue
    data = blob(frame['path'])
    assert len(data) == frame['bytes'] and sha(data) == frame['sha256']
    pins = []
    for route in frame['routes'] + frame.get('binds', []):
        if not route.get('owner'):
            continue
        assert sha(blob(route['owner'])) == route['owner_sha256']
        pins.append({'owner': route['owner'], 'anchor': route['anchor'], 'member_sha256': route['owner_sha256']})
    olddata = blob(prior[frame['id']]['path'], OLD)
    strip = lambda value: re.sub(rb'(?<=sha256=)[0-9a-f]{64}', b'<owner-digest>', value)
    rows.append({'frame': frame['id'], 'bytes': len(data), 'sha256': sha(data),
                 'owner_pin_count': len(pins), 'only_owner_identity_changed': strip(data) == strip(olddata),
                 'routes': pins})
print(json.dumps({'source_A': A, 'previous_source': OLD, 'frames': rows,
                  'result': 'all changed frame sizes, digests and full-owner pins match source A',
                  'limits': 'Copy identity and owner pins do not establish task sufficiency or actual use.'}, indent=2))
