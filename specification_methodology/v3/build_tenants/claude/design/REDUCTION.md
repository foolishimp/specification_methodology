# Claude Tenant Design: Reduction

This file applies the common
[Foundational Reduction Requirement](../../../specification/requirements/README.md#foundational-reduction-requirement)
to this tenant's candidate for iteration 3. It is tenant HOW, written by
Writer activation I3-1 under `EC-CLAUDE-I3-01` and completed by Writer
activation I3-2e (clusters R30 to R34, the loci marked "added by
I3-2e", design discrepancy c and section 4.7). It accepts nothing.

Terms, from the common requirements:

- A **determination** is a rule, definition, list of allowed values or
  procedure step that an actor must apply.
- A **consumer** is a rule or task entry that uses another rule's
  determination.
- The **shared owner** is the one section that states a determination.
  Every other section refers to it, or refines it with a map back to it.
- A **rival** is a section that decides the same question by its own
  determination, even if it also cites the owner. A **duplicate** restates
  the owner's determination consistently but still has to be kept
  consistent by hand.
- A **retained primitive** is a domain mechanism kept on purpose. It must
  state the distinction it supplies and why the shared owner does not
  already decide it.
- A **deciding path** is the rules, bindings and acquired information used
  from a declared entry to determine a permitted result or action for a
  task.
- A **reconciliation** is work an actor must do because two loci on its
  path disagree, overlap without a map, or use one label for two meanings.

Line references are to `build_tenants/claude/standards/` at the preimage
`5ab44d5`. Prefix `P:` marks the installed predecessor's
`standards/`. P abbreviations: AC AXIOMATIC_CALCULUS, BASE
STDO_REFERENCE_FRAME_BASELINE, DMM DESIGN_MODULE_METHOD, ODDM ODD_METHOD,
RF REFERENCE_FRAME_METHOD, SPEC SPEC_METHOD, TICKET TICKET_METHOD, TOP
TRAVERSAL_OCCURRENCE_PROFILE, UXM UX_METHOD.

## 1. Standing and sources of this inventory

The inventory comes from three read-only sweeps run inside activation
I3-1, each by a Claude-family helper:

- the candidate's recurring determinations, swept on owner vocabulary
  across the 23 members, frames, templates and plugin;
- the predecessor's questions decided in more than one place;
- the foundation-to-law tables of the 21 families (section 2).

The quotes it relies on were partly re-read at source by the helpers and
by this activation.

It is a lower bound:

- the sweeps searched on vocabulary, so a rival worded differently can be
  missed;
- consumer lists are samples;
- POSTING_GUIDE, WRITING_GUIDE, schemas and most templates were read only
  at search hits.

Activation I3-2e completed the inventory before the integrated
assessment, by its own read-only sweep at `5ab44d5`, with no helper:

- POSTING_GUIDE, WRITING_GUIDE and the 23 Markdown template files were
  read in full;
- `PRODUCT_DEFINITION_TEMPLATE.json` was read as its scalar values,
  without its URI and identifier lines;
- the two schemas were read by extracting every enumeration, constant,
  pattern and description. They state no value set and no rule beyond
  PRODUCT_DEFINITION and RELEASE, so they add no cluster;
- wording variants were searched across all 23 members, the templates
  and the plugin for these questions: what creates no authority, implicit
  activation and continuation, invalidation, closure conditions,
  promotion blocks, independence triggers, resource limits, hard-stop
  waivers, commentary standing, current-surface writing and version
  labels, value-like uses of "missing", and disposition vocabularies;
- each hit was read in context before it was classified.

What I3-2e added is marked "added by I3-2e" in the existing clusters,
plus five new clusters (R30 to R34), design discrepancy c and the paths
and coverage rows of section 4.7. The inventory is still a lower bound:
the variant search is lexical, and an actor's reading can still find a
rival that no search term reaches.

Source sample by I3-1: after the sweeps, this activation re-read 20 rival
loci at source, spread over R7, R11, R12, R14, R16 and R21:
- `SPEC_METHOD.md:902–905`, `:932`;
- `TICKETS.md:286`, `:1009`, `:1142`;
- `EVALUATION.md:101`, `:230–235`;
- `REFERENCE_FRAME.md:282–287`;
- `AXIOMATIC_CALCULUS.md:481`;
- `IDENTITY.md:194–198`;
- `ACTIVATION.md:403–409`;
- `EXECUTIVE_BASELINE.md:402`, `:656`, `:1290`;
- `UX.md:74`, `:737`;
- `DESIGN_MODULE.md:2272`;
- `PRODUCT_DEFINITION.md:656`;
- `FOUNDATIONS.md:851`;
- `templates/CLAUDE_TEMPLATE.md:13`.

All 20 hold as described. One reference was offset: the ACTIVATION proxy
limit is at `:408–409`, now corrected. The remaining loci rest on the
sweeps, which re-read about half their quotes.

Each "owner" below is a design decision of this file. The update of
[DOCUMENT_STRUCTURE](DOCUMENT_STRUCTURE.md#ownership-decisions) records
them beside D1 to D8 (PLAN I3-2e; recorded as D9). Section 3 lists what each rival
becomes. A change of predecessor meaning in doing so is a proposed
replacement relation for the product owner, never a silent edit.

| Requirement item | Where answered |
|---|---|
| 1, pillar contributions and the four-way split | section 2 |
| 2, recurring determinations, shared owner, consumers | section 3 |
| 3, distinctions kept, retained primitives, scope, force, triggers and exceptions | section 3, per cluster; guards in section 4 |
| 4, member boundaries from responsibilities | DOCUMENT_STRUCTURE, updated by I3-2e (D9, member map, conformance map) |
| 5, deciding paths against the two fixed baselines | section 4 |
| 6, challenge cases | section 5 and [PLAN §5](../qualification/C3-ITER3/PLAN.md#5-trial-design) |

## 2. Pillar account

The common Product's
[pillar table](../../../specification/PRODUCT.md#foundational-reduction)
names ten contributions. The product owner's sign-off on that list is
open (ledger, Iteration 3). This account binds the current list and
changes with it.

**State found.** The candidate binds no pillar. None of the 21 family
tables names a pillar contribution. The family-table format
(`FOUNDATIONS.md:496`) has columns for premises, consequence and policy
but none for a pillar. Relation 1 of the
[standalone successor requirement](../../../specification/requirements/README.md#standalone-successor-requirement)
requires the applicable pillar contributions to be bound to each
argument, so it is unmet for all 21 families. The candidate also uses the
word "pillar" for the four letters S, T, D and O (`SPEC_METHOD.md:94–97`,
`TICKETS.md:15`, `GLOSSARY.md:82`). That collides with the ten.

The table below is a reconstruction from the candidate's text, not a
claim the candidate makes. Coverage terms:

- **decided**: deciding rules and their consumers are present and argued;
- **partial**: rules are present, but the argument is weak, consumers are
  unbound, or a generic rule sits only in an optional profile;
- **missing**: no deciding rule.

| Pillar | Carrying rules | Consumers that apply them | Premises; consequences; policies (owner); implementation choices | Coverage |
|---|---|---|---|---|
| 1 Specification and project structure | SPEC_METHOD#2-the-chain, #3-outcome-conservation, #4-change-management; PRODUCT_DEFINITION#8-what-how-and-work-carriers; TICKETS#one-truth-state-projection-and-drift-refusal-up-009 | TICKETS:243 applies SPEC_METHOD §4; PRODUCT_DEFINITION:717 the tenant binding | P1, P2, P3, P6 and the owned-layer premises; the specification governs, trace closure, re-entry at the owner; six change classes (SPEC_METHOD), overlay and layout (PRODUCT_DEFINITION), carrier kinds (TICKETS); tag forms, JSON overlay, default layout | decided. Commentary ownership rests on POSTING_GUIDE, which has no family table |
| 2 World models, identity and Markov objects | FOUNDATIONS P3 (:387–401); IDENTITY#scoped-identity, #stability; WORLD_MODEL#admissibility, #discrimination, #epistemic-status; FOUNDATIONS#5-hypotheses; REFERENCE_FRAME#rf-003-material-sufficiency | EVALUATION:231; ACTIVATION:536 | P3, P6, the open-world premise; scoped identity, a boundary is a claim with a proof obligation, sufficiency without completeness; authority, kind, value, revision (IDENTITY), entity cut and Markov vocabulary (WORLD_MODEL); mean-offset overlay, Git ledger | partial. Boundary evidence is decided only in the optional WORLD_MODEL profile; the limit on stronger Markov claims is a §5 hypothesis and a profile status |
| 3 Algebraic calculus | FOUNDATIONS#4-algebra, P4a; FOUNDATIONS#conjunction-of-results; AXIOMATIC_CALCULUS#ac-013-transformation; ACTIVATION#refinement | ACTIVATION:264 and SPEC_METHOD §11 rule 4 (conjunction); DESIGN_MODULE:607; SPEC_METHOD:1740 | P4a, P4b, P0, P1, P2, P6; typed composition, record what is preserved, introduced and removed; AC-013 record fields; byte or typed equality, RFC 8785 | partial. "States what it preserves" has no bound consumer, and three places restate preservation on their own (cluster R29) |
| 4 Functional design | DESIGN_MODULE#4-functional-bias-and-typing, #10-realisation-rules, #3-boundary-closure-evaluators; SPEC_METHOD#realisation-shape; FOUNDATIONS §4 Shared machinery | DESIGN_MODULE:607; UX §6 effect membrane; ASSURANCE §14 to §16 | P1, P3, P4a, P5, P6; typed carriers, total functions, explicit effect edge; functional bias at "should" force (profile); Python, Mermaid, Elm | decided, inside the optional design profile; FOUNDATIONS:851 makes that profile own a tier-1 choice (cluster R21) |
| 5 Outcome-driven development | ODD#115d-constructive-evaluation-and-yield-loop, #graph-functions; ACTIVATION#transitions, #4-totality-and-refinement; AXIOMATIC_CALCULUS#ac-015-functor-classification; SPEC_METHOD §11 rule 2 | EXECUTIVE_BASELINE work result through ACTIVATION §3; CONFORMANCE:154 | P0, P2, P4a, P5, P6; closure is a fold over admitted evidence, yield is not failure, operation kind, actor and executor stay distinct; seven closure decisions (ODD); GTL and ABG realisations | decided. ODD §2, §3, §10, §11.2–11.3 and §16 to §20 are untraced; AC-015 has no consumer |
| 6 Information and interpretation | FOUNDATIONS P1 (:363–385); AXIOMATIC_CALCULUS#6-interpretation-and-models, #ac-011-projection; REFERENCE_FRAME#rf-017-proportional-compression, #evidence-or-coordinate-translation; EVALUATION#2-separation; PRODUCT_DEFINITION#5-bounded-context-semantic-resolution | SPEC_METHOD:1752; TICKETS:574 | P0, P1, P6; subject, representation and meaning stay distinct, a compression keeps material distinctions; translation loss (declarer), resolution order (PRODUCT_DEFINITION) | partial. The entry point ACTIVATION §2 (`:494`, `:498`) applies compression and capability fit through predecessor links (rc.2 RF-017, RF-014), not the successor's rules; EVALUATION:115 does the same for AC-018 |
| 7 Reference frames | REFERENCE_FRAME#1-the-frame-as-the-engagement-unit, #rf-002-finite-attention, #rf-003, #rf-006, #rf-014-capability-fit, #frame-set-selection; ACTIVATION#2-context-construction-under-an-envelope | ACTIVATION:484, :536; EVALUATION:413; EXECUTIVE_BASELINE:228–230 | P0, P2, P3, P6 and instance premises a to e; twelve frame-tuple components, frame set (human authority), Executive, Worker and Reviewer (profile); carrier format | decided. Defect: ACTIVATION:465, :498 and :600 cite RF-004, RF-014 and RF-003 by predecessor link |
| 8 Computational calculus and execution binding | SPEC_METHOD#11-build-tenant-binding (:1627–1765); FOUNDATIONS#accounts-of-a-construction; ACTIVATION#6-cost-and-proportionality; EVALUATION#6-conformance-of-realisations | ACTIVATION:1233; EVALUATION:413; CONFORMANCE:152–155 | P1, P2, P6 and others; the binding names operations, outcome values mapped to the core, resource units and boundaries; the three-part division (SPEC_METHOD), each tenant's calculus (tenant design) | partial. Evidence that a binding satisfies its calculus's laws is one sentence (rule 5) with no stated evidence form; the time and spend owner sits in tier 2 while tier-1 members depend on it (design discrepancy b, section 3) |
| 9 Evidence, correction and authority | FOUNDATIONS P6 (:471–481); EVALUATION#1-claims, #3-independent-assessment, #5-acceptance; ASSURANCE#12-counterexample-localisation; SPEC_METHOD#4-change-management; IDENTITY#6-authority-identity-and-conservation-stdo-up-004 | ACTIVATION:341; TICKETS:989; EVALUATION:231; EXECUTIVE_BASELINE:1556 | P0, P2, P5, P6; a claim names its falsifier, self-review is construction output, acceptance is the owner's disposition, a counterexample goes to the earliest causal frontier; triage scales (adopting Product), proxy grants (human authority) | decided. EVALUATION:69 and :78 are hollow arguments; ASSURANCE §12 has no linked consumer |
| 10 Axiomatic calculus | AXIOMATIC_CALCULUS#ac-004, #ac-007, #ac-008, #ac-009, #ac-010, #ac-011; REFERENCE_FRAME#rf-015-residual-uncertainty | TRAVERSAL_OCCURRENCE:855 (AC-007); ACTIVATION:450 (AC-010) | P1, P3, P4b, P5, P6; eight record kinds, ten obligations; RFC 8785, SHA-256 | partial. No member binds the use of a_c to build a task's constraint surface ("constraint surface" has no hit); AC-008, AC-009 and AC-015 have no consumer; the tenant's interpretation is stale (F3) |

**Tally.** Against the requirement: 0 of 10 pillars bound, 0 of 21
families naming one. By reconstruction: 5 decided (1, 4, 5, 7, 9), 5
partial (2, 3, 6, 8, 10), 0 missing.

**Family argument quality.** The 21 tables hold 286 rows. The helper
classed about 177 as argued, 103 as weak and 6 as hollow. A weak row cites
relevant premises without showing the link, often by listing four or more
commitments. A hollow row files a choice as a consequence that its
premises do not force, with no declared policy. The counts are ±20%; F16
and F17 are the least reliable. The hollow rows are `EVALUATION.md:69`,
`:78`, `IDENTITY.md:70`, `TICKETS.md:570`, `ODD.md:115` and
`WORLD_MODEL.md:183`. F3, F8 and F9 declare instance premises that no row
cites. 29 of the 35 rows of F12 to F14 list four or more commitments.
Deciding sections that no table traces include ODD §2, §3, §10,
§11.2–11.3 and §16 to §20, and six subsections of TICKETS §6
(`TICKETS.md:763–926`).

| Family | Locus | Rows | Argued / weak / hollow |
|---|---|---|---|
| F1 Frames and context | REFERENCE_FRAME:151–188 | 36 | 24 / 12 / 0 |
| F2 Transitions and configuration | ACTIVATION:57–66 | 8 | 6 / 2 / 0 |
| F3 Results | FOUNDATIONS:834–852 | 17 | 14 / 3 / 0 |
| F4 Work state and reuse | ACTIVATION:1098–1105 | 6 | 5 / 1 / 0 |
| F5 Proportionality | ACTIVATION:1254–1260 | 5 | 3 / 2 / 0 |
| F6 Claims and acceptance | EVALUATION:67–83 | 15 | 8 / 5 / 2 |
| F7 Conformance | EVALUATION:340–353 | 12 | 8 / 4 / 0 |
| F8 Identity | IDENTITY:58–70 | 11 | 7 / 3 / 1 |
| F9 a_c calculus | AXIOMATIC_CALCULUS:163–182 | 18 | 13 / 5 / 0 |
| F10 Chain and binding | SPEC_METHOD:163–177 | 13 | 9 / 4 / 0 |
| F11 Change management | SPEC_METHOD:722–733 | 10 | 7 / 3 / 0 |
| F12 Project binding | PRODUCT_DEFINITION:113–124 | 10 | 4 / 6 / 0 |
| F13 Work carriers | TICKETS:563–575 | 11 | 4 / 6 / 1 |
| F14 Assurance | ASSURANCE:87–102 | 14 | 7 / 7 / 0 |
| F15 Release | RELEASE:116–129 | 12 | 7 / 5 / 0 |
| F16 Engagement baseline | EXECUTIVE_BASELINE:223–243 | 19 | 10 / 9 / 0 |
| F17 Software design | DESIGN_MODULE:176–201 | 24 | 12 / 12 / 0 |
| F18 ODD | ODD:104–120 | 15 | 11 / 3 / 1 |
| F19 Traversal occurrence | TRAVERSAL_OCCURRENCE:76–86 | 9 | 7 / 2 / 0 |
| F20 UX | UX:120–131 | 10 | 6 / 4 / 0 |
| F21 World model | WORLD_MODEL:172–184 | 11 | 5 / 5 / 1 |

**Repairs this account selects** (scheduled in PLAN):

1. Add a pillar column to the family-table format and the family index,
   and bind each family's applicable contributions (I3-2a, then each
   member's table in wave 2). Rename the S/T/D/O sense of "pillar" (I3-2c).
2. Turn the 6 hollow rows and the weak rows into premise-to-consequence
   arguments or declared policies with owners. Cite the declared instance
   premises. Trace the untraced deciding sections (wave 2).
3. Pillar 10: state the use of the a_c interpretation to build a task's
   constraint surface at an owner (AXIOMATIC_CALCULUS §9, Application
   boundary), with its consumer at the acquisition step of ACTIVATION §2
   (I3-2b, I3-2a). Build the interpretation itself ([INTERPRETATION](INTERPRETATION.md)).
4. Pillar 6 and 7: re-point ACTIVATION §2's rc.2 links (RF-002, RF-003,
   RF-004, RF-014, RF-017) and EVALUATION:115 (AC-018) to the successor's
   own rules, keeping provenance separate (I3-2a, I3-2b).
5. Pillar 3: make the three restatements of preservation refer to
   ACTIVATION §4 Refinement and AC-013 (cluster R29).
6. Pillar 2: state the generic boundary-evidence and Markov-limit law in
   tier 1 (IDENTITY or FOUNDATIONS §2), with WORLD_MODEL as a refinement.
   The [single ownership requirement](../../../specification/requirements/README.md#single-ownership-requirement)
   item 8 requires generic law to be available without an optional
   profile (I3-2a or I3-2b by the owner chosen; WORLD_MODEL in I3-3d).
7. Pillar 8: give SPEC_METHOD §11 rule 5 an evidence form for a binding
   satisfying its calculus's laws, and resolve design discrepancy b
   below.

## 3. Reduction inventory

Each cluster is one question. **Owner** is the shared owner this design
fixes. **Refers or refines** lists sampled consumers. **Still deciding**
lists the rivals and duplicates found. **Removed** quotes the predecessor
and the candidate where a predecessor determination stated in several
places is now stated once. **Retained** lists primitives and whether
their need is stated. **I3 action** is what each rival becomes and the
activation that does it.

### R1 Core result values

- Owner: FOUNDATIONS §4 Results (`:671–686`).
- Refers or refines: RF-012 (`REFERENCE_FRAME.md:348–362`, "defines none
  of them"); `AXIOMATIC_CALCULUS.md:498–525` (map); `CONFORMANCE.md:27`;
  `ACTIVATION.md:614`. Duplicates: `UX.md:746`, `WORLD_MODEL.md:1179`,
  `DESIGN_MODULE.md:1428`.
- Still deciding:
  - `CONFORMANCE.md:24` and `EVALUATION.md:352`: "A case that cannot be
    run with the declared subject returns `out_of_frame`". The owner gives
    an evaluation that was not performed no result (`FOUNDATIONS.md:801`).
  - `TRAVERSAL_OCCURRENCE.md:760`: "Every constraint predicate returns
    exactly one of `satisfied`, `falsified`, `indeterminate` or
    `invalid_basis`". It drops `out_of_frame`. `AXIOMATIC_CALCULUS.md:524`
    maps constraint "out of scope" to `out_of_frame`, and
    `TRAVERSAL_OCCURRENCE.md:964` maps the stop `out_of_scope` to
    `falsified`. No clause states the narrowing as a signature
    refinement.
- Removed:
  - Predecessor, several value sets:
    - P:RF:409–412, "Every evaluation returns a member of its declared
      result algebra";
    - P:AC:414–415, "A failed, missing, indeterminate, out-of-scope, or
      invalid-basis result follows the declared result algebra";
    - P:TOP:679, a four-value set.
  - Candidate: `FOUNDATIONS.md:684–686`, "This core is the only one.
    Results of constraints, judgments, frame evaluations, stops, work
    steps and effects are stated in it or in a refinement mapped into
    it".
  - "Missing" is no longer a value. It is the absence of a result
    (`FOUNDATIONS.md:721`).
- Retained: none.
- I3 action:
  - CONFORMANCE and EVALUATION record an unrunnable case as a planned
    evaluation with no result (I3-2b for EVALUATION, I3-3k for
    CONFORMANCE).
  - TRAVERSAL states its constraint value set as a refinement of AC-007
    with the reason for excluding `out_of_frame`, and aligns `:964` with
    `AXIOMATIC_CALCULUS.md:524` or states the predicate difference
    (I3-3g).

### R2 Conjunction of results

- Owner: FOUNDATIONS §4 Conjunction of results (`:863–955`, gaps `:887`,
  reported value `:912`).
- Refers or refines:
  - `REFERENCE_FRAME.md:572–579` ("defines no conjunction of its own");
    `ACTIVATION.md:262–265`; `ASSURANCE.md:625–628`;
    `SPEC_METHOD.md:924`; `TICKETS.md:1121`.
  - Refinements: RF §5 `conjoin` adds `conflict` → `falsified`, with its
    need stated (`REFERENCE_FRAME.md:527–529`); the RF §8 coverage ledger
    (`:697`).
- Still deciding:
  - `EXECUTIVE_BASELINE.md:991–993`, "A missing or non-commuting seam
    returns the applicable `falsified`, `indeterminate`, `out_of_frame` or
    `invalid_basis`". Under the owner a missing result is a gap with no
    value.
  - `EVALUATION.md:454`, "declared veto return conflict, indeterminate or
    refusal", a third vocabulary.
  - Stale inputs, two answers: `FOUNDATIONS.md:881` treats a stale
    component as a gap (`indeterminate`); `REFERENCE_FRAME.md:277` and
    `EXECUTIVE_BASELINE.md:619` treat stale as `invalid_basis`.
- Removed:
  - Predecessor:
    - P:RF:688–690, "Missing, wrong-subject, conflicted or indeterminate
      mandatory results remain unresolved under the declared rule";
    - P:BASE:769–770, "A missing or non-commuting seam returns the
      applicable `falsified`, `indeterminate`, `out_of_frame`, or
      `invalid_basis` result".
    - These two disagree on a missing result.
  - Candidate: FOUNDATIONS §4 defines conjunction "here once, over the
    core". The BASE sentence survives in `EXECUTIVE_BASELINE.md:991`, so
    the predecessor's reconciliation is only partly removed.
- Retained: the choice among non-satisfied values for the reported value
  ("no universal order"), with its need stated at the owner.
- I3 action:
  - The owner states the two stale predicates (a result bound to a
    superseded basis is `invalid_basis` for the current evaluation; a
    conjunction component without a current result is a gap). RF and EB
    refer to it (I3-2a).
  - `EXECUTIVE_BASELINE.md:991` refers to the gap rule (I3-3a).
  - EVALUATION:454 maps its veto outcomes (I3-2b).

### R3 Work-step result variants

- Owner: ACTIVATION §3 Construction availability (`:677–724`) and
  Disposition (`:725–743`).
- Refers or refines: `EXECUTIVE_BASELINE.md:425–452` ("ACTIVATION §3 owns
  their grounds"), `PRODUCT_DEFINITION.md:422`, `UX.md:767`;
  dispositions at `TICKETS.md:296` and `DESIGN_MODULE.md:1457`.
- Still deciding:
  - `EXECUTIVE_BASELINE.md:442`, "`incomplete` (`falsified`): the Worker
    produced no candidate". That ground also fits `refused` and
    `re_entry_requested`.
  - `EXECUTIVE_BASELINE.md:439` restates `candidate_ready` without the
    owner's prohibition and refusal ground.
  - `ODD.md:1049` grounds `repair(*)` in `local_repair` (→ `falsified`)
    but maps `repair(proof)` to `indeterminate` (`ODD.md:1071`).
- Removed:
  - Predecessor: P:BASE:463–500 maps the variants "disjoint by their
    accompanying Reference Frame Method result". The mapping is restated
    at P:BASE:638, 1316–1323 and 1659.
  - Candidate: `EXECUTIVE_BASELINE.md:425`, "ACTIVATION §3 owns their
    grounds". `incomplete` → `falsified` for availability is a proposed
    replacement (rows 516, 522, 543, 560 and 565 split into `superseded`
    children), pending the product owner's acceptance.
- Retained: none.
- I3 action:
  - EB quotes no grounds of its own; it applies the owner's grounds by
    reference and keeps only its profile binding (I3-3a).
  - ODD either maps `repair(proof)` consistently or states the predicate
    that makes it differ (I3-3c).

### R4 Effects, uncertain completion and retry

- Owner: ACTIVATION §3 Effects (`:791–839`) for values;
  ACTIVATION §5 (`:1047–1053`) for reconciliation before repetition.
- Refers or refines: `TRAVERSAL_OCCURRENCE.md:1326–1344`,
  `PRODUCT_DEFINITION.md:404`, `FOUNDATIONS.md:718`,
  `EXECUTIVE_BASELINE.md:1094`, `ODD.md:1068`. `SPEC_METHOD.md:894–899`
  holds the retry preconditions and defers reconciliation, so it
  complements the owner.
- Still deciding:
  - `plugins/spec/references/GETTING_STARTED.md:550` and
    `plugins/spec/skills/stdo-status/SKILL.md:56`, "the effect owner's
    retry rule". These gate repetition on a retry rule rather than on
    reconciliation, and cite no owner.
  - Suspected: `PRODUCT_DEFINITION.md:416–418`, "a restoration not
    verified is `completion_unknown` … never … `not_effected`", the F2
    pattern ([F1-F5](../qualification/C3-ITER3/F1-F5.md#f2)).
- Removed:
  - Predecessor, values without a core map and a rule with no values:
    - P:TOP:141–142, "`EffectDisposition.value.disposition` is one of
      `no_effect`, `completed_effect`, `partial_effect`, or
      `refused_effect`";
    - P:SPEC:1314–1316, "cannot be silently treated as no effect".
  - Candidate: `ACTIVATION.md:793–795`, "An effectful step's intended
    external effect has one of three values, mapped for the predicate
    'the intended effect occurred'".
- Retained: the end-of-effect residual, with its need stated at
  `ACTIVATION.md:835`.
- I3 action:
  - The plugin texts cite ACTIVATION §5 reconciliation (I3-3d).
  - PRODUCT_DEFINITION:416–418 is checked against the owner and repaired
    if it masks non-attainment (I3-3h).

### R5 Stops and refusals

- Owner, split by layer:
  - ACTIVATION §3 owns the generic stop contract (`:140`, `:642–675`,
    with refusal causes as part of the value);
  - ACTIVATION §4 owns hard stops (`:856–864`);
  - RF §5 owns `activation_refusal(capability|authority|basis)` and the
    translate refusals (`REFERENCE_FRAME.md:519–526`);
  - AC-007 owns `hold`, `gap` and `refusal(constraint|basis)`
    (`AXIOMATIC_CALCULUS.md:532–541`).
  - Each refinement maps to the core.
- Refers or refines: `TRAVERSAL_OCCURRENCE.md:925–930, 957`,
  `EXECUTIVE_BASELINE.md:455`. Duplicate: `AXIOMATIC_CALCULUS.md:926`
  restates the parent-value rule.
- Still deciding:
  - `TRAVERSAL_OCCURRENCE.md:760` (as R1).
  - `EXECUTIVE_BASELINE.md:619`, "A stale or substituted basis is
    `invalid_basis`. Missing material scope is `out_of_frame`", which
    gives direct core values with no refinement or predicate.
  - `templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md:86` and
    `EXECUTIVE_BASELINE.md:393–396` use "non-waivable … hard stops", a
    kind the owner does not define. EB says the Product basis binds them
    "whose owner is ACTIVATION §4", but the division between binder and
    owner is not stated.
- Removed:
  - Predecessor, refusals with no core map: P:BASE:488–490
    `activation_refusal`, P:RF:616–619, AC's three stops and TOP's six
    (P:TOP:668–676).
  - Candidate: `REFERENCE_FRAME.md:523–526`
    `activation_refusal(capability|authority|basis)`, each mapped; TOP's
    extra stops enter through the stop contract
    (`AXIOMATIC_CALCULUS.md:925`).
- Retained: the AC stop algebra (`AXIOMATIC_CALCULUS.md:588`); TRAVERSAL
  `out_of_scope`, with its need stated at `:964`.
- I3 action:
  - EB:619 refers to RF-005 and the owner (I3-3a).
  - The template and EB use the owner's hard-stop term (I3-3a, I3-3d).

### R6 Context fit, remedies and attention

- Owner: ACTIVATION §2 for size, fit test and remedies (`:463–505`);
  EVALUATION §7 for adequate attention (`:395`); FOUNDATIONS for the
  no-trimming rule (`:607`).
- Refers or refines: RF-002 (`REFERENCE_FRAME.md:243`, fit against
  attention kept apart at `:251`), `EVALUATION.md:347`.
- Still deciding:
  - The remedy list is stated at both `REFERENCE_FRAME.md:372–380` and
    `ACTIVATION.md:487–493`.
  - `AXIOMATIC_CALCULUS.md:646` restates the no-trimming rule.
  - `REFERENCE_FRAME.md:461` restates "no universal budget".
  - `CONFORMANCE.md:70`, "Trials declare a per-actor context cap and
    total-work budget", cites no owner.
  - The entry point applies predecessor rules: `ACTIVATION.md:465`,
    `:494`, `:498` and `:600` cite rc.2 RF-004, RF-017, RF-014 and RF-003
    by `stdo://` link instead of the successor's own sections.
- Removed:
  - Predecessor: "no universal budget" at both P:RF:535 and P:BASE:359;
    the remedies at P:RF:430–435 (RF-014); trimming at P:AC:456.
  - Candidate: a single size measurement and fit test at
    `ACTIVATION.md:463–505` (D2). Fit and attention each have one owner,
    so the two-decider pattern Codex's review found in its own candidate
    is absent here.
- Retained: none.
- I3 action:
  - RF refers for the remedy list and the budget statement (I3-2b).
  - AC refers for trimming (I3-2b).
  - CONFORMANCE cites ACTIVATION §2 and §6 (I3-3k).
  - ACTIVATION §2 binds the successor's RF sections and keeps provenance
    separate (I3-2a).

### R7 Reuse and invalidation

- Owner: ACTIVATION §7 (`:1262–1283`, list at `:1271–1279`); hash-only
  reuse at `EVALUATION.md:474`.
- Refers or refines: `EVALUATION.md:293`, `TICKETS.md:991`,
  `EXECUTIVE_BASELINE.md:464`, `DESIGN_MODULE.md:1906`.
- Still deciding:
  - `SPEC_METHOD.md:902–905`: "A changed request, candidate, basis, owner
    or root relation, projection, design trace or acceptance, rule,
    configuration …", its own trigger list.
  - `SPEC_METHOD.md:932`: "[TICKETS §7] owns work-state recording and
    reuse", which names the wrong owner.
  - `TICKETS.md:1142`: "A material counterexample, changed evidence or a
    changed basis invalidates", which omits the revising observation.
    Partial restatements are at `TICKETS.md:1065–1070` and
    `DESIGN_MODULE.md:1897–1902`.
  - `EVALUATION.md:101`: "Evidence change may invalidate a verdict", which
    is permissive where the owner is mandatory.
  - Duplicates of the digest rule are at `PRODUCT_DEFINITION.md:876`,
    `DESIGN_MODULE.md:1889`, `SPEC_METHOD.md:855` and `ASSURANCE.md:788`.
  - Added by I3-2e, further trigger lists that cite no owner:
    - `plugins/spec/skills/stdo-work/SKILL.md:146–147`: "Function
      boundaries alone do not invalidate them; mutation, rollback,
      authority/basis change and actual trust boundaries" do, its own
      list; `:165` and `stdo-ticket/SKILL.md:74` ("invalidate only
      affected support"); `GETTING_STARTED.md:525`;
    - the basis template, `PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md:160–164`
      ("checking its question, subject/basis, evidence and invalidators
      … a new role or session alone does not"), `:184–187` (its own
      fourteen change kinds) and `:191–192`;
    - `REFERENCE_FRAME.md:629–630`, "Changing any material member may
      invalidate the coverage result", permissive like EVALUATION:101;
    - `EXECUTIVE_BASELINE.md:1442`, "a changed candidate or basis
      invalidates the affected review result", a subset list; `:546` and
      `:814–815` are narrower restatements;
    - domain lists: `ASSURANCE.md:728` (testing-frame invalidation, a
      full list of its own), `DESIGN_MODULE.md:388`, `WORLD_MODEL.md:286`.
- Removed: partly. The predecessor has five differing invalidator lists:
  P:RF:635–640, P:SPEC:1318–1321, P:TICKET:787–793 and 885–887,
  P:DMM:2180–2187, P:BASE:497–500. Under the predecessor an actor takes
  their union. The candidate names one owner, but four rival lists
  remain.
- Retained: the admission-fact triggers (`ACTIVATION.md:966`), whose need
  is given by provenance only.
- I3 action: every list refers to ACTIVATION §7. A domain trigger, such as
  a projection change, is stated as a named instance of the owner's
  material-input change, never as a parallel list. EVALUATION:101 takes
  the owner's mandatory force (I3-2b, I3-2c, I3-3b).
  Added by I3-2e: the plugin and template lists refer to ACTIVATION §7
  (I3-3d); RF:630 takes the owner's force (I3-3j, which holds
  REFERENCE_FRAME after I3-2b); EB:1442, :546 and :815 refer (I3-3a);
  ASSURANCE:728 states its list as named instances of the owner's
  material-input change (I3-3h); DM:388 and WM:286 likewise (I3-3b,
  I3-3d).

### R8 Frame revision and diagnostic order

- Owner: REFERENCE_FRAME §10 for the diagnostic order (`:816–829`) and
  for coordinates (`:846–898`); ACTIVATION §7 for result validity.
- Refers or refines: RF-011 (`REFERENCE_FRAME.md:343`),
  `ACTIVATION.md:1050`, `EXECUTIVE_BASELINE.md:1682`.
- Still deciding:
  - `EXECUTIVE_BASELINE.md:1273–1281` reads the owner's order "with two
    specific steps" but drops step 5, the missing material variable. Its
    only reason is "(P2, P6)".
  - `REFERENCE_FRAME.md:889`: "newly acquired admissible evidence that
    bears on a closed result, reopens that result". That is broader than
    ACTIVATION §7's "declared revising observation", an internal seam left
    by the F1 repair.
- Removed: the predecessor's two eight-step orders (P:RF:922–935,
  P:BASE:1517–1526) become one owner with one profile reading.
- Retained: none.
- I3 action:
  - EB applies the full order or states the profile reason for omitting
    step 5 (I3-3a).
  - RF §10 and ACTIVATION §7 use one trigger term (I3-2a, I3-2b).
  - The MT-9 and MT-2 owner rulings ([F1-F5](../qualification/C3-ITER3/F1-F5.md#f1))
    land here.

### R9 Resumption from the workspace

- Owner: ACTIVATION §5 (`:1039–1107`).
- Refers or refines: `SPEC_METHOD.md:894`, `TRAVERSAL_OCCURRENCE.md:1047`.
- Still deciding: duplicates of "grants no restart authority" at
  `EVALUATION.md:297` and `SPEC_METHOD.md:340`, beside the owner at
  `ACTIVATION.md:1063`.
- Removed: not a predecessor reduction case. In the predecessor it
  appears only inside the R7 reuse rules and P:SPEC:1642.
- Retained: ODD replay-visible resume (`ODD.md:917`, need stated at
  `:1177`); UX message replay (`UX.md:403`), need not stated.
- I3 action:
  - The duplicates become references (I3-2b, I3-2c).
  - UX states the need for its replay primitive (I3-3d).

### R10 Applicability and not applicable

- Owner: ACTIVATION §1 applicability (`:251–273`). A false premise
  "excludes only that obligation"; unknown applicability is "unresolved,
  not false".
- Refers or refines: `TICKETS.md:1124`, `SPEC_METHOD.md:765`. Maps:
  `DESIGN_MODULE.md:1418` (`not_applicable` → `satisfied` under the
  disjunctive predicate "meets the axiom or does not apply") and
  `REFERENCE_FRAME.md:699` (`excluded_by_authority` → `satisfied`).
- Still deciding:
  - The owner does not say whether an exclusion is a result.
    `SPEC_METHOD.md:609` and `DESIGN_MODULE.md:54` say exclusions are "not
    results, and map to no core value"; `DESIGN_MODULE.md:1418` and
    `REFERENCE_FRAME.md:699` map them to `satisfied`.
  - The lifecycle three-state rule is decided at both
    `SPEC_METHOD.md:600–602` and `ASSURANCE.md:1040–1044`.
  - `plugins/spec/skills/stdo-work/SKILL.md:111`: "an unknown condition
    needs a bounded resolution or explicit residual". The owner instead
    withholds the dependent claim.
  - Added by I3-2e: the basis template `:58–61` restates the owner ("A
    false predicate excludes only its own obligation; an unknown predicate
    does not mean false"), a duplicate in agreement; I3-3d makes it refer.
- Removed: the predecessor stated "unresolved, not false" twice (P:RF:592–608,
  P:TICKET:874); the candidate states it once. The lifecycle rule
  (P:SPEC:1169, P:DMM:1838–1845) is still stated twice.
- Retained: design-grounded `not_applicable` (`ACTIVATION.md:1020`,
  `DESIGN_MODULE.md:818`).
- I3 action:
  - The owner states that an exclusion is no result. A predicate the
    owner declares as a disjunction may count "does not apply" as
    satisfying that predicate only. Consumers refer (I3-2a).
  - One owner for the lifecycle rule; the other refers (I3-2c).
  - The skill text refers (I3-3d).

### R11 Independence and authorship

- Owner: EVALUATION §3 (`:123–157`).
- Refers or refines: `FOUNDATIONS.md:136`, `EXECUTIVE_BASELINE.md:1390`.
- Still deciding:
  - `TICKETS.md:1005–1010`: "Independent review is required at product,
    qualification, release and explicitly risk-bearing boundaries", its
    own triggers. EVALUATION:75 leaves the triggers to "the governing
    basis".
  - `EXECUTIVE_BASELINE.md:1103` gives its own trigger list and cites
    EVALUATION §3, which does not state it.
  - Added by I3-2e: `plugins/spec/references/GETTING_STARTED.md:603`
    acts on "independent review is required" and adds "freeze before
    material reference exposure where generic-method qualification
    requires it", a condition no member states. The skill refers to the
    TICKETS triggers and states the freeze as an instance of an owner
    rule, or it is reported for an owner (I3-3d).
  - `EXECUTIVE_BASELINE.md:885` credits EVALUATION §3 with a traceability
    rule that sits at `TICKETS.md:1013`.
  - "Author identity" is defined only at `SPEC_METHOD.md:1656`; EVALUATION
    §3 does not import it.
- Removed: partly. The predecessor decides independence at P:TICKET:729–738
  (UP-007), P:RF:208–224 and P:SPEC:1561–1566. The candidate has one owner
  for what counts as independent; the triggers are still split.
- Retained: none stated.
- I3 action:
  - TICKETS keeps the trigger boundaries as a Spec Method policy (UP-007)
    and names EVALUATION §3 for what counts as independent. EB refers to
    TICKETS for triggers (I3-2c, I3-3a).
  - Author identity moves to EVALUATION §3, with SPEC_METHOD §11
    referring (I3-2b).

### R12 Authority, capability and a passing check

- Owner: FOUNDATIONS §2 Authority kinds (`:116–134`; the list of what
  cannot create authority at `:127`); EVALUATION `:110` (each check
  establishes only its own claim); EVALUATION §5 for acceptance (`:219`).
- Refers or refines: `RELEASE.md:607`, `ACTIVATION.md:407`; AC-005
  points to FOUNDATIONS.
- Still deciding:
  - Differing lists of what cannot create authority:
    - `REFERENCE_FRAME.md:282–287`, RF-006: "available capability, evidence
      shape, implementation reachability or frame selection";
    - `AXIOMATIC_CALCULUS.md:481`;
    - `IDENTITY.md:194–196`;
    - `DESIGN_MODULE.md:769`;
    - `PRODUCT_DEFINITION.md:77`.
  - The proxy limit is stated at `EVALUATION.md:230–235`,
    `ACTIVATION.md:408–409` and `IDENTITY.md:198`.
  - "Recording a result without review" is stated at `ACTIVATION.md:426`,
    `TICKETS.md:1135` and `EXECUTIVE_BASELINE.md:171`.
  - Added by I3-2e, domain instances of "creates no authority" that cite
    no owner: `REFERENCE_FRAME.md:320` (an exchange), `EXECUTIVE_BASELINE.md:48`
    (a role), `AXIOMATIC_CALCULUS.md:407` (latitude), `ACTIVATION.md:1200`
    (capability), `SPEC_METHOD.md:819` (C/J/O annotations),
    `plugins/spec/skills/stdo-review/SKILL.md:49` (test presence). Each
    agrees with FOUNDATIONS:127. The lists that make a result or tool
    output authorise continuation are cluster R31.
  - Resolution of the two loci 4.6 left conditional on I3-2e:
    `DESIGN_MODULE.md:769` ("Composition does not widen authority
    implicitly") and `PRODUCT_DEFINITION.md:77` ("A URI locator,
    filename, path or display label cannot mint or widen identity
    authority") are domain instances that agree with the owner. Neither
    yields a different outcome, so no path is added (4.7).
- Removed: no. The predecessor already had differing lists
  (P:RF:361–364, P:IDENTITY:220–222) and two proxy limits (P:RF:203,
  P:IDENTITY:225). The candidate keeps the pattern.
- Retained: none stated.
- I3 action:
  - One list at FOUNDATIONS:127, which the others cite, adding only
    domain instances.
  - One proxy-limit owner, FOUNDATIONS Authority kinds, with EVALUATION
    and IDENTITY referring.
  - One owner for recording a result without review, ACTIVATION §1, with
    the others referring (I3-2a, I3-2b, I3-2c, I3-3b).
  - Added by I3-2e: each domain instance cites FOUNDATIONS:127 and keeps
    only its domain term: RF:320 in I3-3j; EB:48 in I3-3a; SM:819 in
    I3-3f; the skill in I3-3d. AC:407 and ACTIVATION:1200 are prose that
    only I3-2b and I3-2a hold, outside their intake; the Executive extends
    those intakes or schedules a follow-up (return I3-2e).

### R13 Successor dispositions and other disposition vocabularies

- Owner: RELEASE §9 (`:641–659`) for the four UP-015 values.
- Refers or refines: `FOUNDATIONS.md:37`, `TICKETS.md:1104`.
- Still deciding:
  - `SPEC_METHOD.md:1466` classifies inherited material as "adopted,
    superseded, deferred or orphaned", and `SPEC_METHOD.md:494–500` keeps
    the legacy table. No clause relates either to RELEASE §9.
  - The members' own source-disposition tables use values outside the
    four:
    - `PROFILES.md:136–142`, "withdrawn" and "unresolved, pending the
      product owner's ruling"; "unresolved" blocks qualification under
      `RELEASE.md:653`;
    - `ACTIVATION.md:1322`, "superseded in its mapping";
    - `ASSURANCE.md:1096`, "conserved in part here".
- Removed: no. The predecessor already had three unaligned vocabularies:
  - P:RELEASE:507, conserved / superseded / intentionally removed / not
    applicable;
  - P:SPEC:2597, adopted / superseded / deferred / orphaned;
  - P:TICKET:812, retained / superseded / deferred / withdrawn.
- Retained: inherited-material classification may be a different
  question (adoption of working material, not successor claims). Its need
  is not stated.
- I3 action:
  - SPEC_METHOD states the predicate of its classification and its
    relation to RELEASE §9, or maps it (I3-2c).
  - Source-disposition tables use exactly the four values, splitting rows
    where a section is partly conserved (I3-2a to I3-3d, each in its own
    members).

### R14 Lifecycle and closure labels that decide

- Owner: FOUNDATIONS §4 Refinements (`:743`) for the mapping rule;
  ACTIVATION §3 Disposition (`:725–743`) for acceptance dispositions.
- Refers or refines: maps at `TICKETS.md:284`, `ODD.md:447, 1064`,
  `DESIGN_MODULE.md:1407`, `UX.md:713`, `WORLD_MODEL.md:1131`,
  `TRAVERSAL_OCCURRENCE.md:959` and `ASSURANCE.md:668`. Declared states
  with their need stated at `TICKETS.md:505, 1100`, `SPEC_METHOD.md:502`
  and `CONFORMANCE.md:14`.
- Still deciding:
  - `UX.md:259` and `UX.md:302` give two compliance tests; `UX.md:737`
    records that they disagree and are "pending the product owner's
    ruling". The conflict is inherited from P:UXM:125 against P:UXM:333.
  - `EXECUTIVE_BASELINE.md:402` decides that a finding "blocks the current
    promotion boundary, requires narrowing, or may remain an explicit
    residual", with no core map and no declaration as a state.
  - `TICKETS.md:286` calls close classifications "Like a disposition". They
    form a second set beside ACTIVATION's four dispositions, mapped by a
    separate predicate only.
  - The closure condition is duplicated at `SPEC_METHOD.md:924`,
    `TICKETS.md:1121`, `EXECUTIVE_BASELINE.md:1651`, the basis template
    `:165` and `plugins/spec/skills/stdo-ticket/SKILL.md:68`;
    SPEC_METHOD and TICKETS each cite the other.
  - Added by I3-2e: `SPEC_METHOD.md:1580–1582` (§9 Evidence), "Closure
    requires authority trace, realisation proof, negative proof where
    drift is plausible, and a present-tense statement of the residual open
    pressure", a second closure condition with a different content list
    that neither SPEC_METHOD:924 nor TICKETS:1121 relates to;
    `TICKETS.md:111`, "Ticket completion requires every closure-bearing
    milestone to be accepted", a milestone-level condition stated beside
    the owner.
- Removed:
  - UP-020 dispositions: predecessor P:SPEC:1601–1606 (table) and
    P:BASE:1416–1420 ("`STDO-UP-020` disposition within its grant:
    `accept`; `local_repair`; `re_enter`; or `reject`"); candidate
    `ACTIVATION.md:727–728`, "The decision owner disposes an assessed
    candidate with one of four semantic dispositions".
  - Design gate: predecessor P:DMM:1469–1471, "the Ontology and design
    verdict must both be `accepted` before …" as its own verdict;
    candidate `DESIGN_MODULE.md:1453–1458`, "`accepted` is the disposition
    `accept`, which maps to `satisfied`".
  - Sprint close: P:TICKET:327–332 and P:UXM:431–436 stated the same six
    classes; the candidate owns them at `TICKETS.md:272–301` and
    `UX.md:623` refers.
- Retained: ODD's seven closure decisions, mapped at `ODD.md:1064–1076`
  with the predicate difference stated. Two homonym hazards remain:
  `repair(proof)` → `indeterminate` against `local_repair` → `falsified`,
  and `re-enter(undeclared)` → `out_of_frame` against `re_enter` →
  `invalid_basis`.
- I3 action:
  - The UX conflict goes to the product owner as a ruling request; until
    then it stays unresolved (I3-3d).
  - EB:402 is mapped or declared a state with its purpose (I3-3a).
  - TICKETS states how close classifications return through the
    dispositions (I3-2c).
  - One owner for the closure condition, TICKETS, with the others
    referring (I3-2c, I3-3a, I3-3d).
  - ODD resolves the homonyms (I3-3c).
  - Added by I3-2e: SPEC_METHOD:1580 states its four items as evidence
    the owner's condition requires for a realisation claim, or refers;
    TICKETS:111 states how milestone acceptance relates to the owner's
    condition (I3-3f).

### R15 Build-tenant binding

- Owner: SPEC_METHOD §11 (`:1627–1765`).
- Refers or refines: `PRODUCT_DEFINITION.md:713`, `FOUNDATIONS.md:256`,
  `TICKETS.md:335`.
- Still deciding: none.
- Removed: the predecessor had no owner; this is new law. It is listed
  for completeness and as the control path DP-26.
- I3 action: the pillar 8 evidence form (section 2, repair 7).

### R16 Configuration, roles and direct entry

- Owner: ACTIVATION §1 Configuration (`:284`, "prescribes no role
  inventory, hierarchy, coordinator"; direct entry at `:420–430`);
  RF-009 (`REFERENCE_FRAME.md:309`).
- Refers or refines: `FOUNDATIONS.md:50`, `EXECUTIVE_BASELINE.md:1333`.
- Still deciding:
  - The lists of distinct relation structures disagree:
    `EXECUTIVE_BASELINE.md:656` has three, `ACTIVATION.md:322` four,
    `REFERENCE_FRAME.md:980` three and RF-009 six.
  - `EXECUTIVE_BASELINE.md:1290`: "this profile's executive configuration
    or another, is admitted by the smallest existing project authority".
    This is generic law in an optional profile.
  - `templates/CLAUDE_TEMPLATE.md:13` and `AGENTS_TEMPLATE.md`, and the
    plugin's `stdo-work` skill (`:117`), `stdo-help` skill (`:53`) and
    `GETTING_STARTED.md:486`: "use Executive or the declared project
    equivalent for material coordination". `ACTIVATION.md:373` says the
    executive profile "is not the method's default".
  - `EXECUTIVE_BASELINE.md:165–178` repeats `TICKETS.md:1134–1138`.
  - Added by I3-2e: the basis template's sections "Executive Attention,
    Evaluation, And Action" and "Activation And Return Topology"
    (`PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md:103–143`) give every
    project a coordinated Executive topology and state EB's rules
    ("Executive performs no file or Git mutation", `:141`). It binds a
    direct Writer path at `:121–124`, but its remaining structure presumes
    the profile.
- Removed: direct entry was stated twice in the predecessor, at
  P:SPEC:1576–1580 ("When one capable context has sufficient existing
  work authority, exact intake and operation grant, it may enter directly
  as constructor or Writer") and P:BASE:121–127 ("One capable context
  with sufficient work authority, intake and operation grant may enter
  directly as Worker (Writer)"). The candidate states it once at
  `ACTIVATION.md:420–426` ("… coordinating activation is required solely
  to appoint that constructor").
- Retained: EB frames, with their need stated at `EXECUTIVE_BASELINE.md:692`.
- I3 action:
  - One list of relation structures at ACTIVATION §1; the others cite it
    and name any profile addition (I3-2a, I3-2b, I3-3a). Corrected by
    design discrepancy c: the one list is RF-009's, as D3 and
    `ACTIVATION.md:322–324` already state; ACTIVATION §1 and the others
    cite RF-009.
  - Admission of a configuration moves to ACTIVATION §1, and EB refers
    (I3-2a, I3-3a).
  - Templates and skills say "coordination the applicable configuration
    selects" (I3-3d).
  - Added by I3-2e: the basis template marks its Executive sections as
    the executive profile's binding, selected only when that profile is
    adopted, and keeps a configuration-neutral slot (I3-3d).

### R17 Change classes, triage and re-entry

- Owner: SPEC_METHOD §4 (`:739`, `:777–789`, `:812`).
- Refers or refines: `TICKETS.md:443`,
  `plugins/spec/skills/stdo-ticket/SKILL.md:39`. `TICKETS.md:296` reuses
  class names as close values, which `SPEC_METHOD.md:803` acknowledges.
- Still deciding:
  - `TICKETS.md:481`: "The walk goes upward to the first missing layer",
    its own re-entry procedure.
  - `plugins/spec/references/GETTING_STARTED.md:383` rewords the class
    table ("code or configuration only") without a citation.
- Removed: the predecessor stated the classes at P:SPEC:1237–1244 ("The
  minimum lawful change classes are: …"). Its compression restated them
  and dropped the duty to prove no upstream drift. The candidate states
  them once at `SPEC_METHOD.md:777–783`, and no compression restates
  them.
- Retained: ACTIVATION's `re_enter` triggers (`:741`).
- I3 action:
  - TICKETS applies the owner's re-entry rule, or states the walk as its
    refinement (I3-2c).
  - The getting-started text quotes the owner (I3-3d).

### R18 Ambiguity

- Owner: ACTIVATION §3 (`:764`) for outcomes; SPEC_METHOD §5 (`:1073`)
  for the default policy.
- Refers or refines: `PRODUCT_DEFINITION.md:507`, `ODD.md:276`.
- Still deciding:
  - The default-policy sentence appears at both `ACTIVATION.md:849` and
    `SPEC_METHOD.md:1121`.
  - `UX.md:80` and `:755`: "satisfies the stricter interpretation,
    reprices … or records a scoped exemption". These exits are not mapped
    to the owner's outcomes.
- Removed: partly. The predecessor gave ambiguity a different outcome at
  P:SPEC:1052–1122, P:RF:595 (unresolved), RF-005 (`invalid_basis`) and
  P:BASE:489 (`activation_refusal`). The candidate has one outcome owner.
- Retained: none.
- I3 action:
  - ACTIVATION refers to SPEC_METHOD §5 for the policy (I3-2a).
  - UX maps its exits (I3-3d).

### R19 Identity, content and basis

- Owner: FOUNDATIONS §2 (`:51`, `:52`, `:60`: the basis is "immutable, or
  moving with a declared way of detecting advancement"); IDENTITY §2
  (`:79`); RF-005 (`REFERENCE_FRAME.md:274`) for evaluation basis.
- Refers or refines: AC-006 (`AXIOMATIC_CALCULUS.md:490`),
  `ACTIVATION.md:528`, `EVALUATION.md:132`.
- Still deciding:
  - `AXIOMATIC_CALCULUS.md:458–459`: "An identity resolves one member
    under one type, context, owner, scope and basis". `IDENTITY.md:13`
    says AC-002 is the same identity and "neither is restated here".
  - The "equal spelling does not establish identity" list differs at
    `AXIOMATIC_CALCULUS.md:459` and `PRODUCT_DEFINITION.md:484`. The
    predecessor already differed (P:AC:381, P:SPEC:612).
  - The exact-basis rule appears at both `REFERENCE_FRAME.md:276` and
    `AXIOMATIC_CALCULUS.md:492` in the same words.
- Removed: no.
- Retained: AC-013 content identities, with their need stated at
  `AXIOMATIC_CALCULUS.md:700`.
- I3 action:
  - FOUNDATIONS:51 owns the spelling list, and the others cite it.
  - AC-002 refers to IDENTITY §2.
  - AC-006 refers to RF-005 for exact basis, adding only a_c bindings
    (I3-2a, I3-2b, I3-3h).
- Resolution taken (I3-2r, WC1-15): FOUNDATIONS §2 Representation owns
  the rule in general form, "equal representations do not establish equal
  meaning", and holds no spelling list. AC-002 and PRODUCT_DEFINITION §5
  keep their lists as instances naming the representations of their own
  domain, and each cites the owner. This differs from the action above,
  which put one list at FOUNDATIONS: one general rule with cited domain
  instances leaves one decider without forcing one list onto two domains.

### R20 Categorical and refinement claims

- Owner: FOUNDATIONS §4 Formal fragment (`:621`); EVALUATION §6 ladder
  (`:249`); ACTIVATION §4 Refinement (`:879–916`).
- Refers or refines: `AXIOMATIC_CALCULUS.md:960`, `SPEC_METHOD.md:1738`;
  `ODD.md:309` binds its environment as the specialised contract of
  ACTIVATION §4.
- Still deciding:
  - `EVALUATION.md:278`: "Categorical equivalence additionally requires
    the appropriate quasi-inverse and natural isomorphisms". It is not
    mapped to the formal fragment's items.
  - `WORLD_MODEL.md:529`: "Every treatment declares preserved structure,
    changed meaning, loss, surplus and ambiguity". It cites neither
    ACTIVATION §4 nor RF §6, and states no need.
- Removed: not a predecessor reduction case. The predecessor had no owner
  for refinement licensing; it is new law.
- Retained: none.
- I3 action:
  - EVALUATION:278 maps to the formal fragment's items (I3-2b).
  - WM:529 refines ACTIVATION §4 (I3-3d, with R29).

### R21 Imports and profile adoption

- Owner: FOUNDATIONS §2 Imports between members (`:268`); PRODUCT_DEFINITION
  `:656` for adoption.
- Refers or refines: `PRODUCT_DEFINITION.md:543`, `PROFILES.md:28`,
  `REFERENCE_FRAME.md:82`.
- Still deciding:
  - Three field lists for a binding cite no common owner:
    `AXIOMATIC_CALCULUS.md:1243` ("authority, context, basis, scope,
    preservation, loss, refusal and invalidation law"), `PROFILES.md:19`
    and `PRODUCT_DEFINITION.md:571`.
  - `FOUNDATIONS.md:851` makes "the design decision of DESIGN_MODULE §5"
    the owner of a tier-1 choice, though that member is an optional
    profile.
  - Adoption is restated at `UX.md:74`, `UX.md:523`,
    `DESIGN_MODULE.md:2272`, `TRAVERSAL_OCCURRENCE.md:1426` and
    `EXECUTIVE_BASELINE.md:1288`. The UX and DESIGN_MODULE adopter sets
    conflict with the owner, and no reason is stated.
- Removed: no. The predecessor had three adopter statements: P:SPEC:748
  ("Only Product authority may adopt it"), P:UXM:22 ("a product, ticket,
  design module, or review adopts") and P:DMM:2548 ("citing it in ADRs").
  The candidate keeps them as rivals.
- Retained: none.
- I3 action:
  - FOUNDATIONS:268 owns the binding field list, and the others refine it.
  - FOUNDATIONS:851 names a tier-1 owner (I3-2a).
  - Each profile's adoption text refers to PRODUCT_DEFINITION:656. A
    narrower adopter set for one profile is a proposed replacement
    relation, if it changes predecessor meaning (I3-3a, I3-3b, I3-3d,
    I3-3g).

### R22 Claims, observations, acceptance and evidence classes

- Owner: EVALUATION §2 (`:94–106`) for separation; FOUNDATIONS:640 for
  evidence class.
- Refers or refines: `SPEC_METHOD.md:1569`, `AXIOMATIC_CALCULUS.md:847`.
- Still deciding:
  - `REFERENCE_FRAME.md:292–298` states RF-007 in full and says
    "EVALUATION §2 applies this law to review". Yet `EVALUATION.md:525`
    records "RF-007 | conserved; §2".
  - `AXIOMATIC_CALCULUS.md:1044` claims EVALUATION §2 applies AC-018's
    separation, while EVALUATION's own disposition table makes EVALUATION
    the generic form.
- Removed: no. The predecessor stated it at P:RF:368 (RF-007) and
  P:SPEC:2071 (UP-008), and the candidate still states it twice with
  ownership claims that conflict.
- Retained: the WORLD_MODEL evidence hierarchy (`:339`), with its need
  stated.
- I3 action: EVALUATION §2 is the owner. RF-007 and AC-018 refer and keep
  only their domain binding (I3-2b).

### R23 Staleness of derived surfaces

- Owner: PRODUCT_DEFINITION §11 (`:858–882`) for what a derived surface
  is and when it is stale; ACTIVATION §2 (`:517`, `:564`) for use,
  fallback and standalone scope; ACTIVATION §5 (`:1107`) for an actor's
  account.
- Refers or refines: `README.md:90–104`, `GLOSSARY.md:65`.
- Still deciding:
  - `ACTIVATION.md:527` (tier 1) uses "stale" without importing
    PRODUCT_DEFINITION §11, a tier-2 owner.
  - `PRODUCT_DEFINITION.md:879` lets owners "decide when a derived surface
    or frame is stale", which overlaps ACTIVATION's standalone scope.
  - `UX.md:392`: "must carry the governing UX law as a derived surface or
    projected frame". That contradicts ACTIVATION's fallback to owner
    sections.
- Removed:
  - Predecessor, two stances:
    - `authority_compressions/README.md:3–4` (P), the compressions "are
      prompt-construction inputs, not replacement constitutional
      authority";
    - the compressed method text (P `stdo_compressed`, `:1122`) treats raw
      documents as "fallback inputs".
  - Candidate: `PRODUCT_DEFINITION.md:858–862`, "Compressions, templates,
    comments, candidate work, installed copies and mutable source are
    derived, evidential or authoring surfaces".
  - The compression carrier's disposition awaits the product owner's
    ruling.
- Retained: the UP-009 drift refusal (`TICKETS.md:1197`); TRAVERSAL
  `stale_frontier`.
- Added by I3-2e, duplicates in agreement: the basis template `:201–202`
  ("Prompts, summaries, symbolic maps, compressions, and other
  projections may route attention. They do not replace the sources");
  the product-definition schema's selector description ("never operative
  constitutional authority without digest-bound explicit resolution and
  adoption").
- I3 action:
  - The generic staleness rule moves to ACTIVATION §2 (tier 1), with
    PRODUCT_DEFINITION §11 refining it for packaging carriers. This
    removes the tier-1-on-tier-2 dependency (I3-2a, I3-2c).
  - UX:392 refers to ACTIVATION §2 (I3-3d).
  - `ODD.md:1644` summarises rules inside its own member; it is checked as
    a duplicate (I3-3c).

### R24 Hard stops

- Owner: ACTIVATION §4 (`:845–864`).
- Still deciding: as R5 for "non-waivable hard stops". The predecessor
  had three loci (P:SPEC:1117, P:BASE:451–459, P:DMM:2192); the candidate
  has one owner with an unstated binder relation.
- Added by I3-2e: the basis template `:100–101`, "A cutoff cannot waive a
  hard stop", agrees with the owner; it refers with R5's template action
  (I3-3d).
- I3 action: with R5.

### R25 When a finding blocks promotion

- Owner: none today. This design fixes EVALUATION §5 Acceptance.
- Still deciding:
  - `TICKETS.md:1019`: "A finding blocks current promotion only when it
    falsifies that claim; exposes competing …";
  - `EXECUTIVE_BASELINE.md:1183`: by the Product cutoff, "no block follows
    mechanically";
  - `DESIGN_MODULE.md:1876` repeats TICKETS's conditions.
  - Added by I3-2e:
    - the basis template `:86–87` and `:91–101`: "A cutoff cannot waive
      a hard stop or turn an out-of-claim observation into a blocker";
      it agrees with TICKETS:1021 but states it as template law;
    - `plugins/spec/skills/stdo-status/SKILL.md:68–69`, "Keep adjacent
      observations from becoming automatic release blockers";
    - `RELEASE.md:616`, "all release-blocking gaps are closed", which uses
      the predicate without naming its owner;
    - `EXECUTIVE_BASELINE.md:399–400`, none of four values "alone makes
      a finding release-blocking";
    - `DESIGN_MODULE.md:522`, contradictory projections "block
      promotion", a domain instance of falsification.
  - Resolution of the locus 4.6 left conditional on I3-2e:
    `DESIGN_MODULE.md:1876–1884` states what the design check
    determines (lawful boundary, complete claim, competing authority,
    foreclosing decision, falsification or hard stop). It does not state
    when a finding blocks, so it decides no block outcome of its own and
    no path is added (4.7). The existing action, that DESIGN_MODULE
    refers for the block rule, stands.
- I3 action: EVALUATION §5 owns the rule, and TICKETS, EB and
  DESIGN_MODULE refer, keeping their domain triggers (I3-2b, I3-2c,
  I3-3a, I3-3b). Added by I3-2e: the template and the skill refer
  (I3-3d); RELEASE:616 names the owner (I3-3h); EB:399 refers (I3-3a).

### R26 Progress judgement

- Owner: ACTIVATION §5 (`:1072`, churn and forecast).
- Still deciding: `SPEC_METHOD.md:627`, "material advance, prerequisite
  readiness, preservation and regression", which cites no owner.
- I3 action: SPEC_METHOD states its categories as a refinement of the
  owner, or the owner adopts them (I3-2a, I3-2c).

### R27 One label for several questions

- Not one determination, but a source of reconciliations on many paths:
  - `indeterminate` is both a core value and a triage class
    (`EVALUATION.md:196`);
  - `not_applicable` has seven senses (`EVALUATION.md:197`,
    `DESIGN_MODULE.md:1418`, `:56`, `RELEASE.md:652`,
    `SPEC_METHOD.md:609`, `TRAVERSAL_OCCURRENCE.md:594`,
    `ACTIVATION.md:1020`);
  - `refusal` and `refused` occur in ACTIVATION, RF §5, AC-007 and
    TRAVERSAL;
  - `gap` is an AC stop with a value, while a conjunction gap has none
    (`AXIOMATIC_CALCULUS.md:583`);
  - "disposition" names four different sets (ACTIVATION §3, RELEASE §9,
    `TICKETS.md:1095`, `:286`).
  - Added by I3-2e:
    - a fifth "disposition", `activate | non_material | residual`, for an
      evaluation in the basis template's inventory
      (`PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md:53`; cluster R34);
    - "missing" as an evidence status beside "satisfied" and "invalid"
      (`:56`), where FOUNDATIONS:721 makes missing the absence of a
      result;
    - "adoption" in three senses: a profile (`PRODUCT_DEFINITION.md:656`,
      R21), a shared-method lesson (SPEC_METHOD §6, UP-012) and a release
      basis (`RELEASE.md:387`, `templates/README.md:117–122`);
    - `Closed` as a post's discussion state (`POSTING_GUIDE.md:125`)
      beside ticket closure.
- I3 action: each sense either takes a qualified name or states its
  predicate where used. GLOSSARY lists the senses with their owners
  (I3-3e).

### R29 Statements of what a transformation preserves

- Owner: ACTIVATION §4 Refinement and AC-013.
- Still deciding:
  - `REFERENCE_FRAME.md#evidence-or-coordinate-translation`;
  - `SPEC_METHOD.md:1757–1764`;
  - the WORLD_MODEL projection law (`:529`).
  - Each restates preservation independently.
- I3 action: each refers to the owner and adds only its domain fields
  (I3-2b, I3-2c, I3-3d).

### R30 Resource limits (added by I3-2e)

- Owner: ACTIVATION §6 Cost and proportionality, which states the generic
  resource-limit law: an activation declares its context, time, spend and
  other resource limits with their units and measurement boundaries, and
  reports them. SPEC_METHOD §11 binds that law: a tenant's execution
  binding supplies the units, boundaries and values. This is design
  discrepancy b, recorded in DOCUMENT_STRUCTURE D2, D4 and D7.
- Refers or refines: `ACTIVATION.md:193` (intake declares the allowance
  under §6), `:302` (a configuration explains its resource limits),
  `EXECUTIVE_BASELINE.md:722`, `:1347`, `CONFORMANCE.md:44`.
- Still deciding:
  - `ACTIVATION.md:1230–1232`: "Time, spend and other resource limits,
    with the units and boundaries of their measurement, are those of" the
    selected execution binding;
  - `EVALUATION.md:411–412`: "Time, spend and other resource limits are
    those of the selected execution binding";
  - `SPEC_METHOD.md:1523–1524` (§8) and `:1714–1715` (§11), each saying
    the limits "are those of the execution binding".
  - The four agree with one another, but no tier-1 section owns the law
    that tier-1 members apply. A tier-1 path must cross into tier 2,
    which D7 forbids.
- Removed: not a predecessor reduction case; the provenance at
  `ACTIVATION.md:1231` is UP-014's selection rule, which had no binding.
- Retained: none.
- I3 action:
  - ACTIVATION §6 states the generic law (I3-2a, in its row).
  - SPEC_METHOD §11 binds it and §8 (`:1523`) refers (I3-2c; its row
    names §11, and §8 is added here).
  - EVALUATION:411 refers to ACTIVATION §6 (I3-3j, which holds
    EVALUATION).

### R31 Implicit activation and continuation (added by I3-2e)

- Owner: ACTIVATION §1 Admission (`ACTIVATION.md:225–229`). Execution
  begins only after deterministic admission or an explicit human
  override. The drafting actor never infers admission from its own draft,
  a carrier, lane placement or an `active` label. ACTIVATION §3 Admission
  and activation owns the refusal value.
- Refers or refines:
  - a Reviewer does not "authorise continuation":
    `EVALUATION.md:216`, `EXECUTIVE_BASELINE.md:1161`;
  - `EXECUTIVE_BASELINE.md:1567`, the violation table, cites ACTIVATION
    §1 and §5.
- Still deciding:
  - `EXECUTIVE_BASELINE.md:565–570`: "No lateral handoff, child
    completion, model response, tool output or shared actor implicitly
    activates another frame or authorises continuation. A consumer
    receives the closed result and its source routes, not the child's
    hidden reasoning context". This is a generic rule stated only in an
    optional profile, in its own words (conformance row 10). It cites
    ACTIVATION §7, not §1 Admission. The owner's list of what does not
    admit (draft, carrier, lane, label) and the profile's list (handoff,
    child completion, model response, tool output, shared actor) do not
    coincide.
  - The basis template, `PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md:138–143`,
    states the profile's list as template law for every project. It adds
    "Changing roles does not create authority or independent assessment".
- Removed: no. The predecessor stated the profile's sentence in
  STDO_REFERENCE_FRAME_BASELINE ("implicitly activates", one hit at the
  rc.2 tag), and the candidate keeps it in the profile and the template.
- Retained: none.
- I3 action:
  - ACTIVATION §1 Admission states the generic rule once, with both lists
    as instances. Only I3-2a holds that text, and this is outside its
    intake.
  - EB:565–570 refers and keeps the Executive return route (I3-3a).
  - The template refers (I3-3d).

### R32 Current-surface writing and version labels (added by I3-2e)

- Owner: SPEC_METHOD §2 Specification surface rule
  (`SPEC_METHOD.md:398–408`):
  - constitutional specification "is written in the present tense";
  - what is no longer live "is deleted, superseded or moved to
    commentary";
  - explicit version labels "are reserved for immutable release facts,
    selector bindings, or clearly historical or superseded material".
- Refers or refines: `GOALS_TEMPLATE.md:17–18`, `PRODUCT_TEMPLATE.md:3`,
  `INTENT_TEMPLATE.md:3`.
- Still deciding:
  - `WRITING_GUIDE.md:114–125` (§9):
    - "should describe … in present tense", advisory force where the
      owner is mandatory;
    - labels "only for an immutable release fact, an explicit mutable
      selector binding or clearly historical material", which omits
      superseded material;
    - it names SPEC_METHOD §6 as stating "the same boundary", while the
      owner is §2.
    - §7 (`:92–96`) restates the stale-law rule.
  - `SPEC_METHOD.md:1160–1163` (§6): surfaces "should therefore describe
    current truth by role, boundary and status rather than by
    release-line version labels". It is advisory and points back to §2.
  - `SPEC_METHOD.md:168` (F10 consequence): "a version label names an
    immutable release fact, not recency", one use where the owner allows
    three.
  - `RELEASE.md:465–466`: branding "does not belong in live present-tense
    Product or requirements surfaces merely to signal recency". Its scope
    is Product and requirements surfaces only.
- Removed: no. The predecessor stated the rule in SPEC_METHOD and
  WRITING_GUIDE, the latter "present tense at 'should'"
  (`WRITING_GUIDE.md:148`), and the candidate keeps both.
- Retained: WRITING_GUIDE's practice (style, habits, tone, layer checks)
  is the guide's own subject, not a rival.
- I3 action:
  - SPEC_METHOD §6 and the F10 row refer to §2 (I3-2c, inside its
    territory but outside its listed loci; otherwise I3-3f).
  - RELEASE:465 refers (I3-3h).
  - WRITING_GUIDE §7 and §9 refer to the owner for the rule and its
    force, keep the writing practice, and correct the pointer. No step 1
    or step 2 activation holds WRITING_GUIDE; this design proposes I3-3f
    with WRITING_GUIDE added to its territory.
  - If the guide's "should" is predecessor meaning that the owner's
    mandatory force changes, the change is a proposed replacement
    relation (I3-4b).

### R33 Standing of commentary (added by I3-2e)

- Owner:
  - POSTING_GUIDE §2 Boundary and §9 Ratification
    (`POSTING_GUIDE.md:35–40`, `:158–160`) for what a post is used for
    and when its content becomes consequential;
  - FOUNDATIONS §2 Authority kinds for the rule that writing a surface
    creates no authority (R12);
  - PRODUCT_DEFINITION §11 (`:860–863`) for comments as derived or
    authoring surfaces (R23).
- Refers or refines (duplicates in agreement): `PRODUCT_DEFINITION.md:749`,
  `TICKETS.md:113–114`, `EXECUTIVE_BASELINE.md:149`, `EVALUATION.md:176`,
  `plugins/spec/skills/stdo-ticket/SKILL.md:63`.
- Still deciding:
  - `TICKETS.md:71–74`: comments "are for publishing ideas, strategy
    notes, reviews, handoffs, closure summaries, and decisions with their
    reasoning". This is a content list of its own beside POSTING_GUIDE §1
    and §5. It admits "decisions", where POSTING_GUIDE §2 excludes "live
    design decisions" from posts.
  - Both bind the same `ticketing.comments.root` carrier, and neither
    states whether a comment and a post are the same object.
- Removed: no. The predecessor stated both (TICKET_METHOD #comments,
  POSTING_GUIDE).
- Retained: POSTING_GUIDE's categories, structure and discussion states,
  which are the guide's own carrier rules.
- Family: POSTING_GUIDE has no family table (section 2, pillar 1). Its
  deciding rules are accounted under F13 Work carriers through the family
  index.
- I3 action:
  - TICKETS §1 refers to POSTING_GUIDE for what a comment carries, and
    states that a recorded decision's authority is its owning surface
    (I3-3f).
  - The F13 table accounts for POSTING_GUIDE §2, §7 and §9 (I3-3f).
  - The FOUNDATIONS §3 index entry names POSTING_GUIDE under F13. Only
    I3-2a holds that text, and this is outside its intake.

### R34 Determinations stated only in templates (added by I3-2e)

- Owner, by question:
  - REFERENCE_FRAME §8 Coverage for the states of an evaluation in an
    inventory and for coverage completeness;
  - SPEC_METHOD §10 Design records for ADR retention;
  - PRODUCT_DEFINITION §8 for the tenant registry.
  - A template is a derived authoring surface (PRODUCT_DEFINITION §11,
    R23) and owns no determination.
- Still deciding:
  - The basis template's evaluation inventory,
    `PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md:53`: "disposition:
    `activate | non_material | residual`".
    - No member states, maps or declares these values.
    - `non_material` would drop an evaluation from coverage. The coverage
      values of `REFERENCE_FRAME.md:683–703` require
      `excluded_by_authority`, with an authority, for that.
  - The basis template `:155–158`, "Coverage is complete only when every
    mandatory material evaluation and interaction is closed, or governing
    authority explicitly retains its residual", a completeness rule
    beside RF §8.
  - The basis template `:56`, an evidence status "satisfied/missing/invalid"
    (R27).
  - The ADR README templates (`build_tenants/common/design/adrs/README_TEMPLATE.md:41`,
    `:45`, and the variant copy) state two rules that SPEC_METHOD §10
    does not:
    - "ADRs are append-only history; do not delete superseded ADRs unless
      they are being explicitly retired";
    - "If the scope narrows during implementation, move the ADR … and
      record the move in the supersession chain".
  - `TENANT_REGISTRY_TEMPLATE.md:35–41`, "Suggested lifecycle states". No
    owner states a tenant lifecycle; the list is suggested, not deciding.
  - Not a rival: `templates/README.md:78` cites "PRODUCT_DEFINITION.md
    section 6" for the import, translation or equivalence relation, which
    §5 owns. This is a pointer defect.
- Removed: no. These are the predecessor's template texts, conserved as
  packaging. At the rc.2 tag, `non_material` is at
  `templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md:52`. The ADR
  supersession rule is at the common and variant ADR README templates
  (`:45`, `:43`).
- Retained: none stated.
- I3 action:
  - RF §8 either adopts the evaluation-inventory values as declared
    states, mapped to its coverage values or excluded with an authority,
    or the template uses RF §8's values (I3-3j for RF, I3-3d for the
    template).
  - The template's completeness sentence refers to RF §8 (I3-3d).
  - SPEC_METHOD §10 adopts or declines the two ADR rules (I3-3f), and the
    ADR templates refer (I3-3d).
  - I3-3d corrects the README pointer.
  - A change of predecessor template meaning is a proposed replacement
    relation (I3-4b).

### Design discrepancies found

- **a.** D1 says RF-012, RF §6, AC-007 and EVALUATION §4 "define nothing
  further". AC-007 (`AXIOMATIC_CALCULUS.md:519, 542`), EVALUATION §4
  (`:193`) and RF §5, which D1 does not name, each refine with a map.
  `FOUNDATIONS.md:854` permits this. D1's wording is corrected to "refine
  with a map" (I3-2e).
- **b.** D2 sends time and spend limits to the execution binding, which D4
  places in SPEC_METHOD §11 (tier 2). ACTIVATION:1232 and EVALUATION:412
  (tier 1) depend on it, which D7 forbids. ACTIVATION §6 owns the generic
  resource-limit law, and SPEC_METHOD §11 binds it (I3-2a, I3-2c, I3-2e).
  I3-2e made this cluster R30 and recorded the correction in D2, D4 and
  D7.
- **c** (found by I3-2e). Two places name different owners of the list of
  distinct relation structures.
  - D3 and `ACTIVATION.md:322–324` name RF-009 ("under RF-009, which
    owns that rule").
  - R16's action named ACTIVATION §1.
  - This design keeps D3, because the member text already applies it. RF-009
    owns the list; ACTIVATION §1, EB:656 and RF:980 cite it. R16's action
    is corrected in place.
  - I3-2a and I3-2b started from the uncorrected wording. If either has
    moved the list into ACTIVATION §1, the Executive reconciles it before
    I3-3a cites it.

D1 (discrepancy a) is corrected in DOCUMENT_STRUCTURE. The correction
also adds a fifth refinement: D1 counted four for ACTIVATION §3, but
the table that opens ACTIVATION §3 (`ACTIVATION.md:612–637`) has five,
including admission and activation.

### Summary

| Cluster | Owner | Rivals or duplicates remaining | Predecessor multiplicity removed |
|---|---|---|---|
| R1 core values | FOUNDATIONS §4 | 2 | yes |
| R2 conjunction | FOUNDATIONS §4 | 3 | partly |
| R3 work-step variants | ACTIVATION §3 | 3 | yes, with proposed replacements |
| R4 effects | ACTIVATION §3, §5 | 2 (one suspected) | yes |
| R5 stops and refusals | ACTIVATION §3, §4; RF §5; AC-007 | 3 | yes |
| R6 fit and remedies | ACTIVATION §2; EVALUATION §7 | 5 | partly |
| R7 reuse | ACTIVATION §7 | 5 lists, 4 duplicates | partly |
| R8 frame revision | REFERENCE_FRAME §10; ACTIVATION §7 | 2 | yes |
| R9 resumption | ACTIVATION §5 | 2 duplicates | not applicable |
| R10 applicability | ACTIVATION §1 | 3 | partly |
| R11 independence | EVALUATION §3 | 3 | partly |
| R12 authority | FOUNDATIONS §2 | 5 lists, 3 proxy, 3 recording | no |
| R13 dispositions | RELEASE §9 | 4 | no |
| R14 closure labels | FOUNDATIONS §4; ACTIVATION §3 | 4, plus 5 duplicates | partly |
| R15 binding | SPEC_METHOD §11 | 0 | not applicable |
| R16 configuration | ACTIVATION §1 | 4, plus templates | yes for direct entry |
| R17 change classes | SPEC_METHOD §4 | 2 | yes |
| R18 ambiguity | ACTIVATION §3; SPEC_METHOD §5 | 2 | partly |
| R19 identity and basis | FOUNDATIONS §2; IDENTITY §2; RF-005 | 3 | no |
| R20 refinement claims | FOUNDATIONS; EVALUATION §6; ACTIVATION §4 | 2 | not applicable |
| R21 imports and adoption | FOUNDATIONS §2; PRODUCT_DEFINITION | 3 lists, 5 adoption texts | no |
| R22 evidence separation | EVALUATION §2 | 2 | no |
| R23 derived surfaces | ACTIVATION §2 (planned); PRODUCT_DEFINITION §11 | 3 | yes |
| R24 hard stops | ACTIVATION §4 | with R5 | yes |
| R25 promotion block | EVALUATION §5 (new) | 3 | no |
| R26 progress | ACTIVATION §5 | 1 | not applicable |
| R27 label homonyms | per sense | many | no |
| R29 preservation | ACTIVATION §4; AC-013 | 3 | not applicable |
| R30 resource limits (I3-2e) | ACTIVATION §6, bound by SPEC_METHOD §11 | 4 | not applicable |
| R31 implicit activation (I3-2e) | ACTIVATION §1 Admission | 2 | no |
| R32 current surface and labels (I3-2e) | SPEC_METHOD §2 | 5 | no |
| R33 commentary (I3-2e) | POSTING_GUIDE §2, §9 | 1, plus 5 duplicates | no |
| R34 template-only rules (I3-2e) | RF §8; SPEC_METHOD §10; PRODUCT_DEFINITION §8 | 5, plus 1 pointer | no |

Loci still deciding independently or duplicating an owner: about 100
across 26 clusters (R28 is not used; relation-structure lists are in R16). The heaviest are R7, R12, R14, R16 and R21, in SPEC_METHOD,
TICKETS, EXECUTIVE_BASELINE, the profiles and the plugin.

I3-2e added about 60 loci:
- 17 to existing clusters as rivals: R7 9, R11 1, R14 2, R16 1, R25 4;
- about 20 to existing clusters as domain instances or duplicates in
  agreement: R10, R12, R23, R24, R25, and R27's four further senses;
- 17 rivals and 6 duplicates in the new clusters R30 to R34.

The counts in the rows for R1 to R29 above are I3-1's and are not
changed. The loci added by I3-2e are listed in their clusters. The total
is now about 160 loci across 31 clusters. The heaviest are still R7,
R12, R14, R16 and R21; the basis template and the plugin skills are now
the largest single sources outside the members.

## 4. Deciding paths

This section is fixed before any comparison is run. Item 5 of the
reduction requirement forbids replacing the selection after results are
seen. A later activation may only add paths: for a newly found cluster, or
for a rival locus of an existing cluster that the coverage table in 4.6
leaves uncovered. Each addition is declared before any S2 trace exists.
No path here is removed or redefined.

### 4.1 Subjects and entries

| Subject | Exact coordinates |
|---|---|
| S0, predecessor | installed `stdo://releases/v2.5.1-rc.2/`, manifest `3d860ff4…2782` |
| S1, preceding candidate | `5ab44d5c51bf5956d12b120d83159f6c28eee3a9`, `build_tenants/claude/standards/` |
| S2, iteration 3 candidate | the frozen iteration 3 commit (PLAN I3-6) |

Each path is traced from two kinds of entry. They are kept apart because
their acquisition conditions differ.

- **Route entry**, on all three subjects: the subject's own
  `standards/README.md` (for S0 the installed one), then only declared
  routes from it. This is the comparison of record. Every reduction
  verdict against S0 or S1 uses route-entry traces only, so all three
  subjects start from the same kind of uncurated entry.
- **Frame entry**, where the subject publishes a frame for the task: on
  S1 and S2 the frame in `standards/frames/FRAME_INPUTS.json`; on S0 the
  STDO_REFERENCE_FRAME_BASELINE frame for a Worker, Reviewer or Executive
  task where one exists. A frame is curated: it already assembles the
  deciding sections, which favours M4 and M5 by construction. The
  frame-entry traces are reported as a separate frame-entry measure,
  compared between S1 and S2, and against S0 only where S0 has a frame for
  that task. They never stand in for a route-entry verdict.

The three subjects share each path's task, inputs, authority and
acquisition conditions within one entry kind. Each path states the task in one sentence, with
the same facts and the same grant for all three. The tracer starts at the
entry and acquires only through declared routes: a link, a named section
or a frame's source line. It does not search the corpus. A deciding locus
that no declared route reaches is recorded as "unreachable by route". That
is an adverse result, never a skipped step. The a_c interpretation is an
optional route on S2 only (DP-27).

### 4.2 Dimensions, declared now

| Id | Dimension | Unit | How it is counted |
|---|---|---|---|
| M1 | deciding loci | count | distinct sections whose own determination the actor applies to reach the result: the owner plus each refinement used. Pointers are not counted |
| M2 | independent deciders | count | sections met on the path that state a rival determination for the same question (section 3's sense) |
| M3 | reconciliations | count | pairs of loci, or one label with two meanings, that the actor must reconcile to decide: disagreeing lists, unmapped values, contradictory statements, homonyms |
| M4a | supplied bytes | bytes | the entry as supplied: frame or README, by `wc -c` at the subject's commit |
| M4b | cumulative acquired bytes | bytes | the sum of every section acquired along the route, repeated reads counted again, using the frame generator's section boundaries |
| M4c | active retained bound | bytes | the largest sum held at once under the declared reading order, with sections released once their determination is recorded |
| M5 | hops | count | distinct sections acquired beyond the entry |
| G | distinction guard | pass or fail per item | each listed distinction of the path (permission, obligation, failure, uncertainty, modal force, trigger, exception) is preserved against the predecessor claim's meaning or its accepted replacement |

**Outcome rule.** The rule is applied to route-entry traces (4.1). A path
is "simpler to determine and apply" against a baseline only when:

- G passes;
- M2 and M3 do not increase against either baseline;
- at least one of M2 or M3 decreases against the named baseline;
- every increase in M4 or M5 is explained by a declared tradeoff below or
  by a preserved distinction.

Otherwise the path's verdict is "not established". An elimination
witness, meaning one removed rival or reconciliation with G passing,
keeps that narrower standing either way. Adverse changes are reported
against both baselines.

### 4.3 Declared tradeoffs and expected adverse changes

| Id | Tradeoff | Accepted when |
|---|---|---|
| TO1 | Frames carry family tables (premises, pillar contributions) and result maps, which raises M4a and M4b | M3 falls on the same path, or G gains a premise or map an actor needs, and the increase is disclosed against both baselines |
| TO2 | Generic law moves to a tier-1 owner, so a path needs owner plus binding (M5 up) where the predecessor's profile restated the rule locally | M2 or M3 falls on the same path |
| TO3 | Refinement maps carry the domain outcome beside the core value, which adds text per value | required by the single result algebra requirement item 4; disclosed |

Expected adverse, declared before measurement: on the frame-entry
measure, M4a on DP-01, DP-03, DP-04 and DP-08 against S1 (TO1); M5 on DP-01 and DP-03 against S0
(TO2); M4a on DP-23 (bootstrap), direction unknown; and DP-27, which has
no comparable entry on S0 or S1.

### 4.4 Selected paths

Task kinds are the six of the
[C3 contract's tasks](../../../specification/PRODUCT.md#c3-construction-contract):
work (bounded work), resume, review, decide (acceptance or release),
profile (apply a profile), member (build or assess a member).

| Path | Task kind | Situation the task states | Clusters | S1 and S2 entry | Guard items |
|---|---|---|---|---|---|
| DP-01 | review | combine three mandatory results: one `falsified`, one planned but not performed, one bound to a superseded basis | R1, R2 | rf-task-b | failure kept; not performed is no result and stays apart from `indeterminate`; superseded basis handled by one rule |
| DP-02 | review | a conformance case cannot be run with the declared subject | R1 | README route to CONFORMANCE | an unexercised evaluation has no result |
| DP-03 | decide | a Writer returns `incomplete` after an external write whose completion is unknown | R3, R4, R14 | eb-task-d | availability, assessment and acceptance kept apart; unknown completion never "no effect" or "completed"; no retry before reconciliation |
| DP-04 | profile | a deadline-bound outcome is defeated after three of five updates; whether the worker has ended is unknown | R4, R5 | traversal-task-f | established non-attainment is `falsified`; the end stays a residual; no blind retry |
| DP-05 | profile | a consumer update fails, the failure is caught, and restoration is not verified | R4 | README route to PRODUCT_DEFINITION | as DP-04 |
| DP-06 | work | the material a task needs exceeds the actor's declared context | R6 | configuration | no obligation omitted; fit and attention judged apart; the remedies offered are the owner's |
| DP-07 | resume | a retained summary disagrees with the workspace; some closed results depend on a changed input | R7, R9, R23, R26 | stale-summary | the workspace wins; reuse checks every invalidator; a summary grants no restart authority |
| DP-08 | review | a clarification finds a recorded activation outside its frame's family; separately, new admissible evidence arrives on another result | R8, R7 | rf-task-b | F1's two questions kept apart; independent results kept |
| DP-09 | member | a requirement changes: which closed results and work items are invalidated | R7, R17 | README route to SPEC_METHOD | every predecessor trigger kept; mandatory force kept |
| DP-10 | review | the author of a release candidate reviews it in a fresh context; is independent review triggered and satisfied | R11 | README route to EVALUATION and TICKETS | a fresh context is not independence; trigger boundaries kept |
| DP-11 | decide | a proxy with the needed capability and a passing check records acceptance for the owner | R12, R14 | eb-task-d | capability and a passing check grant no authority; proxy limits kept |
| DP-12 | member | dispose predecessor claims and classify inherited working material for the PROFILES member, whose source-disposition table uses values outside the four | R13 | README route to RELEASE §9 | exactly one of the four values per claim; a removal needs the owner |
| DP-13 | profile | close a sprint with one item partly done and one rejected | R14 | README route to TICKETS | close classification, disposition and acceptance kept apart |
| DP-14 | profile | an ODD closure meets a repair needing proof and a re-entry to an undeclared stage | R3, R14 | README route to ODD | each decision maps to exactly one core value without homonym clash |
| DP-15 | profile | judge a view's UX compliance where the two compliance tests disagree | R14 | README route to UX | an unresolved conflict stays unresolved |
| DP-16 | work | one capable context with sufficient authority starts work with no coordinator | R16 | configuration | no role, hierarchy or coordinator is required |
| DP-17 | work | an ambiguous requirement is found mid-task | R18, R5 | README route to SPEC_METHOD §5 | unresolved is never permission; outcome mapped |
| DP-18 | work | a cached reference has the same identifier and new content | R19 | ac-task-a | identity is not content; exact basis |
| DP-19 | profile | a product adopts the UX, design, traversal and executive profiles: who may adopt, and with which binding fields | R21 | dm-task-d | the adopter set of the owner; one binding field list; a generic rule available without the profile |
| DP-20 | review | a compressed summary and an owner section disagree about evidence and acceptance | R22, R23 | stale-summary | a derived view has no authority; claim, observation and acceptance kept apart |
| DP-21 | decide | a release candidate satisfies every criterion except one blocking finding and one hard stop | R24, R25, R2 | README route to RELEASE and EVALUATION §5 | a hard stop is not waived; failure is preserved; the block rule is applied once |
| DP-22 | work | record a transformation step and what it preserves | R29, R20 | ac-task-a | preservation, introduction and removal stated; the licensing law applied |
| DP-23 | work | enter the method for a task not yet specified | ordinary acquisition | bootstrap | basis bound; standalone, no predecessor rule supplies content |
| DP-24 | member | triage a defect recorded on a ticket: change class and re-entry | R17 | README route to SPEC_METHOD §4 and TICKETS | smallest lawful re-entry; upstream-drift duty kept |
| DP-25 | member | assess a member with a conditional obligation of unknown applicability and a design `not_applicable` | R10 | README route to ACTIVATION §1 | unknown applicability unresolved; exclusion is no result; disjunctive predicate scoped |
| DP-26 | work | state a software tenant's and a human-process tenant's binding (control path, no reduction claimed) | R15 | binding | author, actor and operation kind kept apart |
| DP-27 | work | build a task's constraint surface from the interpretation (S2 only) | pillar 10 | the S2 interpretation route | residuals block dependent work; no permission from a missing premise |
| DP-28 | profile | claim a boundary's observed state is sufficient without adopting WORLD_MODEL | pillar 2, R21 | README route | ordinary bounded modelling establishes no stronger Markov property |
| DP-29 | profile | a traversal constraint predicate is evaluated on a subject outside its declared scope | R1, R5 | traversal-task-f | the out-of-scope case has one value across AC-007 and the profile |
| DP-30 | decide | an Executive composite claim has one missing seam result and one component bound to a superseded basis | R2, R5 | eb-task-d | a missing result is a gap; the superseded basis handled by one rule |
| DP-31 | resume | resume through the plugin's status skill after an effect of uncertain completion, in a project bootstrapped from the templates | R4, R10, R14, R16, R17 | the plugin skill and template text | reconciliation before repetition; no coordinator mandated; unknown applicability withholds the dependent claim |
| DP-32 | review | the evidence behind a recorded verdict and a ticket's closed result changes | R7 | README route to EVALUATION and TICKETS | mandatory invalidation; every trigger kept |
| DP-33 | profile | a design trace changes after the design was accepted | R7 | dm-task-d | as DP-32 |
| DP-34 | decide | the Executive revalidates its drift locks after a frame clarification and judges whether a finding blocks the current promotion boundary | R8, R11, R14, R16, R25 | eb-task-d | the full diagnostic order; one promotion-block rule; configuration admitted by existing authority |
| DP-35 | member | set the lifecycle state of a requirement under assurance | R10 | README route to SPEC_METHOD and ASSURANCE | one lifecycle rule; exclusion is no result |
| DP-36 | work | an available tool and a frame selection are offered as authority for a write | R12 | README route to REFERENCE_FRAME RF-006 | no capability, evidence shape or selection creates authority |
| DP-37 | profile | a UX requirement is ambiguous, and the UX law is needed where no frame carries it | R18, R23 | README route to UX | ambiguity exits mapped; fallback to owner sections allowed |
| DP-38 | work | one term is spelled the same in two bounded contexts of a project | R19 | README route to PRODUCT_DEFINITION §5 | equal spelling does not establish identity |
| DP-39 | review | a categorical equivalence between two designs is claimed | R20 | README route to EVALUATION §6 | the formal fragment's items shown before the claim |
| DP-40 | profile | record a world-model projection and an evidence translation, stating what each preserves | R29, R20 | README route to WORLD_MODEL and REFERENCE_FRAME | preservation, loss and surplus stated under one owner |

The column "S1 and S2 entry" names the frame or route the task starts
from for the frame-entry measure. Route-entry traces start at README on
every subject, as stated in 4.1.

Grouping: DP-04 and DP-05 share one guard and can share one comparison
record if their traces reach the same owner. DP-24 and DP-09 share the
change-class part only. No other grouping is declared.

Uncovered material paths:
- R26 and R27 are covered only as reconciliations inside other paths;
- the loci marked uncovered in 4.6, for the reasons given there;
- clusters and loci found later by I3-2e get paths under this section's
  addition rule.

### 4.5 Protocol and independence

A tracer that authored none of the iteration 3 member text traces every
path from route entry on S0, S1 and S2, in that order, and from frame
entry on each subject that publishes a frame for the path's task. For each
trace it records:

- the entry;
- each section acquired, as `file#heading` with its bytes;
- each determination applied, as `file:line`;
- the rivals met and the reconciliations made;
- the guard results;
- the eight measures.

The paths, tasks and dimensions are those above. A Claude tracer is a
declared same-family exception (CONSTRUCTION_BINDING §1), so the result
is working evidence. The integrated assessment by a reviewer the product
owner assigns checks the grouping, the traces and the uncovered paths.
Desk tracing measures the method's deciding structure. Actual use by
fresh actors is measured separately (PLAN §5), and neither stands in for
the other.

### 4.6 Coverage of rival loci

Each rival or duplicate locus of section 3 is listed with the path that
traverses it, or as uncovered with its reason. A duplicate whose text
agrees with its owner yields no different outcome on any path. It is
checked for consistency by the working source reviews, not by a path.

| Cluster | Locus | Path |
|---|---|---|
| R1 | CONFORMANCE:24, EVALUATION:352 | DP-02 |
| R1 | TRAVERSAL:760, :964; AXIOMATIC_CALCULUS:524 | DP-29 |
| R2 | EXECUTIVE_BASELINE:991 | DP-30 |
| R2 | EVALUATION:454 | DP-01 (route through EVALUATION §4) |
| R2 | FOUNDATIONS:881 against REFERENCE_FRAME:277 and EXECUTIVE_BASELINE:619 | DP-01, DP-30 |
| R3 | EXECUTIVE_BASELINE:439, :442 | DP-03 |
| R3 | ODD:1049, :1071 | DP-14 |
| R4 | GETTING_STARTED:550; stdo-status skill:56 | DP-31 |
| R4 | PRODUCT_DEFINITION:416–418 | DP-05 |
| R5 | TRAVERSAL:760 | DP-29 |
| R5 | EXECUTIVE_BASELINE:619 | DP-30 |
| R5 | basis template:86; EXECUTIVE_BASELINE:393–396 | DP-21 (owner side), DP-31 (template) |
| R6 | REFERENCE_FRAME:372–380 against ACTIVATION:487–493; REFERENCE_FRAME:461 | DP-06 |
| R6 | ACTIVATION:465, :494, :498, :600 (rc.2 links) | DP-06, DP-23 |
| R6 | AXIOMATIC_CALCULUS:646 | uncovered: duplicate in agreement with the owner |
| R6 | CONFORMANCE:70 | DP-02 |
| R7 | SPEC_METHOD:902–905, :932 | DP-09 |
| R7 | TICKETS:1142, :1065–1070; EVALUATION:101 | DP-32 |
| R7 | DESIGN_MODULE:1897–1902 | DP-33 |
| R7 | digest-rule duplicates (PRODUCT_DEFINITION:876, DESIGN_MODULE:1889, SPEC_METHOD:855, ASSURANCE:788) | uncovered: duplicates in agreement |
| R8 | EXECUTIVE_BASELINE:1273–1281 | DP-34 |
| R8 | REFERENCE_FRAME:889 | DP-08 |
| R9 | EVALUATION:297, SPEC_METHOD:340 | DP-07 (route), otherwise duplicates in agreement |
| R10 | SPEC_METHOD:609, DESIGN_MODULE:54 against DESIGN_MODULE:1418, REFERENCE_FRAME:699 | DP-25 |
| R10 | SPEC_METHOD:600–602, ASSURANCE:1040–1044 | DP-35 |
| R10 | stdo-work skill:111 | DP-31 |
| R11 | TICKETS:1005–1010 | DP-10 |
| R11 | EXECUTIVE_BASELINE:1103, :885 | DP-34 |
| R11 | SPEC_METHOD:1656 (author identity) | DP-10 |
| R12 | REFERENCE_FRAME:282–287, AXIOMATIC_CALCULUS:481, IDENTITY:194–196 | DP-36 |
| R12 | DESIGN_MODULE:769, PRODUCT_DEFINITION:77 | uncovered: the same question in a profile and in packaging; a path is added if I3-2e finds their lists yield a different outcome |
| R12 | proxy limit at EVALUATION:230–235, ACTIVATION:408–409, IDENTITY:198 | DP-11 |
| R12 | recording without review at ACTIVATION:426, TICKETS:1135, EXECUTIVE_BASELINE:171 | DP-16 |
| R13 | SPEC_METHOD:494–500, :1466; PROFILES:136–142 | DP-12 |
| R13 | ACTIVATION:1322, ASSURANCE:1096 | uncovered: the same vocabulary defect in two further tables; checked row by row in I3-4a |
| R14 | UX:259, :302 | DP-15 |
| R14 | EXECUTIVE_BASELINE:402 | DP-34 |
| R14 | TICKETS:286 | DP-13 |
| R14 | closure condition at SPEC_METHOD:924, TICKETS:1121, EXECUTIVE_BASELINE:1651, template :165, stdo-ticket skill:68 | DP-13 (TICKETS), DP-31 (template, skill); the others duplicates |
| R14 | ODD homonyms | DP-14 |
| R16 | EXECUTIVE_BASELINE:656, ACTIVATION:322, REFERENCE_FRAME:980, RF-009 | DP-16 |
| R16 | EXECUTIVE_BASELINE:1290, :165–178 | DP-34 |
| R16 | templates, stdo-work skill:117, stdo-help skill:53, GETTING_STARTED:486 | DP-31 |
| R17 | TICKETS:481 | DP-24 |
| R17 | GETTING_STARTED:383 | DP-31 |
| R18 | ACTIVATION:849, SPEC_METHOD:1121 | DP-17 |
| R18 | UX:80, :755 | DP-37 |
| R19 | AXIOMATIC_CALCULUS:458–459, REFERENCE_FRAME:276, AXIOMATIC_CALCULUS:492 | DP-18 |
| R19 | PRODUCT_DEFINITION:484 | DP-38 |
| R20 | EVALUATION:278 | DP-39 |
| R20, R29 | WORLD_MODEL:529; REFERENCE_FRAME evidence translation | DP-40 |
| R29 | SPEC_METHOD:1757–1764 | DP-26 |
| R21 | AXIOMATIC_CALCULUS:1243, PROFILES:19, PRODUCT_DEFINITION:571; FOUNDATIONS:851 | DP-19 |
| R21 | UX:74, :523; DESIGN_MODULE:2272; TRAVERSAL:1426; EXECUTIVE_BASELINE:1288 | DP-19 |
| R22 | REFERENCE_FRAME:292–298, AXIOMATIC_CALCULUS:1044 | DP-20 |
| R23 | ACTIVATION:527, PRODUCT_DEFINITION:879 | DP-20, DP-23 |
| R23 | UX:392 | DP-37 |
| R23 | ODD:1644 | uncovered: an in-member summary, checked as a duplicate in I3-3c |
| R24 | hard-stop binder at EXECUTIVE_BASELINE:393–396 | DP-21 |
| R25 | TICKETS:1019 | DP-21 (route through EVALUATION §5 to its consumers) |
| R25 | EXECUTIVE_BASELINE:1183 | DP-34 |
| R25 | DESIGN_MODULE:1876 | uncovered: repeats TICKETS's conditions; a path is added if I3-2e finds it differs |
| R26 | SPEC_METHOD:627 | DP-07, as a reconciliation |

Uncovered loci: 7 rows, each a duplicate in agreement, a row-level check
or a conditional addition.

### 4.7 Additions by I3-2e

Writer activation I3-2e added these paths and rows after I3-1 and before
any measurement, under the addition rule at the head of this section. At
2026-10-14T16:58:51Z no `qualification/C3-ITER3/paths/` file existed, so
no trace on any subject existed. Sections 4.1 to 4.6 are unchanged: no
path, task, guard, dimension or row there is removed or redefined. The
new paths use the same subjects, entries, dimensions, outcome rule and
protocol. Each states a task that is also posed on S0.

| Path | Task kind | Situation the task states | Clusters | S1 and S2 entry | Guard items |
|---|---|---|---|---|---|
| DP-41 | work | a project's frame basis, written from the starter template, marks one mandatory evaluation `non_material`; its frame set then changes and coverage is proposed complete; a tool output is offered as permission to continue | R34, R31, R7, R12 | the basis template and the plugin's work skill | an evaluation leaves coverage only by the owner's exclusion rule and authority; a material change invalidates the coverage result; no tool output, child result or handoff admits a step or grants authority |
| DP-42 | resume | after a repair, one closed review result's candidate has changed and one ticket result's support has not; an observation outside the reviewed claim is proposed as a release blocker | R7, R25, R24 | the plugin's work and status skills; eb-task-d | every invalidator of the owner applied and unrelated valid results kept; a finding blocks only under the one promotion-block rule; no hard stop waived |
| DP-43 | review | a requirements surface narrates a transition and labels current law with a version line | R32 | README route to SPEC_METHOD §2 and WRITING_GUIDE | the owner's modal force kept; only the owner's label uses admitted; one owner for the rule |
| DP-44 | decide | close a ticket whose realisation is proven and whose negative proof is absent where drift is plausible | R14 | README route to SPEC_METHOD §9 and TICKETS | one closure condition applied; review alone does not close |
| DP-45 | work | record a design decision and a closure summary on the project's commentary carrier | R33 | README route to POSTING_GUIDE and TICKETS §1 | commentary establishes no ticket, design or requirement truth; the decision is recorded at its owning surface |
| DP-46 | work | in a human-process tenant, a step reaches its declared time limit before its result is closed | R30 | binding | the limit, its units and its owner are reachable from tier 1; no obligation is dropped; a truthful stop or narrowing is recorded |

DP-46, like DP-26, claims no reduction against S0. S0 has no
build-tenant binding owner (R15, R30), so the outcome rule is applied
against S1 only, and the S0 trace records what an actor reaches.

Expected adverse changes, declared before measurement:
- DP-43, M5 against S0 on route entry, where WRITING_GUIDE refers to the
  owner instead of restating the rule (TO2);
- DP-46, M5 against S1, because the owner moves to tier 1 and the binding
  stays in tier 2 (TO2).

Coverage of the loci added by I3-2e:

| Cluster | Locus | Path |
|---|---|---|
| R7 | stdo-work skill:146–147, :165; stdo-ticket skill:74; GETTING_STARTED:525 | DP-42 |
| R7 | basis template :160–164, :184–187, :191–192; REFERENCE_FRAME:629–630 | DP-41 |
| R7 | EXECUTIVE_BASELINE:1442 | DP-42 (eb-task-d) |
| R7 | EXECUTIVE_BASELINE:546, :814–815; ASSURANCE:728; DESIGN_MODULE:388; WORLD_MODEL:286 | uncovered: domain instances, checked against ACTIVATION §7 by the working check of the member's step 2 activation |
| R10 | basis template :58–61 | DP-31 (template; R10 is among its clusters) |
| R11 | GETTING_STARTED:603 | uncovered: a consumer that acts on the trigger; its added freeze condition is reported for an owner in I3-3d |
| R12 | REFERENCE_FRAME:320, EXECUTIVE_BASELINE:48, AXIOMATIC_CALCULUS:407, ACTIVATION:1200, SPEC_METHOD:819, stdo-review skill:49 | uncovered: domain instances in agreement with FOUNDATIONS:127 |
| R12 | DESIGN_MODULE:769, PRODUCT_DEFINITION:77 (conditional in 4.6) | resolved: domain instances in agreement; no different outcome, no path |
| R14 | SPEC_METHOD:1580–1582; TICKETS:111 | DP-44 |
| R16 | basis template :103–143 | DP-31 (template; R16 is among its clusters) |
| R23 | basis template :201–202; schema selector description | uncovered: duplicates in agreement |
| R24 | basis template :100–101 | DP-42 |
| R25 | basis template :86–87, :91–101; stdo-status skill:68–69 | DP-42 |
| R25 | RELEASE:616 | DP-21 (route through RELEASE; the path is unchanged) |
| R25 | EXECUTIVE_BASELINE:399–400 | DP-34 (the path is unchanged) |
| R25 | DESIGN_MODULE:522 | uncovered: a domain instance of falsification |
| R25 | DESIGN_MODULE:1876–1884 (conditional in 4.6) | resolved: states what the design check covers, not when a finding blocks; no path |
| R27 | basis template :53, :56; the three "adoption" senses; POSTING_GUIDE `Closed` | DP-41 (template senses); otherwise reconciliations inside other paths, as in 4.4 |
| R30 | ACTIVATION:1230–1232, EVALUATION:411–412, SPEC_METHOD:1523–1524, :1714–1715 | DP-46 |
| R31 | EXECUTIVE_BASELINE:565–570; basis template :138–143 | DP-41 |
| R32 | WRITING_GUIDE:92–96, :114–125; SPEC_METHOD:168, :1160–1163; RELEASE:465–466 | DP-43 |
| R33 | TICKETS:71–74 | DP-45 |
| R33 | PRODUCT_DEFINITION:749, :860–863; TICKETS:113–114; EXECUTIVE_BASELINE:149; EVALUATION:176; stdo-ticket skill:63 | uncovered: duplicates in agreement |
| R34 | basis template :53, :155–158, :56 | DP-41 |
| R34 | ADR README templates :41, :45; TENANT_REGISTRY_TEMPLATE:35–41 | uncovered: template-only retention and lifecycle rules with no rival owner text; I3-3f decides whether SPEC_METHOD §10 adopts the ADR rules |
| R34 | templates/README.md:78 | uncovered: a pointer defect, corrected in I3-3d |

The paths of 4.4 are partitioned among I3-7d1 to I3-7d4 by number.
DP-41 to DP-46 need an assignment in PLAN before the S0 and S1 traces
start; this design proposes I3-7d4 or a fifth tracing activation.

## 5. Challenge cases

Item 6 of the reduction requirement asks for independently specified
successful, refused and unresolved cases, including cross-domain
composition, failure preservation and recovery. The actual-use trials in
[PLAN §5](../qualification/C3-ITER3/PLAN.md#5-trial-design) carry them.
Their tasks are drawn from the paths above:

| Kind | Paths whose situations supply cases |
|---|---|
| successful | DP-06, DP-16, DP-18, DP-22, DP-26 |
| refused | DP-10, DP-11, DP-21, DP-36 |
| unresolved | DP-15, DP-17, DP-25, DP-27, DP-37 |
| cross-domain composition | DP-01, DP-19, DP-28, DP-30 |
| failure preservation | DP-01, DP-03, DP-04, DP-05, DP-30 |
| recovery | DP-03, DP-07, DP-08, DP-31 |

The paths added in 4.7 also supply cases: refused, DP-41, DP-44 and
DP-45; failure preservation, DP-46; recovery, DP-42; successful, DP-43. No trial task in PLAN §5 uses them yet.

Expectations are fixed before any trial by an actor that wrote neither
the member text nor the frames. A Claude writer is a declared
same-family exception; a cross-family set is requested through the
product owner.

## 6. Limits

- The inventory is a lower bound (section 1). I3-2e completed the sweep
  of guides, templates and schemas, and a lexical search for wording
  variants. It found 5 clusters and about 60 loci. A rival worded beyond
  those search terms can still be missed, and the integrated assessment
  checks for one. The plugin files that I3-1 left uninspected
  (`plugins/spec/claude-skills/refresh`, `REFRESH.md`, `PRODUCT_BASIS.md`,
  `openai.yaml`) were not read by I3-2e either. They are open for I3-3d.
- Every owner and rival classification is the author's. The integrated
  assessment, by a reviewer the product owner assigns, judges it.
- The pillar account binds a pillar list the product owner has not yet
  signed off.
- The family argument counts are estimates with a stated error.
- No path has been measured. The selection above precedes every
  comparison.
