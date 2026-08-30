# ABIogenesis Map-First Pickup Review

## Subject

- Skill: `skills/axiomatize-corpus/SKILL.md`
- Map: `dogfood/abg/logical-constraint-map.json`
- Evaluation mode: read-only, map first
- ABIogenesis constitutional source opened: none

## Initial result

The fresh agent correctly recovered:

- Wave 2 R2/R3 decision-complete design only;
- no implementation, candidate, E00, or release authority;
- GTL ownership, non-lowering validation, direct HoG traversal, ABG runtime
  admission, Event Calculus, and replay boundaries; and
- the unrelated dirty workspace file as local tooling outside the selected
  work.

It found one structural pickup defect: the HoG-to-ABG relation existed only in
a scalar root-path statement. After that typed edge was added, it found two
remaining prose-only dependencies: validator-to-program and
replay-to-event-history.

## Retained repair

The program now contains typed clauses for:

- `gtl-validator-validates-program`;
- `hog-requires-validated-program`;
- `hog-runtime-effects-require-abg-admission`; and
- `replay-derives-from-event-history`.

## Final disposition

GO. The complete chain is traversable through typed clauses:

```text
GTL Program -> validator -> HoG -> ABG admission
  -> event history -> Event Calculus / replay
```

The agent reported no remaining P1 pickup gap. It did not open ABIogenesis
constitutional prose or edit any file.

## Executive joiner dogfood

A second fresh agent received only the exact rendered Executive request and the
logical map. It had no surrounding Axiom Indexer conversation and worked
read-only.

Exact input boundary:

- program semantic digest:
  `sha256:43fc2c49bbc7d1d7a959031abb458aac990a426944d93232ccf7fc32c670c2c9`;
- map semantic digest:
  `sha256:450acdf44ac9184950166557f9f3574dbce06987a7ff059c9b1be3e326e0e1c6`;
- `executive-sections.json` SHA-256:
  `983525c95b73414e7b35ab5b512e553d1a089e372d383c6cccc2913881fbe57f`;
- `executive-request.txt` SHA-256:
  `76285e24927e7f3b2a64e29edd4d972b8773e30cc68c85c0bcfde800dc107945`;
- `executive-result.md` SHA-256:
  `bce4cc2c08b563ce9c048a61efb7cd82fbc8eeebc7fca109503e12a4130e0ecf`;
- ABIogenesis base commit:
  `9eb0e92f81fea23a4bf6a2d7b74684d460e5b6be`;
- ABIogenesis base tree:
  `78b0fdd706576b882e6b0af9731bd79896c9fe00`.

The request visibly supplied four selected frame URIs, each with purpose and
source route. The downstream Executive used those frames, re-entered the
accepted-design residual, selected R2 ahead of R3, and returned a bounded
design-only Worker assignment, one independent Reviewer criterion, and exact
stop/re-entry URIs. It did not mutate ABIogenesis or infer implementation or
release authority. The full result is retained in `executive-result.md`.
