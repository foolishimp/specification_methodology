"""I5 coordinates and pure helpers; historical libraries are read-only inputs."""
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
PRIOR = HERE.parent / 'iteration-4'
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


def exact_commit(commit):
    if not isinstance(commit, str) or len(commit) != 40 or any(c not in '0123456789abcdef' for c in commit):
        raise ValueError('An exact full commit is required')
    result = subprocess.check_output(['git', 'rev-parse', commit + '^{commit}'], cwd=REPO, text=True).strip()
    if result != commit:
        raise ValueError('Commit does not resolve to itself')
    return commit


def git_bytes(commit, path):
    exact_commit(commit)
    path = Path(path)
    if path.is_absolute() or '..' in path.parts:
        raise ValueError('Git path must be repository relative')
    return subprocess.check_output(['git', 'show', commit + ':' + str(path)], cwd=REPO)


def library(relative):
    path = HERE.parent / relative
    if relative not in INPUTS['libraries'] or sha(path.read_bytes()) != INPUTS['libraries'][relative]:
        raise ValueError('Construction library changed or unselected: ' + relative)
    spec = importlib.util.spec_from_file_location('i5_' + path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def members(root=PACKAGE):
    return [{'path': str(p.relative_to(root)), 'bytes': p.stat().st_size, 'sha256': sha(p.read_bytes())}
            for p in sorted(root.rglob('*')) if p.is_file()]


def exact_source(commit):
    import build_interpretation
    return build_interpretation.documentary_inventory(exact_commit(commit))


def verify_common():
    """Work-state advancement does not rebind constitutional inputs."""
    common = TENANT.parents[1] / 'specification'
    paths = [common / n for n in ('INTENT.md', 'PRODUCT.md', 'REFERENCE_FRAME_BASIS.md')]
    paths += sorted((common / 'requirements').rglob('*.md'))
    paths += sorted((common / 'conformance').rglob('*.md'))
    for path in paths:
        if git_bytes(INPUTS['common_input'], path.relative_to(REPO)) != path.read_bytes():
            raise ValueError('Common constitutional input drift: ' + str(path.relative_to(REPO)))
    return INPUTS['common_input']
