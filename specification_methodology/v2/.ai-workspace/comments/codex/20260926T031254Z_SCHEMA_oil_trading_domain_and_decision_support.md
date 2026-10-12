# SCHEMA: Oil trading strategies, valuation, P&L, and decision support

**Author**: codex
**Date**: 2026-09-26T03:12:54Z
**Updated**: 2026-09-26T03:25:36Z
**Addresses**: [Trading model families, strategy, and epistemic risk](20260926T023304Z_STRATEGY_ontology_calculus_epistemic_risk.md)
**Status**: Open
**Scope**: Pure systems analysis of physical crude and refined products with financial hedges; illustrative USD reporting base; separate market and governance overlays
**Research basis**: Primary market and contract sources checked on 2026-09-26. Numerical examples are synthetic.

## Summary

An oil-trading system manages contractual rights, obligations, physical flows,
cash flows, and financial exposures across products, grades, locations, and
time. Its strategy layer explains why an action could improve a declared
objective. Its valuation and P&L models measure the economics. Its epistemic
model qualifies the evidence and assumptions. Its risk calculus evaluates
the portfolio and proposed action. Its decision function compares candidates
against a declared objective and supplied constraints.

The proposed relationship is:

```text
Objective + market evidence + existing book
  -> strategy thesis and candidate action packages
  -> valuation, projected P&L, and portfolio risk
  -> recommendation with conditions and expiry
  -> action selection and execution
  -> fills, physical performance, cash flows, and reconciliation
  -> measured P&L, forecast evaluation, and revised beliefs
```

This is an applied definition for discussion, not an adopted STDO standard or
an operational recommendation. The first scope covers crude oil, gasoline,
diesel/gasoil, jet fuel, naphtha, and fuel oil; broader feedstocks and other
energy commodities require their own contract and quality bindings.

### Core system and overlay boundary

The core defines oil-domain meaning and dynamics: quantities, grades, flows,
obligations, prices, evidence, beliefs, strategies, valuation, P&L, risk, and
action consequences. Its analysis does not select a regulatory regime,
corporate governance structure, approval process, or human-versus-machine
decision arrangement.

| Layer | Separate responsibility |
|---|---|
| Domain core | Represent the economic and physical system, infer states, calculate outcomes and risk, and compare candidate actions. |
| Market/product profile | Supply the selected benchmark, contract specification, units, pricing calendar, settlement mechanics, and market conventions. |
| Governance overlays | Apply the relevant jurisdictions, regulatory regimes, venue eligibility rules, corporate policies, risk appetite, permissions, and approval arrangements. |
| Reporting overlay | Select statutory or corporate recognition, presentation, allocation, and reporting conventions over explicit economic results. |

The core accepts typed inputs and publishes typed results. A market profile
instantiates domain semantics; a governance overlay evaluates the subject under
its own applicable rules. The same core analysis can be assessed under several
overlays, whose individual outcomes and conflicts remain explicit. An overlay
may select a model or constrain an action while preserving the recorded facts
and identifying the basis of every derived result.

Storage availability, quantity conservation, cash requirements and contractual
payoffs remain analytical inputs and constraints. Corporate exposure ceilings,
permission to trade, and approval chains belong to their external overlays.
No particular governance configuration is a prerequisite for defining or
testing the core.

## Analysis

### Oil as a composition of reusable models

This is one specialization of the generic framework's
[underlying families and instrument composition](20260926T023304Z_STRATEGY_ontology_calculus_epistemic_risk.md#underlying-model-families-and-instrument-composition).
Oil combines stock and flow, storage, transport, transformation, financing,
and contingent cash-flow models. An oil strategy binds the capabilities of
the selected subject and instrument.

The same storage and carry structure can apply to grain or industrial metals
with different quality, loss, funding and delivery parameters. FX binds a
currency-funding model. An oil-company equity binds a business and ownership
model. An oil option combines the selected oil reference with its contractual
payoff and exercise model. These applications share analytical interfaces
while preserving their different economic meanings.

The oil model exposes inventories, grades, locations, curves, costs, capacity,
yields and uncertainty. A strategy chooses among supported actions to optimize
an explicit objective. External prices and other uncertain drivers remain
inputs to that choice. Governance remains a separate overlay.

### Market identity and ontology

The economic identity of an oil exposure is:

```text
product/grade + quality specification + location + delivery window
  + pricing basis + quantity/unit + contractual rights and obligations
```

Global prices connect through production, consumption, inventories, refinery
capacity, transport, and finance. Inventory information can be delayed or
incomplete, and route constraints can change the cost and feasibility of
moving oil. These are direct inputs to the epistemic and risk models.
[EIA inventories](https://www.eia.gov/finance/markets/crudeoil/balance.php),
[EIA transport chokepoints](https://www.eia.gov/international/content/analysis/special_topics/World_Oil_Transit_Chokepoints/).

Crude quality and refinery configuration affect processing and product yields.
The domain therefore represents assays, specifications, and transformation
constraints explicitly.
[EIA refining inputs and outputs](https://www.eia.gov/energyexplained/oil-and-petroleum-products/refining-crude-oil-inputs-and-outputs.php).

| Entity family | Required distinctions |
|---|---|
| Physical commodity | Grade/product, specification version, assay, quantity basis, lot identity, inspection and quality evidence. |
| Physical network | Location, tank, terminal, refinery, vessel/pipeline, route, capacity, reservation, throughput, and availability window. |
| Commercial obligation | Party, agreement, deal, delivery obligation, payment obligation, optional rights, and dispute status. |
| Performance | Order, fill, nomination, movement, inspection, title transfer, invoice, payment, correction, and settlement. |
| Market information | Executable bid/offer, trade, assessment, fixing, settlement price, curve, volatility surface, and source methodology. |
| Strategy | Objective, thesis, evidence, forecast horizon, candidate package, entry/exit conditions, and invalidation. |
| Knowledge | Claim, source, observation time, receipt time, revision, assumption, conflict, and model coverage. |
| Decision and outcome | Book, valuation basis, P&L result, risk result, objective, supplied constraint, recommendation, and execution instruction. |

Contract commitment, order execution, physical movement, title transfer, and
payment are separate events. A transport observation alone does not establish
every commercial fact about the cargo.

The following example market profiles preserve these material distinctions:

| Reference | Binding carried by the model |
|---|---|
| NYMEX WTI `CL` | 1,000 US barrels per contract; physical Cushing delivery under the applicable quality and delivery rules. [CME rulebook](https://www.cmegroup.com/rulebook/NYMEX/2/200.pdf). |
| ICE Brent `B` | 1,000 barrels; EFP-based delivery with an option to cash settle against the ICE Brent Index. [ICE specification](https://www.ice.com/products/219). |
| Platts Dated Brent | A physical assessment with its own delivery and assessment methodology, including eligible WTI Midland alongside North Sea grades. [Platts description](https://www.spglobal.com/energy/en/pricing-benchmarks/assessments/crude-oil/dated-brent-price-explained). |
| Platts Dubai/Oman | Distinct physical assessment families, with their own loading windows and alternative-delivery rules, relevant to Middle East and Asian crude pricing. [Platts description](https://www.spglobal.com/energy/en/pricing-benchmarks/assessments/crude-oil/dubai-crude-oil-price-explained). |
| NYMEX RBOB/ULSD | 42,000 US gallons per standard contract, equivalent to 1,000 barrels; quoted per gallon. [CME product comparison](https://www.cmegroup.com/articles/2024/trading-crack-spreads.html). |
| ICE low-sulphur gasoil | 100 metric tonnes per lot with a specified volumetric delivery convention. [ICE specification](https://www.ice.com/products/34361119). |

Every profile binding retains the exact index, contract month, specification
version, calendar, and source. Dated Brent and a Brent futures month have
different identities. Mass-to-volume conversions require the relevant density,
reference conditions, or contractual conversion factor.

### 1. Strategies: define the reason to act

The following is a candidate strategy catalogue. Availability in the catalogue
does not establish a profitable opportunity.

| Strategy family | Thesis and candidate actions | Evidence and invalidation |
|---|---|---|
| Directional fundamentals | A specified supply/demand change will alter value over a stated horizon; take or reduce outright exposure. | Production, consumption, inventories, outages, spare capacity and demand indicators; invalidate when the mechanism fails or the change is already reflected in price. |
| Calendar and storage | Relative prices across delivery periods justify a calendar position or feasible purchase-storage-sale package. | Forward spread, capacity, losses, financing and throughput; invalidate when full carry or delivery constraints remove the advantage. |
| Geographic netback | Destination proceeds exceed origin acquisition and the complete cost of transport and delivery. | Executable prices, freight, transit time, capacity and quality adjustments; invalidate on adverse cost changes or unavailable logistics. |
| Grade and benchmark relative value | A specified differential will change, such as a local crude price relative to a selected Brent month. | Grade balances, refinery demand, substitutability and transport; invalidate on structural basis change or failed correlation assumptions. |
| Blending and crude selection | A feasible blend or feedstock mix produces a required specification or refinery outcome at better economics. | Assays, compatibility, yields and operating constraints; invalidate on failed quality or conversion assumptions. |
| Refining margin | Product values change relative to feedstock and conversion costs; trade cracks or hedge a refinery book. | Product balances, refinery runs, outages and actual yields; invalidate when the proxy diverges from the physical economics. |
| Volatility and events | An option package provides attractive exposure relative to a defensible distribution of outcomes or protection objective. | Volatility, skew, event scenarios, liquidity and hedge feasibility; invalidate when the distribution or execution assumptions fail. |
| Statistical or trend signals | A documented predictive relationship has prospective value after costs. | Point-in-time validation, stability, turnover and capacity; invalidate on decay, regime change or failed out-of-sample performance. |
| Commercial hedging | A package improves the risk or budget outcome of an existing supply, inventory, refining or consumption exposure. | Underlying exposure and hedge effectiveness; invalidate when the exposure changes or basis risk outweighs the benefit. |

A strategy record contains `objective`, `thesis`, `causal_or_predictive_basis`,
`evidence_refs`, `horizon`, `forecast_model`, `candidate_deal_families`,
`entry_conditions`, `exit_conditions`, `invalidation_conditions`, `cost_model`,
and `evaluation_history`. A commercial hedge is judged against the combined
book and its commercial objective, including cases where the hedge itself loses money.

### 2. Deal types: define the rights and obligations

| Deal family | Required economics and performance |
|---|---|
| Physical spot purchase/sale | Identified commodity, quantity/tolerance, delivery point/window, price formula, quality acceptance, payment and performance terms. |
| Physical term supply/offtake | Repeated delivery obligations, nomination rights, quantity flexibility, pricing schedules, and termination/substitution provisions. |
| Fixed-price physical forward | Future physical delivery against an agreed price, with credit and operational obligations. |
| Listed futures | Exact exchange product/month, signed lots, multiplier, execution price, daily settlement, expiry and delivery/settlement terms. |
| Fixed-for-floating swap | Quantity, fixed price, floating index, fixing weights/calendar, payment date, and collateral/credit terms. |
| Differential or spread swap | Two precisely identified price references, quantity/conversion ratios, averaging windows and settlement formula. |
| Options | Underlying, quantity, strike, premium, exercise style, expiry, averaging if any, settlement, and collateral conventions. |
| Storage, transport, processing rights | Capacity and availability, fees, operating constraints, optional rights, performance obligations and penalties. |

A calendar spread, crack, or geographic package can combine several deals.
The package preserves its constituent obligations and execution dependencies.
Economic offset does not extinguish a contract or guarantee simultaneous fills.

Every deal also binds parties, agreement identity, currencies, fees, settlement
accounts, amendments, and contract version. Physical extensions include title
and risk-transfer clauses, delivery responsibilities, inspection, loss
allowances, freight, demurrage, and destination or substitution rights. The
contract identifies the applicable shipping terms and their named location;
those terms allocate responsibilities under their stated rules.
[ICC Incoterms overview](https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/).

### Algebra and trade calculus

Use typed quantities and prices:

```text
Quantity<Unit, MeasurementBasis>
Price<Currency/Unit, Product, Location, DeliveryPeriod, PricingWindow>
Cashflow<Currency, PaymentDate, ObligationId>
MarketObservation<Source, EventTime, ReceivedTime, Revision, QuoteKind>
```

The initial algebra has these operators and laws:

| Operator | Meaning and constraint |
|---|---|
| `book ⊕ deal` | Compose distinct obligations. Identity-preserving composition is associative; replaying the same recorded event cannot duplicate an obligation. |
| `scale(package, q)` | Resize within lot increments, tolerances and capacity. Costs and optionality are revalued where they are nonlinear. |
| `convert(quantity, basis)` | Convert compatible units with the explicit measurement or contractual basis. |
| `netExposure(book, bucket)` | Derive economic exposure for an exact risk bucket; preserve gross contracts and counterparty obligations. |
| `project(history, cutoff)` | Reconstruct positions, obligations, inventory and cash from recorded events as known at the selected cutoff. |
| `value(subject, market, basis)` | Produce a value and its evidence, or an explicit missing-input/unsupported/conflicted result. |

Quantity times a compatible price produces money. Cash flows aggregate only
under a declared currency and time basis. Opposing quantities at different
locations, grades or pricing windows retain basis exposure. Refining and
blending use declared transformation models; equal input and output barrel
counts are not a conservation law. Physical accounting reconciles the relevant
mass, components, reference conditions, and declared losses.

The trade calculus defines allowed transitions and their evidence:

```text
proposed -> selected -> instructed -> accepted/part-filled/filled/cancelled
contracted physical obligation -> nominated -> delivered/short/disputed
determined price and quantity -> invoice -> payment -> reconciled closure
```

These are linked lifecycles, not one universal state sequence. Governance
overlays can attach authorization conditions at their applicable boundaries.
The core lifecycle does not prescribe those conditions. A correction
references the affected event and preserves the prior record. A cancellation
request leaves outstanding execution possibilities until sufficient evidence
establishes its effect. The contract remains the owner of physical delivery,
pricing and payment consequences.

### 3. Valuation: define the required rates and curves

Here, rates are typed valuation inputs. Each carries source, units, timestamps,
availability, executable size where relevant, methodology, and uncertainty.

| Input surface | Required content and use |
|---|---|
| Commodity curves | Benchmark/product, hub, contract or forward period, bid/offer/mark and fixing calendar. |
| Differential curves | Grade, location, calendar, quality and product basis; preserve their exact reference definitions. |
| Historical fixings | Published index values and revisions for determined portions of pricing windows. |
| Logistics and conversion | Freight, storage, handling, insurance, losses, demurrage, processing costs and yields. |
| Funding and discounting | Currency, tenor, day count, compounding, collateral terms, funding spread and payment schedule. |
| FX | Spot and forwards appropriate to the currency exposure and payment dates. |
| Optionality and dependence | Volatility by expiry/strike, skew, correlations and alternative dependence models. |
| Execution and credit | Bid/offer, fees, impact, liquidity, counterparty exposure and any separately identified valuation adjustments. |

SOFR is one USD reference-rate input; a desk's funding cost and a complete
discount curve require their own construction and contractual basis.
[New York Fed reference rates](https://www.newyorkfed.org/markets/reference-rates).

Valuation preserves three separate meanings:

- **Market-consistent mark:** value using the selected market inputs and
  contract-appropriate pricing model.
- **Executable economics:** proceeds/cost at relevant size, including spread,
  impact, operational feasibility and applicable expenses.
- **Strategy forecast:** a predictive distribution of future outcomes under
  the strategy's evidence and assumptions.

A market forward curve does not, by itself, select the strategy's predictive
probabilities. Where a pricing measure is needed, it is identified separately
from the predictive measure used for expected strategy profit.

For a quantity `q` whose physical price is a weighted index average plus a
contractual differential `d`:

```text
contractPrice = sum_i(w_i * indexFixing_i) + d       where sum_i(w_i) = 1
invoice      = acceptedQuantity * contractPrice + contractualCharges
```

For a single-currency swap receiving that floating average and paying fixed
`K`, with fixed `q` and deterministic discounting:

```text
average_t = sum_fixed(w_i * observedFixing_i)
          + sum_unfixed(w_i * pricingModelForwardFixing_t(i))
swapValue_t = q * DF(t, paymentDate) * (average_t - K)
```

The fixing projection respects the actual index and its averaging convention.
Futures-to-forward or other model adjustments are explicit where material.
[ICE swap cashflow structure](https://idd.ice.com/CM/CMHelp/Content/FM/Swap.htm).

For deterministic cash flows in one currency:

```text
PV_t = sum_j(DF(t, paymentDate_j) * signedCashflow_j)
```

Multi-currency and contingent cash flows use a consistent FX, collateral and
pricing model. Physical valuation includes outstanding delivery rights and
obligations as well as owned inventory; it avoids counting the same barrels
both as inventory and as an additional unperformed acquisition.

A screening measure for storage carry is future sale proceeds less acquisition,
storage, finance, losses and delivery costs, evaluated at consistent dates.
A geographic netback deducts all destination and transport costs before
comparison with origin acquisition. Optional timing or destination rights
require valuation of their feasible choices.

For USD/gallon product prices and USD/barrel crude, a 3:2:1 crack proxy is:

```text
crack_321_per_crude_bbl = (2 * 42 * RBOB + 42 * ULSD - 3 * WTI) / 3
```

This is a gross price-spread proxy. A physical refinery calculation uses its
own yields and operating costs.
[CME crack construction](https://www.cmegroup.com/articles/2024/trading-crack-spreads.html).

Option valuation binds payoff, exercise and averaging rules, curves,
volatility and dependence assumptions. The input and model domains support
negative prices where the instrument permits them. CME's 2020 energy-option
notice illustrates why this matters; the model used today is bound separately
for each selected contract.
[CME negative-price notice](https://www.cmegroup.com/notices/clearing/2020/04/Chadv20-152.html).

### 4. P&L: define the outcome and its reconciliation

The primary control identity is economic P&L in reporting currency:

```text
economicPnL(t0,t1) = NAV(t1) - NAV(t0) - netExternalCapitalContributions(t0,t1)
```

`NAV` consistently includes cash, collateral assets, inventory, receivables,
payables, financing liabilities and remaining contract values. Capital flows
use the declared FX treatment. Expenses and funding interest enter once.
Internal transfers between cash and collateral do not create profit or loss.

Realized/unrealized classification follows an explicit reporting convention and
reconciles to the economic total through a declared bridge. Statutory and
corporate reporting are separate overlays; inventory accounting has its own
recognition and measurement rules.
[IAS 2 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/).

Futures settlement needs its own cash treatment. For an existing signed
position of `n` contracts with multiplier `m`:

```text
variationMargin_d = n * m * (settlement_d - settlement_previous)
```

New fills use their trade-to-settlement difference. Daily settlement cash and
the remaining derivative value are reconciled so an inception-to-date gain is
not counted again after it has settled. Initial margin remains collateral;
its funding costs and fees have separate P&L effects.
[CME cash calculations](https://www.cmegroup.com/education/articles-and-reports/money-calculations-for-futures-and-options).

The reporting views are:

| View | Question |
|---|---|
| Realized and unrealized | How does the selected reporting overlay classify the result? |
| Economic total | What changed in net economic wealth over the interval? |
| Projected/scenario | What could the existing book and proposed actions earn or lose over the stated horizon? |
| Attribution | How much relates to benchmark, basis, FX, carry, optionality, new trades, costs, and model/data revisions? |
| Reconciliation | What remains unexplained or disputed? |

Attribution declares its ordering and treatment of interactions. Components
plus the explicit residual equal total P&L. Every result retains valuation
time, evidence cutoff, market snapshot, model version, accounting basis and
source events. A corrected historical view and the view available to the
original decision remain separately reproducible.

### Epistemology and risk calculus

Represent three sources of uncertainty:

1. **Current state:** quantities filled, cargo quality, inventory, available
   capacity, delivery status and unsettled claims.
2. **Future evolution:** prices, basis, freight, demand, outages and liquidity
   conditional on the current state.
3. **Model adequacy:** uncertain parameters, changing relationships, alternative
   mechanisms and unrepresented failure modes.

An epistemic state contains admissible evidence, supported possibilities,
probabilistic beliefs where justified, assumptions, conflicts and coverage
limits. Observations retain event time and receipt time. Reports derived from
the same underlying source retain that dependency.

Bayesian updates apply a declared transition and observation model. Dynamic
epistemic rules govern what a source establishes and what remains possible.
A high-probability shipment or fill does not become a confirmed operational
fact. Missing or contradictory evidence can trigger reconciliation, wider
bounds, model review or a restricted recommendation. EIA's incomplete global
inventory coverage is a concrete example of why this distinction matters.
[EIA inventory evidence](https://www.eia.gov/finance/markets/crudeoil/balance.php).

For book `B`, proposed package `a`, uncertain current state `x`, future path
`omega`, and horizon `h`, define:

```text
outcome(B, a, x, omega, h) = change in economic wealth including all costs
marginalOutcome(a) = outcome(B, a, ...) - outcome(B, noAction, ...)
loss(B, a, ...) = -outcome(B, a, ...)
```

The forecast objective evaluates the marginal outcome or another explicit
commercial utility. Risk is calculated for the combined book, including every
material partially executed or unresolved-order state. Comparison against a
corporate or regulatory limit belongs to the applicable overlay.

A candidate risk result contains:

- sensitivities and concentrations by grade, location, benchmark and tenor;
- loss distribution and expected shortfall at the selected level and horizon;
- named stress losses, including basis breaks, negative prices, route failure,
  stale marks, quality failure and adverse execution;
- peak cash funding and margin needs along the path;
- counterparty, settlement, inventory, transport and capacity exposure;
- evidence limitations, alternative-model results and unresolved assessments.

For example, expected shortfall can be defined as
`ES_alpha(L) = (1 / (1-alpha)) * integral_alpha^1 VaR_u(L) du`.
Its result retains the selected predictive model and horizon. Portfolio risk
uses joint scenarios; summing standalone leg VaRs is insufficient.

Where plausible models form a set `M`, the core can calculate the worst
assessed risk across `M`. An overlay can compare that result with its selected
tolerance. Low-quality evidence is not converted into an invented probability
merely to produce a score. Delivery feasibility, counterparty exposure and
funding requirements remain core analytical results. Trading eligibility and
institutional credit or exposure ceilings are separate overlay predicates.

### Worked trade: physical crude with a Brent hedge

All prices, probabilities, costs, thresholds and outcomes below are invented to
demonstrate the model. Assume an isolated USD book, unchanged quality and quantity, available
storage and resale capacity, and closure of the selected futures month before
its expiry. Costs scale linearly only for this example.

**Thesis:** a particular local crude differential to the selected Brent month
will strengthen over 30 days. The package buys physical crude and sells Brent
futures to reduce broad benchmark exposure while retaining that basis view.

Initial candidate:

- Buy 100,000 barrels at $81/barrel.
- Sell 100 ICE Brent futures at $80/barrel, with 1,000 barrels per contract.
- Allow $60,000 total storage, finance, insurance, execution and other costs.

Define `basis_t = physicalPrice_t - selectedBrentFuturesPrice_t`. With the same
quantity on both legs, unchanged quantity and closed positions:

```text
netPnL = q * [(physicalPrice_1 - physicalPrice_0)
            - (futuresPrice_1 - futuresPrice_0)] - costs
       = q * (basis_1 - basis_0) - costs
```

The initial basis is $1/barrel. The toy predictive model gives:

| Terminal basis | Synthetic probability | Net P&L at 100,000 barrels |
|---|---:|---:|
| $3/barrel | 60% | $140,000 |
| $1/barrel | 30% | -$60,000 |
| -$1/barrel | 10% | -$260,000 |

The core calculates expected net P&L of $40,000 and an adverse-scenario loss of
$260,000. A path in which Brent rallies $10/barrel requires $1,000,000 of
variation margin on the short hedge. These results exist independently of any
governance regime.

For a parameterized decision experiment, supply an illustrative $150,000 loss
tolerance and $750,000 available margin reserve after physical financing and
initial margin have been provided. The candidate exceeds both supplied bounds.
The loss tolerance is an external policy choice; the available cash is a
resource-state input. Neither number is a universal oil-trading rule.

At 50,000 barrels and 50 futures, the same toy assumptions give expected net
P&L of $20,000, adverse-scenario loss of $130,000, and stressed variation margin
of $500,000. The smaller package fits those two supplied bounds. Its analytical
recommendation retains its evidence, thesis, physical and execution conditions,
resource assumptions and validity window. Applicable governance overlays
evaluate permission and approval separately.

For an assumed closing outcome of physical $77 and Brent $74, the smaller
package produces:

| Component | Calculation | P&L |
|---|---|---:|
| Physical | 50,000 * (77 - 81) | -$200,000 |
| Futures | 50,000 * (80 - 74) | $300,000 |
| Costs | Declared total | -$30,000 |
| Total | Sum | **$70,000** |

This is the $3 terminal-basis scenario. It becomes an observed result only
when the assumed trades and costs actually occur and are reconciled. Failure
to fill either leg changes the risk state immediately. The initial sale of
100 futures is a proposed hedge, not an assumption that execution succeeded.

### Decision-support and action loop

The model exposes these semantic functions; it does not prescribe a particular
runtime or orchestration topology:

| Function | Output and decision condition |
|---|---|
| Observe and reconcile | Evidence with provenance and an explicit set of unresolved current states. |
| Form or revise thesis | Strategy proposition, supporting/contrary evidence, horizon and invalidation conditions. |
| Generate candidates | Typed deal packages, including no action, evidence gathering, hedge reduction and alternative instruments. |
| Value | Market marks, executable costs and predictive outcomes with their separate bases. |
| Assess risk | Joint portfolio/path results, resource and feasibility checks, and unresolved assessments. |
| Rank and recommend | Objective-based comparison using supplied constraints; recommend, resize, defer or return no suitable candidate, with reasons. |
| Select and specify action | Produce exact legs, sizes, price bounds, counterparties/venues, validity and partial-execution contingencies. |
| Execute and reconcile | Revalidate current inputs; track instructions, acknowledgements, fills and physical performance; apply the specified execution contingencies. |
| Evaluate and learn | Attribute P&L, compare forecasts with outcomes, assess calibration and version revised strategies or models. |

A recommendation contains its strategy and thesis revision, evidence cutoff,
market snapshot, existing-book version, exact proposed legs, expected outcome,
downside and stress results, cash requirements, alternatives, missing evidence,
validity window, and the objective and constraints used in its comparison.

New fills, material price changes, expired logistics quotes, lost capacity or
changed thesis evidence can invalidate it. An unknown order outcome triggers
reconciliation before a potentially duplicating instruction. Material legging
risk is assessed during execution; the package label supplies no atomicity.
Human selection and automated selection are alternative realizations of the
same analytical interface. A deployment can compose regulatory, market-rule,
corporate and other governance overlays around the recommendation and action
boundaries. The overlays define any permissions and approval process.

## Recommended Action

Use this definition as an oil-domain application of the generic framework.
The first concrete implementation should bind one physical grade/location,
one benchmark hedge, one strategy thesis, the required market inputs, and the
complete P&L/reconciliation path demonstrated above.

To test the analytical definition, bind a concrete objective, deal terms,
product profiles, market and operational data, resource state, valuation basis,
and outcome measures. Strategy probabilities require prospective calibration
and point-in-time evaluation. Governance analysis is separate work over
explicit overlays and their composition.

Qualification should include partial or missing fills, duplicate reports,
different fixing windows, a failed unit conversion, stale or conflicting
assessments, basis breakdown, margin stress, delayed delivery, and correction
of previously reported P&L. Each case must change the relevant valuation,
risk result or permitted action for the right reason.

The current intake is commentary only. Adopting the domain as a Product would
enter through its own Product definition and requirements. Generic shared
method changes would be separately repriced at their STDO owner.
