# Readback: failure handling before another selected run

Frozen subject: `a3c43335e6d50bb7d6dd247c90de99e7404e1d1a`; I5 source `bc8662a90323d38166164afac03468942667cf7a`. Builder: the previously verified installed STDO 2.5.1 RC2 basis. Specification paths below are relative to `specification_methodology/v3/specification/`.

This is a separately requested narrow readback after `process-review.md` closed. The original report remains unchanged. The parent supplied the potential join, and this reviewer reacquired the exact owning clauses and assessed both restrictive and permissive interpretations. No other current reviews were read and no source, ticket, tenant or Git state was changed.

Result: `falsified` for the narrow predicate that the reassessment clause states an unambiguous next-run rule consistent with the universal construction owner's alternatives. One **Low material wording ambiguity** is supported. The full source supports diagnostic continuation and justified retry; it does not establish an unqualified rule that every failure must be repaired before any subsequent execution. The finding is the local sentence's competing reading, not a demonstrated tenant failure or a general claim that retry is forbidden.

## P-R1 — The closing reassessment sentence can turn repair into a prerequisite for diagnostic execution

Owning locus: `requirements/ASSURANCE.md:121`, final sentence:

> Failures feed causal diagnosis and repair before another selected run.

That sentence contains no qualification limiting the sequence to a diagnosed defect, an already selected repair, or a confirmation run. It can therefore be applied at the test-selection consumer as “perform diagnosis and repair before selecting another run.” The section covers uncertain influence, new assessment work and reassessment generally (`ASSURANCE.md:99-109,119-121`); its scope does not expressly exclude diagnostic reruns or transient failures.

The source also supports a different, coherent reading: failures inform the diagnosis and repair process before the next response is selected, but an actual repair occurs only when the diagnosis supports one. “Feed” does not explicitly require completed repair. Under this reading, a diagnostic run is part of acquisition or causal diagnosis, and an authorised retry can be the appropriate response without a source change.

The second reading is supported by the owning construction contract:

- `PRODUCT.md:76` says diagnosis determines whether to repair the realisation, acquire evidence or revise the governing model.
- `requirements/README.md:110` preserves unresolved causal alternatives and routes each **supported** repair to its owner, rather than inferring a repair from the intake label.
- `requirements/README.md:112` permits continued work whose supported purpose is reducing uncertainty or testing a bounded hypothesis, and lists continuation, repair, recovery, re-entry, yield and stop as applicable responses.
- `ASSURANCE.md:115` itself permits supported reassessment, as well as repair or an authorised obligation change, to dispose a recorded failure. It does not make repair the sole route.
- `ASSURANCE.md:47,66-68` requires diagnosis of unestablished or conflicting observations and shared errors. A reported test failure is not automatically established falsification of the source obligation or proof of which component needs correction.

These provisions prevent treating the last sentence as conclusive evidence of a universal repair gate. They do not make the local sentence unambiguous for a tenant implementing the next-run decision. The restrictive reading changes permitted work and can impose a sequence the universal owner does not otherwise require. Its apparent gate should be clarified at the owner rather than requiring each consumer to invent the exception.

## Discriminatory cases

**1. A genuine failure needs an observational diagnostic run.** A bounded test independently establishes that a delivered result and its checksum disagree. The failed predicate is soundly observed. The available evidence does not locate the cause: a nondeterministic implementation defect and corruption in the observation environment are both possible. An already authorised, read-only rerun on the same frozen candidate captures the relevant intermediate values and transport observations. It has no uncertain external effects, fits its resource limits and preserves the original failure. No implementation, requirement or checker repair is yet justified.

The universal construction rule permits acquiring the evidence needed to choose a supported repair. A literal repair-before-next-run implementation of line 121 refuses that diagnostic run until something is repaired, or pressures an unsupported change solely to unlock execution. The process reading admits the run as causal diagnosis. These are different decisions on the same facts and grant; neither involves accepting the failed candidate.

The same distinction applies where the initial check is only a reported failure and the oracle's fidelity is unresolved, but that weaker case is not necessary to establish the ambiguity.

**2. A transient failure needs no source repair.** A read-only integration check fails because its selected external service is temporarily unavailable. The original observation and bounded failed result remain recorded. A later authoritative observation establishes that the service has recovered; the work authority and risk policy permit one bounded retry on the unchanged candidate. No code, specification or oracle defect has been established, and no repair by the constructing actor is needed. The retry can acquire current evidence without rewriting the earlier failure or satisfying a still-unmet acceptance gate by fiat.

The process reading permits that supported continuation under `README.md:111-112` and the current-reality recovery rule. The restrictive reading demands an unspecified repair first. Calling every new observation or retry a “repair” would erase the distinction among acquisition, continuation, recovery and repair that the owner explicitly preserves.

## Impact, containment and owning correction

Severity is **Low**: this is a locally ambiguous instruction within a broader contract that supplies the supported alternatives. No tenant manifestation, actual denial of service, unjustified repair or failed qualification was examined. The concrete consequence, if the restrictive reading is encoded, is blocking useful diagnosis or justified retry, or prompting a speculative mutation. Confidence is high that the two readings are available; the text does not establish that a careful full-source consumer must choose the restrictive one.

Existing containment is to apply the full construction owner: preserve the failure, diagnose as far as the available evidence permits, and select only an authorised response with supported purpose, effect safety and assurance conditions. A fresh pass cannot erase the original observation or waive a mandatory gate. This containment supplies no new mutation or retry authority.

The smallest correction belongs to `requirements/ASSURANCE.md:121`: make repair conditional on the supported diagnosis and state that the next authorised response may be further observation, a bounded diagnostic run or justified retry, repair, recovery, re-entry or stop as the common construction owner already permits. The correction need not add a carrier, retry policy, new result value or new criterion. It should remove the apparent unconditional repair-before-execution ordering while retaining causal treatment of failures and the prohibition on erasing them through repeated runs.

Affected consumers are the Spec Method's testing/triage/recovery bindings (`PRODUCT.md:80,363`), selected reassessment and failure-control rules (`requirements/README.md:110-118`), acquired assurance frames (`REFERENCE_FRAME_BASIS.md:51`), and the member/integrated checks for diagnosis and affected reruns (`conformance/README.md:76,80-82,98-101,115-117`; criteria 4 and 5 at `PRODUCT.md:419-420`). Their required distinction is already substantially stated. A bounded source clarification and changed-clause readback, plus assessment of any tenant that actually adopted the restrictive rule, is proportionate; a common wording correction alone is no evidence that a tenant needed or received repair.

This supplement narrows the prior report's no-finding conclusion only for this clause and its next-run consumer. Its other closed traces and evidence limits remain on their original subjects. Priority, ratification and any authorised source change remain the parent's/owner's decisions.
