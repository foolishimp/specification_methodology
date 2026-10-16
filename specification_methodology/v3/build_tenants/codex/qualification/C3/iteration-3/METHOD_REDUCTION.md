# Method Consumer Reduction — Iteration 3

This is the method Writer's construction record under EC-CODEX-I3-01. It records
the reduction in SPEC_METHOD, TICKET_METHOD and RELEASE_METHOD, the source
relations it preserves, and candidates for subsequent independent challenge.
It is author evidence, not independent review or C3 acceptance. The earlier
design consultation was also an author contribution to this implementation.

## Exact basis and scope

- Consumer preimage: `3ad1fca31dc93ba0847bbbbf308312a554daa1f6`.
- Frozen shared core/design: `21c5191cca1f8a338359dc985492894209049ace`.
  The three consumer files at this cut were byte-identical to that preimage.
- Common input: `cae6fe366395148558efb84c85501b768f6593fc`.
- Writer selection: T-002-CODEX at main commit `169a9cf`, Execution Record's
  consumer-integration entry. The method Writer owns exactly the three method
  files and this reduction record; it has no shared-core or Git mutation grant.
- Installed builder: `stdo://releases/v2.5.1-rc.2/`, manifest SHA-256
  `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
- No peer source was acquired. No predecessor obligation is intentionally
  removed. The historical evidence and core result/effect algebra were not
  edited by this Writer.

Paths in the tables below are relative to `successor/standards/`. Old line
ranges refer to the exact consumer preimage above; new ranges refer to the
content identities in this table. They locate whole affected sections, including
their retained policies, rather than claiming that every line in a section was
replaced.

| File | Old bytes / SHA-256 | New bytes / SHA-256 |
|---|---|---|
| SPEC_METHOD.md | 166581 / `d89c4c7d5c579a0c3d99b4056e35202167e820579a90b13d8fc26fe852a6f4ae` | 164444 / `7478c7ed34672b0bc4ce8bbf70866ef85ed3b6edbb67196ebfb7d7be1c0c5529` |
| TICKET_METHOD.md | 64807 / `a91012c780f94c8cc0df85dd6912116ef1ad4c47a4bc070526fd39de2fbb1094` | 63262 / `baa5e557d06c2a1a6ac09b6ca53a2d954125e0a9baa82427920c28346c720646` |
| RELEASE_METHOD.md | 29591 / `6149280a25a1b2de88620b533a217f91bb238884238e7e86c63e126cab583ede` | 28774 / `b12ccf45da4baa1038081e6c66a2b8ade0c4e19cfc9bfde36f07708468cd5062` |

The aggregate consumer size changes from 260979 to 256480 bytes, a reduction of
4499 bytes. This is a size observation, not proof of reduced reasoning cost or
whole-method superiority. The semantic contraction is the replacement of
repeated application decisions at the following consumers.

## Shared determinations and consumer bindings

The following short labels locate the shared deciding owners at the frozen core:

- CA: [Contract application](../../../successor/standards/TRANSFORMATION_LIBRARY.md#contract-application),
  lines 96–154: Binding, Support, Preservation, Authority, Currentness and Result.
- CS: [Constraint surface](../../../successor/standards/TRANSFORMATION_LIBRARY.md#constraint-surface),
  lines 156–177: task constraints and unresolved conditions together with the
  actual material subject.
- FP: [Faithful projection](../../../successor/standards/TRANSFORMATION_LIBRARY.md#faithful-projection),
  lines 179–207: source-to-consumer fidelity and currentness.
- Core: [Result algebra](../../../successor/standards/FOUNDATIONS.md#result-algebra),
  [Result conjunction](../../../successor/standards/FOUNDATIONS.md#result-conjunction)
  and [Workspace and context](../../../successor/standards/FOUNDATIONS.md#workspace-and-context).
  CA consumes these owners; it does not define another result or effect algebra.

Admissibility of a proposed operation or reliance is distinct from the outcome
the operation evaluates or constructs. The revised gates bind both relations
where needed. Their conditions may be discharged together in the existing
operation; the edits add no validation stage, record, actor or approval round.

| ID | Consumer section | Old lines → new lines | Shared determination now used; domain binding retained |
|---|---|---|---|
| S1 | SPEC — Universal Intake Triage | 1253–1329 → 1253–1324 | CA binds classification to the exact request and current Product state. Report, governing sources, workspace/external observations, retained results and assessment grant are the instance inputs. Causal triangulation, the smallest sufficient frame selection and lawful change classes remain Spec policy. |
| S2 | SPEC — Computed Classification And Treatment | 1330–1406 → 1325–1395 | CA Support and Currentness replace repeated traversal/reuse rules. C retains producer/procedure revision, reproduction and invalidators; Public membership/value delta, accepted-design coverage, C/J/O and rule-determined treatment remain explicit. Root/grant changes stay material with equal Public bytes. |
| S3 | SPEC — Consistency Gate Rule | 1407–1432 → 1396–1419 | CA Result and core conjunction govern closure evidence. This gate binds upstream sufficiency, downstream consistency and active intended proof, all required judgments/rulings and no active non-closure condition. A local artifact's fitness is a separate predicate. |
| S4 | SPEC — Sufficient Execution Intake | 1603–1628 → 1590–1612 | CA and CS supply sufficient binding/acquisition. The instance retains selected outcome/prerequisite/experiment, affected relations, invariants, admission/design inputs, construction/assessment authority, current A, admitted Z and re-entry conditions. |
| S5 | SPEC — Bounded Causal Construction | 1629–1640 → 1613–1621 | CA Support owns seam closure and justified far-side independence. The instance's completeness criterion is the smallest coherent behavior-producing causal cone preserving every affected governing relation. Unrelated incompleteness remains bounded repricing input. |
| S6 | SPEC — Proportional Disposition | 1679–1728 → 1660–1706 | CA Result replaces the repeated generic verdict/conjunction explanation. The remedy table, cause-sensitive distinctions, governing-coherence admission condition, separate assessment/decision predicates and actual remedy authority remain local. |
| S7 | SPEC — Checkpoint, Continuation, Progress, And Churn | 1748–1786 → 1726–1763 | CA Currentness supplies continuation over the continuing workspace. Destructive rebuild still requires why retained repair is insufficient, surviving obligations/evidence, changed causal assumptions and an actual grant. Progress/churn and checkpoint policies remain. |
| S8 | SPEC — Complete Enclosing-Relation Admission (UP-021) | 1787–1835 → 1764–1806 | Each owner applies CA to admission of the exact complete transition. Its support universe includes every relevant participant and equality join. Owner derivation/validation, trust-boundary invalidators, basis continuity, semantic commit and independent judgment remain mandatory. Atomic admission is this domain's policy. |
| S9 | SPEC — Projection Discipline | 2032–2048 → 2003–2012 | FP governs runtime/reporting/status/topology/proof views. Migration completeness still requires one closure relation: independently closing views, conflicting carriers/laws and a view retaining superseded law all leave the migration incomplete. |
| S10 | SPEC — Release Version Boundary | 2149–2175 → 2113–2125 | Release identities and Selector and consumer adoption now decide exact cut versus discovery. Spec retains the boundary between live constitutional/realisation truth and release metadata/branding. |
| S11 | SPEC — Proof Target Identity And Adequacy (UP-001) | 2180–2191 → 2130–2142 | CA governs reliance on the witness. Before witness selection the proof binds its intended property, witness relation, nearest weaker excluded property and falsifier. Weak packaging/source/syntax evidence cannot replace the required stronger property. |
| S12 | SPEC — Semantic, Evidence, And Projection Separation (UP-008) | 2192–2208 → 2143–2160 | CA Currentness and FP decide affected verdict/view invalidation. The three basis kinds retain their definitions; semantic change requires re-entry, and broad digest invalidation does not establish universal semantic change. |
| S13 | SPEC — Assurance-Boundary Congruence And Method Qualification (UP-022) | 2209–2294 → 2161–2246 | CA binds reliance on assurance to the authoritative composite subject. The existing ordinary-path witness, inference/population scope, fresh-constructor, withheld-oracle, post-exposure and actual-use obligations remain. |
| T1 | TICKET — Upward Propagation Check | 611–634 → 611–630 | Consumes Spec's computed treatment instead of redetermining it from labels/Public delta. The ticket binds requirement/design sufficiency, actual owning-layer re-entry, permitted realization repair and J/O residuals. Missing evidence remains distinct from actual governing insufficiency. |
| T2 | TICKET — Execution Contract Admission | 709–764 → 705–753 | CA evaluates the exact admission predicate using the selected carrier, current work authority, mechanism, identity, criteria and result surface. Core law owns verdict/performance/refusal evidence. Carrier states, original admitted/rejected outcomes, exact human override and growth-basis ownership remain. |
| T3 | TICKET — Recorded Judgment And Owner-Ruling Continuity | 815–864 → 804–849 | CA Currentness replaces repeated reuse/history rules; Authority governs later reliance on the original mandate. Durable question, basis, revising observation, original owner wording, required independent judgment and obligation dispositions remain local. |
| T4 | TICKET — Bounded-Context Term Binding | 865–883 → 850–863 | CA Binding/Preservation consumes Spec semantic resolution for Product, re-entry, execution basis and scope. Unique unqualified use is permitted; cross-context carriers remain required. Unresolved meaning withholds affected admission/closure and re-enters its owner. |
| T5 | TICKET — Condition-Based Closure And Reuse | 915–944 → 895–919 | CA/core conjunction evaluate the exact obligation set and active non-closure conditions. Required owner acceptance is its actual predicate, not any lawful disposition. Direct authorized recording, required assessment exceptions and bounded unrelated repricing remain. |
| T6 | TICKET — One-Truth State Projection And Drift Refusal (UP-009) | 1379–1392 → 1354–1368 | FP binds current work-state views to the stated Goals/ticket/milestone/design authority chain and material acceptance evidence. Contradiction blocks closure; historical evidence keeps historical standing. |
| R1 | RELEASE — Immutable RC Publication | 195–232 → 195–231 | CA binds the granted publication operation and the actual remote-existence predicate. Remote observation governs uncertain dispatch effects; authorized repair cannot move an immutable cut. Publication steps and selector policy remain. |
| R2 | RELEASE — Exact-Cut Qualification | 233–271 → 232–263 | CA/core Result replace the repeated generic pass/skip/verdict/performance algorithm. Each item retains its exact cut coordinates, actual property, observation boundary and diagnostic; the release selects its required conjunction. Human exact-cut acceptance remains separate. |
| R3 | RELEASE — Qualification And Recovery | 471–502 → 463–492 | CA Currentness applies to the exact local/remote ref relation and frozen evidence. The observed complete remote relation decides publication effects. Recovery needs its existing grant; historical-backfill restrictions remain. |
| R4 | RELEASE — Acceptance Criteria | 520–544 → 510–532 | CA governs reliance on qualification evidence and the required actual owner decision. Qualification, exact human acceptance and consumer adoption remain three predicates, each retaining its own evidence, authority and performance. |

These mappings propose semantic conservation through a scoped consumer binding
and its current shared owner. They are not 23 new independent method mechanisms.
All original section headings remain, so this change requires no anchor remap.
The common 691-row frontier and any later row-level acceptance remain separate.

## Retained domain policies

The following 26 complete sections were compared byte for byte with the frozen
consumer preimage and remain identical:

- SPEC: Ambiguity Governance Rule; Product Outcome Conservation (UP-013);
  Proportional Method And Delivery (UP-014); Construction, Assessment, And
  Delegation; Standing Structural Qualification; Constitutional Migration
  Options; Hard-Break Discipline; Proof-Last Rule For Core Interface Changes;
  Fixture And Proof Portability Rule; Installed Dev Proof Rule.
- TICKET: Work-Carrier-To-Execution Rule; Multi-Build-Tenant Ticket Independence;
  Sprint Admission; Sprint Compliance Escrow; Sprint Close Review; Execution And
  Verification Authority Separation (UP-007); Test Case Authority.
- RELEASE: Release Identities; Project-Qualified Git Refs; Project-Subtree
  Release Identity; Historical Ref And Public-URI Conservation; Monotonic
  Version-Line Advancement; Selector And Consumer Adoption; Two-Commit
  Construction And One Publication Transaction; External Qualification
  Dependencies; Successor Baseline Conservation (UP-015).

In addition, the UP-021 suffix from “Derivation and validation bind one exact
admission-valid authoritative basis” through Standing Structural Qualification
is byte-identical. It retains exact basis continuity, effect-free re-entry,
complete-or-none admission, supported direct/composite/nested forms, replay
equality and post-validation atomic-failure coverage. The exact ticket override
exception is also byte-identical. Release's cohort atomic transaction,
create-only immutable tags, per-ref compare-and-swap leases and no sequential
fallback remain in their unchanged owning section. These are not generalized
into requirements for every use of CA.

## Independent challenge candidates

These are author-proposed cases, with expected preserved decisions drawn from
the cited source relations. They are not independent oracles or executed trials.
An independent evaluator must acquire the governing source and decide the
expectations before inspecting later candidate answers.

| Case | Expected preserved distinction | Relevant mappings |
|---|---|---|
| Public bytes are unchanged but the root or effect grant changed | Refresh affected applicability before reliance; byte equality does not settle authority. Preserve independently valid work. | S2, T3 |
| A caller declares a complete admission cone while an omitted far-side participant can change it | Derive the missing material support or refuse/retain the unresolved result without transition effect. An assertion cannot discharge the owner's completeness responsibility. | S5, S8 |
| Two owners supply individually valid judgments on incompatible bases | Refuse the join; a declared coherent composite basis is the permitted comparison case. | S8 |
| A known failure exists beside an absent required assessment | Retain both; do not invent the missing judgment or produce green closure. | S3, T5, R2 |
| A legitimate owner override authorizes bounded work despite a failed or absent admission evaluation | Preserve the original evaluation and separate override decision. Do not infer performance/completion or renewed growth authority. | T2 |
| An outcome was accepted but its ticket remains active | Ended growth authority stays ended; separately admitted preservation or a new outcome retains its own scope. | S2, T2; unchanged UP-013 |
| A publication call times out after remote dispatch | Observe the remote before a dependent retry/repair. Do not assume no effect or move an immutable cut. | R1, R3 |
| Source tests pass while a required external qualification backend is unavailable | Preserve Product classification but leave the dependent release claim unqualified unless lawfully narrowed. | R2; unchanged External Qualification Dependencies |
| Equal-shaped terms resolve to distinct contexts | Require the admitted semantic relation; nominal/schema equality is insufficient. | T4 |
| A sprint closes with explicitly permitted durable paydown | Sprint closure may be satisfied by its own classification/paydown obligations without falsely declaring the deferred delivery work complete. | T5; unchanged Sprint Close Review |
| The author opens a fresh context to supply required independent review | The authorship restriction still defeats that independence claim; an independent reviewer may reuse valid computed facts. | T3; unchanged UP-007 |
| A new role consumes applicable unchanged evidence under an existing exact grant | Permit reuse without another validation stage, repeated derivation or renewed unchanged permission. | S2, S7, T3, T5 |
| A compressed work-state view omits a permission or exception yet passes structural checks | Reject the affected fidelity claim; compare permissible, prohibited and unresolved decisions against the owner. | S9, T6 |
| Evaluation or construction is admissible but its intended outcome is not established | Keep admissibility, candidate availability, fitness, authorized disposition and release acceptance as their actual separate predicates. | S6, T2, T5, R4 |
| A single-carrier check is used for a multi-carrier assurance claim | Leave the unexamined composite obligations open; do not infer broader assurance from the narrower witness. | S11, S13, R2 |

## Checks and limits

Checks performed by the author:

1. The original consumer files at `3ad1fca` and the frozen core cut were identical;
   the worktree preimages matched the frozen core before editing.
2. Every original heading line was preserved in order: 80 in SPEC, 65 in TICKET
   and 23 in RELEASE. This includes headings appearing inside existing examples;
   no original heading or anchor was removed.
3. All 12 newly introduced distinct file/fragment targets resolve against the
   frozen shared source or the revised consumer files.
4. The 26 complete policy sections and two additional exception spans named
   above are byte-identical to their preimages.
5. Scoped `git diff --check` passed. The result/effect shared owner was not
   modified by this Writer.
6. An author source walkthrough checked the intended predicate separation and
   retained-policy routes for the challenge candidates above. This is bounded
   author reasoning, not independent review, actual use or exhaustive semantic
   conservation evidence.

The semantic claims still need independent source challenge, affected current
projections/frames and a_c interpretation, applicable fresh-use comparison and
the owning predecessor frontier dispositions. Parent integration owns those
surfaces. No broad artifact regeneration or historical trial update was made.
No runtime test or paid actor call was selected here; no Git mutation was made.

## Acquisition

This Writer retained its preceding read-only design consultation, which acquired
approximately 190 KB of selected consumer, library and common-contract text.
During this activation, 65,578 additional source bytes were displayed before
line-number/tool framing: root/v3 instructions (6,470), tenant design (9,810),
frozen Library (27,870), the admission excerpt (13,233) and selected Foundations
clauses (8,195). The three full consumer preimages total 260,979 bytes and were
also read by tooling for equality, digest and route checks; that is tool I/O,
not an additional claim that every byte was newly loaded into the Writer's
context. Repeated excerpts, generated diffs, reasoning and retained platform
context were not fully instrumented. No arbitrary context threshold or
whole-method adequacy claim is inferred from these counts.
