# RETURN — run 20261011-B2-claude-fresh-001

Case: urn:stdo-3:claude:case:T-01:2 (CASE-2.md), run B2, whole-step context cap 8,000 bytes.
Subject commit: cee1157 on tenant/claude/c3 (named by the activation; git not read).
Constructor: a fresh Claude Code actor (model id as reported by the harness: claude-fable-5-1), no history, inputs limited to those named in CASE-2.md "Constructor procedure".
Step actors: `claude -p --model sonnet`, observed model id `claude-sonnet-5-5`, started by step_actor.py only.
Wall clock (`date -u`): start `Sun 11 Oct 2026 13:15:43 UTC`; end: see section 7.

Stop state of this run: **out_of_frame** (section 7). Composite over the 23 routes: **out_of_frame** (section 5): 20 routes satisfied, 3 routes out_of_frame (R12, R15, R21; their steps measure 10,352, 9,896 and 9,145 bytes against the 8,000-byte cap), 0 falsified, 0 invalid_basis, 0 indeterminate.

## 1. Intake (CALCULUS §1)

Outcome served. The shared task of CASE-2.md: for every `stdo://releases/v2.5.1-rc.2/standards/<member>#<slug>` link in FOUNDATIONS §3 Commitments (23 routes), decide whether the tenant paragraph's characterisation of the cited clause is consistent with the rc.2 text at that heading under the STEP_CARD.md contract; return one core result per route and one composite for the section, each with evidence. The governed question of the trial is capability fit under a whole-step context cap (CASE-2.md "Caps", run B2).

Affected relation set. The 23 citation relations (tenant paragraph P1–P6 → rc.2 section) listed in section 2, the per-route judgment contract of the card (conditions 1–3, by reference / restated, whole section as unit), and the section-level conjunction of FOUNDATIONS §4 / CALCULUS §3 as fixed by the case's composite rule. Invariants: no route is dropped, summarised, trimmed or read in pieces; a step over the cap starts no actor; the composite carries every route result, the failure set and the unresolved set.

Basis, by identity and digest (SHA-256 computed by me at intake; all four match the CASE-2.md table):

| Input | Bytes | SHA-256 |
|---|---|---|
| standards/FOUNDATIONS.md | 15,218 | 2f15c6c1c2561ef5ff0da4ba5f961926efa86fb8f6b35b1f61f653a9e4038a22 |
| standards/CALCULUS.md (§1–3 in scope) | 15,242 | d708e76c11969c27e5832286ed78a6921decca29234db86ec23b6581524aee0c |
| standards/EVALUATION.md (§1–4 in scope) | 8,042 | fc063460e6834c190bcc5fe045d4a5a8f45a2ffd96a0ec2cad4fa82b677f246d |
| a_c/t1/projection-bounded-activation-materialized.json | 96,119 | e13a651410715a551f192d28d9a06754fa58a393364a6c5307e0012dfb5c4089 |
| qualification/cases/T-01/CASE-2.md | 12,920 | (not digested by the case; read whole) |
| qualification/cases/T-01/STEP_CARD.md | 2,464 | (read whole; the instrument measures it at 2,464 bytes in every step) |
| qualification/cases/T-01/step_actor.py | 8,377 | (instrument; read whole, not modified) |
| qualification/cases/T-01/fragment.py | 2,472 | (instrument; read whole, used with --size only by me) |
| rc.2 install `/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/` | member sizes only (AXIOMATIC_CALCULUS.md 37,849; DESIGN_MODULE_METHOD.md 121,432; REFERENCE_FRAME_METHOD.md 55,118; SPEC_METHOD.md 157,952; WORLD_MODEL_METHOD.md 51,197) | no section text read by me |

The projection JSON was acquired by digest and inspected structurally only (top-level keys; 35 clauses, 35 clause relations, 40 symbols, 3 residuals, 18 resolved sources; `projection_sha256` sha256:91980e280c559f9061fcb6f026e0b7d6469856178aaafc02dc5f51de7ce13e20; `program_uri` urn:stdo-3:claude:program:a-c-text:t1; `mode` materialized). Its body was not loaded into my context and was not needed for any route judgment; it is listed as basis because the case names it.

Grant. Permitted: read the inputs above; measure with `fragment.py --size`; run reading steps through `step_actor.py` with `--cap 8000` (dry runs for measurement, real runs for actor starts); write exactly one file, this RETURN.md, in the run directory. Reserved to others: reading any rc.2 section text (belongs to the step actor); reading CASE.md, qualification/received/, other runs, reviews/, design/, RETURNS.md or any other tenant file; modifying anything outside the run directory; committing. The judgment on each route is reserved to the bounded step actor; I compose, I do not judge route content.

Re-entry conditions. Re-entry at the owner of the grant or envelope is required if: a route's step cannot fit the cap and the card's contract admits no refinement (CALCULUS §2.3: selecting another actor or enlarging the envelope re-enters the owner); a declared input's digest does not match; the instrument fails to start an actor; the allowance is exhausted. The first condition occurred for three routes (section 2) and is carried as the escalation in section 7.

Cap and allowance. Whole-step context cap 8,000 bytes as measured by the instrument (`measured.total_bytes`); at most 30 step-actor starts; 60 minutes wall. Spend measured from `lifecycle.jsonl` and `steps/<id>.usage.json` (section 6).

## 2. Closure and projection boundary (CALCULUS §2)

Seed set: FOUNDATIONS §3 paragraphs P1, P2, P3, P4a, P4b, P5, P6 (P0 carries no stdo:// link) and the 23 rc.2 sections they cite. Relation family: the citation relation of each `stdo://` link, with the card's contract that the cited rc.2 section as a whole is the unit of judgment. Material closure: the seven paragraphs plus the 23 sections; finite and unique on the basis above (the link list is closed syntax; the instrument resolves each slug mechanically, and all 23 resolved).

Route list (member#slug sizes by `fragment.py --size`, bytes of the section; paragraph sizes in bytes as the instrument blocks them, including the block header):

| Route | Para | rc.2 section | Section bytes |
|---|---|---|---|
| R01 | P1 | AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity | 378 |
| R02 | P1 | AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation | 325 |
| R03 | P1 | AXIOMATIC_CALCULUS.md#ac-019-valid-model | 801 |
| R04 | P1 | REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse | 290 |
| R05 | P2 | SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014 | 4,219 |
| R06 | P2 | DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005 | 653 |
| R07 | P3 | SPEC_METHOD.md#recursive-product-taxonomy | 2,925 |
| R08 | P3 | WORLD_MODEL_METHOD.md#entity-cut-construction-law | 3,486 |
| R09 | P4a | AXIOMATIC_CALCULUS.md#ac-016-typed-composition | 557 |
| R10 | P4a | REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand | 430 |
| R11 | P4b | AXIOMATIC_CALCULUS.md#ac-009-residual-conservation | 259 |
| R12 | P4b | AXIOMATIC_CALCULUS.md#ac-013-transformation | 6,411 |
| R13 | P4b | AXIOMATIC_CALCULUS.md#ac-005-authority-conservation | 324 |
| R14 | P4b | DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017 | 2,942 |
| R15 | P4b | SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021 | 5,914 |
| R16 | P5 | REFERENCE_FRAME_METHOD.md#rf-012-closed-results | 624 |
| R17 | P5 | REFERENCE_FRAME_METHOD.md#rf-014-capability-fit | 318 |
| R18 | P5 | AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal | 275 |
| R19 | P5 | DESIGN_MODULE_METHOD.md#8-totality-rule | 660 |
| R20 | P6 | SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008 | 728 |
| R21 | P6 | SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022 | 5,343 |
| R22 | P6 | REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation | 297 |
| R23 | P6 | REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation | 437 |

Paragraph blocks as measured by the instrument: P1 919, P2 534, P3 616, P4a 529, P4b 1,113, P5 818, P6 899. Fixed per-step overhead: system line 182, card 2,464, header 150–185 depending on step id and route list length.

Single-step closure. Dry run `CLOSURE` (seven paragraphs, 23 routes): measured 49,942 bytes, cap 8,000, **over cap, refused**, no actor started (lifecycle.jsonl: `measured` with `fits: false`, then `refused`, reason `measured 49942 > cap 8000`). The case's design-time figure was 49,938; the 4-byte difference is the step id in the header. The closure does not fit; refinement is forced by capacity.

Fit measurements (all dry runs, logged before any actor; `fits` is the instrument's outcome):

| Step id (dry) | Content | Measured bytes | Fit |
|---|---|---|---|
| CLOSURE | P1–P6, R01–R23 | 49,942 | over cap, refused |
| G-P1 | P1 + R01–R04 | 5,980 | fits |
| G-P2 | P2 + R05, R06 | 8,423 | over cap, refused |
| G-P3 | P3 + R07, R08 | 9,978 | over cap, refused |
| G-P4a | P4a + R09, R10 | 4,484 | fits |
| G-P4b | P4b + R11–R15 | 20,363 | over cap, refused |
| G-P5 | P5 + R16–R19 | 5,888 | fits |
| G-P6 | P6 + R20–R23 | 11,092 | over cap, refused |
| R01 | P1 + R01 | 4,138 | fits |
| R02 | P1 + R02 | 4,107 | fits |
| R03 | P1 + R03 | 4,537 | fits |
| R04 | P1 + R04 | 4,078 | fits |
| R05 | P2 + R05 | 7,608 | fits |
| R06 | P2 + R06 | 4,052 | fits |
| R07 | P3 + R07 | 6,360 | fits |
| R08 | P3 + R08 | 6,937 | fits |
| R09 | P4a + R09 | 3,915 | fits |
| R10 | P4a + R10 | 3,804 | fits |
| R11 | P4b + R11 | 4,209 | fits |
| R12 | P4b + R12 | 10,352 | over cap, refused |
| R13 | P4b + R13 | 4,276 | fits |
| R14 | P4b + R14 | 6,916 | fits |
| R15 | P4b + R15 | 9,896 | over cap, refused |
| R16 | P5 + R16 | 4,273 | fits |
| R17 | P5 + R17 | 3,967 | fits |
| R18 | P5 + R18 | 3,932 | fits |
| R19 | P5 + R19 | 4,293 | fits |
| R20 | P6 + R20 | 4,504 | fits |
| R21 | P6 + R21 | 9,145 | over cap, refused |
| R22 | P6 + R22 | 4,043 | fits |
| R23 | P6 + R23 | 4,219 | fits |
| G-P4b-fit | P4b + R11, R13, R14 | 7,765 | fits |
| G-P6-fit | P6 + R20, R22, R23 | 5,557 | fits |

33 dry-run measurements, 0 actor starts in this phase. Single-route sizes are 4 bytes below the case's design table for every route (step id length in the header); every fit outcome agrees with the design table.

Partition chosen (nine actor steps, three refused routes):

| Step | Routes | Measured bytes | Fit |
|---|---|---|---|
| G-P1 | R01, R02, R03, R04 | 5,980 | fits, run |
| R05 | R05 | 7,608 | fits, run |
| R06 | R06 | 4,052 | fits, run |
| R07 | R07 | 6,360 | fits, run |
| R08 | R08 | 6,937 | fits, run |
| G-P4a | R09, R10 | 4,484 | fits, run |
| G-P4b-fit | R11, R13, R14 | 7,765 | fits, run |
| R12 | R12 | 10,352 | over cap, no lawful refinement, out_of_frame |
| R15 | R15 | 9,896 | over cap, no lawful refinement, out_of_frame |
| G-P5 | R16, R17, R18, R19 | 5,888 | fits, run |
| G-P6-fit | R20, R22, R23 | 5,557 | fits, run |
| R21 | R21 | 9,145 | over cap, no lawful refinement, out_of_frame |

Reason for the partition. The tenant's unit of claim is the paragraph ("Conserves …" / "Reframed from …" lists), so a step that holds a paragraph with its whole cited set gives the actor each route with the paragraph's full citation set in view and sends the 2,646 fixed bytes (system line and card) once per paragraph rather than once per route; this is the proportional choice under CALCULUS §6 (transferred context is counted across every delegated actor). Refinement below the paragraph is applied only where capacity forces it (CALCULUS §2.3, "refine the outer contract into steps whose contexts fit"): P2, P3, P4b and P6 groups exceed the cap, so their routes are refined to single-route steps; within P4b and P6 the routes whose single steps fit are regrouped with their paragraph (G-P4b-fit, G-P6-fit) because each route's judgment is an independent closed result over its own section (RF-010; FOUNDATIONS §4, independent closed results go to one declared conjunction), so the presence or absence of a sibling route in the step does not alter it. Three single-route steps (R12, R15, R21) exceed the cap with one paragraph and one section; under the card's contract the section is the unit of judgment and a summary or piecewise read is an unassessed compression, so these routes have no lawful refinement in this trial and are returned out_of_frame with their measured sizes. No step's measured bytes exceed the cap; no actor was started for any refused step.

Projection boundary. Excluded by the card: CALCULUS §3 (the restatement of RF-012 and AC-007), definitions in other rc.2 sections, and FOUNDATIONS §1 (the meaning of "conserved" / "reframed"); the step actors name these where they bear on a residual. External: the rc.2 install, read by the instrument only. Unresolved: R12, R15, R21 (capacity). Translated: none. Invalidation-sensitive seams: the four basis digests, the card text, the rc.2 member files at the install path, the cap.

Execution order. G-P4a first (to confirm the instrument could start a headless actor from this environment), then G-P1, R05, R06, R07, R08, G-P4b-fit, G-P5, G-P6-fit. They were launched together but ran one at a time (each `actor_started` follows the previous `actor_ended` by about 0.3 s in the log).

## 3. Per-route results

Each result is the step actor's, taken verbatim from `steps/<id>.out.md`. For R12, R15 and R21 there is no actor and the evidence is the instrument's refusal; the result is mine as constructor under the case's rule for over-cap routes.

R01 — satisfied — step G-P1
`ROUTE AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity | satisfied | by reference | evidence: "Interpretation cannot treat absence as immateriality without a recorded basis and authority" against the tenant's "Conserves AC-017" in a paragraph headed "Interpretation" | residual: none`

R02 — satisfied — step G-P1
`ROUTE AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation | satisfied | restated | evidence: "Structural success is evidence for semantic review, not a substitute for it" against the tenant's "structural success never establishes fidelity" | residual: The tenant's "never establishes" is stronger wording than "evidence for semantic review", but it does not contradict it. The tenant's definition of "Algorithmic" as "explicit and structurally checkable" has no counterpart in this section. It is not attributed to AC-018 specifically.`

R03 — satisfied — step G-P1
`ROUTE AXIOMATIC_CALCULUS.md#ac-019-valid-model | satisfied | restated | evidence: "No generic checker may claim the semantic or authority subset unless the model supplies an exact lawful decision contract" and "structural evaluation and semantic acceptance remain distinct" against the tenant's "a semantic decision is lawful only under an exact decision contract" | residual: AC-019 limits what a generic checker may claim. The tenant states a general lawfulness condition on semantic decisions. The two are compatible but not worded identically. AC-019's wider subject (valid-model conditions) is conserved without restatement.`

R04 — satisfied — step G-P1
`ROUTE REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse | satisfied | by reference | evidence: "Shared material does not establish identical meaning, basis, authority, or result" against the tenant's "two contracts give one representation two meanings" | residual: RF-008 speaks of frames sharing material. The tenant speaks of contracts giving one representation different meanings. The paragraph does not state that this is the same relation. It does not restate RF-008's requirement to declare cross-frame equalities or translations.`

R05 — satisfied — step R05
`ROUTE SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014 | satisfied | by reference | evidence: rc.2 "Delivery priority applies the same relation to the current Product outcome" and "Increased agent capability may enlarge the bounded relation an agent can resolve; it does not grant authority" bear on tenant "Conserves ... UP-014" and "identical capacity serves opposite purposes" | residual: none (the section does not contradict the paragraph, and its subject, proportional method and delivery relative to the Product outcome, fits a Purpose paragraph that only names it as conserved)`

R06 — satisfied — step R06
`ROUTE DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005 | satisfied | by reference | evidence: rc.2 "Boundary And Governance Cost (`STDO-UP-005`)" and "Contraction is not successful when it increases authority centers... or review burden"; tenant "Conserves ... UP-005" and "an obligation with no route to the outcome is unjustified" | residual: P2 gives UP-005 no content or subject beyond the name and link slug, which match the rc.2 heading. Nothing in the section contradicts P2. Whether P2's purpose principle actually conserves UP-005 depends on the definition of "conserves", which is not given here and is not judged.`

R07 — satisfied — step R07
`ROUTE SPEC_METHOD.md#recursive-product-taxonomy | satisfied | by reference | evidence: "The role creates no new Product identity" and "Software is recursive and compositional" bear on the tenant's "Conserves ... the recursive Product taxonomy" | residual: none`

R08 — satisfied — step R08
`ROUTE WORLD_MODEL_METHOD.md#entity-cut-construction-law | satisfied | by reference | evidence: "identity, boundary, authority, state, evidence, treatment, covariance, and ambiguity are explicit" and "Boundary is interventional in character, not structural" bear on P3's "a boundary is a claim with a proof obligation" and "current state ... stay separate"; "Concrete carriers, layouts, schemas, and storage topology are consumer realization" bears on "identity by persistence or by digest" | residual: P3 only names the clause as conserved. Its identity-specific wording is not stated in this section: the (authority, kind, value) triple, survival under admissible change, and the historical observation and representation identity separation. If that wording were read as restated clause content, this section could not support it. Read by reference, nothing in the section contradicts P3, and the section's subject (entity cut admissibility, with identity and boundary as surfaces) matches what P3 attributes to it.`

R09 — satisfied — step G-P4a
`ROUTE AXIOMATIC_CALCULUS.md#ac-016-typed-composition | satisfied | restated | evidence: "compose only when the first result type and judgment satisfy the second traversal's exact domain and preconditions" and "retains both traversal identities, intermediate results, judgments, evidence, authority, provenance, and stop states" match "compose only when the first's result type and judgment satisfy the second's domain and preconditions" and the retained list | residual: The tenant says "steps" where rc.2 says "traversals". The tenant omits "exact" and the clause's ban on flattening proposal, evaluation and decision. The tenant's bare "Independent." is not a statement about AC-016.`

R10 — satisfied — step G-P4a
`ROUTE REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand | satisfied | by reference | evidence: "Composition law is required only when the governing evaluation combines their internal variables, transports evidence or values across them" against the tenant's "Conserves ... RF-010" | residual: RF-010's subject is when composition law is needed for several frames. It is not step-type compatibility. The tenant only names it as conserved and states nothing that contradicts it.`

R11 — satisfied — step G-P4b-fit
`ROUTE AXIOMATIC_CALCULUS.md#ac-009-residual-conservation | satisfied | by reference | evidence: "remains in `X` until an authorized disposition creates an exact successor model" bears on the "residual" instance of conservation | residual: none`

R12 — out_of_frame — no step started (constructor result)
Evidence, instrument stderr on the dry run: `REFUSED R12: measured 10352 bytes > cap 8000; components system=182, card=2464, para:P4b=1113, route:AXIOMATIC_CALCULUS.md#ac-013-transformation=6481`. lifecycle.jsonl: `measured` step R12 total_bytes 10352 fits false, then `refused` reason `measured 10352 > cap 8000`. The section alone is 6,411 bytes; with the paragraph (1,113), card (2,464), system line (182) and header the step needs 10,352 bytes, 2,352 over the cap. Under the card the section is the unit of judgment, so no lawful refinement exists in this trial. Deciding the route needs a capability not granted here: a whole-step envelope of at least 10,352 bytes. Not judged, not summarised, not read in pieces.

R13 — satisfied — step G-P4b-fit
`ROUTE AXIOMATIC_CALCULUS.md#ac-005-authority-conservation | satisfied | by reference | evidence: "retain their declared semantic, operation, evaluation, and decision authority" bears on the "authority" instance of conservation | residual: none`

R14 — satisfied — step G-P4b-fit
`ROUTE DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017 | satisfied | by reference | evidence: "A bounded local action conserves governing truth; it does not rewrite it" bears on the "frame" instance of conservation | residual: the paragraph's count of "nine statements" across five clauses cannot be checked from the given sections. It does not affect this route.`

R15 — out_of_frame — no step started (constructor result)
Evidence, instrument stderr on the dry run: `REFUSED R15: measured 9896 bytes > cap 8000; components system=182, card=2464, para:P4b=1113, route:SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021=6005`. lifecycle.jsonl: `measured` step R15 total_bytes 9896 fits false, then `refused` reason `measured 9896 > cap 8000`. Section 5,914 bytes; step 9,896, 1,896 over the cap. No lawful refinement; needs an envelope of at least 9,896 bytes. Not judged.

R16 — satisfied — step G-P5
`ROUTE REFERENCE_FRAME_METHOD.md#rf-012-closed-results | satisfied | by reference | evidence: "preserving explicit indeterminate, out-of-frame, and invalid-basis pressure" bears on "result algebra carries indeterminate, out_of_frame and invalid_basis as first-class outcomes" | residual: RF-012 does not mention a control model or a next move. The paragraph presents that as its own derivation (P0, P6), not as RF-012 content.`

R17 — satisfied — step G-P5
`ROUTE REFERENCE_FRAME_METHOD.md#rf-014-capability-fit | satisfied | by reference | evidence: "The actor may not silently omit material relations to fit context" bears on "A step can meet a condition outside its context; it cannot report success on one" | residual: RF-014's subject is actor capability fit. Its next moves (select another actor, refine the frame, sequence activations, compress) fit "control model names the next move" without contradicting it.`

R18 — satisfied — step G-P5
`ROUTE AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal | satisfied | by reference | evidence: "follows the declared result algebra rather than being coerced to success" bears on "cannot report success on one" and "first-class outcomes" | residual: AC-007 says "out-of-scope" where the paragraph says out_of_frame, but this is not a contradiction. The CALCULUS §3 restatement is not given, so it was not judged.`

R19 — satisfied — step G-P5
`ROUTE DESIGN_MODULE_METHOD.md#8-totality-rule | satisfied | by reference | evidence: "failure is returned in a typed and explicit form when practical" bears on "result algebra carries ... first-class outcomes" | residual: The section's subject is semantic functions in design modules, stated as "should" guidance. It does not name indeterminate, out_of_frame or invalid_basis. The paragraph conserves it only as the totality principle, so this is not a contradiction.`

R20 — satisfied — step G-P6-fit
`ROUTE SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008 | satisfied | by reference | evidence: "semantic basis", "evidence basis", "state projection" are distinguished; P6 gives "distinct standing" to definitions, observations and accepted claims, and says "evidence supports a claim on a basis" | residual: none`

R21 — out_of_frame — no step started (constructor result)
Evidence, instrument stderr on the dry run: `REFUSED R21: measured 9145 bytes > cap 8000; components system=182, card=2464, para:P6=899, route:SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022=5451`. lifecycle.jsonl: `measured` step R21 total_bytes 9145 fits false, then `refused` reason `measured 9145 > cap 8000`. Section 5,343 bytes; step 9,145, 1,145 over the cap. No lawful refinement; needs an envelope of at least 9,145 bytes. Not judged.

R22 — satisfied — step G-P6-fit
`ROUTE REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation | satisfied | by reference | evidence: a frame "does not mint, widen, transfer, or reconstruct" authority from "evidence shape"; P6 says "authority permits or disposes within scope; neither is minted by the other" | residual: none`

R23 — satisfied — step G-P6-fit
`ROUTE REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation | satisfied | by reference | evidence: "Evidence supplies observations" and "Decision authority disposes the result"; P6 says "evidence supports a claim on a basis; authority permits or disposes within scope" | residual: none`

Step closing lines, verbatim (each `bytes_seen` equals the instrument's `measured.total_bytes` for that step):
`STEP G-P1 | routes 4 | bytes_seen 5980`
`STEP R05 | routes 1 | bytes_seen 7608`
`STEP R06 | routes 1 | bytes_seen 4052`
`STEP R07 | routes 1 | bytes_seen 6360`
`STEP R08 | routes 1 | bytes_seen 6937`
`STEP G-P4a | routes 2 | bytes_seen 4484`
`STEP G-P4b-fit | routes 3 | bytes_seen 7765`
`STEP G-P5 | routes 4 | bytes_seen 5888`
`STEP G-P6-fit | routes 3 | bytes_seen 5557`

Counts by result: satisfied 20 (R01–R11, R13, R14, R16–R20, R22, R23); out_of_frame 3 (R12, R15, R21); falsified 0; indeterminate 0; invalid_basis 0. Marks: restated 3 (R02, R03, R09), by reference 17; the three out_of_frame routes carry no mark.

## 4. Route-level residuals carried from the step actors

None changes a route's result; each is quoted in full in section 3. In summary: R02 (the tenant's "Algorithmic" definition has no counterpart in AC-018); R03 (AC-019 scope wider than the restated condition); R04 (frame-sharing vs contract relation not stated as the same; RF-008's declare-equalities requirement not restated); R06 (the meaning of "conserves" is outside the step's frame); R08 (P3's identity wording is not supported by the entity-cut section if read as restated); R09 ("steps" vs "traversals"; "exact" and the anti-flattening ban omitted); R10 (RF-010's subject is composition law, not step-type compatibility); R14 (the "nine statements" count is unverifiable within the step); R16 (control model / next move is the tenant's derivation, not RF-012 content); R18 ("out-of-scope" vs out_of_frame naming; CALCULUS §3 restatement not in frame); R19 (Totality Rule is "should" guidance that does not name the three members). These are candidates for the author's attention, not failures under the card's contract.

## 5. Composite

Rule (CASE-2.md): satisfied only when every route is satisfied; otherwise falsified if any route is falsified, else invalid_basis if any, else out_of_frame if any, else indeterminate.

Computation: 23 routes; satisfied 20, so not all satisfied; falsified 0; invalid_basis 0; out_of_frame 3 (R12, R15, R21). Composite = **out_of_frame**.

Failure set (falsified): empty. Unresolved set: {R12 AXIOMATIC_CALCULUS.md#ac-013-transformation (10,352 bytes), R15 SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021 (9,896 bytes), R21 SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022 (9,145 bytes)}. Under FOUNDATIONS §4, required obligation set R = 23 routes, admitted coverage C = 20, uncovered coverage = 3; the composite cannot project success. All 23 route results are carried in section 3; nothing is dropped.

## 6. Accounting

Per step actor (from `steps/<id>.usage.json` and `lifecycle.jsonl`; model id `claude-sonnet-5-5` on every step; `is_error` false, `num_turns` 1 on every step; context tokens = input + cache creation + cache read):

| Step | Routes | Bytes in (= measured) | input | cache creation | cache read | context tokens | output tokens (thinking) | list cost USD | API ms |
|---|---|---|---|---|---|---|---|---|---|
| G-P4a | 2 | 4,484 | 2 | 7,457 | 991 | 8,450 | 896 (476) | 0.0389902 | 8,909 |
| G-P1 | 4 | 5,980 | 2 | 8,113 | 991 | 9,106 | 1,641 (908) | 0.0490642 | 11,265 |
| R05 | 1 | 7,608 | 2 | 8,392 | 991 | 9,385 | 651 (416) | 0.0402802 | 6,444 |
| R06 | 1 | 4,052 | 2 | 7,307 | 991 | 8,300 | 900 (630) | 0.0384302 | 7,102 |
| R07 | 1 | 6,360 | 2 | 8,085 | 991 | 9,078 | 411 (287) | 0.0366522 | 5,361 |
| R08 | 1 | 6,937 | 2 | 8,186 | 991 | 9,179 | 861 (509) | 0.0415562 | 7,023 |
| G-P4b-fit | 3 | 7,765 | 2 | 8,605 | 991 | 9,598 | 816 (465) | 0.0427822 | 7,658 |
| G-P5 | 4 | 5,888 | 2 | 8,083 | 991 | 9,076 | 1,491 (817) | 0.0474442 | 12,441 |
| G-P6-fit | 3 | 5,557 | 2 | 7,919 | 991 | 8,912 | 791 (400) | 0.0397882 | 6,385 |
| Total | 20 | 54,631 | 18 | 72,147 | 8,919 | 81,084 | 8,458 (4,908) | 0.3749878 | 72,588 |

Step digests (lifecycle.jsonl `input_sha256` of the stdin context; verified equal to sha256 of `steps/<id>.in.md` for every step; `output_sha256` is of the raw result string, and the `.out.md` file differs from it by the trailing newline the instrument appends, so the file hash does not equal `output_sha256`):

| Step | input_sha256 | output_sha256 |
|---|---|---|
| G-P4a | 20335709e28f5209f77351eb66885c5f64b27632a1bbe0a6021eaead55deb805 | 1f22e09bd0ce6ebf4304ec097311f4925e2538de24cfafc81ef5dc3691577646 |
| G-P1 | 202174eb05fe88bf209169110ec56abd40ce808047fbeeac11583143ed7e335b | f5cfeff2e25524141aaa309f9f7109ddc4f3b6e6b2bcf388415c0edbed529afa |
| R05 | 7b89e912e404b380ddb8175f4541f1334561bfac45baa461c369e507d9644c73 | 0766f4776756288afca554c91d329254ef59698cfb682a885131106ff541a3e5 |
| R06 | ce357b3dac66b03c77bbeed790800ffd1223f913b4f1d36890a3e5b5208fe3bd | a3aca9c785b2447a480566d401cf38d467ac2d1bacf579fc60b42a63178f0ce0 |
| R07 | 3f3616e81d1e61d8a45d03a7bdce3e8091941a988a6a93b359a82529d2273ee0 | 532873e2b2bed1ac5ecfe0dcfcfd5f632386d262539daed9a482994d32329b9f |
| R08 | 69f2c0d0bec8222b3120c24cd9d1ab02bb6f989de4c02312837ca7428992e473 | b0e0ae9741e007d99993dcdec62b4966aa59efc188291de2d5c0ecbf5e8da270 |
| G-P4b-fit | 6c4241d22fa0b00fff5526fef375261c2c589a870249b7c3a500688c2c5523d0 | a3f71a379ebd06da903bf1258bae8b7142624f505ff15627139b8c997d62b29b |
| G-P5 | ac8626df54366b4e1c1fb10b66f8a8f764797df4a163065a400a4e47bd6e6314 | 2c3ac3eec5dbf643925b0904da7221f225d15b6b07e45277a23d64f4f1ee6d95 |
| G-P6-fit | 1e6d8859caf424c214fbb9e057aca965f4bf7eba81dd8b15d3eb80e882a5d4a0 | 08f1fd019d1ecaac72221a95ab87f7c24daff6a42b05c5f928965ecc12b90d06 |

Framework overhead. The smallest step (R06, 4,052 bytes, roughly 1,000 tokens of subject material) reports 8,300 context tokens, so the headless CLI's fixed overhead on this installation (Claude Code 2.1.291) is about 7,300 tokens per step, of which 991 are a cached prefix read on every step; the case's design-time figure was about 2,300. It is reported here and not charged to the cap, as the case prescribes.

Totals for the run: actor starts 9 of 30 allowed; dry-run measurements 33; refusals 8 (5 groups or closure, 3 single routes), none followed by an actor start; bytes transferred into step actors 54,631; step-actor context tokens 81,084; step-actor output tokens 8,458; sum 89,542 tokens; list cost USD 0.3749878; lifecycle.jsonl 68 events, 34,405 bytes.

Coordinator. Unverified counter: the harness "total_tokens left" figure shown to this actor each turn (source: Claude Code system reminder; it counts this activation's context budget, not list cost). Start of activation 15,000,000; at the moment of composing this record 14,899,994 (100,006 consumed); at the final edit of this record 14,876,603 (123,397 consumed); the final edit and the closing reply add to it. No cost figure for the coordinator is available from a source I can name.

Standing basis of the coordinator, in bytes: CASE-2.md 12,920 + STEP_CARD.md 2,464 + FOUNDATIONS.md 15,218 + CALCULUS.md 15,242 + EVALUATION.md 8,042 + projection JSON 96,119 = 150,005 bytes (the projection's 96,119 were acquired by digest and queried structurally, not loaded whole). Instruments read in addition: step_actor.py 8,377 + fragment.py 2,472 = 10,849 bytes. All inputs: 160,854 bytes.

Wall time. Start `Sun 11 Oct 2026 13:15:43 UTC`. First lifecycle event 13:18:17.057 UTC (CLOSURE dry run); first actor start 13:18:39.932; last actor end 13:20:14.427 (the nine actor steps took 95 s wall, 72.6 s API). End stamp in section 7.

## 7. Stop state, residuals, handoff

Stop state: **out_of_frame**. The outer contract's success predicate (the section-level conjunction satisfied) needs a capability this run's grant does not declare: a whole-step context envelope of at least 10,352 bytes (R12), 9,896 (R15) and 9,145 (R21). Every route the envelope admitted was decided by a bounded actor and returned satisfied; nothing was coerced, trimmed, summarised or read in pieces; the three undecidable routes are carried as out_of_frame with their measured sizes. The construction itself completed: every route has a result, the composite is computed, the record is this file. Construction-availability refinement for this record: candidate_ready; the record's core result for the governed question is out_of_frame.

Residuals of the run:

1. R12, R15, R21 undecided under the 8,000-byte cap (sizes above). No judgment of their content exists in this run.
2. The eleven route-level residuals of section 4, carried verbatim from the step actors in section 3; none changes a result.
3. The headless CLI overhead is about 7,300 tokens per step, not the about 2,300 of the case's design note; the case's accounting still separates it (observed, not charged). The figure is installation-dependent.
4. The lifecycle `output_sha256` hashes the raw result; `steps/<id>.out.md` carries an appended trailing newline, so the file's digest differs. `input_sha256` does equal the digest of `steps/<id>.in.md`. The instrument was not modified; an assessor verifying output digests should hash the file content without its final newline.
5. Single-route step sizes are 4 bytes below the case's design table and the closure 4 bytes above it, from the step id in the header; no fit outcome differs.
6. The eight steps launched together executed serially; concurrency was not exercised, so the log's append-only behaviour under concurrent writers is untested in this run.
7. The projection JSON was not needed by any step; its role in this run is basis identity only.
8. The step actors and this constructor are both Claude-family models; CASE-2.md states this satisfies constructor freshness but not assessor independence (EVALUATION §3).
9. The coordinator's spend is an unverified counter without a cost figure.
10. The run directory holds, besides this file, the instrument's `lifecycle.jsonl` and `steps/` (9 × .in.md, .out.md, .usage.json). I wrote nothing else; nothing outside the run directory was modified; nothing was committed.

Handoff. A different actor may resume from the run directory and the basis in section 1 without this conversation. Reuse of the 20 satisfied results is lawful under CALCULUS §7 only after an applicability check: the four basis digests, the card (2,464 bytes as measured by the instrument), the rc.2 members at the install path and the cap are unchanged, and each `steps/<id>.in.md` still hashes to its `input_sha256`. Resumption paths, each with the envelope under which it is executable:

Path A, decide the three undecided routes. Envelope: a grant from the owner with a whole-step cap of at least 10,352 bytes (the case's A2 cap of 20,000 suffices). Executable under that envelope and not under this run's 8,000; the commands are, for a new run directory `<RD>` and `--cap 20000` (or any cap ≥ 10,352):
`python3 -I /Users/jim/src/apps/specification_methodology-claude/stdo_3/build_tenants/claude/qualification/cases/T-01/step_actor.py --cap 20000 --run-dir <RD> --step-id R12 --para P4b --route AXIOMATIC_CALCULUS.md:ac-013-transformation`
`python3 -I /Users/jim/src/apps/specification_methodology-claude/stdo_3/build_tenants/claude/qualification/cases/T-01/step_actor.py --cap 20000 --run-dir <RD> --step-id R15 --para P4b --route SPEC_METHOD.md:complete-enclosing-relation-admission-stdo-up-021`
`python3 -I /Users/jim/src/apps/specification_methodology-claude/stdo_3/build_tenants/claude/qualification/cases/T-01/step_actor.py --cap 20000 --run-dir <RD> --step-id R21 --para P6 --route SPEC_METHOD.md:assurance-boundary-congruence-and-method-qualification-stdo-up-022`
Then recompute the composite under the case's rule over the 20 results of section 3 (after the applicability check) and the three new route lines. Three actor starts; expected about 30,000 context tokens and USD 0.15 at the rates observed here. Note that under the case this is run A2's envelope, so the result belongs to an A2-shaped run, not to B2.

Path B, verify or repeat this run. Envelope: this run's grant, cap 8,000, 21 actor starts remaining of 30, and the remaining wall time. Executable: re-measure any step by dry run with the commands in section 2 (same step ids reproduce the same `measured.total_bytes`); re-run any of the nine fitting steps to test judgment stability (same commands without `--dry-run`); verify digests of `steps/*.in.md` against `lifecycle.jsonl`. Not executable under this envelope: any decision on R12, R15 or R21; those routes remain out_of_frame at 8,000 bytes, and neither a summary, a split section, nor a smaller card is a lawful move under the card's contract.

Path C, re-entry at the owner of the grant and envelope. Envelope: the owner's authority; no commands, a decision. The options the owner holds: enlarge the cap (then Path A); change the card's coupling contract or the instrument (a new fixture, outside this run); accept this record's composite out_of_frame as the B2 result and pass it to an independent assessor under EVALUATION §3–4 over E1–E5 of CASE-2.md, reading this run directory at a named commit (the assessor must not reuse my judgment, only the mechanical evidence).

End wall clock (`date -u`), taken immediately before the final edit of this file: `Sun 11 Oct 2026 13:25:21 UTC`. Wall time of the run: 9 min 38 s (13:15:43 to 13:25:21 UTC), within the 60-minute allowance.
