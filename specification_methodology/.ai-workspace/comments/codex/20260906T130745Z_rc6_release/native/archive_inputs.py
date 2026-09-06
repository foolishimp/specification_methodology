"""Retain duplicated qualification input copies in a verified compact archive."""
from pathlib import Path
import gzip
import hashlib
import json
import shutil
import tarfile

HERE = Path(__file__).resolve().parent


def file_record(path):
    if path.is_symlink():
        return {'type': 'symlink', 'target': str(path.readlink())}
    return {'type': 'file', 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def main():
    selection = json.loads((HERE / 'coverage-selection.json').read_text())
    inputs = [Path(c['directory']) / 'input' for c in selection['contexts']]
    assert all((p.parent / 'execution-result.json').is_file() for p in inputs)
    archive = HERE / 'input-snapshots.tar.gz'
    assert not archive.exists(), 'Refuse to replace retained custody'
    paths = sorted(p for root in inputs for p in root.rglob('*')
                   if p.is_file() or p.is_symlink())
    expected = {str(p.relative_to(HERE)): file_record(p) for p in paths}
    temporary = archive.with_suffix('.tmp')
    assert not temporary.exists()
    with temporary.open('wb') as raw:
        with gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode='w') as tar:
                for path in paths:
                    info = tar.gettarinfo(str(path), str(path.relative_to(HERE)))
                    info.uid = info.gid = info.mtime = 0
                    info.uname = info.gname = ''
                    if info.isfile():
                        with path.open('rb') as source:
                            tar.addfile(info, source)
                    else:
                        tar.addfile(info)
    observed = {}
    with tarfile.open(temporary, 'r:gz') as tar:
        for member in tar.getmembers():
            assert member.name not in observed
            if member.issym():
                observed[member.name] = {'type': 'symlink', 'target': member.linkname}
            else:
                assert member.isfile()
                observed[member.name] = {'type': 'file', 'sha256': hashlib.sha256(tar.extractfile(member).read()).hexdigest()}
    assert observed == expected
    assert {str(p.relative_to(HERE)): file_record(p) for p in paths} == expected
    temporary.rename(archive)
    report = {'archive': archive.name, 'archive_sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
              'members': expected, 'member_count': len(expected), 'verified': True,
              'scope': 'Only the retained duplicate input directories are compacted. Raw outputs, results and actual isolated worksites are unchanged.',
              'recovery': 'Archive member names preserve each original path relative to this native evidence directory.'}
    (HERE / 'input-custody.json').write_text(json.dumps(report, indent=2) + '\n')
    for root in inputs:
        shutil.rmtree(root)
    print(json.dumps({key: value for key, value in report.items() if key != 'members'}))


if __name__ == '__main__':
    main()
