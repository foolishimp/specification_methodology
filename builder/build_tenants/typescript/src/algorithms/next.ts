/**
 * `next`: of the vectors that take part, the first that is open, in the order
 * of the term in force (`inForce`), the ticket's or the default, or in an
 * inner workflow in the order its edges give (`well_formed`, C7). Either order
 * respects the edges: each vector comes after those that write what it rests
 * on, so what it rests on is accepted once every vector before it is closed
 * (REQ-METHOD-006). While the first vector for a ticket is open, it is next
 * before any other. So no vector is next before every node it rests on is
 * accepted as it stands, the user's decisions the graph declares there among
 * them: in the method's graph, the design is never next before the user has
 * accepted the requirements (REQ-METHOD-003, D189).
 *
 * Which vectors take part in the work on a ticket is read here too: those the
 * term in force denotes, beside the first vector for a ticket. The term in
 * force is the ticket's own where it carries one that reads; for the simplest
 * ticket, on main and for a ticket with none, the registry's default term
 * (REQ-ALG-006, REQ-METHOD-006).
 *
 * @uses C3
 * @is REQ-ALG-006 REQ-METHOD-003
 */
import type { Vector, Workflow } from "../graph/terms.js"
import type { Snapshot } from "./facts.js"
import { open } from "./open.js"
import type { WellFormed } from "./well_formed.js"

/**
 * The term in force on the snapshot's ticket: the vectors of the governing
 * graph it denotes, by name, in its order. The ticket's own term where it
 * carries one that reads; otherwise, for the simplest ticket, on main and for
 * a ticket not yet inducted, the registry's default term (REQ-METHOD-006).
 */
export function inForce(graph: WellFormed, snapshot: Snapshot): readonly string[] {
  return (snapshot.ticket === "simplest" ? undefined : snapshot.ticket.term) ?? graph.byDefault
}

/**
 * Whether a vector takes part in the work on the snapshot's ticket
 * (REQ-ALG-006). The first vector for a ticket takes part for every ticket but
 * the simplest. A vector of an inner workflow (`top` false) takes part
 * wherever the vector that holds it is stepped on. Of the governing graph's
 * other vectors, those the term in force names take part, and no other.
 */
export function takesPart(graph: WellFormed, vector: Vector, snapshot: Snapshot, top = true): boolean {
  if (vector.first === true) return snapshot.ticket !== "simplest"
  if (!top) return true
  return inForce(graph, snapshot).includes(vector.name)
}

/**
 * The next vector of the well-formed graph, or of one of its inner workflows
 * (`within`), or undefined when none may run.
 */
export function next(graph: WellFormed, snapshot: Snapshot, within: Workflow = graph.graph): Vector | undefined {
  const top = within === graph.graph
  const taking = within.vectors.filter((v) => takesPart(graph, v, snapshot, top))
  const first = taking.find((v) => v.first === true)
  if (first !== undefined && open(graph, first, snapshot)) return first
  const order = top ? inForce(graph, snapshot) : (graph.orders.get(within) ?? [])
  return order.flatMap((name) => taking.filter((v) => v.name === name)).find((v) => open(graph, v, snapshot))
}
