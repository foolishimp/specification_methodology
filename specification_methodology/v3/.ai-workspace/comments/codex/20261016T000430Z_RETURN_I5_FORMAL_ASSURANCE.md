# I5 Formal Assurance: Common Specification Return

The common successor adds [Assurance of Construction](../../../specification/requirements/ASSURANCE.md) as the single requirement owner for preservation, assertions, observations, mutual assurance and evidence validity after change. The owner's instruction and bounded effects are in [EC-COMMON-I5-04](../../tickets/active/T-001-common-definition-and-checkpoints.md#iteration-5-formal-assurance). This post records construction evidence; it grants no ratification, tenant admission or acceptance.

## What Changes

The model relates an obligation's interpretation, the assertion derived from it, the observations available to evaluate it, and the conclusion those observations can support. Necessary conditions and sufficient conditions are explicit. Complete decision from an observation requires that no indistinguishable admissible states disagree on the target predicate. Preservation through A → Z requires each step and each join, plus the connection to Z; local checks do not provide the missing argument.

Mutual assurance exposes common failure causes and distinguishes source fidelity from execution records. Different actors and shorter assertion paths do not establish correctness or independence. Quantified claims state their probability model; the conditional chain rule supports the miss calculation without silently assuming independent checks. Bayes' rule makes the required likelihoods and prior explicit, not available by declaration.

Targeted reassessment distinguishes why an assertion is justified from what can invalidate its execution or use. Changes to requirements, refinements, code, observations, environments and assumptions can affect evidence. Supported unchanged claims remain reusable, while unknown impact, new obligations, known failures and mandatory gates remain in the assurance account. Selection includes its own analysis and assessment cost. No fixed cadence, probability threshold, new runtime or per-test ledger is introduced.

Intent explains the purpose. Product, requirements, principles synthesis, capabilities and frame bindings consume the new owner. C3 criteria 4 and 5 are amended in their existing roles; there is no seventh criterion. Eleven member discriminators and two integrated checks cover the new obligations. The [work map](../../tickets/active/T-002-c3-successor-construction.md#assurance-work-and-proof) assigns seven additional duties to existing I5 owners while preserving all fourteen review-finding assignments. No tenant source is changed.

## Bounded Executable Evidence

[check_examples.py](20261016T000430Z_I5_ASSURANCE_ASSETS/check_examples.py) produces [results.json](20261016T000430Z_I5_ASSURANCE_ASSETS/results.json) with Python's standard library. From the repository root:

```sh
python3 specification_methodology/v3/.ai-workspace/comments/codex/20261016T000430Z_I5_ASSURANCE_ASSETS/check_examples.py
```

These are author-produced witnesses for the common specification. They neither assess a tenant nor execute the separately selected categorical steel thread.

| Witness | Observed result | Limit |
|---|---|---|
| A histogram implementation overwrites duplicate counts; its test checks only keys | Across 121 sequences of length 0–4 over {-1, 0, 1}, all weak checks pass, while the count predicate rejects 105 faulty outputs and accepts all 121 correct outputs. | Exhaustive only for these inputs and the two specified programs. The predicate's full-domain fidelity remains a separate argument. |
| Key-only observations alias correct and wrong counts | The same input and observed keys admit opposite count-obligation truth values. | One decisive counterexample to complete decision from this observation. |
| Local postcondition and final target are too weak or incompatible | An established nonnegative output does not establish either a strictly-greater-than-one next precondition or the selected final value. | A finite witness; no real workflow is qualified. |
| Two checks share an error cause | In the declared two-world model, joint miss is 1/2; multiplying marginals gives the unsupported 1/4. | An assumed model demonstrating correlation, not an operational estimate. |
| A histogram repair has a declared bounded dependency footprint | Histogram and integration are reassessed; the independently unaffected sum evidence is retained. Requirement, oracle, shared-runtime, unknown-impact and mandatory-gate variations expand selection as expected. Original failure evidence remains unchanged. | The toy dependency model and one repaired input only; no discovery of dependencies in arbitrary programs is claimed. |

## Mathematical Basis And Limits

The preservation account uses the distinction between preconditions, postconditions, composition and termination found in [Software Foundations' Hoare logic](https://softwarefoundations.cis.upenn.edu/plf-current/Hoare.html). This is support for the conditional reasoning, not a claim that all STDO realisations are programs in that formal system.

The risk account uses prior information and likelihoods to update a specified probability model, following the distinction described in [NIST's Bayesian reliability guidance](https://www.itl.nist.gov/div898/handbook/apr/section2/apr1a.htm). It imposes no quantitative reliability guarantee on uncalibrated actor work. The observation-fibre implication and conditional miss formula are explicit mathematical obligations with their premises stated in the requirement.

The a_c work remains a tenant implementation duty: represent the relationships, expose residual predicates and establish fidelity. Formulae in the common WHAT are not a verified proof system. Full-domain mathematical arguments, mechanical validation, finite examples, independent semantic assessment and actual use support different claims. An unproved universal claim need not stop lawful bounded work unless its governing gate requires it.

## Review And Work Standing

Two fresh same-family nonauthor working reviews have expectations fixed before successor acquisition: [mathematical assurance](20261016T000430Z_EXPECTATIONS_I5_ASSURANCE_MATH.md) and [contract propagation](20261016T000430Z_EXPECTATIONS_I5_ASSURANCE_CONTRACT.md). They receive an exact source freeze. Their reviews cannot supply cross-family acceptance or the owner's decision. The ticket records their results and the descendant input snapshot after readback.

C3-I5-03 retains its original subject and reviews. The new proposal is prepared for exact-source ratification. Existing I4 admissions, the previous principle bodies, installed builder and candidate trees remain unchanged. Native context and token spend are uninstrumented; the witnesses use no paid external actor calls. No improved-method performance claim follows from this source work.
