"""Read the immutable published 3.0.4 native payload for historical controls."""
from functools import lru_cache
import io
from pathlib import Path, PurePosixPath
import subprocess
import tarfile
import tempfile

COMMIT = '16bc30d215915a4b7b3ed2f13e52e14510ae1c9d'
PREFIX = 'specification_methodology/v3/'
_TEMPORARY = []


@lru_cache(maxsize=1)
def published_payload():
    repository = Path(__file__).resolve().parents[4]
    observed = subprocess.run(['git', '--no-optional-locks', '-C', str(repository), 'rev-parse', COMMIT + '^{commit}'],
                              capture_output=True, check=True).stdout.decode().strip()
    if observed != COMMIT:
        raise ValueError('immutable historical native commit differs')
    raw = subprocess.run(['git', '--no-optional-locks', '-C', str(repository), 'archive', '--format=tar', COMMIT, PREFIX.rstrip('/')],
                         capture_output=True, check=True).stdout
    temporary = tempfile.TemporaryDirectory(prefix='stdo-published-304-tests-'); _TEMPORARY.append(temporary)
    destination = Path(temporary.name).resolve()
    with tarfile.open(fileobj=io.BytesIO(raw)) as archive:
        for member in archive:
            if member.isdir():
                continue
            if not member.isfile() or not member.name.startswith(PREFIX):
                raise ValueError('unsupported historical payload member')
            name = member.name[len(PREFIX):]
            if not name or any(p in ('', '.', '..') for p in name.split('/')) or str(PurePosixPath(name)) != name:
                raise ValueError('unsafe historical payload member')
            target = destination / name; target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('xb') as stream:
                stream.write(archive.extractfile(member).read())
            target.chmod(member.mode & 0o777)
    return destination
