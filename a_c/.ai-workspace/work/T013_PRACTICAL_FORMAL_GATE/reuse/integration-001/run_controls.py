"""Bounded integrated-path controls; temporary effects stay in this record tree.

Proof/support/runtime are synthetic in the 60 reviewed controls. The existing
57 Python tests add fixture/CLI/source/process integration coverage, no Lean.
No production source is modified by this harness.
"""
from contextlib import ExitStack
import importlib
import json
import os
from pathlib import Path
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

here = Path(__file__).resolve().parent
root = here.parents[4]
lean = root / 'build_tenants/lean'
graphify = root / 'build_tenants/graphify'
mode = sys.argv[1]
temporary = here / 'tmp' / mode
temporary.mkdir(parents=True, exist_ok=True)
tempfile.tempdir = str(temporary)
os.environ.pop('AC_FORMAL_CONTROL_EVIDENCE', None)
os.environ['TMPDIR'] = str(temporary)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
original_temporary_directory = tempfile.TemporaryDirectory
original_mkdir = Path.mkdir
redirected = {lean / '.cache', lean / '.cache/reuse-unit'}

def temporary_directory(*args, **kwargs):
    if kwargs.get('dir') is not None and Path(kwargs['dir']) in redirected:
        kwargs['dir'] = temporary
    return original_temporary_directory(*args, **kwargs)

def mkdir(path, *args, **kwargs):
    if path in redirected:
        return None
    return original_mkdir(path, *args, **kwargs)

# Imports and execution use the integrated live files. Only temporary storage
# and the two hard-coded test cache mkdir calls are redirected by the harness.
with ExitStack() as stack:
    stack.enter_context(patch.object(tempfile, 'TemporaryDirectory', temporary_directory))
    stack.enter_context(patch.object(Path, 'mkdir', mkdir))
    if mode == 'lean-reuse':
        sys.path.insert(0, str(lean / 'tests'))
        module = importlib.import_module('test_formal_reuse')
        suite = unittest.defaultTestLoader.loadTestsFromModule(module)
        expected = 19
    elif mode == 'graphify-origin':
        sys.path.insert(0, str(graphify / 'test_env'))
        module = importlib.import_module('test_ac_formal_origin_paths')
        suite = unittest.defaultTestLoader.loadTestsFromModule(module)
        expected = 10
    elif mode == 'compatibility':
        sys.path.insert(0, str(graphify / 'test_env'))
        formal = importlib.import_module('test_ac_formal_gate')
        gen = importlib.import_module('test_ac_generate')
        suite = unittest.TestSuite()
        for name in unittest.defaultTestLoader.getTestCaseNames(formal.FormalGateControls):
            if name != 'test_outer_timeout_stops_nested_group_with_stalled_parent_and_bounds_pipe_drain':
                suite.addTest(formal.FormalGateControls(name))
        selected = (
            'test_snapshot_and_chunks_cover_exact_original_source',
            'test_heading_identity_survives_inserted_lines_and_fences',
            'test_fence_width_marker_indentation_and_closing_content_preserve_partitions',
            'test_chunks_pack_files_and_split_sections_without_loss',
            'test_oversize_single_line_explicitly_refuses',
            'test_stale_source_and_path_escape_refuse',
            'test_source_symlink_escape_refuses_before_snapshot',
            'test_exact_quote_and_range_are_checked',
            'test_extra_author_fields_and_missing_source_disposition_refuse',
            'test_partial_assembly_requires_explicit_flag_and_keeps_refusals',
            'test_immutable_successful_answer_and_normal_assembly',
            'test_ordinary_reuse_rechecks_settings_argv_schema_usage_and_source_despite_refreshed_hashes',
            'test_source_instructions_remain_data_and_direct_prompt_has_no_graph',
            'test_graph_context_prioritizes_semantic_nodes_and_retains_links',
            'test_complete_dense_graph_context_stays_inside_exact_character_cap',
            'test_structural_failure_is_retained_and_blocks_discovery_success',
            'test_wrong_chunk_custody_and_nonfinite_json_refuse')
        for name in selected:
            suite.addTest(gen.GenerationTests(name))
        expected = 31
    elif mode == 'lean-existing':
        sys.path.insert(0, str(lean / 'tests'))
        suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromModule(importlib.import_module(name))
                                   for name in ('test_adapter', 'test_formal_gate', 'test_runtime_process'))
        expected = 57
    else:
        raise SystemExit('Unknown bounded control group')
    assert suite.countTestCases() == expected, (mode, suite.countTestCases(), expected)
    started = time.monotonic()
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    record = {'mode': mode, 'integrated_source_root': str(root), 'tests': result.testsRun,
              'expected_tests': expected, 'failures': len(result.failures), 'errors': len(result.errors),
              'skips': len(result.skipped), 'elapsed_seconds': time.monotonic() - started,
              'status': 'PASS' if result.wasSuccessful() else 'FAIL',
              'evidence_kind': 'Python integration controls; synthetic proof support only; no actual proof qualification',
              'temporary_write_root': str(temporary)}
    (here / (mode + '-result.json')).write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(record))
    raise SystemExit(0 if result.wasSuccessful() else 1)
