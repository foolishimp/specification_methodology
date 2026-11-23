/**
 * The stand-in agent of the scenarios: a second layer of the sessions service
 * that writes fixed files and uses no language model (REQ-FLOW-001,
 * acceptance 1). No flow changes when it is used. Its fixed files are given to
 * it as a folder, which holds, for a vector and a kind of session:
 *
 * - `<vector>/<kind>/files/...`: files written into the checkout at the same
 *   paths;
 * - `<vector>/<kind>/append`: text added to the end of the file the brief names
 *   to produce (for the first vector, the ticket);
 * - `<vector>/<kind>/seconds`: how long the session goes on after writing;
 * - `<vector>/<kind>/print`: the text the session prints;
 * - `<vector>/<kind>/fails`: the session fails after it has written and
 *   printed, with the why "the stand-in was told to fail".
 *
 * A vector and kind with no folder is a session that cannot be started. It
 * stands in for whichever agent the settings name, and is named in the event
 * log as the stand-in for that agent.
 *
 * @uses C12 C16 H2
 * @is REQ-FLOW-001 REQ-VERIFY-002
 */
import * as Effect from "effect/Effect"
import * as FileSystem from "effect/FileSystem"
import * as Layer from "effect/Layer"
import { now } from "../kit/clock.js"
import { byName } from "../kit/order_by_name.js"
import { Sessions, type End } from "./sessions.js"

/** The longest a gate holds a session. */
const GATE_MINUTES = 5

const folderOf = (file: string): string => file.slice(0, Math.max(0, file.lastIndexOf("/")))

export const standInSessions = (fixtures: string): Layer.Layer<Sessions, never, FileSystem.FileSystem> =>
  Layer.effect(
    Sessions,
    Effect.gen(function*() {
      const fs = yield* FileSystem.FileSystem
      return Sessions.of({
        // It stands in for the agent the settings name, and the log says both.
        agentOf: (named) => `stand-in for ${named}`,
        start: (call) =>
          Effect.gen(function*() {
            const began = now().millis
            const here = `${fixtures}/${call.vector}/${call.kind}`
            if (!(yield* fs.exists(here))) {
              const why = `the stand-in has no fixed files for ${call.vector} (${call.kind})`
              return { ended: "failed", seconds: 0, why, printed: why } satisfies End
            }
            const files = `${here}/files`
            if (yield* fs.exists(files)) {
              for (const path of byName(yield* fs.readDirectory(files, { recursive: true }))) {
                if ((yield* fs.stat(`${files}/${path}`)).type !== "File") continue
                const to = `${call.checkout}/${path}`
                yield* fs.makeDirectory(folderOf(to), { recursive: true })
                yield* fs.writeFile(to, yield* fs.readFile(`${files}/${path}`))
              }
            }
            if ((yield* fs.exists(`${here}/append`)) && call.brief.kind === "work") {
              yield* fs.writeFileString(`${call.checkout}/${call.brief.produce[0]?.place ?? ""}`, yield* fs.readFileString(`${here}/append`), { flag: "a" })
            }
            if (yield* fs.exists(`${here}/seconds`)) yield* Effect.sleep(Number((yield* fs.readFileString(`${here}/seconds`)).trim()) * 1000)
            // A gate: the session returns only once the file the gate names is there, so a driver can act while it is at work.
            if (yield* fs.exists(`${here}/gate`)) {
              const opens = (yield* fs.readFileString(`${here}/gate`)).trim()
              const until = now().millis + GATE_MINUTES * 60_000
              while (!(yield* fs.exists(opens)) && now().millis < until) yield* Effect.sleep(100)
            }
            const printed = (yield* fs.exists(`${here}/print`)) ? yield* fs.readFileString(`${here}/print`) : ""
            const seconds = (now().millis - began) / 1000
            if (yield* fs.exists(`${here}/fails`)) return { ended: "failed", seconds, why: "the stand-in was told to fail", printed } satisfies End
            return { ended: "returned", seconds, printed } satisfies End
          }).pipe(Effect.catch((e) => {
            const why = `the stand-in could not write: ${e.message}`
            return Effect.succeed({ ended: "failed", seconds: 0, why, printed: why } satisfies End)
          }))
      })
    })
  )
