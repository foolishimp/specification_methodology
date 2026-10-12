# Fictional Service: First-Month Cost Brief

Harbor is estimated at **AUD 106.00** and Cove at **AUD 148.00** for the selected
30-day interval. Each complete offering is below the owner's AUD 160 ceiling.
Neither offering is selected. The owner retains the deployment decision.

This is a documentary estimate using the fictional fixture `cost-brief/source-v1`,
not a current vendor quotation. The work grant permits this brief, its accompanying
guide and the constructor return in this run directory. A cost judgment does not
authorize purchase, account access, contact, payment or deployment.

## Source And Calculation Basis

The deciding input is commit `e5ac730699afcd1fc6a1f610d2186c63ac328ca3`, repository
path `stdo_3/build_tenants/codex/qualification/T2_T6/TASKS.md`, sections
`D: Deployment Cost Brief And Its Review`, `D Source, Revision 1` and
`D Typed Join And Reusable-Guidance Draft`. Its selected D body is lines 80–144,
UTF8 SHA256 `ac077121522e2f3c616c6961fd1b7c07e4782489cb8a224b071ec3f088e9f837`.

| Item | Selected basis |
|---|---|
| Source identity | `cost-brief/source-v1` |
| Currency | AUD; 100 AUD cents = AUD 1 |
| Interval | First month defined here as 30 days, 24 hours per day |
| Service workload | Two nodes, continuously running for the complete interval |
| Outbound workload | 40 GB over that same complete interval |
| Backup basis | One quoted charge per offering for the complete interval |
| Ceiling | AUD 160 for each complete offering separately |
| Included charges | Compute, backup and outbound traffic |
| Excluded charges | Tax, discounts, currency conversion and all other charges |

The exclusions are assumptions of this bounded fixture; they make no claim about
a real vendor. Harbor and Cove are mutually exclusive complete alternatives.
Their costs are not added into one deployment estimate.

The selected HOW is direct line-item arithmetic in cents. All rate applications
and each complete offering's sum retain cents. Only the completed sums, ceiling
comparisons and presentation values are converted to AUD. This realization is
one allowed way to satisfy the source contract.

## Quote Identity And The Producer–Consumer Join

These are the actual source-v1 inputs used below; the quote identities include
the offering and charge, rather than only the numeric rate.

| Quote coordinate | Value and interpretation | Application basis |
|---|---|---|
| `cost-brief/source-v1::Harbor.compute` | 6 AUD cents per node-hour | All two-node running hours |
| `cost-brief/source-v1::Harbor.backup` | AUD 18 per interval | Once for this interval |
| `cost-brief/source-v1::Harbor.outbound` | 4 AUD cents per GB | This interval's 40 GB |
| `cost-brief/source-v1::Cove.compute` | 10 AUD cents per node-hour | All two-node running hours |
| `cost-brief/source-v1::Cove.backup` | AUD 3 per interval | Once for this interval |
| `cost-brief/source-v1::Cove.outbound` | 2.5 AUD cents per GB | This interval's 40 GB |

The Harbor producer's raw field `rate = 6` has the meaning
`6 AUD cents / (node × hour)`, with offering `Harbor` and basis
`cost-brief/source-v1`. The proposed consumer gives its identically shaped
`rate = 6` field the meaning `6 AUD / (node × hour)`. Shape checks can pass while
these meanings differ by a factor of 100. Direct composition is incompatible.

The actual calculation admits the producer as a typed cents rate, preserving
its offering and source identity, and uses that 6 in the Harbor compute line.
If the dollars consumer is used later, a supported unit adapter must produce
`6 × (1 AUD / 100 AUD cents) = 0.06 AUD per node-hour`, retaining the same
Harbor/source-v1 identity. It must not pass an unqualified 6 to that consumer.
The adapter changes representation units; it changes neither the quote nor the
offering. No unresolved rate interpretation is used in this estimate.

## Line-Item Calculation

The interval is `30 days × 24 hours/day = 720 hours`. The compute workload is
`2 nodes × 720 hours = 1,440 node-hours`. Outbound remains 40 GB; it is already
the complete interval quantity, so it receives no extra day or node multiplier.

| Offering | Included charge | Dimensional calculation | Amount in AUD cents |
|---|---|---|---:|
| Harbor | Compute | 1,440 node-hours × 6 AUD cents/node-hour | 8,640 |
| Harbor | Backup | AUD 18/interval × 1 interval × 100 AUD cents/AUD | 1,800 |
| Harbor | Outbound | 40 GB × 4 AUD cents/GB | 160 |
| **Harbor** | **Complete offering** | **8,640 + 1,800 + 160** | **10,600** |
| Cove | Compute | 1,440 node-hours × 10 AUD cents/node-hour | 14,400 |
| Cove | Backup | AUD 3/interval × 1 interval × 100 AUD cents/AUD | 300 |
| Cove | Outbound | 40 GB × 2.5 AUD cents/GB | 100 |
| **Cove** | **Complete offering** | **14,400 + 300 + 100** | **14,800** |

The fractional Cove outbound rate causes no rounding here:
`40 × 2.5 = 100` AUD cents exactly. Completed sums convert as
`10,600 / 100 = AUD 106.00` and `14,800 / 100 = AUD 148.00`.

| Complete offering | First-month total | Ceiling comparison | Remaining ceiling allowance |
|---|---:|---|---:|
| Harbor | AUD 106.00 | 10,600 cents ≤ 16,000 cents; below ceiling | AUD 54.00 |
| Cove | AUD 148.00 | 14,800 cents ≤ 16,000 cents; below ceiling | AUD 12.00 |

Cove's total exceeds Harbor's by `14,800 − 10,600 = 4,200` cents, or AUD 42.00.
That difference describes this fixture's quoted costs. It does not decide
service adequacy or choose an offering for the owner.

## Standing And Use

This constructor used the Codex documentary method at commit
`ea43ca8996f05f8d32e5ad6ab6f2327c39f773ab`, entering through
`stdo_3/build_tenants/codex/standards/README.md`. In particular, F-01/F-03 and
S-04 informed the scoped unit join; W-01/W-04 bound the document effects; E-05
preserved the decision boundary. Its builder is the separately verified
STDO 2.5.1 RC2 basis, manifest SHA256
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.

The accompanying [guide](GUIDE.md) retains this business outcome as an external
example. [RETURN.md](RETURN.md) records exact acquisitions and author checks.
Author arithmetic checks support the calculations only. Independent assessment,
owner acceptance and any deployment authorization remain separate and pending.
