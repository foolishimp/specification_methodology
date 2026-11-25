/**
 * More cases of a ticket built in the workspace's own folder, each driven
 * through the command-line program with the stand-in agent, as the user would
 * (REQ-FLOW-001, REQ-FLOW-003, REQ-ALG-008, REQ-ALG-012). Each is one release
 * 3.2.0, which built a ticket in a checkout of its own, did otherwise.
 *
 * - A checkout release 3.2.0 left holds the active ticket's branch, which
 *   records no branch it left: the run is refused, names the checkout and
 *   gives the command that removes it; once the user has removed it, the next
 *   run goes on (bug item 6, R-16); so too where the user deleted the
 *   checkout's folder and git still records it.
 * - The folder put on the branch the ticket left while the ticket's branch is
 *   checked out in another working tree: the run is refused, names both
 *   branches and that working tree, and gives the command that removes it.
 * - Two products in one repository: while one holds an active ticket, a run
 *   of the other is refused and names the branch the folder is on.
 * - A run killed while the build's session works, after it wrote its files
 *   and the user wrote a file the step does not write: the next run asks on
 *   the user's file alone and, after the yes, commits both as the step's
 *   result; with that session's identities removed, it asks on both, and
 *   commits neither as the user's change by hand (REQ-FLOW-003 step 1).
 * - The user says yes to a file a session wrote, and then takes the ruling's
 *   line out of the ticket: the next run names the file again (bug item 8);
 *   and `show` writes nothing (bug item 9).
 * - S1 inside a larger repository is merged while the user has a file outside
 *   the folder uncommitted, one staged and one untracked: each is as it was,
 *   no file's time changes but the ticket's own, and the folder is on main
 *   (REQ-FLOW-008).
 * - Inside a larger repository, git cannot take main into the ticket's branch
 *   for a file outside the folder; the user resolves it and stages it, and the
 *   next run completes that merge with both parents (REQ-FLOW-008).
 * - Inside a larger repository, a run starts while the user has a merge of
 *   their own under way, of a branch that changed a file outside the folder:
 *   on main with no ticket active, merged and not committed, or left unmerged;
 *   and on the active ticket's branch, left unmerged. The run goes on, the
 *   merge stays under way as the user left it, and no commit of the
 *   framework's completes it or changes a file outside the folder
 *   (REQ-FLOW-001, REQ-FLOW-003 step 1).
 *
 * @uses C13 C14
 * @is REQ-FLOW-001 REQ-FLOW-003 REQ-FLOW-006 REQ-FLOW-008 REQ-ALG-008 REQ-ALG-012 REQ-VERIFY-002
 */
import { execFileSync } from "node:child_process"
import { existsSync, mkdirSync, readdirSync, readFileSync, rmSync, statSync } from "node:fs"
import { basename, join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, gated, S1_FIXTURES, S1_TICKET, s1ToRequirements, temporary, until, Workspace, write, wroteAll, type Said } from "./scenario_driver.js"

const ticketOf = (said: Said): string => /The ticket (\S+) is written/.exec(said.out)?.[1] ?? ""
const BY_HAND = "--grep=^what the user changed by hand$"

/** Every file under a folder, with its size and time of change. */
const filesUnder = (folder: string): string =>
  existsSync(folder)
    ? readdirSync(folder, { recursive: true, encoding: "utf8" }).sort().map((p) => {
      const st = statSync(join(folder, p))
      return `${p} ${st.size} ${st.mtimeMs}`
    }).join("\n")
    : ""

let earlier: { ws: Workspace; ticket: string; place: string; refused: Said; headRefused: string; after: Said; worktrees: string }
let deleted: typeof earlier
let held: { ws: Workspace; ticket: string; place: string; refused: Said }
let two: { a: Workspace; b: Workspace; ticket: string; refused: Said; started: number }
let killed: { ws: Workspace; ticket: string; asked: Said; ruled: Said; after: Said }[] = []
let unruled: { ws: Workspace; first: Said; again: Said; showWroteNothing: boolean }
let merged: { ws: Workspace; done: Said; timesBefore: string; timesAfter: string; statusBefore: string; statusAfter: string; texts: readonly string[] }
interface UsersMerge {
  readonly how: "clean" | "unmerged" | "on the ticket's branch"
  readonly ws: Workspace
  readonly ran: Said
  readonly side: string
  readonly mergeHead: string
  readonly statusBefore: string
  readonly statusAfter: string
  readonly commits: readonly { readonly commit: string; readonly parents: readonly string[]; readonly changed: readonly string[] }[]
}
let usersMerges: UsersMerge[] = []
interface TakeIn {
  readonly ws: Workspace
  readonly ticket: string
  readonly stopped: Said
  readonly ran: Said
  readonly tipStopped: string
  readonly main: string
  readonly merge: { readonly parents: readonly string[]; readonly subject: string; readonly author: string }
  readonly merging: boolean
  readonly onBranch: string
  readonly status: string
}
let takenIn: TakeIn

/** Every file under the repository's top, with its time of change, but git's own, the tickets and the framework's local records, which a run writes. */
const timesUnder = (top: string): string =>
  readdirSync(top, { recursive: true, encoding: "utf8" }).sort()
    .filter((p) => !/(^|\/)(\.git|\.ai-workspace\/tickets|\.stdo-builder\/local)(\/|$)/.test(p))
    .filter((p) => statSync(join(top, p)).isFile())
    .map((p) => `${p} ${statSync(join(top, p)).mtimeMs}`).join("\n")

beforeAll(async () => {
  const cli = build()
  /** The state release 3.2.0 left: the ticket moved to the active lane on main, its branch made there, and checked out in a checkout of its own; with `gone`, the user deleted the checkout's folder and git still records it. */
  const earlierCheckout = async (gone: boolean) => {
    const ws = new Workspace(cli)
    await ws.setup()
    const ticket = ticketOf(await ws.ticket(S1_TICKET))
    ws.git(["add", "-A"])
    ws.git(["commit", "-qm", "the user's ticket"])
    mkdirSync(ws.path(".ai-workspace", "tickets", "active"), { recursive: true })
    ws.git(["mv", `.ai-workspace/tickets/backlog/${ticket}.md`, `.ai-workspace/tickets/active/${ticket}.md`])
    ws.git(["commit", "-qm", `board: ${ticket} to active`])
    ws.git(["branch", `stdo/${ticket}`])
    const place = ws.path(".stdo-builder", "local", "checkouts", ticket)
    ws.git(["worktree", "add", "-q", place, `stdo/${ticket}`])
    if (gone) rmSync(place, { recursive: true, force: true })
    const refused = await ws.run(S1_FIXTURES)
    const headRefused = ws.git(["symbolic-ref", "--short", "HEAD"]).trim()
    // The user runs the command the refusal gives.
    const given = /git worktree remove (\S+)/.exec(refused.out)?.[1] ?? place
    ws.git(["worktree", "remove", given])
    const after = await ws.run(S1_FIXTURES)
    return { ws, ticket, place, refused, headRefused, after, worktrees: ws.git(["worktree", "list", "--porcelain"]) }
  }
  const heldElsewhere = async () => {
    const ws = new Workspace(cli)
    await ws.setup()
    const ticket = ticketOf(await ws.ticket(S1_TICKET))
    await ws.run(S1_FIXTURES)
    ws.git(["switch", "-q", "main"])
    const place = join(temporary("stdo-builder-own-"), "ticket")
    ws.git(["worktree", "add", "-q", place, `stdo/${ticket}`])
    const refused = await ws.run(S1_FIXTURES)
    return { ws, ticket, place, refused }
  }
  const twoProducts = async () => {
    const a = new Workspace(cli, undefined, ["a"])
    execFileSync("git", ["init", "-q", "-b", "main", a.top], { env: a.env })
    write(join(a.top, "README"), "two products\n")
    execFileSync("git", ["-C", a.top, "add", "-A"], { env: a.env })
    execFileSync("git", ["-C", a.top, "commit", "-qm", "the repository's own file"], { env: a.env })
    // The second product's folder lies in the same repository, beside the first's.
    const b = new Workspace(cli, undefined, ["..", basename(a.top), "b"])
    for (const ws of [a, b]) {
      mkdirSync(ws.root, { recursive: true })
      await ws.setup()
    }
    const ticket = ticketOf(await a.ticket(S1_TICKET))
    await a.run(S1_FIXTURES)
    await b.ticket(S1_TICKET)
    const from = b.log().length
    const refused = await b.run(S1_FIXTURES)
    return { a, b, ticket, refused, started: b.log().slice(from).filter((e) => e.event === "session started").length }
  }
  /** S1 to the build, whose session writes its files and waits at a gate; the run is killed there, and the user writes a file the step does not write. */
  const killedAtBuild = async (lost: boolean) => {
    const ws = new Workspace(cli)
    const fixtures = gated(join(temporary("stdo-builder-gate-"), "never"))
    const { ticket } = await s1ToRequirements(ws, fixtures)
    const running = ws.start(["run", ws.root, "--stand-in", fixtures])
    await until(() => wroteAll(fixtures, "write-build", "work", ws.path()), 60)
    running.kill()
    await running.ended
    write(ws.path("notes.txt"), "the user's notes\n")
    if (lost) rmSync(ws.notes("started", `${ticket}.json`), { force: true })
    const asked = await ws.run(S1_FIXTURES)
    const ruled = await ws.answer("yes")
    const after = await ws.run(S1_FIXTURES)
    return { ws, ticket, asked, ruled, after }
  }
  const yesTakenOut = async () => {
    const ws = new Workspace(cli)
    await ws.setup()
    const ticket = ticketOf(await ws.ticket(S1_TICKET))
    // The induction's session writes a file its step does not write.
    const first = await ws.run(fixturesLike((f) => write(join(f, "induct-ticket", "work", "files", "stray.txt"), "written while the session worked\n")))
    await ws.answer("yes")
    // The user takes the ruling's line out of the ticket.
    const path = ws.path(".ai-workspace", "tickets", "active", `${ticket}.md`)
    write(path, readFileSync(path, "utf8").split("\n").filter((l) => !l.startsWith("- framework: ruled yes on what changed at ")).join("\n"))
    const local = ws.path(".stdo-builder", "local")
    const snapshot = (): readonly string[] => [filesUnder(local), readFileSync(join(ws.root, ".git", "index")).toString("hex"), filesUnder(join(ws.root, ".git", "objects"))]
    const before = snapshot()
    await ws.show()
    const after = snapshot()
    const again = await ws.run(S1_FIXTURES)
    return { ws, first, again, showWroteNothing: before.every((b, i) => b === after[i]) }
  }
  const mergedWithTheUsersFiles = async () => {
    const ws = new Workspace(cli, undefined, ["product"])
    const top = ws.top
    const git = (args: readonly string[]): string => execFileSync("git", ["-C", top, ...args], { encoding: "utf8", env: ws.env })
    git(["init", "-q", "-b", "main"])
    write(join(top, "notes.txt"), "the user's notes\n")
    git(["add", "-A"])
    git(["-c", "user.name=User", "-c", "user.email=user@example.com", "commit", "-qm", "the repository's own file"])
    mkdirSync(ws.root, { recursive: true })
    await ws.setup()
    await ws.ticket(S1_TICKET)
    for (let i = 0; i < 3; i++) {
      await ws.run(S1_FIXTURES)
      await ws.answer("yes")
    }
    // Before the run that merges: a file left uncommitted, one staged and one untracked, all outside the workspace's folder.
    write(join(top, "notes.txt"), "the user's notes, changed and not committed\n")
    write(join(top, "staged.txt"), "staged by the user\n")
    git(["add", "staged.txt"])
    write(join(top, "untracked.txt"), "untracked\n")
    const paths = ["notes.txt", "staged.txt", "untracked.txt"]
    const statusBefore = git(["status", "--porcelain", "--", ...paths])
    const timesBefore = timesUnder(top)
    const done = await ws.run(S1_FIXTURES)
    return { ws, done, timesBefore, timesAfter: timesUnder(top), statusBefore, statusAfter: git(["status", "--porcelain", "--", ...paths]), texts: paths.map((p) => readFileSync(join(top, p), "utf8")) }
  }
  /**
   * A workspace at `product/` inside a larger repository of the user's, whose branch `side` changes `other/c.md`, outside the
   * folder. When a run starts, the user has a merge of `side` of their own under way: on main with no ticket active, merged
   * by git and not committed (`clean`), or left unmerged where main changed the file too (`unmerged`); or on the active
   * ticket's branch, left unmerged where the user changed the file on that branch, after the user's yes to the induction.
   */
  const usersMerge = async (how: UsersMerge["how"]): Promise<UsersMerge> => {
    const ws = new Workspace(cli, undefined, ["product"])
    const top = ws.top
    const git = (args: readonly string[]): string => execFileSync("git", ["-C", top, "-c", "user.name=User", "-c", "user.email=user@example.com", ...args], { encoding: "utf8", env: ws.env, stdio: ["ignore", "pipe", "pipe"] })
    const tried = (args: readonly string[]): void => {
      try {
        git(args)
      } catch {
        // Git exits with 1 where it leaves a file unmerged.
      }
    }
    const file = join(top, "other", "c.md")
    git(["init", "-q", "-b", "main"])
    write(file, "the user's file\n")
    git(["add", "-A"])
    git(["commit", "-qm", "the repository's own file"])
    git(["switch", "-qc", "side"])
    write(file, "the user's file, changed on side\n")
    git(["commit", "-qam", "the user's change on side"])
    git(["switch", "-q", "main"])
    mkdirSync(ws.root, { recursive: true })
    await ws.setup()
    if (how === "on the ticket's branch") {
      await ws.ticket(S1_TICKET)
      await ws.run(S1_FIXTURES)
      write(file, "the user's file, changed on the ticket's branch\n")
      git(["commit", "-qam", "the user's change on the ticket's branch"])
      tried(["merge", "--no-edit", "side"])
      await ws.answer("yes")
    } else {
      if (how === "unmerged") {
        write(file, "the user's file, changed on main\n")
        git(["commit", "-qam", "the user's change on main"])
        tried(["merge", "--no-edit", "side"])
      } else git(["merge", "-q", "--no-commit", "--no-ff", "side"])
      await ws.ticket(S1_TICKET)
    }
    const status = (): string => git(["status", "--porcelain", "--", "other"])
    const statusBefore = status()
    const ran = await ws.run(S1_FIXTURES)
    const commits = git(["rev-list", "--all", "--author=STDO Builder", "--parents"]).split("\n").filter((l) => l !== "").map((l) => {
      const [commit = "", ...parents] = l.split(" ")
      const changed = parents[0] === undefined ? git(["ls-tree", "-r", "--name-only", commit]) : git(["diff-tree", "-r", "--name-only", "--no-commit-id", parents[0], commit])
      return { commit, parents, changed: changed.split("\n").filter((p) => p !== "") }
    })
    const mergeHead = existsSync(join(top, ".git", "MERGE_HEAD")) ? git(["rev-parse", "MERGE_HEAD"]).trim() : ""
    return { how, ws, ran, side: git(["rev-parse", "side"]).trim(), mergeHead, statusBefore, statusAfter: status(), commits }
  }
  /**
   * A workspace at `product/` inside a larger repository, a ticket active: the user changes `other/c.md`, outside the folder, on
   * the ticket's branch and on main, each another way. The next run stops where git cannot take main in; the user resolves the
   * file and stages it, commits nothing, and starts a run again.
   */
  const takeInResolved = async (): Promise<TakeIn> => {
    const ws = new Workspace(cli, undefined, ["product"])
    const top = ws.top
    const git = (args: readonly string[]): string => execFileSync("git", ["-C", top, "-c", "user.name=User", "-c", "user.email=user@example.com", ...args], { encoding: "utf8", env: ws.env, stdio: ["ignore", "pipe", "pipe"] })
    const file = join(top, "other", "c.md")
    git(["init", "-q", "-b", "main"])
    write(file, "the user's file\n")
    git(["add", "-A"])
    git(["commit", "-qm", "the repository's own file"])
    mkdirSync(ws.root, { recursive: true })
    await ws.setup()
    const ticket = ticketOf(await ws.ticket(S1_TICKET))
    await ws.run(S1_FIXTURES)
    write(file, "the user's file, changed on the ticket's branch\n")
    git(["commit", "-qam", "the user's change on the ticket's branch"])
    ws.onMain(() => {
      write(file, "the user's file, changed on main\n")
      git(["commit", "-qam", "the user's change on main"])
    })
    const stopped = await ws.run(S1_FIXTURES)
    const tipStopped = git(["rev-parse", `stdo/${ticket}`]).trim()
    write(file, "the user's file, resolved\n")
    git(["add", "--", "other/c.md"])
    const ran = await ws.run(S1_FIXTURES)
    // The newest merge on the ticket's branch; none where the run made none.
    const merge = git(["log", "-1", "--format=%H", "--merges", `stdo/${ticket}`]).trim()
    return {
      ws, ticket, stopped, ran, tipStopped,
      main: git(["rev-parse", "main"]).trim(),
      merge: merge === "" ? { parents: [], subject: "", author: "" } : { parents: git(["rev-list", "--parents", "-n", "1", merge]).trim().split(" ").slice(1), subject: git(["log", "-1", "--format=%s", merge]).trim(), author: git(["log", "-1", "--format=%an", merge]).trim() },
      merging: existsSync(join(top, ".git", "MERGE_HEAD")),
      onBranch: git(["show", `stdo/${ticket}:other/c.md`]),
      status: git(["status", "--porcelain", "--", "other"])
    }
  }
  let kept: typeof killed[number] | undefined
  let lost: typeof killed[number] | undefined
  ;[earlier, deleted, held, two, kept, lost, unruled, merged, takenIn, ...usersMerges] = await Promise.all([earlierCheckout(false), earlierCheckout(true), heldElsewhere(), twoProducts(), killedAtBuild(false), killedAtBuild(true), yesTakenOut(), mergedWithTheUsersFiles(), takeInResolved(), usersMerge("clean"), usersMerge("unmerged"), usersMerge("on the ticket's branch")])
  killed = [kept, lost]
}, 600_000)

afterAll(clean)

describe("bug item 6, R-16: a checkout release 3.2.0 left holds the active ticket's branch (REQ-FLOW-003 step 1)", () => {
  it("the run is refused, names the checkout and gives the command that removes it", () => {
    expect(earlier.refused.code, earlier.refused.out).toBe(2)
    expect(earlier.refused.out).toContain(earlier.place)
    expect(earlier.refused.out).toContain(`git worktree remove ${earlier.place}`)
    expect(earlier.headRefused).toBe("main")
  })
  it("once the user has removed it, the next run goes on: the folder is on the ticket's branch, which records main as the branch it left, and the user is asked on the induction", () => {
    expect(earlier.after.code, earlier.after.out).toBe(0)
    expect(earlier.after.out).toContain("waits for your answer on induct-ticket")
    expect(earlier.ws.git(["symbolic-ref", "--short", "HEAD"]).trim()).toBe(`stdo/${earlier.ticket}`)
    expect(earlier.ws.read(".ai-workspace", "tickets", "active", `${earlier.ticket}.md`)).toContain("- framework: left main")
    expect(earlier.worktrees).not.toContain(earlier.place)
  })
  it("with the checkout's folder deleted and git still recording it, the run is refused and names it, and once the user has run the command the refusal gives, the next run goes on", () => {
    expect(deleted.refused.code, deleted.refused.out).toBe(2)
    expect(deleted.refused.out).toContain(`git worktree remove ${deleted.place}`)
    expect(deleted.headRefused).toBe("main")
    expect(deleted.after.code, deleted.after.out).toBe(0)
    expect(deleted.after.out).toContain("waits for your answer on induct-ticket")
    expect(deleted.ws.git(["symbolic-ref", "--short", "HEAD"]).trim()).toBe(`stdo/${deleted.ticket}`)
    expect(deleted.worktrees).not.toContain(deleted.place)
  })
})

describe("the ticket's branch checked out in another working tree, the folder on the branch it left (REQ-FLOW-003 step 1)", () => {
  it("the run is refused, names both branches and that working tree, and gives the command that removes it", () => {
    expect(held.refused.code, held.refused.out).toBe(2)
    expect(held.refused.out).toContain(`stdo/${held.ticket}`)
    expect(held.refused.out).toContain("on the branch main")
    expect(held.refused.out).toContain(`git worktree remove ${held.place}`)
  })
})

describe("two products in one repository (REQ-FLOW-001)", () => {
  it("while one holds an active ticket, a run of the other is refused, names the branch the folder is on, and starts nothing", () => {
    expect(two.refused.code, two.refused.out).toBe(2)
    expect(two.refused.out).toContain(`on the branch stdo/${two.ticket}`)
    expect(two.started).toBe(0)
    expect(two.a.git(["symbolic-ref", "--short", "HEAD"]).trim()).toBe(`stdo/${two.ticket}`)
  })

  it("each keeps the hold and the identities from a session's start apart, under git's own directory of the one repository, so neither reads the other's (REQ-FLOW-001)", () => {
    expect(two.a.notes()).not.toBe(two.b.notes())
    expect(existsSync(two.a.notes("started", `${two.ticket}.json`))).toBe(true)
    expect(existsSync(two.b.notes("started", `${two.ticket}.json`))).toBe(false)
    expect(existsSync(two.a.path(".stdo-builder", "local", "started"))).toBe(false)
  })
})

describe("REQ-FLOW-003 step 1: a run killed while the build's session works, after it wrote its files and the user wrote a file the step does not write", () => {
  const stepOf = (k: typeof killed[number], path: string): string => k.ws.git(["log", "-1", "--format=%H %s", `stdo/${k.ticket}`, "--", path]).trim()
  it("the next run asks on the user's file alone, and after the user's yes commits both as the step's result, and neither as the user's change by hand", () => {
    const k = killed[0]
    if (k === undefined) throw new Error("no case")
    expect(k.asked.code, k.asked.out).toBe(0)
    expect(k.asked.out).toContain("waits for your ruling")
    expect(k.asked.out).toContain("notes.txt (added)")
    expect(k.asked.out).not.toContain("hello.sh (added)")
    expect(k.ruled.code, k.ruled.out).toBe(0)
    expect(k.after.code, k.after.out).toBe(0)
    expect(stepOf(k, "notes.txt"), `${k.asked.out}\n${k.ruled.out}\n${k.after.out}\n${k.ws.git(["log", "--format=%h %s", "-12"])}`).toBe(stepOf(k, "build_tenants/main/code/hello.sh"))
    expect(stepOf(k, "notes.txt")).toMatch(/^[0-9a-f]{40} the result of the step on write-build$/)
    expect(k.ws.git(["log", "--format=%H", BY_HAND, `main..stdo/${k.ticket}`]).trim()).toBe("")
  })
  it("with that session's identities removed, the next run asks on both files, and after the yes commits both as the step's result, and neither as the user's change by hand", () => {
    const k = killed[1]
    if (k === undefined) throw new Error("no case")
    expect(k.asked.code, k.asked.out).toBe(0)
    expect(k.asked.out).toContain("waits for your ruling")
    expect(k.asked.out).toContain("notes.txt (added)")
    expect(k.asked.out).toContain("build_tenants/main/code/hello.sh (added)")
    expect(k.asked.out).toContain("The identities taken at the start of the session on write-build are missing, so the framework asks you about every file not committed.")
    expect(k.after.code, k.after.out).toBe(0)
    expect(stepOf(k, "notes.txt"), `${k.asked.out}\n${k.ruled.out}\n${k.after.out}\n${k.ws.git(["log", "--format=%h %s", "-12"])}\n${k.ws.git(["status", "--short"])}`).not.toBe("")
    expect(stepOf(k, "notes.txt")).toBe(stepOf(k, "build_tenants/main/code/hello.sh"))
    expect(stepOf(k, "notes.txt")).toMatch(/^[0-9a-f]{40} the result of the step on write-build$/)
    expect(k.ws.git(["log", "--format=%H", BY_HAND, `main..stdo/${k.ticket}`]).trim()).toBe("")
  })
})

describe("bug items 8 and 9 (REQ-ALG-008, REQ-ALG-012)", () => {
  it("REQ-ALG-008 acceptance 8: the user says yes to a file a session wrote, then takes the ruling's line out of the ticket: the next run names the file again", () => {
    expect(unruled.first.out, unruled.first.out).toContain("stray.txt (added)")
    expect(unruled.again.code, unruled.again.out).toBe(0)
    expect(unruled.again.out).toContain("stray.txt (added)")
    expect(unruled.again.out).toContain("waits for your ruling")
  })
  it("REQ-ALG-012 acceptance 10: show writes nothing: no file, and nothing into git's index or store", () => {
    expect(unruled.showWroteNothing).toBe(true)
  })
})

describe("REQ-FLOW-008: a ticket merged inside a larger repository while the user has a file uncommitted, one staged and one untracked", () => {
  it("the ticket is merged and the folder is on main", () => {
    expect(merged.done.code, merged.done.out).toBe(0)
    expect(merged.done.out).toContain("merged into main")
    expect(merged.ws.git(["symbolic-ref", "--short", "HEAD"]).trim()).toBe("main")
  })
  it("each of the user's files is as it was, and no file's time changes but the ticket's own and the framework's records", () => {
    expect(merged.texts).toEqual(["the user's notes, changed and not committed\n", "staged by the user\n", "untracked\n"])
    expect(merged.statusAfter).toBe(merged.statusBefore)
    expect(merged.statusAfter.split("\n").filter((l) => l !== "").sort()).toEqual([" M notes.txt", "?? untracked.txt", "A  staged.txt"])
    expect(merged.timesAfter).toBe(merged.timesBefore)
  })
})

describe("REQ-FLOW-008, REQ-FLOW-003 step 1: inside a larger repository, main taken into the ticket's branch, where git could not merge a file outside the folder that the user then resolved and staged, and did not commit", () => {
  it("the run stopped, and the next run completes the merge, as the user's change by hand, with the ticket's branch and main as its parents, and goes on", () => {
    expect(takenIn.stopped.code, takenIn.stopped.out).toBe(1)
    expect(takenIn.stopped.out).toContain("other/c.md (from the repository's top, outside the workspace's folder)")
    expect(takenIn.ran.code, takenIn.ran.out).toBe(0)
    expect(takenIn.ran.out).toContain("waits for your answer")
    expect(takenIn.merge.parents).toEqual([takenIn.tipStopped, takenIn.main])
    expect(takenIn.merge.subject).toBe("what the user changed by hand")
    expect(takenIn.merge.author).toBe("STDO Builder")
  })
  it("git's merge is no longer under way, and the ticket's branch holds the file as the user resolved it", () => {
    expect(takenIn.merging).toBe(false)
    expect(takenIn.onBranch).toBe("the user's file, resolved\n")
    expect(takenIn.status).toBe("")
  })
})

describe("REQ-FLOW-001, REQ-FLOW-003 step 1, REQ-FLOW-008: inside a larger repository, a run starts while the user has a merge of their own under way, of a branch that changed a file outside the workspace's folder", () => {
  for (const how of ["clean", "unmerged", "on the ticket's branch"] as const) {
    const m = (): UsersMerge => {
      const found = usersMerges.find((u) => u.how === how)
      if (found === undefined) throw new Error(`no case ${how}`)
      return found
    }
    it(`${how}: the run goes on, and is neither refused nor stopped for the user's merge`, () => {
      expect(m().ran.code, m().ran.out).toBe(0)
      expect(m().ran.out).toContain("waits for your answer")
      expect(m().ran.out).not.toContain("other/c.md")
    })
    it(`${how}: the user's merge is still under way, as the user left it: git's merge is of side, and the file outside the folder is as git left it`, () => {
      expect(m().mergeHead).toBe(m().side)
      expect(m().statusAfter).toBe(m().statusBefore)
      expect(m().statusAfter).toBe(how === "clean" ? "M  other/c.md\n" : "UU other/c.md\n")
    })
    it(`${how}: no commit the framework made completes the user's merge or changes a file outside the folder: each has one parent, and changes files under the folder alone`, () => {
      expect(m().commits.length).toBeGreaterThan(0)
      for (const c of m().commits) {
        expect(c.parents, c.commit).not.toContain(m().side)
        expect(c.parents.length, c.commit).toBeLessThanOrEqual(1)
        for (const path of c.changed) expect(path.startsWith("product/"), `${c.commit} changes ${path}`).toBe(true)
      }
    })
  }
})
