# RETURN: T-01 run 20261011-A2-claude-fresh-001

Case: urn:stdo-3:claude:case:T-01:2 (CASE-2.md), run A2, whole-step context
cap 20,000 bytes. Subject commit as named by the launcher: `cee1157` on
`tenant/claude/c3` (not verified by git; git was prohibited). Constructor: a
fresh Claude Code activation, model `claude-fable-5-1`, with no history and
only the inputs named below. Step actors: `claude -p --model sonnet`, observed
id `claude-sonnet-5-5`, started only through `step_actor.py`.

Wall clock (`date -u`): start `Sun 11 Oct 2026 13:15:30 UTC`; end
`Sun 11 Oct 2026 13:24:05 UTC`; elapsed 8 minutes 35 seconds.

Stop state of this run: satisfied. Composite: satisfied (23 of 23 routes
satisfied, no failures, no unresolved routes). Residuals are carried in §7.

## 1. Intake (CALCULUS §1)

Outcome served. The shared task of CASE-2: for each of the 23
`stdo://releases/v2.5.1-rc.2/standards/<member>#<slug>` routes cited in
FOUNDATIONS §3, one core result in the five-member algebra with evidence, and
one composite for the section under the declared conjunction, produced by
bounded step actors whose whole context is measured against the cap before
any actor exists. The run is an instance of the method qualifying itself
(EVALUATION §7) against the expected distinctions E1 to E5 of CASE-2.

Affected set and invariants. The seven cited paragraphs of FOUNDATIONS §3
(P1, P2, P3, P4a, P4b, P5, P6; P0 cites no route) and the 23 rc.2 sections
they cite, under the card's contract. Invariants: the fit test is a byte
measurement recorded before any read (CALCULUS §2.3); a step over the cap
starts no actor; each route's coupled pair (paragraph, whole section) and the
card sit together in one step (CALCULUS §4; CASE-2 Coupling); no trimming,
summarising or piecewise reading of a section; nothing coerced to satisfied
(CALCULUS §3); the composite is the declared conjunction (FOUNDATIONS §4).

Basis by identity and digest. Verified with `shasum -a 256` at intake; all
four match the CASE-2 table:

| File | SHA-256 | Bytes |
|---|---|---|
| `standards/FOUNDATIONS.md` | `2f15c6c1c2561ef5ff0da4ba5f961926efa86fb8f6b35b1f61f653a9e4038a22` | 15,218 |
| `standards/CALCULUS.md` | `d708e76c11969c27e5832286ed78a6921decca29234db86ec23b6581524aee0c` | 15,242 |
| `standards/EVALUATION.md` | `fc063460e6834c190bcc5fe045d4a5a8f45a2ffd96a0ec2cad4fa82b677f246d` | 8,042 |
| `a_c/t1/projection-bounded-activation-materialized.json` | `e13a651410715a551f192d28d9a06754fa58a393364a6c5307e0012dfb5c4089` | 96,119 |

Other inputs: `qualification/cases/T-01/CASE-2.md` 12,920 bytes;
`STEP_CARD.md` 2,464; `step_actor.py` 8,377; `fragment.py` 2,472; the rc.2
install at `/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/`
touched only through `fragment.py --size` and through the instrument.

Grant. Permitted: read the inputs above; measure with `fragment.py --size`;
run reading steps through `step_actor.py` (dry and real); write exactly this
file. Prohibited and not done: reading any rc.2 section text (`--text`, cat,
or `steps/<id>.in.md`); reading CASE.md, `received/`, other runs, reviews,
design, RETURNS.md or any other tenant file; git; modifying anything outside
this run directory; modifying the instrument. Decisions reserved to others:
assessment of this record (an assessor other than the author); acceptance
(Jim); enlarging the envelope or selecting another actor (owner of the
envelope, CALCULUS §2.3).

Re-entry conditions. A slug the instrument cannot resolve (route result
invalid_basis); a route whose single-route step exceeds the cap (out_of_frame
with the measured size, or escalation naming the envelope); an actor failure
or non-conforming output (re-run within the allowance, else indeterminate for
that route); exhaustion of the allowance; a digest mismatch at intake (run
invalid_basis). None of these occurred.

Cap and allowance. Whole-step context cap 20,000 bytes as logged by the
instrument (`measured.total_bytes`). At most 30 step-actor starts and 60
minutes wall. Used: 8 starts, about 6 minutes.

## 2. Closure and projection boundary (CALCULUS §2)

Seed Z: the 23 routes, each a (tenant paragraph, rc.2 section) pair.
Relation family R: the paragraph cites the section; the card's contract
binds the judgment to the whole section. Closure: the seven cited paragraphs,
the 23 sections, the card and the system line.

Route list, with the section sizes measured by `fragment.py --size` (section
bytes only, before the instrument's block header):

| Route | Para | rc.2 section | Section bytes | Step |
|---|---|---|---|---|
| R01 | P1 | AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity | 378 | S01-P1 |
| R02 | P1 | AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation | 325 | S01-P1 |
| R03 | P1 | AXIOMATIC_CALCULUS.md#ac-019-valid-model | 801 | S01-P1 |
| R04 | P1 | REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse | 290 | S01-P1 |
| R05 | P2 | SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014 | 4,219 | S02-P2 |
| R06 | P2 | DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005 | 653 | S02-P2 |
| R07 | P3 | SPEC_METHOD.md#recursive-product-taxonomy | 2,925 | S03-P3 |
| R08 | P3 | WORLD_MODEL_METHOD.md#entity-cut-construction-law | 3,486 | S03-P3 |
| R09 | P4a | AXIOMATIC_CALCULUS.md#ac-016-typed-composition | 557 | S04-P4a |
| R10 | P4a | REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand | 430 | S04-P4a |
| R11 | P4b | AXIOMATIC_CALCULUS.md#ac-009-residual-conservation | 259 | S05-P4b-ac |
| R12 | P4b | AXIOMATIC_CALCULUS.md#ac-013-transformation | 6,411 | S05-P4b-ac |
| R13 | P4b | AXIOMATIC_CALCULUS.md#ac-005-authority-conservation | 324 | S05-P4b-ac |
| R14 | P4b | DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017 | 2,942 | S06-P4b-up |
| R15 | P4b | SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021 | 5,914 | S06-P4b-up |
| R16 | P5 | REFERENCE_FRAME_METHOD.md#rf-012-closed-results | 624 | S07-P5 |
| R17 | P5 | REFERENCE_FRAME_METHOD.md#rf-014-capability-fit | 318 | S07-P5 |
| R18 | P5 | AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal | 275 | S07-P5 |
| R19 | P5 | DESIGN_MODULE_METHOD.md#8-totality-rule | 660 | S07-P5 |
| R20 | P6 | SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008 | 728 | S08-P6 |
| R21 | P6 | SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022 | 5,343 | S08-P6 |
| R22 | P6 | REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation | 297 | S08-P6 |
| R23 | P6 | REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation | 437 | S08-P6 |

All 23 slugs resolved; the instrument refused none for an unresolved slug.

Single-step closure, measured by dry run and refused by the instrument before
any actor existed:

| Dry step | Content | Measured | Fit |
|---|---|---|---|
| S00-closure7 | P1, P2, P3, P4a, P4b, P5, P6 and all 23 sections (the closure as CASE-2 defines it) | 49,948 bytes | over cap; `refused`, exit 3, no actor |
| S00-closure | the same plus P0 (an extra measurement taken first; P0 cites no route and is outside the closure) | 50,557 bytes | over cap; `refused`, exit 3, no actor |

CASE-2 recorded 49,938 at design time; the 10-byte difference is the header,
which carries the step id. The closure does not fit the 20,000-byte envelope,
so the outer contract was refined (CALCULUS §2.3, option "refine").

Partition, first attempt: one step per cited paragraph, each holding all of
that paragraph's routes. Dry-run measurements:

| Dry step | Routes | Measured | Fit |
|---|---|---|---|
| D-P1 | R01 to R04 | 5,981 | fits |
| D-P2 | R05, R06 | 8,420 | fits |
| D-P3 | R07, R08 | 9,975 | fits |
| D-P4a | R09, R10 | 4,485 | fits |
| D-P4b | R11 to R15 | 20,364 | over cap; `refused`, no actor |
| D-P5 | R16 to R19 | 5,889 | fits |
| D-P6 | R20 to R23 | 11,089 | fits |

The P4b group exceeds the cap by 364 bytes, so capacity forced a second
refinement of that group only. Split by member family so that each step
still holds whole sections and the P4b paragraph:

| Dry step | Routes | Measured | Fit |
|---|---|---|---|
| D-P4b-ac | R11, R12, R13 (the three AXIOMATIC_CALCULUS clauses) | 11,197 | fits |
| D-P4b-up | R14, R15 (the two UP clauses) | 12,994 | fits |

Final partition and the real steps' own measurements (each logged as
`measured` immediately before its `actor_started`; the real step ids are two
characters longer than the dry ids, which moves each total by 2 bytes):

| Step | Para | Routes | Measured | Cap | Fit |
|---|---|---|---|---|---|
| S01-P1 | P1 | R01, R02, R03, R04 | 5,983 | 20,000 | fits |
| S02-P2 | P2 | R05, R06 | 8,422 | 20,000 | fits |
| S03-P3 | P3 | R07, R08 | 9,977 | 20,000 | fits |
| S04-P4a | P4a | R09, R10 | 4,487 | 20,000 | fits |
| S05-P4b-ac | P4b | R11, R12, R13 | 11,199 | 20,000 | fits |
| S06-P4b-up | P4b | R14, R15 | 12,996 | 20,000 | fits |
| S07-P5 | P5 | R16, R17, R18, R19 | 5,891 | 20,000 | fits |
| S08-P6 | P6 | R20, R21, R22, R23 | 11,091 | 20,000 | fits |

Reason for the partition. CASE-2 leaves the choice between one route per
step and grouping by paragraph. Grouping by paragraph keeps every route's
coupled pair in one step, satisfies the coupling contract, and transfers the
card and the paragraph once per group instead of once per route: 70,046
bytes into step actors over 8 starts, against about 123,600 bytes over 23
starts by the sum of CASE-2's design-time route-step table. That is the
proportionality obligation of CALCULUS §6 applied to the method's own
execution. The P4b split was not a choice: it was forced by the 20,364-byte
measurement, and the member-family cut was chosen because it keeps every
section whole and both halves well under the cap. No compression, trimming,
summarising, piecewise reading, actor change or envelope enlargement was
used.

Projection boundary. Excluded: P0 (cites no route) and every other part of
the tenant corpus; every rc.2 section not cited in §3. External: the rc.2
text itself, which the constructor never read; it entered only the step
actors' contexts. Unresolved: the P4b sentence that the five clauses' "nine
statements of conservation become one obligation" is a relation across all
five sections; no fitting step can hold all five with P4b (20,364 > 20,000),
so no step could judge it and it is carried as a residual (§7). Translated:
none. Invalidation-sensitive: the four digests above, the rc.2 install at
the named path, and the card text (its bytes enter every step).

## 3. Per-route results

Each route's result and evidence are the step actor's own output lines,
quoted verbatim from `steps/<id>.out.md`. The constructor did not alter,
re-judge or supplement any of them.

Summary:

| Route | Result | Mode | Step | Residual recorded by actor |
|---|---|---|---|---|
| R01 ac-017 | satisfied | by reference | S01-P1 | none |
| R02 ac-018 | satisfied | by reference | S01-P1 | none |
| R03 ac-019 | satisfied | by reference | S01-P1 | none |
| R04 rf-008 | satisfied | by reference | S01-P1 | yes (contracts versus frames) |
| R05 up-014 | satisfied | by reference | S02-P2 | none |
| R06 up-005 | satisfied | by reference | S02-P2 | none |
| R07 recursive-product-taxonomy | satisfied | by reference | S03-P3 | none |
| R08 entity-cut-construction-law | satisfied | by reference | S03-P3 | none |
| R09 ac-016 | satisfied | restated | S04-P4a | yes (steps versus traversals; "exact" omitted; two AC-016 sentences not restated) |
| R10 rf-010 | satisfied | by reference | S04-P4a | yes (subjects differ; judged on 1 and 2 only) |
| R11 ac-009 | satisfied | by reference | S05-P4b-ac | none |
| R12 ac-013 | satisfied | by reference | S05-P4b-ac | yes ("nine statements" not checkable from one section) |
| R13 ac-005 | satisfied | by reference | S05-P4b-ac | none |
| R14 up-017 | satisfied | by reference | S06-P4b-up | none |
| R15 up-021 | satisfied | by reference | S06-P4b-up | yes (section never uses "conservation") |
| R16 rf-012 | satisfied | by reference | S07-P5 | yes ("restated in CALCULUS §3" not judged) |
| R17 rf-014 | satisfied | by reference | S07-P5 | none |
| R18 ac-007 | satisfied | by reference | S07-P5 | yes ("restated in CALCULUS §3" not judged) |
| R19 8-totality-rule | satisfied | by reference | S07-P5 | yes ("should", design-module scope) |
| R20 up-008 | satisfied | by reference | S08-P6 | yes (UP-008 silent on authority; not attributed) |
| R21 up-022 | satisfied | by reference | S08-P6 | none |
| R22 rf-006 | satisfied | by reference | S08-P6 | none |
| R23 rf-007 | satisfied | by reference | S08-P6 | none |

Evidence, verbatim. `steps/S01-P1.out.md`:

```
ROUTE AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity | satisfied | by reference | evidence: "Interpretation cannot treat absence as immateriality without a recorded basis and authority" bears on "Subject, representation and interpretation are distinct; meaning holds within a declared context" and on "structural success never establishes fidelity"; the section's subject is interpretation fidelity, as the paragraph attributes | residual: none

ROUTE AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation | satisfied | by reference | evidence: "Structural success is evidence for semantic review, not a substitute for it" bears on "structural success never establishes fidelity"; "Structural conformance decides closed syntax, types, identities, references" bears on "'Algorithmic' means explicit and structurally checkable" | residual: none

ROUTE AXIOMATIC_CALCULUS.md#ac-019-valid-model | satisfied | by reference | evidence: "No generic checker may claim the semantic or authority subset unless the model supplies an exact lawful decision contract" bears on "a semantic decision is lawful only under an exact decision contract"; "structural evaluation and semantic acceptance remain distinct" bears on "structural success never establishes fidelity" | residual: none

ROUTE REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse | satisfied | by reference | evidence: "Shared material does not establish identical meaning, basis, authority, or result" bears on "with purpose, identity, evidence and authority fixed, two contracts give one representation two meanings" | residual: The paragraph's two-contracts example is about contracts, and RF-008 is about frames. The paragraph only names RF-008 as conserved and does not restate it. Nothing in the section contradicts the paragraph.

STEP S01-P1 | routes 4 | bytes_seen 5983
```

`steps/S02-P2.out.md`:

```
ROUTE SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014 | satisfied | by reference | evidence: "A method obligation is proportional when its contraction of the admissible interpretation space justifies the additional concepts" and "Increased agent capability may enlarge the bounded relation an agent can resolve; it does not grant authority" bear on "an obligation with no route to the outcome is unjustified" and "identical capacity serves opposite purposes". Neither is contradicted, and the section's subject is proportionality, which matches the cited slug. | residual: none
ROUTE DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005 | satisfied | by reference | evidence: "Prime review accounts for governance cost as well as implementation count" and "Evidence remains proportional to semantic change and risk" bear on "an obligation with no route to the outcome is unjustified". The paragraph only names UP-005 as conserved. Nothing contradicts it, and the section's subject, boundary and governance cost, matches the cited slug. | residual: none
STEP S02-P2 | routes 2 | bytes_seen 8422
```

`steps/S03-P3.out.md`:

```
ROUTE SPEC_METHOD.md#recursive-product-taxonomy | satisfied | by reference | evidence: "The role creates no new Product identity" and "do not confuse an immutable RC release cut or installed product with the mutable source project" bear on "Conserves ... the recursive Product taxonomy"; the section's subject is the roles of Product, Install, Source Project and related terms, and nothing in it contradicts the identity paragraph | residual: none
ROUTE WORLD_MODEL_METHOD.md#entity-cut-construction-law | satisfied | by reference | evidence: "identity, boundary, authority, state, evidence, treatment, covariance, and ambiguity" and "Boundary is interventional in character" bear on "identity ... current state ... a boundary is a claim with a proof obligation"; the section's subject is entity cut admissibility, and it lists identity and state as separate surfaces | residual: none
STEP S03-P3 | routes 2 | bytes_seen 9977
```

`steps/S04-P4a.out.md`:

```
ROUTE AXIOMATIC_CALCULUS.md#ac-016-typed-composition | satisfied | restated | evidence: "compose only when the first result type and judgment satisfy the second traversal's exact domain and preconditions" and "retains both traversal identities, intermediate results, judgments, evidence, authority, provenance, and stop states" match "compose only when the first's result type and judgment satisfy the second's domain and preconditions" and the same retained list in P4a | residual: P4a says "steps" where AC-016 says "traversals", and it omits "exact". Neither contradicts AC-016. P4a does not restate AC-016's sentence against flattening proposal, evaluation and decision, or its sentence that no universal F_P -> F_D -> F_H sequence is prescribed.

ROUTE REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand | satisfied | by reference | evidence: "Composition law is required only when the governing evaluation combines their internal variables, transports evidence or values across them" and "Independently activated evaluations may instead return closed results to one declared conjunction or decision rule" do not conflict with P4a's "Independent." and its conservation of typed composition | residual: RF-010's subject is frame composition on demand, while P4a's subject is typed step composition. The overlap is only that both concern when composition law applies. "Independent." is terse and is not a restatement of RF-010, so I judged only criteria 1 and 2.

STEP S04-P4a | routes 2 | bytes_seen 4487
```

`steps/S05-P4b-ac.out.md`:

```
ROUTE AXIOMATIC_CALCULUS.md#ac-009-residual-conservation | satisfied | by reference | evidence: "remains in `X` until an authorized disposition creates an exact successor model" bears on the paragraph's residual instance of conservation, and on "each continues to govern its own scope" | residual: none
ROUTE AXIOMATIC_CALCULUS.md#ac-013-transformation | satisfied | by reference | evidence: "Material residuals remain in the successor residual set unless an exact authorized disposition is included" and "Every input local-record identity is classified exactly once as preserved or removed" bear on the paragraph's transition and residual instances of conservation | residual: This section states several conservation statements (the local delta, the external delta, residuals). The "nine statements" total across the five cited clauses cannot be checked from this section alone.
ROUTE AXIOMATIC_CALCULUS.md#ac-005-authority-conservation | satisfied | by reference | evidence: "retain their declared semantic, operation, evaluation, and decision authority" and "does not transfer authority" bear on the paragraph's authority instance of conservation | residual: none

STEP S05-P4b-ac | routes 3 | bytes_seen 11199
```

`steps/S06-P4b-up.out.md`:

```
ROUTE DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017 | satisfied | by reference | evidence: rc.2 "A bounded local action conserves governing truth; it does not rewrite it" bears on the tenant's naming of UP-017 as a conservation statement with a "frame" instance | residual: none

ROUTE SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021 | satisfied | by reference | evidence: rc.2 "admits the complete transition or none, never a subset" and "Their production and invalidation must be recoverable" bear on the tenant's treatment of UP-021 as a conservation statement with "transition" and "evidence by reference" instances | residual: The section's subject is admission and never uses the word conservation. The conservation reading is supported only through the complete-transition-or-none and recoverable-facts clauses. Nothing contradicts it.

STEP S06-P4b-up | routes 2 | bytes_seen 12996
```

`steps/S07-P5.out.md`:

```
ROUTE REFERENCE_FRAME_METHOD.md#rf-012-closed-results | satisfied | by reference | evidence: "`indeterminate`... `out_of_frame`... `invalid_basis`" and "preserving explicit indeterminate, out-of-frame, and invalid-basis pressure" bear on "result algebra carries indeterminate, out_of_frame and invalid_basis as first-class outcomes" | residual: The claim that RF-012 is "restated once in CALCULUS §3" is about another section and was not judged.

ROUTE REFERENCE_FRAME_METHOD.md#rf-014-capability-fit | satisfied | by reference | evidence: "The actor may not silently omit material relations to fit context" and "human authority may select another actor, refine the frame, sequence activations" bear on "cannot report success on [a condition outside its context]" and "control model names the next move" | residual: none

ROUTE AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal | satisfied | by reference | evidence: "follows the declared result algebra rather than being coerced to success" bears on "cannot report success on one"; "failed, missing, indeterminate, out-of-scope, or invalid-basis result" bears on the first-class outcomes | residual: The claim that AC-007 is "restated once in CALCULUS §3" is about another section and was not judged.

ROUTE DESIGN_MODULE_METHOD.md#8-totality-rule | satisfied | by reference | evidence: "failure is returned in a typed and explicit form when practical" and "Semantic functions should be total or as close to total as the language and problem allow" bear on the paragraph's totality principle (P5) | residual: The section's subject is semantic functions in design modules, and its wording is "should", not an absolute. The tenant paragraph applies totality to steps and result algebras. Because the paragraph only names the rule as conserved, this was not treated as a contradiction.

STEP S07-P5 | routes 4 | bytes_seen 5891
```

`steps/S08-P6.out.md`:

```
ROUTE SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008 | satisfied | by reference | evidence: "semantic basis ... evidence basis ... state projection" bears on "Definitions, assumptions, observations, candidate judgments and accepted claims have distinct standing; evidence supports a claim on a basis" | residual: UP-008 does not mention authority, and the paragraph does not attribute authority content to it. Its subject, the separation of semantic and evidence bases, fits the justification half of P6.
ROUTE SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022 | satisfied | by reference | evidence: "A claim's quantifier, population, and scope cannot exceed its evaluated evidence" and "independently authorized evaluator authority" bear on "evidence supports a claim on a basis; authority permits or disposes within scope" | residual: none
ROUTE REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation | satisfied | by reference | evidence: "does not mint, widen, transfer, or reconstruct ... authority from actor identity, available capability, evidence shape" bears on "neither is minted by the other" | residual: none
ROUTE REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation | satisfied | by reference | evidence: "Evidence supplies observations ... Decision authority disposes the result" bears on "evidence supports a claim on a basis; authority permits or disposes within scope" | residual: none
STEP S08-P6 | routes 4 | bytes_seen 11091
```

Echo check (E4). For every real step the `bytes_seen` the actor echoed
equals the instrument's `measured.total_bytes` and the `actor_started`
`input_bytes`: 5,983; 8,422; 9,977; 4,487; 11,199; 12,996; 5,891; 11,091.
Each output carries exactly as many ROUTE lines as the step's declared
routes, and the STEP line names the step's own id.

## 4. Composite

Rule (CASE-2; FOUNDATIONS §4; CALCULUS §3): a declared conjunction over the
23 route results; satisfied only when every route is satisfied; otherwise
falsified if any route is falsified, else invalid_basis if any, else
out_of_frame if any, else indeterminate.

Computation: 23 route results, all `satisfied`. Set of failures: empty. Set
of unresolved routes (indeterminate, out_of_frame, invalid_basis, or no
result): empty. Required obligation set R = 23 routes; admitted coverage C =
23; uncovered coverage R minus C = 0.

Composite for FOUNDATIONS §3 Commitments: **satisfied**, carrying all 23
route results above and the nine actor-recorded residuals (R04, R09, R10,
R12, R15, R16, R18, R19, R20), none of which any actor treated as a
contradiction. The residuals survive the join and are listed again in §7.

## 5. Accounting

Per step actor, from `lifecycle.jsonl` and `steps/<id>.usage.json`. Context
tokens are input plus cache-creation plus cache-read as the headless CLI
reports them; cost is the CLI's list-basis `total_cost_usd`; model id
observed `claude-sonnet-5-5` on every step.

| Step | Bytes in (measured) | Input tok | Cache create | Cache read | Context tok | Output tok (of which thinking) | List cost USD | API ms |
|---|---|---|---|---|---|---|---|---|
| S01-P1 | 5,983 | 2 | 8,114 | 991 | 9,107 | 1,160 (493) | 0.0442582 | 7,159 |
| S02-P2 | 8,422 | 2 | 8,696 | 991 | 9,689 | 874 (474) | 0.0437262 | 6,350 |
| S03-P3 | 9,977 | 2 | 9,256 | 991 | 10,249 | 829 (493) | 0.0455162 | 8,133 |
| S04-P4a | 4,487 | 2 | 7,458 | 991 | 8,451 | 1,114 (595) | 0.0411742 | 10,300 |
| S05-P4b-ac | 11,199 | 2 | 9,910 | 991 | 10,903 | 729 (308) | 0.0471322 | 6,157 |
| S06-P4b-up | 12,996 | 2 | 10,138 | 991 | 11,131 | 854 (506) | 0.0492942 | 7,889 |
| S07-P5 | 5,891 | 2 | 8,084 | 991 | 9,077 | 1,325 (638) | 0.0457882 | 10,274 |
| S08-P6 | 11,091 | 2 | 9,671 | 991 | 10,664 | 1,085 (510) | 0.0497362 | 8,365 |
| Total | 70,046 | 16 | 71,327 | 7,928 | 79,271 | 7,970 (4,017) | 0.3666256 | 64,627 |

Totals for the run: 8 step-actor starts (of 30 allowed); 70,046 bytes
transferred into step actors; 79,271 context tokens plus 7,970 output tokens
= 87,241 step-actor tokens; list cost USD 0.3666; every step `is_error:
false`, `num_turns: 1`.

Framework overhead. The CLI adds a fixed context not subject to the cap. It
is observed, not measured in isolation: the 991 cache-read tokens are
identical on every step, and a least-squares fit of context tokens against
measured bytes over the eight steps gives context tokens = 7,127 + 0.3178
times bytes (about 3.15 bytes per token), so roughly 7,100 tokens per step
are overhead rather than step material. This is larger than CASE-2's
design-time note of about 2,300 on a trivial input; this run did not start a
trivial-input actor to measure it directly, since that would be a start that
serves no route. The estimate is derived, not measured.

Measurements that started no actor: 11 dry-run `measured` entries
(S00-closure, S00-closure7, D-P1, D-P2, D-P3, D-P4a, D-P4b, D-P5, D-P6,
D-P4b-ac, D-P4b-up), of which three were `refused` (S00-closure 50,557;
S00-closure7 49,948; D-P4b 20,364). The lifecycle log holds 38 lines: 19
`measured`, 3 `refused`, 8 `actor_started`, 8 `actor_ended`. No
`actor_started` follows a `refused` for the same step; every real step's
`measured` precedes its `actor_started` (E1).

Coordinator. The constructor's own consumption is an unverified counter:
the Claude Code harness budget reminder (`<total_tokens>` shown to the
constructor) read 15,000,000 at the first turn and 14,870,635 just before
this record was written, a decrement of 129,365, which excludes writing this
record. It is a harness budget counter, not a billed or cached-token count,
and no cost figure for the constructor is available from it.

Standing basis of the constructor, in bytes, reported once: CASE-2.md
12,920 + STEP_CARD.md 2,464 + FOUNDATIONS.md 15,218 + CALCULUS.md 15,242 +
EVALUATION.md 8,042 + projection 96,119 = 150,005 bytes as CASE-2 defines
the standing basis; 160,854 bytes including step_actor.py 8,377 and
fragment.py 2,472. Of the projection, the constructor's file reader returned
only the first 44,812 characters of 96,119; the remainder was not loaded and
was not needed for any decision in this run.

Wall time: `date -u` start `Sun 11 Oct 2026 13:15:30 UTC`, end
`Sun 11 Oct 2026 13:24:05 UTC` (8 minutes 35 seconds; the end stamp was
taken after the body of this record was written and before this line was
filled in). The eight actor starts span 13:17:55 to 13:19:20 UTC;
the first six ran concurrently, then the two P4b halves.

## 6. Stop state

satisfied. The declared predicate of this activation (23 route results in
the core algebra with step-actor evidence, one composite under the declared
rule, measurement before every read, no over-cap actor, the accounting and
this record) holds on the exact basis. No route is unresolved. The step
actors' outputs are candidates until the assessor evaluates them (P0,
candidate-until-evaluated premise); this record is construction output and
the constructor's self-review, not assessment (EVALUATION §3).

## 7. Residuals

1. Actor-recorded residuals, carried unchanged from §3: R04 (RF-008 is
   about frames, P1's example about contracts); R09 (P4a says "steps" for
   AC-016's "traversals", omits "exact", and does not restate AC-016's
   flattening and sequence sentences); R10 (RF-010 is frame composition, P4a
   is step composition; judged on criteria 1 and 2 only); R12 (the "nine
   statements" total is not checkable from AC-013 alone); R15 (UP-021 never
   uses the word conservation); R16 and R18 ("restated once in CALCULUS §3"
   was outside every step and was not judged); R19 (the totality rule says
   "should" and is scoped to semantic functions in design modules); R20
   (UP-008 is silent on authority). None was treated as a contradiction;
   each is an exactness or scope gap for the tenant author to dispose.
2. Unverified cross-section claim: P4b's "whose nine statements of
   conservation become one obligation with typed instances" relates all five
   cited sections. The only step that could hold them with P4b measures
   20,364 bytes and was refused. No route result depends on it under the
   card's per-route contract, but the claim itself is unassessed in this run.
3. CALCULUS §3 restatement claims (R16, R18): P5 says RF-012 and AC-007 are
   restated once in CALCULUS §3. CALCULUS §3 was outside every step's context
   by design (the card gives only FOUNDATIONS §3 paragraphs); the claim is
   not judged here.
4. Independence: step actors and constructor are one model family (Claude).
   The constructor's freshness requirement is met; assessor independence is
   not claimed and, by EVALUATION §3's default, does not hold for a Claude
   assessor.
5. Grouped steps: an actor holding several sections could in principle draw
   on a co-given section when judging another route. No actor's evidence
   line cites a section other than its route's own, but this record cannot
   prove the actors' internal paths (CALCULUS §1, not governed).
6. Commit identity: the launcher named `cee1157`; the constructor verified
   the four digests, not the commit, since git was prohibited.
7. Framework overhead is estimated by regression (about 7,100 tokens per
   step), not measured directly.

## 8. Handoff

A different actor can resume without this run's conversation from this
record, `lifecycle.jsonl` and `steps/`. Every path names the envelope under
which it is executable.

- Assessment (the next lawful move). Envelope: read-only access to this run
  directory at a named immutable identity (the tenant owner must commit it;
  this constructor did not), plus the two common sources named in CASE-2
  "Expectations owner" at input commit `80b46944f1c1`; no step-actor starts;
  an assessor outside the Claude family if independence is required. Record
  expectations from the common sources first, then evaluate E1 to E5 against
  `lifecycle.jsonl` (E1, E2, E4), `steps/*.out.md` and this file (E4, E5);
  return a review per EVALUATION §4; make no repair.
- Re-running any step. Envelope: cap 20,000 bytes, a fresh run directory,
  within a new run's allowance of 30 starts and 60 minutes; the rc.2 install
  at the path above and the four subject files at the digests above. Use
  exactly the `--para` and `--route` arguments of the step as logged in its
  `measured` entry (`paras`, `routes`), for example
  `python3 -I <tenant>/qualification/cases/T-01/step_actor.py --cap 20000 --run-dir <new run dir> --step-id S06-P4b-up --para P4b --route DESIGN_MODULE_METHOD.md:bounded-frame-conservation-stdo-up-017 --route SPEC_METHOD.md:complete-enclosing-relation-admission-stdo-up-021`.
  Every step in this partition measured at or below 12,996 bytes and is
  executable under the 20,000-byte cap.
- Disposing residual 2 (the P4b nine-statements claim). Not executable
  under the 20,000-byte envelope: the step needs 20,364 bytes. Executable
  only under an enlarged envelope of at least 20,364 bytes (a cap of 20,500
  leaves margin for a longer step id), which re-enters the owner of the
  envelope (CALCULUS §2.3; the case author or Jim); the command is the D-P4b
  dry run with `--cap 20500` and without `--dry-run`. Alternatively the
  claim can be reframed as five per-section counts joined by a declared
  conjunction, which needs a changed step card (a counting contract) and so
  also re-enters the case author. Neither is executable by a constructor
  under this case as written.
- Disposing residuals 1 and 3 (tenant wording exactness; CALCULUS §3
  restatement). Envelope: the tenant author's ordinary editing grant on
  `standards/FOUNDATIONS.md` and `standards/CALCULUS.md`; any change creates
  a new subject with new digests and invalidates this run's route results
  for the changed paragraphs (CALCULUS §7).
- Run B2 (cap 8,000). Envelope: a new run directory and allowance. From the
  measurements here, R12 (AC-013, section 6,411 bytes), R15 (UP-021, 5,914)
  and R21 (UP-022, 5,343) each exceed 8,000 once the card (2,464), system
  line (182), paragraph and header are added, so those routes must return
  out_of_frame or an escalation with the measured size; every other
  single-route step fits; the composite cannot be satisfied.

## 9. What the constructor did and did not do

Did: read CASE-2.md, STEP_CARD.md, step_actor.py, fragment.py, FOUNDATIONS.md,
CALCULUS.md and EVALUATION.md in full (the in-scope sections are CALCULUS
§1-3 and EVALUATION §1-4; the files were returned whole), and the first
44,812 characters of the projection; verified the four digests; measured the
23 section sizes with `fragment.py --size`; ran 11 dry measurements and 8
real steps through the instrument; read `lifecycle.jsonl`, the eight
`.out.md` and the eight `.usage.json` files; wrote this file.

Did not: read any rc.2 section text by any route (no `--text`, no cat of
rc.2 members, no `steps/<id>.in.md`); follow any link out of CASE-2.md;
read CASE.md, `received/`, other runs, reviews, design, RETURNS.md or any
other tenant file; modify the instrument or anything outside this run
directory; use git; start any actor outside the instrument; re-judge or
alter any step actor's output.
