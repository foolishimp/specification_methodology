# Pending actual cross-family review plans

This directory prepares two real host reviewers without dispatching them or modifying selected construction inputs. Exact candidate inventories are still required. `prepare_review.py` reuses the existing native policy, owner and actor adapter; it does not implement a new admission or review engine.

Root supplies a frozen selection JSON per reviewer with `backend` (`claude` or `codex`), `subject` (Identity), `candidate` (SourceRef), `candidate_sources` (complete selected ReviewClaim population), `governing_sources`, `proof_sources`, `component_claims` and `authors`. SourceRefs use existing `product`, `tool`, `method`, `operator`, `successor` aliases. Each whole-parent hash is verified. Candidate selectors may narrow the declared finite review population but cannot silently stand for uninspected whole-file or whole-system qualification. The common/tool and tenant claims retain their separate component conclusions.

Prepare the expectation phase with the selected file and its SHA256. Only after the actual Reviewer has returned its recorded expectation, prepare `candidate` with `--expectation <actual-artifact-sha256>`. Both use the same declared Reviewer actor identity and the same frozen selection. The script writes create-only plans, policies, contracts and packets under this directory. Optional `--preflight` executes actual public observation/context/preflight operations. It never dispatches a host. Root selects each later launch.

Root revised the draft envelope before review admission: the expectation phase is limited to 300 seconds and the candidate phase to 900 seconds, aggregate 1200 seconds per Reviewer. No automatic retries, inherited model settings, 4MiB output per phase, cost unknown. Public CLI is the normal route; no MCP approval dependency. Claude uses the existing selected credential passthrough by name only.

`CONSTRUCTION-BASIS-ISSUE.md` records why the earlier construction return can be currentness-invalidated by its intended writes. These review plans bind stable files only and do not alter or rehabilitate the original results. `OPEN.json` states the remaining selection/preflight work.
