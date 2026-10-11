# Operator Note: First-Month Offering Comparison

This documentary estimate uses the fictional `cost-brief/source-v1` fixture. Harbor totals **AUD 106.00** and Cove totals **AUD 148.00** for the selected interval. Each separately falls within the owner's AUD 160 ceiling. Neither offering is selected; the business owner retains the offering and deployment decisions.

The input is [D Source, Revision 1](../../../TASKS.md#d-source-revision-1) at repository commit `e5ac730699afcd1fc6a1f610d2186c63ac328ca3`. TASKS SHA256 is `a97e1308b02b2bee9037f30b16b3826917feb8cb9f63bda4b0ff9467c380409a`; the selected D/source-v1 section SHA256 is `62060a20714fde7f65e1a7d746daa78cd7034c4f4a40a1b2b630734a59f0176b`. The bounded fixture supplies these quotes; they are not real vendor prices.

## Recompute The Interval And Units

Currency is AUD, with 100 cents per dollar. Two nodes run continuously for 30 days at 24 hours per day: `30 × 24 = 720 hours per node`, giving `2 × 720 = 1,440 node-hours`. Outbound traffic is 40 GB for the whole interval. Each backup quote applies once to that whole interval.

Harbor quotes 6 cents per node-hour, AUD 18 backup per interval and 4 cents per outbound GB. Cove quotes 10 cents per node-hour, AUD 3 backup per interval and 2.5 cents per outbound GB. Divide each cents quote by 100 before multiplying by node-hours or GB. Each total is `compute + backup + outbound`; the mutually exclusive offerings remain separate.

| Offering | Compute AUD/node-hour | Compute AUD | Backup AUD/interval | Outbound AUD/GB | Outbound AUD | Total AUD | Comparison with AUD 160 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Harbor | 0.06 | 86.40 | 18.00 | 0.04 | 1.60 | 106.00 | 54.00 below |
| Cove | 0.10 | 144.00 | 3.00 | 0.025 | 1.00 | 148.00 | 12.00 below |

Harbor: `1,440 × 0.06 + 18 + 40 × 0.04 = 106.00`. Cove: `1,440 × 0.10 + 3 + 40 × 0.025 = 148.00`. These ceiling comparisons concern only each complete offering under the selected inputs and exclusions.

The actual Harbor producer field `rate = 6` means **AUD cents per node-hour** on Harbor/source-v1. A consumer expecting AUD dollars per node-hour can use it after a supported translation: `6 / 100 = 0.06 AUD/node-hour`, retaining Harbor and source-v1. Passing the numeric value 6 directly across that boundary changes its meaning. A matching numeric field shape is insufficient; an unresolved unit or source binding withholds the affected calculation.

## Assumptions And Their Owners

The explicit exclusion assumption is to ignore tax, discounts, currency conversion and other charges because D/source-v1 excludes them. It is part of this bounded source contract. A changed exclusion belongs to the source/fixture responsibility identified in the original Source And Activation Binding, routed through the parent/root for an authorized source-owner decision and successor revision. This worker cannot silently change it. The source identifies a Source/fixture Writer and its delegated territory, but does not name an individual business assumption owner; that individual identity remains unresolved.

The business owner separately owns the AUD 160 ceiling and eventual offering/deployment choice. A changed quote, interval, node count, traffic quantity, backup period, exclusion or ceiling reopens the affected estimate and comparison on a newly bound source. Retain this note as the source-v1 calculation; do not relabel it as evidence for changed inputs.

## Admitted Action And Stops

Under this reader's explicit grant, the first admitted documentary effect is saving this comparison as `stdo_3/build_tenants/codex/qualification/T2_T6/runs/reader/repaired/OPERATOR_NOTE.md`; `RETURN.md` closes its construction record. A later analyst must recover its own current outcome, source revision, output territory and grant before writing. The [selected entry](ENTRY.md) and [index](INDEX.md) route to [Work W-01](../../../../../standards/WORK_METHOD.md#w-01-bind-the-selected-work) and [Evidence E-05](../../../../../standards/EVIDENCE_METHOD.md#e-05-evidence-does-not-grant-authority); those owners retain meaning and authority. Their frozen method basis is `ea43ca8996f05f8d32e5ad6ab6f2327c39f773ab`.

Stop the affected action when a deciding source, interpretation, owner or grant is missing, changed, contradictory or outside scope. Return that unresolved relation to its owner. Stop before cloud access, network contact, payment, purchase, deployment, common-source mutation or owner acceptance: none is granted here. Any later cost review supports its exact cost predicate and source; separate operation and owner grants still have to be recovered.

Current residuals are the unnamed individual assumption owner, the owner's future offering/deployment decision and authority for additional effects. This note records authored documentary work and arithmetic. Independent assessment and owner acceptance remain outside this construction return.
