"""Measure isolated catalog prototype against retained current010 bytes."""
from pathlib import Path
import collections
import hashlib
import importlib.util
import json
import resource
import sys
import time

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'a_c').is_dir() and (p / 'stdo_skills').is_dir())
ORACLE = HERE.parent.parent / 'packaging-integration-001/current-proofs-010'
sys.path.insert(0, str(HERE / 'prototype'))
import proof_reader as optimized
import proof_reader_current as current

spec = importlib.util.spec_from_file_location('baseline_reader', HERE / 'baseline/proof_reader.py')
baseline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(baseline)


def sha(raw): return hashlib.sha256(raw).hexdigest()
def pin(path):
    raw = path.read_bytes()
    return {'path': str(path), 'sha256': sha(raw), 'bytes': len(raw)}
def elapsed(call):
    wall, cpu = time.perf_counter(), time.process_time()
    result = call()
    return result, {'wall_seconds': time.perf_counter() - wall, 'cpu_seconds': time.process_time() - cpu}
def outcome(function, source):
    try: return {'value': function(source)}
    except ValueError as error: return {'error': type(error).__name__, 'message': str(error)}


def main():
    expected_catalog = (ORACLE / 'PROOFS.json').read_bytes()
    expected_html = (ORACLE / 'index.html').read_bytes()
    expected = json.loads(expected_catalog)
    files = {p.relative_to(ORACLE).as_posix(): p.read_bytes() for p in ORACLE.rglob('*') if p.is_file()}
    lexical_measurements = []
    actual_function = optimized.source_catalog
    def measured(sources):
        result, timing = elapsed(lambda: actual_function(sources))
        lexical_measurements.append(timing)
        return result
    optimized.source_catalog = measured
    (value, sources), catalog_time = elapsed(lambda: current.catalog(files))
    optimized.source_catalog = actual_function
    catalog_raw, encoding_time = elapsed(lambda: current.a.encoded(value))
    html, render_time = elapsed(lambda: current.render(value, sources))
    assert catalog_raw == expected_catalog, 'Full catalog bytes differ from retained oracle'
    assert html == expected_html, 'Full HTML bytes differ from retained oracle'
    assert len(lexical_measurements) == 1
    source_pins = []
    for source in expected['sources']:
        name = source['file']
        path = ORACLE / ('machinery/' + name.removeprefix('library/') if name.startswith('library/') else 'evidence/' + name.removeprefix('current/'))
        raw = path.read_bytes()
        assert sha(raw) == source['sha256'] and raw.decode() == sources[name]
        source_pins.append({'file': name, **pin(path)})
    report = {'schema': 'stdo305.reader-performance-investigation/1',
        'standing': 'Isolated prototype evidence only; production/checkpoint unchanged; no fresh Lean or release verdict.',
        'python': {'invocation': sys.executable, 'version': sys.version, 'physical': pin(Path(sys.executable).resolve())},
        'prototype': json.loads((HERE / 'PROTOTYPE.json').read_text()),
        'oracle': {'catalog': pin(ORACLE / 'PROOFS.json'), 'html': pin(ORACLE / 'index.html'),
                   'build_receipt': pin(ORACLE.parent / 'current010-assembly-execution/proof.execution.json')},
        'full_comparison': {'catalog_bytes_equal': True, 'html_bytes_equal': True, 'source_files': len(sources),
            'source_bytes': sum(len(text.encode()) for text in sources.values()),
            'declarations': len(value['declarations']), 'references': sum(len(d['references']) for d in value['declarations']),
            'catalog': catalog_time, 'lexical_source_catalog': lexical_measurements[0],
            'encode_catalog': encoding_time, 'render': render_time,
            'peak_rss_bytes_darwin': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},
        'source_pins': source_pins}
    (HERE / 'FULL_COMPARISON.json').write_bytes(current.a.encoded(report))
    print(json.dumps({'phase': 'full-comparison', **report['full_comparison']}), flush=True)

    library = {name: text for name, text in sources.items() if name.startswith('library/')}
    cases = {
        'actual_six_library_sources': library,
        'nested_scopes_and_ambiguous_suffix': {'Demo.lean': 'namespace A\ndef base : Nat := 1\nnamespace Inner\ndef nested := base + A.base\nend Inner\nend A\nnamespace B\ndef base := 2\ndef uses := base + A.base\nend B\ndef unresolved := base\n'},
        'comment_string_and_anonymous_boundaries': {'Demo.lean': 'namespace Demo\ndef one : Nat := 1\ninstance : Inhabited Nat := ⟨one⟩\n/- theorem Fake : False := by\n /- nested -/ -/\ninstance chosen : Inhabited Nat := ⟨one⟩\nexample : one = 1 := rfl\ndef text : String := "theorem hidden := one"\n-- theorem ignored : False := by\ntheorem valid : one = 1 := rfl\nend Demo\n'},
        'duplicate_token_on_same_and_next_line': {'a.lean': 'def first : Nat := 1\ndef next := first + first +\n first\n\n'},
        'multiline_strings_and_escaped_quote': {'a.lean': 'def first : Nat := 1\ndef hidden := "first\\\" first\nfirst"\ndef visible := first\n'},
        'crlf': {'a.lean': 'def first : Nat := 1\r\ndef next := first +\r\n first\r\n'},
        'cr_and_unicode_line_breaks': {'a.lean': 'def first : Nat := 1\rdef next := first\u2028def final := next\n'},
        'empty_and_final_line_without_newline': {'empty.lean': '', 'one.lean': 'def x := 0\ndef y := x'},
        'long_reference_body': {'long.lean': 'def first : Nat := 1\ndef total :=\n' + ' first +\n' * 4000 + ' first\n'},
        'duplicate_declaration_refusal': {'a.lean': 'def x := 0\n', 'b.lean': 'def x := 1\n'},
        'unterminated_comment_refusal': {'a.lean': 'def x := 0\n/- missing end\n'},
        'unterminated_string_refusal': {'a.lean': 'def x := "missing end\n'},
    }
    comparisons = []
    for name, selected in cases.items():
        old, old_time = elapsed(lambda: outcome(baseline.source_catalog, selected))
        new, new_time = elapsed(lambda: outcome(actual_function, selected))
        assert old == new, name
        raw = current.a.encoded(new)
        comparisons.append({'case': name, 'baseline': old_time, 'prototype': new_time, 'equal': True,
            'result_sha256': sha(raw), 'result_kind': 'refused' if 'error' in new else 'catalog',
            'source_sha256': sha(current.a.encoded(selected))})
    (HERE / 'SMALL_INPUTS.json').write_bytes(current.a.encoded(cases))
    (HERE / 'SMALL_COMPARISONS.json').write_bytes(current.a.encoded(comparisons))
    print(json.dumps({'phase': 'small-comparisons', 'cases': len(comparisons), 'all_equal': True}), flush=True)

    # Count the work implied by the old loops without executing their repeated
    # full-file splitting or quadratic prefix copies/counts.
    masked_lines = {name: optimized.mask_noncode(text).splitlines(keepends=True) for name, text in sources.items()}
    counts = collections.Counter(d['file'] for d in value['declarations'])
    by_file = []
    total_old_prefix = total_new_scan = total_tokens = 0
    for name, lines in masked_lines.items():
        old_prefix = scanned = tokens = 0
        for declaration in (d for d in value['declarations'] if d['file'] == name):
            body = ''.join(lines[declaration['start_line'] - 1:declaration['end_line']])
            previous = 0
            for token in optimized.TOKEN.finditer(body):
                position = token.start()
                old_prefix += position
                scanned += position - previous
                previous = position
                tokens += 1
        by_file.append({'file': name, 'characters': len(sources[name]), 'declarations': counts[name],
            'old_full_file_split_characters': len(sources[name]) * counts[name],
            'new_reference_phase_full_file_splits': 0, 'token_matches': tokens,
            'old_prefix_count_characters': old_prefix, 'new_monotonic_count_characters': scanned})
        total_old_prefix += old_prefix; total_new_scan += scanned; total_tokens += tokens
    costs = {'scope': 'Exact loop-work counts from the retained full corpus; not a timing of the slow full baseline.',
             'files': by_file, 'old_reference_phase_split_characters': sum(r['old_full_file_split_characters'] for r in by_file),
             'old_reference_phase_full_file_splits': len(value['declarations']),
             'new_reference_phase_full_file_splits': 0,
             'old_prefix_count_characters': total_old_prefix, 'new_monotonic_count_characters': total_new_scan, 'token_matches': total_tokens}
    (HERE / 'COST_COUNTS.json').write_bytes(current.a.encoded(costs))
    source_file = REPO / 'specification_methodology/v3/build_tenants/common-tools/proof_reader.py'
    assert pin(source_file)['sha256'] == report['prototype']['baseline_sha256'], 'Production source changed during investigation'
    print(json.dumps({'phase': 'cost-counts', **{k: v for k, v in costs.items() if k != 'files'}, 'production_source_unchanged': True}), flush=True)


if __name__ == '__main__': main()
