/**
 * QA-14, REQ-VERIFY-003: scenario S1 judged from the workspace it leaves, not
 * from the event log. Every answer and every verdict on main stands for the
 * content main holds: each identity it was given on is the identity git gives
 * now of that asset, or of the ticket in the done lane, whole or without its
 * term, or of what the node, or the first vector of the ticket, declares in
 * main's graph (D168, D175). S1's own test is left as it is. S1's term is the specification and
 * then the build: the build's one verdict is recorded at the design, the tests
 * and the code, and its answer at the code, where each of the six reads them
 * (D164).
 *
 * @uses C14 C5 C6 H5
 * @is REQ-VERIFY-003 REQ-ALG-004 REQ-METHOD-006
 */
import { existsSync } from "node:fs"
import { execFileSync } from "node:child_process"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { withoutField } from "../src/kit/field_lines.js"
import { build, clean, methodGraph, onMain, placesIn, S1_FIXTURES, s1Whole, Workspace, resolvedOnMain } from "./scenario_driver.js"
import { placedOf, well_formed } from "../src/algorithms/well_formed.js"
import { declarationsOf } from "../src/flows/workspace.js"

let ws: Workspace
let ticket = ""

beforeAll(async () => {
  ws = new Workspace(build())
  ticket = (await s1Whole(ws, S1_FIXTURES)).ticket
}, 180_000)

afterAll(clean)

/** The identity git gives now, on main, of a node's asset by its name, or of the ticket; of an asset of several paths, each path with its own. */
const now = (key: string): string => {
  const rev = (place: string): string => ws.git(["rev-parse", `main:${place}`]).trim()
  const done = `.ai-workspace/tickets/completed/${ticket}.md`
  if (key === "the ticket") return rev(done)
  // At the vector the ticket enters by, the ticket without its term (D141).
  if (key === "the ticket but its term") {
    return execFileSync("git", ["-C", ws.root, "hash-object", "--stdin"], { input: withoutField(ws.git(["show", `main:${done}`]), "term"), encoding: "utf8" }).trim()
  }
  // What a node declares of itself, or the first vector of the ticket, in its one written form, from main's graph (D168, D175).
  if (key.startsWith("the declaration of ")) {
    const g = well_formed(ws.git(["show", "main:.stdo-builder/graph.json"]), ws.git(["show", "main:.stdo-builder/registry.json"]))
    const written = "yes" in g ? new Map(declarationsOf(g.yes)).get(key) : undefined
    if (written === undefined) throw new Error(`main's graph declares nothing under ${key}`)
    return execFileSync("git", ["-C", ws.root, "hash-object", "--stdin"], { input: written, encoding: "utf8" }).trim()
  }
  const paths = placesIn(ws).get(key) ?? [key]
  return paths.length === 1 ? rev(paths[0] ?? key) : paths.map((p) => `${p} ${rev(p)}`).join("\n")
}

describe("QA-14 S1, judged from the workspace it leaves", () => {
  it("every answer on main is a resolution in a ticket that says yes, and the commit it names holds the content main holds (REQ-FLOW-001, REQ-FLOW-005)", () => {
    const graph = methodGraph()
    const nodes = graph.graph.nodes.filter((n) => n.accepted?.includes("decision") === true).map((n) => n.name)
    for (const node of nodes) {
      const got = resolvedOnMain(ws, node)
      expect(got.length, node).toBeGreaterThan(0)
      const place = placesIn(ws).get(node) ?? []
      for (const path of place) expect(ws.git(["rev-parse", `${got.at(-1)?.commit ?? ""}:./${path}`]), `${node} ${path}`).toBe(ws.git(["rev-parse", `main:./${path}`]))
    }
    // No other file of the framework's holds one, nor a record of a reading or a question (REQ-FLOW-001).
    expect(onMain(ws).filter((p) => p.startsWith(".stdo-builder/answers/") || p.startsWith(".stdo-builder/given/"))).toEqual([])
    expect(existsSync(`${ws.root}/.stdo-builder/local/question.md`)).toBe(false)
  })

  it("every node that an evaluation accepts has a resolution of yes in a ticket, naming the verdict, and its commit holds the content main holds", () => {
    const graph = methodGraph()
    for (const node of graph.graph.nodes.filter((n) => n.accepted?.includes("evaluation") === true).map((n) => n.name)) {
      // A verdict is recorded at each node its vector writes that an evaluation accepts, whoever wrote it (D164).
      const got = resolvedOnMain(ws, node, "evaluation").at(-1)
      expect(got, node).toBeDefined()
      const verdict = /; verdict ([^;]+)/.exec(got?.line ?? "")?.[1] ?? ""
      const holder = graph.graph.vectors.find((w) => w.evaluation?.verdict === verdict)
      expect(holder !== undefined && placedOf(graph, holder).writes.includes(node), node).toBe(true)
      expect(JSON.parse(ws.git(["show", `${got?.commit ?? ""}:./${verdict}`])).verdict, node).toBe("yes")
      for (const path of placesIn(ws).get(node) ?? []) expect(ws.git(["rev-parse", `${got?.commit ?? ""}:./${path}`]), `${node} ${path}`).toBe(ws.git(["rev-parse", `main:./${path}`]))
    }
  })
})
