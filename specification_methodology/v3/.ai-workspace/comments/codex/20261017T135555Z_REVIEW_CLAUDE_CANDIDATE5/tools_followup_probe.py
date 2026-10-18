"""Narrow follow-up: correct the host interpreter and bound enumeration failure.

Run with the existing builder environment, after tools_failure_probe.py:
  /Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B tools_followup_probe.py REPO
Reads its receipt to reuse only that run's isolated scratch; writes no worktree.
"""
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import time
import jsonschema

REPO = Path(sys.argv[1]).resolve()
OUT = REPO / 'specification_methodology/v3/.ai-workspace/comments/codex/20261017T135555Z_REVIEW_CLAUDE_CANDIDATE5'
prior = json.loads((OUT / 'TOOLS_FAILURE_RECEIPT.json').read_bytes())
ROOT = Path(prior['scratch'])
assert ROOT.is_relative_to(Path('/private/tmp'))
PREFIX = 'specification_methodology/v3/build_tenants/claude'
TENANT = ROOT / 'snapshot' / PREFIX
ENV = dict(os.environ, GIT_DIR=str(REPO / '.git'), PYTHONDONTWRITEBYTECODE='1')
ROWS = []


def run(name, command, expected_zero, extra=None):
    r = subprocess.run(command, cwd=TENANT, env=dict(ENV, **(extra or {})),
                       capture_output=True, text=True, timeout=60)
    row = {'name': name, 'command': [str(x) for x in command],
           'exit': r.returncode, 'expected_zero': expected_zero,
           'expectation_holds': (r.returncode == 0) == expected_zero,
           'stdout_tail': r.stdout[-2500:], 'stderr_tail': r.stderr[-1200:]}
    (ROOT / (name + '.stdout')).write_text(r.stdout)
    (ROOT / (name + '.stderr')).write_text(r.stderr)
    ROWS.append(row)
    return row


# No unchanged test suite is repeated: only previously unavailable install cases.
cmd = [sys.executable, '-I', 'release/check_install.py']
row = run('install-positive-correct-interpreter', cmd + [str(ROOT / 'install-correct')], True)
record = json.loads((TENANT / 'release/INSTALL_CHECK.json').read_bytes())
row['installed_files'] = record['installed_files']
row['outside_links'] = len(record['links_outside_package'])
row['missing_anchors'] = len(record['links_with_missing_anchor'])
manifest = TENANT / 'release/manifest.json'
saved = manifest.read_bytes()
m = json.loads(saved)
m['standards']['members'] = [x for x in m['standards']['members'] if x['path'] != 'schemas/product-definition.schema.json']
manifest.write_text(json.dumps(m))
run('install-missing-bootstrap-correct-interpreter', cmd + [str(ROOT / 'install-missing-correct')], False)
manifest.write_bytes(saved)

# Keep check_install.py unchanged. Substitute one Git response to exercise its
# newly gated bad_anchor report, rather than relying only on an exception path.
shimdir = ROOT / 'git-response-shim'
shimdir.mkdir(exist_ok=True)
hook = f"{prior['source_A']}:{PREFIX}/standards/FOUNDATIONS.md"
shim = shimdir / 'git'
shim.write_text('#!' + sys.executable + '\nimport subprocess,sys\n'
                'r=subprocess.run(["/usr/bin/git",*sys.argv[1:]],capture_output=True)\n'
                'sys.stdout.buffer.write(r.stdout)\n'
                'sys.stderr.buffer.write(r.stderr)\n'
                f'if sys.argv[1:]==["show",{hook!r}]: sys.stdout.buffer.write(b"\\n[reviewer adverse](#reviewer-absent-anchor)\\n")\n'
                'sys.exit(r.returncode)\n')
shim.chmod(0o755)
row = run('install-reported-missing-anchor', cmd + [str(ROOT / 'install-anchor-adverse')], False,
          {'PATH': str(shimdir) + os.pathsep + ENV['PATH']})
record = json.loads((TENANT / 'release/INSTALL_CHECK.json').read_bytes())
row['missing_anchors'] = record['links_with_missing_anchor']
row['fault_scope'] = 'One read-only Git response gains an unresolved relative anchor; checker source unchanged.'

# The first probe used valid frozen program bytes and a successful real validate.
# An injected nonzero enumeration represents interruption/resource failure of this
# separate process, not a malformed program that validation already rejects.
shimdir = ROOT / 'shim'
shim = shimdir / 'python3'
shim.write_text('#!/bin/bash\nif [ "$1" = "-I" ] && [ "$2" = "-c" ]; then\n'
                ' echo "reviewer-injected frame-index acquisition failure" >&2\n exit 37\nfi\n'
                'exec ' + shlex.quote(sys.executable) + ' "$@"\n')
shim.chmod(0o755)
fault_env = {'PATH': str(shimdir) + os.pathsep + ENV['PATH']}
checker = ROOT / 'freeze-positive/axiom_indexer_v2.5.1-rc.2/build_tenants/core/code/ac.py'
out = ROOT / 'run-enumeration-stale'
(out / 'projections').mkdir(parents=True, exist_ok=True)
stale = out / 'projections/stale.json'
stale.write_text('{"reviewer_stale_sentinel":true}\n')
row = run('run-ac-enumeration-failure-with-stale-output',
          ['bash', 'qualification/C3-ITER3/tools/run_ac.sh', str(checker), str(out)], False, fault_env)
row['stale_projection_retained'] = stale.exists()
row['projection_names'] = [p.name for p in (out / 'projections').glob('*.json')]
row['commands_log'] = (out / 'commands.log').read_text()
sp = ROOT / 'freeze-enumeration-failure'
(sp / 'out/projections').mkdir(parents=True, exist_ok=True)
stale = sp / 'out/projections/stale.json'
stale.write_text('{"reviewer_stale_sentinel":true}\n')
consumer_record = TENANT / 'a_c/i3/consumers.json'
before = consumer_record.read_bytes()
row = run('freeze-enumeration-failure-contained',
          ['bash', 'qualification/C3-ITER4/tools/freeze_ac.sh', str(sp)], False, fault_env)
row['stale_projection_removed'] = not stale.exists()
row['projection_count'] = len(list((sp / 'out/projections').glob('*.json')))
row['consumers_not_reached'] = consumer_record.read_bytes() == before
row['program_sha256'] = hashlib.sha256((TENANT / 'a_c/i3/axiomatic-program.json').read_bytes()).hexdigest()
print(json.dumps({'source_A': prior['source_A'], 'package_B': prior['package_B'],
                  'scratch': str(ROOT), 'interpreter': sys.executable,
                  'jsonschema_path': jsonschema.__file__, 'cases': ROWS,
                  'limits': ['No claim that a real process interruption occurred; it is the supplied fault.',
                             'Initial install cases were unavailable because their interpreter lacked jsonschema.',
                             'Missing-anchor injection tests gate propagation, not package-byte authenticity.']}, indent=2))
