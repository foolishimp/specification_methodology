# Claude Tenant Design: a_c Interpretation

This file designs the current a_c interpretation of this tenant's
candidate for iteration 3. a_c is the axiomatic calculus: a typed
representation of a method's logical constraints, here written as a
program of symbols, clauses and residuals that the pinned Axiom Indexer
can check for structure. The file is tenant HOW. It accepts nothing and
creates no rule owner. It answers Codex finding F3, which is open: no
current interpretation exists ([C3-ITER3/F1-F5](../qualification/C3-ITER3/F1-F5.md)).

Terms used here:

- The **interpretation** is the model: symbols and constraints bound to
  the meaning of the candidate's members.
- The **carrier** is the set of files that encode it: program, bindings,
  maps, projections.
- The **checker** is `ac.py` of the pinned Axiom Indexer release.
- A **source-to-model disposition** records, for one heading section of a
  member, how that section is represented, or why it carries no
  determination.
- A **fragment** is the part of the program one Writer activation
  authors for one group of members.

## 1. What the common specification requires

| Obligation | Owner |
|---|---|
| Represent the method's logic from its owning prose; bind the exact method subject and, separately, the calculus basis and signature | [constraint surfaces](../../../specification/requirements/README.md#constraint-surfaces-and-logic-compression) item 2; [A_C_DEPENDENCY, Fixed Theory](../../../specification/requirements/A_C_DEPENDENCY.md#fixed-theory) |
| Distinguish premise, derived consequence, policy choice, observation and unresolved claim; shared premises and revisable relations allowed; no tree-only encoding or execution order imposed | constraint surfaces item 2 |
| Cover every material owned determination with its dependencies, conditions, exceptions, permitted choices and unresolved matters; each resolves to its current owning source and basis | constraint surfaces item 3 |
| A residual or external predicate keeps its source and required acquisition and authorises no dependent work before its premise is established | constraint surfaces item 3 |
| A task projection carries sufficient constraints and the material inputs or acquisition routes | constraint surfaces item 4 |
| Prose, interpretation and views express the same determination; an approximation declares its adequacy relation and end-to-end bound | constraint surfaces item 5 |
| Ordinary entry selects the current exact interpretation and its limits; historical models are identified as historical | constraint surfaces item 6 |
| Fidelity evidence on independently specified permissible, prohibited and unresolved cases; a source-first reviewer checks relationship, coverage and actual task use | constraint surfaces item 6; [A_C_DEPENDENCY, Proof Claims](../../../specification/requirements/A_C_DEPENDENCY.md#proof-claims) |
| Theory, interpretation, carrier and checker keep separate identities and proof boundaries; structural validity is not fidelity; tenant output is not the released STDO Representation | constraint surfaces item 7; A_C_DEPENDENCY Standing and Proof Claims |
| Mechanical use only on a separately selected evaluation, through a verified copy of the pinned release | [A_C_DEPENDENCY, Directed Mechanical Dependency Relation](../../../specification/requirements/A_C_DEPENDENCY.md#directed-mechanical-dependency-relation) |

At the construction return, declared gaps with their scope are allowed
(ORACLE C3 [R]). C3 closure for this tenant needs complete required
coverage and independently assessed fidelity. Missing mechanical results
are no defect while no evaluation is selected (ORACLE C8).

## 2. Subject, basis and signature

Three coordinates, recorded separately in the set's README:

| Coordinate | Value |
|---|---|
| Method subject | the 23 members under `standards/` at the frozen iteration 3 candidate commit, named at the freeze (PLAN I3-6), with each member's SHA-256. The candidate's own AXIOMATIC_CALCULUS is part of this subject: it is represented, not used as the encoding basis |
| Calculus basis | `stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`, SHA-256 `cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d`, recorded as the program's `calculus_ref` |
| Signature | the vocabulary URIs declared in the program's `vocabulary_refs` under `urn:stdo-3:claude:i3:vocabulary:`, listed with their meanings in the set's `SIGNATURE.md` |

The released interpretation's encoding basis and its standalone
acquisition are an open owner decision
([PRODUCT, Open Owner Decisions](../../../specification/PRODUCT.md#open-owner-decisions)).
This design does not settle them; it uses the construction basis above
(ORACLE Q7).

## 3. Encoding

### Record kinds

The signature follows the candidate's own typed records
([AXIOMATIC_CALCULUS §3](../standards/AXIOMATIC_CALCULUS.md#3-typed-records)):
semantic object, typed relation, constraint, latitude and residual. The
checker's schema fixes two clause types, `relation` and `constraint`, and
four residual kinds, `ambiguity`, `conflict`, `omission` and `unresolved`
(`program.schema.json` at the pinned tag). Everything else is carried by
declared operators and argument roles.

### Standing

Every clause carries exactly one argument with role `standing`, whose
reference is one of five standing symbols:

| Standing | Meaning | Required companions |
|---|---|---|
| `premise` | a commitment the candidate states without deriving it (FOUNDATIONS §3, P0 to P6 and C, or a domain premise named by its owner) | the owning section |
| `consequence` | a determination the candidate derives | one or more `support` arguments to the premise or consequence clauses it follows from, and the operator `derives` where the source states the derivation |
| `policy-choice` | a determination its owner chooses among admissible alternatives | an `owner` argument naming the owning section; any stated reason |
| `observation` | a recorded fact about a subject, such as a pinned digest or an installed release | the source of the observation and its basis |
| `unresolved` | a claim the source leaves open | a linked residual (below) |

A hollow argument, in which a whole rule is filed as a policy choice to
avoid stating its premises, is a fidelity defect under this design. A
policy choice names what was chosen and among what.

Kind of support (iteration 5). Standing says how a clause stands in the
derivation; the kind of support says which evidence would establish its
statement, one of the five that
[FOUNDATIONS §4 Formal representation](../standards/FOUNDATIONS.md#formal-representation)
distinguishes: `stated-formula`, `discharged-argument`,
`mechanically-checked-structure`, `externally-assessed-predicate` and
`execution-evidence` (the signature's "Kinds of support" table). A clause
may carry one `support-kind` argument; a clause whose owning section is
the construction relation, the construction synthesis or one of the
assurance relations carries exactly one, and `assemble.py` refuses one
that does not. A kind confers no standing and no truth: a formula is not
discharged by being written, and an external predicate is not assessed by
being labelled. The projected constraint surface keeps the kind with the
standing (AXIOMATIC_CALCULUS Constraint surfaces, condition 1).

### Conditions, force and exceptions

Conservation includes scope, modal force, triggers and exceptions
([reduction requirement](../../../specification/requirements/README.md#foundational-reduction-requirement)
item 3). Each constraint clause carries them as arguments:
`condition` (the scope or trigger), `force` (a literal from `must`,
`must-not`, `should`, `should-not`, `may`), `exception`, and
`qualification` for any other limit the source states. A source sentence
that is a preference stays `should`; a statement that something is not
required stays `may`, never `must-not` (ORACLE C6, J18).

### Latitude

A permitted choice the source leaves to the actor is a clause with
operator `permits` and role `latitude`
([AXIOMATIC_CALCULUS AC-008](../standards/AXIOMATIC_CALCULUS.md#ac-008-explicit-latitude)).
Where the source admits several solutions, each admissible one is
represented; none is preferred unless the source prefers it (ORACLE C10,
J17).

### Ownership, consumers and refinements

Each determination is encoded once, at its owning section. A consumer
section that applies the owner's determination is encoded as a `uses`
relation from the consumer to the owner clause, with any binding the
consumer adds. A consumer that refines the owner, such as a domain result
refinement, is encoded as a `maps-to` clause per refined value: the
refined value, its predicate, the conditions that fix its meaning, and
exactly one core value. A refinement map that does not reach exactly one
core value, or raises standing, is a defect the coverage check reports
([single result algebra requirement](../../../specification/requirements/README.md#single-result-algebra-requirement)).
A frame's exact copy is not encoded again.

### Residuals that block

Each residual (record kind `unresolved`, `ambiguity`, `conflict` or
`omission`) names its source section and the acquisition that would
resolve it. Each clause that depends on the residual's premise carries a
`blocked-by` argument referring to it. The checker's projection includes
every residual affecting an included item, so a projected task surface
shows the block. A residual never appears as permission or a satisfied
result (ORACLE C5, J16).

### Source references

Every symbol, clause and residual has `source_refs` naming a heading slug
of its owning section under the source basis
`stdo-3://build_tenants/claude/standards/`. The checker requires heading
slugs, never line numbers. The source-to-model dispositions give line
ranges for human reading.

## 4. Carrier layout

The current set is `a_c/i3/`. Earlier sets stay in place, frozen.

| Path | Content | Author |
|---|---|---|
| `a_c/i3/README.md` | the three coordinates of section 2; the artifact table with SHA-256; coverage totals; the evidence boundary; known gaps with scope; how to reproduce | assembly activation |
| `a_c/i3/SIGNATURE.md` | every vocabulary URI with its meaning and the record kind or role it serves | signature activation |
| `a_c/i3/fragments/<group>.json` | one fragment per member group, each a list of symbols, clauses and residuals under the shared signature | one encoding activation per group |
| `a_c/i3/dispositions/<member>.md` | the source-to-model dispositions: one row per heading section, with line range, disposition (`encoded`, `uses owner`, `refines owner`, `residual`, `no determination`) and the URIs or the reason | the encoding activation of that member |
| `a_c/i3/tools/assemble.py` and its test | merges fragments into one program sorted by URI; checks that every heading section has exactly one disposition, every source reference resolves to a current heading, every refinement maps each value to exactly one core value, every clause has one standing, and every residual-dependent clause carries `blocked-by`. This is a tenant pre-check, not a mechanical result of the dependency | signature activation |
| `a_c/i3/axiomatic-program.json`, `bindings.json` | the assembled program and its URI binding set | assembly activation |
| `a_c/i3/validation-report.json`, `logical-constraint-map.json`, `projections/` | checker outputs, present only after a selected evaluation | checker activation |
| `a_c/i3/fidelity/` | the fidelity cases, fixed before review, and the review results | case and review activations |

The program holds one frame index per published frame task, so a task's
constraint surface can be projected from the same program that the
fidelity review checks.

## 5. Checker route

Mechanical use of the Axiom Indexer needs a separately selected
evaluation. T-002 records that selection of its use remains the product
owner's. The route is:

1. **Selection.** The Executive asks the product owner to select the
   mechanical evaluation of the frozen iteration 3 program, naming its
   exact subject (the program and bindings at the freeze commit) and the
   contract (validate, then project the frame indexes). The decision is
   recorded in the ledger before any run.
2. **Acquisition.** The checker activation materialises the seven Axiom
   Indexer Product members from `refs/tags/axiom_indexer/v2.5.1-rc.2` with
   `git show` into a scratch directory outside any repository, restoring
   the two symlinks, and records the copy's path.
3. **Verification.** Before use it checks: tag object `9bff233c…`, commit
   `9a9c4797…`, repository tree `3a553ceb…`, `axiom_indexer` subtree
   `6dae168d…`; each member's SHA-256 (symlinks hashed by their UTF-8
   target) against the release note `axiom_indexer/releases/v2.5.1.md` at
   the tag; and the inventory aggregate, which is SHA-256 over the lines
   `<sha256>  <kind>  <path>\n` sorted by path (the rule in
   `axiom_indexer/scripts/check_constitution.py` at the tag). The
   executable must be `5a2e0cb5…6c8`, the schema `43326dba…`, the output
   contract `c124264d…`, and the aggregate `55a2061b…`. Any mismatch
   stops the evaluation and returns the drift to its owner.
4. **Run.** `python3 -I <copy>/build_tenants/core/code/ac.py validate`
   then `project` for each frame index in both modes, as in the
   [set-6 reproduction](../a_c/set-6/README.md#reproduction), from the
   frozen bytes. Each command line, exit code, start time and output
   digest is recorded. A second run on the same bytes must reproduce the
   outputs byte for byte.
5. **Claim.** A pass is a structural result for the selected scope only.
   It is not fidelity, truth or acceptance (ORACLE C8, J40).

The I3-1 activation verified step 3 read-only on 2026-10-14: the seven
member digests read from the tag match the release note, and the
recomputed aggregate equals `55a2061bd55ca29e349318a2869bc13518374ef2fa764a73b1688e76d35a63c1`.
No copy was materialised and nothing was run.

Without a selection, the interpretation is still built and its fidelity
still reviewed. Only `assemble.py`'s tenant pre-check is available, and
it is reported as such.

## 6. Fidelity evidence

Fidelity is whether the model preserves the source's meaning, including
premises, consequences and declared choices
([AC-017](../standards/AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity)).
The evidence has three parts.

1. **Cases written first.** A case writer that authored neither the
   member text nor the model reads the source prose, not the model, and
   writes cases before the model is opened. Each case names a
   determination and gives a concrete situation with the source's answer,
   in one of three kinds: a permissible action, a prohibited action, and a
   question the source leaves unresolved, whose correct answer is to stop,
   acquire or refine. Selection: every shared owner of
   [REDUCTION](REDUCTION.md), every refinement map, every residual, and a
   random sample per member at least 10% of its encoded clauses, with the
   seed recorded.
2. **Source-first review.** A reviewer that authored neither reads the
   source, answers each case from the model's projection alone, and
   records agreement, disagreement or a model that cannot answer. It also
   checks the disposition tables for coverage and the standing of each
   sampled clause (hollow arguments, a preference turned into an
   obligation, a missing trigger or exception).
3. **Use.** At least one actual-use trial arm reads a projection from the
   model rather than the prose frame (PLAN §5, arm A4), so actual task use of
   the interpretation is observed.

Under [CONSTRUCTION_BINDING section 1](CONSTRUCTION_BINDING.md#1-three-coordinates-kept-apart),
a Claude case writer or reviewer is a declared same-family exception and
its result is working evidence. The Executive requests a non-Claude case
set and review through the product owner. C3 closure needs fidelity
assessed over the complete interpretation by a reviewer the owner
assigns; the sampled review supports only its stated scope.

Iteration 5 adds group G14, the construction and assurance relations (89
clauses over nine sections of ACTIVATION §1 and FOUNDATIONS §3 and §4)
and the premise P4a. Their cases and review follow the three parts above,
with one addition: the case writer records, for each case, which kind of
support the source gives the determination, so that the review can check
that the encoded kind matches. Until those cases and the review are
written, the fidelity of G14 is unassessed and the set's README says so.

The model is exact, not approximate: each clause states its source's
determination. A projection that omits clauses is a selection, declared
as such, never a weaker restatement. If a later view compresses clauses,
it declares its adequacy relation and end-to-end bound before use.

## 7. Ordinary entry

- `standards/README.md` (currently line 112 describes set-2 to set-6)
  names `a_c/i3/` as the current interpretation and points to
  `a_c/i3/README.md` for its exact subject commit and its limits:
  coverage state, fidelity scope and whether a mechanical result exists.
  The route text is written before the source settles (PLAN I3-4d), so
  README, a member, does not change after it is encoded (fragment G13);
  the changing facts live in `a_c/i3/README.md`, which is carrier, not
  member.
- `a_c/README.md` lists `i3/` as current and marks `t1/` to `t3/`, `set/`
  and `set-2/` to `set-6/` historical, each bound to the member digests it
  names.
- Each historical set README gains one first line stating that it is
  historical and binds earlier member bytes. Its artifacts are not
  changed.
- The bootstrap frame and the frame header name the current set, so an
  actor entering through a frame reaches no historical model as current
  (ORACLE C7, J19).
- No tenant output is called the STDO Representation.

## 8. Size and activations

The members total about 1.65 MB in 23 files. Set-6 encoded part of an
earlier version in 423 clauses. A complete encoding is estimated at 1,800
to 2,600 clauses, an estimate from set-6's density, not a measurement.
Each fragment covers at most about 140 KB of source and is sized for one
fresh Writer in about 45 minutes. Encoding starts only after the source
it encodes is settled (PLAN step 4 starts from the source-settlement commit), because an encoding of text that is
still changing is stale on arrival.

| Group | Members | Source bytes |
|---|---|---|
| G1 | FOUNDATIONS, IDENTITY, PROFILES | about 120 KB |
| G2 | ACTIVATION, CONFORMANCE | about 127 KB |
| G3 | EVALUATION, AXIOMATIC_CALCULUS | about 129 KB |
| G4 | REFERENCE_FRAME | about 93 KB |
| G5 | SPEC_METHOD | about 133 KB |
| G6 | TICKETS, RELEASE | about 140 KB |
| G7 | ASSURANCE, PRODUCT_DEFINITION | about 155 KB, split at the Executive's discretion |
| G8 | EXECUTIVE_BASELINE | about 141 KB |
| G9 | DESIGN_MODULE | about 171 KB, in two halves |
| G10 | ODD | about 100 KB |
| G11 | TRAVERSAL_OCCURRENCE | about 102 KB |
| G12 | WORLD_MODEL, UX | about 146 KB |
| G13 | README, GLOSSARY, WRITING_GUIDE, POSTING_GUIDE, templates, schemas, plugin | about 90 KB of Markdown plus packaging files; mostly `uses owner` and convention rows |
| G14 | ACTIVATION §1 Construction relation; FOUNDATIONS §3 Construction synthesis; FOUNDATIONS §4 Assurance relations and its six subsections (a cross-member group added at iteration 5) | about 40 KB of source, 89 clauses |

The PLAN schedules a signature activation first (signature, standing
symbols, shared premises, core result values, `assemble.py`), then the
fragments in waves of four, then assembly, the checker route if
selected, projections, cases, review and the entry relabel. The
interpretation's [deciding-path role](REDUCTION.md#4-deciding-paths) is
as an optional acquisition route; ordinary entry does not require it.
