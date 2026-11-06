# Source-to-formal correspondence

The exact owner is
`stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`, SHA-256
`cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d`.
Its builder manifest is
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
The common requirements select these obligations; this table does not amend
that calculus or claim all of any neighboring law is formalised.

| Owner clause / requirement | Concrete formal representation or deciding theorem | Exact claim / remaining boundary |
|---|---|---|
| Core Signature; AC-R-001..004; FR-002/006 | `AC.Family`, `AC.Record`, `AC.Model`, `Model.WellFormed`, `checkModel_sound` | Eight distinct tags, full canonical envelope/record content, finite identity/endpoints checks. Source schema/reference-domain interpretation is checked Python, not a Lean theorem. |
| Typed Records; scoped identity, authority and exact basis laws; FR-002/004 | `retained_iff`, `projection_record_conservation`, `projection_authority_basis_conservation`, `projection_parent_conservation` | Exact retained-record equality; original owner/context/scope/basis/payload and parent coordinates conserved. No authority legitimacy or predicate truth. |
| AC-009 Residual Conservation; AC-011; FR-004 | `projection_residual_conservation`, `projection_excluded_residual_exact`, `projection_all_residuals_accounted` | All original residuals remain exact retained unresolved records or named excluded residual records. No residual resolution. |
| AC-010 Material Closure; AC-R-008; FR-003 | `Witness`, `traceSet`, `checkCertificate`; `certificate_seed_inclusion`, `certificate_closed`, `certificate_exact_reachability`, `certificate_least`, `certificate_fixed_point`, `certificate_unique` | Finite directed declared relation; accepted certificate proves exact reflexive-transitive reachability and leastness. Semantic selection/sufficiency of required edges remains external. |
| AC-011 Projection; AC-R-009; FR-004 | `makeProjection`, `project_ok_properties`, `project_ok_exact_reachability`, `projection_excluded_exact`, `projection_external_exact`, `projection_ordinary_exact` | Actual successful operation returns the proved closure with exact retained records and named boundaries. It is a view, not a complete successor model or owner. |
| AC-011 budget prohibition; AC-R-008/012; FR-005 | `projection_success`, `insufficient_budget_refuses`; concrete `success0..31`, `budget_refusal0..31` and toy `0..13` | Local-record-count budget; whole closure or refusal, no truncated success. |
| FR-006/007 | `scripts/import_fixture.py`, `generate_fixture.py`, `check.py`, `AC.Audit`, `AC.Run` | Source custody, exact generation, 204 deciding axiom reports, kernel replay, actual output comparison and adversarial controls. The bridge/runtime trust is explicit. |

The primary source selection is the published supplement's exact native
`C23ca9c0929d7be8570edafaf30542e3daeb8dc1f` /
`Mf7f3f824ee1ac3e048d1b1ea86ce3aae84866e2e9d5010fe5eda2e38e12f4477`.
[Primary custody](../fixtures/stdo-3.0.2/CUSTODY.json) pins copied file bytes,
source locator/checkpoint and canonical model identity. Model raw SHA-256 is
`fc3114dd666218c387a64846b755a14979182f488de64ffff6a6d305a9698793`;
canonical SHA-256 is
`b3f97a2667c277c21417230421aca02c26b3a7b19baa598197e94f67c5439151`.
Both graph carrier inputs recover that same entire model. The adapter generates
index `0..31` in family/ordinal order; its reconstruction check maps every
formal record payload back to exactly that source population member. Reference
paths reach their exact source scalar, and complete schema checks determine
whether each becomes a required pair or boundary occurrence.

The [toy custody](../fixtures/toy/CUSTODY.json) separately pins an existing
application-neutral synthetic model, canonical SHA-256
`d275eb906b8ac2871e6fd7415065c1dabf915242e8583fe3e202bc723a18dec3`.
Its 14 records populate all eight families and test parallel/reversed/self
relations, cycles, repeated references and non-governing boundaries. This
positive control prevents empty traversal/transformation/judgment populations
in the real fixture from being mistaken for coverage of those record families.
Their operations and semantic judgments remain unexecuted.
