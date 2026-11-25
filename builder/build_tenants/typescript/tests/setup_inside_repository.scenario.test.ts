/**
 * Scenario S13, a product inside a larger repository, driven through the
 * command-line program installed from its release, with the stand-in agent.
 * The driver makes a git
 * repository with files of its own and a second branch, and inside it an
 * empty folder the repository does not ignore. Outside the folder one file is
 * changed and not committed and another is changed and staged; among the
 * repository's own files are two at places an asset of the product has from
 * the workspace's folder, here measured from the repository's top. The user
 * sets up a governed product in the folder and goes on as in S1. While the
 * build is asked, the user changes files outside the folder, those two among
 * them, and commits them on the ticket's branch, which the repository is on;
 * puts the repository on main, commits one more file outside the folder there
 * and puts it back; and answers. The next run takes main into the ticket's
 * branch, and the merge carries them all to main; the words that say the
 * ticket is done name those committed on the ticket's branch as taken in, and
 * not the one main held already (D256). After the merge, the user commits one
 * more file outside the folder on main and starts a run.
 *
 * In a second larger repository, the user commits files outside the folder on
 * the active ticket's branch, one of them at the code's place from the
 * repository's top, and changes that file on main too: `show` read while the
 * ticket is active counts neither; the run stops where git cannot take main
 * in, naming the file from the repository's top and saying so. The next run,
 * with the file still unmerged, and the one after it, with the file staged as
 * git left it, lines marking the conflict in it, stop again, name it the same
 * way and commit nothing. Once the user resolves it the merge carries the
 * branch's whole tree to main, and the words that say the ticket is done name
 * the file only the branch has as taken in, and not the one the user resolved
 * to main's.
 *
 * Then a folder not yet there inside a larger repository is set up, and a
 * folder the repository ignores is refused, with the folder and the
 * repository, git's own folder among them, byte for byte as they were.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-001 REQ-FLOW-002 REQ-FLOW-003 REQ-FLOW-008 REQ-ALG-001 REQ-ALG-010 REQ-ALG-012
 */
import { execFileSync } from "node:child_process"
import { createHash } from "node:crypto"
import { existsSync, mkdirSync, readdirSync, readFileSync, statSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, installed, onMain, S1_ASSETS, S1_FIXTURES, s1ToRequirements, testsPass, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const WITHIN = ["apps", "product"]
const FOLDER = WITHIN.join("/")
const USER = ["-c", "user.name=User", "-c", "user.email=user@example.com"]

/** Every file and folder under a root, by its path: a file with its bytes, a folder as a folder; `but` and what lies below them left out. */
const everything = (root: string, but: readonly string[] = []): Map<string, string> =>
  new Map(
    (readdirSync(root, { recursive: true }) as string[])
      .filter((p) => !but.some((b) => p === b || p.startsWith(`${b}/`)))
      .map((p) => {
        const full = join(root, p)
        return [p, statSync(full).isFile() ? createHash("sha1").update(readFileSync(full)).digest("hex") : "a folder"] as const
      })
  )

const changedBetween = (before: Map<string, string>, after: Map<string, string>): string[] =>
  [...new Set([...before.keys(), ...after.keys()])].filter((p) => before.get(p) !== after.get(p)).sort()

/** The words of a command's output, each as a path of its own. */
const words = (out: string): string[] => out.split(/\s+/).map((w) => w.replace(/^[`'"(<]+/, "").replace(/[`'">),.;:]+$/, ""))

let ws: Workspace
let top = ""
const git = (args: readonly string[]): string => execFileSync("git", ["-C", top, ...args], { encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] })
const says = (args: readonly string[]): boolean => {
  try {
    git(args)
    return true
  } catch {
    return false
  }
}

let setUp: Said
let ticket = ""
let answered: Said
let merged: Said
let last: Said
let shown: Said
let before = new Map<string, string>()
let second = ""
let committedByUser = ""
let takenInAfter: LogEntry[] = []
const committedOutside = new Map<string, string>()

beforeAll(async () => {
  const program = installed()
  ws = new Workspace(program.cli, program.bin, WITHIN)
  top = ws.top
  write(join(top, "README.md"), "# The user's own repository\n")
  write(join(top, "other", "kept.md"), "kept\n")
  write(join(top, "other", "edited.md"), "edited\n")
  write(join(top, "other", "staged.md"), "staged\n")
  write(join(top, "lib", "later.md"), "later\n")
  // Two files at places the product's assets have from the workspace's folder, here from the repository's top.
  write(join(top, "specification", "INTENT.md"), "The repository's own intent.\n")
  write(join(top, "build_tenants", "main", "code", "hello.sh"), "echo the repository's own\n")
  git(["init", "-q", "-b", "main"])
  git(["add", "-A"])
  git([...USER, "commit", "-q", "-m", "the user's repository"])
  git(["branch", "second"])
  mkdirSync(ws.root, { recursive: true })
  write(join(top, "other", "edited.md"), "edited, and not committed\n")
  write(join(top, "other", "staged.md"), "staged, and not committed\n")
  git(["add", "other/staged.md"])
  before = everything(top, [".git", FOLDER])
  second = git(["rev-parse", "second"]).trim()

  const got = await s1ToRequirements(ws, S1_FIXTURES)
  setUp = got.said[0] ?? { code: -1, out: "" }
  ticket = got.ticket
  // The build is asked. The user changes files outside the folder, the two at the assets' places among them, and commits them on the ticket's branch, which the repository is on.
  await ws.run(S1_FIXTURES)
  for (const [path, text] of [["lib/later.md", "later, as the user committed it\n"], ["specification/INTENT.md", "The repository's intent, changed.\n"], ["build_tenants/main/code/hello.sh", "echo one\necho two\necho three\necho four\necho five\n"]] as const) {
    write(join(top, path), text)
    committedOutside.set(path, text)
  }
  git([...USER, "commit", "-q", "-m", "the user's change outside the folder", "--", ...committedOutside.keys()])
  // The user puts the repository on main, commits a file outside the folder there, and puts it back: main moves while the ticket is active, outside the folder alone.
  ws.onMain(() => {
    write(join(top, "lib", "on-main.md"), "committed on main while the ticket is active\n")
    git(["add", "--", "lib/on-main.md"])
    git([...USER, "commit", "-q", "-m", "the user's change outside the folder, on main", "--", "lib/on-main.md"])
  })
  committedOutside.set("lib/on-main.md", "committed on main while the ticket is active\n")
  committedByUser = git(["rev-parse", "main"]).trim()
  const from = ws.log().length
  answered = await ws.answer("yes")
  merged = await ws.run(S1_FIXTURES)
  takenInAfter = ws.log().slice(from).filter((e) => e.event === "main taken in")
  shown = await ws.show()
  // After the merge, one more file outside the folder is changed and committed on main.
  write(join(top, "other", "kept.md"), "kept, then changed on main\n")
  committedOutside.set("other/kept.md", "kept, then changed on main\n")
  git([...USER, "commit", "-q", "-m", "one more change outside the folder", "--", "other/kept.md"])
  last = await ws.run(S1_FIXTURES)
}, 300_000)

afterAll(clean)

describe("S13 A product inside a larger repository", () => {
  it("REQ-FLOW-002: set-up goes on, says that the product lies inside a larger repository, and names it by its top folder", () => {
    expect(setUp.code, setUp.out).toBe(0)
    expect(setUp.out).toMatch(/inside a larger git repository/)
    expect(words(setUp.out), setUp.out).toContain(top)
    expect(existsSync(join(ws.root, ".git"))).toBe(false)
  })

  it("REQ-FLOW-002, REQ-FLOW-001: within the folder, the workspace is as S1 leaves it", () => {
    expect(merged.code, merged.out).toBe(0)
    expect(onMain(ws)).toEqual(expect.arrayContaining(S1_ASSETS))
    expect(ws.board().done).toEqual([ticket])
    expect(ws.board().active).toEqual([])
    expect(testsPass(ws)).toBe(true)
  })

  it("REQ-FLOW-001: the ticket is built in the workspace's folder, at its place from the repository's top, and git has no working tree beside it", () => {
    expect(existsSync(ws.path("specification", "INTENT.md"))).toBe(true)
    expect(ws.git(["worktree", "list", "--porcelain"]).split("\n").filter((l) => l.startsWith("worktree "))).toHaveLength(1)
  })

  it("REQ-FLOW-008, REQ-ALG-004: main moved only outside the folder changes no file of a node: the answer on the content asked is taken, and still stands once main is taken in", () => {
    expect(answered.code, answered.out).toBe(0)
    expect(answered.out).not.toMatch(/Nothing is asked/)
    expect(merged.code, merged.out).toBe(0)
    expect(ws.board().done).toEqual([ticket])
  })

  it("REQ-FLOW-008: main moved only outside the folder is taken into the ticket's branch whole: the next run merges it in, and the branch holds the user's commit on main (D240)", () => {
    expect(takenInAfter.map((e) => e.result)).toContain("merged")
    expect(says(["merge-base", "--is-ancestor", committedByUser, `stdo/${ticket}`])).toBe(true)
    expect(git(["show", `stdo/${ticket}:lib/on-main.md`])).toBe("committed on main while the ticket is active\n")
  })

  it("REQ-FLOW-008, REQ-FLOW-001: the ticket's branch is a branch of the repository, merged into main, and the files the user committed outside the folder are on main as the user committed them", () => {
    expect(git(["branch", "--list", `stdo/${ticket}`]).trim()).not.toBe("")
    expect(says(["merge-base", "--is-ancestor", `stdo/${ticket}`, "main"])).toBe(true)
    for (const [path, text] of committedOutside) {
      expect(git(["show", `main:${path}`])).toBe(text)
      expect(readFileSync(join(top, path), "utf8")).toBe(text)
    }
  })

  it("REQ-FLOW-008 step 2, REQ-FLOW-003: the words that say the ticket is done name each file outside the folder the merge took into main, read from the two commits: the files the user committed on the ticket's branch between two runs, and not the one main held already", () => {
    expect(merged.out).toContain(`The work on the ticket ${ticket} is done`)
    const taken = merged.out.split("\n").find((l) => l.startsWith("The merge took these files outside the workspace's folder into main, the branch the ticket left: ")) ?? ""
    for (const path of ["lib/later.md", "specification/INTENT.md", "build_tenants/main/code/hello.sh"]) expect(taken, merged.out).toContain(`${path} (changed)`)
    expect(taken).not.toContain("on-main.md")
    expect(taken).not.toContain("other/")
  })

  it("REQ-FLOW-001: outside the folder every other file is as it was, what the user left uncommitted is still uncommitted, the staged file still staged, and the second branch on its commit", () => {
    const after = everything(top, [".git", FOLDER])
    expect(changedBetween(before, after)).toEqual([...committedOutside.keys()].sort())
    const status = git(["status", "--porcelain", "--", "other"]).split("\n").filter((l) => l !== "")
    expect(status.sort()).toEqual([" M other/edited.md", "M  other/staged.md"])
    expect(git(["show", ":other/staged.md"])).toBe("staged, and not committed\n")
    expect(git(["rev-parse", "second"]).trim()).toBe(second)
  })

  it("REQ-FLOW-001, REQ-FLOW-008: no commit the framework made, other than a ticket's merge, changes a file outside the folder; a ticket's merge, of main into the ticket's branch or of that branch into main, carries what the two branches hold, and the framework made no other merge", () => {
    const made = git(["rev-list", "--all", "--author=STDO Builder"]).split("\n").filter((l) => l !== "")
    expect(made.length).toBeGreaterThan(0)
    const parentsOf = (commit: string): string[] => git(["rev-list", "--parents", "-n", "1", commit]).trim().split(" ").slice(1)
    // The ticket's merge into main: main as it stood before it is its first parent, and the ticket's branch its second.
    const branch = git(["rev-parse", `stdo/${ticket}`]).trim()
    const intoMain = made.filter((c) => parentsOf(c).length === 2 && parentsOf(c)[1] === branch && git(["log", "-1", "--format=%s", c]).trim() === `merge stdo/${ticket}: ${ticket} is done`)
    expect(intoMain).toHaveLength(1)
    const mainBefore = parentsOf(intoMain[0] ?? "")[0] ?? ""
    for (const commit of made) {
      const parents = parentsOf(commit)
      if (parents.length > 1) {
        // Main taken into the ticket's branch: a commit of the branch whose second parent main held before the ticket's merge.
        const takenIn = parents.length === 2 && says(["merge-base", "--is-ancestor", commit, branch]) && says(["merge-base", "--is-ancestor", parents[1] ?? "", mainBefore])
        expect(takenIn || commit === intoMain[0], `${commit} is a merge: ${git(["log", "-1", "--format=%s", commit]).trim()}`).toBe(true)
        continue
      }
      const changed = parents.length === 0 ? git(["ls-tree", "-r", "--name-only", commit]) : git(["diff-tree", "-r", "--name-only", "--no-commit-id", parents[0] ?? "", commit])
      for (const path of changed.split("\n").filter((l) => l !== "")) expect(path.startsWith(`${FOLDER}/`), `${commit} changes ${path}`).toBe(true)
    }
  })

  it("REQ-ALG-012 acceptance 8: a file changed outside the folder is named for no ticket and adds to no count of lines", () => {
    expect(shown.code, shown.out).toBe(0)
    const code = readFileSync(join(S1_FIXTURES, "write-build", "work", "files", "build_tenants", "main", "code", "hello.sh"), "utf8").split("\n").filter((l) => l !== "").length
    expect(shown.out).toMatch(new RegExp(`code \\(${code} lines\\)`))
    expect(shown.out).not.toMatch(/lib\/later|other\//)
  })

  it("REQ-FLOW-001: the framework keeps nothing in the larger repository's git folder but what git keeps there for the whole repository, and the hold and the identities in a folder of the workspace's own; the commit's own index is in the workspace", () => {
    const own = `stdo-builder/at-${encodeURIComponent(FOLDER)}`
    const kept = (readdirSync(join(top, ".git"), { recursive: true }) as string[])
      .filter((p) => !/^(objects|refs|logs)(\/|$)/.test(p) && !/^worktrees\/[^/]+\/(refs|logs)(\/|$)/.test(p))
      .filter((p) => /stdo/i.test(p.split("/").slice(p.startsWith("worktrees/") ? 2 : 0).join("/")))
    const notes = (p: string): boolean => p === "stdo-builder" || p === own || (p.startsWith(`${own}/`) && /^(holds|started)(\/|$)/.test(p.slice(own.length + 1)))
    expect(kept.filter((p) => !notes(p))).toEqual([])
    expect(kept.filter((p) => p.startsWith(`${own}/`)).length).toBeGreaterThan(0)
    expect(existsSync(ws.path(".stdo-builder", "local", "commit.index"))).toBe(true)
  })

  it("REQ-ALG-010 acceptance 3, REQ-ALG-001 acceptance 2: with no ticket waiting, files changed and committed outside the folder, at the assets' places from the repository's top among them, change no asset's identity: done says yes on main and they give no ticket", () => {
    expect(last.code, last.out).toBe(2)
    expect(last.out).toContain("there is nothing to build")
    expect(ws.board().backlog).toEqual([])
  })
})

describe("S13, files committed outside the folder on the active ticket's branch", () => {
  let inner: Workspace
  let at = ""
  let t = ""
  let shownActive: Said
  let answeredHere: Said
  let stoppedHere: Said
  let unmergedHere: Said
  let markedHere: Said
  let mergedHere: Said
  /** The ticket's branch, and whether a merge was in progress, after each run that stopped. */
  const kept: { tip: string; merging: boolean }[] = []
  const onMainText = "echo main's own\n"
  const atTop = (args: readonly string[], where = at): string => execFileSync("git", ["-C", where, ...args], { encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] })
  const codeLines = (): number => readFileSync(join(S1_FIXTURES, "write-build", "work", "files", "build_tenants", "main", "code", "hello.sh"), "utf8").split("\n").filter((l) => l !== "").length

  beforeAll(async () => {
    inner = new Workspace(build(), undefined, WITHIN)
    at = inner.top
    write(join(at, "README.md"), "# The user's own repository\n")
    write(join(at, "build_tenants", "main", "code", "hello.sh"), "echo the repository's own\n")
    atTop(["init", "-q", "-b", "main"])
    atTop(["add", "-A"])
    atTop([...USER, "commit", "-q", "-m", "the user's repository"])
    mkdirSync(inner.root, { recursive: true })
    t = (await s1ToRequirements(inner, S1_FIXTURES)).ticket
    // The build is asked. The repository is on the ticket's branch, and the user commits on it two files outside the folder: one at the code's place from the repository's top, with lines of its own, and one at no asset's place.
    await inner.run(S1_FIXTURES)
    write(join(at, "build_tenants", "main", "code", "hello.sh"), "echo the branch's own\necho one\necho two\necho three\necho four\necho five\necho six\n")
    write(join(at, "other", "branch-only.md"), "only on the ticket's branch\n")
    atTop(["add", "--", "build_tenants/main/code/hello.sh", "other/branch-only.md"])
    atTop([...USER, "commit", "-q", "-m", "the user's change outside the folder, on the ticket's branch"])
    shownActive = await inner.show()
    // The user puts the repository on main, changes the same file outside the folder another way, commits it there, and puts it back (D239).
    inner.onMain(() => {
      write(join(at, "build_tenants", "main", "code", "hello.sh"), onMainText)
      atTop([...USER, "commit", "-q", "-m", "the user's change outside the folder, on main", "--", "build_tenants/main/code/hello.sh"])
    })
    answeredHere = await inner.answer("yes")
    // Main is taken in whole: git cannot merge the file both lines changed, and the run stops (D240).
    stoppedHere = await inner.run(S1_FIXTURES)
    const keep = () => kept.push({ tip: atTop(["rev-parse", `stdo/${t}`]).trim(), merging: existsSync(join(at, ".git", "MERGE_HEAD")) })
    keep()
    // The user starts a run with the file still unmerged; then stages it as git left it, the lines marking the conflict in it, and starts another.
    unmergedHere = await inner.run(S1_FIXTURES)
    keep()
    atTop(["add", "--", "build_tenants/main/code/hello.sh"])
    markedHere = await inner.run(S1_FIXTURES)
    keep()
    // The user keeps main's, and commits the merge in the folder (D240).
    write(join(at, "build_tenants", "main", "code", "hello.sh"), onMainText)
    atTop(["add", "--", "build_tenants/main/code/hello.sh"])
    atTop([...USER, "commit", "-q", "--no-edit"])
    mergedHere = await inner.run(S1_FIXTURES)
  }, 300_000)

  it("REQ-ALG-012 acceptance 8: while the ticket is active, files changed outside the folder on its branch are named for no ticket and add to no count of lines", () => {
    expect(shownActive.code, shownActive.out).toBe(0)
    expect(shownActive.out).toContain(t)
    expect(shownActive.out).toMatch(new RegExp(`code \\(${codeLines()} lines\\)`))
    expect(shownActive.out).not.toMatch(/branch-only|other\//)
  })

  it("REQ-FLOW-008, REQ-FLOW-003: where both lines changed a file outside the folder, the run stops and names it from the repository's top, saying so and where to resolve it; once the user resolves it, the merge carries the branch's whole tree to main, the file only the branch has with it", () => {
    expect(answeredHere.code, answeredHere.out).toBe(0)
    expect(stoppedHere.code, stoppedHere.out).toBe(1)
    expect(stoppedHere.out).toContain("git could not merge build_tenants/main/code/hello.sh (from the repository's top, outside the workspace's folder) by itself")
    expect(stoppedHere.out).toContain("Resolve it where git left it in the repository, and commit in the workspace's folder")
    expect(mergedHere.code, mergedHere.out).toBe(0)
    expect(inner.board().done).toEqual([t])
    expect(atTop(["merge-base", "--is-ancestor", `stdo/${t}`, "main"]) === "").toBe(true)
    expect(atTop(["show", "main:build_tenants/main/code/hello.sh"])).toBe(onMainText)
    expect(readFileSync(join(at, "build_tenants", "main", "code", "hello.sh"), "utf8")).toBe(onMainText)
    expect(atTop(["ls-tree", "-r", "--name-only", "main", "--", "other"]).trim()).toBe("other/branch-only.md")
    expect(existsSync(join(at, "other", "branch-only.md"))).toBe(true)
    expect(onMain(inner)).toEqual(expect.arrayContaining(S1_ASSETS))
    // The words that say the ticket is done name what the merge took in outside the folder, read from main before it and the merge's commit: the file only the branch had, and not the one the user resolved to main's (REQ-FLOW-008 step 2).
    const taken = mergedHere.out.split("\n").find((l) => l.startsWith("The merge took these files outside the workspace's folder into main")) ?? ""
    expect(taken, mergedHere.out).toContain("other/branch-only.md (added)")
    expect(taken).not.toContain("hello.sh")
  })

  it("REQ-FLOW-003, REQ-FLOW-008: until the user resolves it, each next run stops, names the file outside the folder from the repository's top, saying so and where to resolve it, and commits nothing: with the file unmerged, and with it staged holding the lines that mark the conflict", () => {
    for (const ran of [unmergedHere, markedHere]) {
      expect(ran.code, ran.out).toBe(1)
      expect(ran.out).toContain("git could not merge build_tenants/main/code/hello.sh (from the repository's top, outside the workspace's folder), and the merge is not resolved")
      expect(ran.out).toContain("Resolve it where git left it in the repository, and commit in the workspace's folder")
    }
    expect(kept.map((k) => k.tip)).toEqual([kept[0]?.tip, kept[0]?.tip, kept[0]?.tip])
    expect(kept.map((k) => k.merging)).toEqual([true, true, true])
  })
})

/** A repository of the user's with one commit, which ignores the folder `ignored/`. */
function outerRepository(cli: string): Workspace {
  const outer = new Workspace(cli)
  write(outer.path("README.md"), "# The user's own repository\n")
  write(outer.path(".gitignore"), "ignored/\n")
  write(outer.path("ignored", "notes.md"), "a file the repository ignores\n")
  outer.git(["init", "-q", "-b", "main"])
  outer.git(["add", "-A"])
  outer.git([...USER, "commit", "-q", "-m", "the user's repository"])
  return outer
}

describe("set-up in a folder inside a larger repository, there or not yet there, and in one it ignores", () => {
  let outer: Workspace
  let notThere: Said
  let ignoredThere: Said
  let ignoredNotThere: Said
  let unchanged: string[] = []

  beforeAll(async () => {
    const cli = build()
    outer = outerRepository(cli)
    const was = everything(outer.root, ["apps"])
    ignoredThere = await outer.command(["setup", outer.path("ignored"), "--name", "Hello"])
    ignoredNotThere = await outer.command(["setup", outer.path("ignored", "product"), "--name", "Hello"])
    unchanged = changedBetween(was, everything(outer.root, ["apps"]))
    notThere = await outer.command(["setup", outer.path("apps", "product"), "--name", "Hello"])
  }, 120_000)

  it("REQ-FLOW-002: a folder not yet there inside a larger repository is made and set up, and set-up names the repository", () => {
    expect(notThere.code, notThere.out).toBe(0)
    expect(words(notThere.out)).toContain(outer.root)
    expect(existsSync(outer.path("apps", "product", "stdo_hello.json"))).toBe(true)
    expect(existsSync(outer.path("apps", "product", ".git"))).toBe(false)
  })

  for (const [name, said] of [["a folder that is there", () => ignoredThere], ["a folder not yet there", () => ignoredNotThere]] as const) {
    it(`REQ-FLOW-002: ${name} that the repository ignores is refused, names the repository, says that it ignores the folder and where the product may be set up`, () => {
      expect(said().code, said().out).toBe(2)
      expect(words(said().out), said().out).toContain(outer.root)
      expect(said().out).toMatch(/ignores/)
      expect(said().out).toMatch(/does not ignore/)
      expect(said().out).toMatch(/in no (git )?repository/)
      expect(said().out).toMatch(/top folder/)
    })
  }

  it("REQ-FLOW-002: a refused set-up leaves the folder and the repository, git's own folder among them, as they were", () => {
    expect(unchanged).toEqual([])
    expect(existsSync(outer.path("ignored", "product"))).toBe(false)
  })
})
