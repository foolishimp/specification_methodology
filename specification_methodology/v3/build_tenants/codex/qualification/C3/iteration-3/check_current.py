"""Apply the existing artifact checker to this iteration's explicit inputs."""
import sys
from refresh_current import HERE, PREVIOUS, load_module

checker = load_module("i3_artifacts", PREVIOUS / "synthesis/check_artifacts.py")
checker.HERE = HERE
checker.SUPPORT = HERE
if "--idempotence" in sys.argv:
    raise SystemExit("Use refresh_current.py in an isolated tenant copy for a regeneration experiment.")
raise SystemExit(checker.main())
