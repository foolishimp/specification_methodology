The selected proof is [ARTIFACT_PROOF.json](ARTIFACT_PROOF.json). Its copied executable sources and probe inputs are persisted here; the `/private/tmp` location in `PROBE_LOCATION.json` is a convenience, not durable authority. `SOURCE_MANIFEST.json` gives the exact frozen commit, paths, sizes and hashes needed to reconstruct the read-only source snapshot.

For a later authorized replay, run the following from this assessment directory. It reads Git objects, verifies copied bytes, and writes only a new disposable directory and report. It never invokes an actor's `acquire.py`, construction script, checker, or result-writing finalizer. The replay's timestamps will differ from the selected proof; compare observed values and source identities.

```python
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile

assessment = Path.cwd()
repo = Path('/Users/jim/src/apps/specification_methodology-codex')
manifest = json.loads((assessment / 'SOURCE_MANIFEST.json').read_text())
scratch = Path(tempfile.mkdtemp(prefix='i3r2-proof-replay-', dir='/private/tmp'))
snapshot = scratch / 'snapshot'
for record in manifest['sources']:
    raw = subprocess.check_output([
        'git', '-C', str(repo), 'show',
        manifest['commit'] + ':' + record['path'],
    ])
    assert len(raw) == record['bytes']
    assert hashlib.sha256(raw).hexdigest() == record['sha256']
    destination = snapshot / record['relative_snapshot_path']
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(raw)
subprocess.run([
    sys.executable, '-B', str(assessment / 'run_artifact_probe.py'),
    '--snapshot', str(snapshot), '--output', str(scratch / 'REPLAY_PROOF.json'),
], check=True)
print(scratch / 'REPLAY_PROOF.json')
```

`assemble_assessment.py` serializes this assessor's judgments and their exact evidence extractions. It is not an automated correctness oracle and is not needed to replay the executable proof. `GRADES.json` remains the selected fixed-rubric assessment; rerunning the assembly script or changing expectations does not authorize a new trial.
