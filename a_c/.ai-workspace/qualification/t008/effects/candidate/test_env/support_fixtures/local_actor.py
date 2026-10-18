"""Fixed regular-file process fixture; no model/provider/network calls."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import signal
import subprocess
import sys
import time


def main() -> int:
    mode = sys.argv[1]
    if mode == "hold":
        time.sleep(0.8)
        return 0
    raw = sys.stdin.buffer.read()
    target = Path(sys.argv[2])
    if mode == "count":
        count = int(target.read_text()) if target.exists() else 0
        target.write_text(str(count + 1))
    elif mode in ("partial", "ignore-term", "fail"):
        target.write_text("partial-effect")
        print("partial-output", flush=True)
        if mode == "ignore-term":
            signal.signal(signal.SIGTERM, signal.SIG_IGN)
        if mode == "fail":
            return 3
        time.sleep(2)
    elif mode == "descendant":
        subprocess.Popen([sys.executable, __file__, "hold"])
    print(json.dumps({"fixture": mode, "stdin_sha256": hashlib.sha256(raw).hexdigest()}), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
