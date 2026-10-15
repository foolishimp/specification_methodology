"""Exact I4 construction inputs; reuse checked functions, never historical mains."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent.parent
TENANT = HERE.parents[2]
PACKAGE = TENANT / 'successor'
REPO = TENANT.parents[3]
PRIOR = HERE.parent / 'iteration-3'
INPUTS = json.loads((HERE / 'INPUTS.json').read_text())


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode()


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(encoded(value))


def git_bytes(commit, path):
    if len(commit) != 40 or any(c not in '0123456789abcdef' for c in commit):
        raise ValueError('An exact full commit is required')
    return subprocess.check_output(['git', 'show', commit + ':' + str(path)], cwd=REPO)


def library(relative):
    path = HERE.parent / relative
    if sha(path.read_bytes()) != INPUTS['libraries'][relative]:
        raise ValueError('Construction library changed: ' + relative)
    spec = importlib.util.spec_from_file_location('i4_' + path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def members(root=PACKAGE):
    return [{'path': str(p.relative_to(root)), 'bytes': p.stat().st_size,
             'sha256': sha(p.read_bytes())}
            for p in sorted(root.rglob('*')) if p.is_file()]


def exact_source(commit):
    """The documentary freeze excludes the generated interpretation only."""
    return library('iteration-3/build_interpretation.py').documentary_inventory(commit)


def verify_common():
    library('iteration-3/refresh_current.py').verify_common(INPUTS['common_input'])
