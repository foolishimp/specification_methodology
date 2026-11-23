/**
 * Create if absent: a file is written only where there is none; otherwise it
 * is reported and left as it is. Done twice, it changes nothing the second
 * time. The file appears whole: it is written beside its place, in a folder
 * of its own, and linked into place, which the file system does only where
 * nothing is; so no reader ever finds it half written.
 *
 * @carries C15
 */
import * as Effect from "effect/Effect"
import * as FileSystem from "effect/FileSystem"

/** The file could not be written, and why. */
export class CreateRefused {
  readonly _tag = "CreateRefused"
  constructor(readonly file: string, readonly why: string) {}
}

const folderOf = (file: string): string => file.slice(0, Math.max(0, file.lastIndexOf("/")))

/** "written" where there was no file, "there" where there was one, which is not touched. */
export const createIfAbsent = (file: string, text: string): Effect.Effect<"written" | "there", CreateRefused, FileSystem.FileSystem> =>
  Effect.gen(function*() {
    const fs = yield* FileSystem.FileSystem
    if (yield* fs.exists(file)) return "there" as const
    const folder = folderOf(file)
    const name = file.slice(file.lastIndexOf("/") + 1)
    yield* fs.makeDirectory(folder, { recursive: true })
    const beside = yield* fs.makeTempDirectory({ directory: folder, prefix: `.${name}.` })
    return yield* fs.writeFileString(`${beside}/${name}`, text).pipe(
      Effect.flatMap(() => fs.link(`${beside}/${name}`, file)),
      Effect.as("written" as const),
      Effect.catch((error) =>
        fs.exists(file).pipe(Effect.flatMap((there) => (there ? Effect.succeed("there" as const) : Effect.fail(error))))
      ),
      Effect.ensuring(fs.remove(beside, { recursive: true, force: true }).pipe(Effect.ignore))
    )
  }).pipe(Effect.mapError((e) => new CreateRefused(file, e.message)))
