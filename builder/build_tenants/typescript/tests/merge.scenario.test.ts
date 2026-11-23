/**
 * QA-04, REQ-FLOW-004 and REQ-FLOW-008: a run never commits an unresolved
 * merge or a file with conflict markers.
 *
 * One workspace: once the user has confirmed the induction, they edit the
 * active ticket's words on main. The next run takes the ticket as the user
 * edited it, places it again and asks to confirm it again; no commit holds a
 * conflict marker.
 *
 * Another: the user writes, by hand on main, the requirements the ticket's
 * branch has also written. Git cannot merge them; the run stops naming the
 * file and the checkout, and the next run stops again without committing
 * anything. Once the user resolves the file in the checkout, the run goes on,
 * whether they wrote it anew or kept the branch's side.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-004 REQ-FLOW-008
 */
import { execFileSync } from "node:child_process"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, S1_FIXTURES, S1_TICKET, s1ToRequirements, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const EDITED = S1_TICKET.replace("hello, world", "hello, builder")
/** Every file, in any commit of the workspace, that holds a line git writes to mark a conflict. */
const markers = (ws: Workspace): string => {
  const commits = ws.git(["rev-list", "--all"]).split("\n").filter((l) => l !== "")
  try {
    return ws.git(["grep", "-l", "-E", "^(<<<<<<<|>>>>>>>)( |$)", ...commits])
  } catch {
    return ""
  }
}

let edited: { ws: Workspace; ticket: string; ran: Said; log: LogEntry[] }
let conflict: { ws: Workspace; ticket: string; first: Said; second: Said; third: Said; commits: string[] }
let kept: typeof conflict

beforeAll(async () => {
  const cli = build()
  const one = async () => {
    const ws = new Workspace(cli)
    await ws.setup()
    const ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
    await ws.run(S1_FIXTURES)
    await ws.answer("yes")
    const path = ws.path(".ai-workspace", "tickets", "active", `${ticket}.md`)
    write(path, (ws.read(".ai-workspace", "tickets", "active", `${ticket}.md`) ?? "").replace(S1_TICKET, EDITED))
    ws.git(["commit", "-qam", "the user edits the ticket"])
    const from = ws.log().length
    const ran = await ws.run(S1_FIXTURES)
    return { ws, ticket, ran, log: ws.log().slice(from) }
  }
  const two = async (resolve: "anew" | "ours") => {
    const ws = new Workspace(cli)
    const { ticket } = await s1ToRequirements(ws, S1_FIXTURES)
    write(ws.path("specification", "requirements", "HELLO.md"), "# Hello, by hand\n\nWritten on main by the user.\n")
    ws.git(["add", "-A"])
    ws.git(["commit", "-qm", "the user writes the requirements on main"])
    const first = await ws.run(S1_FIXTURES)
    const tip = ws.git(["rev-parse", `stdo/${ticket}`]).trim()
    const second = await ws.run(S1_FIXTURES)
    const commits = [tip, ws.git(["rev-parse", `stdo/${ticket}`]).trim()]
    const checkout = ws.checkout(ticket)
    // The user resolves the file and stages it, without a commit: written anew, or kept as the branch has it.
    if (resolve === "anew") write(ws.checkout(ticket, "specification", "requirements", "HELLO.md"), "# Hello\n\nREQ-HELLO-001: run with no arguments, the program prints hello, world and exits with code 0.\n")
    else execFileSync("git", ["-C", checkout, "checkout", "--ours", "specification/requirements/HELLO.md"], { env: ws.env })
    execFileSync("git", ["-C", checkout, "add", "specification/requirements/HELLO.md"], { env: ws.env })
    const third = await ws.run(S1_FIXTURES)
    return { ws, ticket, first, second, third, commits }
  }
  ;[edited, conflict, kept] = await Promise.all([one(), two("anew"), two("ours")])
}, 240_000)

afterAll(clean)

describe("QA-04 an active ticket the user edited on main", () => {
  it("is taken as the user edited it, with no conflict", () => {
    expect(edited.ran.out).not.toContain("could not merge")
    const onBranch = edited.ws.git(["show", `stdo/${edited.ticket}:.ai-workspace/tickets/active/${edited.ticket}.md`])
    expect(onBranch).toContain(EDITED)
    expect(onBranch).not.toContain(S1_TICKET)
    expect(markers(edited.ws)).toBe("")
  })

  it("is inducted again and the user is asked to confirm it again", () => {
    expect(edited.log.filter((e) => e.event === "session started").map((e) => e.vector)).toEqual(["induct-ticket"])
    expect(edited.ran.code, edited.ran.out).toBe(0)
    expect(edited.ran.out).toContain("The run waits for your answer on induct-ticket")
  })
})

describe("QA-04 a file git cannot merge", () => {
  it("stops the run, naming the file and the checkout", () => {
    expect(conflict.first.code, conflict.first.out).toBe(1)
    expect(conflict.first.out).toContain("git could not merge specification/requirements/HELLO.md")
  })

  it("keeps the run stopped, with nothing committed, until the user resolves it", () => {
    expect(conflict.second.code, conflict.second.out).toBe(1)
    expect(conflict.second.out).toContain("specification/requirements/HELLO.md")
    expect(conflict.second.out).toContain(`.stdo-builder/local/checkouts/${conflict.ticket}`)
    expect(conflict.commits[1]).toBe(conflict.commits[0])
    expect(markers(conflict.ws)).toBe("")
  })

  it("goes on once the user has resolved it in the checkout", () => {
    expect(conflict.third.out).not.toContain("could not merge")
    expect(conflict.third.out).not.toContain("not resolved")
    expect(markers(conflict.ws)).toBe("")
  })

  it("goes on too where the user kept the branch's side, so nothing differs from the branch but the merge itself", async () => {
    expect(kept.third.out).not.toContain("could not merge")
    expect(kept.third.out).not.toContain("would not take main")
    expect(await kept.ws.gitSays(["merge-base", "--is-ancestor", "main", `stdo/${kept.ticket}`])).toBe(0)
    expect(markers(kept.ws)).toBe("")
  })
})
