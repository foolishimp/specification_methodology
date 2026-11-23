/**
 * The first item of the ticket `261120-c4a1-findings-of-the-calculus-build`
 * (F9): a run that cannot write its first or its last entry of the event log
 * ends as one of the four endings, and not with the exit code of a fault. The
 * fault is the log left read-only, as the user or another program may leave
 * it.
 *
 * The first entry: after set-up and a ticket, the log is left read-only and a
 * run is started. It cannot write `run started`. The run ends as refused, with
 * the refused ending's exit code, and its words name the log and say what the
 * user does next. The log holds nothing of it. The user makes the log
 * writable again and starts a run, and that run goes on.
 *
 * The last entry: S1 is run to the build step, whose working session waits at
 * a gate. The log is left read-only and the gate is opened. The run cannot
 * write `session returned`, so it reaches the stopped ending, at the build's
 * vector. It cannot write `run ended` either. It keeps the ending it reached,
 * since the log changes no decision, and its words say the event log could
 * not be written. The user makes the log writable again and starts a run, and
 * that run goes on.
 *
 * @uses C14 C5 C6
 * @is REQ-FLOW-003 REQ-FLOW-007
 */
import { chmodSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, gated, S1_FIXTURES, S1_TICKET, s1ToRequirements, since, temporary, until, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

/** The place of the event log in a workspace, as its words may name it. */
const LOG = /\.stdo-builder\/local\/events\.log/
const logOf = (ws: Workspace): string => ws.path(".stdo-builder", "local", "events.log")

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
  const from = ws.log().length
  chmodSync(logOf(ws), 0o444)
  refused = await ws.run(S1_FIXTURES)
  chmodSync(logOf(ws), 0o644)
  log = since(ws.log(), from)
  again = await ws.run(S1_FIXTURES)

  const gate = join(temporary("stdo-builder-gate-"), "open")
  const fixtures = gated(gate)
  atStep = new Workspace(program)
  ticket = (await s1ToRequirements(atStep, fixtures)).ticket
  const fromStep = atStep.log().length
  const running = atStep.start(["run", atStep.root, "--stand-in", fixtures])
  await until(() => atStep.log().some((e) => e.event === "session started" && e.vector === "write-build" && e.kind === "work"), 60)
  chmodSync(logOf(atStep), 0o444)
  write(gate, "")
  stopped = await running.ended
  chmodSync(logOf(atStep), 0o644)
  stepLog = since(atStep.log(), fromStep)
  goesOn = await atStep.run(fixtures)
}, 360_000)

afterAll(clean)

describe("a run that cannot write its first entry ends as refused (F9)", () => {
  it("the run ends as refused before any step, with the refused ending's exit code", () => {
    expect(refused.code, refused.out).toBe(2)
    expect(refused.out).toContain("The run is refused before any step")
  })

  it("its words name the event log and say what the user does next", () => {
    expect(refused.out).toMatch(LOG)
    expect(refused.out).toContain("start a run again")
  })

  it("the event log holds nothing of the run", () => {
    expect(log, JSON.stringify(log)).toEqual([])
  })

  it("with the log writable again, a run started again goes on", () => {
    expect(again.code, again.out).toBe(0)
    expect(again.out).toContain("waits for your answer on induct-ticket")
  })
})

describe("a run that cannot write its last entry keeps the ending it reached (F9)", () => {
  it("the run ends as stopped at write-build, with the stopped ending's exit code", () => {
    expect(stopped.code, stopped.out).toBe(1)
    expect(stopped.out).toContain(`The run stopped on the ticket ${ticket}, at write-build`)
  })

  it("its words say the event log could not be written, and what the user does next", () => {
    expect(stopped.out).toMatch(new RegExp(`the event log could not be written at \\S*${LOG.source}`, "i"))
    expect(stopped.out).toContain("start a run again")
  })

  it("the event log holds the run up to the start of the build's session, and no later entry", () => {
    const started = stepLog.filter((e) => e.event === "run started")
    expect(started.length, JSON.stringify(stepLog)).toBe(1)
    const of = stepLog.filter((e) => e.run === started[0]?.run)
    const last = of.at(-1)
    expect({ event: last?.event, vector: last?.vector, kind: last?.kind }, JSON.stringify(of)).toEqual({ event: "session started", vector: "write-build", kind: "work" })
    expect(of.some((e) => e.event === "run ended")).toBe(false)
  })

  it("with the log writable again, a run started again goes on", () => {
    expect(goesOn.code, goesOn.out).toBe(0)
    expect(goesOn.out).toContain("waits for your answer on write-build")
  })
})
