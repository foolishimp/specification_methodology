from pathlib import Path
stage=Path(__file__).resolve().parent
p=stage/'candidate/a_c/build_tenants/graphify/code/ac_generate.py';s=p.read_text()
def replace(a,b):
    global s
    assert a in s,a[:100]
    s=s.replace(a,b,1)
replace('def load(path: Path) -> Any:\n', 'def _decode(raw: bytes) -> Any:\n')
replace('    return json.loads(path.read_bytes(), object_pairs_hook=pairs, parse_constant=invalid_constant)', '    return json.loads(raw, object_pairs_hook=pairs, parse_constant=invalid_constant)\n\n\ndef load(path: Path) -> Any:\n    return _decode(path.read_bytes())')
pos=s.index('\ndef prepare(')
s=s[:pos]+'''

def _selected_path(checker: dict[str, Any] | None, path: Path, *, write: bool = False,
                   directory: bool = False, absent: bool = False) -> Path:
    if checker is not None:
        return ac_formal_gate.guard_path(checker, path, output=write, directory=directory, absent=absent)
    return path


def _selected_read(checker: dict[str, Any] | None, path: Path) -> bytes:
    return ac_formal_gate.read_selected(checker, path) if checker is not None else path.read_bytes()


def _resolve_selection(plan: dict[str, Any], retained: Any, present: bool,
                       selected: dict[str, Any] | None) -> dict[str, Any] | None:
    prior = plan.get("formal_checker")
    if present:
        require(prior is None or retained == prior, "prepared formal checker selection changed")
        prior = retained
    elif prior is not None:
        raise GenerationError("prepared required formal checker selection is missing")
    if prior is not None and selected is not None:
        require(prior == selected, "required formal checker cannot be changed during generation")
    result = prior if prior is not None else selected
    if result is not None:
        ac_formal_gate.validate_config(result)
    return result


def _startup(output: Path, selected: dict[str, Any] | None = None) -> tuple[dict[str, Any], dict[str, Any] | None]:
    """Read only the operator-owned fixed startup files before reservation.

    This does not authenticate arbitrary request-selected run directories. The
    operator/wrapper owns the run and selection, under the cooperative host
    contract. No plan-named content is read until selected guards are active.
    """
    if selected is not None:
        ac_formal_gate.validate_config(selected)
        _selected_path(selected, output, write=True, directory=True)
    plan_path, selection_path = output / "plan.json", output / "formal-selection.json"
    _selected_path(selected, plan_path)
    _selected_path(selected, selection_path, absent=True)
    plan_raw = plan_path.read_bytes()
    present = selection_path.exists()
    selection_raw = selection_path.read_bytes() if present else None
    try:
        plan = _decode(plan_raw)
        retained = _decode(selection_raw) if present else None
    except (ValueError, UnicodeError) as exc:
        raise GenerationError("Malformed trusted generation startup metadata") from None
    checker = _resolve_selection(plan, retained, present, selected)
    if checker is not None:
        _selected_path(checker, output, write=True, directory=True)
        require(_selected_read(checker, plan_path) == plan_raw, "generation plan changed during startup")
        _selected_path(checker, selection_path, absent=True)
        if present:
            require(_selected_read(checker, selection_path) == selection_raw, "formal selection changed during startup")
    return plan, checker


def _run_path(output: Path, path: Path, *, write: bool = False, directory: bool = False,
              absent: bool = False) -> Path:
    _, checker = _startup(output)
    return _selected_path(checker, path, write=write, directory=directory, absent=absent)


def _upstream_path(output: Path, path: Path) -> Path:
    _run_path(output, path, directory=True)
    _run_path(output, path / UPSTREAM_PROMPT)
    return path
''' +s[pos:]
replace('    corpus = corpus.resolve(strict=True)\n    manifest = load(manifest_path)', '''    if formal_checker is not None:
        ac_formal_gate.validate_config(formal_checker)
        _selected_path(formal_checker, output, write=True)
        _selected_path(formal_checker, corpus, directory=True)
        if upstream is not None:
            _selected_path(formal_checker, upstream, directory=True)
            _selected_path(formal_checker, upstream / UPSTREAM_PROMPT)
    corpus = corpus.resolve(strict=True)
    manifest = _decode(_selected_read(formal_checker, manifest_path))''')
replace('        raw = source.read_bytes()', '        raw = _selected_read(formal_checker, source)')
replace('        destination.write_bytes((corpus / entry["path"]).read_bytes())', '        _selected_path(formal_checker, destination, write=True).write_bytes(_selected_read(formal_checker, corpus / entry["path"]))')
replace('        shutil.copyfile(Path(upstream_record["root"]) / UPSTREAM_PROMPT, output / "upstream-extraction-spec.md")', '        (output / "upstream-extraction-spec.md").write_bytes(_selected_read(formal_checker, Path(upstream_record["root"]) / UPSTREAM_PROMPT))')
start=s.index('def checkpoint(');end=s.index('\ndef schema_errors(',start)
s=s[:start]+'''def checkpoint(output: Path, *, formal_checker: dict[str, Any] | None = None) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    plan, checker = _startup(output, formal_checker)
    require(plan.get("profile") == "ac.generation.plan/1", "unknown generation plan")
    def read(path: Path) -> bytes:
        return _selected_read(checker, path)
    require(sha(read(output / "source-manifest.json")) == plan["source_manifest_sha256"], "source manifest changed")
    chunks_raw = read(output / "chunks.json")
    require(sha(chunks_raw) == plan["chunks_sha256"], "chunk plan changed")
    require(sha(read(Path(__file__))) == plan["runner_sha256"], "runner changed since preparation; create a new plan")
    require(sha(read(HERE / "ac_graph.py")) == plan["codec_sha256"], "codec changed since preparation")
    require({path.name: sha(read(path)) for path in ASSETS.iterdir() if path.is_file()} == plan["assets"], "generation schemas/prompts changed")
    for entry in plan["files"]:
        relative = safe_relative(entry["path"]) if checker is not None else entry["path"]
        source = output / "corpus" / relative
        _selected_path(checker, source)
        require(source.resolve(strict=True).is_relative_to((output / "corpus").resolve()), "snapshot source escapes checkpoint")
        require(sha(read(source)) == entry["sha256"], "frozen source bytes changed: " + relative)
    if plan["mode"] == "graphify":
        require(sha(read(output / "upstream-extraction-spec.md")) == plan["upstream"]["prompt_sha256"], "upstream prompt changed")
    return plan, _decode(chunks_raw)

''' +s[end:]
start=s.index('def _formal_selection(');end=s.index('\ndef check_formal_proposal(',start)
s=s[:start]+'''def _formal_selection(output: Path, plan: dict[str, Any], selected: dict[str, Any] | None) -> dict[str, Any] | None:
    path = output / "formal-selection.json"
    if selected is not None:
        ac_formal_gate.validate_config(selected)
        _selected_path(selected, output, write=True, directory=True)
        _selected_path(selected, path, absent=True)
    present = path.exists()
    # This fixed inherited startup locator has the same trusted custody as plan.
    raw = path.read_bytes() if present else None
    result = _resolve_selection(plan, _decode(raw) if present else None, present, selected)
    if result is not None:
        _selected_path(result, output, write=True, directory=True)
        _selected_path(result, path, write=not present)
        if present:
            require(_selected_read(result, path) == raw, "formal selection changed during startup")
        else:
            save(path, result, exclusive=True)
    return result

''' +s[end:]
replace('    plan, chunks = checkpoint(output)\n    formal_checker = _formal_selection(output, plan, formal_checker)', '    plan, chunks = checkpoint(output, formal_checker=formal_checker)\n    formal_checker = _formal_selection(output, plan, formal_checker)')
replace('            plan, _ = checkpoint(args.output)', '            plan, _ = checkpoint(args.output, formal_checker=formal_checker)')
replace('                raw = (folder / (format + ".json")).read_bytes()', '                raw = _selected_read(formal_checker, folder / (format + ".json"))')
# Guard reopened source paths at their actual downstream acquisition boundary.
replace('    reference = (output / "upstream-extraction-spec.md").read_text()', '    reference = _run_path(output, output / "upstream-extraction-spec.md").read_text()')
s=s.replace('upstream_modules(upstream or Path(plan["upstream"]["root"]))', 'upstream_modules(_upstream_path(output, upstream or Path(plan["upstream"]["root"])))')
replace('    structural = modules["extract"].extract([corpus / entry["path"] for entry in plan["files"]]', '    structural = modules["extract"].extract([_run_path(output, corpus / entry["path"]) for entry in plan["files"]]')
# All ordinary output destinations receive protection before creating/reopening.
replace('            path.parent.mkdir(parents=True, exist_ok=True)\n            if path.exists():', '            _run_path(output, path, write=True)\n            path.parent.mkdir(parents=True, exist_ok=True)\n            if path.exists():')
replace('        attempt = root / f"attempt-{len(attempts) + 1:03d}"\n        result = run_actor', '        attempt = root / f"attempt-{len(attempts) + 1:03d}"\n        _run_path(output, attempt, write=True)\n        result = run_actor')
replace('    folder = output / "discovery"\n    if folder.exists():', '    folder = _run_path(output, output / "discovery", write=True)\n    if folder.exists():')
replace('    folder = output / ("partial-proposal" if len(answers) < len(chunks) else "proposal")', '    folder = _run_path(output, output / ("partial-proposal" if len(answers) < len(chunks) else "proposal"), write=True)')
replace('    settings_path = output / "actor-settings.json"', '    settings_path = _run_path(output, output / "actor-settings.json", write=True)')
replace('    save(output / (name + "-status.json"), summary)', '    save(_run_path(output, output / (name + "-status.json"), write=True), summary)')
# Authentication must not read an actor artifact alias before refusing it.
replace('    result = load(attempt / "result.json")\n    invocation = load(attempt / "invocation.json")', '''    for name in paths:
        _run_path(output, attempt / name)
    _run_path(output, attempt / "validation.json", absent=True)
    _run_path(output, output / "actor-settings.json")
    result = load(attempt / "result.json")
    invocation = load(attempt / "invocation.json")''')
replace('    if not (attempt / "result.json").is_file() or load(attempt / "result.json").get("status") != "completed":', '    _run_path(output, attempt / "result.json", absent=True)\n    _run_path(output, attempt / "validation.json", absent=True)\n    if not (attempt / "result.json").is_file() or load(attempt / "result.json").get("status") != "completed":')
replace('    record = load(output / "discovery" / "result.json")', '    record = load(_run_path(output, output / "discovery" / "result.json"))\n    _run_path(output, output / "discovery" / "coverage.json")')
replace('        require(sha((output / "discovery" / path).read_bytes()) == expected, "discovery graph changed: " + path)', '        require(sha(_run_path(output, output / "discovery" / safe_relative(path)).read_bytes()) == expected, "discovery graph changed: " + path)')
replace('    graph = load(output / "discovery" / "graph.json")', '    graph = load(_run_path(output, output / "discovery" / "graph.json"))')
p.write_text(s)
print('Updated selected prepare/checkpoint/resume and actual acquisition guards; no CLI/schema change.')
