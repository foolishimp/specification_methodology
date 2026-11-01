#!/usr/bin/env python3
"""Compatibility entry for the registered common package checker."""
from pathlib import Path
import hashlib
import json
import sys

_target = Path(__file__).resolve().parents[3] / "build_tenants/common-tools/package_tools.py"
try:
    _source = _target.read_bytes()
    if hashlib.sha256(_source).hexdigest() != "30b70f6e7771535cf50b37e56a51bb595b477364b6c1112acf044c7b76e4ceac":
        raise ValueError("registered package checker differs from compatibility selection")
except (OSError, ValueError) as _error:
    print(json.dumps({"valid": False, "error": str(_error)}))
    raise SystemExit(2)
# The authenticated wrapper pin covers this fixed dependency pin. The canonical
# file remains directly runnable with the original single-file trust contract.
__file__ = str(_target)
exec(compile(_source, __file__, "exec"), globals())
