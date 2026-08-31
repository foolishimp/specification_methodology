# STDO Representation Requirements

The active requirements define one thin LLM-operated path:

```text
Source STDO
  -> LLM-authored a_c.STDO
  -> exact Axiom Indexer validation and logical map
  -> LLM-selected frames and ordered sections
  -> exact Axiom Indexer join
  -> native Codex or Claude use
```

1. [`REQ-P-BASIS-AND-IDENTITY.md`](REQ-P-BASIS-AND-IDENTITY.md) binds exact
   Source STDO, Axiom Indexer, program, map, skill, and request coordinates.
2. [`REQ-P-STDO-AUTHORING-MAP.md`](REQ-P-STDO-AUTHORING-MAP.md) specializes the
   released Axiom Indexer `a_c.text` program for Source STDO.
3. [`REQ-P-CANDIDATE-VALIDATION.md`](REQ-P-CANDIDATE-VALIDATION.md) defines the
   LLM author/diagnose/repair boundary and imports the released validator.
4. [`REQ-P-NATIVE-FRAME-USE.md`](REQ-P-NATIVE-FRAME-USE.md) defines native
   Codex and Claude pickup, explicit LLM frame selection, and exact joining.
5. [`REQ-P-DOGFOOD-VERIFICATION.md`](REQ-P-DOGFOOD-VERIFICATION.md) determines
   whether the thin Product is useful enough to release and keep using.

Source STDO remains semantic authority. Axiom Indexer owns its released
mechanical contracts. This Product owns only the selected STDO authoring map,
native instructions, and their bounded usefulness claim.

The active requirement set does not define a complete admitted `a_c` model,
GTL overlay, GraphFunction, automatic closure, deterministic prompt packet,
renderer, skill generator, or ABG runtime. Retained implementations of those
earlier directions are historical evidence outside the `0.1.0` Product.
