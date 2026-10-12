# Independent Reviewer Report: C3 finite interpretation at 804b396

## Standing and limits

- **Inputs:** I used only the bytes in your message. I used no tools, including the advisor tool, because you said "no tools". I did not run any code, read any files or consult any peer tenant.
- **Hashes:** I cannot get the files again or compute any hash. Where I say hashes match, I compared the hash strings you supplied with each other. That shows they are consistent; it does not show the bytes are authentic. Authenticity rests on the Host Writer.
- **No disposition:** these results are evidence, not acceptance. They give no authority to accept, repair, re-enter or take a next action. Labels inside the files, such as `invariants_valid` and `complete_selected_clause_closure`, are treated as evidence only.
- **Owners:**
  - **Owning obligation:** SOURCE.md owns these predicates. It calls itself an authored qualification contract, "not new STDO law".
  - **Non-deciding correspondence:** the candidate TRANSFORMATION_LIBRARY.md and FOUNDATIONS.md, and the program's `source_refs` that point to them. Both documents say they are non-deciding.
  - **Not supplied:** the UP-020, RF and AC owners they cite, so I make no claim about them.
- **Names:** Alpha = `program-mutant.json`, Beta = `program.json`. "Executable mutant" = `operation(..., infer_permission=True)`.

---

## Beta (`program.json`, intended to be faithful)

| # | Predicate | Result | Basis |
|---|---|---|---|
| B1 | Token-state fidelity | **satisfied** (finite scope) | The `permission` qualifications match SOURCE#token-state: unknown → unresolved, no effect; known but missing exact permission → refused, no effect. The issuer must equal the current owner, with exact token, destination and `assign`. A label or inspect grant gives no permission. `token-transfer` keeps every unselected token unchanged, keeps the token set and single ownership, and disclaims idempotence. |
| B2 | Typed-join fidelity | **satisfied**, with a note | The premise copies the source text exactly. Note: SOURCE says "No source grant follows". Beta writes "confer no operation permission", which is narrower wording. Both restrict; neither grants anything. "Despite equal float representations" survives only as the statement "Field-shape equality cannot supply semantic compatibility." |
| B3 | Finding conservation | **satisfied** | Beta keeps A falsified, its original producer, the citation `source/A.md#permission-branch`, and B as uncovered rather than as an omitted slot. The result stays non-green. Note: the premise merges "the plan contains exactly A" with "A is supplied and authenticated". The qualification separates them again. |
| B4 | Missing and unauthenticated slot exceptions | **satisfied** (qualitative) / **out_of_frame** (executable) | "Missing or supplied-but-unauthenticated A invalidates a complete planned-set claim; never invent the judgment" matches SOURCE's "not supplied/authenticated", read as an OR. The library's Conjoin section agrees: absence does not infer falsification, and the owner's admission rule decides. That agreement does not decide anything. As ENCODING declares, finite_check.py does not model this exception. |
| B5 | Authority and recovery | **satisfied** | `role-boundary` says results give no action or acceptance grant. It uses "action" where SOURCE says "next-action", which is a stronger restriction. `effect-recovery` matches "observe/reconcile or stop unresolved". The residual lists the same distinct claims as SOURCE. |
| B6 | Complete indexes and closure | **satisfied** for direct references / **indeterminate** for tool closure | All 4 `frame_refs` have an index. Each of the 6 clauses appears in at least one index. All 7 vocabulary terms are used and each has a SOURCE heading. Every cited heading exists in SOURCE or the candidates. The indexes themselves are not closed, though. `index:authority` lists `role-boundary`, whose premises refer to `finding-conservation`, `token-transfer` and `typed-join`; none of those is in that index. Whether the projection computes that closure cannot be checked: `map.json`, the projection files and `bindings.json` were not supplied. |
| B7 | Explicit encoding latitude | **satisfied**, with minor gaps | Declared: indices 0/1, the owner tuple, `label:A`/`label:B`, the observation flag (current observation, not post-effect completion), and the mutant flag as test machinery. Not declared: the dict shape of typed grants and the result string `completed`. SOURCE says "performs the selected assignment" there, so this is harmless. |
| B8 | Executable ↔ model correspondence | **satisfied** for permission and transfer / **out_of_frame** for the rest | By reading the code: 4 states × 2 tokens × 2 destinations × 19 grants × 2 observation values = 608 cases. That gives 304 unresolved and 16 completed (one exact grant per state, token and destination, 4×2×2). The remaining 288 are refused (16 × 18 non-matching grants). A check on completed cases requires the grant to equal the exact dict, independently of the guard that admits it. The assertions refuse to run under `-O`. |
| B9 | Receipt binding | **satisfied** (string agreement) / **indeterminate** (authenticity) / **gap** | The FINITE_RESULT hashes match the supplied SOURCE, program, mutant and finite_check hashes. The MECHANICAL pins match those plus ENCODING and FINITE_RESULT. Gaps are listed below. |

Gaps under B6 and B8:
- **Effect-recovery under the token index:** `index:tokens` lists `effect-recovery`, but the finite check does not exercise it. The FINITE_RESULT limit "not an already-issued effect with unknown completion" correctly bounds this. Don't read the index as finite coverage of recovery.
- **Weak closure receipt:** `complete_selected_clause_closure: true` only checks that the union of all four indexes covers every program clause. Every clause is listed directly in some index, so this cannot fail. It does not test how closure is computed for a partial selection. Treat it as a structural label, not evidence of closure.

Gaps under B9:
- `qualify.py` (967f31…) produced MECHANICAL_RESULT, but neither receipt pins it.
- `bindings.json`, `INSTALL_VERIFICATION.json` and the 7 tool members are counted but not pinned in the report.
- I could not check the `map.json`, projection and `REQUEST.txt` pins.
- The `wrong-program-old-map` step only checks for a non-zero exit, with no diagnostic code. A tool crash would pass it as a "refusal". The empty-selection step, by contrast, checks for `empty_selection`.

---

## Alpha (`program-mutant.json`, permission mutant)

| # | Predicate | Result |
|---|---|---|
| A1 | Token-state fidelity | **falsified** |
| A2–A5 | Typed join, findings, authority, slot exceptions | **satisfied**. These clauses, the residual and all indexes are identical to Beta's in the supplied bytes. |
| A6 | Indexes and closure | Same as B6 |
| A7 | Internal coherence | **falsified** |

**A1, source-linked:** the premise "A named current owner or display label supplies permission without an exact grant" contradicts two SOURCE#token-state sentences: "A display label grants no permission" and "Permission is issued by that token's current owner for that exact token/destination/operation".

- **Counterexample:** owners (A,A), token t0, destination B, grant `label:A`, state known.
  - SOURCE → refused, state stays (A,A).
  - Alpha → completed, state becomes (B,A).

**A7, internal coherence:** Alpha keeps the qualification "known missing exact permission returns refused" next to a premise that grants permission without an exact grant. With the same `label:A` case, the clause gives both completed and refused. Also, `token-transfer` still assumes "exact permission" while depending on a permission clause that no longer requires it.

**Structural evidence:** MECHANICAL records `validate -mutant` with exit 0. This shows that a_c structural validity does not detect the semantic mutation. Structural success does not support any fidelity claim.

---

## Executable mutant (`infer_permission=True`) and token scope

**Against SOURCE: falsified, 32 counterexamples.** Any string grant is admitted once the state is known. That is 4 states × 2 tokens × 2 destinations × 2 labels = 32 cases. None of them involves unknown observation, because the unknown check runs first.

- **16 change state.** The literal recorded in FINITE_RESULT: owners (A,A), t0, destination B, `label:A`, known → correct refused, mutant completed, state becomes (B,A). This is the first state-changing case in iteration order, so the receipt is consistent with the code.
- **16 change only the result.** For example: owners (A,A), t0, destination A, `label:A`, known → correct refused, mutant completed, state unchanged. This still violates "missing permission returns refused". The counter name `unauthorized_mutant_counterexamples` covers both kinds without distinguishing them.

**ENCODING's description of the executable mutant: satisfied.** The mutant does still refuse `None`, mismatched dicts and inspect dicts, as ENCODING says. Only label strings are newly admitted.

**Alpha ↔ executable mutant: partial correspondence, not a match.** The executable mutant implements only the "display label" part of Alpha. It does not implement "named current owner".

- **Counterexample:** owners (A,A), t0, destination B, grant `{issuer:A, token:0, destination:A, operation:inspect}`, known.
  - Under Alpha's premise, the current owner is named → permitted.
  - The executable mutant → refused.
- ENCODING's word "correspondingly" therefore overstates the match. ENCODING's explicit "retaining refusal of … mismatched or inspect grants" partly corrects this.

**Token scope: satisfied, as limited.**
- The proof covers single steps plus one resumption trace: completed → unknown/unresolved → old issuer refused after the state change → current-owner grant completed.
- The re-observation in that trace is the trace author passing in the current state. It is model-local and does not show a system re-observing anything.
- Grants are not consumed. If a grant's destination equals the current owner, it "completes" with no change.
- These are not covered:
  - uncertain completion after an effect
  - stale observation
  - multi-step exhaustive recovery
  - the finding, join and authority clauses

---

## Wider claims these results do not support

Passing structure, projection, join and the 608-case enumeration supports none of the following:
- the fidelity of any clause not listed above
- the correctness of tool-computed closure
- universal idempotence, or exactly-once behaviour over a distributed transport
- categorical equivalence
- practical adequacy, corpus qualification, acceptance or release

The candidate library and foundations `source_refs` (#bind, #transform, #conjoin, #dispose, #typed-composition-and-conservation, #orthogonal-descriptions) match on wording. They are non-deciding correspondences and supply no owning obligation. For `role-boundary`, the library's Evaluate section ("A judgment supplies no repair, acceptance or next-action authority") would be a closer citation than Dispose.
