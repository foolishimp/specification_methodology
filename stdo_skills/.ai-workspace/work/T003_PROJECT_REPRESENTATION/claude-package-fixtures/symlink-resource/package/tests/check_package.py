#!/usr/bin/env python3
"""Read-only wrapper for the delivered Claude bundle validator."""
import importlib.util
import json
from pathlib import Path
import sys

PACKAGE = Path(__file__).resolve().parents[1]
path = PACKAGE / "skills/stdo-release-install/scripts/manage_install.py"
spec = importlib.util.spec_from_file_location("claude_bundle_integrity", path)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
errors = module.validate_package(PACKAGE)
print(json.dumps({"status": "refused" if errors else "ok", "errors": errors}, indent=2))
raise SystemExit(1 if errors else 0)
