/**
 * The files service: the framework reads the workspace and writes its own
 * files (REQ-FLOW-001, "Write the set-up files" and "Write its own files"),
 * and moves a ticket from lane to lane. It is carried out by the platform's
 * file module and by create if absent (C15). It never deletes a file.
 *
 * Set-up's one write outside the workspace, installing and verifying the
 * method release (REQ-FLOW-002 step 2), is the method's own release manager,
 * started through the supervised child (C12). A run asks the same manager,
 * once, where it keeps that release, for the activation packets (D89); what it
 * prints is read through C14.
 *
 * It also reads the manifest of the release of this product that is running,
 * where the library says it would be, with the sha256 of its bytes (C1), for
 * the record of the release that builds the product (REQ-FLOW-010).
 *
 * @uses C15 C12 C14 C1 H2
 * @is REQ-FLOW-001 REQ-FLOW-002 REQ-FLOW-010 REQ-INTERFACE-002
 */
import * as Context from "effect/Context"
import * as Effect from "effect/Effect"
import * as FileSystem from "effect/FileSystem"
import * as Layer from "effect/Layer"
import type * as ChildProcessSpawner from "effect/process/ChildProcessSpawner"
import { sha256Of } from "../kit/content_addressing.js"
import { createIfAbsent } from "../kit/create_if_absent.js"
import { anything, read } from "../kit/lossless_encoding.js"
import { byName } from "../kit/order_by_name.js"
import { supervise } from "../kit/supervised_child.js"

/** The method's release manager, which installs and verifies the release a definition file selects. */
export const METHOD_MANAGER = ["stdo", "sync", "--definition"] as const
/** The same manager, asked where it keeps a release, by the release's identity. */
export const METHOD_RESOLVER = ["stdo", "resolve"] as const

/** When a file was last written, in milliseconds, and the node of the disk that holds it. */
export interface Stamp {
  readonly written: number
  readonly node: string
}

/** A file could not be read or written, and why. */
export class FileRefused {
  readonly _tag = "FileRefused"
  constructor(readonly path: string, readonly why: string) {}
}

export class Files extends Context.Service<Files, {
  /** The text of a file, or undefined where there is none. */
  readonly read: (path: string) => Effect.Effect<string | undefined>
  /** The text of a file and the sha256 of its bytes (C1), or undefined where there is none. */
  readonly hashed: (path: string) => Effect.Effect<{ readonly text: string; readonly sha256: string } | undefined>
  /** When a file was last written and which node of the disk holds it, or undefined where there is none. */
  readonly stamp: (path: string) => Effect.Effect<Stamp | undefined>
  /** Writes a file of the framework's own, making its folder. */
  readonly write: (path: string, text: string) => Effect.Effect<void, FileRefused>
  /** Writes a file only where there is none (C15). */
  readonly create: (path: string, text: string) => Effect.Effect<"written" | "there", FileRefused>
  /** The names in a folder, sorted; none where there is no folder. */
  readonly list: (folder: string) => Effect.Effect<readonly string[]>
  readonly exists: (path: string) => Effect.Effect<boolean>
  /** Moves a file, making the folder it goes to. */
  readonly move: (from: string, to: string) => Effect.Effect<void, FileRefused>
  /** The path with every link followed. */
  readonly real: (path: string) => Effect.Effect<string, FileRefused>
  /** Makes a folder, and the folders it lies in, where they are not there. */
  readonly makeFolder: (path: string) => Effect.Effect<void, FileRefused>
  /** Has the method's release manager install and verify the release the definition file selects. */
  readonly installMethod: (definition: string, folder: string) => Effect.Effect<{ readonly installed: string } | { readonly refused: string }>
  /** Where the method's release manager keeps the release of this identity, or undefined where it cannot say. */
  readonly methodAt: (uri: string, folder: string) => Effect.Effect<string | undefined>
}>()("stdo-builder/Files") {}

const folderOf = (file: string): string => file.slice(0, Math.max(0, file.lastIndexOf("/")))

export const filesLive: Layer.Layer<Files, never, FileSystem.FileSystem | ChildProcessSpawner.ChildProcessSpawner> = Layer.effect(
  Files,
  Effect.gen(function*() {
    const fs = yield* FileSystem.FileSystem
    const context = yield* Effect.context<ChildProcessSpawner.ChildProcessSpawner>()
    const refused = (path: string) => (e: { readonly message: string }) => new FileRefused(path, e.message)
    return Files.of({
      read: (path) => fs.readFileString(path).pipe(Effect.orElseSucceed(() => undefined)),
      hashed: (path) =>
        fs.readFile(path).pipe(
          Effect.flatMap((bytes) => Effect.all([fs.readFileString(path), sha256Of(bytes)])),
          Effect.map(([text, sha256]) => ({ text, sha256 })),
          Effect.orElseSucceed(() => undefined)
        ),
      stamp: (path) =>
        fs.stat(path).pipe(
          Effect.map((info): Stamp => ({
            written: info.mtime._tag === "Some" ? info.mtime.value.getTime() : 0,
            node: info.ino._tag === "Some" ? String(info.ino.value) : ""
          })),
          Effect.orElseSucceed(() => undefined)
        ),
      write: (path, text) =>
        fs.makeDirectory(folderOf(path), { recursive: true }).pipe(
          Effect.andThen(fs.writeFileString(path, text)),
          Effect.mapError(refused(path))
        ),
      create: (path, text) =>
        createIfAbsent(path, text).pipe(
          Effect.mapError((e) => new FileRefused(path, e.why)),
          Effect.provideService(FileSystem.FileSystem, fs)
        ),
      list: (folder) => fs.readDirectory(folder).pipe(Effect.map((names) => byName(names)), Effect.orElseSucceed(() => [])),
      exists: (path) => fs.exists(path).pipe(Effect.orElseSucceed(() => false)),
      move: (from, to) =>
        fs.makeDirectory(folderOf(to), { recursive: true }).pipe(Effect.andThen(fs.rename(from, to)), Effect.mapError(refused(from))),
      real: (path) => fs.realPath(path).pipe(Effect.mapError(refused(path))),
      makeFolder: (path) => fs.makeDirectory(path, { recursive: true }).pipe(Effect.mapError(refused(path))),
      installMethod: (definition, folder) => {
        const [command, ...args] = METHOD_MANAGER
        return supervise({ command, args: [...args, definition], cwd: folder, deadline: 10 * 60_000 }).pipe(
          Effect.provideContext(context),
          Effect.map((o) =>
            o.outcome === "returned" && o.code === 0
              ? { installed: o.output.trim() }
              : { refused: o.outcome === "returned" ? (o.errors || o.output).trim() : o.outcome === "ran over" ? "it ran over" : `${o.outcome}: ${o.why}` }
          )
        )
      },
      methodAt: (uri, folder) => {
        const [command, ...args] = METHOD_RESOLVER
        return supervise({ command, args: [...args, uri], cwd: folder, deadline: 60_000 }).pipe(
          Effect.provideContext(context),
          Effect.map((o) => {
            const got = o.outcome === "returned" && o.code === 0 ? read(anything, o.output) : undefined
            const said = got !== undefined && "value" in got && typeof got.value === "object" && got.value !== null && !Array.isArray(got.value)
              ? new Map(Object.entries(got.value)).get("path")
              : undefined
            return typeof said === "string" ? said : undefined
          })
        )
      }
    })
  })
)
