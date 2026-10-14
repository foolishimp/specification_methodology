## Verdict: consistent

The composite now uses the single-effect rule as the owner of part classification and adds nothing of its own. The sentence "The composite supplies no different classification for either case" closes the earlier duplication. Parts owned by absent slots also go through the same rule.

### Discriminators (owner → composite join)

| Part state | Owner classification | Composite treatment |
|---|---|---|
| Requested, observed not to begin | `not_started` | joins as `not_started` |
| Unrequested possible part, observed not to begin | `not_requested`, observation retained, explicitly "not an uncompleted requested remainder" | absorbed by every non-unknown rule |
| Requested, unknown | `unknown` | any unknown gives `unknown` |
| Unrequested possible part, insufficient observation | `unknown` | any unknown gives `unknown` |
| Requested or unintended, completed | `completed` (the boundary includes observed departures) | `completed` |
| Begun, all reversed | `reverted` | `reverted`, also absorbing `not_started` and `not_requested` |

### Required checks

- **completed (requested) + observed absent (unrequested) = `completed`.** The owner maps the unrequested part to `not_requested`. The join rule "completed with only completed or not_requested" then gives `completed`. It does not give `partial`, so the original defect is fixed.
- **completed (requested) + unknown (unrequested) = `unknown`.** The owner classifies the unrequested part as `unknown`. Both the join ("any unknown") and the owner's own rule ("unknown completion → unknown, retaining completed parts") give `unknown`.

The other mixtures also agree with the owner's definitions:
- completed + `not_started` or `reverted` gives `partial`.
- `reverted` + `not_started` gives `reverted`, matching "any unstarted remainder retained".

### Minor wording notes (not contradictions)

1. **"unexecuted" in the owner's `partial` definition.** The phrase "observed unexecuted or reverted remainder" could be read as including an unrequested part observed absent. A later sentence rules that reading out. Changing "unexecuted" to "requested remainder observed not started" would remove the ambiguity at the definition itself.
2. **Owner aggregation of a multi-part single effect.** The owner names `partial`, `unknown` and `reverted` mixtures, but never states that completed + `not_requested` gives `completed`. That result follows only by elimination, while the composite join states it explicitly. One owner sentence would close this. Alternatively, the owner could reference the join as the shared rule, so the two cannot drift apart again.

Neither note changes any outcome above.
