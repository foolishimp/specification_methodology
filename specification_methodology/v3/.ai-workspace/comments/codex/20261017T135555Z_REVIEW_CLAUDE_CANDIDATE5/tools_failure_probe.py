"""Bounded RC5 failure-family probes. All candidate executions use unique scratch.

Run: python3 -B tools_failure_probe.py /path/to/specification_methodology
No Git mutations, native installs, external calls, or broad test suites.
The enumeration probe injects a subprocess failure, not a source defect.
"""
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time

REPO = Path(sys.argv[1]).resolve()
A = '4a63c9293ddaa568803b81f1ed5dcc1d3dc19cec'
B = 'a85f9ec98e43b942048a6c151aafd9662d2def90'
COMMON = '4c340f7adec9f3c893e3e267b23e4cadeb357854'
PREFIX = 'specification_methodology/v3/build_tenants/claude'
ROOT = Path(tempfile.mkdtemp(prefix='stdo-rc5-failure-family-', dir='/private/tmp'))
TENANT = ROOT / 'snapshot' / PREFIX
START = time.time()
ROWS = []
ENV = dict(os.environ, GIT_DIR=str(REPO / '.git'), PYTHONDONTWRITEBYTECODE='1')


def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])


with tarfile.open(fileobj=io.BytesIO(git('archive', B, PREFIX))) as archive:
    archive.extractall(ROOT / 'snapshot', filter='data')
for name in ('A_C_DEPENDENCY.md', 'PREDECESSOR_CLAIMS.md'):
    path = 'specification_methodology/v3/specification/requirements/' + name
    data = git('show', COMMON + ':' + path)
    assert data == git('show', A + ':' + path)
    dst = ROOT / 'snapshot' / path
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(data)


def run(name, command, expected_zero, cwd=TENANT, extra=None):
    env = dict(ENV, **(extra or {}))
    start = time.time()
    r = subprocess.run(command, cwd=cwd, env=env, capture_output=True, text=True, timeout=90)
    row = {'name': name, 'command': [str(x) for x in command], 'cwd': str(cwd),
           'expected_zero': expected_zero, 'exit': r.returncode,
           'expectation_holds': (r.returncode == 0) == expected_zero,
           'elapsed_seconds': round(time.time() - start, 3),
           'stdout_tail': r.stdout[-2000:], 'stderr_tail': r.stderr[-1000:]}
    ROWS.append(row)
    (ROOT / (name + '.stdout')).write_text(r.stdout)
    (ROOT / (name + '.stderr')).write_text(r.stderr)
    return row


def py(rel, *args):
    return [sys.executable, '-I', str(TENANT / rel), *map(str, args)]


# Tiny independent fixtures isolate the newly added gate predicates.
fixture = ROOT / 'fixtures'
(fixture / 'standards').mkdir(parents=True)
(fixture / 'frontier').mkdir()
doc = fixture / 'standards/OWNER.md'
doc.write_text('# Owner\n\n[known](#owner)\n')
run('links-positive', py('qualification/C3-ITER3/tools/links.py', 'standards'), True, fixture)
doc.write_text('# Owner\n\n[missing](absent.md)\n[anchor](OWNER.md#absent)\n')
run('links-missing-file-and-anchor', py('qualification/C3-ITER3/tools/links.py', 'standards'), False, fixture)
doc.write_text('# Owner\n\n[notation](X_v)\n')
run('links-exception-not-global', py('qualification/C3-ITER3/tools/links.py', 'standards'), False, fixture)
doc.write_text('# Owner\n')
frontier = fixture / 'frontier/PREDECESSOR_CLAIMS.md'
frontier.write_text('## Member\n| claim | `#source` | `OWNER.md#owner` |\n')
run('locus-positive', py('qualification/C3-ITER3/tools/locus_check.py'), True, fixture)
frontier.write_text('## Member\n| claim | `#source` | `OWNER.md#absent` |\n')
run('locus-unresolved', py('qualification/C3-ITER3/tools/locus_check.py'), False, fixture)
common = fixture / 'common.md'
good = '## Member\n| claim | `#source` | value |\n'
common.write_text(good)
frontier.write_text(good + '| extra | `#tenant-extra` | value |\n')
fc = py('qualification/C3-ITER3/tools/frontier_check.py', common, frontier)
run('frontier-positive-with-tenant-extra', fc, True, fixture)
frontier.write_text('## Member\n')
run('frontier-missing', fc, False, fixture)
frontier.write_text(good + '| claim | `#source` | value |\n')
run('frontier-duplicate', fc, False, fixture)

# Full frozen records, with one isolated adverse mutation and restoration.
frontier = TENANT / 'frontier/PREDECESSOR_CLAIMS.md'
saved = frontier.read_bytes()
run('frontier-review-positive', py('qualification/C3-ITER4/tools/frontier_review.py'), True)
txt = saved.decode()
import re
match = re.search(r'^\| .*?`#([^`]+)`', txt, re.M)
assert match
txt = txt[:match.start(1)] + 'reviewer-unknown-predecessor' + txt[match.end(1):]
frontier.write_text(txt)
run('frontier-review-unknown-predecessor', py('qualification/C3-ITER4/tools/frontier_review.py'), False)
frontier.write_bytes(saved)
consumer_record = TENANT / 'a_c/i3/consumers.json'
consumer_original = consumer_record.read_bytes()
run('consumers-positive', py('qualification/C3-ITER4/tools/consumers.py'), True)
lcm = TENANT / 'a_c/i3/logical-constraint-map.json'
saved = lcm.read_bytes()
value = json.loads(saved)
clause = next(c for c in value['clauses'] if any(str(x).startswith('stdo-3://build_tenants/claude/standards/') for x in c.get('source_refs', [])))
clause['source_refs'][0] = 'stdo-3://build_tenants/claude/standards/FOUNDATIONS.md#reviewer-missing-owner'
lcm.write_text(json.dumps(value))
run('consumers-unresolved-owner', py('qualification/C3-ITER4/tools/consumers.py'), False)
lcm.write_bytes(saved)
consumer_record.write_bytes(consumer_original)

# Whole real freeze: baseline, failed required control, and unknown control.
freeze = ['bash', 'qualification/C3-ITER4/tools/freeze_ac.sh']
run('freeze-positive', freeze + [str(ROOT / 'freeze-positive')], True)
consumer_record = TENANT / 'a_c/i3/consumers.json'
consumer_record.write_bytes(b'REVIEWER: downstream consumers not yet run\n')
before = consumer_record.read_bytes()
row = run('freeze-forced-failed-control', freeze + [str(ROOT / 'freeze-adverse')], False,
          extra={'AC_CONTROLS_FORCE_FAIL': 'identity-positive'})
row['consumers_not_reached'] = consumer_record.read_bytes() == before
control_report = TENANT / 'qualification/C3-ITER5/returns/ac_controls.json'
row['holds_all'] = json.loads(control_report.read_bytes())['holds_all']
before = control_report.read_bytes()
row = run('controls-unknown-name', py('qualification/C3-ITER4/tools/ac_controls.py', ROOT / 'unknown-control'), False,
          extra={'AC_CONTROLS_FORCE_FAIL': 'reviewer-control-does-not-exist'})
row['report_not_rewritten'] = control_report.read_bytes() == before

# Validate and project failures must survive subsequent successful commands.
stub = ROOT / 'checker_stub.py'
stub.write_text('import os,sys\nsys.exit(23 if sys.argv[1] == os.environ["CHECKER_FAIL"] else 0)\n')
for command in ('validate', 'project'):
    run('run-ac-failed-' + command,
        ['bash', 'qualification/C3-ITER3/tools/run_ac.sh', str(stub), str(ROOT / ('run-' + command))], False,
        extra={'CHECKER_FAIL': command})

# A distinct required subprocess enumerates frame indexes outside run().
shimdir = ROOT / 'shim'
shimdir.mkdir()
shim = shimdir / 'python3'
shim.write_text('#!/bin/bash\nif [ "$1" = "-I" ] && [ "$2" = "-c" ]; then\n  echo "reviewer-injected frame-index acquisition failure" >&2\n  exit 37\nfi\nexec ' + __import__('shlex').quote(sys.executable) + ' "$@"\n')
shim.chmod(0o755)
checker = ROOT / 'freeze-positive/axiom_indexer_v2.5.1-rc.2/build_tenants/core/code/ac.py'
row = run('run-ac-frame-enumeration-failure',
          ['bash', 'qualification/C3-ITER3/tools/run_ac.sh', str(checker), str(ROOT / 'run-enumeration')], False,
          extra={'PATH': str(shimdir) + os.pathsep + ENV['PATH']})
row['projection_count'] = len(list((ROOT / 'run-enumeration/projections').glob('*.json')))
row['commands_log'] = (ROOT / 'run-enumeration/commands.log').read_text()

# Installed-layout closure: only the admitted source bytes are materialized.
run('install-positive', py('release/check_install.py', ROOT / 'install-positive'), True)
manifest = TENANT / 'release/manifest.json'
saved = manifest.read_bytes()
value = json.loads(saved)
value['standards']['members'] = [m for m in value['standards']['members'] if m['path'] != 'schemas/product-definition.schema.json']
manifest.write_text(json.dumps(value))
run('install-missing-bootstrap-schema', py('release/check_install.py', ROOT / 'install-adverse'), False)
manifest.write_bytes(saved)
run('frames-current', py('qualification/instruments/generate_frames.py', '--check'), True)

print(json.dumps({'source_A': A, 'package_B': B, 'common': COMMON, 'scratch': str(ROOT),
                  'elapsed_seconds': round(time.time() - START, 3), 'cases': ROWS,
                  'limits': ['Synthetic fault controls test propagation, not checker semantics.',
                             'Install closure is materialization, not a native installer.',
                             'Expected report-only install links remain ungated.',
                             'No acceptance, semantic fidelity or active-context fit is inferred.']}, indent=2))
