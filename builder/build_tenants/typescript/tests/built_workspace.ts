/**
 * A snapshot of a workspace the method's graph has built and the user has
 * accepted, as the algorithms read it: every asset there, every check of every
 * node saying yes, and each verdict and answer recorded at each
 * node that declares it, for that node, what it declares of itself and the
 * nodes it depends on, as `step`, `answer` and `gather` record and read them
 * (REQ-ALG-004, D164, D168). `changes` gives an asset other content after they
 * were given, or takes it away (null), so that what stood for it no longer
 * does; keyed by `declaration(node)`, it gives what the node declares another
 * identity. The first vector's facts
 * are added by `inducted`, with the outcome of the term's check worked out on
 * the snapshot as `gather` works it out.
 *
 * @uses C3 C5 C6 C14
 * @is REQ-METHOD-006 REQ-ALG-004 REQ-VERIFY-004
 */
import { ASKED, declaration, TICKET, type BranchTicket, type CheckResult, type Given, type Recorded, type Snapshot, type VectorFacts } from "../src/algorithms/facts.js"
import { composes, recordsOf, standingKeys } from "../src/algorithms/passes.js"
import type { WellFormed } from "../src/algorithms/well_formed.js"
import { reference, sequence } from "../src/graph/terms.js"
import { writeTerm } from "../src/graph/written.js"

/** The identity of each asset, by node name: `<node>-1`; and of what each node that declares what accepts it, and the first vector, declares, `declared-<name>-1`; but where `changes` says otherwise. */
function identitiesOf(graph: WellFormed, changes: Readonly<Record<string, string | null>>): Map<string, string> {
  const ids = new Map<string, string>()
  const set = (key: string, first: string): void => {
    const id = key in changes ? changes[key] : first
    if (id !== null && id !== undefined) ids.set(key, id)
  }
  for (const n of graph.graph.nodes) {
    set(n.name, `${n.name}-1`)
    if ((n.accepted ?? []).length > 0) set(declaration(n.name), `declared-${n.name}-1`)
  }
  for (const v of graph.graph.vectors.filter((x) => x.first === true)) set(declaration(v.name), `declared-${v.name}-1`)
  return ids
}

/**
 * The workspace once built by the vectors `by`, in order, by default every
 * vector of the graph but the first, and accepted; then changed by `changes`,
 * with the ticket given.
 */
export function built(graph: WellFormed, ticket: Snapshot["ticket"], changes: Readonly<Record<string, string | null>> = {}, by?: readonly string[]): Snapshot {
  const then = identitiesOf(graph, {})
  const now = identitiesOf(graph, changes)
  const was: Snapshot = { identities: then, ticket: "simplest", vectors: new Map() }
  const records = new Map<string, Recorded>()
  for (const v of graph.graph.vectors.filter((x) => x.first !== true && (by === undefined || by.includes(x.name)))) {
    for (const kind of ["evaluation", "decision"] as const) {
      for (const node of recordsOf(graph, v, kind)) {
        const given: Given = { says: "yes", on: new Map(standingKeys(graph, node, was).map((key) => [key, then.get(key) ?? ""])) }
        records.set(node, { ...records.get(node), [kind === "evaluation" ? "verdict" : "answer"]: given })
      }
    }
  }
  const checks = new Map(graph.graph.nodes.flatMap((n) => (n.checks ?? []).map((c) => [c.name, { result: "yes" as const }] as const)))
  return { identities: now, ticket, checks, vectors: new Map(), records }
}

/**
 * The snapshot with each acceptance at the node the ticket enters at given
 * also on the ticket without its term as it is (D141): what the user accepted
 * there after the ticket was inducted.
 */
export function acceptedOn(graph: WellFormed, s: Snapshot): Snapshot {
  if (s.ticket === "simplest" || s.ticket.enters === undefined) return s
  const asked = s.ticket.asked ?? ""
  const enters = s.ticket.enters
  const give = (g: Given): Given => ({ ...g, on: new Map([...g.on, [ASKED, asked]]) })
  return {
    ...s,
    records: new Map([...(s.records ?? [])].map(([at, r]) => [at, at !== enters ? r : {
      ...(r.verdict === undefined ? {} : { verdict: give(r.verdict) }),
      ...(r.answer === undefined ? {} : { answer: give(r.answer) })
    }]))
  }
}

/** The written form of a term of the entries named, in order, as a ticket's field holds it. */
export const termText = (names: readonly string[]): string => writeTerm(sequence(names.map((n) => reference(n))))

/** The fields the induction writes that the term's check reads. */
export const fieldsOf = (names: readonly string[], enters: string, ends: string): ReadonlyMap<string, string> =>
  new Map([["term", termText(names)], ["enters", enters], ["ends", ends]])

/**
 * The snapshot with a ticket inducted on it: the ticket carries the term
 * named, entering and ending where given; the first vector's checks say yes,
 * the user's answer stands for the ticket, and the term's check is worked out
 * on the snapshot.
 */
export function inducted(graph: WellFormed, s: Snapshot, names: readonly string[], enters: string, ends: string): Snapshot {
  const ticket: BranchTicket = { path: ".ai-workspace/tickets/active/261121-a.md", identity: "t1", asked: "a1", enters, term: names }
  const at = confirmed(graph, { ...s, ticket }, "t1")
  const first = graph.graph.vectors.find((v) => v.first === true)
  if (first === undefined) return at
  const facts: VectorFacts = { ...at.vectors.get(first.name), composes: composes(graph, fieldsOf(names, enters, ends), at) }
  return { ...at, vectors: new Map([...at.vectors, [first.name, facts]]) }
}

/** The induction confirmed on the ticket whose identity is given, and on what the first vector declares as it is (D175), its checks saying yes. */
export function confirmed(graph: WellFormed, s: Snapshot, identity: string): Snapshot {
  const first = graph.graph.vectors.find((v) => v.first === true)
  if (first === undefined) return s
  const declared = declaration(first.name)
  return {
    ...s,
    checks: new Map<string, CheckResult>([...(s.checks ?? []), ...(first.checks ?? []).map((c) => [c.name, { result: "yes" }] as const)]),
    vectors: new Map([...s.vectors, [first.name, s.vectors.get(first.name) ?? {}]]),
    records: new Map([...(s.records ?? []), [first.name, { answer: { says: "yes", on: new Map([[TICKET, identity], [declared, s.identities.get(declared) ?? ""]]) } }]])
  }
}
