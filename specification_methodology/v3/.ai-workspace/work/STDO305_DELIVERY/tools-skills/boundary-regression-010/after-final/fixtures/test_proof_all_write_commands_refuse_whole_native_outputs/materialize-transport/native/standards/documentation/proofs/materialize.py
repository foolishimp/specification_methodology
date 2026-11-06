#!/usr/bin/env python3
"""Exact deterministic transport and safe materialization of retained Lean evidence."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import stat
import sys
import unicodedata
import zipfile

MAX_EXPANDED = 2 * 1024 * 1024 * 1024
MAX_MEMBERS = 256
PART_BYTES = 64 * 1024 * 1024
MAX_COMPRESSED = 512 * 1024 * 1024


def boundary():
    path = Path(__file__).absolute().with_name('payload_boundary.py')
    spec = importlib.util.spec_from_file_location('stdo_payload_boundary', path)
    module = importlib.util.module_from_spec(spec)
    # Source execution intentionally bypasses SourceFileLoader's .pyc writer.
    # Ordinary documented Python invocation must keep the installation intact.
    exec(compile(path.read_bytes(), str(path), 'exec'), module.__dict__)
    return module


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def ordinary(path):
    path = Path(path).absolute()
    require('..' not in path.parts and not any(p.is_symlink() for p in (path, *path.parents)), 'redirected/traversing evidence path')
    return path


def regular(path):
    path = ordinary(path)
    require(stat.S_ISREG(path.stat().st_mode), 'nonregular evidence member')
    return path.read_bytes()


def safe(name):
    require(isinstance(name, str) and name not in ('', '.', '..') and '/' not in name and '\\' not in name and ':' not in name and
            not name.endswith((' ', '.')) and not any(ord(c) < 32 for c in name), 'unsafe evidence member name')
    return name


def separate(output, protected):
    output, protected = ordinary(output), ordinary(protected)
    require(not output.is_relative_to(protected) and not protected.is_relative_to(output), 'evidence output overlaps protected input')
    for one, other in ((output, protected), (protected, output)):
        require(not any(p.exists() and other.exists() and os.path.samefile(p, other) for p in (one, *one.parents)), 'evidence output aliases protected input')


def inspect(raw, expected_sha=None, *, visible=False):
    require(0 < len(raw) <= MAX_COMPRESSED, 'compressed evidence exceeds bound')
    if expected_sha is not None:
        require(sha(raw) == expected_sha, 'evidence archive digest differs')
    rows, data, folded = {}, {}, set()
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        infos = archive.infolist()
        require(0 < len(infos) <= MAX_MEMBERS and sum(i.file_size for i in infos) <= MAX_EXPANDED, 'evidence archive exceeds bound')
        for info in infos:
            name = safe(info.filename); key = unicodedata.normalize('NFC', name).casefold(); mode = info.external_attr >> 16
            require(name not in rows and key not in folded, 'duplicate/aliased evidence member')
            require(info.create_system == 3 and stat.S_ISREG(mode) and stat.S_IMODE(mode) == 0o644 and
                    not info.flag_bits & 1 and info.compress_type == zipfile.ZIP_DEFLATED, 'unsupported evidence archive member')
            digest = hashlib.sha256(); length = 0; chunks = []
            retain = name in ('manifest.json', 'result.json') or (visible and name.endswith(('.json', '.lean', '.log')))
            with archive.open(info) as stream:
                while chunk := stream.read(1024 * 1024):
                    digest.update(chunk); length += len(chunk)
                    if retain: chunks.append(chunk)
            require(length == info.file_size, 'evidence member length differs')
            rows[name] = {'sha256': digest.hexdigest(), 'bytes': length}; folded.add(key)
            if retain: data[name] = b''.join(chunks)
    require({'manifest.json', 'result.json'} <= rows.keys(), 'evidence manifest/result missing')
    manifest, result = json.loads(data['manifest.json']), json.loads(data['result.json'])
    require(manifest.get('schema') == 'a_c.formal-gate.bundle/1' and result.get('schema') == 'a_c.formal-gate.result/1', 'unsupported formal evidence')
    require(set(rows) == set(manifest['members']) | {'manifest.json', 'result.json'}, 'evidence archive member closure differs')
    require(all(rows[safe(n)]['sha256'] == h for n, h in manifest['members'].items()), 'archived evidence member digest differs')
    require(result['evidence'] == {'manifest_sha256': rows['manifest.json']['sha256'], 'members': manifest['members']}, 'archived manifest/result binding differs')
    return {'kind': 'stdo.formal-evidence-transport/1', 'archive_sha256': sha(raw), 'archive_bytes': len(raw),
            'members': rows, 'expanded_bytes': sum(r['bytes'] for r in rows.values()),
            'result_sha256': rows['result.json']['sha256'], 'manifest_sha256': rows['manifest.json']['sha256']}, data


def pack(bundle, output):
    bundle, output = ordinary(bundle), ordinary(output)
    boundary().guard([output], [bundle], anchors=[Path(__file__).absolute()])
    separate(output, bundle); require(not output.exists(), 'preserve existing evidence archive')
    manifest_raw = regular(bundle / 'manifest.json'); result_raw = regular(bundle / 'result.json')
    manifest = json.loads(manifest_raw)
    names = set(manifest['members']) | {'manifest.json', 'result.json'}
    actual = {p.name for p in bundle.iterdir()}
    require(actual in (names, names | {'local-origin.json'}), 'unselected evidence member (origin private keys are never transported)')
    sizes = [ordinary(bundle / safe(n)).stat().st_size for n in names]
    require(len(names) <= MAX_MEMBERS and sum(sizes) <= MAX_EXPANDED, 'retained evidence exceeds transport bound')
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9, allowZip64=True) as archive:
        for name in sorted(names):
            raw = regular(bundle / name)
            if name in manifest['members']: require(sha(raw) == manifest['members'][name], 'retained evidence differs: ' + name)
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0)); info.create_system = 3; info.external_attr = 0o100644 << 16
            archive.writestr(info, raw, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    raw = buffer.getvalue(); meta, _ = inspect(raw)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('xb') as stream: stream.write(raw)
    return dict(meta, status='packed', path=str(output))


def split(archive_path, destination):
    archive_path, destination = ordinary(archive_path), ordinary(destination)
    boundary().guard([destination], [archive_path], anchors=[Path(__file__).absolute()])
    separate(destination, archive_path); require(not destination.exists(), 'preserve existing evidence transport')
    raw = regular(archive_path); meta, _ = inspect(raw)
    parts = [(f'part-{i // PART_BYTES + 1:03}.bin', raw[i:i + PART_BYTES]) for i in range(0, len(raw), PART_BYTES)]
    descriptor = {**meta, 'parts': [{'path': name, 'bytes': len(value), 'sha256': sha(value)} for name, value in parts]}
    encoded = (json.dumps(descriptor, sort_keys=True, indent=2) + '\n').encode()
    destination.mkdir(parents=True, exist_ok=False)
    for name, value in parts: (destination / name).write_bytes(value)
    (destination / 'TRANSPORT.json').write_bytes(encoded)
    return dict(meta, status='transported', path=str(destination), parts=descriptor['parts'], transport_sha256=sha(encoded))


def join(descriptor_raw, read, *, visible=False):
    descriptor = json.loads(descriptor_raw)
    require(descriptor.get('kind') == 'stdo.formal-evidence-transport/1', 'unsupported evidence transport descriptor')
    rows = descriptor['parts']; require(isinstance(rows, list) and 0 < len(rows) <= MAX_COMPRESSED // PART_BYTES, 'invalid evidence part count')
    require([r['path'] for r in rows] == [f'part-{i + 1:03}.bin' for i in range(len(rows))], 'evidence part order/population differs')
    require(all(type(r['bytes']) is int and 0 < r['bytes'] <= PART_BYTES for r in rows) and
            all(r['bytes'] == PART_BYTES for r in rows[:-1]), 'evidence part bounds differ')
    parts = []
    for row in rows:
        value = read(safe(row['path']))
        require(len(value) == row['bytes'] and sha(value) == row['sha256'], 'evidence part digest/length differs')
        parts.append(value)
    raw = b''.join(parts)
    meta, data = inspect(raw, descriptor['archive_sha256'], visible=visible)
    require(descriptor == {**meta, 'parts': rows}, 'evidence transport descriptor/expanded inventory differs')
    return raw, descriptor, data


def read_transport(path, expected_sha=None, *, visible=False):
    path = ordinary(path); raw = regular(path)
    if expected_sha is not None: require(sha(raw) == expected_sha, 'evidence transport descriptor digest differs')
    descriptor = json.loads(raw)
    require({p.name for p in path.parent.iterdir()} == {'TRANSPORT.json'} | {safe(r['path']) for r in descriptor['parts']}, 'evidence transport directory population differs')
    return join(raw, lambda name: regular(path.parent / name), visible=visible)


def verify_tree(raw, destination, expected_sha=None, *, allow_local_origin=False):
    meta, _ = inspect(raw, expected_sha)
    destination = ordinary(destination); require(destination.is_dir(), 'extracted evidence directory missing')
    actual = {p.name for p in destination.iterdir()}
    require(actual == set(meta['members']) or (allow_local_origin and actual == set(meta['members']) | {'local-origin.json'}), 'extracted evidence population differs')
    for name, row in meta['members'].items():
        path = ordinary(destination / name)
        require(stat.S_ISREG(path.stat().st_mode), 'extracted evidence is not regular')
        with path.open('rb') as stream: digest = hashlib.file_digest(stream, 'sha256').hexdigest()
        require(digest == row['sha256'] and path.stat().st_size == row['bytes'], 'extracted evidence bytes differ: ' + name)
    return dict(meta, status='checked', destination=str(destination))


def materialize(archive_path, destination, expected_sha, *, protected_root=None):
    archive_path, destination = ordinary(archive_path), ordinary(destination)
    protected = ordinary(protected_root) if protected_root else archive_path.parent
    raw = regular(archive_path)
    return materialize_data(raw, destination, expected_sha, protected)


def materialize_data(raw, destination, expected_sha, protected):
    destination = ordinary(destination)
    boundary().guard([destination], [protected], anchors=[Path(__file__).absolute()])
    separate(destination, protected)
    require(not destination.exists() and destination.parent.is_dir(), 'absent evidence destination/existing parent required')
    meta, _ = inspect(raw, expected_sha)
    destination.mkdir(mode=0o700, exist_ok=False)
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        for name in sorted(meta['members']):
            with archive.open(name) as source, (destination / name).open('xb') as target:
                while chunk := source.read(1024 * 1024): target.write(chunk)
            (destination / name).chmod(0o644)
    result = verify_tree(raw, destination, expected_sha)
    return dict(result, status='materialized', notice='Exact retained proof bytes; no new Lean execution or authentication claim.')


def materialize_transport(path, destination, expected_sha=None, *, protected_root=None):
    path = ordinary(path); descriptor_raw = regular(path)
    raw, descriptor, _ = read_transport(path, expected_sha)
    result = materialize_data(raw, destination, descriptor['archive_sha256'], protected_root or path.parent)
    return dict(result, parts=descriptor['parts'], transport_sha256=sha(descriptor_raw))


def current_request(raw, evidence, output, protected):
    """Derive executable local paths; never replace the original request/verdict."""
    evidence, output = ordinary(evidence), ordinary(output)
    boundary().guard([output], [evidence, protected], anchors=[Path(__file__).absolute()])
    separate(output, evidence); separate(output, protected)
    require(not output.exists() and output.parent.is_dir(), 'absent request output/existing parent required')
    verify_tree(raw, evidence)
    result = json.loads(regular(evidence / 'result.json'))
    original = regular(evidence / 'request.json'); request = json.loads(original)
    require(result.get('status') == 'verified' and request.get('schema') == 'a_c.formal-gate.request/1' and
            request.get('input', {}).get('format') == 'model', 'verified current model request required')
    require(request['selections'] == result['selections'] and request['context_binding'] == result['context_binding'], 'retained request selections/context differs')
    for key, input_key in (('input', 'input'), ('supplied_views', 'supplied_views')):
        selected = result['inputs'][input_key]
        path = evidence / safe(selected['retained_path'])
        digest = sha(regular(path))
        require(digest == selected['raw_sha256'] == request[key]['raw_sha256'], 'retained request input differs')
        request[key]['path'] = str(path)
    require(request['input']['raw_sha256'] == result['inputs']['model']['raw_sha256'], 'current model input differs')
    encoded = (json.dumps(request, sort_keys=True, indent=2) + '\n').encode()
    with output.open('xb') as stream: stream.write(encoded)
    return {'kind': 'stdo.current-proof-request/1', 'status': 'prepared', 'path': str(output), 'sha256': sha(encoded),
            'original_request_sha256': sha(original), 'model': result['model'],
            'input_sha256': request['input']['raw_sha256'], 'supplied_views_sha256': request['supplied_views']['raw_sha256'],
            'notice': 'Local request paths only; execute the selected installed Lean runtime for a new verdict.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path)
    parser.add_argument('--archive-sha256')
    parser.add_argument('--transport', type=Path, default=Path(__file__).absolute().parent / 'transport/TRANSPORT.json')
    parser.add_argument('--transport-sha256')
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('pack'); p.add_argument('--bundle', type=Path, required=True); p.add_argument('--output', type=Path, required=True)
    p = sub.add_parser('split'); p.add_argument('--input', type=Path, required=True); p.add_argument('--destination', type=Path, required=True)
    sub.add_parser('check')
    for name in ('materialize', 'verify-tree'):
        sub.add_parser(name).add_argument('--destination', type=Path, required=True)
    p = sub.add_parser('request'); p.add_argument('--evidence', type=Path, required=True); p.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        # Include the invoked installed entrypoint even when an explicit raw
        # archive or transport lives elsewhere. Check before reading/computing.
        if args.command in ('pack', 'split', 'materialize', 'request'):
            output = args.output if args.command in ('pack', 'request') else args.destination
            source = args.bundle if args.command == 'pack' else args.input if args.command == 'split' else args.archive or args.transport
            inputs = [source] + ([args.evidence] if args.command == 'request' else [])
            boundary().guard([output], inputs, anchors=[Path(__file__).absolute()])
        if args.command == 'pack': result = pack(args.bundle, args.output)
        elif args.command == 'split': result = split(args.input, args.destination)
        elif args.archive is None:
            expected = args.transport_sha256
            if expected is None:
                catalog = json.loads(regular(args.transport.parent.parent / 'PROOFS.json'))
                expected = catalog['transport_sha256']
            raw, meta, _ = read_transport(args.transport, expected)
            protected = args.transport.parent
            if args.command == 'check': result = dict(meta, status='checked', transport_sha256=sha(regular(args.transport)))
            elif args.command == 'verify-tree': result = dict(verify_tree(raw, args.destination), parts=meta['parts'], transport_sha256=sha(regular(args.transport)))
            elif args.command == 'request': result = current_request(raw, args.evidence, args.output, protected)
            else:
                result = materialize_transport(args.transport, args.destination, expected, protected_root=protected)
        else:
            expected = args.archive_sha256
            require(expected is not None, 'explicit archive digest required for raw archive mode')
            if args.command == 'check': result = dict(inspect(regular(args.archive), expected)[0], status='checked')
            elif args.command == 'verify-tree': result = verify_tree(regular(args.archive), args.destination, expected)
            elif args.command == 'request':
                inspect(regular(args.archive), expected)
                result = current_request(regular(args.archive), args.evidence, args.output, args.archive.parent)
            else:
                protected = args.archive.parent
                result = materialize(args.archive, args.destination, expected, protected_root=protected)
        print(json.dumps(result, sort_keys=True)); return 0
    except (OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile, RuntimeError) as error:
        print(json.dumps({'status': 'refused', 'reason': str(error)})); return 2


if __name__ == '__main__':
    raise SystemExit(main())
