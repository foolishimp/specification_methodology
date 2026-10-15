

### Item `REFERENCE_FRAME §1 declaration` (not a frontier row; R2b2-03: the declaration must state direction, loss and target context as the rule requires; repaired with one declaration sentence)

Judge: does the declaration below meet the rule below? Answer in the row form with id `REFERENCE_FRAME.md#imports-into-this-context`, `conserved` meaning the declaration meets the rule, `changed` meaning it does not (say what is missing), `indeterminate` if you cannot tell.

The rule, `FOUNDATIONS.md#imports-between-members`:

```text
A member that uses a concept another member defines imports it and does
not define it again (P1, P3; provenance
`stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#bounded-context-semantic-resolution`,
whose semantic import adopts the cited meaning unchanged). An import is
reference-only. Source and target meanings are identical owner-qualified
references, not new local definitions. Direction is from the named source
to the importing context; loss is none and no translation or ownership
transfer is asserted. An import provides no semantic, evaluation,
operation or decision authority (P6; Authority kinds, What creates no
authority). A use that changes, narrows or loses
the source meaning is not an import and is never declared as one.

An import declaration states, for each imported concept (P1, P3, P6):

- what is imported: the concept, under the name its owner gives it;
- its owner: the owning section of the member that defines it, which is a
  place in the text, not a semantic authority (Authority kinds above);
- the source context: the bounded context the owning member declares, or
  that member itself where it declares none;
- the target context and the member that owns it;
- the direction and the loss, which one sentence may state for all the
  concepts of one declaration.

An import takes one of two forms. A declaration states these contents
for each imported concept in one place; between members of this corpus it
rests on the authority of the Product that owns the corpus, so the
relation is owner-authorised (P6). A reference at the point of use
that names the owning section is also an import: it states what is
imported and its owner; its source context is the one the list above
names, its target is the using member's context, and its direction, loss
and lack of authority are those stated above. A concept another member
defines enters a bounded context only by one of these forms, never by
proximity or equal spelling (P1, P3).

An activation binds each member's distinct coordinates in its selected
complete governing basis; equal cut selection does not mean equal member
coordinates. Adoption is a target's taking an imported concept into use
under the conditions its source states, which are its adoption premises.
Lifecycle and adoption remain source-owned. A changed member,
selected basis, source declaration or adoption premise requires fresh
applicability before use. An activation lacking the source meaning,
adoption or authority binding reports that unresolved relation before
dependent reliance rather than interpreting it from equal spelling (P3,
P5). For an evaluation that depends on the imported concept, a missing
source meaning, adoption or authority binding is an undeclared material
relation, the ground of `out_of_frame` ([Results](#results), Out of frame
or indeterminate); a changed member or basis whose applicability is not
yet re-established is the ground of `invalid_basis` (§4 Results).

Purpose and material relation of the declaration's contents, its two
forms, a member as source context and the two grounds above: a concept
used outside its owning section keeps one meaning and one owner, so two
members cannot answer one question two ways, and using a concept grants
no authority over it (P1, P6).
```

The declaration, `REFERENCE_FRAME.md#imports-into-this-context`:

```text
This member imports the concepts below into
`urn:stdo:bounded-context:reference-frame-evaluation` under the import rule
of [FOUNDATIONS §2](FOUNDATIONS.md#imports-between-members), which states
what an import is, its direction and loss, and that it transfers no
ownership and confers no authority. As that rule requires of a
declaration: the direction is from each source member named below to
this context, and the loss is none, for every concept in the table; the
target context is `urn:stdo:bounded-context:reference-frame-evaluation`,
owned by this member as Scope above declares. FOUNDATIONS, ACTIVATION and
EVALUATION declare no bounded-context identity, so each row's source
context is its member (P1, P3).

| Referenced concept | Source context | Exact source concept and owner |
|---|---|---|
| evaluation, evaluation family, workspace, material-relation manifold, coordinate, topology, capability envelope, reference frame, activated frame, frame set, active frame configuration, lens; role, persona, abstraction and component | FOUNDATIONS | [Frame objects](FOUNDATIONS.md#frame-objects), FOUNDATIONS §2 |
| subject, outcome, basis, material relation, evidence, actor, claim, judgment, residual | FOUNDATIONS | [Ontology](FOUNDATIONS.md#2-ontology), FOUNDATIONS §2 |
| frame-set, semantic, evaluation, operation and decision authority; actor identity | FOUNDATIONS | [Authority kinds](FOUNDATIONS.md#authority-kinds), FOUNDATIONS §2 |
| frame disjointness, evaluation independence and assurance independence | FOUNDATIONS | [Disjointness and independence](FOUNDATIONS.md#disjointness-and-independence), FOUNDATIONS §2 |
| the frame tuple ⟨Q, B, M, C, I, A, E, X, R, J, K, D⟩ | FOUNDATIONS | [The frame tuple](FOUNDATIONS.md#the-frame-tuple), FOUNDATIONS §2 |
| the core result values, their meanings and standing, the evaluation not performed, and refinements of the core | FOUNDATIONS | [Results](FOUNDATIONS.md#results), FOUNDATIONS §4 |
| conjunction and composition of results, with the declared decision rule | FOUNDATIONS | [Conjunction of results](FOUNDATIONS.md#conjunction-of-results), FOUNDATIONS §4 |
| activation as a step: intake, admission, applicability, context construction with its size measurement, activation and evaluation | ACTIVATION | [The step](ACTIVATION.md#1-the-step), ACTIVATION §1; [Context construction under an envelope](ACTIVATION.md#2-context-construction-under-an-envelope), ACTIVATION §2 |
| the step's result refinements and disposition | ACTIVATION | [Step results and disposition](ACTIVATION.md#3-step-results-and-disposition), ACTIVATION §3 |
| the closed result and its reuse | ACTIVATION | [Closed result and reuse](ACTIVATION.md#7-closed-result-and-reuse), ACTIVATION §7 |
| qualification of a frame and of this method | EVALUATION | [Qualification of frames and of the method](EVALUATION.md#7-qualification-of-frames-and-of-the-method), EVALUATION §7 |

Scope bounds what
this member owns; a concept of those kinds that another member defines,
such as evaluation, basis, the activation step, the core results or
qualification, is imported here, and this member defines it no second
time. A refinement this member states, such as the function outcomes of §5
or the coverage statuses of §8, names its owner in this table and maps
back to it. A frame or frame family that a profile or product declares in
this context is that owner's specialisation under Scope above and is not
imported here (P1, P3, P6).
The declaration is new in this corpus. Purpose and material relation: each
concept used here keeps one owning section, so its meaning cannot diverge
between that owner and this member (P1, P6).
```
