# TASK F: judge occurrence lineage and stops

## Subject

Product `inventory-sync`: it reconciles warehouse stock with a shop
catalogue under a traversal occurrence profile. The facts below are the
whole subject; the record is invented for this task and is evidence about
no real product.

Events and edges in the admitted history:

- `ev-101` "stock of SKU-9 observed as 40" (09:00:00, actor `sync-bot`)
  and `ev-102` "reorder issued for SKU-9" (09:00:40, actor `sync-bot`).
  A projection records `causally_precedes_event(ev-101, ev-102)` because
  `ev-102` followed `ev-101` within one minute on the same SKU and by the
  same actor. No causal claim about these events was submitted or
  admitted.
- `ev-103` "stock of SKU-9 observed as 14" was later found to be a
  miscount. An operator edited `ev-103` in the event store so that it now
  reads 41, keeping its id `ev-103`. No other event was added.
- Edge `L-9` is recorded as `causally_precedes_occurrence` with source
  `ev-107`, a framework event, and target `occ-22`, an occurrence.
- The reorder policy selects current stock by the declared precedence
  coordinate `observed_at`, latest first. The policy also treats the
  event with the greatest `observed_at` as the decision on whether a
  pending reorder is approved.

Stopped occurrences:

- `occ-23`: the judgment needs the currentness of event frontier `F-9`.
  The newest frontier has not yet been observed. Every relation and
  capability the judgment needs is declared in the profile and was
  exercised.
- `occ-24`: the effect began and decremented warehouse stock for 3 of 5
  SKUs, then the warehouse system returned an error. The observed
  post-state defeats the intended outcome as a whole.
- `occ-25`: the occurrence seed's `identity_depends_on` names record
  `r-77`, which does not resolve in the model.

## Instruction

1. For `ev-101` and `ev-102`, say whether cause is established and what
   would establish it.
2. For `ev-103`, say whether the operator's edit is lawful and what a
   lawful correction records.
3. For `L-9`, say whether the edge is lawful, which law decides, and the
   stop and core result member that follow.
4. For the reorder policy, say what the precedence coordinate may and may
   not do.
5. For each of `occ-23`, `occ-24` and `occ-25`, give the stop kind and
   its core result member, and say what, if anything, must survive beside
   that member.

Then, under a heading `No method source`, list anything the task needed
that the METHOD block did not supply; write `none` if nothing.

Return only those six parts, in that order. Do not restate the subject.
