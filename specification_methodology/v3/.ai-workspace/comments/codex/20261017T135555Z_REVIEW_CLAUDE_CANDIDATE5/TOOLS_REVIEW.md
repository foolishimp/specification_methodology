# Candidate 5: verification tools and package binding

The prior C3-02 failed-control defect is repaired on this subject. The complete
freeze returns 1 for a failed required control and does not execute its final
consumer step. The newly named predicate gates propagate their tested failures.
One **Low** residual remains in the standalone `run_ac.sh` helper: failure of
its separate frame-index acquisition process is omitted from its exit status.
The complete freeze contains that counterexample by removing old output and
failing when the new projections are absent.

The exact manifest, admitted payload, bootstrap specimen and three changed frame
copies pass the bounded identity checks below. These results grant no member,
candidate, installation, release or adoption acceptance.

## Subject, basis and independent expectations

- Source A: `4a63c9293ddaa568803b81f1ed5dcc1d3dc19cec`.
- Package B: `a85f9ec98e43b942048a6c151aafd9662d2def90`.
- Tenant prefix: `specification_methodology/v3/build_tenants/claude/`.
- Common input: `4c340f7adec9f3c893e3e267b23e4cadeb357854`.
- Installed builder: v2.5.1-rc.2, manifest
  `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`,
  reverified by the parent. This reviewer read its bootstrap and applicable
  RELEASE_METHOD and REFERENCE_FRAME_METHOD source excerpts.
- Fresh nonauthor Reviewer `/root/peer5_tools`; Codex family, no authorship of
  the Claude repair. The parent's competing-line/common authorship is disclosed
  in the activation and supplies no independent acceptance evidence here.

[TOOLS_EXPECTATIONS.md](TOOLS_EXPECTATIONS.md) was written before candidate-body
or candidate-diff acquisition. Common Assurance supplies the composition,
failure/unknown-outcome, assertion/execution provenance and targeted-reassessment
obligations. Product C3 and conformance retain source fidelity, exact evidence
subjects and the acceptance boundary. The author review package and previous
probe programs supplied routes; their old or author-side results were not
treated as current proof.

All code loci below are relative to the tenant prefix at source A. No candidate
command was executed in an actual worktree.

## T5-T01 — Low: standalone enumeration failure returns success

**Locus:** `qualification/C3-ITER3/tools/run_ac.sh:4-12`, specifically the command
substitution at line 8. `FAIL` records only commands invoked through `run()`.
The frame-index enumeration runs outside that function; its nonzero exit is
discarded when the `for` loop receives no indexes. The script then exits 0.

**Counterexample:** on the exact valid frozen program, the real pinned checker
successfully validates. A PATH shim makes only the subsequent `python3 -I -c`
enumeration process exit 37. `run_ac.sh` exits 0, produces no fresh projections,
and records only `validate ... exit=0`. With a pre-existing sentinel projection
in its output directory, it again exits 0 and retains that file. The unchanged
program hash is
`5fea30ce62bbc8eea3b1904712d47ae0feb23ac0d8d4b49174dc8c1ea74b3b22`.

This supplies a process failure, representing interruption/resource failure of
the separate acquisition process. It does not claim such a real interruption
occurred during normal use, nor rely on malformed input that validation would
already reject. The direct helper's successful exit cannot alone establish that
it completed all required projections under this condition.

**Containment and severity:** `qualification/C3-ITER4/tools/freeze_ac.sh:9`
removes `$SP/out` before running the helper. With the same injected failure and
a preseeded old projection, the complete frozen wrapper removes the old file,
then exits 1 at its projection copy on line 12; it never reaches consumers.
There is no demonstrated false successful freeze. That containment and the
narrow process-failure trigger justify Low severity.

**Disposition:** retain as a bounded standalone-helper defect. Check the
enumeration's own status before iterating. No wider checker redesign or
historical-suite rerun is implied. This does not reopen the repaired
validate/project/control result propagation identified by prior C3-02.

Evidence: `run-ac-frame-enumeration-failure` in
[TOOLS_FAILURE_RECEIPT.json](TOOLS_FAILURE_RECEIPT.json), and
`run-ac-enumeration-failure-with-stale-output` plus
`freeze-enumeration-failure-contained` in
[TOOLS_FOLLOWUP_RECEIPT.json](TOOLS_FOLLOWUP_RECEIPT.json).

## Supported repairs and bounded checks

| Path | Independent observation | Standing |
|---|---|---|
| `links.py:22-38` | A valid fixture returns 0; missing file plus missing anchor returns 1; `X_v` outside the two exact exceptions returns 1. | Named broken-link gate repaired; no whole-Markdown-parser claim. |
| `locus_check.py:30-41` | A resolving locus returns 0; an unresolved locus returns 1. | Named locus gate repaired. |
| `frontier_check.py:17-28` | An exact common row plus tenant-only row returns 0; missing and duplicated common rows each return 1. | Named membership gate repaired. |
| `frontier_review.py:93-116` | Frozen records return 0; a newly unresolved predecessor anchor outside the exact exception set returns 1. | The new exception-bounded failure gate holds. Semantic row assessment belongs to the parent/other scope. |
| `consumers.py:44-50` | Current owners return 0; changing one owner reference to an absent heading returns 1. | Named owner-resolution gate repaired; consumer counts alone do not establish fidelity. |
| `run_ac.sh:4-12` | A failed validate survives later successful projection commands; failed projections also produce exit 1. | Checker-command propagation repaired; T5-T01 limits broader subprocess reliability. |
| `ac_controls.py:70-75`, `freeze_ac.sh:5,24-25` | The complete current freeze returns 0 with seven controls holding. Forcing `identity-positive` false produces `holds_all:false`, wrapper exit 1 and an unchanged downstream-consumer sentinel. An unknown forced-control name returns 1 and does not rewrite the report. | Prior C3-02 is supported as repaired on A. |
| `release/check_install.py:57-65` | With the existing builder interpreter, exact package materialization returns 0. Omitting its bootstrap schema returns 1. A separate injected missing-anchor observation is written into the report and returns 1 through the newly added gate. | Named bootstrap/anchor gates hold. |

The missing-anchor test substitutes one read-only `git show` response while
leaving `check_install.py` unchanged. It tests propagation of a reported failure;
it is not an authenticity test. The independent manifest verifier supplies that
separate claim below. The first install attempts lacked `jsonschema` in their
default interpreter and support no install-gate judgment; only those unavailable
cases were rerun using
`/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python`, with its dependency
location recorded. Successful unrelated cases were not rerun.

The source readback covered every newly changed C3-ITER3/C3-ITER4 verification
tool, both changed shell layers and `release/check_install.py`, plus the
unchanged materializer they call. This is broader than checking the final
`sys.exit` lines, but is not an exhaustive fault audit of every shell operation.

## Exact package and frame binding

[TOOLS_PACKAGE_RECEIPT.json](TOOLS_PACKAGE_RECEIPT.json) independently verifies
the manifest SHA-256
`6793ad888ba980ec867582d4f8a900d7a49621da08908df22f34972ece3a82bc`.
The qualified ref identifies annotated tag object
`92ca34cdee52cdd305fc32a5160574651e4bb743`, which peels to A. Repository,
standards and Product-subtree tree identities agree. All 62 standards files,
17 plugin files, license and release note reproduce their recorded digests;
the standards set digest is
`29fe90e3e3814240283e2882384d0a5088095ee94af3294d16f303f5e3b09e79`.
Standards/plugins/a_c bytes are unchanged from A to B. There are 81 payload
files, or 82 including the installed manifest. The manifest and a concretely
filled Product Definition specimen validate against the admitted schemas, and
all four specimen entrypoints are admitted files.

The materialized-layout check reports 15 outside-package link occurrences and
no missing anchors on the positive subject. Its own author package explicitly
leaves outside links report-only, including the pending interpretation/package
boundary. This green exit establishes its stated bootstrap/anchor checks,
not complete package closure or native installation. No toolchain install or
host activation was performed; owner decisions remain open.

[TOOLS_FRAME_RECEIPT.json](TOOLS_FRAME_RECEIPT.json) verifies the byte counts,
frame digests and 44 full-owner pins across `bootstrap`, `binding` and
`dm-task-d`. `bootstrap` and `binding` change only owner identity pins.
`dm-task-d` additionally carries the new DESIGN_MODULE F13 import with rebased
links. The current generator's `--check` returns 0 in scratch. These are copy
and identity results, not new independent task-use evidence or a sufficiency
judgment. Interpretation inventory remains 155 clauses, five frame indexes and
zero residuals; no semantic fidelity inference follows from those counts.

## Closed result, reproduction and limits

The bounded broad claim that every required subordinate operation contributes
to the standalone verification command's exit is **falsified** by T5-T01.
Prior C3-02's concrete failed-control/checker-command repair and complete caller
behavior are **satisfied for the tested conditions**. Exact package and changed
copy identity checks are also satisfied in their stated scope. No integrated
C3 or release-acceptance judgment is supplied.

Reproduction uses the scripts beside this report:

```sh
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B tools_failure_probe.py /Users/jim/src/apps/specification_methodology > TOOLS_FAILURE_RECEIPT.json
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B tools_followup_probe.py /Users/jim/src/apps/specification_methodology > TOOLS_FOLLOWUP_RECEIPT.json
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B tools_package_probe.py /Users/jim/src/apps/specification_methodology > TOOLS_PACKAGE_RECEIPT.json
python3 -B tools_frame_probe.py /Users/jim/src/apps/specification_methodology
```

Run from this commentary directory. The failure script creates unique scratch;
the follow-up uses that run's receipt to select only its scratch. Receipts retain
the original host-interpreter failure, corrected narrow observations, supplied
faults, commands and output tails. They do not depend on today's scratch still
existing to understand or reproduce the counterexamples. The package verifier
is adapted from the earlier review's script, rebound to A/B and strengthened
with annotated-tag and exact-ref equality; old results receive no credit.

Conservative cumulative source accounting is **413,305 bytes**, below the
524,288-byte allocation: full-file charges overbound excerpted/truncated reads,
and repeated diff source counts again. Model-authored probes, machine-only
payload acquisition and returned observation JSON are separately excluded from
that source measure. Approximately 12.5 minutes elapsed from the recorded
expectations to this return; preliminary bootstrap time is
uninstrumented (estimated in the expectations). The 30-minute progress
checkpoint was not reached. Host-retained context, token usage and spend remain
uninstrumented; **active-context fit is indeterminate**. See
[TOOLS_ACQUISITION_RECEIPT.json](TOOLS_ACQUISITION_RECEIPT.json).

Only this commentary directory and unique `/private/tmp` scratch received
writes. The three actual tenant/common worktrees remain clean at their original
HEADs; pre-existing main-worktree tracked changes remain present. Concurrent
review commentary is visible. No Git mutation command was issued. See
[TOOLS_STATE_RECEIPT.json](TOOLS_STATE_RECEIPT.json). No further tests, external
calls, repairs or agents were selected.
