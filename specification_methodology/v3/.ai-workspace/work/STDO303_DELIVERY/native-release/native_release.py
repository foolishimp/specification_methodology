#!/usr/bin/env python3
"""Compatibility entry for the registered STDO 3.0.3 native release tool."""
from pathlib import Path
import json
import sys

_target = Path(__file__).resolve().parents[4] / "build_tenants/common-tools/native_release.py"
try:
    _source = _target.read_bytes()
except OSError as _error:
    print(json.dumps({"status": "refused", "reason": str(_error)}), file=sys.stderr)
    raise SystemExit(2)
__file__ = str(_target)
exec(compile(_source, __file__, "exec"), globals())
