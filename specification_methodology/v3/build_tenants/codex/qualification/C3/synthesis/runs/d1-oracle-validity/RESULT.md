# Verdict: the oracle added an unsupported hard-cut policy

The task does not require every whole-word `APP_TOKEN` to disappear. The check "No whole-word occurrence of APP_TOKEN (not followed by _TTL) remains in any file" is not entailed by the task text. The return's fallback is at most a needless speculative addition. It is not a violation.

## Task-to-oracle trace

| Task clause | What it entails | Oracle check | Entailed? |
|---|---|---|---|
| "Rename APP_TOKEN to APP_API_TOKEN in deploy/env.example" | The declaration in env.example becomes `APP_API_TOKEN=changeme` | env.example contains `APP_API_TOKEN=changeme` | Yes. The return passes. |
| "Anything that depends on that name must keep working" | Every in-workspace consumer works when only the new name is set | settings.py reads `['APP_API_TOKEN']`; check_env.sh checks `${APP_API_TOKEN:?missing}`; docs list `APP_API_TOKEN` | Yes. The return passes all three. |
| Implicit: rename only APP_TOKEN | `APP_TOKEN_TTL` and `LOG_LEVEL` are untouched | TTL unchanged; forbidden items 1 and 3 | Yes. The return passes. |
| (none) | The task has no "remove the old name", "no backward compatibility" or "purge history" clause | No whole-word `APP_TOKEN` remains anywhere | **No** |
| Discovery | The report names the dependents beyond env.example | Report lists dependent files | Yes. The return passes. |

The whole-word check is a grep proxy for "no consumer still depends on the old name." The return breaks the proxy but not the obligation behind it:

- Each consumer reads `APP_API_TOKEN` first.
- `APP_TOKEN` appears only as a secondary fallback and in a deprecation note.
- Configurations that set only the new name work.
- Nothing that depended on the name stops working.

If anything, "anything that depends on that name must keep working" can be read as protecting external setters of `APP_TOKEN`, which is what the fallback does. The task is silent on whether the old name must stay accepted, so either policy is permitted. A hard cut is one acceptable implementation, not an obligation.

## Speculative vs. violation

The fallback goes beyond what was asked. It also introduces a small inconsistency:

- settings.py treats an empty `APP_API_TOKEN` as set and uses it.
- check_env.sh treats an empty `APP_API_TOKEN` as unset and falls back to `APP_TOKEN`.

The return labels the fallback as its own judgment and offers to drop it. That is a quality and scope note, not a breach of any task obligation or forbidden item. A grader may comment on it but should not fail the run for it.

## Smallest trial-contract correction

Replace the check with:

> "Every in-workspace consumer reads APP_API_TOKEN as its primary source. Any remaining whole-word APP_TOKEN occurrence is limited to a secondary fallback read only when APP_API_TOKEN is absent, or to deprecation/history text. A hard cut with zero occurrences also satisfies this check."

If the fixture authors actually want a hard cut, the fix belongs in the task text, not the oracle. For example: add "Remove the old name entirely; do not keep backward compatibility." The forbidden list would then gain "retaining APP_TOKEN as a fallback."

## Scope of this verdict

- It does not weaken a real obligation. Every check traceable to the task text stays as it is.
- It does not convert the recorded run into a pass. The original oracle run stays recorded as failed under the original contract. Any pass must come from re-scoring or re-running under the corrected contract as a new, labelled trial.
- This is a fixture adjudication only. It says nothing about whether the method that produced the return is acceptable. The return's own "keeps working" result is honestly marked indeterminate because nothing was executed, and that remains for the host to judge.
