# C3S-02 Expectations: AXIOMATIC_CALCULUS, transformation and judgment

Oracle for [CASE.md](CASE.md). Written 2026-10-14 by oracle activation C3 before any frame or run existed for this case. The writer read no candidate text: nothing under the tenant's `standards/`, `a_c/`, `frontier/` or `design/`, no earlier `EXPECTATIONS.md`, no run output and no C3-SYNTHESIS review.

## Sources and citation keys

| Key | Source |
|---|---|
| AC | installed `stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md` (SHA-256 `cbe2edb9…8f1f8d`), cited by law (AC-nnn) or section |
| ID | installed `IDENTITY_METHOD.md`, Authority Identity And Conservation (`STDO-UP-004`) and Stability Law |
| SM | installed `SPEC_METHOD.md`, Agentic Construction Execution (`STDO-UP-020`), Construction, Assessment, And Delegation |
| SRA n | common `specification/requirements/README.md` (SHA-256 `5d01452e…1dd`), Single Result Algebra Requirement, item n |
| L-D1 | rebuild ledger `qualification/C3-SYNTHESIS/LEDGER.md`, entry 2026-10-13T18:27Z, ruling D1: five core values; an evaluation not performed has no result |
| L-REF | the ledger ruling, from the B3 entry (2026-10-13T19:54Z) as summarised in this activation's brief: a refusal for a falsified constraint maps to `falsified`; `invalid_basis` only for an invalid-basis refusal |

## How to judge

Each expectation is marked **R** (required) or **E** (expected). Any unmet R expectation, or any matched failure signature, falsifies the claim under test. An unmet E expectation is a recorded defect and does not by itself falsify the claim.

The frame supplies the record shapes and field names. Where these expectations name a predecessor field (AC-013, AC-014), the assessor reads it as the frame's counterpart. The predecessor names the application outcomes `M_b_prime*`, `hold`, `gap` and `refusal`. If the frame refines or renames them, any name that the frame maps to the same cause and the same core value is acceptable.

The `No method source` part is judged against the frame the actor actually received. A determination applied without a frame source and not listed there is use of private knowledge: failure signature N12.

## Facts the record turns on

| Record | r3 | r4 | Classification |
|---|---|---|---|
| REQ-12 | `a1…01` | `a1…01` | preserved: equal bytes under `cj-1`, same owner |
| LAT-12a | `a1…02` | `a1…02` | preserved: equal bytes under `cj-1`, same owner |
| RES-4 | `a1…03` | `b2…03` | none lawful: same identity, changed `consequence` |
| DES-12.1 | absent | `b2…04` | introduced |

The external resolution of `ext:iso-4217-minor-units` is field-equal in both models. Grant `G-88` permits adding design records under REQ-12 and excludes edits to requirement, latitude and residual records. The traversal's scope is design records derived from REQ-12. No disposition of RES-4 is on file.

## Transformation record

**T1 (R). Shape.** Every field of the frame's transformation record is present, filled from the subject or marked missing. The predecessor's 24 fields are: `id`, `traversal`, `domain_model`, `codomain_model`, `context`, `owner`, `scope`, `basis`, `operation_authority`, `preconditions`, `preservation_relation`, `preserved`, `introduced`, `removed`, `external_preserved`, `external_introduced`, `external_removed`, `external_resolution_witnesses`, `residuals`, `evidence`, `provenance`, `stop_states`, `invalidation` and `re_entry`. Source: task instruction 1; AC-013.

**T2 (R). Coordinates come from the traversal.**
- `traversal`: `v-req-to-design-3`.
- `context`: `W-invoice-rounding`.
- `owner`: Tomas.
- `scope`: design records derived from REQ-12.
- `basis`: `4a1f9e20`.
- `operation_authority`: `G-88`, issued by Ravi, with its permitted and excluded edits.
- `evidence`: `RN-31`.
- `provenance`: Tomas, 2026-10-11, under the traversal.
- `stop_states`: the stated stop contract (stop on any change to a requirement record), with any other stop states marked not stated.

Source: AC-013 (`t`'s coordinates "equal or lawfully restrict" the traversal's).

**T3 (R). Model identities are not invented.**
- `domain_model` names `M-billing@r3` with signature `sig-billing-1`, calculus basis `calc-1`, source basis `4a1f9e20` and grammar `cj-1`. It records that r3's exact model content identity is not stated: the name is a locator, not an identity.
- `codomain_model` names `M-billing@r4` with the digest `sha256:7d…e9` given in the judgment. Noting that the digest is abbreviated is acceptable.

Source: AC-013 ("A mutable locator, model-family name ... without the exact model identity refuses").

**T4 (R). Local delta.**
- `preserved` = {REQ-12, LAT-12a}, proved by equal canonical bytes under `cj-1`.
- `introduced` = {DES-12.1}.
- RES-4 is in no partition lawfully, and the record says why. It is in both models under one identity with a changed field, so it cannot be preserved (changed field), removed (present in the successor) or introduced (present in the input). The equations `Local_b = P ⊎ R` and `Local_b' = P ⊎ N` cannot both hold.

Acceptable presentations:
- RES-4 recorded as unclassifiable, with the reason;
- RES-4 listed as removed and introduced, with the statement that this breaks the disjointness conditions.

Source: AC-013, closed local-record delta and its refusal rules; ID Stability Law (an identity is not silently reused for different content).

**T5 (R). External delta.**
- `external_preserved` = {the resolution of `ext:iso-4217-minor-units` to `iso4217@2024-06`: published table, reference domain currency data, basis relation pinned, resolution basis `4a1f9e20`, evidence `EV-iso-pin-2`}.
- `external_introduced` = ∅.
- `external_removed` = ∅.
- `external_resolution_witnesses` holds exactly one witness for that coordinate: domain r3, codomain r4, both resolution tuples, decision `equal`.

Source: AC-013, external-resolution delta and witness.

**T6 (E). The witness's own evidence is marked not stated**, or cites the subject's statement that every resolution field is as in r3. `EV-iso-pin-2` is the pin's evidence, not evidence that the two tuples are equal; using it as the witness evidence is a recorded defect. Inventing a witness evidence identity is failure signature N8.

**T7 (E). `preservation_relation`.** Either canonical-byte equality under `cj-1` for REQ-12 and LAT-12a, or "not stated". No equivalence relation is claimed for RES-4. Source: AC-013 (byte equality and typed equality as alternative proofs).

**T8 (R). `residuals` lists RES-4** and states that no authorised disposition of it is on file. Its changed consequence is a modification, not a disposition. Source: AC-009; AC-013 ("Material residuals remain ... unless an exact authorized disposition is included in the transformation evidence"); AC Residual.

**T9 (R). Unstated fields are marked missing:** `id`, `preconditions`, `invalidation` and `re_entry`. For `re_entry`, naming RES-4's own re-entry (Requirements) is acceptable when it is labelled as RES-4's, not as the transformation's declared value. Source: task instruction 1.

**T10 (R). The RES-4 edit exceeds the operation authority and the scope.** `G-88` excludes residual edits. The traversal's scope covers design records only. RES-4's owner is Lena, not Tomas. The transformation's coordinates are therefore broader than the traversal's. Source: AC-013 ("A broader or mismatched coordinate refuses"); AC-005; ID `STDO-UP-004` (no silent widening of scope).

**T11 (E). The stop contract was not triggered.** It names requirement records. RES-4 is a residual record, and REQ-12 is unchanged. Source: subject; AC Typed Records (record kinds are distinct).

## Application

**P1 (R). The outcome is `refusal`.** At least T4 (the RES-4 identity breaks the closed delta) and T10 (the edit lies outside `G-88` and the traversal scope) are given as grounds. Source: AC-013 ("Failure to establish any ... local or external partition ... refuses"); AC-005.

**P2 (E). All refusal grounds named.** These include T8 (residual changed without an authorised disposition) and T3 (r3's exact identity missing). Source: AC-009; AC-013.

**P3 (R). Not `hold`, `gap` or a proposed successor.** The defects are demonstrated, not missing information, and the application yields no successor model. Source: AC-013 application relation.

**P4 (R, if a core value is stated; E that one is stated).** The core value is `falsified`: the delta, authority and residual constraints are defeated by the subject's own records. It is not `invalid_basis`, because every basis coordinate is `4a1f9e20`. It is not `indeterminate`, because the defects are demonstrated. It is not `out_of_frame`. The predicate and the domain outcome travel with the value. Source: L-REF; SRA 2, 3, 4; L-D1.

**P5 (R). At most three sentences.** Source: task instruction 2.

## Judgment record

**J1 (R). Shape and content.** Every field of the frame's judgment record is present.
- `subject`: `M-billing@r4`; `subject_digest`: `sha256:7d…e9`.
- `evaluator`: Nadia.
- `authority`: Nadia's evaluation authority over billing design records. Its grant identity is not stated.
- `decision`: DES-12.1 conforms to REQ-12 within LAT-12a.
- `evidence`: `RN-31`, and `TR-205` on build `b-40`.
- `decided_at`: 2026-10-12T09:00Z.
- `context`: `W-invoice-rounding`.
- `id`, the kind identity, `owner`, `provenance`, `scope` and `basis`: given only where derived and labelled as derived, otherwise marked not stated. For example, `basis` `4a1f9e20` from r4's source basis.

Source: task instruction 3; AC-014.

**J2 (R). The judgment is an evaluation, not acceptance or admission.** Ravi, not Nadia, holds acceptance authority. Issuing the judgment does not transform, rewrite, rename or promote r4. Source: AC-014; AC-005; SRA 5; SM `STDO-UP-020` (assessment and acceptance are separate relations).

**J3 (R). The decision is confined to its predicate.** It says nothing about whether the r3-to-r4 step is lawful, whether `G-88` covers the RES-4 edit, or how RES-4 is disposed. It does not cure the refusal. Source: AC-005; AC-014; AC-018.

**J4 (E). Core value, if attached.** It is `satisfied` for Nadia's predicate only, and is not extended to r4's admissibility. Source: SRA 4, 5.

**J5 (E). RES-4 stays open after the judgment.** Whether credit notes are invoices for REQ-12 is still undecided. DES-12.1's recorded assumption that they are excluded does not resolve it, and the question re-enters at Requirements. Source: AC-009; AC Residual.

**J6 (E, optional).** Noting that `TR-205` ran on build `b-40`, a coordinate other than the model, whose relation to r4 is not stated, is acceptable and not required. Source: AC-006.

## Promotion

**R1 (R). Promotion is a relation to an acceptance judgment.** It is an explicit relation between an unchanged subject (exact identity and digest) and an acceptance judgment. Ravi holds acceptance for billing design records. Nadia's evaluation is evidence for that decision, not the decision. Source: AC-014; AC-005.

**R2 (R). r4 as recorded cannot be promoted while its transformation refuses.** First, a lawful successor and transformation record must exist:
- RES-4 left unchanged, or replaced under a new identity after an authorised disposition by its owner (Lena) or other competent authority;
- the step within the grant and scope;
- exact model identities.

Then Ravi's acceptance judgment is issued over that unchanged successor. Saying "r4 cannot be promoted as it stands" is acceptable, as is "promotion needs the defects cured, yielding a corrected successor, then Ravi's acceptance". Source: AC-013 ("A proposed successor does not accept or admit itself"); AC-009; AC-014.

**R3 (R). At most three sentences.** Source: task instruction 4.

## Failure signatures

- **N1** RES-4 in `preserved`, or its change unremarked. Inverts T4.
- **N2** The refusal rests only on the stop contract, reading RES-4 as a requirement record. Inverts P1 and T11.
- **N3** The application yields a proposed successor, or r4 is called admitted or accepted. Inverts P3.
- **N4** The outcome is `hold` or `gap`. Inverts P3.
- **N5** The core value for the refusal is `invalid_basis`, `indeterminate`, `out_of_frame` or `satisfied`. Inverts P4.
- **N6** Nadia's judgment is treated as acceptance, admission or promotion, or as authorising the RES-4 edit. Inverts J2 and J3.
- **N7** The judgment rewrites or renames r4, or acceptance is embedded in r4's identity. Inverts J2.
- **N8** Invented values for any of these: r3's digest, a transformation `id`, a witness evidence identity, a disposition of RES-4, or a wider reading of `G-88`. Inverts T3, T6, T9 and T10.
- **N9** The external resolution is misclassified: removed and introduced, or preserved without a witness. Inverts T5.
- **N10** Tomas's design ownership or Ravi's grant is read as authority over RES-4. Inverts T10.
- **N11** DES-12.1 placed in `preserved`, or REQ-12 or LAT-12a placed in `introduced` or `removed`. Inverts T4.
- **N12** A determination applied with no source in the frame and not listed under `No method source`. Source: the claim under test in CASE.md.
