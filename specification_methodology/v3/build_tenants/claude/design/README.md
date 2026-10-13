# Claude Design

This territory holds the Claude build tenant's HOW: how its candidate of
the product is organised and how the tenant builds it. The common WHAT is
the [specification](../../../specification/); nothing here replaces it or
is accepted by being present.

| File | Standing | Content |
|---|---|---|
| [DOCUMENT_STRUCTURE.md](DOCUMENT_STRUCTURE.md) | current design | tiers, members and what each owns; the ownership decisions D1 to D8; the member map; the disposition record; the activation unit; per-member proof |
| [CONSTRUCTION_BINDING.md](CONSTRUCTION_BINDING.md) | current design | this tenant's build-tenant binding for its own construction: how independence is read, the computational calculus, measured resources and limits, the execution environment, declared variances, and the configuration with its reasons |
| [CROSS_SYNTHESIS.md](CROSS_SYNTHESIS.md) | current design | the parts taken from the Codex candidate, with exact sources, receiving owners, frontier cones, mode, the frame generator's requirements and the review of ported text |
| [PRINCIPLES.md](PRINCIPLES.md) | accepted C1 record, frozen | the tenant's C1 principles attempt, accepted at SHA-256 `28c9b1275ca23c53d80cf64afa45acf0d25ce8aa7daddd62b5c7aaf490b2b7ec`; kept byte for byte because that digest is the accepted subject and other records link to its sections |

PRINCIPLES.md is a record of C1, not current design. Where it and the
current common specification differ, the specification governs and the
current design files apply it. In particular:

- its proposal to unify the RF-012 and AC-007 algebras (the reference-frame
  and a_c result algebras) as a later capability (correction 4) is settled
  by the
  [single result algebra requirement](../../../specification/requirements/README.md#single-result-algebra-requirement)
  and applied in decision D1;
- its open question on independence across model families (gap 7) is
  governed by the Independence paragraph of the
  [C3 Construction Contract](../../../specification/PRODUCT.md#c3-construction-contract)
  and the conformance discriminator on an author reviewing in a fresh
  context, which [CONSTRUCTION_BINDING](CONSTRUCTION_BINDING.md) section 1
  applies to this rebuild;
- its proposed principles C and P0 to P6 are carried into the candidate's
  FOUNDATIONS §3, where their standing is stated.

The current rebuild's decisions and record are in
[qualification/C3-SYNTHESIS/](../qualification/C3-SYNTHESIS/LEDGER.md), and
its work plan in [PLAN](../qualification/C3-SYNTHESIS/PLAN.md).
