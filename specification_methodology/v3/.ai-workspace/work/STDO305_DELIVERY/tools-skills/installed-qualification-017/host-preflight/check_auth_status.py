"""Use documented status commands; retain only coarse non-secret availability."""
from pathlib import Path
import json
import subprocess
import time

ROOT = Path(__file__).absolute().parent
ROWS = []
for host, argv in (
    ('codex', ['/Users/jim/bin/codex', 'login', 'status']),
    ('claude', ['/Users/jim/.local/bin/claude', 'auth', 'status', '--json']),
):
    start = time.time_ns()
    observed = subprocess.run(argv, capture_output=True, timeout=30)
    end = time.time_ns()
    available = None
    shape = 'unrecognized'
    if host == 'codex':
        # No raw output, account identity, key, token, or output digest is retained.
        status = (observed.stdout + observed.stderr).decode(errors='replace')
        if 'Logged in using' in status:
            available = True
            shape = 'recognized logged-in status'
        elif 'Not logged in' in status:
            available = False
            shape = 'recognized logged-out status'
        del status
    else:
        try:
            status = json.loads(observed.stdout)
            if type(status.get('loggedIn')) is bool:
                available = status['loggedIn']
                shape = 'recognized loggedIn boolean'
            del status
        except (ValueError, AttributeError):
            pass
    ROWS.append({'host': host, 'argv': argv, 'returncode': observed.returncode,
                 'started_ns': start, 'ended_ns': end, 'elapsed_seconds': (end-start)/1e9,
                 'authentication_status_reported_available': available, 'parsed_shape': shape,
                 'raw_status_output_retained': False})
    del observed

result = {'schema': 'stdo305.native-host-auth-preflight/1', 'rows': ROWS,
          'selected_model_calls': 0,
          'standing': 'CLI-reported authentication availability only. No credential file/value read by this recorder, no raw authentication output retained, no model access/entitlement/quality or resolved-model claim.'}
with (ROOT / 'AUTH_STATUS.json').open('x') as stream:
    json.dump(result, stream, indent=2, sort_keys=True)
    stream.write('\n')
print(json.dumps(result))
