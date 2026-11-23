/**
 * One event log, and the ticket as the work order (D202 to D205): S1 to the
 * specification, then the build asked on with the log deleted, an answer
 * refused after the asset changed, a no with its reason and a ruling, and a
 * yes. Judged from the workspace and the log it leaves.
 *
 * @uses C14 C5 C6 C10
 * @is REQ-FLOW-001 REQ-FLOW-004 REQ-FLOW-005 REQ-FLOW-006 REQ-FLOW-007 REQ-ALG-004 REQ-ALG-007 REQ-ALG-012
 */
import { appendFileSync, existsSync, readFileSync, rmSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, S1_FIXTURES, s1ToRequirements, write, Workspace, type LogEntry, type Said } from "./scenario_driver.js"

let ws: Workspace
let ticket = ""
let withoutLog: Said
let asked: Said
let askedWithoutLog: Said
let changedThenAnswered: Said
let refusedNo: Said
let ruledNo: Said
let ticketText = ""
let briefAfterRuling = ""
let last: Said
let log: LogEntry[] = []
const CODE = "build_tenants/main/code/hello.sh"

/** The build's working session after the user's no answers it: the code in fewer lines, as the ruling asks. */
const answeringTheNo = (): string =>
  fixturesLike((f) => write(join(f, "write-build", "work", "files", ...CODE.split("/")), "#!/bin/sh\n# Hello. Carries out REQ-HELLO-001, in fewer lines.\nprintf 'hello, world\\n'\n"))

beforeAll(async () => {
  ws = new Workspace(build())
  ticket = (await s1ToRequirements(ws, S1_FIXTURES)).ticket
  const folder = ws.path()
  rmSync(ws.path(".stdo-builder", "local", "events.log"))
  withoutLog = await ws.command(["show", folder])
  asked = await ws.run(S1_FIXTURES)
  rmSync(ws.path(".stdo-builder", "local", "events.log"))
  askedWithoutLog = await ws.command(["show", folder])
  // The asset asked on changes after the question and before the answer.
  appendFileSync(ws.checkout(ticket, CODE), "# changed by hand\n")
  changedThenAnswered = await ws.command(["answer", folder, "yes"])
  ws.git(["-C", ws.checkout(ticket), "checkout", "--", CODE])
  refusedNo = await ws.command(["answer", folder, "no"])
  ruledNo = await ws.command(["answer", folder, "no", "--reason", "it is too large", "--ruling", "keep every file under ten lines"])
  const after = answeringTheNo()
  await ws.run(after)
  briefAfterRuling = readFileSync(ws.checkout(ticket, ".stdo-builder", "local", "briefs", "write-build.work.md"), "utf8")
  await ws.command(["answer", folder, "yes"])
  ticketText = readFileSync(ws.checkout(ticket, ".ai-workspace", "tickets", "active", `${ticket}.md`), "utf8")
  last = await ws.run(after)
  log = ws.log()
}, 300_000)

afterAll(clean)

describe("REQ-ALG-012: show reads the event log, the ticket and the workspace, and no other record", () => {
  it("without the event log, it says so, and for a ticket that waits on neither the user nor its induction, that a run finds what it waits on", () => {
    expect(withoutLog.out).toContain("not found")
    expect(withoutLog.out).toContain("a run finds what it waits on")
  })
  it("REQ-ALG-012 acceptance 7: with the event log deleted, it gives what a ticket waiting for the user's answer is asked, from the ticket, with when it was asked", () => {
    expect(asked.out).toContain("waits for your answer on write-build")
    expect(askedWithoutLog.out).toContain("waits for your answer on write-build, as the ticket shows (written at ")
    expect(askedWithoutLog.out).toContain("asked:")
    expect(askedWithoutLog.out).toContain("Do you accept")
  })
})

describe("REQ-FLOW-006: the answer reads the ticket alone", () => {
  it("the asset asked on is changed after the question and before the answer: the answer is refused, and says that a run asks again", () => {
    expect(changedThenAnswered.code).toBe(2)
    expect(changedThenAnswered.out).toContain("Start a run, and you are asked again")
  })
  it("an answer of no comes with the user's reason", () => {
    expect(refusedNo.code).toBe(2)
    expect(ruledNo.code).toBe(0)
  })
  it("a ruling given with an answer is named in the brief of every later session on the ticket (REQ-ALG-007)", () => {
    expect(briefAfterRuling).toContain("the context this session starts from; the rulings in it bind this session")
    expect(briefAfterRuling).not.toContain("keep every file under ten lines")
  })
})

describe("REQ-FLOW-004: the ticket holds the checklist, the resolutions and the rulings, each with its commit", () => {
  it("each line names a commit git holds, and the ticket copies no finding and nothing a session printed", () => {
    const lines = ticketText.split("\n").filter((l) => l.startsWith("- framework: "))
    expect(lines.some((l) => /^- framework: delivered write-build for the user's decision at [0-9a-f]{40} \(/.test(l))).toBe(true)
    expect(lines.some((l) => /^- framework: resolved user no at code on [0-9a-f]{40}; reason it is too large$/.test(l))).toBe(true)
    expect(lines.some((l) => /^- framework: ruling on [0-9a-f]{40}: keep every file under ten lines$/.test(l))).toBe(true)
    expect(lines.some((l) => /^- framework: resolved user yes at code on [0-9a-f]{40}$/.test(l))).toBe(true)
    const verdict = lines.find((l) => /^- framework: resolved evaluation yes at design on [0-9a-f]{40}; verdict \S+; findings \S+$/.test(l))
    expect(verdict).toBeDefined()
    for (const l of lines) for (const c of l.match(/[0-9a-f]{40}/g) ?? []) expect(ws.git(["cat-file", "-t", c]).trim(), l).toBe("commit")
    // REQ-FLOW-005: git gives, under the commit the evaluation's resolution names, the content it judged.
    const commit = /on ([0-9a-f]{40})/.exec(verdict ?? "")?.[1] ?? ""
    expect(ws.git(["show", `${commit}:./build_tenants/main/evaluations/build/verdict.json`])).toContain("yes")
    expect(ticketText).not.toContain("What the checks of")
  })
  it("the framework adds lines to its part of a confirmed ticket: the confirmation still stands, and the user is not asked to confirm it again", () => {
    const lines = ticketText.split("\n")
    const confirmed = lines.findIndex((l) => /^- framework: resolved user yes at induct-ticket on [0-9a-f]{40}$/.test(l))
    expect(confirmed, ticketText).toBeGreaterThanOrEqual(0)
    expect(lines.slice(confirmed + 1).filter((l) => l.startsWith("- framework: ")).length).toBeGreaterThan(0)
    // The log since it was last deleted covers the runs that added those lines: none asked on the induction or started its session.
    expect(log.filter((e) => e.event === "user asked").map((e) => e.vector)).not.toContain("induct-ticket")
    expect(log.some((e) => e.event === "session started" && e.vector === "induct-ticket")).toBe(false)
  })
  it("the work then ends as S1 does", () => {
    expect(last.code).toBe(0)
    expect(ws.board().done).toContain(ticket)
  })
  it("REQ-FLOW-001: no file of the framework's but the tickets holds a resolution, and none holds a reading of a ticket or a question", () => {
    for (const folder of [ws.path(), ws.checkout(ticket)]) {
      for (const record of [[".stdo-builder", "answers"], [".stdo-builder", "given"], [".stdo-builder", "local", "found", "snapshot.json"], [".stdo-builder", "local", "question.md"]]) {
        expect(existsSync(join(folder, ...record)), join(folder, ...record)).toBe(false)
      }
    }
  })
})

describe("REQ-FLOW-007: the log holds the entries and details the user named", () => {
  const one = (event: string): LogEntry | undefined => log.find((e) => e.event === event)
  it("a run started with the release in force; a session with its command and the commit it starts from, and where what it printed is kept", () => {
    expect(one("run started")?.release).toBeDefined()
    const started = one("session started")
    expect(started?.command?.length ?? 0).toBeGreaterThan(0)
    expect(started?.commit).toMatch(/^[0-9a-f]{40}$/)
    expect(log.find((e) => e.event === "session returned")?.printed).toMatch(/printed/)
  })
  it("a check run with how long it took; a verdict read with what it says and where its findings are; an answer with the ticket that holds it", () => {
    expect(log.filter((e) => e.event === "check run").every((e) => typeof e.seconds === "number" && e.result !== undefined)).toBe(true)
    expect(one("verdict read")?.findings).toBeDefined()
    expect(one("answer written")?.path).toContain(ticket)
    expect(log.filter((e) => e.event === "commit made").every((e) => typeof e.commit === "string" && e.why !== undefined)).toBe(true)
  })
})
