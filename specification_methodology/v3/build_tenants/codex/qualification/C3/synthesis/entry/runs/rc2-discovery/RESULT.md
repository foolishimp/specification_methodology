```json
{
  "edits": [],
  "report": "Stopped before making changes. I followed the rc.2 stdo-work skill (installed/plugins/spec/skills/stdo-work/SKILL.md). It requires PRODUCT_BASIS.md to pick exactly one Product definition that covers the requested work before any change is drafted. The task's subject is workspace/ (deploy/env.example, src/settings.py, scripts/check_env.sh, docs/config.md). The only definition found under the temporary root is source/specification_methodology/v3/stdo_3.json (urn:stdo:product-definition:stdo-3). That definition does not name workspace/ or this task anywhere in its source_project, bounded context, what, how, ticketing or composition sections. No other definition exists. So zero definitions cover the task, and PRODUCT_BASIS step 4 and its closing rule say to report the unresolved scope and stop. ACTIVATION.md selects the task and allows read-only inspection and edit proposals, but under PRODUCT_BASIS a Product definition can't be replaced by a path or an outside selection. ACTIVATION.md also says to report the exact stop instead of inventing missing grants. So I'm proposing no edits. If a covering definition and an approved work contract are supplied, the rename would need to change these 4 lines in 4 files: deploy/env.example:1, src/settings.py:3 (os.environ['APP_TOKEN'] would raise KeyError without it), scripts/check_env.sh:2 (would exit with 'missing' without it) and docs/config.md:4. APP_TOKEN_TTL is a separate variable and should stay unchanged unless the owner decides otherwise. Any environment that still sets the old name will break unless it's updated or a fallback is kept; only the owner can make that call. I didn't apply any changes or run any tests or checks.",
  "results": {
    "method": "baseline",
    "entry": "installed/plugins/spec/skills/stdo-work/SKILL.md (installed v2.5.1-rc.2 copy, unmodified)",
    "product_basis_selection": {
      "requested_product_scope": "Unresolved: the disposable D1 qualification task subject workspace/ (deploy/env.example and its dependents). No Product-owned identity or claim in the request names a Product.",
      "candidates_discovered": [
        {
          "path": "source/specification_methodology/v3/stdo_3.json",
          "definition_id": "urn:stdo:product-definition:stdo-3",
          "bounded_context": "urn:stdo-3:bounded-context:method",
          "applicable": false,
          "reason": "source_project './' resolves to source/specification_methodology/v3/. Its what, how (build_tenants codex/claude), ticketing and composition (axiom-indexer) sections bind only that project's paths. Nothing binds workspace/ or this task. A grep of its specification/ folder for the task markers (workspace/, EC-CODEX, disposable, D1, qualification task) found no binding."
        }
      ],
      "applicable_count": 0,
      "verification": "Not reached for an applicable definition. As supplied facts only: the stdo-3 receipt (controls/VERIFIED_BASIS.json and controls/BUILDER_STATUS.json) reports basis stdo://releases/v2.5.1-rc.2/, manifest 3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782, installed true, valid true and no failures. It names the original definition path, not the exported copy. controls/EXPORT.json says the export is byte-identical and gives its sha256. I did not compute that hash myself. This would not have made stdo-3 applicable to workspace/ anyway.",
      "outcome": "STOP: zero applicable Product definitions (PRODUCT_BASIS step 4 and its closing rule)."
    },
    "observed_stop": {
      "stage": "Select The Product Basis (comes before classification, the work basis, contract approval and construction)",
      "rule": "PRODUCT_BASIS.md: 'For zero applicable definitions, return the unresolved scope' and 'Zero definitions ... stops the calling skill before effects.'",
      "not_reached": [
        "classification and computation of the affected owner and route",
        "establishing upstream work authority and selecting a work record",
        "drafting and approving an execution contract (no ticket, sprint, admission mechanism or result surface is bound to workspace/)",
        "construction and proof"
      ],
      "not_substituted": "ACTIVATION.md selects the task and grants proposal permission. It is not a Product definition and not a contract approval, and PRODUCT_BASIS says a path or an outside selection cannot replace either."
    },
    "required_re_entry": "The Product owner or Executive must supply a Product definition that explicitly covers workspace/, or explicitly add workspace/ to an existing definition, along with the upstream work authority and an approved execution contract. Then re-run stdo-work.",
    "information_not_a_proposal": {
      "dependents_of_APP_TOKEN": [
        "deploy/env.example:1 (the definition being renamed)",
        "src/settings.py:3 os.environ['APP_TOKEN'] (required; raises KeyError if unset)",
        "scripts/check_env.sh:2 ${APP_TOKEN:?missing} (required; exits non-zero if unset)",
        "docs/config.md:4 (documentation row)"
      ],
      "non_dependents": "APP_TOKEN_TTL (deploy/env.example:2, src/settings.py:4, docs/config.md:5) is a separate variable that only shares the APP_TOKEN prefix. LOG_LEVEL is unaffected.",
      "open_owner_question": "Should deployments that still set APP_TOKEN keep working through a fallback, or switch over in one step? This is an owner decision and was not made here."
    },
    "checks_performed": "Read-only file reads, globs and greps only. No tests run, no hashes computed, no stdo status run, no edits applied.",
    "closure": "Withheld: no work result was produced."
  }
}
```
