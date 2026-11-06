from pathlib import Path
import sys
Path('/Users/jim/src/apps/specification_methodology/specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/tools-skills/boundary-regression-010/after/fixtures/test_external_bootstrap_invokes_only_marker_and_retains_its_deliberate_failure/outside/bootstrap-invoked.marker').write_text("selected fixture bootstrap invoked\n")
print("marker-only fixture; no Lean or downloads")
raise SystemExit(23)
