# STRATEGY: Trading model families, strategy, and epistemic risk

**Author**: codex
**Date**: 2026-09-26T02:33:04Z
**Updated**: 2026-09-26T03:25:36Z
**Addresses**: Reusable underlying models, tradable instruments, strategy, P&L, and decisions under uncertainty
**Status**: Open
**Scope**: Pure systems analysis, illustrated through trading and risk management; governance is a separate overlay; commentary only

## Summary

A system definition should explain what exists, how it can change, what the
system can establish about it, and why an action serves an objective. An
ontology, domain algebra, and domain calculus provide the semantic foundation.
The epistemic layer represents evidence, beliefs, and unresolved possibilities.
Strategy proposes actions for an explicit reason. Valuation estimates their
outcomes, including P&L; risk evaluates their consequences; a decision function
compares actions against an explicit objective and supplied constraints.

Trading domains specialize reusable models of the underlying economic subject.
That subject exposes variables, dynamics, feasible operations and constraints.
An instrument defines the rights, obligations and payoffs being traded. A
strategy selects actions to optimize an objective over their composed model.

Bayesian inference can supply quantitative belief updates within that framework.
Its conclusions remain conditional on the evidence and model assumptions.

## Analysis

### Existing method and proposed development

The current source already includes ontology and epistemology in
[constitutional-set sufficiency](../../../specification/standards/SPEC_METHOD.md#constitutional-set-sufficiency).
The World Model Method places probabilistic correspondence and uncertainty in
[epistemic overlays](../../../specification/standards/WORLD_MODEL_METHOD.md#probability-belongs-in-the-epistemic-overlay).

This proposal develops those distinctions into a way of defining systems that
act with incomplete observations. Trading supplies the example; the framework
also applies to inventory, fulfilment, distributed operations, and autonomous
agents. These layers give requirements, design, implementation, and validation
a shared semantic basis within the development lifecycle.

### Core analysis and separate overlays

The core defines entities, operations, evidence, inference, valuation, risk,
and the relationship between action and outcome. It remains neutral about
regulatory regimes, organizational authority, corporate approvals, and whether
a person or machine selects and executes an action.

Market and product profiles supply contract-specific semantics. Separate
governance overlays supply regulatory, venue, jurisdictional, and corporate
requirements, including permissions and approval structures. Reporting overlays
select accounting presentations. These layers bind to explicit core inputs
and outputs; their rules retain their own identities and applicability.

Physical feasibility and economic consequences are core analytical concerns.
Risk appetite and approval requirements are supplied policy concerns. An
overlay can constrain action or select an analytical basis while preserving
the underlying observations, obligations, and recorded history.

### The generic framework

| Layer | Responsibility | Trading example |
|---|---|---|
| Objective | State the outcome being pursued and its scope. | Seek net returns over a declared horizon. |
| Ontology | Identify entities, relations, identities, and lifecycles. | Account, instrument, order, fill, position, venue. |
| Domain algebra | Define typed operations, composition, and invariants. | Compose fills for the same order while reconciling executed and remaining quantities. |
| Domain calculus | Define lawful derivations and transitions over that domain. | Submission, acceptance, partial fill, cancellation, and settlement have distinct consequences. |
| Epistemic calculus | Define how actions, observations, and elapsed time change knowledge and beliefs about domain states. | A submission timeout leaves acceptance and execution unresolved. |
| Bayesian inference | Assign and revise probabilities over represented possibilities using a declared model. | Estimate execution likelihood from order history, venue behaviour, and message reliability. |
| Strategy | Propose actions from an explicit thesis, objective, evidence, horizon, and invalidation conditions. | Trade a hypothesized temporary price dislocation while the supporting evidence holds. |
| Valuation and P&L | Measure economic outcomes and value possible outcomes under explicit bases. | Economic and projected P&L with declared prices, costs and currency; reporting classifications are supplied by overlays. |
| Risk model | Evaluate consequences of possible states and proposed actions. | Assess exposure, losses, and funding needs, including unresolved orders. |
| Decision function | Compare candidate actions using objectives, outcome estimates, risk, and supplied constraints. | Recommend a trade, resize, wait, or seek more evidence. |

These are distinct semantic responsibilities; their implementation may share
components. Here, algebra and calculus name generic domain structures. Applying
the separately governed STDO `a_c` would require an explicit interpretation.

### Underlying model families and instrument composition

Use two independent classification dimensions: the economic subject and the
instrument expressing exposure to it. The families below are proposed
analytical groupings with explicit domain bindings.

| Underlying family | Variables and dynamics exposed | Characteristic strategy capabilities and constraints |
|---|---|---|
| Agricultural commodities | Crop year, acreage, yield, weather, harvest timing, stocks, grade, location and quality change during storage. | Seasonal allocation, storage, processing and basis hedging; respect biological timing, commodity-specific deterioration, handling and delivery. [USDA crop estimation](https://www.nass.usda.gov/Education_and_Outreach/Understanding_Statistics/Estimating_Programs/Crops/index.php), [CME grain basis](https://www.cmegroup.com/education/courses/introduction-to-grains-and-oilseeds/learn-about-basis-grains). |
| Energy and bulk resources | Production and consumption, inventories, location, transport, capacity, conversion yields and delivery periods. | Carry, transport, conversion and relative value; bind the actual storage and transformation capability of each resource. [Oil domain application](20260926T031254Z_SCHEMA_oil_trading_domain_and_decision_support.md). |
| Industrial metals | Grade, form, location, inventory, warehouse entitlement, processing requirements, funding and deliverability. | Inventory carry, location premiums, transformation and hedging; physical entitlement and delivery specification remain explicit. [LME warrants](https://www.lme.com/Sustainability-and-Physical-Markets/Warehousing/LME-warrants). |
| Precious metals | Metal quantity, fineness, location, allocation status, custody and financing. | Physical inventory and financial exposure can use related prices while carrying different delivery and counterparty characteristics. [LBMA market structure](https://www.lbma.org.uk/market-standards/about-loco-london). |
| FX | Two currency balances, spot quotation, settlement dates, funding curves, forward points and cross-currency basis. | Currency conversion, funding, hedging and relative value; bind both currencies and their funding/settlement conditions. Forward pricing uses interest-rate relationships and observed basis. [BIS analysis](https://www.bis.org/publications/qr-201609/covered-interest-parity-lost-understanding-cross-currency-basis). |
| Equities | Ownership class, share count, distributions and corporate actions, with a model of business assets, earnings, cash flows, financing and uncertainty. | Valuation, relative value, event and exposure strategies; distinguish market-price observations from estimates of business value. [SEC ownership definition](https://www.investor.gov/introduction-investing/investing-basics/glossary/stock). |

Families can overlap. Resources can be an umbrella for energy, mineral
feedstocks and metals. Agricultural perishability varies by product. Oil,
grain and metal can share a storage operator while retaining different loss,
quality, financing and deliverability models.

The instrument dimension includes direct physical ownership, currency
balances, equity ownership, forwards, futures, swaps and options. Derivatives
compose a contractual payoff and lifecycle with one or more underlying
references. They can therefore express commodity, FX, equity or other
exposures. This economic use of the term is described in the
[CFTC derivatives glossary](https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/CFTCGlossary/index.htm);
the classification here imports no regulatory regime.

For example:

```text
wheat inventory = agricultural model + physical holding and delivery model
FX forward     = currency-pair model + forward exchange contract
oil equity     = business model + equity ownership claim
equity option  = equity model + option payoff, exercise and settlement model
oil future     = oil benchmark model + futures settlement and delivery model
```

An oil producer's share exposes the economics of that business, including its
assets and financing. A claim on barrels and a claim on the business retain
their own variables and cash-flow relations.

### What the underlying exposes to a strategy

Each model publishes a typed analytical interface:

| Element | Meaning |
|---|---|
| State variables | Quantities, balances, obligations, condition, location and lifecycle state. |
| Observable evidence | Prices, transactions, inventories, crop reports, company reports and other observations, each with provenance and time. |
| Uncertain drivers and parameters | Future prices, weather, demand, yields, default, dependencies and model assumptions. |
| Available operations | Buy, sell, hold, exchange, finance, transport, store, transform, hedge or exercise, where the subject actually supports them. |
| Dynamics and constraints | State transitions, conservation, capacity, timing, quality, settlement and resource requirements. |
| Outcome functions | Cash flows, value, P&L, service or production results, sensitivities and risk. |

Exposed variables have explicit roles. A strategy can select an order quantity
or a feasible shipment; a forecast oil price or crop yield is an uncertain
input. Observing a variable does not make it a control. Available operations
also depend on the actual subject and resources: holding a futures contract
does not by itself provide storage capacity or control of production.

A reusable strategy binds the capabilities it needs. Inventory carry uses
storage and financing; FX carry uses currency funding and exchange; conversion
strategies use an explicit input/output process. Reuse preserves the strategy
structure while binding the particular economics, observations and constraints.

One possible mathematical form, where predictive probabilities are justified,
is:

```text
pi* = argmax over feasible policies pi:
        E[U(outcomes(M, I, pi, horizon)) | epistemicState]
```

`M` is the underlying model, `I` the instrument model, and `pi` an action policy
that can respond to later observations. `U` expresses the objective, including
costs and selected trade-offs. Feasibility includes intrinsic dynamics and
resource constraints plus any explicitly supplied analytical constraints.
External governance evaluates the resulting recommendation separately.

The optimized object is the objective evaluated through the model. The model
itself remains subject to evidence, falsification and revision. Scenario or
robust comparisons can replace expectation when probabilities are insufficient.
An optimizer's result retains its model assumptions and search limits.

### Connecting the calculi

The epistemic layer refers to the same domain entities and transitions. Its
additional concepts include claims, evidence, source identity, observation and
receipt times, assumptions, and conflicts. An observation can revise a belief
about a fill; changing that belief does not execute or undo the fill.

One possible functional boundary is:

```text
E_next   = updateKnowledge(E, domainActions, observations, elapsedTime)
C        = proposeActions(underlyingModel, instrumentModel, objective, strategy, E_next)
V        = valueOutcomes(C, underlyingModel, instrumentModel, E_next, valuationBasis)
R        = assessRisk(C, underlyingModel, instrumentModel, E_next, V, riskModel)
decision = compareActions(C, V, R, E_next, objective, suppliedConstraints)
```

`E` includes supported possibilities, evidence, assumptions, and any justified
probability model. The domain calculus constrains the possible transitions;
the epistemic calculus governs what observations warrant concluding about them.
`C` includes doing nothing and seeking evidence. Governance overlays evaluate
the recommendation and its context separately. Execution produces new domain
events and observations, which feed the next epistemic and strategy evaluation.

### Strategy: the reason to act

An objective states the desired outcome. A strategy states a testable reason
why particular actions could achieve it. In trading, this is the investment or
trading thesis: the opportunity, supporting evidence, expected mechanism,
relevant horizon, candidate entries and exits, and conditions that invalidate
the thesis. Forecast benefit is evaluated after applicable costs.

For illustration, a strategy hypothesizes that a temporary liquidity
dislocation has depressed a price and will unwind within its stated horizon.
It proposes a purchase while the evidence supports that mechanism. New evidence
of a lasting impairment can invalidate the thesis and withdraw the proposal,
even when the measured risk remains unchanged.

The thesis is itself an epistemic claim. Evidence about whether the order
filled and evidence about whether the opportunity exists answer different
questions. Each proposed action carries its thesis and supporting evidence so
later evaluation can reconstruct why it was proposed.

P&L supplies outcome feedback. Strategy evaluation compares observed results
with its predictions and assumptions; a profitable individual trade alone
does not establish a reliable strategy. In another domain, the corresponding
outcome could be service reliability, delivery success, or resource use.

### Trading example: an unresolved order

Assume the strategy above proposes purchases, an initial position of zero, and
no other activity. Supply a maximum-exposure parameter of 150 units of one
instrument for this decision experiment. The core calculates exposure; the
selection and ownership of that threshold belong to a separate policy overlay.

1. A buy order for 100 units is submitted. The response times out. The system
   has evidence of submission, while rejection, partial execution, and full
   execution remain possible. A missing acknowledgement does not establish
   rejection.
2. A second buy for 80 units is proposed. With the first order unresolved,
   combined potential exposure reaches 180 units. The proposal exceeds the
   supplied threshold. A Bayesian estimate favouring no execution does not
   remove the possible 100-unit exposure from this comparison.
3. A trusted, reconciled final report establishes 60 units filled and the
   remaining 40 cancelled for the first order. Potential exposure after the
   proposed second order is now 140 units. It satisfies this supplied bound;
   the strategy still needs a supported thesis and acceptable projected net
   outcome, alongside price, liquidity, credit, and other applicable checks.

The observed information changes the justified decision. Reconciliation is
therefore an available risk-management action: it can reduce uncertainty before
further exposure is taken. Increasing observation age can also change the
risk assessment, even without a new confirmed trade.

### P&L: value the outcome and its uncertainty

The economic model derives P&L from trade history, positions, cash flows,
prices, FX rates and costs. Reporting overlays select accounting conventions.
For the simple cash-equity example, distinguish realized P&L from closed
positions, unrealized P&L at selected marks, and projected P&L across future scenarios.
Matching and cost conventions affect the calculation; the
[IBKR reporting guide](https://www.interactivebrokers.com/download/reportingguide.pdf)
provides concrete examples.

Suppose, before final reconciliation, 60 shares are confirmed bought at $100
and another 40 may have filled at that same price. At a selected mark of $102,
unrealized P&L ranges from $120 to $200 before costs. Those bounds describe
uncertainty about the current holding under a fixed mark. Future price changes
produce a separate range or distribution of projected outcomes.

A P&L result carries its valuation time, evidence cutoff, currency, accounting
and valuation basis, and unresolved assumptions. This allows a late fill report
to correct the result without presenting the correction as a new market gain.
Bayesian inference can weight represented outcomes. Expected P&L remains a
forecast or estimate under that model; reported realized and unrealized values
retain their declared evidence and accounting basis.

### Bayesian updating and incomplete knowledge

[Dynamic Update with Probabilities](https://link.springer.com/article/10.1007/s11225-009-9209-y)
formalizes probabilistic dynamic epistemic updates using prior probabilities,
event occurrence probabilities, and observation probabilities. This provides a
mathematical basis for combining logical information change with quantitative
belief updates.

For an evolving system, an implementation would first predict how represented
states may have changed, then condition on the observation through its
likelihood model. Delayed, duplicated, or correlated messages need corresponding
treatment; duplicate reports do not supply independent evidence.

Two limitations remain explicit:

- **Uncertainty within the model:** several represented states fit the evidence.
  Bayesian inference can update their relative probabilities.
- **Incompleteness of the model:** relevant behaviours or failure modes may be
  absent. A posterior distribution does not establish that the model covers
  reality. Model assumptions and evidence of their failure remain risk inputs.

High confidence remains a belief with an evidence and model basis. The risk
model retains consequential alternatives and model limitations; the decision
function evaluates their significance for its objective. Where probabilities
lack a defensible basis, explicit possibilities or bounds can still support
decisions.

## Recommended Action

Develop this as generic guidance for composing underlying model families,
instrument models, evidence, strategies, valued outcomes, risk, and action.
Use worked scenarios to show how both the reason to act and the selected
action change as evidence changes, with governance supplied through separate
overlays.

Shared methodology can define the required semantic distinctions and evidence
relations. A domain application specifies its objectives, domain meanings,
evidence model, strategy, outcome measures, and risk calculations. Its design
specifies the strategy realization, inference machinery, calibration, and
computational representation. Governance overlays independently specify
regulatory and organizational constraints. Bayesian inference remains a
design choice where the analytical needs justify it.

This post is commentary-only intake. Adoption that changes shared obligations
would enter through `requirement_reprice` at the owning standards. No such
adoption is asserted here.
