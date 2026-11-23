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
 * them, commits them on main and answers. After the merge, the user commits
 * one more file outside the folder on main and starts a run.
 *
 * In a second larger repository, the user commits files outside the folder on
 * the active ticket's branch, one of them at the code's place from the
 * repository's top, and changes that file on main too: `show` read while the
 * ticket is active counts neither, and the merge keeps main's files outside
 * the folder.
 *
 * Then a folder not yet there inside a larger repository is set up, and a
 * folder the repository ignores is refused, with the folder and the
 * repository, git's own folder among them, byte for byte as they were.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-001 REQ-FLOW-002 REQ-FLOW-008 REQ-ALG-001 REQ-ALG-010 REQ-ALG-012
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
  // The build is asked. The user changes files outside the folder, the two at the assets' places among them, and commits them on main.
  await ws.run(S1_FIXTURES)
  for (const [path, text] of [["lib/later.md", "later, as the user committed it\n"], ["specification/INTENT.md", "The repository's intent, changed.\n"], ["build_tenants/main/code/hello.sh", "echo one\necho two\necho three\necho four\necho five\n"]] as const) {
    write(join(top, path), text)
    committedOutside.set(path, text)
  }
  git([...USER, "commit", "-q", "-m", "the user's change outside the folder", "--", ...committedOutside.keys()])
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

  it("REQ-FLOW-001: a ticket's checkout holds the workspace's folder alone, at its place from the repository's top", () => {
    const checkoutTop = ws.path(".stdo-builder", "local", "checkouts", ticket)
    expect(readdirSync(checkoutTop).filter((f) => f !== ".git").sort()).toEqual(["apps"])
    expect(readdirSync(join(checkoutTop, "apps"))).toEqual(["product"])
    expect(existsSync(ws.checkout(ticket, "specification", "INTENT.md"))).toBe(true)
  })

  it("REQ-FLOW-001: main moved only outside the folder has not changed for the product: the answer on the content asked is taken", () => {
    expect(answered.code, answered.out).toBe(0)
    expect(answered.out).not.toMatch(/Nothing is asked/)
  })

  it("REQ-FLOW-008: main moved only outside the folder is not taken into the ticket's branch", () => {
    expect(takenInAfter.length).toBeGreaterThan(0)
    expect(takenInAfter.map((e) => e.result)).not.toContain("merged")
    expect(says(["merge-base", "--is-ancestor", committedByUser, `stdo/${ticket}`])).toBe(false)
  })

  it("REQ-FLOW-008, REQ-FLOW-001: the ticket's branch is a branch of the repository, merged into main, and the files the user committed outside the folder are on main as the user committed them", () => {
    expect(git(["branch", "--list", `stdo/${ticket}`]).trim()).not.toBe("")
    expect(says(["merge-base", "--is-ancestor", `stdo/${ticket}`, "main"])).toBe(true)
    for (const [path, text] of committedOutside) {
      expect(git(["show", `main:${path}`])).toBe(text)
      expect(readFileSync(join(top, path), "utf8")).toBe(text)
    }
  })

  it("REQ-FLOW-001: outside the folder every other file is as it was, what the user left uncommitted is still uncommitted, the staged file still staged, and the second branch on its commit", () => {
    const after = everything(top, [".git", FOLDER])
    expect(changedBetween(before, after)).toEqual([...committedOutside.keys()].sort())
    const status = git(["status", "--porcelain", "--", "other"]).split("\n").filter((l) => l !== "")
    expect(status.sort()).toEqual([" M other/edited.md", "M  other/staged.md"])
    expect(git(["show", ":other/staged.md"])).toBe("staged, and not committed\n")
    expect(git(["rev-parse", "second"]).trim()).toBe(second)
  })

  it("REQ-FLOW-001, REQ-FLOW-008: no commit the framework made changes a file outside the folder", () => {
    const made = git(["rev-list", "--all", "--author=STDO Builder"]).split("\n").filter((l) => l !== "")
    expect(made.length).toBeGreaterThan(0)
    for (const commit of made) {
      const parents = git(["rev-list", "--parents", "-n", "1", commit]).trim().split(" ").slice(1)
      const changed = parents.length === 0
        ? git(["ls-tree", "-r", "--name-only", commit])
        : git(["diff-tree", "-r", "--name-only", "--no-commit-id", parents.length > 1 ? "--cc" : parents[0] ?? "", commit])
      for (const path of changed.split("\n").filter((l) => l !== "")) expect(path.startsWith(`${FOLDER}/`), `${commit} changes ${path}`).toBe(true)
      // A merge into main is as main had it before, outside the folder.
      if (parents.length > 1 && parents[0] !== undefined) {
        for (const path of git(["diff-tree", "-r", "--name-only", "--no-commit-id", parents[0], commit]).split("\n").filter((l) => l !== "")) {
          expect(path.startsWith(`${FOLDER}/`), `${commit} changes ${path} from its first parent`).toBe(true)
        }
      }
    }
  })

  it("REQ-ALG-012 acceptance 8: a file changed outside the folder is named for no ticket and adds to no count of lines", () => {
    expect(shown.code, shown.out).toBe(0)
    const code = readFileSync(join(S1_FIXTURES, "write-build", "work", "files", "build_tenants", "main", "code", "hello.sh"), "utf8").split("\n").filter((l) => l !== "").length
    expect(shown.out).toMatch(new RegExp(`code \\(${code} lines\\)`))
    expect(shown.out).not.toMatch(/lib\/later|other\//)
  })

  it("REQ-FLOW-001: the framework keeps nothing in the larger repository's git folder but what git keeps there for the whole repository; the commit's own index is in the workspace", () => {
    const kept = (readdirSync(join(top, ".git"), { recursive: true }) as string[])
      .filter((p) => !/^(objects|refs|logs)(\/|$)/.test(p) && !/^worktrees\/[^/]+\/(refs|logs)(\/|$)/.test(p))
      .filter((p) => /stdo/i.test(p.split("/").slice(p.startsWith("worktrees/") ? 2 : 0).join("/")))
    expect(kept).toEqual([])
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
  let mergedHere: Said
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
    // The build is asked. In the ticket's checkout the user commits, on its branch, two files outside the folder: one at the code's place from the repository's top, with lines of its own, and one at no asset's place.
    await inner.run(S1_FIXTURES)
    const checkout = inner.path(".stdo-builder", "local", "checkouts", t)
    write(join(checkout, "build_tenants", "main", "code", "hello.sh"), "echo the branch's own\necho one\necho two\necho three\necho four\necho five\necho six\n")
    write(join(checkout, "other", "branch-only.md"), "only on the ticket's branch\n")
    atTop(["add", "--sparse", "--", "build_tenants/main/code/hello.sh", "other/branch-only.md"], checkout)
    atTop([...USER, "commit", "-q", "-m", "the user's change outside the folder, on the ticket's branch"], checkout)
    shownActive = await inner.show()
    // On main, the user changes the same file outside the folder another way.
    write(join(at, "build_tenants", "main", "code", "hello.sh"), onMainText)
    atTop([...USER, "commit", "-q", "-m", "the user's change outside the folder, on main", "--", "build_tenants/main/code/hello.sh"])
    answeredHere = await inner.answer("yes")
    mergedHere = await inner.run(S1_FIXTURES)
  }, 240_000)

  it("REQ-ALG-012 acceptance 8: while the ticket is active, files changed outside the folder on its branch are named for no ticket and add to no count of lines", () => {
    expect(shownActive.code, shownActive.out).toBe(0)
    expect(shownActive.out).toContain(t)
    expect(shownActive.out).toMatch(new RegExp(`code \\(${codeLines()} lines\\)`))
    expect(shownActive.out).not.toMatch(/branch-only|other\//)
  })

  it("REQ-FLOW-008: the merge changes no file outside the folder: main keeps its own of the file both lines changed there, and the file only the branch has is not brought to main", () => {
    expect(answeredHere.code, answeredHere.out).toBe(0)
    expect(mergedHere.code, mergedHere.out).toBe(0)
    expect(inner.board().done).toEqual([t])
    expect(atTop(["merge-base", "--is-ancestor", `stdo/${t}`, "main"]) === "").toBe(true)
    expect(atTop(["show", "main:build_tenants/main/code/hello.sh"])).toBe(onMainText)
    expect(readFileSync(join(at, "build_tenants", "main", "code", "hello.sh"), "utf8")).toBe(onMainText)
    expect(atTop(["ls-tree", "-r", "--name-only", "main", "--", "other"]).trim()).toBe("")
    expect(existsSync(join(at, "other"))).toBe(false)
    const changed = atTop(["diff-tree", "-r", "--name-only", "--no-commit-id", "main^1", "main"]).split("\n").filter((l) => l !== "")
    expect(changed.length).toBeGreaterThan(0)
    for (const path of changed) expect(path.startsWith(`${FOLDER}/`), `the merge changes ${path}`).toBe(true)
    expect(onMain(inner)).toEqual(expect.arrayContaining(S1_ASSETS))
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
