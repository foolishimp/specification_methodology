/**
 * The gap in one form (REQ-ALG-007, D177). On the workspace S1 left, the user
 * changes the accepted product definition by hand and starts a run, accepts
 * the change, and a run builds what depends on it. Then the user rewords the
 * requirements and does the same. Every packet states, for each node its
 * session writes or judges, the node as it stands, what is recorded at it and
 * what that was given on that differs now, by the identity git holds it under
 * as it was. The stand-in has only the sessions the framework should start; a
 * session it should not start finds no fixed files, fails, and shows in the
 * log.
 *
 * @uses C14 C5 C6
 * @is REQ-ALG-007 REQ-FLOW-005
 */
import { readFileSync, rmSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, S1_FIXTURES, s1Whole, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const VECTORS = ["induct-ticket", "write-specification", "write-build", "write-intent", "write-product", "write-requirements", "write-design", "write-tests", "write-code"]
/** The S1 fixtures with only the sessions named. */
const only = (sessions: readonly string[]): string => fixturesLike((f) => {
  for (const v of VECTORS) for (const kind of ["work", "evaluation"]) if (!sessions.includes(`${v}/${kind}`)) rmSync(join(f, v, kind), { recursive: true, force: true })
})

const PRODUCT = ["specification", "PRODUCT.md"] as const
const HELLO = ["specification", "requirements", "HELLO.md"] as const

let ws: Workspace
let first = ""
let productWas = ""
let requirementsWas = ""
let requirementsOnMain = ""
const tickets: string[] = []
const said: Said[] = []
const logs: LogEntry[][] = []

/** The lines of a packet a session of the ticket was given. */
const packet = (ticket: string, name: string): readonly string[] =>
  readFileSync(ws.checkout(ticket, ".stdo-builder", "local", "briefs", name), "utf8").split("\n")
const standing = (lines: readonly string[]): readonly string[] => lines.filter((l) => l.startsWith("- as it stands, "))
/** The identity a line names for what changed, and what `git show` gives for it in the ticket's checkout. */
const shown = (ticket: string, line: string, suffix = ""): { readonly id: string; readonly out: string } => {
  const id = /as it was: `git show ([0-9a-f]+)`/.exec(line)?.[1] ?? ""
  return { id, out: ws.git(["-C", ws.checkout(ticket), "show", `${id}${suffix}`]) }
}
const sessions = (log: readonly LogEntry[]) => log.filter((e) => e.event === "session started").map((e) => `${e.vector ?? ""} ${e.kind ?? ""}`)
const asked = (log: readonly LogEntry[]) => log.filter((e) => e.event === "user asked").map((e) => e.vector)
const newDone = (): string => ws.board().done.find((t) => t !== first && !tickets.includes(t)) ?? ""

beforeAll(async () => {
  ws = new Workspace(build())
  first = (await s1Whole(ws, S1_FIXTURES)).ticket
  productWas = ws.read(...PRODUCT) ?? ""
  requirementsWas = ws.read(...HELLO) ?? ""
  // The user changes the accepted product definition by hand.
  write(ws.path(...PRODUCT), `${productWas}\nIt is for anyone who wants to see that a terminal works.\n`)
  const requirements = only(["write-requirements/work"])
  let from = ws.log().length
  said.push(await ws.run(requirements), await ws.answer("yes"), await ws.run(requirements), await ws.answer("yes"), await ws.run(requirements))
  logs.push(ws.log().slice(from))
  tickets.push(newDone())
  requirementsOnMain = ws.git(["rev-parse", "main:specification/requirements"]).trim()
  // The user rewords the requirements by hand.
  write(ws.path(...HELLO), requirementsWas.replace("prints the line", "writes the line"))
  const judged = only(["write-design/evaluation", "write-tests/evaluation", "write-code/evaluation"])
  from = ws.log().length
  said.push(await ws.run(judged), await ws.answer("yes"), await ws.run(judged), await ws.answer("yes"), await ws.run(judged))
  logs.push(ws.log().slice(from))
  tickets.push(newDone())
}, 360_000)

afterAll(clean)

describe("REQ-ALG-007 acceptance 8: on an empty workspace, every packet states the gap in its one form", () => {
  it("the working packet for the specification has each node not there, with nothing recorded at it", () => {
    const lines = packet(first, "write-specification.work.md")
    expect(lines.some((l) => l.startsWith("- gap: the work is the gap between each asset as it stands"))).toBe(true)
    expect(standing(lines)).toEqual(["intent", "product", "requirements"].map((n) => `- as it stands, ${n}: not there; nothing is recorded at it.`))
  })

  it("the evaluating packet for the build has each node it judges there, with nothing recorded at it yet", () => {
    const lines = standing(packet(first, "write-build.evaluation.md"))
    expect(lines.length).toBeGreaterThan(0)
    for (const l of lines) expect(l).toMatch(/^- as it stands, \w+: there; nothing is recorded at it\.$/)
  })
})

describe("REQ-ALG-007 acceptance 9: a change flows through what depends on it, and the packet carries the accepted base", () => {
  it("each run and answer after the product definition changed ended well, and the ticket was merged", () => {
    expect(said.slice(0, 5).map((s) => s.code), said.slice(0, 5).map((s) => s.out).join("\n---\n")).toEqual([0, 0, 0, 0, 0])
    expect(tickets[0]).not.toBe("")
  })

  it("the user was asked on the product definition and then on the requirements, and the one session was the requirements' work", () => {
    expect(asked(logs[0] ?? [])).toEqual(["write-product", "write-requirements"])
    expect(sessions(logs[0] ?? [])).toEqual(["write-requirements work"])
  })

  it("the requirements' working packet names the user's yes and the product definition as it was, which git shows in the checkout", () => {
    const lines = standing(packet(tickets[0] ?? "", "write-requirements.work.md"))
    expect(lines).toHaveLength(1)
    expect(lines[0]).toMatch(/^- as it stands, requirements: there; the user said yes to it \(in the ticket \S+ on the commit [0-9a-f]{40}\); changed since: product \(as it was: `git show [0-9a-f]+`\)\.$/)
    expect(shown(tickets[0] ?? "", lines[0] ?? "").out).toBe(productWas)
  })

  it("the requirements are left as they were, and nothing below them was reopened", () => {
    expect(requirementsOnMain).toBe(ws.git(["rev-parse", `stdo/${first}:specification/requirements`]).trim())
    expect(sessions(logs[0] ?? []).some((s) => /^write-(design|tests|code) /.test(s))).toBe(false)
  })

  it("after the requirements were reworded, the user was asked on them, the nodes below them were judged again and no working session was started", () => {
    expect(said.slice(5).map((s) => s.code), said.slice(5).map((s) => s.out).join("\n---\n")).toEqual([0, 0, 0, 0, 0])
    expect(tickets[1]).not.toBe("")
    expect(asked(logs[1] ?? [])).toEqual(["write-requirements", "write-code"])
    expect([...sessions(logs[1] ?? [])].sort()).toEqual(["write-code evaluation", "write-design evaluation", "write-tests evaluation"])
  })

  it("the design's evaluating packet names the evaluation's yes and the requirements as they were, which git shows in the checkout", () => {
    const lines = standing(packet(tickets[1] ?? "", "write-design.evaluation.md"))
    expect(lines).toHaveLength(1)
    expect(lines[0]).toMatch(/^- as it stands, design: there; the evaluation said yes to it \(in the ticket \S+ on the commit [0-9a-f]{40}\); changed since: requirements \(as it was: `git show [0-9a-f]+`\)\.$/)
    const { id } = shown(tickets[1] ?? "", lines[0] ?? "")
    expect(id).toBe(requirementsOnMain)
    expect(shown(tickets[1] ?? "", lines[0] ?? "", ":HELLO.md").out).toBe(requirementsWas)
  })
})
