---
name: stdo-status
description: Produce an evidence-backed read-only STDO project status and bounded triage candidates. Use when a user says stdo status or explicitly asks for progress, blockers, monitoring, or triage help in an STDO-governed project. Do not invoke for generic status.
---

# STDO Status

Report Product and work truth without changing it. The shell command `stdo
status` reports installed-basis integrity; this skill reports project delivery
state from Product-owned authority and evidence.

## Select The Product Basis

Read and apply
[`PRODUCT_BASIS.md`](../../references/PRODUCT_BASIS.md) before reporting status.
Continue only from its exactly-one verified selection. This skill remains
read-only.

## Procedure

1. From the verified definition, read Goals, bound work lanes, selected outcome,
   exact checkpoint/workspace,
   accepted design, proof, and exact review results. Comments and dashboards
   are projections.
2. Compare with the user's baseline, last accepted checkpoint, or prior durable
   work state. Without one, report current state without inventing a delta.
3. Separate accepted Product movement, active construction, prerequisite
   readiness, preservation/regression evidence, rejected or superseded churn,
   blockers, uncertainty, drift, and next authorized action.
4. Findings may propose triage and a smallest re-entry point. Do not create
   tickets, reprioritize, mutate status, or apply disposition without separate
   authorization.
5. Keep technical triage separate from Product-owned priority and boundary
   effect. When the STDO engagement profile is adopted, this is the Reviewer to
   Executive separation. Use only Product-bound scales, cutoff, and hard stops.
   Never infer percentage completion from prose, commits, test counts, or
   review counts.

## Return

Lead with Product outcome and current boundary. Report basis health, completed
since the comparison point, current work/evidence, blockers/findings, proposed
triage or decisions, and one next already-authorized action. State stale,
missing, or unverified evidence. Keep adjacent observations from becoming
automatic release blockers.
