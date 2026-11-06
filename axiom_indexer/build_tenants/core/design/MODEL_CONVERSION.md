# a_c model to Axiom Program conversion

Implements REQ-P-MODEL-CONVERSION. `ac_model.py` is the generic conversion
boundary; `ac.py` retains its existing validator/map/projection/join contracts.

The input is the public source-semantic a_c proposal. Only its five authored
families may be populated. Each non-residual record becomes a relation or
constraint clause with the same identity, exact authored statement, ordered
explicit local references and a canonical JSON string containing the unchanged
record. Residuals use the ordinary residual contract with original subject
identity, exact source routes and a canonical string containing the unchanged
record. One unselected metadata clause preserves all non-population model
fields. It supplies no additional normative meaning.

The explicit conversion configuration binds program URI, source basis,
calculus URI, metadata source URI, path-prefix to logical-URI mappings and
caller-authored frame-index declarations with record roots. Source grounds
map to member URIs; the original section/line/quote remains in the exact record
payload. Local links are those exact record-identity strings already present
in the model, exposed under JSON-pointer roles. No graph adjacency inference,
automatic membership or source interpretation is performed.

Restoration validates the conversion marker, payload roles, family inventory,
original identities and exact regeneration using the retained configuration.
Round-trip equality therefore covers every input field and rejects tampered
visible statements/references, not only raw payload. Program validation then
checks existing Axiom source/reference laws. Conversion does not certify the
input a_c model; caller retains its provider's admission evidence.

Positive evidence covers all five families, conditions/exceptions, Unicode,
explicit references, overlapping frame roots and exact restoration. Refusal
cases cover duplicate/dangling identities, altered visible fields, unsupported
operational records, absent source mapping and output/input collision. Normal
and optimized Python runs exercise the same mandatory checks.
