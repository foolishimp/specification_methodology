I found every reference to the name. Here is the JSON result:

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
  "report": "Proposed renaming APP_TOKEN to APP_API_TOKEN in deploy/env.example and in everything that uses the exact name: src/settings.py (required os.environ lookup), scripts/check_env.sh (the ${...:?missing} guard) and docs/config.md (the variables table). APP_TOKEN_TTL is a separate variable that only shares the prefix, so it stays as it is in all four files. I didn't add a fallback to the old APP_TOKEN name: nothing in the workspace or the task asks for one, and keeping it would add a mechanism with no stated purpose or removal plan. That means any external environment still setting only APP_TOKEN will now fail at settings import and in check_env.sh. That is the intended effect of the rename, but the owner should know about it. Nothing was applied or run. Only Read, Glob and Grep were available, so these are proposals only.",
  "results": {
    "method": "baseline",
    "entry": "installed/plugins/spec/skills/stdo-work/SKILL.md (rc.2 ordinary entry, read unmodified)",
    "product_basis": {
      "requested_scope": "Disposable D1 fixture: TASK.md is the WHAT, workspace/ is the HOW",
      "definition_id": "urn:stdo:qualification-fixture:entry-d1",
      "definition_path": "/private/tmp/stdo-bound-rc2-jifw4sir/stdo_fixture.json",
      "basis": "stdo://releases/v2.5.1-rc.2/",
      "manifest_sha256": "3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782",
      "verification": "Used the supplied verified receipt (controls/VERIFIED_BASIS.json, receipt_sha256 2f36ad08…): installed true, valid true, failures []. Its definition id, path, basis and manifest match stdo_fixture.json. I did not run `stdo status --verify` myself and did not recompute definition_sha256, because only read tools were available."
    },
    "work_authority_and_carrier": {
      "upstream_authority": "EXECUTION_CONTRACT.md grant (EC-CODEX-SYN-01 bounded entry-harness activation). The contract states that the existing grant and task are sufficient upstream work authority.",
      "carrier": "Run-scoped: this return plus the host's application or rejection record. The contract adopts no ticket or sprint, and stdo-ticket was not invoked.",
      "admission": "Cited the existing admitted grant (EXECUTION_CONTRACT.md) instead of asking for new approval. No other admission mechanism was run.",
      "change_intent": "Rename the environment variable APP_TOKEN to APP_API_TOKEN without breaking anything that uses the name",
      "change_class_reentry": "Realization change. TASK.md is the requirement and is unchanged. DESIGN.md says the fixture declares no interface policy or solution design, so it is unaffected.",
      "write_territory": "workspace/ only",
      "target_truth": "The exact variable APP_TOKEN is called APP_API_TOKEN in the example env, the code that reads it, the startup check script and the docs",
      "superseded_truth": "The exact variable name APP_TOKEN"
    },
    "classification_evidence": {
      "tool": "Grep for 'APP_TOKEN|APP_API' across workspace/",
      "affected_relations": [
        "deploy/env.example:1 (defines the name)",
        "src/settings.py:3 (required read via os.environ[...])",
        "scripts/check_env.sh:2 (required-variable guard)",
        "docs/config.md:4 (documentation)"
      ],
      "excluded_prefix_matches": [
        "APP_TOKEN_TTL in env.example:2, settings.py:4, config.md:5: a different variable, not renamed"
      ],
      "unknowns": "Deployments outside the workspace that may still set APP_TOKEN cannot be seen. I added no fallback because no requirement asks for one."
    },
    "proof": {
      "performed": "A static re-read of the proposed contents: every exact APP_TOKEN reference has been changed, every APP_TOKEN_TTL reference is unchanged, and nothing else in the files changed.",
      "not_performed": "Did not run check_env.sh, did not import settings.py, and ran no tests. Nothing is executable with the available tools."
    },
    "non_changes": [
      "APP_TOKEN_TTL and LOG_LEVEL are unchanged",
      "No files outside workspace/ were changed",
      "No ticket was created"
    ],
    "residuals": [
      "Environments outside the workspace that set only APP_TOKEN must switch to APP_API_TOKEN",
      "The host still has to validate and apply these proposals"
    ],
    "closure": "Withheld. This is a candidate only. Applying it and evaluating it against the oracle is up to the host."
  }
}
```
