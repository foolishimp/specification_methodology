"""Qualification operator for three declared third-party caches; not Product setup.

Each regular file uses clonefile(2) without a copy fallback. A successful copy
is only dependency acquisition: ordinary bootstrap and fresh support/proof are
still required. Cooperative checks do not defend against hostile path races.
"""
from pathlib import Path
import argparse
import ctypes
import hashlib
import json
import os
import platform
import stat
import sys
import time

REPO = Path('/Users/jim/src/apps/specification_methodology')
HERE = Path(__file__).resolve().parent
EVIDENCE = HERE
CACHES = ('.toolchain', '.lake/packages', '.cache/mathlib')
LOCKS = ('toolchain-lock.json', 'lake-manifest.json', 'lean-toolchain')

def require(condition, message):
    if not condition: raise ValueError(message)

def sha(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()

def ref(path):
    path = Path(path).absolute()
    return {'path': str(path), 'sha256': sha(path), 'bytes': path.stat().st_size}

def ordinary(path, exists=True):
    path = Path(path).absolute()
    require(not any(p.is_symlink() for p in (path, *path.parents)), 'redirected path: ' + str(path))
    if exists: require(path.exists(), 'missing selected path: ' + str(path))
    return path

def pinned(row):
    path = ordinary(REPO / row['path'])
    actual = ref(path)
    require(actual['sha256'] == row['sha256'] and actual['bytes'] == row['bytes'], 'selected bytes changed: ' + str(path))
    return path

def save(path, value):
    with Path(path).open('x') as stream:
        stream.write(json.dumps(value, sort_keys=True, indent=2) + '\n')

def identity(path):
    s = Path(path).lstat()
    return {'device': s.st_dev, 'inode': s.st_ino, 'bytes': s.st_size,
            'mode': stat.S_IMODE(s.st_mode), 'links': s.st_nlink,
            'mtime_ns': s.st_mtime_ns, 'ctime_ns': s.st_ctime_ns,
            'allocated_bytes': s.st_blocks * 512}

def free_space(path):
    s = os.statvfs(path)
    return {'available_bytes': s.f_bavail * s.f_frsize, 'free_bytes': s.f_bfree * s.f_frsize,
            'block_bytes': s.f_frsize, 'device': Path(path).stat().st_dev}

def clone(source, destination):
    require(sys.platform == 'darwin', 'clonefile(2) operator requires Darwin')
    require(stat.S_ISREG(source.lstat().st_mode), 'clone source is not a regular file')
    require(not destination.exists() and not destination.is_symlink(), 'clone destination already exists')
    require(source.stat().st_dev == destination.parent.stat().st_dev, 'different source/destination filesystems')
    library = ctypes.CDLL('/usr/lib/libSystem.B.dylib', use_errno=True)
    call = library.clonefile
    call.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    call.restype = ctypes.c_int
    ctypes.set_errno(0)
    code = call(os.fsencode(source), os.fsencode(destination), 0)
    if code != 0:
        error = ctypes.get_errno()
        raise OSError(error, os.strerror(error), str(source) + ' -> ' + str(destination))
    before, after = identity(source), identity(destination)
    require((before['device'], before['inode']) != (after['device'], after['inode']), 'clone is not an independent filesystem object')
    return {'api': 'clonefile(2)', 'flags': 0, 'returncode': code,
            'source_identity': before, 'destination_identity': after, 'copy_fallback': False}

def probe():
    output = HERE / 'clone-probe-001'
    ordinary(output, exists=False)
    require(not output.exists(), 'preserve existing capability observation')
    output.mkdir()
    source, destination = output/'source.bin', output/'clone.bin'
    payload = bytes(range(256)) * 4096
    with source.open('xb') as stream: stream.write(payload)
    source_before = ref(source); identity_before = identity(source)
    before = free_space(output); started = time.time_ns()
    call = clone(source, destination)
    after_clone = free_space(output); cloned_before_write = ref(destination)
    require(source_before['sha256'] == cloned_before_write['sha256'], 'probe cloned bytes differ')
    with destination.open('r+b') as stream:
        stream.write(b'\xff'); stream.flush(); os.fsync(stream.fileno())
    require(ref(source) == source_before and identity(source) == identity_before, 'probe changed source')
    require(sha(destination) != source_before['sha256'], 'probe did not exercise a private destination write')
    after_write = free_space(output)
    record = {'kind': 'stdo.rc-reset.clone-capability/1', 'status': 'observed',
        'operator': ref(__file__), 'argv': sys.argv, 'cwd': str(Path.cwd()),
        'python': {'invocation': sys.executable, 'physical': str(Path(sys.executable).resolve()),
                   'sha256': sha(Path(sys.executable).resolve()), 'version': sys.version},
        'platform': platform.platform(), 'started_ns': started, 'ended_ns': time.time_ns(),
        'source_before': source_before, 'source_after': ref(source),
        'cloned_before_private_write': cloned_before_write, 'clone_after': ref(destination),
        'clone_call': call, 'source_identity_unchanged': True, 'source_bytes_unchanged': True,
        'destination_private_write_observed': True, 'before': before, 'after_clone': after_clone,
        'after_private_write': after_write,
        'available_byte_deltas': {'clone': after_clone['available_bytes'] - before['available_bytes'],
                                  'private_write': after_write['available_bytes'] - after_clone['available_bytes']},
        'scope': 'One 1MiB scratch file on this volume; no runtime cache has been copied. clonefile succeeded without fallback and the destination write preserved source bytes/identity. Free-space deltas are snapshots and may include concurrent filesystem activity; st_blocks is not a unique shared-block accounting.'}
    save(output/'RESULT.json', record)
    print(json.dumps({'result': ref(output/'RESULT.json'), 'source_preserved': True, 'clonefile_returncode': 0}))

def prime(plan_path, plan_sha):
    plan_path = ordinary(plan_path)
    require(sha(plan_path) == plan_sha, 'cache plan changed')
    plan = json.loads(plan_path.read_bytes())
    require(plan['kind'] == 'stdo.rc-reset.cache-clone-plan/1' and plan['version'] == '3.0.5-rc.1', 'wrong cache plan')
    require(tuple(plan['cache_roots']) == CACHES, 'cache population changed')
    require(plan['max_seconds'] == 900 and plan['max_entries'] == 200000 and plan['max_logical_bytes'] == 17179869184, 'unselected resource limits')
    require(pinned(plan['operator']) == Path(__file__).absolute(), 'operator selection differs')
    handoff = json.loads(pinned(plan['native_handoff']).read_bytes())
    require(handoff['version'] == plan['version'], 'wrong native cut')
    workspace = ordinary(handoff['workspace']); native = ordinary(handoff['native_root'])
    require(sha(native/'manifest.json') == handoff['native_manifest']['sha256'], 'installed native manifest changed')
    prepared_path = pinned(plan['prepared_derivation']); prepared = json.loads(prepared_path.read_bytes())
    require(prepared['kind'] == 'stdo.ac-runtime-derivation/1' and prepared['status'] == 'prepared' and prepared['version'] == plan['version'], 'fresh prepared runtime required')
    runtime = ordinary(prepared['runtime_root']); custody = ordinary(prepared['source_root'])
    require(runtime == workspace/'runtime/a_c' and custody == workspace/'source-tools/a_c', 'unexpected runtime/custody path')
    source = ordinary(plan['source_lean_root']); target = ordinary(runtime/'build_tenants/lean')
    require(source == REPO/'a_c/build_tenants/lean', 'unexpected source cache root')
    require(prepared['allowed_source_delta'] == 'build_tenants/lean/profiles/proof-support-v1.json', 'runtime derivation scope differs')
    helper = pinned(plan['boundary_helper']); namespace = {}
    exec(compile(helper.read_bytes(), str(helper), 'exec'), namespace)
    overlap = namespace['overlaps_existing']
    record = ordinary(plan['record_directory'], exists=False)
    require(record.is_relative_to(EVIDENCE) and not record.exists(), 'fresh owned receipt directory required')
    destinations = [target/name for name in CACHES]
    for path in [record, *destinations]:
        ordinary(path, exists=False)
        require(not path.exists(), 'preserve preexisting output: ' + str(path))
        for protected in (source, custody, native, plan_path, prepared_path):
            require(not overlap(path, protected), 'output overlaps selected input: ' + str(path))
    require(not overlap(record, runtime), 'receipt overlaps derived runtime')
    for name in LOCKS:
        selected = pinned(plan['source_locks'][name])
        require(selected == source/name and selected.read_bytes() == (target/name).read_bytes(), 'source/target dependency locks differ')
        row = prepared['source_members']['build_tenants/lean/'+name]
        require(sha(selected) == row['sha256'], 'lock differs from selected source custody')
    # Retained proof/profile identifies the selected cache source, not a verdict
    # for the new runtime. Own support/profile/origin/build are never copied.
    source_proof = json.loads(pinned(plan['source_proof']).read_bytes())
    profile = pinned(plan['source_support_profile'])
    require(profile == source/'profiles/proof-support-v1.json', 'unexpected source support profile')
    require(source_proof['status'] == 'verified' and source_proof['observations']['support']['manifest_sha256'] == sha(profile), 'source cache custody differs')
    started = time.monotonic(); entries = []; total = 0
    for root_name in CACHES:
        root = ordinary(source/root_name); require(root.is_dir(), 'missing source cache')
        pending = [root]
        while pending:
            path = pending.pop(); observed = path.lstat(); relative = path.relative_to(source).as_posix()
            require(time.monotonic()-started < 900, 'cache preflight exceeded selected bound')
            if stat.S_ISDIR(observed.st_mode):
                entries.append((path, relative, 'directory', identity(path)))
                pending.extend(sorted(path.iterdir(), reverse=True))
            elif stat.S_ISREG(observed.st_mode):
                entries.append((path, relative, 'file', identity(path))); total += observed.st_size
            elif stat.S_ISLNK(observed.st_mode):
                link = os.readlink(path)
                require(not Path(link).is_absolute(), 'absolute cache symlink is not admitted')
                resolved = path.resolve(strict=True)
                require(any(resolved.is_relative_to(source/name) for name in CACHES), 'cache symlink escapes selected cache population')
                entries.append((path, relative, 'symlink', identity(path)))
            else: raise ValueError('nonordinary cache entry: '+str(path))
            require(len(entries) <= 200000 and total <= 17179869184, 'cache population exceeds selected finite envelope')
    record.mkdir(parents=True)
    save(record/'INVOCATION.json', {'plan': ref(plan_path), 'operator': ref(__file__), 'argv': sys.argv,
        'cwd': str(Path.cwd()), 'source': str(source), 'target': str(target), 'entries': len(entries),
        'logical_bytes': total, 'excluded': ['own .lake/build', 'support profiles', 'formal origins', 'proof bundles'],
        'claim': 'Dependency cache acquisition only; ordinary bootstrap and fresh support/proof remain required.'})
    before = free_space(target); completed = 0
    try:
        with (record/'members.jsonl').open('x') as ledger:
            for path, relative, kind, original in entries:
                require(time.monotonic()-started < 900, 'cache clone exceeded selected bound')
                destination = target/relative
                require(identity(path) == original, 'source cache entry changed')
                destination.parent.mkdir(parents=True, exist_ok=True)
                row = {'path': relative, 'kind': kind, 'source_identity': original}
                if kind == 'directory': destination.mkdir(mode=original['mode'])
                elif kind == 'symlink':
                    row['link'] = os.readlink(path); destination.symlink_to(row['link'])
                else:
                    row['sha256'] = sha(path); row['clone'] = clone(path, destination)
                    require(sha(destination) == row['sha256'], 'cloned bytes differ')
                require(identity(path) == original, 'source changed while cloning')
                row['destination_identity'] = identity(destination)
                require((original['device'], original['inode']) != (row['destination_identity']['device'], row['destination_identity']['inode']), 'source and destination alias')
                ledger.write(json.dumps(row, sort_keys=True)+'\n'); ledger.flush(); completed += 1
        after = free_space(target)
        save(record/'RESULT.json', {'kind': 'stdo.rc-reset.cache-clone/1', 'status': 'cache-cloned',
            'plan': ref(plan_path), 'ledger': ref(record/'members.jsonl'), 'entries': completed,
            'logical_bytes': total, 'elapsed_seconds': time.monotonic()-started,
            'before': before, 'after': after, 'available_byte_delta': after['available_bytes']-before['available_bytes'],
            'copy_fallback': False, 'support_established': False,
            'limits': 'No own build/profile/origin/proof copied. Free space is a shared-volume snapshot, not exclusive attribution. Clone metadata and full per-file hashes bind this acquisition; fresh bootstrap/support/proof decide the new runtime.'})
    except Exception as error:
        save(record/'INCOMPLETE.json', {'status': 'incomplete', 'completed_entries': completed,
             'error_type': type(error).__name__, 'error': str(error), 'recovery': 'Preserve partial cache and records. No fallback, cleanup or automatic retry.'})
        raise
    print(json.dumps({'result': ref(record/'RESULT.json'), 'entries': completed, 'support_established': False}))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='operation', required=True)
    sub.add_parser('probe')
    selected = sub.add_parser('prime'); selected.add_argument('--plan', required=True, type=Path); selected.add_argument('--sha256', required=True)
    args = parser.parse_args()
    if args.operation == 'probe': probe()
    else: prime(args.plan, args.sha256)

if __name__ == '__main__': main()
