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
import { using } from "../kit/calculus.js";
import { now } from "../kit/clock.js";
import { EventLog } from "../services/log.js";
import { at, PLACES } from "./workspace.js";
export const logOf = (root) => at(root, PLACES.log);
/** Adds one entry, stamped with the time. */
export const note = (root, entry) => using(EventLog, (log) => log.append(logOf(root), { at: now().written, ...entry }));
/** Whether the log is there. */
export const logFound = (root) => using(EventLog, (log) => log.exists(logOf(root)));
