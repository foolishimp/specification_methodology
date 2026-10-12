# TASK I: check a product definition and resolve one term

## Subject

Product `clinic-booking`: appointment booking for a group of clinics. The
facts below are the whole subject; the record is invented for this task
and is evidence about no real product.

Authorities: Ana owns the clinic-booking Product and its specification
`booking-spec.md` (basis: booking-spec v4). Ravi owns the separate billing
product and its specification `billing-spec.md` (basis: billing-spec
v2.1). No relation between the two specifications is recorded anywhere.

`booking-spec.md` §1 declares the bounded context
`urn:clinic:ctx:booking` for the whole document, owned by Ana under
booking-spec v4. Its §2 defines "Visit: a reserved time slot with one
clinician". Its §3 holds R-7: "A cancelled Visit is not charged."
`billing-spec.md` §1 declares `urn:clinic:ctx:billing`, owned by Ravi
under billing-spec v2.1; its §2 defines "Visit: a completed billable
encounter".

The product definition `product.json` holds:

- `$schema` and `kind: "stdo.product-definition"`;
- `product`: identity `urn:clinic:product:clinic-booking`, a display name,
  a source-project locator, and `bounded_context` set to the list
  `["urn:clinic:ctx:booking", "urn:clinic:ctx:billing",
  "urn:clinic:ctx:patient-records"]`;
- `constitution.stdo`: the STDO repository and the selector `v3.*`; no
  installed release basis and no manifest digest;
- `constitution.additional_authorities: []`, `constitution.entrypoints`
  and `constitution.agent_bootstrap`, each filled;
- `local_constitution`: `axioms: []`, `overrides: []`, and one
  disambiguation `{term: "Visit", context: "urn:clinic:ctx:booking",
  disambiguates: ["booking-spec.md#visit", "billing-spec.md#visit"],
  resolves_to: "booking-spec.md#visit", uri: "docs/decisions/D-3.md"}`;
  `D-3.md` reads "In booking, Visit means the reserved slot" and names no
  author or authority;
- no `reference_frame_bases` key;
- `what`: the Intent, Product and specification bindings, plus a field
  `requirements_text` holding a copy of the full text of R-1 to R-9;
- `how`: one build tenant, `tenant-a`;
- `ticketing`: Goals, ticket and comment bindings, no sprint;
- no `composition` key, although clinic-booking calls the billing
  product's API.

The project glossary has three rows, in this order: `Visit` ->
`urn:clinic:ctx:billing` -> `billing-spec.md#visit`; `Visit` ->
`urn:clinic:ctx:booking` -> `booking-spec.md#visit`; `Patient` ->
`urn:clinic:ctx:patient-records` -> `patient-records-spec.md#patient`.
No file `patient-records-spec.md` exists.

Lee, a developer, implemented R-7 by reading billing's encounter status,
because the billing row comes first in the glossary and 30 of the 40 code
files use the billing meaning.

## Instruction

1. Under a heading `Definition`, name each required relation that is
   missing or defective and state its defect; do not list conformant
   relations.
2. Under a heading `Visit in R-7`, walk the resolution steps in order for
   the occurrence of "Visit" in R-7, give its semantic address and its
   result (exactly one concept, unresolved or ambiguous), and say whether
   Lee's selection is lawful and why.
3. Under a heading `D-3`, say whether the disambiguation binding resolves
   anything as it stands, naming each coordinate it lacks, and whether it
   needs a cross-context relation.
4. Under a heading `Glossary`, say for each of the three rows what it
   contributes to resolution and whether it is a valid row.

Then, under a heading `No method source`, list anything the task needed
that the METHOD block did not supply; write `none` if nothing.

Return only those five parts, in that order. Do not restate the subject.
