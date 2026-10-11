# First-month cost comparison: Harbor and Cove

This fictional service estimate totals **AUD 134.80 for Harbor** and **AUD 148.00 for Cove**. Each offering is below the owner's separate AUD 160.00 ceiling. Neither offering has been selected; the owner retains the deployment choice.

The estimate is for `cost-brief/source-v2`, R Source Revision 2 in `TASKS.md` at `e5ac730699afcd1fc6a1f610d2186c63ac328ca3`, lines 201–213, conserving the unchanged D/source-v1 clauses at lines 87–115. Its “first month” means exactly 30 days of continuous operation, 24 hours a day, with two nodes and 40 GB outbound traffic over that interval. The node count applies to each complete offering; the offerings are alternatives.

Tax, discounts, currency exchange and all charges other than the quoted compute, backup and outbound charges are excluded by this fixture. These exclusions describe the estimate's boundary, not a real vendor's prices.

## Stage 1: normalize the quote units

The source quotes compute and outbound rates in **AUD cents**. The cost calculator consumes **AUD dollars**. The translation is a unit conversion within AUD: one AUD dollar is 100 AUD cents. It changes no currency, quote revision or offering.

| Current source-v2 quote; unchanged clauses conserved from source-v1 | Normalized calculator input |
|---|---|
| Harbor: 8 AUD cents per node-hour | 0.08 AUD dollars per node-hour |
| Harbor: 4 AUD cents per GB | 0.04 AUD dollars per GB |
| Harbor: AUD 18 backup per interval | AUD 18 per 30-day interval |
| Cove: 10 AUD cents per node-hour | 0.10 AUD dollars per node-hour |
| Cove: 2.5 AUD cents per GB | 0.025 AUD dollars per GB |
| Cove: AUD 3 backup per interval | AUD 3 per 30-day interval |

For Harbor compute, the actual producer is:

```text
(source = cost-brief/source-v2,
 offering = Harbor,
 rate = 8,
 unit = AUD_cent / node_hour,
 quote_basis = TASKS.md@e5ac730699afcd1fc6a1f610d2186c63ac328ca3:201-213
 conserved_basis = TASKS.md@e5ac730699afcd1fc6a1f610d2186c63ac328ca3:87-115)
```

The normalized result retains those producer coordinates and adds:

```text
rate = 8 × (1 AUD_dollar / 100 AUD_cent)
     = 0.08 AUD_dollar / node_hour
translation = same-AUD cents-to-dollars, factor 1/100
```

This explicitly establishes the join with a dollar-rate consumer. Passing the raw numeric field `rate = 8` to that consumer would misinterpret the quote as AUD 8 per node-hour and produce AUD 11,520.00 of Harbor compute cost. Matching numeric field shapes cannot admit that interpretation. The permitted translation consumes the source's actual typed quote rather than silently relabelling it.

## Stage 2: calculate complete totals

The normalized rates feed a separate calculation stage:

```text
node-hours = 2 nodes × 30 days × 24 hours/day = 1,440 node-hours
compute = normalized AUD dollars/node-hour × 1,440 node-hours
outbound = normalized AUD dollars/GB × 40 GB
total per offering = compute + backup for the interval + outbound
```

The units cancel to AUD dollars. Backup is already a whole-interval amount and is added once per offering. The 40 GB source is a service-wide interval quantity; the source does not make it 40 GB per node.

| Offering | Compute | Backup | Outbound | First-month total | AUD 160 ceiling |
|---|---:|---:|---:|---:|---|
| Harbor | 0.08 × 1,440 = AUD 115.20 | AUD 18.00 | 0.04 × 40 = AUD 1.60 | **AUD 134.80** | Under by AUD 25.20 |
| Cove | 0.10 × 1,440 = AUD 144.00 | AUD 3.00 | 0.025 × 40 = AUD 1.00 | **AUD 148.00** | Under by AUD 12.00 |

## Stage 3: present the comparison

The calculation uses exact decimal rates and amounts, retaining Cove's 0.025 AUD dollars/GB without rounding it to 0.03. Presentation alone formats final money amounts to two decimal places; these totals require no rounding.

Harbor is AUD 13.20 lower for the included charges on this exact source and interval. This comparison establishes no service suitability, availability or real-market quote. It does not combine the offerings into a single cost.

The owner can use the documented totals and assumptions to make a separate choice. A correct calculation or a passing cost review does not authorize a purchase, account creation, contact, deployment, payment, network action or common-method edit.

## Revision and retained evidence

Only Harbor's compute quote changed, from 6 to 8 AUD cents per node-hour. Its compute cost rises by AUD 28.80 over the same 1,440 node-hours, and its total moves from the historical AUD 106.00 to the current AUD 134.80. Its ceiling margin and comparison with Cove therefore change. The Cove calculation, interval, outbound quantities, backup quotes, exclusions, cents-to-dollars conversion and reserved owner decision retain unchanged support. This dependency independence is not a claim of author-independent assessment.

The [original source-v1 B brief](../deployment/b/BRIEF.md), frozen at `457ba021b680251b4f9127e0f75b7652e4313792`, remains byte-identical with SHA256 `6a1c84882c8afd469c1b3b1e63a5f57c0229b5a1cfa5d5dbdd296ac7ca22fd56`. Its [reusable guide](../deployment/b/GUIDE.md) also remains byte-identical, SHA256 `34aabef599d7168132fda6b991117326653ba82aa347748de3c50fd5a213655a`. The guide's general unit, scope and owner-decision guidance remains useful. Its Harbor/source-v1 numerical example and original B-writer file grant remain historical; use the revised quote here and this occurrence's actual activation.

The available receipt record concerns only `cost-v1-receipt`, `cost-brief/source-v1`, and that original brief digest. It is preserved evidence for its original document and interval. It does not acknowledge this revised brief. Source-v2 receipt effects remain suspended without their exact owner grant, and all future writes for `cost-v1-receipt` are withdrawn. [Current state](CURRENT_STATE.md) preserves the receipt reconciliation, distinct token uncertainty and pending completion. This document is an authored candidate with local checks; required independent assessment and actual owner completion remain separate.
