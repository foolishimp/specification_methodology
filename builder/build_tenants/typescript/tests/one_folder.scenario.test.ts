/**
 * A ticket is built in the workspace's own folder, on a branch of its own
 * (REQ-FLOW-001, REQ-FLOW-003, REQ-FLOW-004, REQ-FLOW-008, REQ-ALG-004,
 * REQ-ALG-008, REQ-ALG-012). Each case is one a release that built a ticket in
 * a checkout of its own did otherwise.
 *
 * - S1 built from a branch of the user's, `dev`: no checkout is made and no
 *   working tree is added; the ticket records `dev` as the branch it left, and
 *   is merged into `dev` and no other, by a commit of the branch's whole tree
 *   with both parents, with no file written; while `dev` is checked out in
 *   another working tree, the merge is refused, naming it (bug items 1 and 2).
 *   A working tree of the user's own, whose folder is away while the ticket is
 *   built and merged, is still known to git when the folder is back (bug item
 *   5, R-11).
 * - The folder put on main while a ticket is active: the run, the answer and
 *   a ticket are refused, naming both branches, and `show` answers and says
 *   so; the folder on no branch with no ticket active: the run is refused.
 * - Inside a larger repository, main changes a file outside the folder in
 *   which the user has work not committed: main is not taken in, and the run
 *   names the file (item 4 of what follows from one folder).
 * - A clone that has the ticket's branch only as a remote branch: the run
 *   makes the local branch at the remote branch's commit, asks the question
 *   the workspace cloned waits on and starts no session; a clone with no such
 *   branch is refused (bug item 4, G-5).
 * - An answer of the user's no longer stands where main, taken in after it,
 *   changed a file of its node, though the file holds what it held (R-9).
 *   On the code: main holds the code's file as the branch does before the
 *   user's yes; after it main changes the file, the next run takes it in, a
 *   working session writes the file back as it was at the yes, and the user is
 *   asked on the code again, with the ticket not merged.
 * - The user's yes taken out of the ticket, and `show` writing nothing (bug
 *   items 8 and 9): `one_folder_cases.scenario.test.ts`.
 *
 * @uses C13 C14
 * @is REQ-FLOW-001 REQ-FLOW-003 REQ-FLOW-004 REQ-FLOW-007 REQ-FLOW-008 REQ-ALG-004 REQ-ALG-008 REQ-ALG-012 REQ-VERIFY-002
 */
import { execFileSync } from "node:child_process"
import { existsSync, mkdirSync, readFileSync, renameSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, S1_FIXTURES, S1_TICKET, s1ToRequirements, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const ticketOf = (said: Said): string => /The ticket (\S+) is written/.exec(said.out)?.[1] ?? ""

let dev: { ws: Workspace; ticket: string; mainBefore: string; devBefore: string; elsewhere: Said; done: Said; worktreesBefore: string; worktreesAfter: string; log: LogEntry[]; mine: string; knownAfter: string; heldAsItWas: readonly string[]; pulledAt: { commit: string; subject: string } }
let off: { ws: Workspace; ticket: string; run: Said; answer: Said; written: Said; show: Said; detached: Said; detachedKept: boolean; quiet: boolean; tipsKept: boolean; mine: string; done: Said }
let outside: { ws: Workspace; ticket: string; run: Said; branchBefore: string; branchAfter: string }
let clone: { ws: Workspace; ticket: string; asked: Said; run: Said; log: LogEntry[]; local: string; remote: string; fromMain: boolean; bare: Said; bareBranches: string }
let r9: { ws: Workspace; ticket: string; run: Said }
let code: { ws: Workspace; ticket: string; asked: Said; answered: Said; run: Said; log: LogEntry[]; atYes: string }

beforeAll(async () => {
  const cli = build()
  const onDev = async () => {
    const ws = new Workspace(cli)
    await ws.setup()
    const mainBefore = ws.git(["rev-parse", "main"]).trim()
    ws.git(["switch", "-q", "-c", "dev"])
    // A working tree of the user's own, whose folder is away while the ticket is built and merged (R-11).
    const mine = join(ws.top, "..", `${ws.top.split("/").pop()}-mine`)
    ws.git(["worktree", "add", "-q", "-b", "mine", mine])
    renameSync(mine, `${mine}-away`)
    const worktreesBefore = ws.git(["worktree", "list", "--porcelain"]).split("\n").filter((l) => l.startsWith("worktree ")).join("\n")
    const ticket = ticketOf(await ws.ticket(S1_TICKET))
    ws.git(["add", "-A"])
    ws.git(["commit", "-qm", "the user's ticket"])
    let pulledAt = { commit: "", subject: "" }
    for (let i = 0; i < 3; i++) {
      await ws.run(S1_FIXTURES)
      // Until the merge, dev stays at the commit that moved the ticket to the active lane.
      if (i === 0) pulledAt = { commit: ws.git(["rev-parse", "dev"]).trim(), subject: ws.git(["log", "-1", "--format=%s", "dev"]).trim() }
      await ws.answer("yes")
    }
    const devBefore = ws.git(["rev-parse", "dev"]).trim()
    // dev checked out in another working tree: the merge is refused, naming it.
    const other = join(ws.top, "..", `${ws.top.split("/").pop()}-dev`)
    ws.git(["worktree", "add", "-q", other, "dev"])
    const folderBefore = ws.git(["rev-parse", "HEAD"]).trim()
    const elsewhere = await ws.run(S1_FIXTURES)
    // The branch left, the folder and the other working tree, as they were.
    const heldAsItWas = [ws.git(["rev-parse", "dev"]).trim() === devBefore, ws.git(["rev-parse", "HEAD"]).trim() === folderBefore, ws.git(["-C", other, "rev-parse", "HEAD"]).trim() === devBefore, ws.git(["-C", other, "status", "--porcelain"]) === ""].map(String)
    ws.git(["worktree", "remove", "--force", other])
    const done = await ws.run(S1_FIXTURES)
    const worktreesAfter = ws.git(["worktree", "list", "--porcelain"]).split("\n").filter((l) => l.startsWith("worktree ")).join("\n")
    renameSync(`${mine}-away`, mine)
    const knownAfter = ws.git(["worktree", "list", "--porcelain"])
    ws.git(["worktree", "remove", "--force", mine])
    return { ws, ticket, mainBefore, devBefore, elsewhere, done, worktreesBefore, worktreesAfter, log: ws.log(), mine, knownAfter, heldAsItWas, pulledAt }
  }
  const offBranch = async () => {
    const ws = new Workspace(cli)
    await ws.setup()
    const ticket = ticketOf(await ws.ticket(S1_TICKET))
    await ws.run(S1_FIXTURES)
    // The user puts the folder on a branch of their own and commits there (R-1).
    ws.git(["switch", "-q", "-c", "mine"])
    write(ws.path("mine.txt"), "the user's own work\n")
    ws.git(["add", "mine.txt"])
    ws.git(["commit", "-qm", "the user's own commit"])
    const tips = (): string => ws.git(["rev-parse", "main", `stdo/${ticket}`, "mine"])
    const tipsBefore = tips()
    const from = ws.log().length
    const run = await ws.run(S1_FIXTURES)
    const answer = await ws.answer("yes")
    const written = await ws.ticket("Another change.")
    const show = await ws.show()
    const quiet = !ws.log().slice(from).some((e) => e.event === "session started" || e.event === "commit made")
    const tipsKept = tips() === tipsBefore
    const mine = ws.git(["rev-parse", "mine"]).trim()
    // The user puts the folder back on the ticket's branch: the ticket goes on, and is merged into the branch it left.
    ws.git(["switch", "-q", `stdo/${ticket}`])
    await ws.answer("yes")
    for (let i = 0; i < 2; i++) {
      await ws.run(S1_FIXTURES)
      await ws.answer("yes")
    }
    const done = await ws.run(S1_FIXTURES)
    // A workspace with no ticket active, its folder on no branch.
    const bare = new Workspace(cli)
    await bare.setup()
    bare.git(["switch", "-q", "--detach"])
    await bare.ticket(S1_TICKET)
    const detached = await bare.run(S1_FIXTURES)
    const detachedKept = bare.board().active.length === 0 && !bare.log().some((e) => e.event === "ticket pulled")
    return { ws, ticket, run, answer, written, show, detached, detachedKept, quiet, tipsKept, mine, done }
  }
  const outsideFolder = async () => {
    const ws = new Workspace(cli, undefined, ["product"])
    execFileSync("git", ["init", "-q", "-b", "main", ws.top], { env: ws.env })
    write(join(ws.top, "notes.txt"), "the user's notes\n")
    execFileSync("git", ["-C", ws.top, "add", "-A"], { env: ws.env })
    execFileSync("git", ["-C", ws.top, "commit", "-qm", "the repository's own file"], { env: ws.env })
    mkdirSync(ws.root, { recursive: true })
    await ws.setup()
    await ws.ticket(S1_TICKET)
    await ws.run(S1_FIXTURES)
    // The setup's own ticket is built first; its branch is the one the folder is on.
    const ticket = ws.git(["branch", "--show-current"]).trim().replace(/^stdo\//, "")
    await ws.answer("yes")
    ws.onMain(() => {
      write(join(ws.top, "notes.txt"), "main's notes\n")
      execFileSync("git", ["-C", ws.top, "commit", "-qam", "main changes the notes"], { env: ws.env })
    })
    write(join(ws.top, "notes.txt"), "the user's notes, not committed\n")
    const branchBefore = ws.git(["rev-parse", `stdo/${ticket}`]).trim()
    const run = await ws.run(S1_FIXTURES)
    return { ws, ticket, run, branchBefore, branchAfter: ws.git(["rev-parse", `stdo/${ticket}`]).trim() }
  }
  const cloned = async () => {
    const ws = new Workspace(cli)
    await ws.setup()
    const ticket = ticketOf(await ws.ticket(S1_TICKET))
    const asked = await ws.run(S1_FIXTURES)
    // A clone of the workspace, on main, whose active ticket waits for the user's answer on its induction.
    const there = new Workspace(cli)
    execFileSync("git", ["clone", "-q", "--branch", "main", ws.root, there.root], { env: there.env })
    const run = await there.run(S1_FIXTURES)
    const tip = (name: string): string => there.git(["rev-parse", name]).trim()
    const remote = tip(`origin/stdo/${ticket}`)
    // A branch made from main, as release 3.2.0 made one, does not hold the remote branch's commit.
    const fromMain = (await there.gitSays(["merge-base", "--is-ancestor", remote, `stdo/${ticket}`])) !== 0
    // A clone with main alone: the repository has no branch of the ticket, local or remote.
    const bare = new Workspace(cli)
    execFileSync("git", ["clone", "-q", "--single-branch", "--branch", "main", ws.root, bare.root], { env: bare.env })
    const refused = await bare.run(S1_FIXTURES)
    return { ws: there, ticket, asked, run, log: there.log(), local: tip(`stdo/${ticket}`), remote, fromMain, bare: refused, bareBranches: bare.git(["branch", "--list", "stdo/*"]).trim() }
  }
  const answerMoved = async () => {
    const ws = new Workspace(cli)
    const { ticket } = await s1ToRequirements(ws, S1_FIXTURES)
    const path = "specification/requirements/HELLO.md"
    const same = ws.git(["show", `stdo/${ticket}:${path}`])
    // Main gets the file the branch wrote, as the branch holds it: the node's content is as it was at the answer.
    ws.onMain(() => {
      write(ws.path(path), same)
      ws.git(["add", "-A"])
      ws.git(["commit", "-qm", "the user writes the requirements on main, as the branch has them"])
    })
    const run = await ws.run(S1_FIXTURES)
    return { ws, ticket, run }
  }
  const codeMoved = async () => {
    const ws = new Workspace(cli)
    const { ticket } = await s1ToRequirements(ws, S1_FIXTURES)
    const path = "build_tenants/main/code/hello.sh"
    const written = readFileSync(join(S1_FIXTURES, "write-build", "work", "files", ...path.split("/")), "utf8")
    // Main holds the code's file as the build will write it, so the branch and main share it once main is taken in.
    ws.onMain(() => {
      write(ws.path(path), written)
      ws.git(["add", "-A"])
      ws.git(["commit", "-qm", "the user writes the code's file on main, as the build writes it"])
    })
    const asked = await ws.run(S1_FIXTURES)
    const answered = await ws.answer("yes")
    const atYes = ws.git(["show", `stdo/${ticket}:${path}`])
    // After the user's yes on the code, a commit on main changes that file.
    ws.onMain(() => {
      write(ws.path(path), "echo main's own\n")
      ws.git(["add", "-A"])
      ws.git(["commit", "-qm", "the user changes the code's file on main"])
    })
    const from = ws.log().length
    const run = await ws.run(S1_FIXTURES)
    return { ws, ticket, asked, answered, run, log: ws.log().slice(from), atYes }
  }
  ;[dev, off, outside, clone, r9, code] = await Promise.all([onDev(), offBranch(), outsideFolder(), cloned(), answerMoved(), codeMoved()])
}, 600_000)

afterAll(clean)

describe("bug items 1 and 2: S1 built from the user's branch dev", () => {
  it("makes no checkout and adds no working tree (REQ-FLOW-001)", () => {
    expect(existsSync(dev.ws.path(".stdo-builder", "local", "checkouts"))).toBe(false)
    expect(dev.worktreesAfter).toBe(dev.worktreesBefore)
  })
  it("records dev as the branch the ticket left, and names it in the pull (REQ-FLOW-004, REQ-FLOW-007)", () => {
    expect(dev.ws.read(".ai-workspace", "tickets", "completed", `${dev.ticket}.md`)).toContain("- framework: left dev")
    expect(dev.log.find((e) => e.event === "ticket pulled")).toMatchObject({ main: "dev", branch: `stdo/${dev.ticket}` })
    // The ticket's branch was made from the commit that moved the ticket to the active lane on dev.
    expect(dev.pulledAt.subject).toBe(`board: ${dev.ticket} to active`)
    expect(dev.ws.git(["rev-list", "--first-parent", `stdo/${dev.ticket}`]).split("\n")).toContain(dev.pulledAt.commit)
    expect(dev.ws.git(["rev-list", "--first-parent", dev.devBefore]).split("\n")).toContain(dev.pulledAt.commit)
  })
  it("refuses the merge while dev is checked out in another working tree, naming it, and merges nothing (REQ-FLOW-008)", () => {
    expect(dev.elsewhere.out, dev.elsewhere.out).toContain("is checked out in another working tree")
    expect(dev.elsewhere.out).toContain("-dev")
    // No session of the run started: the run is refused (REQ-FLOW-008).
    expect(dev.elsewhere.code).toBe(2)
    expect(dev.heldAsItWas).toEqual(["true", "true", "true", "true"])
  })
  it("bug item 5, R-11: a working tree of the user's own, whose folder was away while the ticket was built and merged, is still known to git when the folder is back (REQ-FLOW-001)", () => {
    expect(dev.done.code, dev.done.out).toBe(0)
    expect(dev.knownAfter).toContain(`worktree ${dev.mine}\n`)
    expect(dev.knownAfter).toContain("branch refs/heads/mine")
    expect(dev.knownAfter).not.toContain("prunable")
  })
  it("merges into dev and no other, by a commit of the branch's whole tree with both parents, with the folder on dev and nothing left to commit (REQ-FLOW-008)", () => {
    expect(dev.done.code, dev.done.out).toBe(0)
    expect(dev.done.out).toContain("merged into dev")
    const git = (args: string[]) => dev.ws.git(args).trim()
    expect(git(["rev-parse", "main"])).toBe(dev.mainBefore)
    expect(git(["rev-parse", "dev^1"])).toBe(dev.devBefore)
    expect(git(["rev-parse", "dev^2"])).toBe(git(["rev-parse", `stdo/${dev.ticket}`]))
    expect(git(["rev-parse", "dev^{tree}"])).toBe(git(["rev-parse", `stdo/${dev.ticket}^{tree}`]))
    expect(git(["symbolic-ref", "--short", "HEAD"])).toBe("dev")
    expect(git(["status", "--porcelain"])).toBe("")
    expect(dev.log.find((e) => e.event === "ticket merged")).toMatchObject({ main: "dev" })
  })
})

describe("the folder not on the active ticket's branch (REQ-FLOW-001, REQ-FLOW-003, REQ-ALG-012)", () => {
  const both = (said: Said): void => {
    expect(said.out, said.out).toContain(`stdo/${off.ticket}`)
    expect(said.out).toContain("on the branch mine")
  }
  it("refuses the run, naming both branches", () => {
    expect(off.run.code).toBe(2)
    both(off.run)
  })
  it("starts and commits nothing while the folder is on the user's branch", () => {
    expect(off.quiet).toBe(true)
    expect(off.tipsKept).toBe(true)
  })
  it("R-1: once the user has put the folder back, the ticket goes on and is merged into the branch it left, once, and into no other", () => {
    expect(off.done.code, off.done.out).toBe(0)
    expect(off.done.out).toContain("merged into main, the branch it left")
    const merges = off.ws.git(["log", "--merges", "--format=%s", "main"]).split("\n").filter((l) => l.startsWith(`merge stdo/${off.ticket}:`))
    expect(merges).toHaveLength(1)
    expect(off.ws.git(["rev-parse", "mine"]).trim()).toBe(off.mine)
    expect(off.ws.git(["branch", "--contains", "main", "--format=%(refname:short)"]).trim().split("\n")).toEqual(["main"])
  })
  it("refuses the answer and a ticket, naming both branches", () => {
    expect(off.answer.code).toBe(2)
    both(off.answer)
    expect(off.written.code).toBe(2)
    both(off.written)
  })
  it("REQ-ALG-012 acceptance 11: show still answers, and says so", () => {
    expect(off.show.code).toBe(0)
    both(off.show)
    expect(off.show.out).toContain(`A run and an answer are refused, and so is every command that writes in the workspace, until the folder is back on stdo/${off.ticket}`)
  })
  it("with no ticket active and the folder on no branch, refuses the run", () => {
    expect(off.detached.code).toBe(2)
    expect(off.detached.out).toContain("on no branch")
    expect(off.detachedKept).toBe(true)
  })
})

describe("item 4 of what follows from one folder: main changed a file outside the folder in which the user has work not committed (REQ-FLOW-008)", () => {
  it("takes nothing in and names the file", () => {
    // No session of the run started: the run is refused (REQ-FLOW-008).
    expect(outside.run.code, outside.run.out).toBe(2)
    expect(outside.run.out).toContain("notes.txt")
    expect(outside.branchAfter).toBe(outside.branchBefore)
    expect(readFileSync(join(outside.ws.top, "notes.txt"), "utf8")).toBe("the user's notes, not committed\n")
  })
})

describe("bug item 4, G-5: a clone of a workspace whose active ticket waits for the user's answer (REQ-FLOW-003)", () => {
  const question = (said: Said): string => said.out.split("\n").find((l) => l.startsWith("Is the ticket inducted as you want it?")) ?? ""
  it("with the ticket's branch only as a remote branch: the run makes the local branch at the remote branch's commit and puts the folder on it", () => {
    expect(clone.run.code, clone.run.out).toBe(0)
    expect(clone.ws.git(["symbolic-ref", "--short", "HEAD"]).trim()).toBe(`stdo/${clone.ticket}`)
    // The local branch holds the remote branch's commit; on it, the run adds what a second run on the workspace cloned adds: the question delivered again in the ticket.
    expect(clone.fromMain).toBe(false)
    const added = clone.ws.git(["log", "--format=%s", `${clone.remote}..stdo/${clone.ticket}`]).trim().split("\n")
    expect(added).toHaveLength(1)
    expect(added[0]).toMatch(new RegExp(`^ticket ${clone.ticket}: the user is asked, at [0-9a-f]{12}$`))
    expect(clone.ws.git(["diff", "--name-only", clone.remote, `stdo/${clone.ticket}`]).trim()).toBe(`.ai-workspace/tickets/active/${clone.ticket}.md`)
  })
  it("asks the question the workspace cloned waits on, starts no session to induct the ticket, and pulls nothing", () => {
    expect(clone.run.out).toContain("The run waits for your answer on induct-ticket")
    expect(question(clone.run)).not.toBe("")
    expect(question(clone.run)).toBe(question(clone.asked))
    expect(clone.log.filter((e) => e.event === "session started")).toEqual([])
    expect(clone.log.filter((e) => e.event === "ticket pulled")).toEqual([])
  })
  it("with no branch of the ticket at all: the run is refused, says so, and makes no branch", () => {
    expect(clone.bare.code, clone.bare.out).toBe(2)
    expect(clone.bare.out).toContain(`the repository has no branch of it, stdo/${clone.ticket}, local or remote`)
    expect(clone.bareBranches).toBe("")
  })
})

describe("R-9, REQ-ALG-004 acceptance 7: an answer main changed the node of, taken in after it", () => {
  it("no longer stands: the user is asked again on write-specification", () => {
    expect(r9.run.code, r9.run.out).toBe(0)
    expect(r9.run.out).toContain("The run waits for your answer on write-specification")
  })
})

describe("REQ-FLOW-008, REQ-ALG-004: the user's yes on the code, then a commit on main that changes a file of the code", () => {
  it("after main is taken in, a working session writes the file back as it was at the yes, the user is asked on the code again, and the ticket is not merged", () => {
    expect(code.asked.out).toContain("The run waits for your answer on write-build")
    expect(code.answered.code, code.answered.out).toBe(0)
    expect(code.log.filter((e) => e.event === "main taken in").map((e) => e.result)).toContain("merged")
    expect(code.log.filter((e) => e.event === "session started").map((e) => e.vector)).toContain("write-build")
    expect(code.ws.git(["show", `stdo/${code.ticket}:build_tenants/main/code/hello.sh`])).toBe(code.atYes)
    expect(code.run.code, code.run.out).toBe(0)
    expect(code.run.out).toContain("The run waits for your answer on write-build")
    expect(code.log.some((e) => e.event === "ticket merged")).toBe(false)
    expect(code.ws.git(["ls-tree", "--name-only", "main", `.ai-workspace/tickets/active/${code.ticket}.md`]).trim()).not.toBe("")
  })
})
