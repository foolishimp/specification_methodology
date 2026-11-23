/**
 * The user's command to record the release that builds the product
 * (REQ-FLOW-010): the settings on main are given the record of the release of
 * this product that is running, in place of the record there was. It changes
 * nothing else, adds nothing to the event log and commits nothing: the next
 * run commits it as the user's, with what else the user left uncommitted on
 * main (REQ-FLOW-001). Where the settings already record what is running, it
 * writes nothing.
 *
 * The settings are read as any value and written back in their one written
 * form (C14), each field as it was and in its place; a record not there is put
 * after the definition file's name, where set-up puts it (D197).
 *
 * It is the term `record` of the calculus page (section 5).
 *
 * @uses C14 C17
 * @is REQ-FLOW-010 REQ-FLOW-001 REQ-FLOW-007
 */
import { decide, end, sequence, using } from "../kit/calculus.js"
import { anything, read, write } from "../kit/lossless_encoding.js"
import { Files } from "../services/files.js"
import type { Flow } from "../services/services.js"
import { note } from "./events.js"
import { at, open, PLACES, recordedIn, releaseWords, running, sameBuilder, type Builder, type BuilderRecord, type Fault, type Opened } from "./workspace.js"

/** What the command gives: why `open` refused it; that the settings do not read as an object; or what is now recorded, what was, and whether the file changed. */
export type RecordGiven =
  | Exclude<Opened, { readonly root: string }>
  | { readonly refused: "settings" }
  | { readonly recorded: Builder; readonly was: BuilderRecord; readonly changed: boolean }

/** The record's field in the settings. */
const FIELD = "builder"

/** The settings' fields with the record given `builder`: in its place where it is there, and otherwise after the definition file's name, or at the end. */
const withRecord = (fields: readonly (readonly [string, unknown])[], builder: Builder): readonly (readonly [string, unknown])[] =>
  fields.some(([name]) => name === FIELD)
    ? fields.map(([name, value]) => [name, name === FIELD ? builder : value] as const)
    : fields.some(([name]) => name === "definition")
    ? fields.flatMap(([name, value]) => (name === "definition" ? [[name, value] as const, [FIELD, builder] as const] : [[name, value] as const]))
    : [...fields, [FIELD, builder] as const]

/** Records the release whose manifest would be at `manifest` as the one that builds the product in `folder`. */
export const recordRelease = (folder: string, manifest: string): Flow<RecordGiven, Fault> =>
  decide(open(folder), (opened): Flow<RecordGiven, Fault> => {
    if ("refused" in opened) return end(opened)
    const place = at(opened.root, PLACES.settings)
    return using(Files, (files) =>
      decide(files.read(place), (text) =>
        decide(running(manifest), (now): Flow<RecordGiven, Fault> => {
          const got = read(anything, text ?? "")
          const value = "value" in got ? got.value : undefined
          if (typeof value !== "object" || value === null || Array.isArray(value)) return end({ refused: "settings" })
          const was = recordedIn(text ?? "")
          if ("builder" in was && sameBuilder(was.builder, now)) return end({ recorded: now, was, changed: false })
          return sequence(
            files.write(place, write(anything, Object.fromEntries(withRecord(Object.entries(value), now)))),
            note(opened.root, { event: "release recorded", path: PLACES.settings, release: releaseWords({ builder: now }) }),
            end({ recorded: now, was, changed: true })
          )
        })))
  })
