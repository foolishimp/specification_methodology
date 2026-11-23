/**
 * REQ-FLOW-005, "Where the step does not close", and REQ-PARAM-003: with one
 * attempt allowed, a working session leaves a check failing and the next
 * leaves none, and the evaluation is made. Only an evaluation's no is an
 * attempt, so the second working session is in the same attempt as the first.
 *
 * After set-up, the user allows the build one attempt in the workspace's
 * graph, then goes through S1 to the build. The build's first working session
 * writes code that fails the tests and waits at a gate. While it waits, the
 * driver gives the stand-in S1's code for the next session, then opens the
 * gate.
 *
 * @uses C14 C5 C6
 * @is REQ-FLOW-005 REQ-PARAM-003 REQ-VERIFY-002
 */
import { readFileSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, S1_FIXTURES, S1_TICKET, since, temporary, until, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const CODE = ["build_tenants", "main", "code", "hello.sh"] as const
const FAILING = "#!/bin/sh\n# Hello. Carries out REQ-HELLO-001.\nprintf 'hello\\n'\n"
const GRAPH = [".stdo-builder", "graph.json"] as const

let ws: Workspace
let ticket = ""
let ran: Said
let log: readonly LogEntry[] = []

beforeAll(async () => {
  ws = new Workspace(build())
  const gate = join(temporary("stdo-builder-gate-"), "open")
  const fixtures = fixturesLike((f) => {
    write(join(f, "write-build", "work", "files", ...CODE), FAILING)
    write(join(f, "write-build", "work", "gate"), `${gate}\n`)
  })
  await ws.setup()
  // The user allows the build one attempt, in the workspace's graph.
  const g = JSON.parse(ws.read(...GRAPH) ?? "") as { vectors: { name: string; attempts?: number }[] }
  const buildVector = g.vectors.find((v) => v.name === "write-build")
  if (buildVector === undefined) throw new Error("the graph has no write-build")
  buildVector.attempts = 1
  writeFileSync(ws.path(...GRAPH), `${JSON.stringify(g, null, 2)}\n`)
  ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
  await ws.run(fixtures)
  await ws.answer("yes")
  await ws.run(fixtures)
  await ws.answer("yes")
  const from = ws.log().length
  const running = ws.start(["run", ws.root, "--stand-in", fixtures])
  await until(() => ws.read(".stdo-builder", "local", "checkouts", ticket, ...CODE) === FAILING, 120)
  // The first session has written its code; the next writes S1's, which passes the tests.
  write(join(fixtures, "write-build", "work", "files", ...CODE), readFileSync(join(S1_FIXTURES, "write-build", "work", "files", ...CODE), "utf8"))
  write(gate, "")
  ran = await running.ended
  log = since(ws.log(), from)
}, 300_000)

afterAll(clean)

describe("REQ-FLOW-005: with one attempt allowed, a working session leaves a check failing and the next leaves none", () => {
  it("the build's working packet gives the one attempt the graph allows", () => {
    expect(readFileSync(ws.checkout(ticket, ".stdo-builder", "local", "briefs", "write-build.work.md"), "utf8")).toContain("- attempts: 1,")
  })

  it("the first working session leaves the tests failing and the second leaves none, so no evaluation is made between them", () => {
    expect(log.filter((e) => e.event === "check run" && e.vector === "write-build" && e.check === "the tests pass").map((e) => e.result)).toEqual(["no", "yes"])
  })

  it("the evaluation is made, and the user is asked: the second working session was in the same attempt", () => {
    const sessions = log.filter((e) => e.event === "session started" || e.event === "user asked").map((e) => `${e.vector ?? ""} ${e.kind ?? "asked"}`)
    expect(sessions).toEqual(["write-build work", "write-build work", "write-build evaluation", "write-build asked"])
    expect(ran.code, ran.out).toBe(0)
    expect(ran.out).toContain("waits for your answer on write-build")
  })
})
