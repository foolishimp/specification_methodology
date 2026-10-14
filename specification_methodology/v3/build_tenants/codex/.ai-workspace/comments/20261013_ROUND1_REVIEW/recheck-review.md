# Recheck of frozen Codex repair round 8bb3213

I reviewed only the supplied bytes. I did not run any code. Every execution claim below rests on the supplied receipts (`IDENTITY_CHECK.json`, `ACQUISITION_CHECK.json`, `DISTRIBUTION_CHECK.json`). None of them records the commit or a package digest, so they are not bound to the frozen bytes except by assertion. This is a source recheck only. It grants no acceptance, release or tenant ranking.

## Disposition of the initial findings

| Finding | Status | Basis |
|---|---|---|
| F1 hidden dependency and fragment completeness | Closed for the dependency and duplicate address. Narrowed for population independence. | See F1 below. |
| F2 unsupported proof claims | Closed for the specific claims. Narrowed for control coverage. | See F2 below. |
| F3 frame routing and scope | Closed for the omitted owners and fixture language. Narrowed for fidelity evidence. | See F3 below. |
| F4 ownership and absent material | Closed for placement and absence disposition. Narrowed for the membership recipe and profile text. | See F4 below. |
| F5 library row 2 | Closed. | The row now says domain seam declarations are design evidence and each UP-021 owner still derives and validates the enclosing relation and far-side independence. UP-017 is supplied and says the same (include the far side or state why it cannot participate). |

### F1

**Closed:**
- `derivation_material.py` no longer loads `check_candidate.py`.
- The address rule is recorded in the resource as `semantic_address_rule`. `verify` refuses unless it equals the checker's `ADDRESS_RULE`.
- `resolves_once` refuses an address that occurs zero times or more than once. The control "duplicate semantic address under coherent publication pins" expects "ambiguous profile signature fragment".
- `refs()` consumes every inline link in "Derivation Provenance" or refuses. It rejects reference-style links and addresses with a path or whitespace.
- `verify` recomputes the required references from the publication-pinned calculus bytes, rather than trusting the record or resource lists.

**Duplicate heading versus duplicate address.**
- Two headings with the same text receive `slug` and `slug-1`. Each address occurs once, so each resolves. This is not a duplicate semantic address.
- Refusal fires only when one address has two producers. Examples are an explicit `<a id>` colliding with a heading slug, or a literal heading "Foo 1" colliding with the generated `foo-1`.
- The supplied control covers only the anchor collision. No positive control shows that ordinal-distinguished duplicate headings still resolve.

**Residuals:**
- The address population is recomputed by the same `refs()` function the builder uses. That demonstrates faithful recomputation from the pinned section, not independent discovery. The guard test (`METHOD2.md#clause_2`) exercises only the parsing branch. Unsupported-syntax refusal has no negative control.
- `PROFILE_FRAGMENTS` and `core-signature` are hard-coded in the checker. The supplied Profile section is truncated at "exactly these fragments … ```text", so I cannot compare the hard-coded list to the prose.
- A bare address resolves to the first of several same-slug headings. Inserting an earlier same-titled heading would retarget it while still passing "exactly once". Only the member-digest pins (the signature's `profile_member_sha256`, the resource source pins) contain this. The address rule alone does not.
- The heading regex `^#{1,6}\s+(.+?)\s*#*\s*$` strips trailing `#` even without a preceding space. A heading such as "Using C#" would slug as `using-c`, contrary to a plain reading of the recorded rule. No required fragment is shown to trigger it.
- Explicit anchors are counted inside fenced code, but headings are not. The recorded rule is silent on this. The effect is over-refusal, not under-refusal.
- The checker implements only the reconstruction form of historical material. Identity Method also permits "carried as exact evidence bytes". A carrier using that form would be refused, which is the safe direction, but that form is untested.

### F2

**Closed:**
- Reads are now observed with `sys.addaudithook` on `open` and `socket.*` during `verify` only. An out-of-package open or a socket event raises. The report lists six package reads.
- The hard-coded literal `outside_package_reads: 0` remains in the report, but it is backed by the raising hook.
- The "no literal body bytes" claim is now computed. The supplied resource contains only `start_byte`/`end_byte` segments, and the report gives `literal_reconstruction_bytes: 0`.
- `refused()` now asserts the exact expected reason. A wrong reason raises `AssertionError`.
- New controls cover duplicate and extra member, duplicate and out-of-order ranges, literal tamper, source pin versus published member, out-of-package source path, symlink escape, a missing authentic historical fragment under coherent pins, and a duplicate address.
- The top-level `valid` in the report is `all(refused)`. It is true whenever execution reaches the end, so the meaningful assertions are the raised errors, not that field.

**Residuals:**
- The audit hook sees `open`, not `stat`, `lstat` or `listdir`. "No outside reads" means no outside data opens. Existence probes are unmeasured.
- The "relative path escape" control actually fires the `uncatalogued publication member` reason, which comes from the inventory check. The `..` guard in `read_member` is exercised only through the symlink case.
- Missing controls:
  - record kind/version tamper;
  - profile signature digest tamper;
  - a different (not just absent) address rule;
  - derivation release equal to the publication release;
  - empty `principle_refs`;
  - a calculus link added without updating the material;
  - removing one profile fragment.
- The positive case uses a fixture manifest and bases generated from the same cold bytes. It shows internal consistency only, and `v0.0.0-rc.1` is a fixture, not an issued release. The printed basis identities are fixture-only. The report should label them as such, since only the limits list says "hypothetical".
- Evidence limit: the historical manifest is pinned by `BUILDER_SHA`, and `members()` recomputes its `member_set_sha256` successfully in the positive case. If the receipt is credible, that is independent evidence that the membership recipe reproduces a genuinely issued manifest digest. It is not independent evidence about the new fixture manifest.

### F3

**Closed:**
- Both previously missing views are now supplied.
- `CONSTITUTIONAL_DERIVATION` includes the library specialization, the Design consumer, UP-016, UP-021 in full, UP-017, seam closure, totality, RF-003, RF-005, RF-006, RF-012 and RF-014. The README description now matches the content.
- The "fixture answer" and "author's private selection" language is absent from the supplied README and `stdo-work/SKILL.md`. `DESIGN.md`, which sits outside the package, still says "a fixture answer does not select it".
- The Source headers carry the digests `e6e3…` (Library), `c268…` (Design), `fbdc…` (Spec), `44bb…` (Frame Method) and `2cbd…` (Ticket). They match `FRAME_INPUTS.json`.
- The header counts (18 and 14 in the two views, 71 across six) match the receipts. Anchors resolve under the slug function (e.g. `workrecovery-specialization`).

**Ordinary-entry routing:**
- Closed in the supplied text.
- Triage, re-entry, carrier selection and execution admission route to `TRIAGE_CARRIER`. Typed handoff and transformation admission route to `CONSTITUTIONAL_DERIVATION`.
- The routing sentence is task-neutral and says a prepared frame grants no work or admission.
- The `CONSTITUTIONAL_DERIVATION` scope line reads "WHAT-to-HOW derivation and producer/consumer contract" and does not name admission. That is a wording mismatch with the route, not a content gap.

**Residuals:**
- The derivation view carries material that does not obviously serve admission (UP-013, Test Authority Rule, and the ontology derivation order inside UP-017). The "Admission contract use" text appears twice. This costs attention. It adds no authority.
- `check_acquisition.py` runs `refresh()` before checking, so the check mutates files. It compares pre-refresh hashes to post-refresh hashes, which does detect staleness.
- It re-renders with the same `slug` and `relocate` helpers it checks. This is reproducibility and internal consistency, not independent fidelity. The receipt itself says it is not an actor-sufficiency test.
- The renderer finds headings with no fence tracking, so `##` lines inside code fences could mis-bound a section. It also refuses same-slug owner headings where the derivation address rule would assign ordinals. Its slug lowercases before NFC, while the recorded rule normalizes before lowercasing. No supplied instance triggers any of these.

### F4

**Closed:**
- Identity Method calls the resource "distribution evidence for these byte predicates, not a second constitutional surface".
- It states that acceptance of the historical cut, semantic derivation, successor admission and publication stay at their existing owners.
- It states "Missing, duplicate, altered, incomplete or unbound material refuses the affected verification", and that an installed predecessor is neither an exception nor an implicit fallback. The disposition is stated once at one owner.
- The calculus text points to it without restating refusal, and adds no field to either basis record. The checker's exact-key shape checks enforce this.
- Release Method keeps cut acceptance, membership and publication. Identity Method uses the existing publication-manifest digest and does not define membership.
- The checker raises a refusal for the verification. It returns no global verdict.

**Residuals:**
- The member-set stream recipe lives in the checker. Its owner (Release Method or the manifest schema) is not in the supply, so alignment of the recipe is evidenced only by the receipt's historical-manifest success.
- The Profile's own absent-material sentence is cut off in the supply, so I cannot confirm it cross-refers without duplicating.
- The resource source pins (IDENTITY_METHOD `258e…`, Frame Method `44bb…`, Spec `fbdc…`) are consistent with the digests cited elsewhere. I cannot recompute the IDENTITY pin. The positive receipt implies it matches the frozen bytes only if the receipt was taken at 8bb3213.
- Edits to the calculus and profile change their member digests. No basis has been issued, so no stale issued basis exists. Real re-issuance at publication belongs to Release Method and is not evidenced here.

## Evaluation by requested axis

- **Authority conservation:** I found no widening. The library imports are reference-only. The checker returns content and reference validity, with its limits stating that acceptance, derivation, admission and publication are separate. Frame views and the fixture mint no grant. UP-021 admission ownership is unchanged.
- **Fragment/address completeness:** Duplicate-address refusal and reconstructed-fragment resolution are mechanically evidenced. Population independence and the Profile fragment list are residuals.
- **Record and resource pins:** Shape, publication, source and reconstruction pins are all checked, and the path-escape and symlink guards are sound. Receipt-to-commit binding is the gap.
- **Expected-reason controls:** The exact-reason assertion is real. Coverage is partial, as listed under F2.
- **Evidence limits:** The limits are honestly stated in the receipts (hypothetical fixture, content-only, qualification tooling not an installed engine). Python 3.8 compatibility is syntax-only, as the DISTRIBUTION receipt itself says.

## Verdict

None of the five initial findings remains open. F1 and F2 are narrowed, and F3 and F4 are narrowed on evidence rather than text. F5 is closed. I found no authority-widening counterexample in the changed cone. The residuals are:

1. Population and fragment-list independence.
2. The unbound receipts.
3. Control gaps, and the unexercised ordinal-duplicate positive case.
4. The membership recipe owner and the truncated Profile text.
5. The renderer and checker heading-parser divergences.

Reliance on the construction and reference-resolution claims is reasonable, subject to those residuals. Nothing here supports a claim of semantic equivalence, owner acceptance, release or publication.
