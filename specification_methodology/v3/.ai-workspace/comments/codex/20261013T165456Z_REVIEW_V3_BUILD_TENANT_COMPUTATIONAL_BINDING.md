# REVIEW: Build-tenant computational binding

**Author**: Dimitar Popov
**Date**: 2026-10-13T16:54:56Z
**Addresses**: `832efd3f68b0557fdce2826e5efaf811b448c924` compared with `8828aea60988b8aa11657d8f74ff2e7ce5b252aa`
**Status**: Complete — bounded source review; owner acceptance remains open

## Result

No changes required within the bounded review. The update implements the owner's clarification recorded in [T-001](../../tickets/active/T-001-common-definition-and-checkpoints.md#owner-instruction): the build tenant binds the requirements calculus to a computational calculus, which is grounded in a concrete execution environment, including a human process.

The fresh reader, `v3_binding_review`, read the frozen change independently of its authorship and returned no material findings. This is a same-family Codex source review. It supplies no C3 member acceptance, execution qualification or release conclusion.

## Checked relationships

| Relation | Source and finding |
|---|---|
| Requirements to computation to execution | [Product](../../../specification/PRODUCT.md#build-tenant-binding), frozen lines 60–64, states the relationship. The [binding requirement](../../../specification/requirements/README.md#build-tenant-binding-requirement), lines 46–55, owns the detailed obligations. Human, machine and mixed processes are covered within the common requirements. |
| Representation and execution | The binding requirement distinguishes author, actor and operation kind. Human participation alone does not establish human adjudication. An a_c representation supplies neither an executor nor execution conformance by its structural validity. |
| Meaning and authority | Conformance must preserve applicable authority, independence, failure and recovery conditions. The [discriminators](../../../specification/conformance/README.md), lines 21–24, reject replacing a required human decision or merging required independent assessments even when outputs match. |
| Use by the method | The [C3 Spec Method obligation](../../../specification/PRODUCT.md#c3-construction-contract), line 295, consumes the binding requirement. Acceptance criterion 5, line 350, consumes its conformance cases. The [tenant entry](../../../build_tenants/README.md) routes both candidates to the requirement. |
| Reuse and scope | The same calculus may serve different environments where its laws hold. Resource accounting is limited to material obligations. External runtimes remain outside this Product; the five-layer design remains a reference example. |
| Categorical claims | The architecture paragraph in [the proposed formalisation](../../../specification/requirements/PRINCIPLES.md#proposed-formalisation-and-open-claims) admits people, machines and combinations. The conditional demonstration standard remains unchanged; the update proves no new category, functor or equivalence. |

## Verification and limits

- Eight common files changed at the reviewed commit. Whitespace checking passed, all 173 checked affected links resolved, and the Product Definition verified valid.
- The exact installed builder, `v2.5.1-rc.2`, verified against manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
- Frozen Git comparison confirms both tenant trees, the v2 source, companion products, cohort, Product Definition and instruction files are unchanged. The six principle bodies, historical C1 disposition and steel-thread contract are also unchanged.
- The reader made no mutations and read no tenant implementation bodies. No runtime or human-process trial was performed.

The clarification is ready for owner review. The next C3 input snapshot and tenant activation still follow their existing sign-off and admission conditions.
