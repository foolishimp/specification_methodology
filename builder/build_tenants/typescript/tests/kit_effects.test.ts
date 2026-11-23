/**
 * The kit modules that act on the world, each tested by its law, as section 1
 * of the design states it: content addressing (C1), the supervised child
 * (C12), the three-way merge (C13), the append-only log (C10), the exclusive
 * hold (C11) and create if absent (C15). Every git repository here is a new
 * one in a temporary folder outside this repository.
 *
 * @uses C1 C10 C11 C12 C13 C15
 * @is REQ-VERIFY-004 REQ-ALG-001 REQ-FLOW-010
 */
import * as NodeServices from "@effect/platform-node/NodeServices"
import * as Effect from "effect/Effect"
import { execFileSync } from "node:child_process"
import { existsSync, mkdirSync, mkdtempSync, readFileSync, realpathSync, rmSync, writeFileSync } from "node:fs"
import { tmpdir } from "node:os"
import { join } from "node:path"
import { afterAll, describe, expect, it } from "vitest"
import { append, exists, fold } from "../src/kit/append_only_log.js"
import { identitiesOf, sha256Of } from "../src/kit/content_addressing.js"
import { createIfAbsent } from "../src/kit/create_if_absent.js"
import { held, holding } from "../src/kit/exclusive_hold.js"
import { supervise } from "../src/kit/supervised_child.js"
import * as Lines from "../src/kit/three_way_merge.js"

const on = <A, E>(effect: Effect.Effect<A, E, NodeServices.NodeServices>): Promise<A> => Effect.runPromise(effect.pipe(Effect.provide(NodeServices.layer)))

const made: string[] = []
const folder = (): string => {
  const f = realpathSync(mkdtempSync(join(tmpdir(), "stdo-builder-kit-")))
  made.push(f)
  return f
}
afterAll(() => {
  for (const f of made) rmSync(f, { recursive: true, force: true })
})

/** A new repository, with one line of work named main. */
const repository = async (): Promise<string> => {
  const f = folder()
  await on(Lines.makeRepository(f, "main"))
  return f
}

/** Commits the whole folder on `line`, as the commit flow does, with the commit's own index, where it needs one, kept outside the folder. Gives the commit, or undefined where nothing changed. */
const commitAll = (f: string, line: string, message: string) =>
  Lines.commit(f, join(folder(), "commit.index"), line, message).pipe(Effect.map((c) => ("commit" in c ? c.commit : undefined)))

/** The identities at the assets' places, as `gather` asks for them, from an index of identities kept outside the folder. */
const indexes = new Map<string, string>()
const assets = (f: string, places: readonly string[]) => {
  const index = indexes.get(f) ?? join(folder(), "identity.index")
  indexes.set(f, index)
  return on(identitiesOf(f, index, places, !existsSync(index)))
}

describe("C1 content addressing", () => {
  it("REQ-FLOW-010: the sha256 of a file's bytes, by which the record names a release's manifest, is the value worked out by hand for FIPS 180-2's examples (D197)", async () => {
    const bytes = (text: string): Uint8Array => new Uint8Array([...text].map((c) => c.charCodeAt(0)))
    expect(await on(sha256Of(bytes("abc")))).toBe("ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")
    expect(await on(sha256Of(bytes("")))).toBe("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
    // Equal identity, equal content: one byte changed gives another.
    expect(await on(sha256Of(bytes("abd")))).not.toBe(await on(sha256Of(bytes("abc"))))
  })

  it("REQ-ALG-001 acceptance 1: a file changed by one byte has another identity; changed back, it has the first again", async () => {
    const f = await repository()
    writeFileSync(join(f, "a.txt"), "hello\n")
    const first = (await assets(f, ["a.txt"])).identities.get("a.txt")
    writeFileSync(join(f, "a.txt"), "hellp\n")
    const second = (await assets(f, ["a.txt"])).identities.get("a.txt")
    writeFileSync(join(f, "a.txt"), "hello\n")
    const third = (await assets(f, ["a.txt"])).identities.get("a.txt")
    expect(first).toBeDefined()
    expect(second).not.toBe(first)
    expect(third).toBe(first)
  })

  it("REQ-ALG-001 law 1: two contents have the same identity only when they are the same; a folder's identity covers all it holds", async () => {
    const f = await repository()
    mkdirSync(join(f, "x"))
    mkdirSync(join(f, "y"))
    writeFileSync(join(f, "x", "a.txt"), "same\n")
    writeFileSync(join(f, "y", "a.txt"), "same\n")
    writeFileSync(join(f, "y", "b.txt"), "other\n")
    const ids = (await assets(f, ["x", "y"])).identities
    expect(ids.get("x/a.txt")).toBe(ids.get("y/a.txt"))
    expect(ids.get("y/b.txt")).not.toBe(ids.get("y/a.txt"))
    expect(ids.get("x")).not.toBe(ids.get("y"))
    writeFileSync(join(f, "x", "b.txt"), "other\n")
    const again = (await assets(f, ["x", "y"])).identities
    expect(again.get("x")).toBe(again.get("y"))
  })

  it("files git is set to ignore are no part of an asset; the content is not copied, only named", async () => {
    const f = await repository()
    mkdirSync(join(f, "x"))
    writeFileSync(join(f, "x", "a.txt"), "kept\n")
    const before = (await assets(f, ["x"])).identities.get("x")
    writeFileSync(join(f, ".gitignore"), "*.log\nbuild/\n")
    writeFileSync(join(f, "x", "noise.log"), "ignored\n")
    mkdirSync(join(f, "x", "build"))
    writeFileSync(join(f, "x", "build", "out.txt"), "a folder ignored whole\n")
    mkdirSync(join(f, "x", "sub", ".git"), { recursive: true })
    writeFileSync(join(f, "x", "sub", ".git", "HEAD"), "git never holds a .git folder\n")
    const got = await assets(f, ["x"])
    expect(got.identities.get("x")).toBe(before)
    expect(got.files).not.toContain("x/noise.log")
    expect(got.files).not.toContain("x/build/out.txt")
    expect(got.files).not.toContain("x/sub/.git/HEAD")
    expect(got.files).toContain("x/a.txt")
  })

  it("follows what changed: a new index starts from the folder's own, and the root is the one git gives the folder", async () => {
    const f = await repository()
    mkdirSync(join(f, "x"))
    writeFileSync(join(f, "x", "a.txt"), "one\n")
    await on(commitAll(f, "main", "base"))
    writeFileSync(join(f, "x", "b.txt"), "two\n")
    const got = await assets(f, ["x"])
    const git = (args: string[]) => execFileSync("git", ["-C", f, ...args], { encoding: "utf8", stdio: "pipe" }).trim()
    git(["add", "-A"])
    expect(got.root).toBe(git(["write-tree"]))
    expect(got.identities.get("x/b.txt")).toBe(git(["rev-parse", ":x/b.txt"]))
    expect(got.files).toEqual(["x/a.txt", "x/b.txt"])
  })

  it("an index of identities that git cannot read is started again, and the identities are given", async () => {
    const f = await repository()
    writeFileSync(join(f, "a.txt"), "hello\n")
    const first = await assets(f, ["a.txt"])
    writeFileSync(indexes.get(f) ?? "", "not an index\n")
    expect((await assets(f, ["a.txt"])).root).toBe(first.root)
  })
})

describe("C12 supervised child", () => {
  it("gives exactly one outcome: returned, with its code and what it printed", async () => {
    const got = await on(supervise({ command: "sh", args: ["-c", "echo out; echo err >&2; exit 3"], cwd: folder(), deadline: 10_000 }))
    expect(got).toEqual({ outcome: "returned", code: 3, output: "out\n", errors: "err\n" })
  })
  it("could not start", async () => {
    const got = await on(supervise({ command: "no-such-program-stdo-builder", args: [], cwd: folder(), deadline: 10_000 }))
    expect(got.outcome).toBe("could not start")
  })
  it("ran over, and the child is stopped", async () => {
    const f = folder()
    const began = Date.now()
    const got = await on(supervise({ command: "sh", args: ["-c", "sleep 1; touch late"], cwd: f, deadline: 200 }))
    expect(got).toEqual({ outcome: "ran over" })
    expect(Date.now() - began).toBeLessThan(1_000)
    await new Promise((r) => setTimeout(r, 1_500))
    expect(existsSync(join(f, "late"))).toBe(false)
  })
  it("starts the child without the variables the caller has set for git, as C1 and C13 ask", async () => {
    const f = folder()
    const got = await on(supervise({ command: "sh", args: ["-c", "echo ${GIT_DIR-unset}"], cwd: f, deadline: 10_000, env: { GIT_DIR: undefined } }))
    const before = process.env.GIT_DIR
    process.env.GIT_DIR = join(f, "elsewhere.git")
    try {
      const again = await on(supervise({ command: "sh", args: ["-c", "echo ${GIT_DIR-unset}"], cwd: f, deadline: 10_000, env: { GIT_DIR: undefined } }))
      expect(again).toMatchObject({ outcome: "returned", output: "unset\n" })
    } finally {
      if (before === undefined) delete process.env.GIT_DIR
      else process.env.GIT_DIR = before
    }
    expect(got).toMatchObject({ outcome: "returned", output: "unset\n" })
  })
  it("takes its input when one is given", async () => {
    const got = await on(supervise({ command: "cat", args: [], cwd: folder(), deadline: 10_000, input: "given\n" }))
    expect(got).toEqual({ outcome: "returned", code: 0, output: "given\n", errors: "" })
  })
})

describe("C13 three-way merge", () => {
  it("merges lines that change different files, and leaves a conflict as git leaves it, naming the file", async () => {
    const f = await repository()
    writeFileSync(join(f, "a.txt"), "one\n")
    writeFileSync(join(f, "b.txt"), "one\n")
    const base = await on(commitAll(f, "main", "base"))
    expect(base).toBeDefined()
    expect(await on(commitAll(f, "main", "nothing changed"))).toBeUndefined()
    const checkout = join(f, "..", `${f.split("/").pop()}-line`)
    made.push(checkout)
    await on(Lines.checkoutOf(f, "stdo/t", "main", checkout))
    writeFileSync(join(checkout, "a.txt"), "two\n")
    await on(commitAll(checkout, "stdo/t", "on the line"))
    writeFileSync(join(f, "b.txt"), "two\n")
    await on(commitAll(f, "main", "on main"))
    expect(await on(Lines.holdsAll(checkout, "main"))).toBe(false)
    const taken = await on(Lines.merge(checkout, "stdo/t", "main", "take main in", true))
    expect(taken).toEqual({ merged: "yes", changed: true })
    expect(await on(Lines.holdsAll(checkout, "main"))).toBe(true)
    expect(readFileSync(join(checkout, "b.txt"), "utf8")).toBe("two\n")

    writeFileSync(join(checkout, "a.txt"), "three\n")
    await on(commitAll(checkout, "stdo/t", "line again"))
    writeFileSync(join(f, "a.txt"), "four\n")
    await on(commitAll(f, "main", "main again"))
    const clash = await on(Lines.merge(f, "main", "stdo/t", "merge the line", false))
    expect(clash).toEqual({ merged: "conflict", files: ["a.txt"] })
    expect(readFileSync(join(f, "a.txt"), "utf8")).toContain("<<<<<<<")
    expect(await on(Lines.linesNamed(f, ["stdo"]))).toEqual(["stdo/t"])
  }, 30_000)
  it("works on the folder it is given, whatever the caller's git variables point at", async () => {
    const f = folder()
    const elsewhere = join(folder(), "elsewhere.git")
    const before = process.env.GIT_DIR
    process.env.GIT_DIR = elsewhere
    try {
      await on(Lines.makeRepository(f, "main"))
      writeFileSync(join(f, "a.txt"), "one\n")
      expect(await on(commitAll(f, "main", "first"))).toBeDefined()
    } finally {
      if (before === undefined) delete process.env.GIT_DIR
      else process.env.GIT_DIR = before
    }
    expect(existsSync(join(f, ".git"))).toBe(true)
    expect(existsSync(elsewhere)).toBe(false)
  })
  it("a commit goes on the line it names, whatever the folder's HEAD names, and a merge into a folder not on the line is refused", async () => {
    const f = await repository()
    writeFileSync(join(f, "a.txt"), "one\n")
    const base = (await on(commitAll(f, "main", "base"))) ?? ""
    const git = (args: string[]) => execFileSync("git", ["-C", f, ...args], { encoding: "utf8", stdio: "pipe" }).trim()
    git(["branch", "other"])
    // HEAD is put on another line, and a tag and a file of git's take main's name: none of them is where main's commit goes.
    git(["symbolic-ref", "HEAD", "refs/heads/other"])
    git(["tag", "main", base])
    writeFileSync(join(f, ".git", "main"), `${base}\n`)
    writeFileSync(join(f, "a.txt"), "two\n")
    const made = (await on(commitAll(f, "main", "on main by its name"))) ?? ""
    expect(git(["rev-parse", "refs/heads/main"])).toBe(made)
    expect(git(["rev-parse", "refs/heads/other"])).toBe(base)
    expect(git(["rev-parse", `${made}^`])).toBe(base)
    expect(await on(Lines.currentLine(f))).toBe("other")
    expect(await on(Lines.merge(f, "main", "other", "a merge into main", false))).toEqual({ merged: "refused", why: `${f} is on other, not on main` })
    expect(git(["rev-parse", "refs/heads/main"])).toBe(made)
    git(["checkout", "-q", "--detach", made])
    expect(await on(Lines.currentLine(f))).toBeUndefined()
    expect(await on(Lines.linesNamed(f, ["main"]))).toEqual(["main"])
  })

  it("names the files a line changed, with their lines", async () => {
    const f = await repository()
    writeFileSync(join(f, "a.txt"), "one\n")
    const first = (await on(commitAll(f, "main", "first"))) ?? ""
    writeFileSync(join(f, "a.txt"), "one\ntwo\nthree\n")
    const second = (await on(commitAll(f, "main", "second"))) ?? ""
    expect(await on(Lines.changedLines(f, first, second))).toEqual([{ path: "a.txt", lines: 2, added: 2, removed: 0 }])
  })
})

describe("C10 append-only log", () => {
  it("a fold sees every entry in the order added, and passes over a partial last line", async () => {
    const file = join(folder(), "log", "events.log")
    expect(await on(exists(file))).toBe(false)
    expect(await on(fold(file, [] as string[], (r, e) => [...r, e]))).toBeUndefined()
    await on(append(file, "one"))
    await on(append(file, "two"))
    writeFileSync(file, readFileSync(file, "utf8") + "thr", { flag: "w" })
    expect(await on(fold(file, [] as string[], (r, e) => [...r, e]))).toEqual(["one", "two"])
  })
})

describe("C11 exclusive hold", () => {
  it("at most one holds it; a second is refused while the first holds; it is released at the end", async () => {
    const file = join(folder(), "holds", "t")
    const inner = await on(holding(file, holding(file, Effect.succeed("inner"))))
    expect(inner).toEqual({ done: "held" })
    expect(await on(held([file]))).toEqual([])
    expect(await on(holding(file, Effect.succeed(1)))).toEqual({ done: 1 })
  })
  it("a hold whose holder has ended is taken", async () => {
    const file = join(folder(), "t")
    writeFileSync(file, "999999999\n")
    expect(await on(held([file]))).toEqual([])
    expect(await on(holding(file, Effect.succeed("taken")))).toEqual({ done: "taken" })
  })
})

describe("C15 create if absent", () => {
  it("writes a file that is not there, and never changes one that is", async () => {
    const file = join(folder(), "a", "b.txt")
    expect(await on(createIfAbsent(file, "first\n"))).toBe("written")
    expect(await on(createIfAbsent(file, "second\n"))).toBe("there")
    expect(readFileSync(file, "utf8")).toBe("first\n")
  })
})
