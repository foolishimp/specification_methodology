/**
 * What changed among the branches, tags and stash and outside the workspace's
 * folder while a session worked, and the workspace's folder found on a branch that is not
 * the ticket's (findings G-9 and R-12; D228, D231). Every session is started
 * by the agent's command as a process of its own: the fixture agent.
 *
 * - In a repository of its own: while the induction's session works, a tag
 *   and a branch are made and main is moved by a commit that changes no file;
 *   the user then switches the workspace's folder to another branch and
 *   starts a run, puts it back, answers, and the specification's session
 *   switches it again.
 * - The cut at twenty: while a session works, 25 tags are made.
 * - S13: inside a larger repository, while the induction's session works, the
 *   user commits a file outside the folder on main, in a working tree of the
 *   user's own, which is named as committed on main while the session worked
 *   and asked nothing on (ticket 261125-083337-0fdf, item 7; D257), changes a
 *   second that git did not list, makes a tag and a
 *   branch, stashes a change to a third, and commits a fourth that git listed
 *   as changed before the session started, on the ticket's branch, which is
 *   named as committed while the session worked (bug item 7; D256); while the
 *   specification's session works, switches the folder to that branch; then a
 *   run is killed while the build's session works, and the ticket is built to
 *   its end, whose words name the fourth as taken into main.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-001 REQ-FLOW-003 REQ-FLOW-005 REQ-FLOW-008 REQ-PARAM-001
 */
import { execFileSync } from "node:child_process"
import { mkdirSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { fixtureAgent, type Fixed } from "./script_agent.js"
import { build, clean, S1_FIXTURES, S1_TICKET, temporary, until, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const USER = ["-c", "user.name=User", "-c", "user.email=user@example.com"]

interface Case {
  readonly ws: Workspace
  readonly agent: Fixed
  readonly ticket: string
}

async function begun(ws: Workspace): Promise<Case> {
  await ws.setup()
  const agent = fixtureAgent(ws, S1_FIXTURES)
  const ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
  return { ws, agent, ticket }
}

const tips = (c: Case): string => c.ws.git(["rev-parse", "main", `stdo/${c.ticket}`])
const inFolder = (c: Case, args: readonly string[]): string => execFileSync("git", ["-C", c.ws.path(), ...args], { encoding: "utf8", env: c.ws.env })

let own: { c: Case; first: Said; refused: Said; tipsBefore: string; tipsRefused: string; refusedLog: readonly LogEntry[]; switched: Said; switchedLog: readonly LogEntry[]; after: Said }
let many: Said
let inside: { c: Case; top: string; first: Said; switched: Said; after: Said; cut: Said; done: Said }

beforeAll(async () => {
  const cli = build()
  await Promise.all([
    (async () => {
      const c = await begun(new Workspace(cli))
      c.agent.does("induct-ticket.work", `git -C "$ROOT" tag a-tag-made-while-it-worked\ngit -C "$ROOT" branch a-branch-made-while-it-worked\ngit -C "$ROOT" branch -f main $(git -C "$ROOT" ${USER.join(" ")} commit-tree -p main -m "a commit that changes no file" "main^{tree}")\n`)
      const first = await c.ws.run("")
      inFolder(c, ["switch", "-q", "-c", "a-branch-of-the-user"])
      const tipsBefore = tips(c)
      const from = c.ws.log().length
      const refused = await c.ws.run("")
      const tipsRefused = tips(c)
      const refusedLog = c.ws.log().slice(from)
      inFolder(c, ["switch", "-q", `stdo/${c.ticket}`])
      await c.ws.answer("yes")
      c.agent.does("write-specification.work", "git switch -q -c switched-while-it-worked\n")
      const from2 = c.ws.log().length
      const switched = await c.ws.run("")
      const switchedLog = c.ws.log().slice(from2)
      inFolder(c, ["switch", "-q", `stdo/${c.ticket}`])
      const after = await c.ws.run("")
      own = { c, first, refused, tipsBefore, tipsRefused, refusedLog, switched, switchedLog, after }
    })(),
    (async () => {
      const c = await begun(new Workspace(cli))
      c.agent.does("induct-ticket.work", `for i in $(seq 1 25); do git -C "$ROOT" tag "tag-$i"; done\n`)
      many = await c.ws.run("")
    })(),
    (async () => {
      const ws = new Workspace(cli, undefined, ["apps", "product"])
      const top = ws.top
      const git = (args: readonly string[]): string => execFileSync("git", ["-C", top, ...args], { encoding: "utf8", env: ws.env })
      git(["init", "-q", "-b", "main"])
      for (const f of ["a.txt", "b.txt", "c.txt", "d.txt"]) write(join(top, f), `${f}\n`)
      mkdirSync(ws.root, { recursive: true })
      git(["add", "-A"])
      git([...USER, "commit", "-q", "-m", "the repository's own files"])
      const c = await begun(ws)
      // A file outside the folder that git lists as changed before the session starts.
      writeFileSync(join(top, "d.txt"), "d, changed before the session\n")
      c.agent.gate("induct-ticket.work")
      const running = ws.start(["run", ws.root])
      await until(() => c.agent.waiting("induct-ticket.work"), 60)
      // The folder is on the ticket's branch: the user commits on main in a working tree of their own, and removes it after (D239).
      const own = join(temporary("stdo-builder-own-"), "main")
      git(["worktree", "add", "-q", own, "main"])
      writeFileSync(join(own, "a.txt"), "a, committed by the user\n")
      execFileSync("git", ["-C", own, ...USER, "commit", "-q", "-m", "the user's commit outside the folder", "--", "a.txt"], { env: ws.env })
      git(["worktree", "remove", own])
      writeFileSync(join(top, "b.txt"), "b, left uncommitted\n")
      git(["tag", "the-users-tag"])
      git(["branch", "the-users-branch", `stdo/${c.ticket}`])
      writeFileSync(join(top, "c.txt"), "c, stashed\n")
      git(["stash", "push", "-q", "--", "c.txt"])
      // The user commits the file git listed as changed, where the repository's folder is: on the ticket's branch.
      git([...USER, "commit", "-q", "-m", "the user commits d", "--", "d.txt"])
      c.agent.open("induct-ticket.work")
      const first = await running.ended
      await ws.answer("yes")
      c.agent.gate("write-specification.work")
      const again = ws.start(["run", ws.root])
      await until(() => c.agent.waiting("write-specification.work"), 60)
      execFileSync("git", ["-C", ws.path(), "switch", "-q", "the-users-branch"], { env: ws.env })
      c.agent.open("write-specification.work")
      const switched = await again.ended
      execFileSync("git", ["-C", ws.path(), "switch", "-q", `stdo/${c.ticket}`], { env: ws.env })
      const after = await ws.run("")
      await ws.answer("yes")
      c.agent.gate("write-build.work")
      const killed = ws.start(["run", ws.root])
      await until(() => c.agent.waiting("write-build.work"), 60)
      killed.kill()
      await killed.ended
      c.agent.open("write-build.work")
      const cut = await ws.run("")
      // The ticket is built to its end: each question answered yes.
      let done = cut
      for (let n = 0; n < 4 && done.out.includes("waits for your answer"); n++) {
        await ws.answer("yes")
        done = await ws.run("")
      }
      inside = { c, top, first, switched, after, cut, done }
    })()
  ])
}, 600_000)

afterAll(clean)

describe("in a repository of its own (REQ-FLOW-001, G-9)", () => {
  it("a tag and a branch made and main moved by a commit that changes no file while a session works: the run names the three and asks nothing on them", () => {
    const { first } = own
    expect(first.code, first.out).toBe(0)
    expect(first.out).toContain("a-tag-made-while-it-worked (added)")
    expect(first.out).toContain("a-branch-made-while-it-worked (added)")
    expect(first.out).toContain("main (changed)")
    expect(first.out).toContain("it may have been the session or you")
    expect(first.out).toContain("waits for your answer on induct-ticket")
    expect(first.out).not.toContain("waits for your ruling")
  })

  it("the workspace's folder found on a branch that is not the ticket's: the run names that branch, starts nothing and commits nothing (REQ-FLOW-003)", () => {
    const { refused } = own
    expect(refused.code, refused.out).toBe(2)
    expect(refused.out).toContain("a-branch-of-the-user")
    expect(own.tipsRefused).toBe(own.tipsBefore)
    expect(own.refusedLog.some((e) => e.event === "session started" || e.event === "commit made")).toBe(false)
  })

  it("the workspace's folder switched to another branch while a session works: the run names it and stops, and commits nothing of the step (REQ-FLOW-005 step 3)", () => {
    const { switched, switchedLog } = own
    expect(switched.code, switched.out).toBe(1)
    expect(switched.out).toContain("switched-while-it-worked")
    const started = switchedLog.findIndex((e) => e.event === "session started")
    expect(switchedLog.slice(started).some((e) => e.event === "commit made" || e.event === "check run")).toBe(false)
  })

  it("once the user has put it back, the next run goes on", () => {
    expect(own.after.code, own.after.out).toBe(0)
    expect(own.after.out).toContain("waits for your answer on write-specification")
  })
})

describe("more than twenty things differ (REQ-PARAM-001, REQ-FLOW-001)", () => {
  it("twenty are named, with how many there are", () => {
    expect(many.code, many.out).toBe(0)
    expect(many.out).toContain("20 named of 25")
    expect(many.out.match(/tag-\d+ \(added\)/g)).toHaveLength(20)
  })
})

describe("S13 inside a larger repository (R-12, G-9)", () => {
  it("main's move, the second file, the tag, the branch and the stash are named as changed while the session worked, and nothing is asked on them", () => {
    const { first } = inside
    expect(first.code, first.out).toBe(0)
    for (const named of ["main (changed)", "b.txt outside the workspace's folder (changed)", "the-users-tag (added)", "the-users-branch (added)", "the stash (added)"]) expect(first.out).toContain(named)
    expect(first.out).toContain("waits for your answer on induct-ticket")
    expect(first.out).not.toContain("waits for your ruling")
  })

  it("bug item 7, REQ-FLOW-001: a file git did not list, changed while the session worked, is named as changed; one git listed as changed, committed then, is named as committed while the session worked", () => {
    const { first } = inside
    expect(first.out).toContain("b.txt outside the workspace's folder (changed)")
    expect(first.out).not.toContain("b.txt outside the workspace's folder (added)")
    expect(first.out).not.toContain("d.txt outside the workspace's folder")
    const committed = first.out.split("\n").find((l) => l.startsWith("While the session on induct-ticket worked, these files outside the workspace's folder were committed")) ?? ""
    expect(committed, first.out).toContain("d.txt (changed)")
    expect(committed).toContain("the ticket's merge takes what was committed there into main, the branch the ticket left")
    // The file committed on main, the one left uncommitted and the one stashed were not committed on the branch the folder is on.
    for (const f of ["a.txt", "b.txt", "c.txt"]) expect(committed).not.toContain(f)
  })

  it("ticket 261125-083337-0fdf item 7, REQ-FLOW-001, REQ-PARAM-001: the file the user committed on main outside the folder while the session worked is named as committed on main, by what happened to it; nothing is asked on it, and none holds the ticket", () => {
    const { first } = inside
    const onMain = first.out.split("\n").find((l) => l.startsWith("While the session on induct-ticket worked, these were committed on main, the branch the ticket left, outside the workspace's folder")) ?? ""
    expect(onMain, first.out).toContain("a.txt (changed)")
    expect(onMain).toContain("nothing is asked on them, and none of them holds the ticket")
    // Only a.txt was committed on main: the others were left uncommitted, stashed or committed on the ticket's branch.
    for (const f of ["b.txt", "c.txt", "d.txt"]) expect(onMain).not.toContain(f)
    expect(first.out.split("\n").filter((l) => l.startsWith("- ")).some((l) => l.includes("a.txt"))).toBe(false)
    expect(first.out).not.toContain("waits for your ruling")
  })

  it("the workspace's folder switched to the user's branch while a session works: the run names it and goes no further; the next run, the folder put back, goes on", () => {
    expect(inside.switched.code, inside.switched.out).toBe(1)
    expect(inside.switched.out).toContain("the-users-branch")
    expect(inside.after.code, inside.after.out).toBe(0)
    expect(inside.after.out).toContain("waits for your answer on write-specification")
  })

  it("the files outside the folder are as the user left them: the committed one on main, the second uncommitted, the third's change in the stash", () => {
    const git = (args: readonly string[]): string => execFileSync("git", ["-C", inside.top, ...args], { encoding: "utf8" })
    expect(git(["show", "main:a.txt"])).toBe("a, committed by the user\n")
    expect(git(["status", "--porcelain", "--", "b.txt"]).trim()).toBe("M b.txt")
    expect(git(["stash", "list"]).trim().split("\n")).toHaveLength(1)
  })

  it("after a run killed while its session worked, the next run says it cannot tell what changed among the branches, tags and stash, nor outside the workspace's folder (REQ-FLOW-003)", () => {
    expect(inside.cut.out).toContain("cannot tell what changed then among the repository's branches, tags and stash, nor outside the workspace's folder")
  })

  it("REQ-FLOW-008 step 2: the words that say the ticket is done name the file the user committed while the session worked as taken into main, and not the one main held already, the one left uncommitted or the one stashed", () => {
    const { done } = inside
    expect(done.code, done.out).toBe(0)
    expect(done.out).toContain(`The work on the ticket ${inside.c.ticket} is done`)
    const taken = done.out.split("\n").find((l) => l.startsWith("The merge took these files outside the workspace's folder into main")) ?? ""
    expect(taken, done.out).toContain("d.txt (changed)")
    for (const f of ["a.txt", "b.txt", "c.txt"]) expect(taken).not.toContain(f)
    const git = (args: readonly string[]): string => execFileSync("git", ["-C", inside.top, ...args], { encoding: "utf8" })
    expect(git(["show", "main:d.txt"])).toBe("d, changed before the session\n")
  })
})
