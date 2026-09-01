# Axiom Indexer Requirements

The Product has six requirement families:

| Family | Owns |
|---|---|
| `REQ-P-AUTHORING` | LLM semantic compression and residual honesty |
| `REQ-P-PROGRAM` | the symbolic axiomatic-program contract |
| `REQ-P-RESOLUTION` | URI late binding and source re-entry |
| `REQ-P-VALIDATION` | small deterministic checks and diagnostics |
| `REQ-P-JOINING` | exact LLM-supplied labeled-text joining |
| `REQ-P-RELEASE-COUPLING` | exact Source STDO and Axiom cut alignment |

The LLM authors meaning and selects request frames, labels, text, and order.
Code resolves, validates, instantiates, reports, and joins. GTL, automatic
frame selection, carrier admission, and semantic acceptance remain deferred.
Release publication adds no Product requirement family; the installed STDO
Release Method and the selected release record govern each point-in-time cut.
The release-coupling family owns the permanent cross-release identity and
dependency relation, not publication operations.
