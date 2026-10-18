# F_D Tooling Source-Owner Map

This is a read-only derivation reference for the additional deterministic tools.
It is not a method definition, installed release, adopted constitution or
implementation/qualification claim. STDO3.0 owns the method; a_c owns only the
tool behavior specified in [the operation family](fd-support-tools.md).

## Exact reference and basis roles

- Derivation commit: `494451522072ec34381c644f1ccfa2331f2b1e27`.
- Repository package: `specification_methodology/v3/build_tenants/common/`.
- Package tree: `082df4ea2b7b3658aab528bbfbcfe81234ccc810`.
- Status: common standalone V3 candidate, outside main at selection; not
  accepted, released or installed. A later verification-only checkpoint does
  not change this selected reference.
- a_c builder: the unchanged installed `stdo_a_c.json` basis,
  STDO v2.5.1-rc.2, manifest
  `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
- Consumer operation: the exact method/profile and Product authority selected
  by that consumer. A tool binding must explicitly support it. This provisional
  source reference is not silently substituted for the consumer's method.

All members below are relative to that package. Their SHA-256 values bind exact
UTF-8 member bytes in the selected Git object, without relying on the location
or mutable state of another worktree. Retrieve a deciding member from this
repository's object database, for example:

```sh
git show 494451522072ec34381c644f1ccfa2331f2b1e27:specification_methodology/v3/build_tenants/common/standards/ACTIVATION.md
```

No v3 release URI, remote/GitHub availability, Product composition, runtime
dependency on the candidate or regenerated frozen representation is asserted.
If the exact objects/bytes are unavailable, this derivation reference is
unresolved; a moving branch or similarly named member is not a replacement.

## Owning members and deciding clauses

The labels below route each requirement to its upstream owner. The clause names
and Markdown anchors name that exact member's sections; they do not copy the
rules into a_c or select the optional profile. Derived references retain the
owner's conditions, permissions, exclusions and limits.

### PDEF

Member: `standards/PRODUCT_DEFINITION.md`.
SHA-256: `9287fd7387fcab2bcebfaf7192a4616ce1117e77cd814af4f1ac0558a2a037a6`.
Deciding clauses: §4 (`4-shared-installed-release-basis-and-toolchain-manager`),
§8 (`8-what-how-and-work-carriers`), §11
(`11-one-constitutional-surface-and-version-boundary`) and §12 (`12-bootstrap`).
They own basis selection, source/derived authority, layout/tenant/carrier
bindings and the method/realization boundary.

### FOUND

Member: `standards/FOUNDATIONS.md`.
SHA-256: `8c8cf97691fc97fd9939bdbb07e2669435842a60a1d658e7121fb10f1d11c8a8`.
Deciding clauses: §4 `results`, `conjunction-of-results`,
`assertions-and-observation`, and `change-impact-and-evidence-reuse`.
They own result and predicate meaning, method-owned joins, assertion/observation
claims and supported change-impact/reuse. The tools implement only the declared
decidable portion of the caller-selected contracts.

### RF

Member: `standards/REFERENCE_FRAME.md`.
SHA-256: `8152838639950b09389f99181172792100e4470b4807b4e112870cd4e6f6ba21`.
Deciding clauses: §3 RF-005/006/012/013/014/016; §6
(`6-frames-in-conjunction`); §8 (`8-workspace-coverage`); §10
(`10-discovery-and-revision`); §11 (`11-the-activation-packet`).
These own exact frame binding, authority, reconstructability, capability,
coverage, revision and the packet. a_c does not restate a second packet schema
or define frame selection.

### ACT

Member: `standards/ACTIVATION.md`.
SHA-256: `22e39f1c5804c297eec2982e0b859438222b83b3439a810eed58d89b84bbb619`.
Deciding clauses: §1 `intake`, `admission`, `applicability` and
`roles-and-delegation`; §2 (`2-context-construction-under-an-envelope`),
including Acquisition, Standalone scope and `staleness-of-derived-surfaces`;
§3 (`3-step-results-and-disposition`), including `effects`;
§5 (`5-work-state-and-restart`); §6 (`6-cost-and-proportionality`), including
`resource-limits`; §7 (`7-closed-result-and-reuse`). These own activation,
context fit/acquisition, effects and recovery, work-state and resource/reuse
semantics. Tools expose corresponding checks and observations, not new states.

### EVAL

Member: `standards/EVALUATION.md`.
SHA-256: `3b30baee4f6941d35491e4ae0aa5e5a332f8b8afbae833dc3b4631da3426060e`.
Deciding clauses: §§1–6 (`1-claims`, `2-separation`,
`3-independent-assessment`, `4-review-results`, `5-acceptance`,
`when-a-finding-blocks-promotion`, `6-conformance-of-realisations`). These own
claim/evidence boundaries, independence/exposure, review results and owner
disposition. In particular review recommendations are not mechanically adopted
as dispositions. Source acquisition/diff/trace tools supply no semantic verdict.

### ASSURE

Member: `standards/ASSURANCE.md`.
SHA-256: `03e54928fa345897693bf7feaff64ba1aba3b06fd4a0a4304854b3ac26cdc349`.
Deciding clauses: §3 (`3-test-authority`); §10
(`10-testing-evidence-composition`); §§13–16
(`13-end-to-end-interface-integration-frame`, `14-design-to-module-evidence-route`,
`15-module-derived-unit-tests`, `16-module-lifecycle-confirmation`). They own
test authority, proof composition and interface/module qualification. The tools
preserve exact source/proof/effect evidence and claim boundaries for F_P actors.

### TICK

Member: `standards/TICKETS.md`.
SHA-256: `5f7e4cb0785a27b9e6dda1fd91044e775183b6a0e6e80b33811e54665b144b57`.
Deciding clauses: §5 (`5-from-carrier-to-execution`, `carrier-selection`,
`execution-contract-admission`) and §7 (`7-authority-judgment-closure-and-state`,
`recorded-judgment-and-owner-ruling-continuity`,
`condition-based-closure-and-reuse`,
`one-truth-state-projection-and-drift-refusal-up-009`). They own work-carrier
selection/authority and recorded judgment/ruling/closure/state. Tool projections
and Writer interfaces do not create a new work ledger or choose dispositions.

### EXEC

Member: `standards/EXECUTIVE_BASELINE.md`.
SHA-256: `fcef434630e270d216f494de97ee727ad46690db89a4b73edac4b88ff921c62e`.
Deciding clauses: §2 (`2-status-and-authority-boundary`); §6
(`6-executive-attention-evaluation-and-action`, `event-driven-attention`,
`no-mutation-while-executive`); §§8–10 (`8-derived-executive-frame`,
`9-derived-worker-frame`, `10-derived-reviewer-frame`); §17
(`17-actor-binding-and-independence`); §19
(`19-baseline-specific-basis-and-activation-additions`). This is an optional
profile. Its mappings and extra checks apply only when the consumer selects it;
file presence, the derivation reference and a role label do not adopt it.

### SPEC

Member: `standards/SPEC_METHOD.md`.
SHA-256: `5fe14955b40d1b9763b788d91aacd939799225be032811524be85fce44128c3d`.
Deciding clauses: §4 (`4-change-management`, `universal-intake-triage`,
`computed-classification-and-treatment`) and §8
(`8-bounded-execution-in-this-method`). They own triage/re-entry and consume
bounded execution. Impact/classification tools return supplied/computed facts;
they do not take over causal diagnosis, priority or authorized next-action choice.

### AC

Member: `standards/AXIOMATIC_CALCULUS.md`.
SHA-256: `fb56ac87f017abefd81416e28c5e2b6ef512caafa8c75c979cca4865af61cb87`.
Deciding clauses: §5 (`5-traversals-and-functor-kinds`,
`ac-015-functor-classification`, `ac-016-typed-composition`). `F_D[v]` evaluation
or proof, F_P interpretation/construction and named domain operations keep
their separate identities and evidence. This target reference does not replace
the exact installed calculus selected by a_c's Product Definition.

## Tool-to-owner trace

Every new requirement cites its deciding owners in its body. This index groups
those routes for review, without making a second method rule.

| Requirement | Tool obligation | Deciding source routes |
|---|---|---|
| REQ-AC-FD-001 | Public operation/contract discovery | PDEF §8/11; RF RF-016; ASSURE §13 |
| REQ-AC-FD-002 | Exact workspace/method observation | PDEF §4/12; RF RF-005; ACT §5/7 |
| REQ-AC-FD-003 | Record/source/grounding acquisition | ACT §2; PDEF §11; EVAL §1–3 |
| REQ-AC-FD-004 | Declared dependency/impact/coverage queries | FOUND Change impact and evidence reuse; RF §6/8/10; ACT Applicability; SPEC §4 |
| REQ-AC-FD-005 | Selected packet/context assembly and fit checks | RF §11/RF-013/014; ACT §2; selected EXEC §19 |
| REQ-AC-FD-006 | Product-bound contract preflight/admission evidence | ACT Admission; TICK §5 |
| REQ-AC-FD-007 | Granted dispatch, observations and notification | ACT §1/3/5; selected EXEC §6 |
| REQ-AC-FD-008 | Closed-return capture and binding checks | FOUND Results/Conjunction; RF RF-012; ACT §3/7; EVAL §4 |
| REQ-AC-FD-009 | Independent source/proof/review acquisition and comparisons | EVAL §1–4/6; ASSURE §3/10/13–16; selected EXEC §9/10/17/19 |
| REQ-AC-FD-010 | Declared F_D checks and supplied method operators | AC §5; FOUND Results/Conjunction/Assertions; EVAL §1/2; ASSURE §10 |
| REQ-AC-FD-011 | Existing work/evidence projections and authorized records | PDEF §8; TICK §7; ACT §5; EVAL §4; selected EXEC §6 |
| REQ-AC-FD-012 | Affected refresh, reuse checks and handoff | FOUND Change impact and evidence reuse; RF §10; ACT §5/7; TICK §7 |
| REQ-AC-FD-013 | Attempt/usage evidence and selected resource checks | ACT §6; EVAL §1; SPEC §8 |
| REQ-AC-FDV-001 | Actual ordinary tool/actor path qualification | EVAL §1/3/6; ASSURE §3/13–16 |
| REQ-AC-FDV-002 | Refusal, unknown and recovery cases | ACT Applicability/§2/3/5/7; FOUND Results/Conjunction; ASSURE §3/13 |
| REQ-AC-FDV-003 | Bounded accepted-result comparison | ACT §6; EVAL §1; FOUND Assertions/Change impact and evidence reuse |
