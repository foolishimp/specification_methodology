# Requirements

Requirements are decomposed from [the product definition](../PRODUCT.md) and
[the intent](../INTENT.md). Every family is a draft until the product owner
accepts it. Status says whether an obligation binds the first build (Active)
or is put off until after it (Deferred).

The product's functions are stated as algorithms and process flows. How much,
how fast and for how many is stated apart, as parameters. No page names a
technology stack: that is bound last, in the build
([how work is done](../REFERENCE_FRAME_BASIS.md)).

| Family | File | Covers |
|---|---|---|
| REQ-ALG-* | [ALGORITHMS.md](ALGORITHMS.md) | What the product decides, as twelve algorithms |
| REQ-FLOW-* | [FLOWS.md](FLOWS.md) | What happens and in what order: set-up, a run, a ticket, a step, a question, the event log, merging, several tickets at once, the release that builds a product |
| REQ-PARAM-* | [PARAMETERS.md](PARAMETERS.md) | Every number: scale, cost and limits |
| REQ-GRAPH-* | [GRAPH-LANGUAGE.md](GRAPH-LANGUAGE.md) | The graph language and the registry |
| REQ-METHOD-* | [METHOD-GRAPH.md](METHOD-GRAPH.md) | The method's own work as a graph |
| REQ-INTERFACE-* | [INTERFACE.md](INTERFACE.md) | The library and the four ways it is instanced; the workspace; releasing and installing |
| REQ-VERIFY-* | [VERIFICATION.md](VERIFICATION.md) | How the product is shown to work |

The scenarios are in [SCENARIOS.md](SCENARIOS.md).
