/**
 * The event log of a governed product (REQ-FLOW-007): one log, in the main
 * checkout's local folder, added to by every run whichever ticket it works on.
 * Each entry names nodes, vectors, checks and files by name, path or content
 * identity and holds no content of an asset. Every entry a run adds names the
 * run by its id. The framework takes no decision from it; a run only adds to
 * it, and says so when it finds none.
 *
 * @uses C10 C14 C16 C17
 * @is REQ-FLOW-007
 */
import { using } from "../kit/calculus.js"
import { now } from "../kit/clock.js"
import { EventLog, type Entry } from "../services/log.js"
import type { Flow } from "../services/services.js"
import { at, PLACES, type Fault } from "./workspace.js"

export type Note = Omit<Entry, "at">

export const logOf = (root: string): string => at(root, PLACES.log)

/** Adds one entry, stamped with the time. */
export const note = (root: string, entry: Note): Flow<void, Fault> =>
  using(EventLog, (log) => log.append(logOf(root), { at: now().written, ...entry }))

/** Whether the log is there. */
export const logFound = (root: string): Flow<boolean> => using(EventLog, (log) => log.exists(logOf(root)))
