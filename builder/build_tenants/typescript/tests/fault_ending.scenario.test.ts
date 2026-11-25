/**
 * The ticket's second item (QA-13): a run that meets a fault ends as one of
 * the four endings, with what the user does next, and the event log holds its
 * ending. Each fault is git's lock left on an index, as another git at work
 * there leaves it.
 *
 * Before any step: after set-up and a ticket, the lock is left on main's
 * index and a run is started. git refuses the run's commit on main. The run
 * ends as refused, with the refused ending's exit code. The user does what the
 * words say, removes the lock and starts a run again, and that run goes on.
 *
 * After a step has started: S1 is run to the build step, whose working
 * session, once it has written its files, waits at a gate. The lock is left
 * on the workspace's folder's own index and the gate is opened, so git refuses
 * the step's commit. The run ends as stopped, naming the build's vector, with
 * the stopped ending's exit code. The user removes the lock and starts a run
 * again, and that run goes on.
 *
 * @uses C14 C5 C6
 * @is REQ-FLOW-003
 */
import { rmSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, gated, S1_FIXTURES, S1_TICKET, s1ToRequirements, since, temporary, until, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

let ws: Workspace
let refused: Said
let again: Said
let log: readonly LogEntry[] = []

let atStep: Workspace
let ticket = ""
let stopped: Said
let goesOn: Said
let stepLog: readonly LogEntry[] = []

beforeAll(async () => {
  const program = build()

  ws = new Workspace(program)
  await ws.setup()
  await ws.ticket(S1_TICKET)
  const lock = ws.path(".git", "index.lock")
  write(lock, "")
  const from = ws.log().length
  refused = await ws.run(S1_FIXTURES)
  log = since(ws.log(), from)
  rmSync(lock)
  again = await ws.run(S1_FIXTURES)

  const gate = join(temporary("stdo-builder-gate-"), "open")
  const fixtures = gated(gate)
  atStep = new Workspace(program)
  ticket = (await s1ToRequirements(atStep, fixtures)).ticket
  const fromStep = atStep.log().length
  const running = atStep.start(["run", atStep.root, "--stand-in", fixtures])
  await until(() => atStep.read("build_tenants", "main", "code", "hello.sh") !== undefined, 60)
  const ownIndex = atStep.git(["-C", atStep.path(), "rev-parse", "--path-format=absolute", "--git-path", "index"]).trim()
  const stepLock = `${ownIndex}.lock`
  write(stepLock, "")
  write(gate, "")
  stopped = await running.ended
  stepLog = since(atStep.log(), fromStep)
  rmSync(stepLock)
  goesOn = await atStep.run(fixtures)
}, 360_000)

afterAll(clean)

describe("a fault ends the run as one of the four endings (QA-13)", () => {
  it("the run ends as refused before any step, with the refused ending's exit code", () => {
    expect(refused.code, refused.out).toBe(2)
    expect(refused.out).toContain("The run is refused before any step")
  })

  it("its words say what git refused and what the user does next", () => {
    expect(refused.out).toContain("git refused")
    expect(refused.out).toContain("index.lock")
    expect(refused.out).toContain("start a run again")
  })

  it("the event log holds the run's ending", () => {
    const started = log.filter((e) => e.event === "run started")
    expect(started.length, JSON.stringify(log)).toBe(1)
    const ended = log.filter((e) => e.event === "run ended" && e.run === started[0]?.run)
    expect(ended.length, JSON.stringify(log)).toBe(1)
    expect(ended[0]?.ending).toBe("refused")
    expect(ended[0]?.why).toContain("git refused")
    expect(log.some((e) => e.event === "session started")).toBe(false)
  })

  it("with the lock removed, a run started again goes on", () => {
    expect(again.code, again.out).toBe(0)
    expect(again.out).toContain("waits for your answer on induct-ticket")
  })
})

describe("a fault after a step has started ends the run as stopped, naming the vector (QA-13)", () => {
  it("the run ends as stopped at write-build, with the stopped ending's exit code", () => {
    expect(stopped.code, stopped.out).toBe(1)
    expect(stopped.out).toContain(`The run stopped on the ticket ${ticket}, at write-build`)
  })

  it("its words say what git refused and what the user does next", () => {
    expect(stopped.out).toContain("git refused")
    expect(stopped.out).toContain("index.lock")
    expect(stopped.out).toContain("start a run again")
  })

  it("the event log holds the run's ending", () => {
    const started = stepLog.filter((e) => e.event === "run started")
    expect(started.length, JSON.stringify(stepLog)).toBe(1)
    const ended = stepLog.filter((e) => e.event === "run ended" && e.run === started[0]?.run)
    expect(ended.length, JSON.stringify(stepLog)).toBe(1)
    expect(ended[0]?.ending).toBe("stopped")
    expect(ended[0]?.vector).toBe("write-build")
    expect(ended[0]?.why).toContain("git refused")
  })

  it("with the lock removed, a run started again goes on", () => {
    expect(goesOn.code, goesOn.out).toBe(0)
    expect(goesOn.out).toContain("waits for your answer on write-build")
  })
})
