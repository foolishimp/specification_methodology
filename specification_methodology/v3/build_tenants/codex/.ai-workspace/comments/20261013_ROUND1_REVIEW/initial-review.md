# Review: frozen Codex v3 repair cone 84c6ebd

**Role:** author-independent source reviewer. No effect or acceptance grant. This is not whole-C3 or release acceptance, and it does not rank tenants.

## Verdict

**Qualified, not clear for reliance.** The supplied normative prose shows no authority widening and no direct semantic regression against UP-016 or UP-021. Three things stop reliance:

- The proof claims go beyond what the prototype demonstrates.
- The acquisition and fidelity claims for the new frames cannot be checked from the supplied material.
- The verification-material rule has ownership and absence-disposition ambiguities.

## What holds

- **Transformation-admission specialization** (TRANSFORMATION_LIBRARY, new section; DESIGN_MODULE_METHOD, "Admission contract use"). It keeps UP-021 as sole owner of admission and standing-test semantics, as UP-016 states. A projected or satisfied judgment is evidence rather than a grant. The text disclaims a new schema, a common enum and an extra validation pass. The anchor `#admission-contract-use` resolves. I found no rival owner or grant.
- **Derivation verification material** (IDENTITY_METHOD, new section; AXIOMATIC_CALCULUS and TRAVERSAL_OCCURRENCE_PROFILE, new paragraphs). The additions disclaim acceptance, derivation, admission and publication. They add no field to the basis records, and the historical clauses are stated not to become operative. Both records still cannot be mixed up with the published carrier. This is consistent with the standalone-successor requirement.

## Findings

**F1. Fragment and population checks are weaker than the clauses say, and the checker has a hidden dependency (material).**

- *Owning clauses:* IDENTITY_METHOD "Derivation Verification Material" ("every required fragment resolves under the recorded semantic-address rule"); TRAVERSAL_OCCURRENCE_PROFILE "Exact Profile Identity" ("each fragment resolves one heading", population "exactly the … expansion of every derivation address").
- The prototype loads `anchors` from `../check_candidate.py`, found by a relative path outside the publication package. That rule is neither recorded in the verification material nor pinned by digest. This is a hidden executable dependency, and the clause says "recorded".
- Fragment resolution is set membership (`fragment in anchors(...)`). It cannot refuse duplicate headings, so "resolves one heading" is not demonstrated.
- `build` and `verify` both extract addresses with the same regex, `\]\(([A-Z_]+\.md#[a-z0-9-]+)\)`, over "Derivation Provenance". A link with a digit in the filename or an unusual fragment is dropped consistently by both. The check proves self-consistency, not "every derivation address". The count of 14 is not independent evidence.

**F2. Unsupported proof claims in the report (material).**

- *Owning clause:* the proof limits as supplied; IDENTITY_METHOD's "content and reference checks only".
- `predecessor_or_network_reads: 0` is a hard-coded literal, not a measurement. `verify` also reads an out-of-package module (F1).
- The positive case verifies a manifest, bases and signature that `fixture()` generated from the same bytes. It shows internal consistency only. The manifest `member_set_sha256` rule is invented for the fixture, and the printed basis identities exist only for that fixture. They must not be cited as issued.
- The negative-control `valid: true` is tautological. Controls catch `ValueError, KeyError, FileNotFoundError, TypeError, UnicodeError` and never assert the intended reason, so an incidental failure counts as a refusal. In the supplied report the stated reasons do match the case labels, but nothing enforces that.
- Control gaps:
  - duplicate or extra segments;
  - literal-segment tampering;
  - source-pin versus manifest mismatch;
  - a missing historical fragment, or a duplicate heading;
  - overlapping or out-of-order ranges;
  - a symlink or path-escape case.
- The proof limit says three members are reconstructed "without literal body bytes". `build` emits `literal_utf8` for every deleted or replaced line. These statements are compatible only if those three members are pure subsets of current bytes. That is unshown, and the resource is not supplied.

**F3. Frame routing is unverifiable, and the described scope may omit deciding owners (material for acquisition fidelity).**

- *Owning clauses:* standards/README "Responsibility views" and the added paragraph; stdo-work "Acquire the Responsibility Frame"; TRANSFORMATION_LIBRARY "Reference-only semantic imports" and the work-entry paragraph.
- The delta and supplied files omit `frames/TRIAGE_CARRIER.md`, `frames/CONSTITUTIONAL_DERIVATION.md` and `DERIVATION_SOURCES.json`. Claims that each view "names its owner sections and exact member digests" and makes acquisition "reproducible" are therefore unsupported here.
- The README says the constitutional-derivation frame "projects the library specialization and its deciding Design Method consumer". The Library table names UP-021 (SPEC_METHOD) as sole admission owner and UP-017 as the seam owner. SKILL routes "transformation admission" to that frame. If the frame matches the README description, it omits the admission-deciding owner. The README's re-entry caveat mitigates this but does not remove the risk of treating the frame as sufficient.
- The edits to the stdo-work routing paragraph and the README paragraph carry evaluation vocabulary into normative or entry prose: "a candidate's fixture answer" and "without an author's private selection". That signals tuning to a test and is not task-neutral rule text.
- The library edit changes the Library's member digest. Any digest-bound compression or frame referencing it needs regeneration. That is not shown.
- A stray blank line inserted after `## Bind` is cosmetic but unreviewed digest churn.

**F4. Ownership placement and absence disposition are ambiguous (moderate).**

- *Owning clauses:* IDENTITY_METHOD scope (the README table assigns it "Scoped names and exact identities"; "Exact cuts, successor conservation and publication" belong to Release Method); Profile "Exact Profile Identity".
- Byte reconstruction, manifest membership and refusal conditions are a publication and verification matter. They are placed in Identity Method and cited from the calculus and the profile. They duplicate refusal rules in Identity Method and the Profile ("Missing, duplicate… refuses"; "absent or defective material retains the refusal conditions above"). Identity Method adds "historical retrieval is optional… not a hidden fallback". It is unclear whether an installed predecessor is still a lawful alternative when the material is absent. The Profile says it is not required, but gives no explicit disposition.
- Reconstruction depends on the current bytes of source members. The text says changed sources require new material. This delta edits IDENTITY_METHOD, AXIOMATIC_CALCULUS and TRAVERSAL_OCCURRENCE_PROFILE, and the resource is outside the delta. I cannot confirm the resource pins postdate these edits if any of those files is a projection source. The edits also change the calculus and profile member digests, which invalidates any previously issued basis. That is correct under the Profile's rule, but no re-issuance is evidenced.

**F5. Library table wording, mild (low).**

- *Owning clauses:* TRANSFORMATION_LIBRARY transformation-admission specialization, row 2 ("domain declares material seams and proves far-side independence"); UP-021 ("each admission owner is independently responsible for deriving and validating the complete enclosing relation… owner assertions… do not establish truth").
- The row can be read as letting a domain declaration stand in for the owner's derivation. It should say the declaration is design evidence and UP-021 derivation remains per owner. UP-017 text was not supplied, so the row 2 and Design Method citations of it are unverifiable here.

## Limits

- I reviewed only the supplied material. The frames, the resource JSON, `check_candidate.py`, UP-017, PREDECESSOR_CLAIMS and the Frame Method were not supplied.
- I ran no code. All run results come from the supplied report.
- I did not assess predecessor-claim dispositions under STDO-UP-015, whole-C3 coherence, release adoption, or semantic acceptance of the historical derivation.
- Positive reconstruction would at most establish byte and reference consistency for the fixture.

**Recommended repair path:**
- Pin or record the semantic-address rule inside the material, with a duplicate-heading refusal.
- Derive the address population independently of the shared regex, or state that it is only self-consistent.
- Remove or instrument the `0` reads claim.
- Make the controls assert reasons and cover the missing cases.
- Supply the frames, resource and digests for review.
- Align the frame scope with UP-021 and UP-017, strip fixture language from normative prose, and state the absent-material disposition once, at one owner.
