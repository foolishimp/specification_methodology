# Independent review of Codex candidate `97e3484`: SPEC_METHOD.md and IDENTITY_METHOD.md

**Results:** SPEC_METHOD.md is **satisfied**. IDENTITY_METHOD.md is **satisfied**. I found no concrete contradiction introduced by the new Foundation or Transformation Library bindings.

**How this was assessed:** I used only the four texts you supplied and called no tools. That includes the advisor, because you said not to use tools. I compared the predecessor and successor text by reading them section by section, not with a byte diff. A mechanical diff would confirm the "verbatim" findings below; I did not run one.

---

## Member 1: SPEC_METHOD.md — **satisfied**

### Source first: conservation of predecessor determinations

Every predecessor section from Canonical Compression through ADR Folder Convention is carried in the successor unchanged, in the same order. I checked the most load-bearing sections closely:

- the recursive-product URNs;
- the Toolchain Manager command boundaries and Explicit Complete Consumer Update;
- semantic-resolution order and the conformance-case table, including its examples;
- `STDO-SURFACE-001`;
- C/J/O computed classification;
- STDO-UP-013, 014, 020, 021 (including the Standing Qualification table), 001, 008 and 022;
- Testing Strategy Taxonomy and the portability rule;
- the Reconstruction Litmus;
- the Bootstrap sequence, Method steps 1–11 and the ADR tables.

Under your rule, carried source wording is full local operative text. So every predecessor owner, predicate, permission, refusal, conditional applicability and invalidator is still present in the member.

### Complete successor: the three new preamble paragraphs

**¶1** calls SPEC_METHOD a refinement of Foundations and the Transformation Library. It says a purpose, subject, specification, evidence and owner grants "supply the premises of the constitutional chain," and that finite capacity alone confers no authority.
- This adds no link to the chain, and the Goals → … → Delta diagram is unchanged.
- It agrees with Foundations ("Foundational explanation does not transfer authority from a named detailed method owner") and with the Library ("does not supersede those meanings").
- No authority moves.

**¶2** maps Bind, Acquire, Transform, Evaluate, Conjoin and Dispose onto existing sections.
- It says they are not "compulsory workflow stages or runtime APIs."
- It ends with an explicit retention clause: the following clauses "retain their owners, predicates, permissions, refusals, lifecycle and invalidation conditions."
- It adds no new obligation, quota or interface.

**¶3** keeps graph-native meaning with ODD_METHOD and module realization with DESIGN_MODULE_METHOD, as conditionally applicable profiles.
- This conditionality comes from the predecessor itself: Method step 5 ("When … applies / does not apply") and UP-020 ("Where `DESIGN_MODULE_METHOD.md` applies").
- It does not narrow the "D — Design, owned by `DESIGN_MODULE_METHOD.md`" identity, which is carried verbatim. Its phrase "each detailed relation remains owned by its declared standard" makes clear the list is not exhaustive.

**Other checks:**
- **Construction-state narration:** none. There is no v3, candidate or tenant wording in the deciding text.
- **Test-to-Product leakage:** none.
- **Stronger category or Markov theorem:** none.
- **Anchors** to SPEC sections from Foundations and the Library resolve to existing headings: `#bounded-context-semantic-resolution`, `#product-outcome-conservation-stdo-up-013` and `#agentic-construction-execution-stdo-up-020`.

**Residual limit:** the body's links into REFERENCE_FRAME_METHOD and STDO_REFERENCE_FRAME_BASELINE were already in the predecessor. Whether they resolve in the successor is **out_of_frame** here.

---

## Member 2: IDENTITY_METHOD.md — **satisfied**

### Source first

The whole predecessor body is carried in the successor unchanged: Position through Consequence For Implementations. That includes:
- Core Law 1–4 and the minimum model `identity = authority + kind + value`;
- UP-004, with its full list of decisions: elevation, transfer, split, merge, proxy grant, revocation and retirement;
- the ABG defaults and override rules;
- Parsing Law;
- the Lawful and Unlawful examples.

### Complete successor: the three new preamble paragraphs

- **¶1:** "Equal representation alone supplies neither identity equality nor permission" matches the predecessor's readable-versus-opaque rule and UP-004. "Continuing identity alone supplies no claim that content … is current" matches Foundations' Identity, State and Evidence section and adds no new obligation.
- **¶2:** It disclaims any "mandatory identity format, runtime API, actor or workflow stage." Elevation and transfer requiring an owning decision is grounded in UP-004.
- **¶3:** Keeping engine, domain and release owners separate, and treating ABG as conditional, matches Authority Split, Defaults ("not universal doctrine") and Release Version Boundary.

### Observations (low technical severity; not falsifying)

**I-1. ¶1 coordinate list (successor ¶1 against predecessor Core Law §1):** "A declared owner, kind, scope, governing basis and lifecycle supply identity meaning."
- The list leaves out *value* and adds *governing basis* and *lifecycle*, mixing the object-identity model with UP-004's authority-identity coordinates.
- It is descriptive, not a "must," and the minimum model it sits beside is unchanged. So it creates no obligation.
- A reader could still take governing basis as a mandatory object-identity coordinate. That is an interpretive risk, not a contradiction.

**I-2. ¶2 decision list (successor ¶2 against UP-004):** "where elevation, transfer, supersession or retirement is required."
- It lists a subset of UP-004's decisions and adds supersession.
- It does not displace the full UP-004 list, which is carried verbatim.
- Supersession is grounded in the Stability Law ("make the relationship explicit") and UP-004's preserved supersession.

**Pre-existing, not introduced:** IDENTITY's "latest-accepted version-line selector" differs from SPEC's "highest-ordinal published immutable RC." Both texts are carried verbatim from the predecessor, so this is not a successor defect.

---

## New Foundation and Library bindings: no concrete contradiction found

Three apparent conflicts each resolve consistently:

- **Assessor versus disposition owner** (SPEC UP-020 Proportional Disposition: "Assessment returns one of these semantic dispositions"):
  - The Library's Evaluate section keeps the assessor's disposition classification as evidence alongside the predicate result. Dispose gives the authoritative selection to the decision owner.
  - The predecessor never gave assessors acceptance authority. A bounded proxy can still accept under the governing relation.
  - This is a reconciliation, not a transfer of authority, and the detailed UP-020 text governs.
- **No universal quota:** Library "Cost and contraction" says "Measure costs appropriate to the claim." This is limited to the claim, so it does not contradict UP-014's "No universal resource quota … follows."
- **Category and Markov claims:** both Foundations "Orthogonal descriptions" and Library "Composition law" explicitly disclaim universal theorems.

These Library and Foundations observations sit outside my assigned members, so I give them only a technical severity:

**L-1 (low). Library Recovery law against UP-020 Checkpoint:**
- The Library says: "Discarding retained work requires an owning decision explaining why repair is insufficient…"
- The source says: "A proposed restart identifies why repair … is insufficient…" — it requires no explicit owning decision.
- The word "proposed" implies someone decides, so the gap is small. But the Library says it is summarising UP-020, and `STDO-SURFACE-001` says a summary "cannot require a stricter … relation by compression." The source text governs.
- "Reassess only materially affected premises" should be read together with the source's "recompute the wider frontier where independence is unproved."

**L-2 (low). Foundations' symbol scoping against SPEC's Bounded-Context Semantic Resolution:**
- Foundations puts `U_foundation`, `Sigma_contract` and `kappa_interpretation` in "this foundational account" but gives no stable bounded-context identity.
- Under SPEC's own law, that means they lack a declared context. This is harmless only while no material boundary relies on them, which neither assigned member does.

**L-3 (low). Foundations "Purpose and interfaces" against UP-013 and UP-014:**
- The general rule "An obligation with no requiring purpose … must be justified or removed by its owner" is credited to the Product outcome law (UP-013). That law applies only within Product-outcome-bearing work waves.
- The rule fits method obligations better under UP-014 proportionality. The decision is still reserved to the owner, so this is a citation-precision issue only.

---

## Residual limits (not failures)

- **Out_of_frame (not supplied to me):**
  - the anchors Foundations and the Library point to in AXIOMATIC_CALCULUS (AC-014, AC-017), REFERENCE_FRAME_METHOD, DESIGN_MODULE_METHOD (UP-017, §8 Totality) and RELEASE_METHOD (UP-015);
  - TICKET_METHOD's ownership of "condition-based closure."
- Whole-release qualification, practical efficacy across the corpus, and publication are separate claims and were not assessed.
