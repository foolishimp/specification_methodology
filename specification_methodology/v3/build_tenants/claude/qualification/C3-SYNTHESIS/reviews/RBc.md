# RBc: Working Review Of B3, B3b, B8, B1b And B9

Status: same-family working check, not acceptance. Commentary, not specification or design.

| Coordinate | Value |
|---|---|
| Reviewer | RBc, a fresh Claude context; it wrote none of the subjects |
| Authors | Claude Writer activations B3, B3b, B8, B1b, B9 (same model family) |
| Subject commit | `fbd5d37`; previous `f7851aa` |
| Subjects | `build_tenants/claude/standards/` ODD, TRAVERSAL_OCCURRENCE, AXIOMATIC_CALCULUS, IDENTITY, CONFORMANCE; returns B3, B3b, B8, B1b, B9; deltas B3, B8, B1 (B1b section) |
| Sources read first | `specification/requirements/README.md`, `A_C_DEPENDENCY.md`, `specification/conformance/README.md`; C3-SYNTHESIS EXPECTATIONS and LEDGER; FOUNDATIONS §1, §3, §4 at `fbd5d37`; installed rc.2 AXIOMATIC_CALCULUS, TRAVERSAL_OCCURRENCE_PROFILE, ODD_METHOD, IDENTITY_METHOD |
| Repairs | none; this file is the only write |

Paths are relative to `specification_methodology/v3/`. `file:line` cites the file at `fbd5d37`; rc.2 cites the installed predecessor.

## Expectations

Recorded from the sources before any subject was opened.

### Q1 Unified algebra

- X1-1. AXIOMATIC_CALCULUS restates AC-007 as a law over constraints that uses the FOUNDATIONS §4 core and defines no value set of its own. AC-007's five result kinds (rc.2 AXIOMATIC_CALCULUS:293–295: failed, missing, indeterminate, out-of-scope, invalid-basis) each have one disposition: failed to `falsified`; missing to no closed result (a gap under FOUNDATIONS §4 Not performed), never a core value; indeterminate to `indeterminate`; invalid-basis to `invalid_basis`; out-of-scope to exactly one core value per cause, the cause carried in the refined value (FOUNDATIONS:722–724).
- X1-2. The operation stops `gap`, `hold` and `refusal` (rc.2 AC-010 :320, AC-011 :329, AC-013 :632, Interpret :755) map with a predicate. Neither maps to `satisfied`. A proposed successor `M*` maps only to availability ("a candidate is available"), never to fitness or acceptance (R §Single Result Algebra 5; N-7).
- X1-3. No parallel algebra: RF-012 and AC-007 are restated once in FOUNDATIONS §4; REFERENCE_FRAME §3 and AXIOMATIC_CALCULUS §4 use it (E-5-1, E-5-9).
- X1-4. TRAVERSAL's constraint values (`satisfied`, `falsified`, `indeterminate`, `invalid_basis`) are core values. Its judgment decisions and stop kinds (rc.2 TRAVERSAL :668–717) each map to one core value with a predicate. A refusal or stop that AXIOMATIC_CALCULUS also names gets the same core value in both members.
- X1-5. The parent-value rule (LEDGER:217: a further refinement maps each child to its parent's core value; a different core value needs a different parent value at the owning member) has one owning locus. TRAVERSAL's per-traversal `stop_states` refine without re-mapping `refusal(constraint)` away from `falsified` (LEDGER:209).
- X1-6. The 2026-10-12 meanings hold (LEDGER:232–235): `partial_effect` and `partial` map to `falsified` only on demonstrated non-attainment, otherwise `indeterminate`; a refusal for a falsified constraint, structural included, maps to `falsified`; `invalid_basis` only for an invalid-basis refusal or a co-emitted `invalid_basis` decision.
- X1-7. Effect dispositions keep unknown completion distinct: `partial_effect` never maps to `no_effect` or `completed_effect` (R §Single Result Algebra 3, item 4).
- X1-8. A basis mismatch inside a model or a qualifier record is AC-006 mixed bases, `refusal(basis)`, `invalid_basis` (LEDGER:222).

### Q2 ODD and TRAVERSAL splits

- X2-1. Each split value names its cause, its predicate and one core value (E-5-3). No split maps upward (E-5-4, N-2): ODD `yield` and `block` never `satisfied` for a closure predicate; `close` is `satisfied` only for the closure predicate, never acceptance (N-7); the ODD audit outcome "valid and worth incorporation" is not `satisfied` for "compliant with the current method" (rc.2 ODD :428).
- X2-2. Rows disposed "carried exactly" keep predecessor tables and code blocks byte-for-byte except declared changes.

### Q3 Family tables F8, F9, F18, F19

- X3-1. Each table has the four columns of FOUNDATIONS:472, labelled instance premises, and premises whose standings match FOUNDATIONS:317–324 (P0 recovered; P1, P2, P3, P4a, P6 independent; P4b derived from P0 and P2; P5 derived from P0 and P6).
- X3-2. Each consequence links its rule; each added choice has an owner or "none"; the table states no determination its rule does not state (FOUNDATIONS:490–492).
- X3-3. Profile tables (F18, F19) name the families they import (FOUNDATIONS:476–478).
- X3-4. Every deciding section of the member is traced or given a reason; the FOUNDATIONS index (FOUNDATIONS:513–535) agrees with what exists (E-1-2, E-1-3).

### Q4 CONFORMANCE

- X4-1. Each of the 31 rows of `specification/conformance/README.md` (rows at :9–:39) maps to a case or a named logical-review check (E-8-10, E-7-1 to E-7-31).
- X4-2. The coverage claim says no more than the mapping shows: a logical-review check is not an executed case, and no row passes on a mechanical check alone.
- X4-3. No rule is carried only by an `stdo://` link (E-1-5, E-1-7).

### Q5 Conservation

- X5-1. For at least 20 changed determinations, weighted to AC-007, AC-010 and AC-011, TRAVERSAL refusals and ODD closure decisions, the successor text supplies the predecessor determination (R §Standalone Successor 3; E-1-5).

### Q6 Links and writing

- X6-1. Every relative link resolves to a file and heading at `fbd5d37`.
- X6-2. No undefined term, floral language, history narration or person's name in member text; no modal changed (must to should, or the reverse) without a disposition.

## Results

Abbreviations: AC `standards/AXIOMATIC_CALCULUS.md`; T `standards/TRAVERSAL_OCCURRENCE.md`; O `standards/ODD.md`; ID `standards/IDENTITY.md`; CF `standards/CONFORMANCE.md`; F `standards/FOUNDATIONS.md`; rc.2 AC, rc.2 T, rc.2 O are the installed predecessor members.

| Q | Result | Evidence | Findings |
|---|---|---|---|
| 1 Unified algebra | falsified | X1-1: AC:515–530 maps each AC-007 outcome once (holds, failed, indeterminate, out of scope to out_of_frame, invalid basis); a missing result has no closed result (AC:527–530). X1-2: AC:542–548 maps the operation outcomes; `M_b_prime*` and `M_subject*` establish availability only (AC:544). X1-3: AC:501–513 and F:704–715 restate AC-007 and RF-012 once in F §4; no "core member" or `#3-result-algebra` remains in the five members. X1-4: T:925–936 gives `hold` indeterminate, `gap` invalid_basis, `refusal(constraint)` falsified, `refusal(basis)` invalid_basis, the values AC:545–548 gives. X1-6: T:908–934 keeps `partial_effect`/`partial` falsified only on demonstrated non-attainment, otherwise indeterminate; T:877–903 keeps a refusal for a falsified constraint, structural included, at falsified, with the qualification in Note N1. X1-7: T:1297–1303 and ACTIVATION:786–792. X1-8: AC:555–562, T:858–868. | M1 (material); m1, m2, m3, m13 (minor); N1 (note for the cross-family review) |
| 2 ODD and TRAVERSAL splits | satisfied | O:1032–1063: `retry`, `repair`, `re-enter`, `block` split by cause, each value with one core value for "the edge's obligations are fulfilled on the exact basis"; `yield` indeterminate (O:1054), `close` satisfied for the edge predicate only and kept apart from availability (O:1013–1019). O:453–457: "valid and worth incorporating" maps to out_of_frame, not satisfied. T:842–936 and T:1297–1303: every split value names cause, predicate and one core value; none maps to satisfied. Carried exactly: a script compared every fenced block and table row of rc.2 TRAVERSAL_OCCURRENCE_PROFILE (257 rows) and rc.2 ODD_METHOD (31 rows) with the subject; all are present byte for byte. | none |
| 3 Family tables F8, F9, F18, F19 | falsified | Four columns: ID:58, AC:163, O:103, T:73. Instance premises labelled: ID:51–56, AC:155–161, O:93–98, T:64–68. Profile imports named: O:84–89 (F2, F3, F4, F9), T:57–60 (F3, F9). Consequences link their rules; choices carry owners or "none". F8 accounts for every IDENTITY section (ID:72–73 for §11, §13). F9 accounts for every AC section. | m4, m5, m6, m7 (minor); the precedence in M1 is also a choice presented as a consequence (AC:170) |
| 4 CONFORMANCE | satisfied with minor findings | CF:127–159 restates all 31 rows of `specification/conformance/README.md` in common order, each mapped to a case or a named check; 11 to cases, 20 to L checks only, counted correctly at CF:161–165. CF:119–124 states that a case tests only its part and every row is also read by logical review. No pass is claimed (CF:165–173). The common specification is provenance only (CF:7–11); no rule rests on an `stdo://` link. Case links resolve. | m8, m9, m10, m11 (minor) |
| 5 Conservation | satisfied with one minor risk | 30 changed or newly mapped determinations sampled (table below); every predecessor determination is supplied by owned text. | m12 (minor); M1 changes a value but loses no predecessor clause |
| 6 Links and writing | satisfied | A link script resolved every relative link and anchor in the five members and the eight returns and deltas at `fbd5d37` (one false positive inside the fenced block at AC:899). No person's name, floral wording or modal change in the diffs `f7851aa..fbd5d37`; IDENTITY F8 rows keep the predecessor's "should" (ID:60–70). | the undefined "refusal qualifier" of a judgment-level refusal is m3 |

## Findings

### M1 (material). One defective transformation gets two different core values, depending on how many grounds its refusal names

- Text: AC:548 lists as a `refusal(basis)` condition "an input model, subject or carrier whose exact identity, basis or admission is not established". AC:553–554 rules that a refusal naming conditions of both kinds takes `refusal(basis)`. T:851–852 and T:872–876 repeat the precedence.
- Counterexample: oracle `qualification/cases/C3S-02/EXPECTATIONS.md` at `fbd5d37`, written before any frame without reading candidate text.
  - P2 (E) expects the refusal to name T3 together with T4 and T10. T3 is that r3's exact model identity is only a locator, which AC-013's "mutable locator … refuses" covers. T4 and T10 are demonstrated violations.
  - P4 (R) requires `falsified`, and N5 says that `invalid_basis` inverts P4.
  - Under AC:548 and AC:553–554, an actor that names all grounds, as P2 asks, must return `invalid_basis`, which fails P4. An actor that names only T4 and T10 returns `falsified`.
- Determinacy: the same subject with the same demonstrated defects gets a different core value according to how complete the refusal's list of grounds is. Under FOUNDATIONS §4 Recording (F:666–671), the counterexample still travels in the domain outcome, but not as a known failure. F:858–863 defines a known failure as a `falsified` result, so the union of known failures in a conjunction omits it.
- FOUNDATIONS side: a member may declare an order among non-satisfied values in its own rule (F:801 choice column; F:881–885). Basis precedence is therefore a lawful choice in principle. F9's row at AC:170, however, presents "the basis taking precedence" as a consequence that follows from P5 and P6. It is an added choice, and the choice column names no owner for it.
- Smallest repair: an Executive ruling between AC-007 and the C3S-02 oracle, then one of these:
  - (a) At AC:553–554, a refusal that names a demonstrated violation takes `refusal(constraint)` and records the basis condition with it as a residual. T:851–852 and T:872–876 follow, keeping the co-emitted `invalid_basis` decision case that the 2026-10-12 meaning allows.
  - (b) Keep basis precedence, move it to F9's choice column with AXIOMATIC_CALCULUS as owner, state that the violated constraint's counterexample is kept in the record as a known failure, and have the owner amend C3S-02 P4.

### m1 (minor). The parent-value rule is stated twice

AC:911–921 owns it. T:951–961 restates it in full ("Each refined value names its parent value and a cause … maps to its parent's core value …") and adds the PROFILES §1 binding shape, without referring to AC §5 for the rule itself. F §4 Refinements (F:717–728) does not state the rule for a refinement of a refined value, although T:1297–1303 nests one under ACTIVATION §3 Effects. The rule is respected in every case read. Smallest repair: replace T:954–961 with a reference to AC §5's rule and keep only the binding shape. Optionally, state the general form once in F §4 Refinements and have AC §5 apply it to stops.

### m2 (minor). AC-007's two refusal causes are not total

AC:547 defines `refusal(constraint)` positively, as a violated law of the member or a constraint of its signature, and AC:548 defines `refusal(basis)` positively. A refusal that names neither has no value in AC. One example is the `refuse` of `J_X` at AC:1081–1082 on grounds other than a fidelity defect. T:877 closes the same gap with "every other refusal". Smallest repair: in AC:547, ground the value as "every refusal that names no condition of the basis", as at T:877.

### m3 (minor). TRAVERSAL reads a judgment refusal's cause from a qualifier that the refusal does not have

T:853 says that the qualifier records the cause and does not choose it. T:904–907 then chooses `refused(basis)` or `refused(constraint)` by whether the refusal "carries `refuse_invalid_basis`". The refusal qualifier is a field of `OccurrenceRelationQualifiers` (T:574–611), so only relations carry one. A judgment-level refusal has no qualifier from that domain: an acyclicity violation at `model_validation`, an `unauthorized` readiness, or an inconsistent semantic cut. T:881–882's claim that every `refusal(constraint)` "carries `refuse_missing`, `refuse_duplicate`, `refuse_wrong_type` or `refuse_out_of_scope`" is unsupported for these, and none of the four values describes a cycle. The core values are unaffected because AC-007's condition decides them. Smallest repair: T:904–907 reads the cause from AC-007's condition, and T:881–882 and T:858–860 say "where a relation qualifier records it".

### m4 (minor). The FOUNDATIONS index still marks F8 and F9 "table pending"

F:522–523 says "table pending", and F:507–510 says such a row "traces none of their rules". The tables exist at ID:43 and AC:147. Smallest repair: drop "table pending" from F8 and F9. F14, F15, F20 and F21 should be checked the same way; they are outside this subject.

### m5 (minor). The F18 standing line omits P3, and F18 and F19 give "derived" without premises

O:100–101 gives standings for P0, P1, P2, P4a, P6, P4b and P5, but rows O:115, O:116 and O:117 cite P3. O:100–101 and T:70–71 write "P4b and P5 derived" without "from P0 and P2" and "from P0 and P6", which F:322–323 and F:475–477 carry. Smallest repair: add "P3 independent" to O:100–101, and add the derivation premises to both lines.

### m6 (minor). F18 and F19 do not account for every deciding section in their rule columns

F18 and the "other sections" sentence (O:121–124) do not account for:

- §11.2A, the outcome-first realisation order (O:555–581), which sets a required order and limits imperative adapter code;
- §11.5C, projection-source coherence (O:688–707), whose rules include reconcile, fail closed and "name equality is not enough";
- §5 Nodes, Vectors and Traversal (O:209–223, O:334–339).

F19 has the same pattern. Row T:75 accounts for four sections only in its choice column, although each holds refusal and congruence rules: Closed semantic-object sorts, Finite reference-domain table, Closed event-kind population and Closed relation families. Its rule column links only Imported calculus boundary and Exact profile identity.

Smallest repair:

- F18: add §11.2A to row O:110 or O:115, §11.5C to row O:112, and §5 Nodes, Vectors and Traversal to row O:115.
- F19: link the four sections in row T:75's rule column.

### m7 (minor). F9 presents a choice as a consequence

This is the AC:170 point of M1. If M1 repair (a) is taken, the precedence clause is deleted. If repair (b) is taken, the clause moves to the choice column.

### m8 (minor). The coverage claim does not say that the logical-review checks are unperformed

CF:164–165 says that 20 discriminators "are exercised by logical-review checks only", and CF:165–173 states the evidence state of the cases. No L check has a recorded result. Smallest repair: add one sentence after CF:173: no logical-review check is recorded for this revision, and each is a planned assessment without a closed result until a review records it (F §4 Not performed).

### m9 (minor). Rows 17, 20 and 21 map to one case alone, but each case tests only part of its discriminator

CF:119–122 requires a cell to name the L check for any part its case does not test. Each row below was tested by asking whether the case's subject and expected distinction instantiate the whole discriminator.

- Row 17 (CF:145) includes "including when the candidate's bytes are unchanged". T-06 (CF:65) does not state that part.
- Row 20 (CF:148) is an interruption that leaves work partly written. T-05 (CF:64) is a pause and context clear, which states no partly written work.
- Row 21 (CF:149) holds the claim mechanical until semantic and practical evidence exists. T-07 (CF:66) tests structural green against required behaviour, not the practical-evidence part.

Row 7 passes the same test: T-01 (CF:60) covers narrowing, lawful escalation and a truthful out_of_frame stop.

Smallest repair: add "L-17 for unchanged bytes", "L-20 for partly written work" and "L-21 for practical evidence" to those cells, and recount CF:161–165.

### m10 (minor). The F7 accounting of CONFORMANCE is stale

This is outside the subject but bears on Q4. EVALUATION:355–357 says that "CONFORMANCE §1 to §3 list the cases … its §4 records dispositions". After B9, §4 holds the CD cases, §5 the coverage and §6 the dispositions. B9 reported this (returns/B9.md:79–83), and it is unrepaired at `fbd5d37`. Smallest repair: "§1 to §4 list the cases, §5 maps the common discriminators, §6 records dispositions".

### m11 (minor). C-09 names an index as its mechanism

CF:51 names "PROFILES §2" as the mechanism. PROFILES §2 is the graph-execution index, and the boundary's owner is ODD §5 with F §2 Work boundary. B9 noted this (returns/B9.md:88–89) and left it. Smallest repair: change the cell to name ODD §5 Probabilistic compute and F §2 Work boundary.

### m12 (minor). Open gap versus dangling reference is undefined

AC:546 separates a `gap`, "a required reference not yet resolved", from a dangling reference "established to resolve to nothing". It does not say what makes a resolution open or established. In a closed model, AC:274–276 (rc.2 AC:210–213) refuses "an identity in `I` with neither one local record nor one lawful external resolution", and AC:298 refuses dangling external identities. A reader can therefore move an unresolved local reference from `refusal(constraint)` (falsified) to `gap` (invalid_basis). That is the inversion N8 of the C3S-03 oracle forbids for occ-25. The predecessor's own "unresolved refs retain `gap`" (rc.2 T:689) is the source of the tension. Smallest repair: one sentence at AC:546. A local reference with no record in the closed population is dangling. `gap` applies only to a resolution that a declared relation has not yet decided, such as an external resolution not yet evaluated.

### m13 (minor). TRAVERSAL's `Projection` is not marked as distinct from AC-011's projection

AC:626–628 makes every AC-011 projection refusal `gap` or `refusal(basis)`, that is, invalid_basis. TRAVERSAL's `frontier_complete` maps a falsified result to `refused` plus `refusal` (T:795), which T:877–886 makes `refusal(constraint)`, falsified.

The two members do not conflict. `frontier_projection` judges a `Projection` record, a profile semantic-object sort (T:190, T:1339–1342), and does not perform `project(M, Z, R)`. AC:563–566 lets one defect bear on two predicates. Neither member states this, however, and T:18–21, which lists the profile terms that claim no core meaning, omits "projection". Smallest repair: add `Projection` and projection to T:18–21's list, with "a `frontier_projection` judgment judges a `Projection` record and is not an AC-011 projection".

### N1 (note for the cross-family review, not blocking). Two refusals were reclassified after the 2026-10-12 meanings

At `f7851aa`, TRAVERSAL listed a basis-relation mismatch at model validation among the falsified structural constraints and mapped it to falsified. B1b moved it and the qualifier basis mismatch to `refusal(basis)`, invalid_basis. The sources are T:858–868, T:987–989 and the B1b row 636 in `deltas/B1.md`. The move rests on a same-family Executive ruling (LEDGER:222).

The 2026-10-12 cross-family meaning allows invalid_basis "only for an invalid-basis refusal or a co-emitted `invalid_basis` decision". This check reads both reclassifications as invalid-basis refusals, and so as consistent with that meaning. A same-family check cannot confirm that the cross-family ruling still holds after the tenant has reinterpreted it. The cross-family review should confirm it.

### Note, not a finding

The spelling "out of scope" decides three cases:

- the AC-007 constraint result "out of scope" maps to out_of_frame (AC:524);
- TRAVERSAL's stop `out_of_scope` and `refuse_out_of_scope` map to falsified (T:930, T:881);
- a scope that is not exact gives `refusal(basis)` (AC:548).

Each case has its own predicate and ground, so none conflicts with another. T:930 separates the stop from the core's out_of_frame but not from AC-007's "out of scope" row, and one clause there would remove the misreading.

## Q5 Conservation Sample

Each row compares the subject at `fbd5d37` with the installed predecessor. "Kept" means the subject's own text supplies the predecessor determination.

| # | Determination | Predecessor | Subject | Result |
|---|---|---|---|---|
| 1 | AC-007: a constraint names subject, predicate, judgment kind, latitude, refusal | rc.2 AC:414–415 | AC:500–501 | kept |
| 2 | AC-007: failed, missing, indeterminate, out-of-scope, invalid-basis results are not coerced to success | rc.2 AC:415–417 | AC:505–508, AC:527–530 | kept; tightened to the core |
| 3 | AC-010 closure defined only on exact inputs, finite unique fixed point; otherwise gap or refusal | rc.2 AC:440–442 | AC:607–611 | kept; split by cause |
| 4 | AC-010 least closure claims no minimal size or cost | rc.2 AC:442–444 | AC:611–613 | kept |
| 5 | AC-011 projection contains the closure, records seams, owns no meaning, trims nothing silently | rc.2 AC:448–457 | AC:619–631 | kept |
| 6 | AC-013 coordinates equal or lawfully restrict the traversal's; broader refuses | rc.2 AC:501–504 | AC:679–682 | kept |
| 7 | AC-013 exact model identities; a mutable locator refuses | rc.2 AC:506–512 | AC:684–690 | kept |
| 8 | AC-013 failure to establish identity, partition, witness or residual refuses | rc.2 AC:624–627 | AC:810–814 | kept |
| 9 | AC-013 application yields a proposed successor that does not admit itself | rc.2 AC:629–637 | AC:816–826 | kept |
| 10 | AC-015 an application without `[v]` is incomplete | rc.2 AC:730–732 | AC:952–960 | kept; mapped to `refusal(constraint)` |
| 11 | §5 `Omega_v` is the closed stop algebra of one traversal | rc.2 AC:698–704 | AC:899–904 | kept; tightened to a refinement of the core |
| 12 | Interpretation yields a proposed model; structural evaluation does not prove semantic retention | rc.2 AC:753–778 | AC:984–1012 | kept |
| 13 | Encoding requires `accepted`; hold or refusal cannot be encoded | rc.2 AC:838–843 | AC:1073–1076 | kept |
| 14 | An identity with neither local record nor lawful external resolution refuses the model | rc.2 AC:210–213 | AC:274–276 | kept; at risk through AC:546 (m12) |
| 15 | AC-003 dangling and wrong-basis references refuse structural admission | rc.2 AC:384–391 | AC:466–472 | kept; wrong-basis now `refusal(basis)` by ruling |
| 16 | Constraint predicate returns one of four values; no omitted result, residual or stop becomes success | rc.2 T:679–683 | T:757–762 | kept |
| 17 | Closed judgment-domain table | rc.2 T:687–696 | T:766–775 | byte-identical rows |
| 18 | Closed constraint-domain table | rc.2 T:705–717 | T:784–796 | byte-identical rows |
| 19 | Residual re-entry table | rc.2 T:722–731 | T:802–811 | byte-identical rows |
| 20 | Qualifier defects refuse structural admission; materialisation copies the qualifier byte for byte | rc.2 T:572–579 | T:651–656 | kept; basis mismatch takes `refusal(basis)` by ruling |
| 21 | Edge defects refuse `occurrence_admission` | rc.2 T:600–603 | T:678–681 | kept |
| 22 | Closed disposition law, four dispositions | rc.2 T:974–984 | T:1268–1278 | kept |
| 23 | `invokes_effect` iff dispatched; `unauthorized` or `stale` never dispatches | rc.2 T:986–989 | T:1280–1284 | kept |
| 24 | A begun effect without complete disposition stays `partial_effect` with bounded post-observation | rc.2 T:995–997 | T:1314–1316 | kept; the mapping never reads it as absent or complete (T:1002–1008) |
| 25 | A8 closure vocabulary closed; each decision replay-visible with basis and reason refs | rc.2 O:1088–1103 | O:991–1005 | kept |
| 26 | A9 `yield` returns control without failure classification | rc.2 O:1105–1119 | O:1065–1076, O:1054 | kept; indeterminate, never falsified |
| 27 | A10 liveness alone never declares semantic failure or closure | rc.2 O:1121–1125 | O:1078–1081, O:1033–1035 | kept; `retry(undecided)` respects it |
| 28 | A11 repair and re-entry are graph actions selected by `evaluate_next` | rc.2 O:1127–1135 | O:1083–1088 | kept |
| 29 | §9 audit outcomes; incorporation not approved until the profile is updated; non-compliance repriced, repaired or rejected | rc.2 O:422–430 | O:438–444, O:453–457 | kept; modals unchanged |
| 30 | §9 grey work is not silently absorbed; shared law is updated in the profile | rc.2 O:415–420 | O:433–436 | kept |

No sampled determination is lost or weakened. Row 14's risk is m12. The value changes in rows 15 and 20 follow the recorded Executive ruling (LEDGER:222) and the 2026-10-12 exception for an invalid-basis refusal.

## Disposition

- Q1 falsified (M1 material; m1–m3 and m13 minor; N1 for the cross-family review).
- Q2 satisfied.
- Q3 falsified on minor findings (m4–m7).
- Q4 satisfied with minor findings (m8–m11).
- Q5 satisfied with one minor risk (m12).
- Q6 satisfied.

M1 needs an Executive ruling before the AC-007 text or the C3S-02 oracle changes. This record is a same-family working check, not acceptance.
