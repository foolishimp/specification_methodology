# Claude candidate 3: affected repair review

**Verdict: targeted changes required.** Most original defects are repaired.
Two material issues remain: ODD drops a newly performed selection judgment
after a prior closure, and the offered interpretation-freeze command can
exit successfully after failed controls. Two Low corrections concern a
missing family import and a stale scope count. No architectural rewrite or
whole-suite rerun is warranted by these findings.

The subject is candidate A `9e901690e9f9b66917cafd917fff9ad755efa2a6`, with
manifest and final records at B `7b40bdb65056967efa8cdcc682ab33af9ded32a2`.
The manifest SHA-256 is
`ec928980f6aafec5d40d384f5958160464eda74d03bfb61ccd1f6401cc552316`.
The common WHAT is ratified C3-I5-06 at
`4c340f7adec9f3c893e3e267b23e4cadeb357854`. Paths and line numbers below
are relative to `specification_methodology/v3/build_tenants/claude/` at A
unless B is named. The builder is verified installed v2.5.1-rc.2, manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.

## Remaining findings

**C3-01 — Medium: prior closure suppresses a different, current judgment.**
`standards/ODD.md:1024–1030` recognizes no-action as a material determination,
but says it adds no core result after `post_retry`, `post_repair`,
`post_reenter`, `post_block` or `post_reprice`. The preceding closure's
predicate is whether the attempted edge's obligations were fulfilled
(`:1118–1124`). Current selection asks whether a published lawful action can
be selected for the current gap. The former cannot stand in for the latter.

Concrete case: an attempted edge returns `retry(defeated)` with `falsified`.
Fresh gap observation then shows the previous action is no longer lawful,
no other lawful published action is available, and recovery needs an
unpublished capability. That new refusal needs `out_of_frame` for its
selection predicate. A4 suppresses it solely because the earlier closure
exists. A3 and A4 admit this case; it is not an invented new outcome.
`ACTIVATION.md:945–954` requires a predicate-bound result for each performed
evaluation. The original initial-selection case is fixed, but the
post-closure case is still inconsistent with that owner.

Repair the exemption at A4 and its consumers: the function row at `:865`,
family row at `:130`, and stale disposition summary at `:1859`. A previous
result may be reused only if it supports this same determination on the
current basis. Keep ordinary selection data separate from judgments. Check
initial refusal, a new post-closure refusal, and completed work with no next
action. The defect loses a material result; it does not demonstrate an
unauthorized effect. Full argument: [core review](CORE_REVIEW.md).

**C3-02 — Medium: the verification command does not reliably propagate
failed controls.** `qualification/C3-ITER4/tools/ac_controls.py:67–70`
records `holds_all: false` and prints failure, but returns normally.
`qualification/C3-ITER4/tools/freeze_ac.sh:5,24–25` also pipes the control
process through `tail` under `set -e` without `pipefail`; even a nonzero
control-process exit can be hidden, after which the consumers command runs
and the wrapper exits zero.

The [independent probe](control_failure_probe.py) executes the frozen
reporting tail with a supplied failed control, and the frozen wrapper tail
with a control process returning 7. The former returns normally; the
latter continues and exits 0. [Receipt](CONTROL_FAILURE_PROBE.json).
The successful unchanged-output rerun repair is real, but successful command
completion alone is still not a trustworthy control verdict. Propagate a
failed control or subprocess as failure, or make the freeze command
explicitly inspect the control report before returning success. Verify one
adverse case through the complete wrapper after repair.

This is a defect in the offered verification route, not evidence that the
stored controls failed. The frozen `returns/ac_controls.json` does record
all seven controls as holding. This review did not independently rerun that
whole suite or adopt its result as semantic proof.

**C3-03 — Low: the Design family omits a required dependency.**
`standards/DESIGN_MODULE.md:160–181,217` now correctly consumes generic
ticket recurrence policy, but omits F13 from the imported-family declaration
and recurrence row's premises. `PROFILES.md:31–43` expressly requires that
family ID and its argument-table section. Add the import; retain the
existing policy outcome. The choice column already links the policy owner,
so this is incomplete dependency accounting, not a demonstrated wrong
recurrence decision. [Policy review](POLICY_REVIEW.md).

**C3-04 — Low: four named scopes above five actual scopes.**
`a_c/i3/README.md:56` says “four task scopes”; its table at `:62–66` and the
program contain five. Correct the word. No checker rerun is needed for it.

## Disposition of the original review

| Finding | Current conclusion |
|---|---|
| R1, absent installed bootstrap inputs | Repaired. The declared set now includes the schema and template. Independent materialization verifies their hashes, a filled template validates against the packaged schema, and its four entrypoints exist. |
| R2, observations required to distinguish identities instead of predicate truth | Repaired. ASSURANCE §11 now tests indistinguishability across opposite predicate truth and retains instrument support. Supported parity is sufficient; a constant observation hiding even and odd values is not. |
| R3, preference overriding necessary-mutation exception | Repaired. The default preference and the justified, confined necessity exception coexist. Convenience alone remains insufficient. |
| R4, alleged import of optional recurrence into generic tickets | The original classification was wrong: installed rc.2 TICKET_METHOD already imposed the generic recurrence policy. Candidate 3 correctly locates that policy at TICKETS and makes Design its conditional refinement. C3-03 is the remaining account defect. |
| R5, material no-action outside the core result system | Original initial-selection case repaired; affected result contract still fails in C3-01. |
| R6, external deciding oracle described as provenance-only | Repaired by expressly scoping CONFORMANCE §5 as this corpus's construction qualification map. Its external expected distinctions must be acquired for that qualification; no adopting-Product rule is declared dependent on §5. This does not make whole-corpus qualification standalone. |
| R7, obsolete interpretation entry | Current root entry repaired: 155 clauses, five indexes, declared partial coverage. C3-04 is a small residual in the child entry. |

The R4 correction matters: absence of the Design profile does not waive an
existing generic implementation-migration ticket obligation. Installed
`TICKET_METHOD.md:1085–1118` preserves the second-credible-recurrence review,
third-local-rebuild stop, its three discharge alternatives, and the
distinction from merely discovered opportunities. A policy change remains
an owner decision; this review supplies none.

## What was independently established

The [package probe and receipt](PACKAGE_PROBE.json) reproduced all 81
admitted file digests, both inventory counts, the standards-set digest,
manifest schema, recorded trees and tag target. The manifest itself makes
82 materialized files in the author's count. Standards, plugins and a_c
have no delta between A and B. The bootstrap specimen uses only admitted
package bytes, not schema or template files borrowed from the source tree.
It proves the repaired input path, not a native install or all bootstrap
semantics. [Source-first package conclusions](PACKAGE_SOURCE_READBACK.md).

The five changed frames' recorded byte counts and hashes match, as do all
78 declared route/bind owner-hash occurrences across those frames. B's
three superseded conservation readings expressly say that current reread
is owed; they are not reported as accepted. The ODD frontier note now
describes the implemented initial/post-closure split, although the inline
source-disposition summary remains stale as included in C3-01. The unchanged
output-table branch in `freeze_ac.sh` now reaches the control invocation;
C3-02 concerns failure handling after it reaches that invocation.

These are affected-path checks and sampled semantic readbacks. They do not
requalify every excerpt, interpretation clause or ordinary-use frame. The
author's 52 generator tests, finite-oracle runs and seven controls were not
used in place of independent source reasoning.

## Next increment and standing

Make one bounded successor covering C3-01 and C3-02, with C3-03/C3-04 in the
same increment. Regenerate only affected views and accounts, then read back
the changed owners, their named consumers and the adverse cases above.
These findings do not justify another broad historical suite or expansion
of the deferred interpretation/actual-use work.

The closed result is `falsified` for “the affected repairs and offered
verification route preserve their governing contracts.” That result neither
erases repaired cases nor confers a whole-Product verdict. Current criteria,
reserved replacement decisions and release acceptance remain open. The
owner's baseline deferrals remain in force.

Expectations preceded candidate-body reads. Two fresh nonauthor reviewers
covered observation/results and design/recurrence. The parent checked the
package, conformance scope, interpretation entry, changed records and
reported counterexamples. All are Codex-family contexts; the parent authored
the competing implementation and prior review. These are bounded independent
readings of Claude's source, not independent statistical votes or new
cross-family acceptance for donor-authored parts. Acquisition limitations,
including truncated search output not treated as read evidence, are disclosed
in the [activation](ACTIVATION_AND_EXPECTATIONS.md) and both delegated
reports. No external paid actor call or native context-cost measurement was
used.

Only this commentary directory was written. Candidate source, common law,
tickets, indexes, refs and both tenant worktrees were left untouched. No
commit, merge, tag, push or publication was performed.
