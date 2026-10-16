**T2 — Frame Evaluation Result**

The replacement produces the required planning dockets for B1 and rejects B2 before constructing any docket. It establishes no authority to return equipment to service.

**Binding and decision**

- **Activation:** T2, maintenance docket builder.
- **Subject:** The replacement function below, evaluated against the supplied requirements and batches B1 and B2.
- **Basis:** `task`, SHA256 `4d0ac41cc85f301b86aed094aee60bdad01881365c3dbc2a9dc9ef4479ff35e8`; selected `run://T2/frame`, SHA256 `17461e64170dabfe45e9eb8b469c84f5af21953ee7be587fe7718c0fe7e0fc2f`.
- **Predicate:** For finite ordered batches of string request IDs and risks `high`, `low`, or `unknown`, route each request correctly, retain IDs and relative order, and reject any repeated-ID batch before producing dockets.
- **Actor and capability:** Nonauthor task actor; source reading, response construction and local in-memory Python execution.
- **Authority:** Construct and exercise a replacement. Equipment-state changes and duty-manager decisions are outside the grant.
- **Method selection:** Generic method only. No optional graph, traversal, Ontology or architectural realization profile was adopted. The acquired design owner explicitly distinguishes generic law from its adoptable profile. [Source: `run://T2/method/standards/DESIGN_MODULE_METHOD.md#governing-relations`]

The current procedure fails the requirements: its `otherwise` branch sends R18 and R20 to service, and it contains no whole-batch duplicate rejection. The replacement preserves the supplied requirements rather than changing their meaning. [Source: `task`, “Required behavior”, “Current procedure”, B1 and B2]

**Replacement**

The function’s admitted input is a finite immutable tuple of `(request_id, risk)` pairs, with string IDs and one of the three declared risk values. The supplied batches are represented below without changing their values or order.

```python
def build_dockets(batch):
    """Domain: finite immutable tuples of (string ID, high|low|unknown)."""
    first_position = {}
    for position, (request_id, risk) in enumerate(batch, start=1):
        if request_id in first_position:
            return {
                "outcome": "rejected",
                "reason": "duplicate_id",
                "request_id": request_id,
                "positions": (first_position[request_id], position),
            }
        first_position[request_id] = position

    dockets = {"isolation": [], "service": [], "inspection": []}
    destination = {
        "high": "isolation",
        "low": "service",
        "unknown": "inspection",
    }
    for request_id, risk in batch:
        dockets[destination[risk]].append(request_id)
    return {"outcome": "planned", "dockets": dockets}
```

The material states are: supplied batch → duplicate validation → complete planning result or rejection. Docket construction begins only after the whole batch passes duplicate validation. The routing table covers all three admitted risk values. The second pass appends each unchanged ID once, in input order, preserving relative order within every docket. A duplicate returns an explicit reason before the docket containers exist.

These operations realize the task’s WHAT through a concrete HOW without introducing equipment actions or transferring decision authority. [Sources: `run://T2/frame#what-how-and-work-carriers`; `run://T2/method/standards/TRANSFORMATION_LIBRARY.md#foundational-contract`; `run://T2/method/standards/FOUNDATIONS.md#foundational-commitments`]

**Execution evidence E1**

I executed the displayed function in memory with:

```python
B1 = (
    ("R17", "high"),
    ("R18", "unknown"),
    ("R19", "low"),
    ("R20", "unknown"),
)
B2 = (
    ("R17", "high"),
    ("R19", "low"),
    ("R17", "low"),
)

result1 = build_dockets(B1)
result2 = build_dockets(B2)
```

Observed output:

```text
B1: {'outcome': 'planned', 'dockets': {'isolation': ['R17'], 'service': ['R19'], 'inspection': ['R18', 'R20']}}
B2: {'outcome': 'rejected', 'reason': 'duplicate_id', 'request_id': 'R17', 'positions': (1, 3)}
All assertions passed; both input batches remain unchanged.
```

The process exited with code `0`. Assertions checked both exact results, the absence of a `dockets` field in B2’s rejection, and preservation of both inputs. B2 produces **no dockets**, including no partial docket containing its earlier entries.

| Evaluation | Core verdict | Performance | Original domain outcome and support |
|---|---|---|---|
| B1 satisfies routing, retention and order requirements | `satisfied` | `performed` | `planned`; E1 yields isolation `[R17]`, service `[R19]`, inspection `[R18, R20]` |
| B2 satisfies the whole-batch duplicate-rejection requirement | `satisfied` | `performed` | `rejected`, reason `duplicate_id`, R17 at positions 1 and 3; E1 and the validation-before-construction control flow |
| Replacement fulfills the bounded construction and exercise task | `satisfied` | `performed` | Replacement constructed and exercised; requirement-preservation argument and E1 |
| Physical fitness of the equipment for return to service | `out_of_frame` | `performed` for the scope diagnosis only | This activation supplies no physical assessment capability or evidence; physical assessment was not performed |

B2’s domain outcome `rejected` satisfies its required handling predicate. It is not interpreted as failure merely because its outcome label says “rejected.” This preserves the selected method’s distinction between the actual predicate, original domain outcome, evaluation performance and observed effects. [Sources: `run://T2/frame#result-algebra`; `run://T2/method/standards/FOUNDATIONS.md#core-contract-derivations`]

**Return-to-service conclusion and effects**

R19’s service-docket entry is a planning result. Returning any equipment to service still requires a separate duty-manager signature, and none is supplied. This artifact provides classification evidence only; it supplies neither that signature nor a physical fitness determination. [Sources: `task`, authority and signature condition; `run://T2/frame#rf-006-authority-conservation`]

For this activation, response and in-memory planning effects are `completed`. Equipment-state effects are `not_requested`: the operating boundary consists of pure computation and response output, with no equipment interface or equipment-changing operation. Parent-owned reader acquisition recording is separate instrumentation.

No installation, adoption or wider qualification conclusion follows. The result would require reconsideration if the requirements, risk meanings, ID equality rule, input operating model or signature requirement changed. Inputs outside the declared function domain remain unevaluated.

**Acquisition and observed limits**

Actual routes read:

| Route | Selection |
|---|---|
| `task` | Complete task packet, including both case batches |
| `catalog` | Complete supplied-route inventory |
| `run://T2/frame` | Full acquisition, then lines 280–820 |
| `run://T2/method/standards/FOUNDATIONS.md` | `core-contract-derivations`; `foundational-commitments` |
| `run://T2/method/standards/SPEC_METHOD.md` | `method-families` |
| `run://T2/method/standards/TRANSFORMATION_LIBRARY.md` | `foundational-contract` |
| `run://T2/method/standards/DESIGN_MODULE_METHOD.md` | `governing-relations` |
| `measurements` | Once, near completion |

The catalogue reports **2,154 supplied task bytes** and **71,215 supplied frame bytes**. The reader reported **124,706 cumulative acquired UTF-8 bytes before its measurement report**, including repeated reads, against **317,628 bytes** allowed. It reported **112.619 seconds elapsed** against **600 seconds** allowed.

The initial broad frame response was display-truncated. The subsequent line selection and owning-source sections supplied the material used above; no claim depends on unseen text.

For the reader-supplied portion, cumulative acquisition provides an upper bound of 124,706 source bytes before the measurement report. Actual active and retained host context, native spend and attention adequacy are unmeasured; cumulative acquisition does not establish them. Additional paid calls were **0**. The activation prompt, native surrounding context, execution transcript, response generation and measurement-report text are outside that reported pre-report acquisition total.
