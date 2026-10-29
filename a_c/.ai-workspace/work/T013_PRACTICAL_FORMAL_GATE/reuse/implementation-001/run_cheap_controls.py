"""Explicit lightweight selection; no compiler, live origin, F_P or full model."""
from pathlib import Path
import sys,tempfile,unittest
root=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'candidate/a_c/build_tenants/graphify/test_env'))
tempfile.tempdir=str(root/'tmp')
import test_ac_formal_gate as formal
import test_ac_generate as gen
suite=unittest.TestSuite()
for name in unittest.defaultTestLoader.getTestCaseNames(formal.FormalGateControls):
    if name!='test_outer_timeout_stops_nested_group_with_stalled_parent_and_bounds_pipe_drain':
        suite.addTest(formal.FormalGateControls(name))
selected=(
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
for name in selected:suite.addTest(gen.GenerationTests(name))
result=unittest.TextTestRunner(verbosity=2).run(suite)
raise SystemExit(0 if result.wasSuccessful() else 1)
