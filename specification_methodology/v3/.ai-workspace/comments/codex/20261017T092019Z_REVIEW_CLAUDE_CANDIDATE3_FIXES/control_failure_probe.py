"""Bounded failure propagation probe of frozen qualification code.

Run: python -B control_failure_probe.py /path/to/specification_methodology
No candidate script is run in a tenant. Only the exact reporting tail and
wrapper tail run in an automatically removed scratch directory. This supplies
a failed-control input and a failing subprocess; it does not claim the stored
candidate controls actually failed.
"""
import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from types import SimpleNamespace

repo = Path(sys.argv[1]).resolve()
candidate = "9e901690e9f9b66917cafd917fff9ad755efa2a6"
prefix = "specification_methodology/v3/build_tenants/claude/qualification/C3-ITER4/tools/"


def source(name):
    return subprocess.check_output(["git", "-C", str(repo), "show",
                                    candidate + ":" + prefix + name], text=True)


controls = source("ac_controls.py")
wrapper = source("freeze_ac.sh")
assert controls.count("rec['elapsed_seconds'] =") == 1
tail = controls[controls.index("rec['elapsed_seconds'] ="):]
wrapper_lines = wrapper.splitlines()
start = next(i for i, line in enumerate(wrapper_lines)
             if line.startswith("python3 -I qualification/C3-ITER4/tools/ac_controls.py"))
wrapper_tail = "\n".join(wrapper_lines[start:])
shell_options = "\n".join(line for line in wrapper_lines if line.startswith("set "))

with tempfile.TemporaryDirectory(prefix="claude-control-failure-") as tmp:
    root = Path(tmp).resolve()
    report = root / "failed-control.json"
    namespace = {
        "rec": {"controls": [{"control": "reviewer-supplied-failed-control",
                               "holds": False, "detail": "false input to reporting tail"}]},
        "time": time, "t0": time.time(), "json": json,
        "sys": SimpleNamespace(argv=["ac_controls.py", str(root), str(report)]),
    }
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout):
        exec(compile(tail, prefix + "ac_controls.py:reporting-tail", "exec"), namespace)
    record = json.loads(report.read_text())
    assert record["holds_all"] is False
    # A normal return from the script's final statements means successful exit.
    harness = shell_options + "\nSP=" + str(root) + "\n" + '''python3() {
      case "$*" in
        *ac_controls.py*) printf '%s\\n' 'simulated control subprocess failure' >&2; return 7 ;;
        *consumers.py*) printf '%s\\n' 'subsequent consumers command reached'; return 0 ;;
        *) return 99 ;;
      esac
    }
    ''' + wrapper_tail + "\n"
    result = subprocess.run(["/bin/bash", "-c", harness], cwd=root,
                            text=True, capture_output=True)
    assert result.returncode == 0 and "subsequent consumers" in result.stdout
    print(json.dumps({
        "candidate": candidate,
        "scope": "exact final reporting statements and exact final wrapper commands; supplied adverse outcomes",
        "failed_control_record": record["holds_all"],
        "reporting_tail": "returns normally despite failed control",
        "reporting_stdout": stdout.getvalue().strip(),
        "simulated_control_subprocess_exit": 7,
        "wrapper_tail_exit": result.returncode,
        "wrapper_stdout": result.stdout.strip(),
        "wrapper_stderr": result.stderr.strip(),
        "limits": "Does not refute the stored all-hold result or execute the full checker/control suite",
    }, indent=2))
