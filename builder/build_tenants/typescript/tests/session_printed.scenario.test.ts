/**
 * Item 3 of the ticket `261120-9636-findings-of-the-first-use-on-itself`: what
 * a failed session printed is kept. The user sets up, writes S1's ticket and
 * starts a run. The stand-in's working session on the induction prints a line
 * and fails, at every attempt, so the run ends. The run names where what that
 * session printed is kept. The line is there, in the workspace, and is neither
 * in the event log nor in the history.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-001
 */
import { existsSync, readFileSync, rmSync, statSync } from "node:fs"
import { isAbsolute, join, relative } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, S1_TICKET, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

/** The line the session prints: words no other part of the scenario writes. */
const LINE = "the stand-in printed this line and then failed: 5d1c7e"

let ws: Workspace
let ticket = ""
let ran: Said
let log: readonly LogEntry[] = []
let logText = ""
let history = ""

/** Each path the words name that is a file of the workspace, from the workspace's folder or whole. */
const filesNamed = (words: string, root: string): string[] =>
  words
    .split(/\s+/)
    .map((w) => w.replace(/^[`'"(<]+/, "").replace(/[`'">),.;:]+$/, ""))
    .filter((w) => w.includes("/"))
    .map((w) => (isAbsolute(w) ? w : join(root, w)))
    .filter((p) => !relative(root, p).startsWith("..") && existsSync(p) && statSync(p).isFile())

beforeAll(async () => {
  const fixtures = fixturesLike((f) => {
    // The session writes nothing, so each attempt is a new session and each fails.
    rmSync(join(f, "induct-ticket", "work", "append"))
    write(join(f, "induct-ticket", "work", "print"), `${LINE}\n`)
    write(join(f, "induct-ticket", "work", "fails"), "")
  })
  ws = new Workspace(build())
  await ws.setup()
  ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
  ran = await ws.run(fixtures)
  log = ws.log()
  logText = ws.read(".stdo-builder", "local", "events.log") ?? ""
  history = ws.git(["log", "--all", "-p", "--format=%H%n%B"])
}, 120_000)

afterAll(clean)

describe("what a failed session printed is kept (the ticket's item 3)", () => {
  it("the session on the induction failed, and the run ended", () => {
    expect(ticket).not.toBe("")
    expect(log.filter((e) => e.event === "session failed").map((e) => e.vector)).toContain("induct-ticket")
    expect(log.filter((e) => e.event === "session returned" && e.vector === "induct-ticket")).toEqual([])
    const ended = log.filter((e) => e.event === "run ended")
    expect(ended, ran.out).toHaveLength(1)
    expect(ended[0]?.ending).toBe("stopped")
    expect(ran.code, ran.out).toBe(1)
  })

  it("the run names where what the session printed is kept, and the line is there, in the workspace", () => {
    const holding = filesNamed(ran.out, ws.root).filter((p) => readFileSync(p, "utf8").includes(LINE))
    expect(holding.length, ran.out).toBeGreaterThan(0)
  })

  it("the line is not in the event log", () => {
    expect(logText).not.toContain(LINE)
  })

  it("the line is not in the history", () => {
    expect(history).not.toBe("")
    expect(history).not.toContain(LINE)
  })
})
