/**
 * `done`: yes when `passes` says yes for every vector that takes part, on the
 * workspace as it is; otherwise the vectors and the checks that say no. For a
 * ticket, the vectors that take part are those of the term in force: its own,
 * or the default (REQ-ALG-006).
 *
 * @uses C3
 * @is REQ-ALG-011
 */
import { all, type Tri } from "../kit/three_valued.js"
import type { Workflow } from "../graph/terms.js"
import type { Snapshot } from "./facts.js"
import { takesPart } from "./next.js"
import { passes, type Outcome } from "./passes.js"
import type { WellFormed } from "./well_formed.js"

export interface SaysNo {
  readonly vector: string
  readonly outcomes: readonly Outcome[]
}

export type Done = { readonly done: "yes" } | { readonly done: "no"; readonly saysNo: readonly SaysNo[] }

export function done(graph: WellFormed, snapshot: Snapshot, within: Workflow = graph.graph): Done {
  const saysNo: SaysNo[] = []
  const results: Tri[] = []
  for (const v of within.vectors) {
    if (!takesPart(graph, v, snapshot, within === graph.graph)) continue
    const p = passes(graph, v, snapshot)
    results.push(p.result)
    if (p.result !== "yes") saysNo.push({ vector: v.name, outcomes: p.outcomes.filter((o) => o.result !== "yes") })
  }
  return all(results) === "yes" ? { done: "yes" } : { done: "no", saysNo }
}
