# Review of C3-I5-01, the universal construction model, at `455ce5d`

Subject: the common specification at `455ce5d` ("Add universal construction
model to v3 common specification"), recorded as C3-I5-01 at `1c18117`, with
Codex's nonauthor working review recorded at `b16faca`. Expectations were
fixed before opening it (`20261015T155533Z_EXPECTATIONS_REVIEW_C3_I5_01_455CE5D.md`,
commit `b463d88`). Read: the whole specification diff `3c4c503..455ce5d`
(seven files, 94 lines in, 19 out), the new PRODUCT, requirements,
principles and conformance sections in full, the INTENT and CAPABILITIES
changes, Codex's review, the T-001 and T-002 entries, and the GOALS change
after the source commit.

Standing: I am the Claude tenant's builder, an interested party; this is a
review for blocking defects and for the effect on the running iteration 4
builds. It accepts nothing. The product owner's exact-commit ratification
is the acceptance.

## Verdict

No blocking defect. `455ce5d` is ratifiable as it stands. Four Low
findings below are worth one successor before ratification if the owner
wants the text exact on first ratification; none changes a determination.

## Expectations against the text

| Id | Result |
|---|---|
| E1 addition, no silent change to the settled law | Met. P1 to P6 are byte-identical (Codex's check reproduced by the snapshot hashes); the six criteria, the three closure checks, the result algebra, Cross-Synthesis and Candidate Comparison are untouched. One stated change: criterion 5's discriminator set grows by nine member cases and one integrated check (`conformance/README.md`, 57 to 68 table rows). See F1 |
| E2 calculus, outcome, strategy, execution, evidence separated | Met. PRODUCT, Universal Construction Model, second paragraph; requirement items 1 and 7. Lawful incomplete construction and conditional proofs with retained premises are stated |
| E3 feedback, bugs, resources, recursion under existing owners | Met. Requirement item 4 routes a bug through the same intake and to its affected owner, "its label creates no separate delivery or authority mechanism"; item 8 says the model adds no independent ledger, role sequence or runtime; item 2 imposes no universal budget or scalar cost; item 6 requires no universal termination proof. See F3 on wording |
| E4 owners and re-entry for new obligations | Met. Item 8 binds the relation at the candidate's shared owner under single ownership and reduction; the discriminators apply to criterion 5 within the member's declared responsibility, in the form of the existing table, and add no candidate-text predicate |
| E5 no external theorem asserted | Met. "Universal scope establishes no general solver, fixed organisational structure, guaranteed convergence or theorem of categorical universality"; any categorical claim meets the demonstration standard |
| E6 hashes and links | Met for the specification. 18 of 18 snapshot hashes and byte counts reproduce from `455ce5d`. Every link added in the specification and entry files between `3c4c503` and `b16faca` resolves. Four links in Codex's I4 construction return post point to absolute paths in the Codex worktree, a commentary matter outside this review |
| E7 I4 remains the tenant basis | Met. GOALS, AGENTS, CLAUDE, `build_tenants/README.md` and T-002 say the last ratified input is C3-I4-03 at `3c4c503`, I5 admits no tenant work, and I5-01 to I5-04 are later tenant work. See the consequence below |
| E8 no acceptance claimed | Met |

## Findings

| Id | Severity | Finding | Smallest repair |
|---|---|---|---|
| F1 | Low | Criterion 5 reads "the applicable member-conformance discriminators"; after I5 there are two sets in play, 52 for a candidate admitted at C3-I4-03 and 61 for one admitted at an I5 input. Candidate Comparison's "same criteria, discriminators" does not say which set binds a candidate when the two lines are admitted at different inputs | In `conformance/README.md` or the C3 contract: a candidate is assessed under the discriminators of its admitted common input; scope the two inputs do not share is reported as unmatched under comparable coverage |
| F2 | Low | The model says strategy selection "belongs to the realisation and its work authority" and names steel thread, waterfall and iterative delivery as possible strategies, while Categorical Construction prescribes a steel thread as step 2 and the owner list carries "the steel thread" as a decision | One sentence at Categorical Construction: the sequence is this source project's selected strategy under the model, not a strategy the method prescribes to consumers |
| F3 | Low | "A bug is a category of feature or change work" (PRODUCT, requirement item 4, and "Bugs and new features enter the same work process" in INTENT): a bug is a kind of change work, not a kind of feature. "Homeostatic" is used without definition | "a category of change work, entering the same intake and delivery process as a feature"; define or drop "homeostatic" |
| F4 | Low | `GOALS.md` is a snapshot member of C3-I5-01 (hash at `455ce5d`) and was edited at `b16faca` (two status lines) after the source was frozen, so main's GOALS no longer equals the recorded member | Ratify `455ce5d` exactly, as recorded; keep post-freeze edits to status lines off snapshot members, or re-freeze and re-record before ratification |

## Consequence for the iteration 4 lines, for the ticket

- The I4 builds, their freezes and the Stage 3 and 4 comparison are
  unchanged: both candidates are assessed under C3-I4-03 and its 52
  discriminators and three closure checks. Nothing in I5 is owed by an I4
  candidate.
- An I5 admission would owe each line the work T-002 names as I5-01 to
  I5-04, which is not small: a shared owner for the construction relation
  (in the Claude candidate, FOUNDATIONS, with SPEC_METHOD applying it);
  every frame binding the construction requirement (the CAPABILITIES
  change); the nine new discriminators mapped in the candidate's
  CONFORMANCE member and read on the successor; the a_c interpretation and
  the entry projections brought into agreement; and integrated-use
  evidence through "the actual deciding path from the selected outcome
  through bounded work, observation, diagnosis and lawful continuation or
  closure".
- The cheapest lawful order is the one the staged plan already has:
  finish Stage 3 and let the owner choose the basis at Stage 4 on the I4
  evidence, then run I5 construction on the chosen line only. Running I5
  on both lines before the choice doubles that work.

## Codex's review

Read after my expectations were fixed. Its seven closed clause results
and six counterexample probes are consistent with what I found; it did
not raise F1 to F4, which are below its "material common-law finding"
threshold and are offered here as text repairs, not as defects in the
model.

## Checks

`i5_01_checks.py` in the session scratchpad: 18 of 18 hashes and byte
counts from `455ce5d`; links added between `3c4c503` and `b16faca` in the
specification, entry files, tickets and comments resolve except the four
absolute-path links in `comments/codex/20261015T132852Z_RETURN_CODEX_I4_CONSTRUCTION.md`.
