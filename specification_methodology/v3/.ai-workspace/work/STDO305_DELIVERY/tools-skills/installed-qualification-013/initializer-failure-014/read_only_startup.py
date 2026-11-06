from pathlib import Path
import sys,hashlib
sys.dont_write_bytecode=True
sys.path.insert(0,'/Users/jim/.local/share/stdo-qualification/v3.0.5/local-001/runtime/a_c/build_tenants/graphify/code')
import ac_support_core as core
p=Path('/Users/jim/.local/share/stdo-qualification/v3.0.5/local-001/hosts/codex/cases/readonly-initializer/policy.json')
core.Runtime.from_policy(p,hashlib.sha256(p.read_bytes()).hexdigest(),"executive")
