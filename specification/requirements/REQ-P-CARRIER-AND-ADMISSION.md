# REQ-P-CARRIER-AND-ADMISSION — Independent Encoding Boundary

Family: `REQ-P-CARRIER-*`
Status: Active
Category: Capability
Design ownership: carrier-neutral boundary owned by WHAT; each selected carrier
tenant owns only its encoding, canonicalization, and structural carrier law

Derives from: `../PRODUCT.md#core-relation`,
`../PRODUCT.md#extension-boundary`, `../PRODUCT.md#authority`

## Purpose

Allow multiple direct carrier realizations without allowing encoding or
structural validation to shape or ratify accepted semantics.

## Requirements

### REQ-P-CARRIER-001

Every carrier tenant shall bind one exact Carrier Basis
and one exact Carrier Profile before construction.

### REQ-P-CARRIER-002

A Carrier Profile shall map the complete accepted common
program directly into its selected carrier. It shall not import another tenant
as a mandatory intermediate representation.

### REQ-P-CARRIER-003

Carrier construction shall receive only the accepted
program, accepted selection ledger, exact accepting semantic-selection
judgment, exact carrier basis, and exact profile. Before construction, the
tenant shall verify that the judgment accepts those exact program and ledger
identities. It shall not reopen semantic selection or interpret structural
eligibility as acceptance.

### REQ-P-CARRIER-004

A carrier unable to represent accepted meaning shall
return an explicit profile gap or refusal. It shall not omit, approximate,
rename, or reinterpret accepted records.

### REQ-P-CARRIER-005

Carrier construction shall produce canonical immutable
bytes and identity before Carrier Admission is evaluated.

### REQ-P-CARRIER-006

Carrier Admission shall validate the unchanged carrier's
exact basis, profile, canonical bytes, identity, record law, and closed
references and return a separate admitted or refuse judgment.

### REQ-P-CARRIER-007

Carrier Admission shall not construct, transform,
rewrite, rename, reissue, or semantically accept its subject. Refusal shall
leave the subject identity and bytes unchanged.

Carrier Admission shall not synthesize or replace the semantic-selection
judgment. Admission proves only the declared structural properties of the
unchanged carrier subject.

### REQ-P-CARRIER-008

Structural reliability means typed, closed, canonical,
addressable, reproducible, and structurally rejectable under an exact carrier
law. It does not mean that probabilistic extraction is true or uniquely correct.

### REQ-P-CARRIER-009

Different carrier bases or profiles produce distinct
Axiom Index artifacts even when they encode the same accepted program. Their
shared accepted-program identity shall remain externally comparable.

### REQ-P-CARRIER-010

Carrier-specific code, validators, schemas, and runtime
libraries belong to the carrier tenant HOW and shall not become common Product
authority.
