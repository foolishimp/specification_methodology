# Iteration 5 Handoff, Claude Line: candidate 6

Current candidate: candidate 6, `3.0.0-rc.6`, commit A `99054970ea3e30c76e52c20c0ef7ae22b4e78396`, local tag
`specification_methodology-claude/v3.0.0-rc.6` (object `c9e14d6b6b0a4d4e9db1382647069679d09fecc0`, not pushed),
commit B the commit that adds `release/manifest.json` for it. It repairs
the two findings of Codex's reciprocal review of candidate 5 and routes
the same class through diagnosis at four more places (Q19, eight rows).
Its freeze script writes the interpretation's digests after the consumers
step. The [review package](REVIEW-PACKAGE-RC6.md) is written for Codex's
affected readback, with the adverse cases and the rerun commands. The
[results table](RESULTS.md) and the [decision list](DECISIONS.md) (Q1 to
Q19) are current. Candidate 5, `4a63c92`, is superseded. The unrun
conservation batches in `reassess/` were built from an earlier candidate,
and batches 04, 05, 06, 11, 12, 13 and 14 hold text of sections the
repairs changed; batches are rebuilt from the candidate when the reading
is scheduled. Nothing is accepted.

The record of candidate 2 follows unchanged below.

---

# Iteration 5 Handoff, Claude Line: candidate 2

Current candidate: candidate 2, `3.0.0-rc.2`, commit A `ba882bc71a259fbe027fb2004d62d566b1ee2799`, local tag
`specification_methodology-claude/v3.0.0-rc.2` (object `fd37a5f3621e393d945057a451fc76c1db2ee43e`, not pushed),
commit B the commit that adds `release/manifest.json` for it. It repairs the
seven findings of the independent content review of candidate 1; the
[review package](REVIEW-PACKAGE-RC2.md) states the changed clauses, the
six counterexamples, the closure and bootstrap check and the readback
scope. The [results table](RESULTS.md) and the [decision list](DECISIONS.md)
(Q1 to Q18) are current. Every count in the record comes from
`tools/counts.py`. Nothing is accepted.

The record of candidate 1 follows unchanged below; its counts "26 members"
and "505" were wrong (23 and 471), as the ledger records.

---

# Iteration 5 Handoff and RC1 Candidate, Claude Line

The closing record of the Claude line's iteration 5 on the ratified common
input C3-I5-06 (`4c340f7`), written at the product owner's instruction
"run to RC1" and for the owner's assessment of both lines. Every check
named here is same-family working evidence unless it says otherwise.
Nothing here is accepted, and nothing claims acceptance or eligibility.

## Candidate

| Coordinate | Value |
|---|---|
| Branch | `tenant/claude/c3-synthesis` (worktree `specification_methodology-claude`), not merged, not pushed |
| Frozen candidate, commit A | `af3b8b7107c92a216cc53d629ddeefecd7f77fca` |
| Local annotated tag over commit A | `specification_methodology-claude/v3.0.0-rc.1`, object `32dfe61979fb727b9b3285efce66c1b7c2090bf2`, not pushed; a tenant-namespaced candidate tag, not the product's cut tag, which is the common pen's act under RELEASE §3 and §7 |
| Commit B | this commit: `release/manifest.json` bound to commit A and the tag object, validated against the manifest schema; this handoff; the ledger entry |
| Preceding candidate | `c66ed4e` (iteration 4), handoff `qualification/C3-ITER4/HANDOFF.md` |
| Donors | the Codex iteration 4 candidate (`9a93c5a`, `903f119`); the named techniques of the Codex iteration 5 candidate (`28d87ee`, `1e4bed6`), read only at those commits |
| Common input | C3-I5-06 at `4c340f7`, merged inward at `0a05106` |
| Ledger | `qualification/C3-SYNTHESIS/LEDGER.md`, section "Iteration 5" |
| Results table | [RESULTS.md](RESULTS.md); decisions [DECISIONS.md](DECISIONS.md); plan [PLAN.md](PLAN.md); returns `returns/` |

Digests at commit A: SHA-256 of the sorted `shasum -a 256` lines of each tree's files.

| Tree | Files | SHA-256 |
|---|---|---|
| `standards/` | 62 | `db3ba57dbac670cf85055f8435d1f51c4d8bf2d2c5ee8feabf37f9ff9827238e` |
| `a_c/` | 197 | `831c0aeb4b4f4330eee01e86f04be49722a9b306f3476ab8a22ab5320fe6736b` |
| `design/` | 7 | `18025a2cc05aed66b7cf56bd547c0ba2f93aa058b5cdbc965d2a85fabff447b5` |
| `qualification/` | 910 | `ba3d36000b540849bb501415b4c62b4767233c0b9e05960c93a3984a92de951c` |
| `plugins/` | 17 | `dae3a7ff9bbc002d89df9704011c47e62664df3f075a25c837ef1e83bd418d96` |
| `frontier/` | 3 | `51154e2841c91d8b6f37fcfb1fefe2e9c9db6e74159a909cfa1f28903f90e199` |
| `release/` | 3 | `b818141b6334ed2c03ab44bcc45c67a1ae0ffae7df83737254be3ce283c09cd3` |

## What changed in this iteration

- **Construction relation and assurance relations** (I5-01, E2E-01): owned at ACTIVATION §1 and FOUNDATIONS §3 and §4; two fresh-context readbacks, 37 findings repaired; one delivery-and-correction path carried through the candidate's own law.
- **Consumers** (I5-02): every family table carries a consumers paragraph, 319 rows, each consumer linked and judged; two readbacks, 33 findings repaired; a false regeneration claim corrected on the record.
- **Interpretation** (I5-05): rebuilt for the iteration 5 text, 155 clauses, group G14 with the five kinds of support; same-family fidelity cases and review, 7 disagreements repaired; reproduced from a clean archive with the pinned checker, every output byte-identical, 7 of 7 controls.
- **Frames and trial** (I5-06): twelve frames bind the construction and assurance relations by owner section and digest; the trial design delta with the `W` and `A` items and the grader's pair check; two readbacks, 28 findings repaired; the reconstruction-return distinction given an owner at EVALUATION §6.
- **Entry** (I5-08): README and release record at iteration 5; provenance out of constitutional text.
- **Ports** (I5-04): the determinations record and the finite assurance witness, adapted from the Codex iteration 5 techniques with attribution.
- **Reduction** (I5-07): TO4 declared before the traces; the two residual rivals repaired; traces deferred.
- **Conservation and decisions** (I5-03): the unread scope stated exactly; the consolidated owner decision list Q1 to Q16.
- **Blind read on `main`** (owner's instruction): test 1, owner texts of both candidates against the specification, Claude 55 present, 6 changed, 0 absent of 65; Codex 42, 19, 1; repairs to this line's owner texts from its findings.

## Working results (same family, fresh contexts, Fable at maximum effort)

| Activation | Subject | Result |
|---|---|---|
| R-I5-01, R-I5-01b | the construction relation and assurance relations owner texts | 25 then 12 findings, all repaired |
| Writers B1 to B7; R-I5-02, R-I5-02b | consumers of 318 family rows | 22 then 11 findings, all repaired |
| R-I5-06, R-I5-06b | frame bindings and the trial design delta | 16 then 12 findings, all repaired; one High found in the author's own repair |
| fidelity cases and review | group G14 and P4a of the interpretation | 22 cases: 14 agree, 7 disagree, 1 cannot answer; all repaired |
| blind read, test 1 | both candidates' owner texts against the specification | tallies above (`main` `bbaaebd`) |
| checker, controls, clean archive | `a_c/i3` at `1df225b` and again at each refreeze | valid, 0 diagnostics; 7 of 7 controls; byte-identical reproduction |
| finite oracles | conjunction (re-declared); assurance (new) | every assertion holds; every mutant falsified |

## Gaps the product owner should know

- **Criterion 4.** The trial is designed and instrumented; no actor has run; the shared protocol, resources and the harness disclosure that fit needs are the owner's.
- **Conservation.** 505 of 611 `conserved` rows unread by a nonauthor; every proposed relation pending.
- **Interpretation.** 24 sections encoded in part; 182 uncovered; G5 to G13 not encoded; fidelity same-family; the repaired clauses not re-read.
- **Reduction.** 38 of 46 paths untraced; TO1's frame-entry traces not made.
- **Reviews owed, bundled into one pass after this cut at the owner's instruction:** the conservation reading, the traces, the receiving-line assessment of the ports, the integrated readback of the iteration 5 repairs, and tests 2 and 3 of the blind read. Their findings may lead to candidate 2 on the same version line.
- **Manifest conventions.** `standards.source_root` and the release note's `source_path` carry the values the manifest schema fixes for a published cut (`specification/standards`, `releases/v3.0.0.md`); at this candidate the standards live under the project subtree root named in the manifest, and the note at `release/release-note.md`. The pen relocates them at publication.

## Corrections after the freeze

- The release note, `RESULTS.md` and the I5-03 return say 505 `conserved` rows are unread; the exact count by `frontier/REVIEW.json` is 471 (REFERENCE_FRAME_METHOD 70, WORLD_MODEL_METHOD 69, STDO_REFERENCE_FRAME_BASELINE 53, ODD_METHOD 48, SPEC_METHOD 46, AXIOMATIC_CALCULUS 37, TICKET_METHOD 25, TRAVERSAL_OCCURRENCE_PROFILE 24, DESIGN_MODULE_METHOD 21, RELEASE_METHOD 19, UX_METHOD 18, GLOSSARY_GUIDE 14, IDENTITY_METHOD 9, POSTING_GUIDE 9, WRITING_GUIDE 8, README 1). The I5-03 return's per-member list counts all 611 `conserved` rows. Commit A is not edited; candidate 2 carries the corrected figures (ledger, record correction).

## Owner scoping after the freeze

The product owner put out of scope for this candidate as the baseline STDO v3 (ledger, verbatim): complete interpretation coverage, the remaining actual-use expectation sets, and the authority compressions with their projections. They are follow-on work on the baseline, not conditions of it.

## Open decisions for the product owner

[DECISIONS.md](DECISIONS.md), Q1 to Q16.

## Rerunning the checks

`qualification/instruments/generate_frames.py --check`; `qualification/instruments/finite_oracle/*/check.py --check`; `a_c/i3/tools/assemble.py --check`; `qualification/C3-ITER4/tools/freeze_ac.sh <scratch>` (pinned checker and controls); `qualification/C3-ITER3/tools/{links,locus_check,frontier_check}.py`; `qualification/C3-ITER5/tools/determinations.py`; `qualification/C3-ITER4/tools/frontier_review.py`; `python3 -c "import json, jsonschema; jsonschema.validate(json.load(open('release/manifest.json')), json.load(open('standards/schemas/installed-release-manifest.schema.json')))"`.
