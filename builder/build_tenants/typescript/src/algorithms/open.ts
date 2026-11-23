/**
 * `open` and `changed`: a vector is open when `passes` does not say yes for
 * it on the workspace as it is now, and closed when it does.
 * `changed` names the nodes it rests on, and the ticket without its term at
 * the node the ticket enters at, whose identity differs from the one its
 * verdict (or, with no evaluation, its answer) was given on, at any node it is
 * recorded at: `since` (C2) of each record. An outer vector is open or closed
 * by its own checks and the records at the nodes it writes, whichever vector
 * gave them.
 *
 * @uses C2 C3
 * @is REQ-ALG-005 REQ-GRAPH-006
 */
import type { Vector } from "../graph/terms.js"
import { ASKED, type Snapshot } from "./facts.js"
import { passes, recordAt, recordsOf, since } from "./passes.js"
import { placedOf, type WellFormed } from "./well_formed.js"

export function open(graph: WellFormed, vector: Vector, snapshot: Snapshot): boolean {
  return passes(graph, vector, snapshot).result !== "yes"
}

/** The nodes it rests on, and the ticket without its term under ASKED, whose content changed since its verdict or answer was given, each compared on what that record stands for. */
export function changed(graph: WellFormed, vector: Vector, snapshot: Snapshot): readonly string[] {
  const kind = vector.evaluation !== undefined ? "evaluation" : "decision"
  const keys = [...placedOf(graph, vector).rests, ASKED]
  const differs = new Set(recordsOf(graph, vector, kind).flatMap((at) => {
    const record = recordAt(at, kind, snapshot)
    return record === undefined ? [] : since(graph, at, record.on, snapshot)
  }))
  return keys.filter((key) => differs.has(key))
}
