```json
{
  "edits": [
    {
      "path": "deploy/env.example",
      "content": "APP_API_TOKEN=changeme\nAPP_TOKEN_TTL=3600\nLOG_LEVEL=info\n"
    },
    {
      "path": "src/settings.py",
      "content": "import os\n\nTOKEN = os.environ['APP_API_TOKEN']\nTOKEN_TTL = int(os.environ.get('APP_TOKEN_TTL', '3600'))\n"
    },
    {
      "path": "scripts/check_env.sh",
      "content": "#!/bin/sh\n: \"${APP_API_TOKEN:?missing}\"\necho ok\n"
    },
    {
      "path": "docs/config.md",
      "content": "# Configuration\n| Variable | Meaning |\n|---|---|\n| APP_API_TOKEN | API token |\n| APP_TOKEN_TTL | Token lifetime in seconds |\n| LOG_LEVEL | Log verbosity |\n"
    }
  ],
  "report": "Observations (acquired only from the supplied workspace snapshot, per FOUNDATIONS 'Workspace and context'): the exact identifier APP_TOKEN appears in four files. It is the line `APP_TOKEN=changeme` in deploy/env.example, `os.environ['APP_TOKEN']` in src/settings.py, `${APP_TOKEN:?missing}` in scripts/check_env.sh, and a table row in docs/config.md. A distinct variable, APP_TOKEN_TTL, shares the prefix and appears in env.example, settings.py and docs/config.md. The task scopes the rename to APP_TOKEN only, so APP_TOKEN_TTL is intentionally unchanged in all three files. Renaming it would change a second contract that the task did not grant.\n\nWork: I renamed APP_TOKEN to APP_API_TOKEN in deploy/env.example as requested. I also updated every in-workspace dependent on that name (settings.py, check_env.sh, docs/config.md) so that the rename does not break the reader. Without the settings.py change, the KeyError would occur at import time. Without the check_env.sh change, the script would fail with 'missing'. All other bytes are preserved.\n\nNon-changes: APP_TOKEN_TTL, LOG_LEVEL, the Python constant name TOKEN, and the script logic are unchanged. I added no backward-compatibility fallback to APP_TOKEN. That would keep the old name live and widen the requested change. It is a product choice that remains with the owner.\n\nLimits (RF-006 and the result algebra; no execution tools): I ran nothing and observed no applied effect. These are proposals only. Whether the host's write preserves the executable bit on scripts/check_env.sh is unobserved.\n\nUnresolved (FOUNDATIONS 'Workspace and context': absence from a partial projection is not evidence of absence): dependents outside this workspace are unobserved. Examples include real .env files, CI variables, secret stores, container or orchestration manifests, and running deployments that set APP_TOKEN. Any such environment must start setting APP_API_TOKEN, or the owner must choose a transitional fallback. Otherwise settings.py and check_env.sh will fail there. For this reason, 'everything that depends on the name keeps working' stays indeterminate beyond the workspace boundary.",
  "results": [
    {
      "predicate": "deploy/env.example declares APP_API_TOKEN in place of APP_TOKEN, with APP_TOKEN_TTL and LOG_LEVEL unchanged",
      "subject": "proposed replacement content for deploy/env.example",
      "basis": "task statement + supplied workspace snapshot",
      "verdict": "satisfied",
      "performance": "performed",
      "evidence": "static comparison of the proposed content against the snapshot",
      "effect": {"state": "unknown", "boundary": "sandbox file write by host; not observed by this actor"},
      "unresolved": []
    },
    {
      "predicate": "every in-workspace reference to the exact variable APP_TOKEN is updated to APP_API_TOKEN, and no reference to APP_TOKEN_TTL is altered",
      "subject": "proposed contents of src/settings.py, scripts/check_env.sh, docs/config.md, deploy/env.example",
      "basis": "supplied workspace snapshot (4 files)",
      "verdict": "satisfied",
      "performance": "performed",
      "evidence": "manual exact-token inspection of all four supplied files; the only exact references were the four lines changed",
      "effect": {"state": "unknown", "boundary": "sandbox file writes by host; not observed by this actor"},
      "unresolved": []
    },
    {
      "predicate": "everything that depends on the variable name keeps working after the rename",
      "subject": "workspace plus any external deployment environments",
      "basis": "supplied snapshot only; external environments not supplied",
      "verdict": "indeterminate",
      "performance": "not_performed",
      "evidence": "no execution of settings.py or check_env.sh was possible. In-workspace consumers were statically updated, but external environment sources that set APP_TOKEN are unobserved",
      "effect": {"state": "not_requested", "boundary": "no runtime or external effect performed by this actor"},
      "unresolved": [
        "external env and secret configurations must provide APP_API_TOKEN, or the owner must decide on a transitional APP_TOKEN fallback",
        "runtime execution of settings.py and check_env.sh under the new variable has not been run",
        "executable bit on scripts/check_env.sh after the host write"
      ]
    }
  ]
}
```
