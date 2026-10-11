# Claude Tenant Returns

Tenant-local return record. Under the rule that each tenant writes only inside
its own build tenant, returns after 2026-10-11T07:00Z are recorded here. The
ticket `stdo_3/.ai-workspace/tickets/backlog/T-001-CLAUDE-principles.md`
carries the earlier returns (initial author, first successor, Codex
cross-review disposition) and is not updated by this tenant; the common pen
may mirror this record there.

Builder basis for every entry: `stdo://releases/v2.5.1-rc.2/`, manifest
SHA-256 `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
Common inputs: snapshot `C1-inputs-20261011-02`, 16 members.

## Candidate lineage

| Candidate | SHA-256 | Lines / words | Frozen | Standing |
|---|---|---|---|---|
| Initial | `329fe4228eb9d6e2a5f79bf597fa25a82d6a798a30146a93dd5773678c73d0bb` | 400 / 4,402 | 2026-10-11T05:58:13Z | superseded; Codex review `CHANGES REQUIRED` |
| First successor | `454770386c4cbe7c8aa2269afeafa3084a26ed0960774fae25e577a407f900a2` | 454 / 4,941 | 2026-10-11T06:48:18Z | superseded; two review items still open |
| Second successor | `28c9b1275ca23c53d80cf64afa45acf0d25ce8aa7daddd62b5c7aaf490b2b7ec` | 484 / 5,214 | 2026-10-11T07:48:06Z | current; not independently reviewed |

Each predecessor's bytes are retained in the activation scratchpad; the
repository holds only the current candidate at
`stdo_3/build_tenants/claude/design/PRINCIPLES.md`.

## Second successor return, 2026-10-11T07:48:06Z

Activation: Claude Writer, own tenant only, authorised by Jim ("go") after
the Codex posted review
`stdo_3/build_tenants/codex/reviews/20261011T072147Z_REVIEW_claude_c1_principles.md`
(SHA-256 `189aa62232dbbd7c530e05d4194523cbe05f3bf25e433eb7c8302fc4ddeb90af`,
92 lines), which binds the initial candidate `329fe422…d0bb`.

Disposition of that review's four findings against the first successor:

| Finding | State in first successor | Action here |
|---|---|---|
| 1. Cost fields as universal ritual | already applied (selected-by-claim) | none |
| 2. "Never semantically decidable" | already applied (AC-019 decision contract) | none |
| 3a. Contradictions against retired `-01` text | already applied (withdrawn) | none |
| 3b. ABG handoff and post-mortems described as tuple members | open | restated: the 504.8 MB figure and the post-mortem lessons are attributed to the Claude plan post and the two plan posts in the tuple, as indirectly reported historical observations; primary sources deferred to C2 and not reacquired |
| 4a. Sole-output premise | already applied (Pr2a, step-produced facts) | none |
| 4b. P1 and P6 independence asserted, not argued | open | non-entailment arguments added: P1 (vary only the interpretation contract with purpose, identity, evidence and authority fixed; RF-008 states the law); P6 (a finite actor satisfying C and P1–P5 can still accept a green label as acceptance or treat capability as permission; UP-022 and RF-006 are the separate commitments that forbid it) |

Changes to the candidate: header status and lineage; one paragraph after P1;
P6's standing paragraph; gap 3 attribution; the mechanisms paragraph's
attribution; one lineage bullet in the residuals. No other section changed.

Verification at freeze: 93 links resolve, 90 `stdo://` fragment-link
occurrences to 65 unique installed headings; no trailing whitespace; zero
occurrences of the stale "in the tuple" attributions; snapshot 16/16
unchanged at start (07:47:26Z) and at freeze. Bytes changed by this
activation: the candidate and this file only.

Resource observation: start 2026-10-11T07:47:26Z, end 07:48:06Z, 40 seconds
wall by `date -u`; generated-token counters unavailable on this host against
the 60,000 planning allowance.

Work result: `candidate_ready` / `satisfied` for the declared output. No
acceptance claimed. Independent review of this successor is Jim's to
authorise.

## Cross-review of the Codex tenant, 2026-10-11T06:53:37Z

Performed under the earlier grant, before the tenant-only rule. Closed result
and findings:
`stdo_3/build_tenants/codex/qualification/C1_REVIEW.md` (SHA-256
`40700da54763fdeac4103c2f3c0530e2266070ce6bcb57cd2c3a8d3eab9ba8be`), posted
verbatim in this tenant at
`../reviews/20261011T065337Z_REVIEW_codex_c1_principles.md` (SHA-256
`351e8e86f7927431f0475d02f34da2564a474fbba7702287ef764b027dcf46ef`). Subject
`52fbd93ad31476823d5bed7a991ee85b5d8e8e188037fcdb80ac052540051611`. Result:
`satisfied` on derivations, hypotheses, mechanisms, boundaries, prose and cost
reporting; `falsified` on source-recovery completeness for seven items;
recommended `local_repair`. 4 minutes 43 seconds wall.
