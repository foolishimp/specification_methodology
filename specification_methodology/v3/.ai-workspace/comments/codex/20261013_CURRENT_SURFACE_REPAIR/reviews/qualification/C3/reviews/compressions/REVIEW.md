# Review: authority compressions, STDO RC2 → v3 (subject commit `b0ec615`)

**Overall result for the group: `falsified`, one low-severity finding.** All 10 members keep their RC2 content and obligations. The successor also adds one new obligation that no supplied owner defines, and one clause in the README now disagrees with the bootstrap.

I used only the supplied artifacts: the RC2 bytes of each member, the frozen successor bytes, and the two new owners `FOUNDATIONS.md` and `TRANSFORMATION_LIBRARY.md`. I did not call the advisor tool because you asked for no peer acquisition. This is a document comparison, not native-host qualification.

## Results per member

| Member | Change from RC2 | Result |
|---|---|---|
| `README.md` | `../FOUNDATIONS.md` and `../TRANSFORMATION_LIBRARY.md` added to the list of deciding sources; rest of the text unchanged | **falsified** (F1) |
| `axiomatic_calculus.compressed.md` | Only `source_digest` and `generated_at` changed; body identical | satisfied |
| `design_module_method.compressed.md` | Only header fields changed; body identical, including the IACS revision path, the `STDO-UP-022` routing and UP-023 | satisfied |
| `odd_method.compressed.md` | Only header fields changed; body identical | satisfied |
| `spec_method.compressed.md` | Only header fields changed; body identical, including the consumer-update, adopt/sync, qualification and C-walk clauses | satisfied |
| `stdo_bootstrap.md` | Two new sources and digests; four other source digests changed (schema digest unchanged); new opening paragraph; steps 1–8 and the trailing adopt/sync/marker clauses identical | satisfied for conservation; one new clause `indeterminate` (I1) |
| `stdo_compressed.md` | Two new sources; 13 source digests and the glossary index digest changed; same new opening paragraph; every RC2 section identical | satisfied for conservation; `indeterminate` on I1 |
| `ticket_method.compressed.md` | Only header fields changed; body identical | satisfied |
| `traversal_occurrence_profile.compressed.md` | Only header fields changed; body identical | satisfied, with residual R3 |
| `ux_method.compressed.md` | Only header fields changed (last generated 2026-06-06); body identical | satisfied |

The new opening paragraph in the bootstrap and the aggregate matches the new owners on the points that matter:
- **"organise … no compulsory stages, new record schema or automatic authority":** the library says it is "not six compulsory stages or six runtime APIs", "not a mandatory record schema", and its members refine the families "without acquiring authority from the library".
- **"Detailed owners retain … result domains and operation grants":** the library says "Domain members determine their admitted outcome and disposition sets", and `FOUNDATIONS.md` (Construction and use) says "Foundational explanation does not transfer authority from a named detailed method owner."

The paragraph keeps these authority limits and the "raw owners decide" fallback.

## Findings

**F1 — the README's description of the bootstrap is now out of date (`falsified`, low).**
- **Where:** the last paragraph of the successor `README.md`: "It is digest-bound to Specification Method, Reference Frame Method, the optional STDO Reference Frame Baseline, Release Method, and the Product Definition schema and cannot select or replace them."
- **What it contradicts:** the successor `stdo_bootstrap.md` header now lists seven sources and digests, including `../FOUNDATIONS.md` (`13e9c41d…`) and `../TRANSFORMATION_LIBRARY.md` (`7515a652…`).
- **Why it matters:** in RC2 this sentence matched the bootstrap's five sources exactly. The successor added two sources to the bootstrap and to the README's own deciding-source list, but did not update this sentence.
- **Consequence:** someone using the README to check when the bootstrap goes stale would miss that a change to either new owner makes it stale, and that the bootstrap cannot select or replace those two either. The bootstrap's own `stale_if_source_digest_changes` still works, so the actual stale check is unaffected.
- **Fix:** small, one sentence. Risk of breaking anything else is minimal.

**I1 — "responsibility frame" is not defined by any supplied owner (`indeterminate`, low to medium).**
- **Where:** the new opening paragraph of both `stdo_bootstrap.md` and `stdo_compressed.md`: "Use a sufficient responsibility frame for the selected claim".
- **The problem:** this is a new instruction. Neither new owner uses the term "responsibility frame". `FOUNDATIONS.md` only says "sufficient projected reference frame" and "sufficient material context and capability". Under the bounded-context rule, a term that resolves to no concept fails closed.
- **Why it is not falsified:** the successor `REFERENCE_FRAME_METHOD.md` or `SPEC_METHOD.md` (digests `e305e2fa…` and `077f43af…`) may define it, but they were not supplied.
- **Fix:** have that owner define the term, or change the clause to "sufficient reference frame".

## Other observations (not findings)

- **The README lists the two new owners as deciding sources without their own caveat.** Both describe themselves as explanatory. `FOUNDATIONS.md` says its explanatory consolidation "preserves their source-owned determinations", and the library "does not supersede those meanings". The bootstrap and aggregate state this caveat; the README does not. Adding one sentence there would remove any chance of a precedence inversion.
- **The aggregate binds both new owners by digest but projects almost none of their obligations.** It says "cannot be closed from one source-specific compression". Obligations from the new owners that are absent or only partly present in the aggregate:
  - an uncertain effect must be observed or reconciled before any repetition (Foundations);
  - the categorical, functor and Markov claim burdens;
  - authentication of planned assessment slots in Conjoin;
  - keeping the evidence classification from the UP-020 assessor-disposition field;
  - "repeating an unchanged failed relation … is a prohibited retry practice";
  - the dimensions to measure for a cost or improvement claim.

  This does not violate conservation: nothing from RC2 was lost, the relative links resolve, and the raw-fallback rule still applies. But a current digest only shows the projection is fresh, not that it covers these owners.

## Residuals (not falsified, still open)

1. **Digest correctness:** I could not hash anything, so I cannot confirm that any `source_digest` or `source_digests` value matches its owner's bytes. That includes the two new owners and the 13 changed method digests. Even if checked, digest equality would not prove the projection is faithful.
2. **Unsupplied owners:** the successor bytes of SPEC, RFM, Baseline, DMM, ODD, TOP, AC, Ticket, UX, World Model, Identity, Release, Posting and Glossary were not supplied. For each member whose body is unchanged while its owner's digest changed, I cannot tell whether the unchanged text is still faithful to the changed owner. Each of those members needs a review against its own owner.
3. **The traversal profile's fixed count:** "the bound candidate has fourteen" principle refs survives verbatim, while both the AC and TOP owner digests changed. It holds only if the calculus member's derivation addresses are unchanged, which was not shown.
4. **Directory inventory:** no installed manifest was supplied, so I cannot confirm that this directory has exactly these 10 members, with nothing dropped or added, or that any of it is installed.
5. **Release examples and the RC2 release note:** no concrete release coordinate appears in these members; they only use the `stdo://releases/v<version>-rc.<n>/` template. Nothing here mints a v3 cut. The historical RC2 note was not supplied, so it was not evaluated, and I made no current v3 publication claim.
6. **Native acceptance:** owner acceptance, qualification and publication of the v3 successor are outside this comparison and remain open.
