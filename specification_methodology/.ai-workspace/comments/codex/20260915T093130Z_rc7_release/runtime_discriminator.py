"""Observe the existing symlink-loop fixture under one selected Python runtime."""
from pathlib import Path
import copy
import argparse
import hashlib
import json
import platform
import sys
import tempfile

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
CODE = ROOT / 'axiom_indexer/build_tenants/core/code'
sys.path.insert(0, str(CODE))
from test_ac import FrameProjectionTests, canonical_bytes

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repaired', action='store_true')
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix='runtime-discriminator.', dir=OUT) as temp:
        tempfile.tempdir = temp
        case = FrameProjectionTests('test_unresolved_physical_target_withholds_output_cleanup')
        case.setUp()
        try:
            first, second = case.root / 'loop-a.md', case.root / 'loop-b.md'
            first.symlink_to(second)
            second.symlink_to(first)
            changed = copy.deepcopy(case.value)
            changed['frame_indexes'][0]['source_refs'] = ['repo://fixture/loop-a.md#unknown']
            case.program_path.write_bytes(canonical_bytes(changed))
            output = case.root / 'projection.json'
            original = b'Old result retained and explicitly diagnosed as unsafe.'
            output.write_bytes(original)
            source_before = {p.name: sha(p) for p in case.root.iterdir() if p.is_file() and not p.is_symlink() and p != output}
            result = case.cli(output=output)
            source_after = {p.name: sha(p) for p in case.root.iterdir() if p.is_file() and not p.is_symlink() and p != output}
            record = {'python': sys.version, 'executable': sys.executable, 'platform': platform.platform(),
                'test_route': str(CODE / 'test_ac.py') + '#test_unresolved_physical_target_withholds_output_cleanup',
                'test_sha256': sha(CODE / 'test_ac.py'), 'ac_sha256': sha(CODE / 'ac.py'),
                'argv': list(map(str, result.args)), 'returncode': result.returncode,
                'stdout': result.stdout.decode(), 'stderr': result.stderr.decode(),
                'output_preimage_sha256': hashlib.sha256(original).hexdigest(),
                'output_exists_after': output.exists(),
                'output_preimage_retained': output.exists() and output.read_bytes() == original,
                'ordinary_source_and_inputs_preserved': source_before == source_after,
                'loop_links_preserved': first.is_symlink() and second.is_symlink() and first.readlink() == second and second.readlink() == first,
                'loop_resolution': 'not_observed'}
            try:
                record['loop_resolution'] = {'returned': str(first.resolve())}
            except (OSError, RuntimeError) as exc:
                record['loop_resolution'] = {'raised': type(exc).__name__, 'detail': str(exc)}
            name = 'runtime-discriminator-python-' + '.'.join(map(str, sys.version_info[:3])) + ('-repaired' if args.repaired else '') + '.json'
            assert not (OUT / name).exists(), 'Preserve an existing discriminator'
            (OUT / name).write_text(json.dumps(record, indent=2) + '\n')
            print(json.dumps({'record': name, 'python': platform.python_version(), 'returncode': result.returncode,
                'output_preimage_retained': record['output_preimage_retained'],
                'ordinary_source_and_inputs_preserved': record['ordinary_source_and_inputs_preserved']}))
        finally:
            case.tearDown()

if __name__ == '__main__':
    main()
