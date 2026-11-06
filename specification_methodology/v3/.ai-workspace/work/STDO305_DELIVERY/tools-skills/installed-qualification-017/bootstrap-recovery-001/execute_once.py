"""Prospective operator recovery: restore one exact removed preimage, retry once."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import time
import zipfile

HERE = Path(__file__).absolute().parent
sys.path.insert(0, str(HERE.parent))
import run_observed as observed


def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def checked(row):
    path = Path(row['path'])
    assert path.is_file() and not any(p.is_symlink() for p in (path, *path.parents)), str(path)
    assert digest(path) == row['sha256'] and path.stat().st_size == row['bytes'], str(path)
    return path


def write_new(name, value):
    with (HERE / name).open('x') as stream:
        json.dump(value, stream, sort_keys=True, indent=2)
        stream.write('\n')


def main():
    assert len(sys.argv) == 2, 'Expected the independently selected PLAN SHA256'
    plan_path = HERE / 'PLAN.json'
    assert digest(plan_path) == sys.argv[1]
    plan = json.loads(plan_path.read_bytes())
    assert digest(__file__) == plan['driver']['sha256']
    observations = json.loads(checked(plan['observations']).read_bytes())
    for row in plan['unchanged_inputs']:
        checked(row)
    for row in observations['failed_uuid_evidence']:
        checked(row)
    for row in observations['compiled_core_presence_and_hashes']:
        checked(row)
    prepared_path = checked(observations['prepared'])
    prepared = json.loads(prepared_path.read_bytes())
    runtime = Path(prepared['runtime_root'])
    source = Path(prepared['source_root'])
    profile_name = prepared['allowed_source_delta']
    assert profile_name == 'build_tenants/lean/profiles/proof-support-v1.json'
    target = Path(plan['restore']['target'])
    assert target == runtime / profile_name and not target.exists() and not target.is_symlink()
    assert not any(p.is_symlink() for p in target.parents)
    for name, row in prepared['source_members'].items():
        assert digest(source / name) == row['sha256']
        if name != profile_name:
            assert digest(runtime / name) == row['sha256']
    retained = checked(observations['retained_preimage'])
    original_source = checked(observations['materialized_source_preimage'])
    raw = original_source.read_bytes()
    assert raw == retained.read_bytes()
    archive = observations['native_archive_entry']
    with zipfile.ZipFile(archive['archive']) as stream:
        assert stream.read(archive['entry']) == raw
    assert hashlib.sha256(raw).hexdigest() == prepared['source_members'][profile_name]['sha256']
    for name in plan['must_be_absent']:
        path = Path(name)
        assert not path.exists() and not path.is_symlink(), name
    active = []
    for line in subprocess.check_output(['ps', '-axo', 'pid=,ppid=,pgid=,comm='], text=True).splitlines():
        fields = line.strip().split(None, 3)
        if len(fields) == 4 and Path(fields[3]).name in ('lean', 'leanchecker', 'lake'):
            active.append(fields)
    assert not active, active
    write_new('PRE_INVOCATION.json', {'plan_sha256': sys.argv[1], 'observed_ns': time.time_ns(),
        'retry_of': plan['retry_of'], 'target_absent': True, 'original_preimage_sha256': digest(retained),
        'compiler_process_snapshot': active, 'argv': plan['public_argv'],
        'standing': 'All observed input conditions checked before the one selected restoration and public invocation.'})
    with target.open('xb') as stream:
        stream.write(raw)
    target.chmod(int(prepared['source_members'][profile_name]['git_mode'], 8) & 0o777)
    assert digest(target) == digest(retained) and not os.path.samefile(target, retained)
    write_new('RESTORATION.json', {'observed_ns': time.time_ns(), 'source': str(original_source),
        'independently_matching_retained_preimage': str(retained),
        'target': str(target), 'bytes': len(raw), 'sha256': digest(target), 'samefile': False,
        'standing': 'Original prepared-source preimage restored only. This is not a successful local support result; unchanged bootstrap must remove it and perform fresh replay.'})
    receipt, result = observed.run(plan['receipt_name'], plan['public_argv'],
        'specification_methodology/v3/build_tenants/common-tools/tooling_setup.py',
        inputs=[prepared_path], output_tree=Path(plan['public_output']), output_files=[target])
    write_new('OUTCOME.json', {'retry_of': plan['retry_of'], 'receipt': observed.ref(
        HERE.parent / 'executions' / plan['receipt_name'] / 'execution.json'),
        'returncode': receipt['execution']['returncode'], 'result': result,
        'standing': 'Actual second public bootstrap outcome only. No dependent origin, checker, host, or formal operation is launched by this driver.'})
    if receipt['execution']['returncode'] != 0 or not isinstance(result, dict) or result.get('status') != 'support-established':
        raise SystemExit(2)


if __name__ == '__main__':
    main()
