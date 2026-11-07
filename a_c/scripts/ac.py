#!/usr/bin/env python3
"""Portable a_c 3.0.5-rc.1 command router; each tenant owns its command contract."""
from pathlib import Path
import os
import sys

ROOT = Path(__file__).resolve().parents[1]
COMMANDS = {
    'graph': 'build_tenants/graphify/code/ac_graph.py',
    'upstream': 'build_tenants/graphify/code/ac_upstream.py',
    'project': 'build_tenants/graphify/code/ac_project.py',
    'code': 'build_tenants/graphify/code/ac_code.py',
    'support': 'build_tenants/graphify/code/ac_support.py',
    'formal': 'build_tenants/lean/scripts/formal_gate.py',
    'formal-select': 'build_tenants/graphify/code/ac_formal_gate.py',
    'bootstrap': 'scripts/bootstrap.py',
}
if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
    print('a_c 3.0.5-rc.1: ' + ', '.join(COMMANDS))
    print('Usage: python3 /path/to/a_c/scripts/ac.py COMMAND [tenant arguments]')
    raise SystemExit(0)
if sys.argv[1] == '--version':
    print('3.0.5-rc.1')
    raise SystemExit(0)
entry = COMMANDS.get(sys.argv[1])
if entry is None:
    raise SystemExit('Unknown a_c command: ' + sys.argv[1])
os.execv(sys.executable, [sys.executable, '-B', str(ROOT / entry), *sys.argv[2:]])
