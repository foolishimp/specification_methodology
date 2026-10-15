# Reproduce The Bounded Mechanical Review

The retained JSON files record the original runs. Replaying the Python probes requires this repository's named Git objects and the installed STDO 2.5.1-rc.2 at the paths declared in the scripts. They verify the checker and theory pins before use. Semantic findings are supported by the exact source excerpts in the adjacent review evidence, not by these mechanical checks.

The scripts expect frozen extracts under `/tmp/stdo-i4-review-20261015T160637Z`. If those inputs have been removed, restore them from the main checkout with this command. It refuses to overwrite an existing review directory. It creates no worktree or branch and writes only temporary files.

```sh
python3 - <<'PY'
from pathlib import Path
import subprocess

repo = Path('/Users/jim/src/apps/specification_methodology')
base = Path('/tmp/stdo-i4-review-20261015T160637Z')
base.mkdir()
prefix = 'specification_methodology/v3/build_tenants/'
subjects = {
    'claude': ('8a0ea226e8662695f8c0a79e56be7416a21549b0',
               ['standards', 'a_c']),
    'codex': ('62318d3b0be35985a0397aa39daee0ec8836eabc',
              ['successor', 'a_c']),
}
for tenant, (commit, members) in subjects.items():
    destination = base / tenant
    destination.mkdir()
    paths = [prefix + tenant + '/' + member for member in members]
    archive = subprocess.Popen(['git', 'archive', commit, *paths],
                               cwd=repo, stdout=subprocess.PIPE)
    result = subprocess.run(['tar', '-xf', '-', '-C', str(destination)],
                            stdin=archive.stdout)
    archive.stdout.close()
    assert archive.wait() == 0 and result.returncode == 0
PY
```

Then run these commands from this assets directory, in order:

```sh
python3 -B interpretation-review-reproduce.py
python3 -B interpretation-review-claude-map-probe.py
python3 -B interpretation-review-static-probes.py
```

Runtime outputs go to the temporary review directory. The first script records expected failing Claude projections as well as passing checks; a successful script exit does not mean every candidate command passed. The map probe isolates stale published artifacts by generating only a temporary map. The static probe copies the Codex package to another temporary directory, verifies its binding, changes a source file in that copy, and checks refusal. No candidate source or installed dependency is modified.

Projection sizes are emitted JSON bytes. They are not active model context, application memory, complete task acquisition, semantic fidelity or comparative task performance. Native wall timings are diagnostic observations only; semantic coverage differs between candidates.
