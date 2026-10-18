import os
from pathlib import Path
import copy,json,hashlib,subprocess,importlib.util,sys
from stdo_toolchain.manifest import verify_materialization, standards_member_set_sha256
sys.dont_write_bytecode=True
b=Path(os.environ['STDO_RC9_REPLAY_ROOT']);cl=b/'claude/specification_methodology/v3/build_tenants/claude';cx=b/'codex/specification_methodology/v3/build_tenants/codex/successor';installed=b/'claude-manifest-set';m=json.loads((installed/'manifest.json').read_text())
n=copy.deepcopy(m);n['release'].update(project_release_namespace='specification_methodology',qualified_ref='refs/tags/specification_methodology/v3.0.0-rc.9',project_subtree_root='specification_methodology/v3')
r={'namespace_and_subtree_only_normalized':verify_materialization(installed,n)}
n['standards']['member_set_sha256']=standards_member_set_sha256(n['standards']['members']);r['plus_canonical_digest_normalized']=verify_materialization(installed,n)
r['manifest_inventory']={'standards':len(m['standards']['members']),'plugin':len(m['auxiliary']['plugin']['members']),'license':1,'release_note':1,'manifest':1,'interpretation':0};r['manifest_source_path_misses']=[row['path'] for row in m['standards']['members'] if not (cl/m['standards']['source_root']/row['path']).exists()]
# Compiler pure function generation against frozen semantic account and scratch source.
compiler=b/'codex/specification_methodology/v3/build_tenants/codex/qualification/C3/iteration-5/tools/build_interpretation.py'
s=importlib.util.spec_from_file_location('replay_build',compiler);mod=importlib.util.module_from_spec(s);s.loader.exec_module(mod);mod.PACKAGE=cx
account=json.loads((cx/'interpretation/source-account.json').read_text());mod.validate_account(account,package=cx)
p,mapping,frames=mod.build_program(account)
r['codex_regeneration']={'program_byte_identical':mod.json_bytes(p)==(cx/'interpretation/program.json').read_bytes(),'frames_byte_identical':frames.encode()==(cx/'interpretation/FRAMES.md').read_bytes(),'mapping_rows_identical':mapping==json.loads((cx/'interpretation/MAPPING.json').read_text())['rows'],'determinations':len(account['determinations']),'clauses':len(p['clauses']),'indexes':len(p['frame_indexes'])}
for name,root in [('claude',cl),('codex',cx)]:
 std=list((root/'standards').glob('*.md')); allstd=[p for p in (root/'standards').rglob('*') if p.is_file()]; plug=[p for p in (root/'plugins').rglob('*') if p.is_file()]
 r[name+'_sizes']={'top_level_standards_files':len(std),'top_level_standards_bytes':sum(p.stat().st_size for p in std),'all_standards_files':len(allstd),'all_standards_bytes':sum(p.stat().st_size for p in allstd),'plugin_files':len(plug),'plugin_bytes':sum(p.stat().st_size for p in plug)}
(b/'controls-results.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
