/**
 * The event log of a governed product (REQ-FLOW-007): one log, in the
 * workspace's local folder, added to by every run whichever ticket it works on.
 * Each entry names nodes, vectors, checks and files by name, path or content
 * identity and holds no content of an asset. Every entry a run adds names the
 * run by its id. The framework takes no decision from it; a run only adds to
 * it, and says so when it finds none. Where the log a run was adding to is gone
 * when the run next adds to it, the run starts a new one, whose first entry
 * says so, with the release in force, and says so once in its words (D247).
 *
 * @uses C10 C14 C16 C17
 * @is REQ-FLOW-007 REQ-FLOW-003
 */
import { decide, end, sequence, using } from "../kit/calculus.js";
import { now } from "../kit/clock.js";
import { Files } from "../services/files.js";
import { EventLog } from "../services/log.js";
import { at, PLACES, recordedIn, releaseWords } from "./workspace.js";
export const logOf = (root) => at(root, PLACES.log);
/** Adds one entry, stamped with the time. Where the entry is a run's and the log that run was adding to is gone, a new log is started first, whose first entry says so, with the release the settings record (REQ-FLOW-007, D247). */
export const note = (root, entry) => using(EventLog, (log) => decide(entry.run === undefined || entry.event === "run started" ? end(false) : log.gone(logOf(root)), (gone) => !gone
    ? log.append(logOf(root), { at: now().written, ...entry })
    : using(Files, (files) => decide(files.read(at(root, PLACES.settings)), (settings) => sequence(log.append(logOf(root), { at: now().written, event: "new log started", ...(entry.run === undefined ? {} : { run: entry.run }), release: releaseWords(recordedIn(settings ?? "")), why: "the event log this run was adding to was not found; this run starts a new one" }), log.append(logOf(root), { at: now().written, ...entry }))))));
/** How many times this run found the log it was adding to gone, and started a new one (D247). */
export const logsStarted = (root) => using(EventLog, (log) => log.startedAnew(logOf(root)));
/** Whether the log is there. */
export const logFound = (root) => using(EventLog, (log) => log.exists(logOf(root)));
