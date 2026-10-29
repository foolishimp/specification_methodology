"""Private local cold establishments. Public bundles contain lookup hints only.

No caller path, environment variable or bundle selects an origin. Import has no
store effect. Only explicit tenant setup creates it; only the completed internal
cold path calls _establish. Python API/host administrators remain trusted.
"""
from __future__ import annotations
import hashlib
import hmac
import json
import os
from pathlib import Path
import re
import secrets
import stat

ROOT = Path(__file__).resolve().parents[1]
STORE_RELATIVE = '.cache/formal-origin-v1'
ORIGIN_SELECTION_PIN = STORE_RELATIVE + '/selection.json'
SELECTION = 'a_c.formal-gate.local-origin-selection/1'
ENTRY = 'a_c.formal-gate.local-origin-entry/1'
HINT = 'a_c.formal-gate.local-origin-hint/1'
DOMAIN = b'a_c.formal-gate.local-origin-entry/1\x00'
METADATA = ('result.json', 'manifest.json', 'request.json', 'replay-request.json')


class OriginError(ValueError):
    def __init__(self, reason, status='refused'):
        super().__init__(reason)
        self.status = status


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':'), allow_nan=False).encode('utf-8')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def decode(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise OriginError('Duplicate evidence JSON key')
            result[key] = value
        return result
    def invalid(value):
        raise OriginError('Nonfinite evidence JSON number')
    try:
        value = json.loads(raw, object_pairs_hook=pairs, parse_constant=invalid)
        canonical(value)  # rejects overflowing JSON floats and invalid Unicode
        return value
    except (ValueError, UnicodeError, RecursionError) as exc:
        raise OriginError('Malformed finite evidence JSON') from exc


def _hex(value, width=64):
    return isinstance(value, str) and re.fullmatch('[0-9a-f]{' + str(width) + '}', value) is not None


def _unalias(path):
    path = Path(path).absolute()
    for part in reversed((path, *path.parents)):
        try:
            mode = part.lstat().st_mode
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(mode):
            raise OriginError('Symlink path is outside the protected acquisition contract')
    return path.resolve(strict=False)



def _contains(parent, child):
    """Containment by existing ancestor identity, including host case aliases.

    Only a missing suffix has no inode. Reserve case variants of that fixed
    suffix conservatively; do not fold or ban unrelated existing source roots.
    """
    anchor, suffix = parent, []
    while True:
        try:
            info = anchor.stat()
            break
        except FileNotFoundError:
            suffix.insert(0, anchor.name)
            anchor = anchor.parent
    identity = (info.st_dev, info.st_ino)
    for candidate in (child, *child.parents):
        try:
            info = candidate.stat()
        except FileNotFoundError:
            continue
        if (info.st_dev, info.st_ino) == identity:
            tail = child.relative_to(candidate).parts
            return len(tail) >= len(suffix) and tuple(p.casefold() for p in tail[:len(suffix)]) == tuple(p.casefold() for p in suffix)
    return False


def guard(path, *, output=False, directory=False, absent=False):
    """Reserve the fixed subtree before ordinary I/O, even without selection."""
    path = _unalias(path)
    protected = _unalias(ROOT / STORE_RELATIVE)
    if _contains(protected, path) or (output and _contains(path, protected)):
        raise OriginError('Ordinary path overlaps protected formal origin material')
    try:
        info = path.stat()
    except FileNotFoundError:
        if absent or output:
            return path
        raise
    if directory:
        if not stat.S_ISDIR(info.st_mode):
            raise OriginError('Expected a regular evidence directory')
    elif not output and not stat.S_ISREG(info.st_mode):
        raise OriginError('Ordinary input is not a regular file')
    if stat.S_ISREG(info.st_mode) and info.st_nlink != 1:
        raise OriginError('Multiply linked ordinary files are unsupported')
    return path


def _read_regular(path, *, private=False, single_link=True, max_bytes=None):
    flags = os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK
    fd = os.open(path, flags)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or (single_link and info.st_nlink != 1):
            raise OriginError('Expected a singly linked regular file')
        if private and (info.st_uid != os.getuid() or info.st_mode & 0o077):
            raise OriginError('Formal origin file is not owner-only')
        if max_bytes is not None and info.st_size > max_bytes:
            raise OriginError('Input exceeds selected byte resource limit', 'incomplete')
        with os.fdopen(fd, 'rb', closefd=False) as stream:
            raw = stream.read() if max_bytes is None else stream.read(max_bytes + 1)
        if max_bytes is not None and len(raw) > max_bytes:
            raise OriginError('Input exceeds selected byte resource limit', 'incomplete')
        after = os.fstat(fd)
        if (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns) != (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns):
            raise OriginError('Input changed during acquisition')
        return raw
    finally:
        os.close(fd)


def read(path, *, max_bytes=None):
    return _read_regular(guard(path), max_bytes=max_bytes)


def _private_dir(path):
    path = _unalias(path)
    info = path.stat()
    if not stat.S_ISDIR(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o077:
        raise OriginError('Formal origin directory is not owner-only')
    return path


def selection():
    """Trusted fixed startup coordinate; absence never initializes a store."""
    path = ROOT / ORIGIN_SELECTION_PIN
    _unalias(path)
    if not path.exists():
        return None
    _private_dir(ROOT / STORE_RELATIVE)
    raw = _read_regular(path, private=True)
    selected = decode(raw)
    if (not isinstance(selected, dict) or set(selected) != {'schema', 'origin_id', 'store_relative', 'key_sha256'}
            or selected['schema'] != SELECTION or selected['store_relative'] != STORE_RELATIVE
            or not _hex(selected['origin_id'], 32) or not _hex(selected['key_sha256'])):
        raise OriginError('Invalid fixed formal origin selection')
    return selected, sha(raw)


def _origin():
    selected = selection()
    if selected is None:
        return None, 'no selected local origin'
    store = _private_dir(ROOT / STORE_RELATIVE)
    try:
        key = _read_regular(_unalias(store / 'origin.key'), private=True)
        _private_dir(store / 'entries')
        _private_dir(store / 'pending')
    except FileNotFoundError:
        return None, 'selected local origin unavailable'
    if len(key) != 32 or sha(key) != selected[0]['key_sha256']:
        raise OriginError('Selected local origin key binding changed')
    return (selected[0], selected[1], key), None


def _write(path, raw):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    try:
        with os.fdopen(fd, 'wb', closefd=False) as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(fd)
    finally:
        os.close(fd)


def _flush(directory):
    fd = os.open(directory, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def init_origin():
    """Explicit setup only. No location/key arguments and no overwrite/repair."""
    store = _unalias(ROOT / STORE_RELATIVE)
    store.parent.mkdir(mode=0o700, exist_ok=True)
    store.mkdir(mode=0o700, exist_ok=False)
    (store / 'entries').mkdir(mode=0o700)
    (store / 'pending').mkdir(mode=0o700)
    key = secrets.token_bytes(32)
    selected = {'schema': SELECTION, 'origin_id': secrets.token_hex(16),
                'store_relative': STORE_RELATIVE, 'key_sha256': sha(key)}
    _write(store / 'origin.key', key)
    _write(store / 'selection.json', canonical(selected))
    _flush(store)
    return selected


def compatible(saved, current):
    """Standalone cold compatibility only; full local/live equality stays strict."""
    for identity in (saved, current):
        if (not isinstance(identity, dict) or set(identity) != {'sha256', 'pins'}
                or not isinstance(identity['pins'], dict) or not identity['pins']
                or not _hex(identity['sha256']) or sha(canonical(identity['pins'])) != identity['sha256']):
            raise OriginError('Malformed aggregate runtime identity')
        for name, value in identity['pins'].items():
            if (not isinstance(name, str) or not name or '\\' in name or Path(name).is_absolute()
                    or any(part in ('', '.', '..') for part in name.split('/')) or not _hex(value)):
                raise OriginError('Malformed runtime identity member')
    return ({k: v for k, v in saved['pins'].items() if k != ORIGIN_SELECTION_PIN}
            == {k: v for k, v in current['pins'].items() if k != ORIGIN_SELECTION_PIN})


def bundle(directory):
    directory = guard(directory, directory=True)
    manifest_raw, result_raw = read(directory / 'manifest.json'), read(directory / 'result.json')
    manifest, result = decode(manifest_raw), decode(result_raw)
    if (not isinstance(manifest, dict) or set(manifest) != {'schema', 'members'}
            or manifest['schema'] != 'a_c.formal-gate.bundle/1' or not isinstance(manifest['members'], dict)
            or not isinstance(result, dict) or result.get('evidence') != {'manifest_sha256': sha(manifest_raw), 'members': manifest['members']}):
        raise OriginError('Evidence manifest binding mismatch')
    for name, expected in manifest['members'].items():
        member_name(name)
        if not _hex(expected) or sha(read(directory / name)) != expected:
            raise OriginError('Retained evidence member missing or changed: ' + name)
    return result, manifest


def member_name(name):
    if (not isinstance(name, str) or not name or name in ('.', '..', 'result.json', 'manifest.json', 'local-origin.json')
            or '/' in name or '\\' in name or '\x00' in name):
        raise OriginError('Malformed retained member name')
    return name


def origin_name(name, layout):
    return 'origin-' + name if layout == 'reuse' and name in METADATA else name


def binding(directory, layout, selected, selection_sha):
    """Reconstruct exact claims from retained bytes; this does not confer trust."""
    result_raw = read(directory / origin_name('result.json', layout))
    manifest_raw = read(directory / origin_name('manifest.json', layout))
    result, manifest = decode(result_raw), decode(manifest_raw)
    if (not isinstance(manifest, dict) or set(manifest) != {'schema', 'members'}
            or manifest['schema'] != 'a_c.formal-gate.bundle/1' or not isinstance(manifest['members'], dict)
            or not isinstance(result, dict) or result.get('status') != 'verified' or not result.get('checked_claims')
            or result.get('requested_claims') != result['checked_claims']
            or result.get('evidence') != {'manifest_sha256': sha(manifest_raw), 'members': manifest['members']}):
        raise OriginError('Original cold result or manifest binding changed')
    for name, expected in manifest['members'].items():
        member_name(name)
        if name.startswith('origin-') or not _hex(expected) or sha(read(directory / origin_name(name, layout))) != expected:
            raise OriginError('Original cold artifact binding changed')
    original = decode(read(directory / origin_name('request.json', layout)))
    replay = decode(read(directory / origin_name('replay-request.json', layout)))
    if sha(canonical(original)) != result['request_sha256']:
        raise OriginError('Original cold request binding changed')
    observations = result['observations']
    return {'origin_id': selected['origin_id'], 'origin_selection_sha256': selection_sha,
            'request_sha256': result['request_sha256'], 'replay_request': replay,
            'resource_limits': observations['limits'], 'model': result['model'], 'inputs': result['inputs'],
            'requested_claims': result['requested_claims'], 'checked_claims': result['checked_claims'],
            'runtime_identity': result['runtime_identity'], 'support': observations['support'],
            'proof_modules': observations['proof_modules'], 'theorem_audit': observations['theorem_audit'],
            'result_sha256': sha(result_raw), 'manifest_sha256': sha(manifest_raw), 'members': manifest['members']}


def _install(pending, final, raw, *, private):
    """POSIX atomic no-overwrite insertion; an existing meaning is immutable."""
    try:
        os.link(pending, final, follow_symlinks=False)
    except FileExistsError:
        existing = _read_regular(_unalias(final), private=True, single_link=False) if private else read(final)
        if existing != raw:
            raise OriginError('Concurrent publication differs from immutable entry')
    _flush(final.parent)


def publish_hint(directory, origin_id, entry_id, layout):
    raw = canonical({'schema': HINT, 'origin_id': origin_id, 'entry_id': entry_id, 'layout': layout})
    guard(directory, output=True, directory=True)
    temp = directory / ('.origin-hint-' + secrets.token_hex(16))
    _write(temp, raw)
    try:
        _install(temp, directory / 'local-origin.json', raw, private=False)
    finally:
        temp.unlink(missing_ok=True)


def _establish(directory, origin):
    """Called only by the completed cold path, after result/manifest finalization."""
    selected, selection_sha, key = origin
    if _origin()[0] != origin:
        raise OriginError('Local origin changed during cold checking')
    body = binding(directory, 'cold', selected, selection_sha)
    raw_body = canonical(body)
    entry_id = sha(raw_body)
    raw = canonical({'schema': ENTRY, 'body': body, 'hmac_sha256': hmac.new(key, DOMAIN + raw_body, hashlib.sha256).hexdigest()})
    store = _private_dir(ROOT / STORE_RELATIVE)
    pending = store / 'pending' / (secrets.token_hex(16) + '.json')
    _write(pending, raw)
    try:
        publish_hint(directory, selected['origin_id'], entry_id, 'cold')
        # The only eligibility commit. A hint/pending file cannot establish it.
        _install(pending, store / 'entries' / (entry_id + '.json'), raw, private=True)
    finally:
        pending.unlink(missing_ok=True)
    return entry_id


def lookup(directory, current_identity, limits):
    origin, unavailable = _origin()
    if origin is None:
        return None, unavailable
    hint_path = directory / 'local-origin.json'
    if not hint_path.exists() and not hint_path.is_symlink():
        return None, 'no local origin hint'
    hint = decode(read(hint_path))
    if (not isinstance(hint, dict) or set(hint) != {'schema', 'origin_id', 'entry_id', 'layout'}
            or hint['schema'] != HINT or not _hex(hint['origin_id'], 32) or not _hex(hint['entry_id'])
            or hint['layout'] not in ('cold', 'reuse')):
        raise OriginError('Malformed public origin hint')
    selected, selection_sha, key = origin
    if hint['origin_id'] != selected['origin_id']:
        return None, 'foreign local origin hint'
    path = ROOT / STORE_RELATIVE / 'entries' / (hint['entry_id'] + '.json')
    try:
        entry = decode(_read_regular(_unalias(path), private=True, single_link=False))
    except FileNotFoundError:
        return None, 'no committed local establishment'
    if not isinstance(entry, dict) or set(entry) != {'schema', 'body', 'hmac_sha256'} or entry['schema'] != ENTRY:
        raise OriginError('Malformed private local establishment')
    raw_body = canonical(entry['body'])
    tag = hmac.new(key, DOMAIN + raw_body, hashlib.sha256).hexdigest()
    if not _hex(entry['hmac_sha256']) or not hmac.compare_digest(entry['hmac_sha256'], tag) or sha(raw_body) != hint['entry_id']:
        raise OriginError('Private local establishment seal mismatch')
    body = binding(directory, hint['layout'], selected, selection_sha)
    if canonical(body) != canonical(entry['body']) or body['runtime_identity'] != current_identity or canonical(body['resource_limits']) != canonical(limits):
        raise OriginError('Exact local establishment binding changed')
    return {'body': body, 'hint': hint, 'directory': directory}, None
