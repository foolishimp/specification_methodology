/**
 * Scenario S12, the life of one ticket, on the workspace S1 left. The user
 * writes a ticket and starts a run; says no at the confirmation, with a
 * reason, starts a run and confirms. After accepting the requirements, the
 * user edits the ticket on main and starts a run, confirms, and a run builds
 * the requirements again. Then the user deletes the ticket and starts a run.
 * Asked where the work stands at each point, the framework gives the ticket's
 * state: in the backlog, waiting for the user, withdrawn.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-004 REQ-FLOW-006 REQ-ALG-012
 */
import { readFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, inducted, S1_FIXTURES, s1Whole, ticketFields, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const TICKET = "Hello also takes one option, --version, with which it prints its version and exits with code 0."
const EDITED = TICKET.replace("prints its version", "prints its version on one line")
const REASON = "The scope does not say where the version comes from: it is the one the product definition names."
const ANSWER = "- scope: one option, --version, which prints the version the product definition names\n"

/** The induction writes the triage and the term: the requirements and then the build. */
const INDUCTED = fixturesLike((f) => write(join(f, "induct-ticket", "work", "append"), inducted({ kind: "feature", klass: "requirement_reprice", enters: "requirements", ends: "code", scope: "one option, --version", term: ["write-requirements", "write-build"] })))
/** The induction after the no adds the line that answers the reason; the last line of a field is the ticket's (H5). */
const ANSWERED = fixturesLike((f) => write(join(f, "induct-ticket", "work", "append"), ANSWER))

let ws: Workspace
let ticket = ""
let s1Main = ""
let log: LogEntry[] = []
const said = new Map<string, Said>()
const shown = new Map<string, string>()
let afterNo = ""
let briefAfterNo: readonly string[] = []
/** What the place the packet names for the answer of no held when the session after the no ran. */
let keptNo = ""
let sessionsAt = new Map<string, readonly string[]>()

/** What main holds but the board, by path and identity. */
const mainButBoard = (w: Workspace): string => w.git(["ls-tree", "-r", "main"]).split("\n").filter((l) => l !== "" && !l.includes("\t.ai-workspace/")).join("\n")
/** The sessions started from the log entry at `from`, as `<vector> <kind>`. */
const sessionsFrom = (from: number): readonly string[] => ws.log().slice(from).filter((e) => e.event === "session started").map((e) => `${e.vector ?? ""} ${e.kind ?? ""}`)

beforeAll(async () => {
  ws = new Workspace(build())
  await s1Whole(ws, S1_FIXTURES)
  s1Main = mainButBoard(ws)
  ticket = /The ticket (\S+) is written/.exec((await ws.ticket(TICKET)).out)?.[1] ?? ""
  shown.set("backlog", (await ws.show()).out)
  const step = async (name: string, act: () => Promise<Said>): Promise<void> => {
    const from = ws.log().length
    said.set(name, await act())
    sessionsAt = new Map([...sessionsAt, [name, sessionsFrom(from)]])
  }
  await step("first", () => ws.run(INDUCTED))
  shown.set("waiting", (await ws.show()).out)
  await step("no", () => ws.answer("no", REASON))
  await step("again", () => ws.run(ANSWERED))
  afterNo = readFileSync(ws.checkout(ticket, ".ai-workspace", "tickets", "active", `${ticket}.md`), "utf8")
  briefAfterNo = readFileSync(ws.checkout(ticket, ".stdo-builder", "local", "briefs", "induct-ticket.work.md"), "utf8").split("\n")
  const at = /^- as it stands, the ticket: .*the user said no to it(?: \(in the ticket \S+ on the commit [0-9a-f]+\))?, with the reason at (.+?)(?:; |\.$)/.exec(briefAfterNo.find((l) => l.startsWith("- as it stands, the ticket: ")) ?? "")?.[1]
  keptNo = at === undefined ? "" : readFileSync(ws.checkout(ticket, at), "utf8")
  await step("confirmed", () => ws.answer("yes"))
  await step("requirements", () => ws.run(S1_FIXTURES))
  await step("accepted", () => ws.answer("yes"))
  // The user edits the active ticket's words on main, and commits.
  const onMain = ws.path(".ai-workspace", "tickets", "active", `${ticket}.md`)
  write(onMain, readFileSync(onMain, "utf8").replace(TICKET, EDITED))
  ws.git(["commit", "-qam", "the user edits the ticket"])
  await step("edited", () => ws.run(INDUCTED))
  await step("reconfirmed", () => ws.answer("yes"))
  await step("rebuilt", () => ws.run(S1_FIXTURES))
  // The user withdraws the ticket: deletes its file on main, and commits.
  ws.git(["rm", "-q", `.ai-workspace/tickets/active/${ticket}.md`])
  ws.git(["commit", "-qm", "the user withdraws the ticket"])
  await step("withdrawn", () => ws.run(S1_FIXTURES))
  shown.set("withdrawn", (await ws.show()).out)
  log = ws.log()
}, 480_000)

afterAll(clean)

describe("S12 the life of one ticket", () => {
  it("written, the ticket is in the backlog", () => {
    expect(ticket).not.toBe("")
    expect(shown.get("backlog")).toContain(`- ${ticket}: backlog`)
  })

  it("the first run inducts it and waits for the user to confirm it", () => {
    expect(said.get("first")?.code, said.get("first")?.out).toBe(0)
    expect(sessionsAt.get("first")).toEqual(["induct-ticket work"])
    expect(said.get("first")?.out).toContain("waits for your answer on induct-ticket")
    expect(shown.get("waiting")).toContain(`- ${ticket}: active, waits for your answer on induct-ticket`)
  })

  it("after the no, the ticket was inducted again: the session's packet names where the reason is kept, and what was added answers it", () => {
    expect(said.get("no")?.code, said.get("no")?.out).toBe(0)
    expect(sessionsAt.get("again")).toEqual(["induct-ticket work"])
    expect(keptNo).toContain(REASON)
    // What the session added ends the ticket but for the framework's part (REQ-FLOW-004).
    expect(afterNo.split("\n").filter((l) => !l.startsWith("- framework: ")).join("\n").endsWith(ANSWER)).toBe(true)
    expect(ticketFields(afterNo).get("scope")).toContain("the product definition names")
    expect(said.get("again")?.out).toContain("waits for your answer on induct-ticket")
  })

  it("confirmed, the run builds the requirements, which the user accepts", () => {
    expect(said.get("confirmed")?.code, said.get("confirmed")?.out).toBe(0)
    expect(sessionsAt.get("requirements")).toEqual(["write-requirements work"])
    expect(said.get("requirements")?.out).toContain("waits for your answer on write-requirements")
    expect(said.get("accepted")?.code, said.get("accepted")?.out).toBe(0)
  })

  it("after the edit on main, the ticket is taken as the user edited it, the user is asked to confirm it again, and the requirements are built again", () => {
    expect(said.get("edited")?.code, said.get("edited")?.out).toBe(0)
    expect(ws.git(["show", `stdo/${ticket}:.ai-workspace/tickets/active/${ticket}.md`])).toContain(EDITED)
    expect(sessionsAt.get("edited")).toEqual(["induct-ticket work"])
    expect(said.get("edited")?.out).toContain("waits for your answer on induct-ticket")
    expect(said.get("edited")?.out).toContain("The ticket changed after you confirmed it, and did not pass the induction's checks: ")
    expect(said.get("edited")?.out).toContain("the ticket's term composes (the ticket gives no term)")
    expect(said.get("reconfirmed")?.code, said.get("reconfirmed")?.out).toBe(0)
    expect(sessionsAt.get("rebuilt")).toEqual(["write-requirements work"])
    expect(said.get("rebuilt")?.out).toContain("waits for your answer on write-requirements")
  })

  it("after the ticket was deleted, the run is refused with nothing to build, and the ticket is withdrawn", () => {
    expect(said.get("withdrawn")?.code, said.get("withdrawn")?.out).toBe(2)
    expect(said.get("withdrawn")?.out).toContain("there is nothing to build")
    expect(sessionsAt.get("withdrawn")).toEqual([])
    expect(shown.get("withdrawn")).toContain("Withdrawn: ")
    expect(shown.get("withdrawn")).toContain(ticket)
    expect(shown.get("withdrawn")).not.toContain(`- ${ticket}:`)
  })

  it("main is as S1 left it, apart from the board, and the ticket's branch is still there", () => {
    expect(mainButBoard(ws)).toBe(s1Main)
    expect(ws.git(["rev-parse", "--verify", `stdo/${ticket}`]).trim()).not.toBe("")
    expect(log.filter((e) => e.event === "commit made" && e.ticket === ticket && e.vector !== undefined).length).toBeGreaterThan(0)
  })
})
