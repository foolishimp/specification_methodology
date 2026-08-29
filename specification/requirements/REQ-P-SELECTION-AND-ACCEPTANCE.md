# REQ-P-SELECTION-AND-ACCEPTANCE — Semantic Governance

Family: `REQ-P-SELECT-*`
Status: Active
Category: Governance
Design ownership: semantic-selection and artifact-acceptance boundaries owned
by WHAT; each decision remains with its exact external authority

Derives from: `../INTENT.md#product-relation`,
`../PRODUCT.md#core-relation`, `../PRODUCT.md#authority`

## Purpose

Keep semantic selection, target-artifact acceptance, and release external to
the compiler, structural inspectors, and carriers that produce their subjects.

## Requirements

### REQ-P-SELECT-001

Authorized semantic selection shall evaluate the exact
candidate against the exact corpus and structural judgment and shall return an
immutable semantic-selection judgment whose decision is `accepted`, `rework`,
or `rejected`. An accepting judgment shall bind one exact accepted Axiomatic
Program and one exact selection ledger; a non-accepting judgment shall produce
no accepted semantic subject. `D_Q = eligible` is required but is not semantic
acceptance; `D_Q = refuse` shall prohibit an accepting judgment.

### REQ-P-SELECT-002

Every semantic-selection judgment `J_X` shall bind its own identity; actor;
authority and exact grant; unchanged compilation-candidate identity; unchanged
structural-judgment identity; corpus, calculus, and target-profile bases;
resulting accepted-program and selection-ledger identities when accepted;
evidence-acquisition boundary and admitted evidence; decision; rationale; and
time.

### REQ-P-SELECT-003

Compiler authorship, human presence, successful structural
inspection, carrier construction, or carrier admission shall grant no ambient
semantic-selection authority.

### REQ-P-SELECT-004

The selection ledger shall disposition every candidate record, proposed
source-selection row, and residual exactly once as retained, omitted,
uncertain, reworked, or rejected and shall preserve exact source routes and
rationale. Missing, duplicate, conflicting, or unresolved dispositions shall
prohibit an accepting `J_X`.

### REQ-P-SELECT-005

Semantic selection shall not mutate the candidate or
structural judgment. The accepted program and ledger shall receive new content
identities bound to those unchanged inputs. `J_X` shall point to those
identities and shall remain outside their identity preimages.

### REQ-P-SELECT-006

Semantic selection shall not select a carrier, construct
an index, admit carrier bytes, accept a target artifact, or authorize release.

### REQ-P-SELECT-007

A target Product may accept an exact admitted Axiom Index
artifact only through a separate judgment binding target authority, grant,
artifact identity and bytes, accepted program, carrier admission, evidence,
decision, rationale, and time.

### REQ-P-SELECT-008

Rework, rejection, or artifact refusal shall not erase or
overwrite the evaluated candidate, program, carrier, or prior judgment.

### REQ-P-SELECT-009

Accepted-population conservation shall be total and typed rather than inferred
from cardinality. Every retained or uncertain candidate item shall map to exact
accepted model or calculus-conforming residual identities. Every reworked item
shall map to exact replacement identities with source-preserving lineage. Every
omitted or rejected item shall retain its source route, disposition and
rationale. Every accepted model record shall resolve to candidate or rework
lineage.

### REQ-P-SELECT-010

The exact Target Profile shall declare which omission, rejection, uncertainty,
split, merge, and replacement relations permit semantic acceptance and which
require rework or rejection. A selection process shall not invent that policy
from a carrier limitation, structural-inspection result, or local heuristic.

### REQ-P-SELECT-011

Carrier construction and context projection shall require and verify the exact
accepted relation `(P_X, S_X, J_X)`. Structural eligibility, successful
encoding, carrier admission, projection closure, or downstream use shall not
synthesize, infer, or replace `J_X`.
