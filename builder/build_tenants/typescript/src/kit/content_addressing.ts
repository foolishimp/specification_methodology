/**
 * Content addressing: the identity of a file is a hash of its content, and the
 * identity of a folder a hash of the names and identities in it. Git computes
 * both; this is the one module that asks git for identities. It starts git
 * through the supervised child (C12).
 *
 * Git keeps the identities in an index of their own, which the caller names,
 * apart from the folder's own index. Each time, git is told the files that
 * changed since it last looked (`ls-files --modified --deleted --others`) and
 * records their identities alone (`update-index --info-only`), so the work
 * follows the files that changed and no content is kept. A new index starts
 * from what the folder's own index knows of the last commit (`read-tree -m`),
 * so it too follows what changed. The folders' identities are written as
 * trees, which hold names and identities and no content of a file. Files git
 * ignores are no part of them. A file git holds is read back by its identity.
 *
 * Git is started in the folder, so the files are those under it, by their
 * paths from it. Where the folder lies below the top of its repository, its
 * identity is that of the folder within git's tree of the whole, and the
 * places are read in it, so a file outside the folder is part of no identity
 * (REQ-ALG-001, D201).
 *
 * A release of this product names its manifest by the sha256 of the
 * manifest's bytes, which git does not give: that identity is computed here
 * too, by Effect's digest module on the platform's WebCrypto (D197).
 *
 * @carries C1
 */
import { Digest } from "effect/crypto"
import * as Effect from "effect/Effect"
import type * as ChildProcessSpawner from "effect/process/ChildProcessSpawner"
import { covers } from "./place_containment.js"
import { supervise } from "./supervised_child.js"

/** Content identities by path. */
export type IdentityMap = ReadonlyMap<string, string>

/** The identity of a folder, and of the files and folders at the places asked for. */
export interface Identities {
  /** The identity of the whole folder, files git ignores left out. */
  readonly root: string
  /** By path relative to the folder: each file and folder at the places, and each folder above one. */
  readonly identities: IdentityMap
  /** The paths of the files alone at the places, in git's order. */
  readonly files: readonly string[]
  /** All the content but the places asked to be left apart, where some are: the entries at the top and in each folder that holds one of them, but those, each with its identity. */
  readonly beside?: string
}

/** Git could not give the identities, and why. */
export class IdentityRefused {
  readonly _tag = "IdentityRefused"
  constructor(readonly folder: string, readonly why: string) {}
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

const asks = (folder: string, args: readonly string[], extra?: { input?: string | Uint8Array; index?: string }) =>
  supervise({
    command: "git",
    args,
    cwd: folder,
    deadline: 10 * MINUTE,
    ...(extra?.input === undefined ? {} : { input: extra.input }),
    env: extra?.index === undefined ? clean : { ...clean, GIT_INDEX_FILE: extra.index }
  }).pipe(
    Effect.flatMap((o) =>
      o.outcome === "returned" && o.code === 0
        ? Effect.succeed(o.output)
        : Effect.fail(new IdentityRefused(folder, o.outcome === "returned" ? o.errors.trim() : o.outcome === "ran over" ? "git ran over" : o.why))
    )
  )

const parts = (output: string): readonly string[] => output.split("\0").filter((p) => p !== "")

/**
 * The identities of the folder as it is now: of the whole folder, of each
 * file and folder at `places`, and of the folder beside the places `apart`.
 * `index` is where git keeps them, in a place git ignores; `fresh` says there
 * is none there yet. An index git cannot read is started again.
 */
export const identitiesOf = (folder: string, index: string, places: readonly string[], fresh: boolean, apart: readonly string[] = []): Effect.Effect<Identities, IdentityRefused, ChildProcessSpawner.ChildProcessSpawner> =>
  Effect.gen(function*() {
    // From the folder's own index, where git can read it against the last commit; otherwise empty.
    const start = asks(folder, ["read-tree", "-m", "HEAD", `--index-output=${index}`]).pipe(
      Effect.catch(() => asks(folder, ["read-tree", "--empty"], { index }))
    )
    const update = Effect.gen(function*() {
      // A path that ends in "/" is a repository of its own inside the folder; it is no file of this one.
      const changed = [...new Set(parts(yield* asks(folder, ["ls-files", "-z", "--modified", "--deleted", "--others", "--exclude-standard"], { index })))].filter((p) => !p.endsWith("/"))
      if (changed.length > 0) yield* asks(folder, ["update-index", "-z", "--add", "--remove", "--info-only", "--stdin"], { input: changed.map((p) => `${p}\0`).join(""), index })
      const whole = (yield* asks(folder, ["write-tree", "--missing-ok"], { index })).trim()
      const prefix = (yield* asks(folder, ["rev-parse", "--show-prefix"])).trim().replace(/\/$/, "")
      if (prefix === "") return whole
      // The folder within the whole; a folder that holds no file git keeps is the empty one.
      const found = yield* asks(folder, ["ls-tree", "-z", "--full-tree", whole, "--", prefix]).pipe(Effect.map(parts))
      const entry = found.find((line) => line.slice(line.indexOf("\t") + 1) === prefix)
      return entry === undefined ? (yield* asks(folder, ["hash-object", "-t", "tree", "--stdin"], { input: "" })).trim() : (entry.split(" ")[2]?.split("\t")[0] ?? "")
    })
    if (fresh) yield* start
    const root = yield* update.pipe(Effect.catch(() => start.pipe(Effect.andThen(update))))
    const identities = new Map<string, string>()
    const files: string[] = []
    const listed = places.length === 0 ? [] : parts(yield* asks(folder, ["ls-tree", "-r", "-t", "-z", "--full-tree", root, "--", ...places]))
    for (const line of listed) {
      const tab = line.indexOf("\t")
      const [, type, identity] = line.slice(0, tab).split(" ")
      const path = line.slice(tab + 1)
      if (identity === undefined) continue
      identities.set(path, identity)
      if (type === "blob") files.push(path)
    }
    if (apart.length === 0) return { root, identities, files }
    // Git lists the entries at the top and in each folder that holds a place apart, and not the folders it passes through on the way.
    const holding = [...new Set(apart.flatMap((p) => (p.includes("/") ? [`${p.slice(0, p.lastIndexOf("/"))}/`] : [])))]
    const beside = parts(yield* asks(folder, ["ls-tree", "-z", "--full-tree", root, "--", ".", ...holding])).filter((line) => !apart.some((p) => covers(p, line.slice(line.indexOf("\t") + 1))))
    return { root, identities, files, beside: beside.join("\n") }
  })

/**
 * The identity at `from` and at `to` of each path whose identity differs
 * between two identities of the folder, written as trees from the index of
 * identities, by path from the folder: `git diff-tree -r --no-renames`, which
 * reads names and identities and no content. None where git no longer holds
 * `from`: the identities from then are missing (REQ-ALG-008, D226).
 */
export const treeDifference = (folder: string, from: string, to: string): Effect.Effect<{ readonly start: IdentityMap; readonly end: IdentityMap } | undefined, IdentityRefused, ChildProcessSpawner.ChildProcessSpawner> =>
  asks(folder, ["cat-file", "-e", `${from}^{tree}`]).pipe(
    Effect.matchEffect({
      onFailure: () => Effect.succeed(undefined),
      onSuccess: () =>
        asks(folder, ["diff-tree", "-r", "-z", "--no-renames", from, to]).pipe(Effect.map((out) => {
          const start = new Map<string, string>()
          const end = new Map<string, string>()
          const fields = out.split("\0")
          const none = /^0+$/
          for (let i = 0; i + 1 < fields.length; i += 2) {
            const meta = (fields[i] ?? "").split(" ")
            const path = fields[i + 1] ?? ""
            const before = meta[2] ?? ""
            const after = meta[3] ?? ""
            if (path === "" || meta.length < 5) continue
            if (!none.test(before)) start.set(path, before)
            if (!none.test(after)) end.set(path, after)
          }
          return { start, end }
        }))
    })
  )

/**
 * The identity at `from`, a tree of the folder kept from a session's start,
 * and now of each path whose identity differs, by path from the folder, read
 * without writing anything: no index, no tree and no file's content is
 * written into git's store (REQ-ALG-012, D242). The tree is listed
 * (`ls-tree -r --full-tree`). Now is read through the index of identities at
 * `index`, which no one writes here: its entries whose files' times and sizes
 * still match are taken as they stand (`ls-files -s`), and each file it lists
 * as changed or does not hold, files git ignores left out, is hashed with
 * nothing stored (`hash-object --stdin-paths`). None where git no longer holds
 * `from`: the identities from then are missing (REQ-ALG-008).
 */
export const differenceNow = (folder: string, index: string, from: string): Effect.Effect<{ readonly start: IdentityMap; readonly end: IdentityMap } | undefined, IdentityRefused, ChildProcessSpawner.ChildProcessSpawner> =>
  asks(folder, ["cat-file", "-e", `${from}^{tree}`]).pipe(
    Effect.matchEffect({
      onFailure: () => Effect.succeed(undefined),
      onSuccess: () =>
        Effect.gen(function*() {
          // `ls-tree` gives the mode, the type and the identity; `ls-files -s` the mode, the identity and the stage.
          const entries = (out: string, at: number): Map<string, string> =>
            new Map(parts(out).flatMap((l) => {
              const tab = l.indexOf("\t")
              const id = l.slice(0, tab).split(" ")[at]
              return id === undefined || tab < 0 ? [] : [[l.slice(tab + 1), id] as const]
            }))
          const atStart = entries(yield* asks(folder, ["ls-tree", "-r", "-z", "--full-tree", from]), 2)
          const held = entries(yield* asks(folder, ["ls-files", "-s", "-z"], { index }), 1)
          const gone = new Set(parts(yield* asks(folder, ["ls-files", "-z", "--deleted"], { index })))
          const changed = parts(yield* asks(folder, ["ls-files", "-z", "--modified", "--others", "--exclude-standard"], { index })).filter((p) => !p.endsWith("/") && !gone.has(p))
          // git reads these paths from the repository's top, not from the folder within it; each is given whole.
          const hashed = changed.length === 0 ? [] : (yield* asks(folder, ["hash-object", "--stdin-paths"], { input: changed.map((p) => `${folder}/${p}\n`).join("") })).split("\n").filter((l) => l !== "")
          const now = new Map([...held].filter(([p]) => !gone.has(p)))
          changed.forEach((p, i) => now.set(p, hashed[i] ?? ""))
          const start = new Map<string, string>()
          const end = new Map<string, string>()
          for (const [p, id] of atStart) if (now.get(p) !== id) start.set(p, id)
          for (const [p, id] of now) if (atStart.get(p) !== id) end.set(p, id)
          for (const p of start.keys()) if (now.has(p) && !end.has(p)) end.set(p, now.get(p) ?? "")
          return { start, end }
        })
    })
  )

/** The tree of the folder in `commit`, from the folder: what the identities of the commit the folder is on are, as a tree; the empty tree where the commit holds no file under the folder (REQ-FLOW-003 step 1, D241). */
export const folderTreeAt = (folder: string, commit: string): Effect.Effect<string, IdentityRefused, ChildProcessSpawner.ChildProcessSpawner> =>
  asks(folder, ["rev-parse", "--verify", "--quiet", `${commit}:./`]).pipe(
    Effect.map((out) => out.trim()),
    Effect.catch(() => asks(folder, ["hash-object", "-t", "tree", "--stdin"], { input: "" }).pipe(Effect.map((out) => out.trim())))
  )

/** The files git holds in the folder or does not ignore there, by path relative to it. */
export const filesOf = (folder: string): Effect.Effect<readonly string[], IdentityRefused, ChildProcessSpawner.ChildProcessSpawner> =>
  asks(folder, ["ls-files", "-z", "--cached", "--others", "--exclude-standard"]).pipe(Effect.map((out) => parts(out).filter((p) => !p.endsWith("/"))))

/** The text of the file git holds under an identity, in the repository the folder lies in. */
export const textOf = (folder: string, identity: string): Effect.Effect<string, IdentityRefused, ChildProcessSpawner.ChildProcessSpawner> =>
  asks(folder, ["cat-file", "blob", identity])

/**
 * The identity of each of `places` that is there under `commit`, from the
 * folder, as git holds it in that commit's tree: the same identity the index of
 * identities gives the same content. None where git does not hold the commit
 * (REQ-ALG-004). It reads no index.
 */
export const underCommit = (folder: string, commit: string, places: readonly string[]): Effect.Effect<ReadonlyMap<string, string> | undefined, IdentityRefused, ChildProcessSpawner.ChildProcessSpawner> =>
  asks(folder, ["cat-file", "-e", `${commit}^{commit}`]).pipe(
    Effect.matchEffect({
      onFailure: () => Effect.succeed(undefined),
      onSuccess: () =>
        places.length === 0
          ? Effect.succeed(new Map<string, string>())
          : asks(folder, ["ls-tree", "-z", commit, "--", ...places]).pipe(
            Effect.map((out) =>
              new Map(out.split("\0").filter((l) => l !== "").flatMap((l) => {
                const [meta = "", path = ""] = l.split("\t")
                const id = meta.split(" ")[2]
                return id === undefined ? [] : [[path, id] as const]
              }))
            )
          )
    })
  )

/** The text of the file at `path`, from the folder, under `commit`; none where git holds no such file there. */
export const textAt = (folder: string, commit: string, path: string): Effect.Effect<string | undefined, never, ChildProcessSpawner.ChildProcessSpawner> =>
  asks(folder, ["cat-file", "blob", `${commit}:./${path}`]).pipe(Effect.orElseSucceed(() => undefined))

/** The identity git gives to a text, as it would to a file holding it. Nothing is stored. */
export const identityOfText = (folder: string, text: string): Effect.Effect<string, IdentityRefused, ChildProcessSpawner.ChildProcessSpawner> =>
  asks(folder, ["hash-object", "--stdin"], { input: text }).pipe(Effect.map((out) => out.trim()))

/** The sha256 of a file's bytes, in lowercase hex, as a release's manifest is named by it (D197). */
export const sha256Of = (bytes: Uint8Array): Effect.Effect<string> =>
  Effect.gen(function*() {
    const digest = yield* Digest.Digest
    return yield* digest.digestHex(Digest.sha256, bytes)
  }).pipe(Effect.provide(Digest.layerWebCrypto))
