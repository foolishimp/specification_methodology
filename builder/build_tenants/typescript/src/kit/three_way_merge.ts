/**
 * Three-way merge from a common ancestor: git's merge of two lines of work.
 * This is the one module that asks git to keep lines of work: to make a
 * repository and to say the top of the one a folder lies in, a branch and its
 * checkout, to commit on a line, to merge one
 * line into another, and to say what a line changed. It decides nothing about
 * which side of a merge is right. It starts git through the supervised child
 * (C12).
 *
 * A commit is made the way git makes one, from the files of the folder, and
 * goes on the line it names.
 *
 * The folder may lie below the top of the repository (REQ-FLOW-001, D201).
 * Git is then started in the folder, so each path it is given or gives is
 * from the folder, and every commit, checkout, merge and change it reads
 * concerns only files under it. A ticket's checkout then holds only the
 * folder: git's sparse checkout, set for that checkout alone.
 *
 * @carries C13
 */
import * as Effect from "effect/Effect"
import type * as ChildProcessSpawner from "effect/process/ChildProcessSpawner"
import { byName } from "./order_by_name.js"
import { covers } from "./place_containment.js"
import { supervise, type Outcome } from "./supervised_child.js"

type Spawner = ChildProcessSpawner.ChildProcessSpawner

/** Git could not do what it was asked, and why. */
export class LineRefused {
  readonly _tag = "LineRefused"
  constructor(readonly folder: string, readonly asked: string, readonly why: string) {}
}

const MINUTE = 60_000
/** Git's own variables that would point it at another repository, index or object store; a child is started without them. */
const clean = {
  GIT_DIR: undefined,
  GIT_WORK_TREE: undefined,
  GIT_INDEX_FILE: undefined,
  GIT_COMMON_DIR: undefined,
  GIT_OBJECT_DIRECTORY: undefined,
  GIT_ALTERNATE_OBJECT_DIRECTORIES: undefined,
  GIT_NAMESPACE: undefined
}
/** The commits are the framework's: made under its name, with no hook or signing of the user's in the way. */
const env = {
  ...clean,
  GIT_AUTHOR_NAME: "STDO Builder",
  GIT_AUTHOR_EMAIL: "stdo-builder@localhost",
  GIT_COMMITTER_NAME: "STDO Builder",
  GIT_COMMITTER_EMAIL: "stdo-builder@localhost",
  GIT_TERMINAL_PROMPT: "0",
  GIT_EDITOR: "true"
}
/**
 * A ticket's checkout of a folder below the repository's top holds only the
 * folder, by the patterns git keeps for that checkout alone (D201). Git reads
 * them where these two settings are given; they are given on each call, not
 * written in the repository's settings, so the user's configuration is not
 * changed. Where a checkout has no patterns, as main's own folder and every
 * checkout of a repository of its own, git holds every file, as without them.
 */
const sparse = ["-c", "core.sparseCheckout=true", "-c", "core.sparseCheckoutCone=false"]
/**
 * Git starts no upkeep of its own after a merge, either: that runs detached,
 * past the child's return and its deadline (C12), and at 100,000 files
 * (REQ-PARAM-001) it is still writing in the workspace when the command has
 * ended. The user's own git commands keep the repository as its settings say.
 */
const settings = ["-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null", "-c", "gc.auto=0", "-c", "maintenance.auto=false", ...sparse]

type Returned = Extract<Outcome, { outcome: "returned" }>
type Env = Readonly<Record<string, string>>

const git = (folder: string, args: readonly string[], extra: Env = {}, input?: string): Effect.Effect<Returned, LineRefused, Spawner> =>
  supervise({ command: "git", args: [...settings, ...args], cwd: folder, deadline: 10 * MINUTE, env: { ...env, ...extra }, ...(input === undefined ? {} : { input }) }).pipe(
    Effect.flatMap((o) =>
      o.outcome === "returned"
        ? Effect.succeed(o)
        : Effect.fail(new LineRefused(folder, args.join(" "), o.outcome === "ran over" ? "git ran over" : o.why))
    )
  )

/** Git, which must exit with zero; its output. */
const must = (folder: string, args: readonly string[], extra: Env = {}, input?: string): Effect.Effect<string, LineRefused, Spawner> =>
  git(folder, args, extra, input).pipe(
    Effect.flatMap((o) => (o.code === 0 ? Effect.succeed(o.output) : Effect.fail(new LineRefused(folder, args.join(" "), o.errors.trim() || o.output.trim()))))
  )

const parts = (output: string): readonly string[] => output.split("\0").filter((p) => p !== "")

/** The most bytes of paths one call of git is given, well within what a system lets one command line hold. */
const PATH_BYTES = 64 * 1024

/** The paths in groups, each within PATH_BYTES, in their order: a commit may change every file of a workspace of 100,000 (REQ-PARAM-001). */
const inGroups = (paths: readonly string[]): readonly (readonly string[])[] => {
  const groups: string[][] = []
  let bytes = PATH_BYTES
  for (const path of paths) {
    // A UTF-16 unit of a path is at most three bytes on the command line.
    const size = 3 * path.length + 1
    if (bytes + size > PATH_BYTES) {
      groups.push([])
      bytes = 0
    }
    groups[groups.length - 1]?.push(path)
    bytes += size
  }
  return groups
}

/**
 * The top folder of the repository the folder lies in, as git gives it; none
 * only where git says the folder is in no repository. Git's words are read in
 * English, so this one call sets `LC_ALL=C`. Any other refusal is refused.
 */
export const topOf = (folder: string): Effect.Effect<string | undefined, LineRefused, Spawner> =>
  git(folder, ["rev-parse", "--show-toplevel"], { LC_ALL: "C" }).pipe(
    Effect.flatMap((o) =>
      o.code === 0
        ? Effect.succeed(o.output.trim())
        : o.errors.includes("not a git repository")
        ? Effect.succeed(undefined)
        : Effect.fail(new LineRefused(folder, "rev-parse --show-toplevel", o.errors.trim() || o.output.trim()))
    )
  )

/** The folder's place from the top of its repository, as git gives it: empty at the top. */
const prefixOf = (folder: string): Effect.Effect<string, LineRefused, Spawner> =>
  must(folder, ["rev-parse", "--show-prefix"]).pipe(Effect.map((out) => out.trim().replace(/\/$/, "")))

/** Whether the repository whose top folder is `top` ignores the folder at `path`, from that top; a folder not yet there is judged as a folder (D201). */
export const ignores = (top: string, path: string): Effect.Effect<boolean, LineRefused, Spawner> =>
  git(top, ["check-ignore", "-q", "--", `${path}/`]).pipe(
    Effect.flatMap((o) =>
      o.code === 0 ? Effect.succeed(true) : o.code === 1 ? Effect.succeed(false) : Effect.fail(new LineRefused(top, "check-ignore", o.errors.trim() || o.output.trim()))
    )
  )

/** Makes the folder a repository whose first line of work is `line`. */
export const makeRepository = (folder: string, line: string): Effect.Effect<void, LineRefused, Spawner> =>
  must(folder, ["init", "-q", "-b", line]).pipe(Effect.asVoid)

/** Where git keeps the tips of the lines of work. A line is named to git in full, so a tag of the same name does not stand for it. */
const HEADS = "refs/heads"
const refOf = (line: string): string => `${HEADS}/${line}`
/** The line a full name of git's names, or none where it names no line. */
const lineNamed = (ref: string): string | undefined => (ref !== HEADS && covers(HEADS, ref) ? ref.slice(HEADS.length + 1) : undefined)

/** The line of work the folder has checked out, by its name; none where its HEAD names a commit alone or anything but a line. */
export const currentLine = (folder: string): Effect.Effect<string | undefined, LineRefused, Spawner> =>
  git(folder, ["symbolic-ref", "-q", "HEAD"]).pipe(
    Effect.map((o) => (o.code === 0 ? lineNamed(o.output.trim()) : undefined))
  )

/** The commit a line or other name stands for, or undefined. */
export const tipOf = (folder: string, name: string): Effect.Effect<string | undefined, LineRefused, Spawner> =>
  git(folder, ["rev-parse", "--verify", "--quiet", `${name}^{commit}`]).pipe(Effect.map((o) => (o.code === 0 ? o.output.trim() : undefined)))

/** A line git writes to mark where it could not merge, at the start of a line: `<<<<<<<` or `>>>>>>>`. */
const MARKER = "^(<<<<<<<|>>>>>>>)( |$)"

/** What a commit gave: the new commit, or none where nothing changed; or, where git could not merge them, the files, and no commit. */
export type Committed = { readonly commit: string | undefined } | { readonly unresolved: readonly string[] }

/**
 * Commits what the folder holds, or what it holds at `paths`, on the line
 * named `line`, with `message`: its parent is that line's tip and that line is
 * moved, whatever the folder's HEAD names. Git is started in the folder, so
 * the paths are from it, and what it holds is its files alone, files git
 * ignores left out (REQ-FLOW-001). At the top of a repository, git stages the
 * whole folder in the folder's own index (`add -A -- .`). For `paths`, or
 * below the top, it stages them in an index of the commit's own, at `index`,
 * which the caller names in a place git ignores within the folder, as C1's
 * index of identities is named. It is read from the line's tip with what the
 * folder's own index knows of it (`read-tree -m`), so the commit differs from
 * the tip at the paths or under the folder alone, and holds nothing the user
 * staged outside it; then they are staged in the folder's own index, where
 * git holds them or finds them there. Gives the new commit, or none when
 * nothing changed.
 *
 * A merge git could not make is never committed. Where git left a file of the
 * commit unmerged, or a file the commit changes holds a line marking a
 * conflict, nothing is committed and the files are given. A merge in progress
 * whose files are resolved is committed with both its parents, even where they
 * were resolved to what the line already held, from the folder's own index,
 * which holds what the merge took in. That is done in a ticket's checkout, or
 * where the folder is the top of its repository: a merge the user has under
 * way elsewhere in a larger repository is the user's (D201).
 */
export const commit = (folder: string, index: string, line: string, message: string, paths?: readonly string[]): Effect.Effect<Committed, LineRefused, Spawner> =>
  Effect.gen(function*() {
    const only = ["--", ...(paths ?? ["."])]
    const head = yield* tipOf(folder, refOf(line))
    const within = (path: string) => paths === undefined || paths.some((p) => covers(p, path))
    // Staging would take a file git left unmerged as resolved, so those are found first.
    const unmerged = parts(yield* must(folder, ["ls-files", "-u", "-z"])).map((e) => e.slice(e.indexOf("\t") + 1)).filter(within)
    if (unmerged.length > 0) return { unresolved: byName(new Set(unmerged)) }
    const prefix = yield* prefixOf(folder)
    const [own = "", common = ""] = (yield* must(folder, ["rev-parse", "--path-format=absolute", "--git-dir", "--git-common-dir"])).trim().split("\n")
    const merging = paths === undefined && (prefix === "" || own !== common) ? yield* tipOf(folder, "MERGE_HEAD") : undefined
    const named = merging !== undefined || (paths === undefined && prefix === "") ? undefined : index
    const staging = named === undefined ? {} : { GIT_INDEX_FILE: named }
    if (named !== undefined) {
      const fromOwn = head === undefined ? undefined : yield* git(folder, ["read-tree", "-m", head, `--index-output=${named}`])
      if (fromOwn === undefined || fromOwn.code !== 0) yield* must(folder, head === undefined ? ["read-tree", "--empty"] : ["read-tree", head], staging)
    }
    yield* must(folder, ["add", "-A", ...only], staging)
    const tree = (yield* must(folder, ["write-tree"], staging)).trim()
    const changed = parts(yield* must(folder, head === undefined ? ["ls-tree", "-r", "-z", "--name-only", tree] : ["diff-tree", "-r", "-z", "--name-only", "--no-renames", "--relative", head, tree]))
    const found = yield* Effect.forEach(inGroups(changed), (group) => git(folder, ["grep", "-l", "-z", "-I", "-E", MARKER, tree, "--", ...group]))
    const marked = found.flatMap((o) => parts(o.output)).map((p) => p.slice(tree.length + 1))
    if (marked.length > 0) return { unresolved: byName(new Set(marked)) }
    if (changed.length === 0 && merging === undefined) return { commit: undefined }
    const parents = [...(head === undefined ? [] : ["-p", head]), ...(merging === undefined ? [] : ["-p", merging])]
    const made = (yield* must(folder, ["commit-tree", tree, ...parents, "-m", message])).trim()
    yield* must(folder, ["update-ref", "-m", `commit: ${message}`, refOf(line), made, head ?? ""])
    if (merging !== undefined) yield* must(folder, ["merge", "--quit"])
    if (named !== undefined) {
      // A path neither on disk nor in the folder's own index is as the commit has it there already.
      const held = paths === undefined ? ["."] : parts(yield* must(folder, ["ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", ...paths]))
      yield* Effect.forEach(inGroups(held), (group) => must(folder, ["add", "-A", "--", ...group]))
    }
    return { commit: made }
  })

/**
 * The checkout of `line` at `checkout`, made by git. Where the line does not
 * yet exist it is made from the line `from`; where its checkout is there, it
 * is taken up. Where `repository` lies below the top of its repository, the
 * checkout holds that folder alone: git makes it with no files, sets the
 * folder as its one pattern (`sparse-checkout set`, with the settings above,
 * so the repository's own settings are not changed) and then puts the files
 * under the folder in it (`read-tree -mu`). The folder is then at its place
 * from the top within the checkout (D201).
 */
export const checkoutOf = (repository: string, line: string, from: string, checkout: string): Effect.Effect<void, LineRefused, Spawner> =>
  Effect.gen(function*() {
    const listed = yield* must(repository, ["worktree", "list", "--porcelain", "-z"])
    if (parts(listed).includes(`worktree ${checkout}`)) return
    yield* must(repository, ["worktree", "prune"])
    const exists = (yield* tipOf(repository, refOf(line))) !== undefined
    const prefix = yield* prefixOf(repository)
    const empty = prefix === "" ? [] : ["--no-checkout"]
    yield* must(repository, exists ? ["worktree", "add", "-q", ...empty, checkout, line] : ["worktree", "add", "-q", ...empty, "-b", line, checkout, refOf(from)])
    if (prefix === "") return
    yield* must(checkout, ["sparse-checkout", "set", "--", `/${prefix.replace(/[\\*?[]/g, (c) => `\\${c}`)}/`])
    yield* must(checkout, ["read-tree", "-mu", "HEAD"])
  })

export type Merged =
  | { readonly merged: "yes"; readonly changed: boolean }
  | { readonly merged: "conflict"; readonly files: readonly string[] }
  | { readonly merged: "refused"; readonly why: string }

/**
 * Merges the line `from` into the line `line`, which `folder` has checked
 * out. Git merges into what the folder's HEAD names, so where the folder is
 * not on `line` the merge is refused, and nothing is merged. A merge git
 * cannot make by itself is left as git leaves it, with the files under the
 * folder it could not merge named from the folder (`--relative`, D201).
 */
export const merge = (folder: string, line: string, from: string, message: string, fastForward: boolean): Effect.Effect<Merged, LineRefused, Spawner> =>
  Effect.gen(function*() {
    const on = yield* currentLine(folder)
    if (on !== line) return { merged: "refused", why: `${folder} is ${on === undefined ? "on no line of work" : `on ${on}`}, not on ${line}` } as const
    const before = yield* tipOf(folder, "HEAD")
    const o = yield* git(folder, ["merge", "--no-edit", fastForward ? "--ff" : "--no-ff", "-m", message, refOf(from)])
    if (o.code === 0) return { merged: "yes", changed: (yield* tipOf(folder, "HEAD")) !== before } as const
    const files = parts(yield* must(folder, ["diff", "--name-only", "--diff-filter=U", "--relative", "-z"]))
    return files.length > 0 ? ({ merged: "conflict", files } as const) : ({ merged: "refused", why: (o.errors || o.output).trim() } as const)
  })

/** The entries of a tree, as git lists them from its top (`ls-tree --full-tree`, whatever folder git is started in), each with its name. */
const entriesOf = (folder: string, tree: string, path?: string): Effect.Effect<readonly { readonly entry: string; readonly name: string; readonly id: string; readonly type: string }[], LineRefused, Spawner> =>
  must(folder, ["ls-tree", "-z", "--full-tree", tree, ...(path === undefined ? [] : ["--", path])]).pipe(
    Effect.map((out) =>
      parts(out).map((entry) => {
        const tab = entry.indexOf("\t")
        const [, type = "", id = ""] = entry.slice(0, tab).split(" ")
        return { entry, name: entry.slice(tab + 1), id, type }
      })
    )
  )

/** The tree at `path`, from the top, in the tree `tree`; none where there is no folder there. */
const treeAt = (folder: string, tree: string, path: string): Effect.Effect<string | undefined, LineRefused, Spawner> =>
  entriesOf(folder, tree, path).pipe(Effect.map((found) => found.find((e) => e.name === path && e.type === "tree")?.id))

/**
 * The tree `tree` with the tree `put` at the path whose folders are `path`,
 * from the top, and every other entry as `tree` has it: each tree on the way
 * is written again by git (`mktree`), and no index is used. A folder on the
 * way that `tree` does not have is made.
 */
const graft = (folder: string, tree: string, path: readonly string[], put: string): Effect.Effect<string, LineRefused, Spawner> =>
  Effect.gen(function*() {
    const [name, ...rest] = path
    if (name === undefined) return put
    const entries = yield* entriesOf(folder, tree)
    const there = entries.find((e) => e.name === name && e.type === "tree")?.id ?? (yield* must(folder, ["mktree", "-z"], {}, "")).trim()
    const inner = yield* graft(folder, there, rest, put)
    const kept = entries.filter((e) => e.name !== name).map((e) => e.entry)
    return (yield* must(folder, ["mktree", "-z", "--missing"], {}, [...kept, `040000 tree ${inner}\t${name}`].map((e) => `${e}\0`).join(""))).trim()
  })

/**
 * Merges the line `from` into the line `line`, which the repository's own
 * folder has checked out, with a commit of the merge. Where the folder is the
 * top of its repository, it is `merge`, with no fast-forward. Where it lies
 * below, git's merge would refuse while the user has a file staged anywhere in
 * the repository, so git makes the merge apart from the index
 * (`merge-tree --write-tree`). The merge takes the folder alone from it:
 * the commit's tree is the line's own tree with the folder's tree from git's
 * merge in its place (`graft`), so outside the folder every file is as the
 * line had it, whatever the other line changed there, and a file git could
 * not merge outside the folder is no conflict. Git commits it
 * (`commit-tree`), puts what the merge changed in the index and the files
 * (`read-tree -m -u`), which refuses where that would overwrite a change the
 * user has not committed, and only then moves the line (`update-ref`). Every
 * other file and entry of the index stays as the user left it (REQ-FLOW-008,
 * D201). Where git cannot merge a file under the folder by itself, nothing is
 * written and the files are named, from the folder.
 */
export const mergeInto = (folder: string, line: string, from: string, message: string): Effect.Effect<Merged, LineRefused, Spawner> =>
  Effect.gen(function*() {
    const prefix = yield* prefixOf(folder)
    if (prefix === "") return yield* merge(folder, line, from, message, false)
    const on = yield* currentLine(folder)
    if (on !== line) return { merged: "refused", why: `${folder} is ${on === undefined ? "on no line of work" : `on ${on}`}, not on ${line}` } as const
    const before = yield* tipOf(folder, refOf(line))
    const theirs = yield* tipOf(folder, refOf(from))
    if (before === undefined || theirs === undefined) return { merged: "refused", why: `${line} or ${from} has no commit` } as const
    const o = yield* git(folder, ["merge-tree", "--write-tree", "-z", "--name-only", refOf(line), refOf(from)])
    const [first = "", ...conflicted] = (o.output.split("\0\0")[0] ?? "").split("\0")
    if (o.code !== 0 && o.code !== 1) return { merged: "refused", why: (o.errors || o.output).trim() } as const
    const under = conflicted.filter((p) => p !== "" && covers(prefix, p)).map((p) => p.slice(prefix.length + 1))
    if (under.length > 0) return { merged: "conflict", files: byName(new Set(under)) } as const
    const merged = yield* treeAt(folder, first.trim(), prefix)
    if (merged === undefined) return { merged: "refused", why: `git's merge holds no folder ${prefix}` } as const
    const own = (yield* must(folder, ["rev-parse", "--verify", `${before}^{tree}`])).trim()
    const tree = yield* graft(folder, own, prefix.split("/"), merged)
    const made = (yield* must(folder, ["commit-tree", tree, "-p", before, "-p", theirs, "-m", message])).trim()
    const put = yield* git(folder, ["read-tree", "-m", "-u", before, made])
    if (put.code !== 0) return { merged: "refused", why: (put.errors || put.output).trim() } as const
    yield* must(folder, ["update-ref", "-m", `merge: ${message}`, refOf(line), made, before])
    return { merged: "yes", changed: true } as const
  })

/** The file at `path` as the line `from` has it, put in the checkout and in git's index by git. */
export const takeFrom = (folder: string, from: string, path: string): Effect.Effect<void, LineRefused, Spawner> =>
  must(folder, ["checkout", refOf(from), "--", path]).pipe(Effect.asVoid)

/**
 * The line checked out in `folder` holds all of the line `name` under the
 * folder: every commit of it, or every change it made under the folder since
 * the two last met (`diff HEAD...name -- .`). A line that has moved only
 * outside the folder is held (REQ-FLOW-008, D201).
 */
export const holdsAll = (folder: string, name: string): Effect.Effect<boolean, LineRefused, Spawner> =>
  Effect.gen(function*() {
    if ((yield* git(folder, ["merge-base", "--is-ancestor", refOf(name), "HEAD"])).code === 0) return true
    return (yield* git(folder, ["diff", "--quiet", `HEAD...${refOf(name)}`, "--", "."])).code === 0
  })

/** The files under the folder that differ between two commits, or over a range such as `a...b`, by their paths from the folder, with how many lines of each were added or taken out (D201). */
export const changedLines = (folder: string, from: string, to?: string): Effect.Effect<readonly Changed[], LineRefused, Spawner> =>
  must(folder, ["diff", "--numstat", "--no-renames", "--relative", "-z", from, ...(to === undefined ? [] : [to])]).pipe(
    Effect.map((out) =>
      parts(out).map((entry) => {
        const [added = "0", removed = "0", ...path] = entry.split("\t")
        const count = (n: string): number => (n === "-" ? 0 : Number(n))
        return { path: path.join("\t"), lines: count(added) + count(removed), added: count(added), removed: count(removed) }
      })
    )
  )

/** A file that differs between two commits: its path from the folder, and the lines added and taken out, with their sum. */
export interface Changed {
  readonly path: string
  readonly lines: number
  readonly added: number
  readonly removed: number
}

/** The commit where `from` and the line `name` last met, git's merge base; none where they share none (REQ-FLOW-006, D211). */
export const mergeBase = (folder: string, from: string, name: string): Effect.Effect<string | undefined, LineRefused, Spawner> =>
  git(folder, ["merge-base", from, refOf(name)]).pipe(Effect.map((r) => (r.code === 0 && r.output.trim() !== "" ? r.output.trim() : undefined)))

/** The lines of work named one of `names`, or below one of them as `stdo/x` is below `stdo`, by name. */
export const linesNamed = (folder: string, names: readonly string[]): Effect.Effect<readonly string[], LineRefused, Spawner> =>
  must(folder, ["for-each-ref", "--format=%(refname)", ...names.map(refOf)]).pipe(
    Effect.map((out) => out.split("\n").flatMap((ref) => {
      const line = lineNamed(ref)
      return line === undefined ? [] : [line]
    }))
  )

/** The merge commits on `line`, newest first, each with its parents. */
/** The subject of each merge the line holds, newest first. */
export const mergeSubjects = (folder: string, line: string): Effect.Effect<readonly string[], LineRefused, Spawner> =>
  must(folder, ["log", "--merges", "--format=%s", refOf(line)]).pipe(Effect.map((out) => out.split("\n").filter((l) => l !== "")))

export const mergesOn = (folder: string, line: string): Effect.Effect<readonly { readonly commit: string; readonly parents: readonly string[] }[], LineRefused, Spawner> =>
  must(folder, ["rev-list", "--merges", "--parents", refOf(line)]).pipe(
    Effect.map((out) =>
      out.split("\n").filter((l) => l !== "").map((l) => {
        const [commit = "", ...parents] = l.split(" ")
        return { commit, parents }
      })
    )
  )
