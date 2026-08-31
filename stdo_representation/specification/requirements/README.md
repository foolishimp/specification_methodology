# STDO Representation Requirements

The active requirements define one thin LLM-operated path:

```text
Source STDO
  -> LLM-authored a_c.STDO semantic compression
  -> exact Axiom Indexer validation and logical constraint index
  -> LLM-selected frames and ordered sections
  -> exact Axiom Indexer join
  -> native Codex or Claude use
```

1. [`REQ-P-BASIS-AND-IDENTITY.md`](REQ-P-BASIS-AND-IDENTITY.md) binds exact
   Source STDO, Axiom Indexer, program, map, skill, and request coordinates.
2. [`REQ-P-STDO-AUTHORING-MAP.md`](REQ-P-STDO-AUTHORING-MAP.md) defines the
   Source STDO semantic compression and deterministic index over it.
3. [`REQ-P-CANDIDATE-VALIDATION.md`](REQ-P-CANDIDATE-VALIDATION.md) defines the
   LLM author/diagnose/repair boundary and imports the released validator.
4. [`REQ-P-NATIVE-FRAME-USE.md`](REQ-P-NATIVE-FRAME-USE.md) defines native
   Codex and Claude pickup, explicit LLM frame selection, and exact joining.
5. [`REQ-P-DOGFOOD-VERIFICATION.md`](REQ-P-DOGFOOD-VERIFICATION.md) determines
   whether the thin Product is useful enough to release and keep using.

Source STDO remains semantic authority. Axiom Indexer owns its released
mechanical contracts. This Product owns the selected `a_c.STDO` compression,
its constraint index, native instructions, and their bounded usefulness claim.

The active requirement set does not define a complete admitted `a_c` model,
GTL overlay, GraphFunction, automatic closure, deterministic prompt packet,
renderer, skill generator, or ABG runtime. Retained implementations of those
earlier directions are historical evidence outside the active Product.
