# Codex V3 Graphify consumer

This consumer transports the latest authored Codex interpretation visible at
checkpoint `8884178770672c933aef706947a864ab6422e1c6`. Its current RC1 end-review
repair package is `d1b33480b46f45bb46198a2f63ca197e84e40e55`, documentary source
`2e0c77b909a97648f8edd70981b9a426662df9cc`, authored account
`0c1ffdb49097c630f9b33a50099e3afb0850d755` and common input
`4c340f7adec9f3c893e3e267b23e4cadeb357854`.

The tenant entry still describes the historical I5 package `b2ad4d99...`.
The selected later RC1 inventory, source inventory and current successor agree
on the package above. This discrepancy is preserved in custody and the input
manifest; the consumer does not edit the candidate or its historical entry.

## Custody and coverage

[`input/manifest.json`](input/manifest.json) authenticates every normal archive
member with its immutable repository path, commit, Git blob, byte count and
SHA-256. [`input/candidate.tar.gz`](input/candidate.tar.gz) contains the complete
90-file current package, the exact authored determinations and a small selection
of current construction/qualification records and compiler source. It omits
historical qualification archives. Archive metadata and gzip time are fixed.
`prepare.py` recreates these exact bytes using immutable Git objects and refuses
to replace different existing outputs:

```sh
python3 dogfood/stdo-v3-i5-codex/prepare.py
```

The complete native program has 712 clauses, 732 selectors, five residuals and
no declared symbols. Its semantic account has 708 determinations and 37 shared
contracts. All 81 documentary member pins and the interpretation's program,
semantic-account, vocabulary, frames and mapping pins are checked during
acquisition. The inherited `iteration-3-r2` URI namespace remains unchanged.

`repo://codex-v3/successor/` resolves to `package/` inside custody. Native frame
references and vocabulary references resolve into that same package. The
encoding theory remains the exact external STDO 2.5.1-rc.2 calculus; the
successor's own calculus document is an interpreted subject member.

## Commands

From the independent `a_c/` directory:

```sh
python3 dogfood/v3_graphify.py --tenant codex build
python3 dogfood/v3_graphify.py --tenant codex check
python3 dogfood/v3_graphify.py --tenant codex find 'applicable independence conditions'
python3 dogfood/v3_graphify.py --tenant codex select 'urn:codex-stdo3:iteration-3-r2:index:FOUNDATIONS.parallel-assurance-and-provenance'
```

The representation is a proposed-model view. Explicit native references supply
required closure. Conditional and provenance routes remain inspectable without
becoming unconditional dependencies. Clause-local scopes, JSON Pointers,
qualification references, exact conditions, inline contracts and source routes
remain authored content. Search and selection do not establish applicability,
predicate satisfaction or a work grant.

The five retained residual records carry two release questions and the known UX
compliance conflict at its three preserved loci. The candidate's current return
leaves affected independent readback, material consumer/complete-member
coverage, actual-use/context qualification, owner decisions, acceptance,
adoption and publication open. Transport checks and actual Graphify compatibility
do not settle those questions or demonstrate an efficiency gain. The original
Codex worktree and its independent review remain separate and untouched.
