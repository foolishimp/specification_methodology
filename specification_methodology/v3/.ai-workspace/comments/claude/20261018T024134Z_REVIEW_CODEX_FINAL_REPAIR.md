# Review: Codex final repair round, cross-family readback

Author: the Claude tenant session, at the product owner's instruction ("ok
whatever - review codex"). It authored the rival Claude candidate and the
RC4 review that this round answers, and none of Codex's repair.

Hypotheses, fixed at 20261018T022223Z after reading Codex's return,
reciprocal-review addendum and readback (main `06f2cf19`) and the
changed-file list, before reading any diff hunk:

- H1: the restored Reviewer compression still decides differently from its
  unchanged Baseline source, by barring a defect report or recheck, or by
  permitting a non-repair edit under a write grant.
- H2: the restored tenth drift signal decides a cause from a symptom, by
  presuming a missing requirement that diagnosis has not established.
- H3: the Totality clarification adds a permission while its row stays
  conserved.
- H4: a source Codex cites to reject this line's RC4 finding 4 does not
  state the claim, or did not state it at RC4.
- H5: an interpretation argument no longer matches its source span; the
  account and the program differ; or a frame excerpt or compression pin no
  longer equals its owner.
- H6: the inherited shortcut family survives in the interpretation beyond
  the three arguments Codex repaired.
- H7: a figure Codex reports does not reproduce: 32 pins, 120 excerpts, 81
  inventory entries, 709 determinations, 95 replacements, 36 questions.

## Verdict

**Yes: the final round repairs RC4 findings 1 to 3 and the remaining item
of finding 4, and its three interpretation repairs hold. No finding remains
in the repaired scope.**

Two of finding 4's three items were wrong and are withdrawn below. The RC4
review also missed the three interpretation readings that Codex repaired in
this round.

| Coordinate | Value |
|---|---|
| Reviewed package | `5a5b5ad80f0ba4b56b83aadd42ac130de53ba803`, Codex's `3.0.0-rc.5`; checkpoint `87512593` adds records only, `successor/` identical |
| Predecessor package | RC4, `92fdb01c52bc4c6c7a7e265f92a668d0adb65098` |
| Review answered | this line's RC4 review, `16ff2497` |
| Common input; builder | C3-I5-06 `4c340f7`; installed `v2.5.1-rc.2` |

This is a cross-family, source-first readback by a nonauthor of the repair.
It accepts nothing. Codex's return, addendum, readback and check records
were read as claims and pointers, not as evidence. Every figure below comes
from this reviewer's own scripts on Git objects at the exact commits.

## RC4 findings and the interpretation repairs

| Item | Final text | Result |
|---|---|---|
| 1, Reviewer compression narrower than its source | `stdo_compressed.md`: "The Reviewer does not edit the candidate, direct the repair, apply an STDO disposition, or authorize continuation"; it keeps "Findings and counterexamples may identify already-required behavior and be independently rechecked". The Baseline source and its pin are unchanged. | Repaired. A non-repair edit under a write grant is barred again. A defect report and a recheck stay permitted. |
| 2, Worked Binding recorded as conserved | The source is unchanged since RC4. Its row is now `superseded`, as an author proposal, under relation `RC5-EXAMPLE-R001` in question `RC1-CONSUMER-Q002`. The relation depends on the pending RF-005 replacement `RC1-CONSUMER-R002`. | Repaired. The relation states what the source decides: `invalid_basis` when the governing basis cannot interpret the predicate, and `indeterminate` when stale support leaves it undecidable under an interpretable basis (REFERENCE_FRAME_METHOD:1285–1290, RF-005 at 411–416). This is the only row whose disposition changed. |
| 3, tenth drift signal names no drift | SPEC_METHOD: "If a realization patch is treated as closing a real use-case gap whose required meaning is absent from current requirements, the governing gap remains unresolved. Intake selects the owning layer whose meaning must change; missing requirement meaning does not establish a direction or scope change." | Repaired. The symptom is back. Under a sufficient requirement the signal does not fire. With the meaning absent it fires and routes through intake, with no forced Intent change. |
| 4, item 3, Totality omits continuation and recovery | DESIGN_MODULE_METHOD §8 now lists "continuation, repair, recovery, re-entry, refusal, yielding or termination", the list of its unchanged owner, FOUNDATIONS Bounded construction. "should" is kept. | Repaired. It adds no permission beyond the owner, so the `conserved` row stands. |
| 4, items 1 and 2 | | Withdrawn, below. |
| Interpretation, constitutional chain | The chain endpoint "Repricing / new Goals / Intent" became "Intake-selected re-entry or observation", as in both source diagrams. | Holds. |
| Interpretation, persistent delta | "wrong code or stale governing stack, diagnosis still required" became "Universal Intake Triage establishes cause; persistence alone proves neither a defective realization, stale governing meaning nor adequate observation". A new obligation rules out the code-or-stale assumption. | Holds. |
| Interpretation, tenth signal | "constitutional renewal, not code hack" became "a realization patch cannot close a governing requirements gap; intake selects the smallest owning re-entry, with no forced direction or scope change". | Holds. It matches the repaired source. |

## Withdrawals

This line's earlier results were wrong in three places.

- **RC4 finding 4, items 1 and 2, and the first two bullets of the
  root-cause result's finding 4 (`f3f60f21`).** FOUNDATIONS Configuration
  states the one-actor permission: "An adequate configuration can use one
  actor, peers, a hierarchy or supported adaptive allocation. Producing,
  checking and accepting remain different responsibilities even where one
  actor is permitted to perform several." AC-005 applies FOUNDATIONS
  Judgment and authority, whose list of sources "cannot mint, widen,
  transfer or reconstruct authority", and it says: "Bind each copied,
  interpreted, encoded, evaluated or transported record to those existing
  grants". All three texts are present at `ad384bbe`, at `92fdb01c` and at
  `5a5b5ad8`. Codex's rejection of both items is correct.
- **RC4 H1, for the interpretation.** The RC4 review reported one
  compatible hit in the 709 determinations. At `92fdb01c` the account, the
  program and the map still carried the three predecessor readings in the
  table above, in the arguments of two determinations. H1 should have held
  there. Codex repaired them in this round (`91b06ebb`).
- **The RC4 pin count.** "31 of 31 compression pins" should read 32 of 32.
  That parse read only `source_digests:` blocks and missed the
  `index_digests:` pin for GLOSSARY_GUIDE.md in `stdo_compressed.md`. The
  pin matched then and matches now.

## Hypothesis results

- **H1 to H3 rejected**, by the two-case tests in the table.
- **H4 rejected**, which gives the first withdrawal.
- **H5 rejected**, by the identity checks below.
- **H6 rejected.**
  - Across all 709 determinations, 126 sentences pair a symptom with a
    remedy. None selects a re-entry layer from the symptom alone: each
    routes through triage, diagnosis or the owning layer, or states a scope
    limit.
  - The one that names Product re-entry, UP-013, follows its source:
    "Changing an outcome's meaning or scope, or introducing a new Product
    outcome, requires lawful re-entry at Product."
  - A phrase sweep of the account, program, map and mapping for the
    predecessor's wording finds the three repaired readings at RC4 and none
    at final. Its other hits are conditional routes at both commits.
- **H7 rejected.** Every figure reproduces.

## Checked independently

- **The authored diff under `successor/`, `92fdb01c..5a5b5ad8`:**
  - SPEC_METHOD, 8 lines; DESIGN_MODULE_METHOD, 4 lines;
  - four compressions: digest lines, plus the Reviewer sentence;
  - six regenerated frames;
  - DERIVATION_SOURCES: byte offsets and one digest;
  - two plugin manifests and the README: version label only;
  - the interpretation.
- **The account:** 709 determinations at both commits, none added or
  removed. Three changed in meaning (Totality, constitutional chain, drift
  signals) and 113 in coordinates only. `semantic_contracts` is unchanged.
- **Spans and program:** all 709 owner spans equal their source. The 709
  program literals equal the account in every material field.
- **Frames:** 120 of 120 excerpts equal their owner sections, with correct
  member digests, at `5a5b5ad8` and `87512593`. A one-word change to an
  excerpt was caught.
- **Compression pins:** 32 of 32 match (25 pin-block entries and 7
  `source_digest:` lines) at `92fdb01c`, `5a5b5ad8` and `87512593`.
- **`SOURCE_INVENTORY`:**
  - 81 of 81 entries match hash and size;
  - they cover every tracked file outside `interpretation/`;
  - its input commit, `91b06ebb`, holds the same member bytes;
  - its five interpretation digests match their files.
- **DERIVATION_SOURCES:** the three historical rc.2 members rebuild
  byte-exactly from successor spans and literals, at both commits.
- **Records:**
  - CONSERVATION has 691 rows: 595 conserved, 95 superseded, 1 not
    applicable.
  - REPLACEMENT_QUESTIONS has 36 questions.
  - Both bind source `91b06ebb` and account `2bcc60c7`.

## Same class in the Claude line

Claude candidate 8, source `9aee01f` and records `1db13bfe`, was read for
each class repaired here. One is present, and Codex has already reported
it.

- **Low: a failed scenario is still read as actual disagreement.**
  ASSURANCE:61–63 says "When a scenario fails, actual behaviour disagrees
  with the scenario's expected outcome". The next sentence allows that the
  scenario's observation is wrong. With a correct implementation and a
  faulty observation, actual behaviour agrees with the expected outcome,
  and the first sentence is false. It is the assumption of adequate
  observation that Codex's persistent-delta repair removes from its
  interpretation. The family row at ASSURANCE:96 carries the same reading.
  Codex's review of candidate 8, uncommitted in the main checkout at this
  writing, reports it as RC8-01. This review read the source after reading
  that finding, so this is a confirmation, not an independent discovery.
  Repairing candidate 8 is the product owner's decision.
- **Tenth drift signal:** SPEC_METHOD:610–613 keeps the symptom, "not a
  code hack", and routes by change class. The persistent-delta signal at
  601–604 names four causes for triage to diagnose.
- **Totality:** DESIGN_MODULE:1809 lists no responses, as rc.2 does, so no
  partial list arises.
- **Reviewer edit:** EXECUTIVE_BASELINE:1265 says "It does not edit the
  candidate, direct the repair or authorise continuation". Anti-Patterns
  item 10 at 1740 repeats it.
- **Interpretation:**
  - The rows of `qualification/C3-ITER5/determinations/DETERMINATIONS.json`
    that reach the five sites repaired since candidate 5 match their
    sources. ASSURANCE row 1 and DESIGN_MODULE row 6 changed with them; the
    unchanged rows state no route that the repairs changed.
  - The current encoding, `a_c/i3/`, carries none of the predecessor
    phrases.
  - The historical sets `a_c/set-5/` and `a_c/set-6/` still carry the
    earlier design-surprise reading, "require one bounded design_reframe".
    `a_c/README.md` declares them historical, not current interpretations
    of the rebuilt members, and names re-encoding as open work.
  - The other hits are dispositions quoting rc.2, historical reassessment
    batches, run inputs and the release note.

## Limits

- Codex's gates were not run, because they write into its records and need
  its toolchain. Its "package checks pass" is unverified here.
- Codex's own readback is a claim here.
- Not assessed:
  - the whole candidate;
  - the account's semantic fidelity beyond the sweeps above;
  - the frames' selection of sections.
- The hypotheses were committed together with this result, so only this
  record shows that they preceded the diff.
- Codex's line citations served as pointers only.
- Elapsed time and token spend are not instrumented.
