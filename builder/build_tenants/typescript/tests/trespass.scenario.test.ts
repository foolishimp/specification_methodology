/**
 * REQ-ALG-008: what changed while a session worked is compared in the
 * workspace's folder. While the build's working session, which writes S1's
 * code with its design and tests (REQ-METHOD-006), is held at a stand-in gate,
 * the user changes by hand the governing graph and the definition file. Each
 * is named to the user and the run waits for the ruling. A run refused meanwhile only adds to
 * the event log, which git ignores and is not named (S1).
 *
 * REQ-FLOW-005 step 3, REQ-FLOW-006: the framework puts nothing back; the next
 * run without a ruling asks again, and after a yes commits what stands.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-ALG-008 REQ-FLOW-005 REQ-FLOW-006
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
  await until(() => ws.read("build_tenants", "main", "code", "hello.sh") !== undefined, 60)
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
/** The run after the graph changed, before the user rules; the main and branch tips then; the run after the user's yes. */
let next: Said
let tipsBefore = ""
let tipsAfterNext = ""
let graphAfterNext = ""
let ruled: Said
let afterYes: Said

beforeAll(async () => {
  const cli = build()
  ;[graph, definition] = await Promise.all([
    heldAtCode(cli, (ws) => {
      const path = ws.path(".stdo-builder", "graph.json")
      const g = JSON.parse(readFileSync(path, "utf8"))
      for (const n of g.nodes) if (n.name === "code") n.result = [...n.result, "The user changed this line by hand."]
      writeFileSync(path, `${JSON.stringify(g, null, 2)}\n`)
    }),
    heldAtCode(cli, (ws, ticket) => appendFileSync(ws.path("stdo_hello.json"), "\n"))
  ])
  const tips = (): string => graph.ws.git(["rev-parse", "main", `stdo/${graph.ticket}`])
  tipsBefore = tips()
  next = await graph.ws.run(S1_FIXTURES)
  tipsAfterNext = tips()
  graphAfterNext = graph.ws.git(["show", `stdo/${graph.ticket}:.stdo-builder/graph.json`])
  ruled = await graph.ws.answer("yes")
  afterYes = await graph.ws.run(S1_FIXTURES)
}, 240_000)

afterAll(clean)

describe("what changed while a session worked, in the workspace's folder (REQ-ALG-008, REQ-FLOW-005, REQ-FLOW-006)", () => {
  it("a change to the governing graph during the session is named, and the run waits for the user's ruling", () => {
    expect(graph.stopped.code, graph.stopped.out).toBe(0)
    expect(graph.stopped.out).toContain("waits for your ruling on what changed while the session on write-build worked")
    expect(graph.stopped.out).toContain(".stdo-builder/graph.json (changed)")
    expect(graph.stopped.out).toContain("it may have been the session or you")
    const ended = graph.log.filter((e) => e.event === "run ended")
    expect(ended.at(-1)?.ending).toBe("waiting")
    expect(ended.at(-1)?.vector).toBe("write-build")
    expect(graph.log.some((e) => e.event === "vector closed" && e.vector === "write-build")).toBe(false)
    expect(graph.log.filter((e) => e.event === "user asked" && e.vector === "write-build").map((e) => e.named)).toEqual([1])
  })

  it("a change to the definition file is named, by a path the user can open from the workspace's folder", () => {
    expect(definition.stopped.code, definition.stopped.out).toBe(0)
    expect(definition.stopped.out).toContain(`stdo_hello.json (changed)`)
  })

  it("another run's entries added to the event log meanwhile are not named", () => {
    expect(graph.stopped.out).not.toContain("events.log")
    const refused = graph.log.filter((e) => e.event === "run ended" && e.ending === "refused").map((e) => e.why)
    expect(refused).toEqual(["held"])
  })

  it("the next run, before the user has ruled, asks again and commits nothing on the ticket's branch or on main (REQ-FLOW-003 step 1, C-2, C-18)", () => {
    expect(next.code, next.out).toBe(0)
    expect(next.out).toContain("waits for your ruling on what changed while the session on write-build worked")
    expect(next.out).toContain(".stdo-builder/graph.json (changed)")
    expect(tipsAfterNext).toBe(tipsBefore)
    expect(graphAfterNext).not.toContain("The user changed this line by hand.")
  })

  it("after the user's yes, the next run commits the change as it stands, on the ticket's branch (REQ-FLOW-006)", () => {
    expect(ruled.code, ruled.out).toBe(0)
    expect(graph.ws.read(".ai-workspace", "tickets", "active", `${graph.ticket}.md`)).toContain("- framework: ruled yes on what changed at write-build: .stdo-builder/graph.json ")
    expect(afterYes.out).not.toContain("waits for your ruling")
    expect(afterYes.out).not.toContain("refused")
    expect(graph.ws.git(["show", `stdo/${graph.ticket}:.stdo-builder/graph.json`])).toContain("The user changed this line by hand.")
  })
})
