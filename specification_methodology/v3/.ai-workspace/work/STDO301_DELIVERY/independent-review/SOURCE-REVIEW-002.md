# Source repair readback 002 (bounded)

**Overall: `falsified`, but only on F5 trace completeness.**
- F1–F4 and F6–F10 are satisfied, and so are all the S4 items you listed.
- There are no S0–S2 findings and no change of meaning anywhere in the affected cone.
- What's left: four sections that apply a changed rule aren't listed in the family-trace consumer paragraphs (S3). Each of those sections already cites its owner, so no decision changes. Adding four references would close F5.

This is a working assessment, not an acceptance or publication decision. Inherited `not_ready` standing, pending supersessions, actual use and the supplemental representation are outside it.

The severity scale is the same as SOURCE-REVIEW-001. Paths are under `specification_methodology/v3/build_tenants/common/standards/` unless stated.

## Repair dispositions

**F1: satisfied.**
- `DESIGN_MODULE.md:282-285` lists all five predecessor classes again, with no F_D qualifier.
- `:292` says the scope "does not depend on F_D eligibility", so new non-qualifying helpers stay governed.
- Transforms and effect shells are "not automatically qualified" (`:297-298`).
- Existing helpers keep their permissions through the migration relation (`:299-301`), and `:2467` now says "referenced".
- Nothing is narrowed.

**F2: satisfied.** AC-015 (`AXIOMATIC_CALCULUS.md:1075-1093`) now separates the cases:
- A missing required declaration, a shown undeclared dependency, a disallowed kind or shown non-totality is a contract violation. Its judgment is falsified, and structural admission returns `refusal(constraint)` (AC-007 `:585`).
- If totality can't be decided on a valid basis, the judgment is `indeterminate`. Eligibility stays unestablished and the operation isn't admitted as qualifying F_D.
- An assessment that wasn't performed has no result.
- Causes found before a step exists take the ACTIVATION §3 admission outcomes (`ACTIVATION.md:982-989`).
- An applied operation waiting for evidence stops under AC-007, by cause.

AC-019 clause 3 (`:1177-1179`) makes model validity depend on this. `:1045-1051` rejects any rule that every process must have a kind. New non-total deterministic work gets no F_D or F_P standing; the route to F_D is a separately identified bounded successor. `ACTIVATION.md:1175-1177` keeps total handling separate from termination. The existing owners settle the ambiguity without a universal stop or forcing a result.

**F3: satisfied.** ODD A5 (`ODD.md:1084-1097`):
- Product admission owns Product facts, and ABG admission takes evidence and evaluator outputs into L/E (A1/A1a, `:920-966`).
- Closure truth is ABG's `evaluate_action` fold, recorded as `EdgeClosureDecision` (A4a `:1072-1074`, A6, A8; this matches the audit table at `:738`).
- F_P evaluator output stays a proposal until it is admitted.
- Gates keep deterministic validation and their own grants (`:1092-1093`, `:1545-1546`).
- The kind's no-authority rule is referred to AC §5.
- The closure fold stays deterministic through A6/A8 (a fold over admitted evidence with reproducible basis, `:1142-1143`) and the rule that F_P must not close an edge.

**F4: satisfied.**
- Premise (iii) (`AXIOMATIC_CALCULUS.md:161-164`) now includes construction.
- The row 13 choice column (`:180`) and the derivation statement (`:112-116`) declare the purpose extension, total-domain requirement and evaluation profile as §5 choices.
- ACTIVATION §3 has joined the provenance list (`:79-80`).
- No construction scope rests on the predicate premise alone.

**F5: partially satisfied; see the S3 finding below.**
- Every consumer that review 001 named is now listed (`AXIOMATIC_CALCULUS.md:204`, `FOUNDATIONS.md:1099`, `RELEASE.md:125`, `:147`).
- The listed sections do apply the rule (AC-011 `:692`, AC-016 `:1114`, `ACTIVATION.md:714`, `:1695`, AC §7 `:1216`).
- FOUNDATIONS row 4's "sound complete decision" matches its owner (`FOUNDATIONS.md:1224-1226`).

**F6: satisfied.**
- `specification_methodology/v3/build_tenants/common/release/release-note.md:35-41` states `not_ready`, `not_given`, `unassigned`, unperformed actual use, and that the kind and ODD supersessions are pending.
- `:19-22` discloses the ODD authority change, and `:45` says the supplement "remains to be prepared".

**F7: satisfied.**
- The literal authority set, the setup dict, the U/I tautology and the ungoverned log append are removed.
- The weak-observation counterexample is now computed (`examples/deterministic_contracts.py:154-158`).
- Authority, witness permission, attribution and the setup case are labelled as logical-review checks (`CONFORMANCE.md:226-233`; `examples/DETERMINISTIC_CONTRACTS.md:11-13`, `:49-54`, `:82-83`).
- The stated counts match the code: 40, 21, 45, 16 (+1,024 sequences), 24 and 10.

**F8: satisfied.**
- The acquisition model (`deterministic_contracts.py:65-74`, `:177-198`) covers inaccessible, missing, stale and resolved targets, and checks that nothing is mutated.
- `DETERMINISTIC_CONTRACTS.md:133-153` leaves result mapping to the consuming owner and limits the currentness test to the basis-version invalidator.
- It also disclaims any real filesystem, transport or human use.
- This is consistent with `FOUNDATIONS.md:655-657`.

**F9: satisfied.** The example members are listed at `README.md:66` and `:123-125`, and accounted for at `FOUNDATIONS.md:623-628`.

**F10: satisfied.**
- `RELEASE.md:726-741` now decides between row 2 (an identified gap or remediation, or a selected bounded successor) and row 3 (none selected).
- Both rows keep only lawful legacy standing on the exact old basis.
- Generic and schematic contracts are not treated as operations to qualify (also AC §7 `:1212-1216`).
- The five example traversals are classified (`DETERMINISTIC_CONTRACTS.md:190-196`); the transition and acquisition fixtures are excluded.

**S4 items you listed: all satisfied.**
- Symbols are tied to the traversal (`AXIOMATIC_CALCULUS.md:994-999`, `FOUNDATIONS.md:1243-1251`).
- A stop and its report are one outcome (`:996-999`; `DETERMINISTIC_CONTRACTS.md:64-68`, `:74`).
- D301 has its check column and the manual handover (`CONFORMANCE.md:224-233`).
- The a_c representation obligation is stated as still open (`DETERMINISTIC_CONTRACTS.md:172-186`, `FOUNDATIONS.md:715-717`).
- The no-authority rule has one owner (`AXIOMATIC_CALCULUS.md:1025-1030`), and its consumers refer to it (`ODD.md:1095-1097`, `DESIGN_MODULE.md:295-296`, `EVALUATION.md:132`, `RELEASE.md:743-744`).
- The task entry is coherent (`specification_methodology/v3/build_tenants/README.md:9-26`).

Review 001's other S4 items are also fixed: AC-016 `:1106`, RELEASE `:719-721`, SPEC_METHOD `:1802-1803`, ACTIVATION `:708-709`, `DETERMINISTIC_CONTRACTS.md:37-40`, and the five named traversals.

## S3 finding: consumer traces still incomplete (F5)

FOUNDATIONS §3 Consumers (`FOUNDATIONS.md:542-548`) requires each row to name the sections that apply its rule. AC's lists include sections of AC itself; for example, row 10 names "AC-019, clause 3" at `:201`. Four applying sections are missing:

1. **Row 13 (`AXIOMATIC_CALCULUS.md:204`) omits AC-019 clause 3** (`:1177-1179`). This repair made clause 3 apply AC-015 and the bound kind's contract. Row 13 already lacked clause 3 for composition in 3.0.0. *New in this repair.*
2. **Row 13 omits AC §7** (`:1212-1216`). §7 applies §5's total-domain contract and profile to `F_D[v_carrier_admission]`. That sentence dates from the first 3.0.1 construction, and review 001 didn't list it.
3. **Row 5 (`AXIOMATIC_CALCULUS.md:196`) omits §5's no-authority paragraph** (`:1025-1030`), which calls itself "the kind-specific application of AC-005". *New in this repair.*
4. **RELEASE's migration consumer list (`RELEASE.md:147`) omits ODD §11.7A** (`ODD.md:1553-1554`, "stays open under the migration relation").

- **Trigger:** someone starting at those rows can't reach the sections that apply them.
- **Consequence:** DISPOSITIONS' F5 coverage claim is overstated against discriminator 2 (`CONFORMANCE.md:142`). No decision changes.
- **Correction:** add the four references, or record why each one isn't a consumer.

## New S4 findings (clarity only)

- **`DESIGN_MODULE.md:282`:** "evaluators and proofs" loses the "deterministic" sense that 3.0.0's `F_D` carried. The context keeps it (`:280`, `:2443`), but "deterministic evaluators and proofs" would restore the exact class.
- **`DESIGN_MODULE.md:2461`:** the inherited label "default `F_D` helpers" now reads as kind-qualified, and the identity-default permission depends on it. `:2467` makes eligibility conditional.
- **`ODD.md:1094`, `:1487`, `:1551`:** a bare "§5" inside ODD reads as ODD §5. Both readings lead to AC §5.
- **Release note `:36`:** it says "covering acceptance review". The predecessor note says "covering independent source review", and `specification_methodology/v3/.ai-workspace/work/STDO301_DELIVERY/native-release/release-gates.md:39` says "covering source review".
- **`deterministic_contracts.py:122` and `:196`:** two assertions are true by construction. Line 122 checks a literal against itself; line 196 holds because of how the fixture is built. Neither is cited as evidence.
- **`RELEASE.md:729`:** it says "declared" bounded successor, while `:735` and `STDO_3_0_1.md:43` say "selected".

## Checked, no finding

- **The repair edited the owning requirement** (`specification_methodology/v3/specification/requirements/STDO_3_0_1.md:39-48`).
  - "Each existing use" became "each existing operation proposed for migration". The row is now decided by evidence plus the declared remediation status.
  - This matches the proposal's "assess each proposed import" and its P301-06 rows. It is within the Writer's grant (`specification_methodology/v3/.ai-workspace/tickets/active/T-004-STDO-3.0.1-delivery.md:31`).
  - DISPOSITIONS F10 only says "the same distinction". The owner should see the scope wording at acceptance.
- **AC-019 clause 3 now covers every kind.** For F_P and F_H it adds nothing beyond their existing §5 definitions, AC-005 and AC-015.
- **Review 001's valid coverage stands.** That covers the P301-01 core, P301-02–05, predicate-specific exhaustion and the fixed-Γ witness. The added paragraphs don't change the contract, and `delta(s,u)=delta_hat(alpha(s),u)` states the same factorisation more precisely.
- **The three feedback subjects hold:** ODD authority migration (F3), the stronger totality migration (F2, F10) and predicate-specific exhaustion.

## Limits

- I used only Read, Glob and Grep. I computed no hashes and did not run the Python; I checked the case counts by reading the code.
- I did not examine the frames, FRAME_INPUTS, the package, the representation, the release tooling, or REFERENCE_FRAME's F1 consumer list. Unchanged members were only searched, not read.
- Spend was about US$7 by the session meter. Wall time wasn't measured.

## Independence and access

- I'm Claude Opus 5.5 and authored none of the subject. Codex wrote it, so this review is cross-family.
- Review 001 is the same model as me. I read it first as directed, so I'm not independent of its framing.
- I worked out my expectations for F1–F3 and F6–F10 before opening DISPOSITIONS, then tested its claims against the source. The F5 trace sweep came after I had read it.
- I didn't open RETURN, CHECKS or PACKAGE_CHECK, and I made no writes.
