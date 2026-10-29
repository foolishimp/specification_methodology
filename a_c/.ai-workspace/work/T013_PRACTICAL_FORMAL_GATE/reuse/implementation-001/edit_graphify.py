from pathlib import Path
stage=Path(__file__).resolve().parent
root=stage/'candidate/a_c/build_tenants/graphify/code'
p=root/'ac_formal_gate.py';s=p.read_text();s=s.replace('import signal\n','import signal\nimport stat\n',1)
pos=s.index('\ndef validate_config(')
s=s[:pos]+'''

def _unalias(path: Path) -> Path:
    path = path.absolute()
    for part in reversed((path, *path.parents)):
        try:
            info = part.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode):
            raise GateError("refused", "Symlink path is outside selected formal acquisition")
    return path.resolve(strict=False)


def guard_path(config: dict[str, Any], path: Path, *, output: bool = False,
               directory: bool = False, absent: bool = False) -> Path:
    """Reserve actual mediated paths; broad registered source roots stay valid.

    The selected checker configuration is trusted. No Lean/helper/key read is
    needed for reservation, including before local origin setup exists.
    """
    path = _unalias(path)
    protected = _unalias(Path(config["root"]) / ".cache/formal-origin-v1")
    if path == protected or path.is_relative_to(protected) or (output and protected.is_relative_to(path)):
        raise GateError("refused", "Ordinary path overlaps protected formal origin material")
    try:
        info = path.stat()
    except FileNotFoundError:
        if output or absent:
            return path
        raise
    if directory:
        if not stat.S_ISDIR(info.st_mode):
            raise GateError("refused", "Expected a regular selected directory")
    elif not output and not stat.S_ISREG(info.st_mode):
        raise GateError("refused", "Selected input is not a regular file")
    if stat.S_ISREG(info.st_mode) and info.st_nlink != 1:
        raise GateError("refused", "Multiply linked selected input/output is unsupported")
    return path


def read_selected(config: dict[str, Any], path: Path) -> bytes:
    path = guard_path(config, path)
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise GateError("refused", "Expected singly linked selected input")
        with os.fdopen(fd, "rb", closefd=False) as stream:
            raw = stream.read()
        after = os.fstat(fd)
        if (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns) != (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns):
            raise GateError("refused", "Selected input changed during acquisition")
        return raw
    finally:
        os.close(fd)
''' +s[pos:]
s=s.replace('    (bundle.parent / "checker.stdout").write_bytes(process.stdout)', '    guard_path(config, bundle.parent / "checker.stdout", output=True)\n    guard_path(config, bundle.parent / "checker.stderr", output=True)\n    (bundle.parent / "checker.stdout").write_bytes(process.stdout)',1)
s=s.replace('_regular(bundle / "result.json")', 'read_selected(config, bundle / "result.json")')
s=s.replace('    current(config)\n    output = output.absolute()\n    output.mkdir(parents=True, exist_ok=False)', '    validate_config(config)\n    output = guard_path(config, output, output=True)\n    current(config)\n    output.mkdir(parents=True, exist_ok=False)',1)
s=s.replace('    """Fresh proof replay from a hash-bound protected receipt, never saved success."""\n    current(config)\n    bundle = Path(retained["bundle"])', '    """Current exact checking; eligible local cold establishments may be reused."""\n    validate_config(config)\n    output = guard_path(config, output, output=True)\n    bundle = guard_path(config, Path(retained["bundle"]), directory=True)\n    current(config)',1)
p.write_text(s)
p=root/'ac_support_core.py';s=p.read_text();needle='def source_path(runtime: Runtime, ref: Object, *, write: bool = False,'
pos=s.index(needle)
s=s[:pos]+'''def _formal_source_path(runtime: Runtime, path: Path, *, write: bool, absent: bool = False) -> Path:
    selected = runtime.policy.get("formal_gate")
    if selected is not None:
        try:
            ac_formal_gate.guard_path(as_object(selected)["checker"], path, output=write, absent=absent)
        except ac_formal_gate.GateError as exc:
            raise SupportError("path_refused", str(exc)) from exc
    return path


'''+s[pos:]
s=s.replace('                return current\n            raise SupportError("source_missing"', '                return _formal_source_path(runtime, current, write=write, absent=True)\n            raise SupportError("source_missing"',1)
s=s.replace('    return current\n\n\ndef read_source(', '    return _formal_source_path(runtime, current, write=write)\n\n\ndef read_source(',1)
p.write_text(s)
print('Updated staged Graphify adapter and precise SourceRef guards.')
