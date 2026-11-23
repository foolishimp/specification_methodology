/**
 * QA-01, REQ-ALG-008: the protected files are in the trespass snapshot in both
 * folders. While the build's working session, which writes S1's code with its
 * design and tests (REQ-METHOD-006), is held at a stand-in gate, the
 * user changes by hand the governing graph on main (one workspace) and the
 * definition file in the ticket's checkout (another). Each change is returned
 * as trespass and the run stops. A run refused meanwhile only adds to the
 * event log, which is no trespass (S1).
 *
 * REQ-FLOW-005 step 3: the framework puts nothing back, and the next run goes
 * on from the workspace as it is.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-ALG-008 REQ-FLOW-005
 */
import { appendFileSync, readFileSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, gated, S1_FIXTURES, s1ToRequirements, temporary, until, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

interface Held {
  readonly ws: Workspace
  readonly ticket: string
  readonly stopped: Said
  readonly log: LogEntry[]
}

/** S1 up to the build step, whose working session waits at a gate while `byHand` changes the workspace. */
async function heldAtCode(cli: string, byHand: (ws: Workspace, ticket: string) => void): Promise<Held> {
  const ws = new Workspace(cli)
  const opens = join(temporary("stdo-builder-gate-"), "open")
  const fixtures = gated(opens)
  const ticket = (await s1ToRequirements(ws, fixtures)).ticket
  const running = ws.start(["run", ws.root, "--stand-in", fixtures])
  // The session has started once the stand-in has written its code; it then waits at the gate.
  await until(() => ws.read(".stdo-builder", "local", "checkouts", ticket, "build_tenants", "main", "code", "hello.sh") !== undefined, 60)
  byHand(ws, ticket)
  // A second run while the session is at work is refused, and adds to the event log as it is refused.
  const refused = await ws.run(fixtures)
  expect(refused.out).toContain("a run already works on every active ticket")
  write(opens, "")
  const stopped = await running.ended
  return { ws, ticket, stopped, log: ws.log() }
}

let graph: Held
let definition: Held
/** The run after the graph's trespass. */
let next: Said

beforeAll(async () => {
  const cli = build()
  ;[graph, definition] = await Promise.all([
    heldAtCode(cli, (ws) => {
      const path = ws.path(".stdo-builder", "graph.json")
      const g = JSON.parse(readFileSync(path, "utf8"))
      for (const n of g.nodes) if (n.name === "code") n.result = [...n.result, "The user changed this line by hand."]
      writeFileSync(path, `${JSON.stringify(g, null, 2)}\n`)
    }),
    heldAtCode(cli, (ws, ticket) => appendFileSync(ws.checkout(ticket, "stdo_hello.json"), "\n"))
  ])
  next = await graph.ws.run(S1_FIXTURES)
}, 180_000)

afterAll(clean)

describe("QA-01 the trespass snapshot holds the protected files of both folders", () => {
  it("a change to the governing graph on main during the session is returned, and the run stops", () => {
    expect(graph.stopped.code, graph.stopped.out).toBe(1)
    expect(graph.stopped.out).toContain("changed protected files")
    expect(graph.stopped.out).toContain(".stdo-builder/graph.json in the workspace's own folder")
    const ended = graph.log.filter((e) => e.event === "run ended" && e.ending === "stopped")
    expect(ended.map((e) => e.vector)).toEqual(["write-build"])
    expect(graph.log.some((e) => e.event === "vector closed" && e.vector === "write-build")).toBe(false)
    expect(graph.log.some((e) => e.event === "user asked" && e.vector === "write-build")).toBe(false)
  })

  it("a change to the definition file in the ticket's checkout is returned", () => {
    expect(definition.stopped.code, definition.stopped.out).toBe(1)
    expect(definition.stopped.out).toContain(`stdo_hello.json in the ticket's checkout, .stdo-builder/local/checkouts/${definition.ticket}`)
  })

  it("another run's entries added to the event log meanwhile are not returned", () => {
    expect(graph.stopped.out).not.toContain("events.log")
    const refused = graph.log.filter((e) => e.event === "run ended" && e.ending === "refused").map((e) => e.why)
    expect(refused).toEqual(["held"])
  })

  it("REQ-FLOW-005: the next run goes on from the workspace as it is", () => {
    expect(next.code, next.out).not.toBe(2)
    expect(next.out).not.toContain("refused")
  })

  it("the files are named by paths the user can open from the workspace's folder", () => {
    expect(definition.stopped.out).toContain(`The files: .stdo-builder/local/checkouts/${definition.ticket}/stdo_hello.json`)
  })
})
