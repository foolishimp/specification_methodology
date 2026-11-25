/**
 * A commit (REQ-FLOW-001, "Commit"). Every commit the framework makes, a
 * step's result, an answer, what the user left on main, a move on the board
 * and set-up, is made here: git commits what the folder holds, files git
 * ignores left out, or only the paths named, on the folder's line by its name
 * (C13). Where git stages in an index of the commit's own, it keeps that index
 * in the folder's local place, beside C1's index of identities, so nothing is
 * kept outside the workspace (REQ-FLOW-001, D201).
 *
 * @uses C13 C17 H1
 * @is REQ-FLOW-001 REQ-FLOW-005
 */
import { decide, end, fault, sequence, using } from "../kit/calculus.js";
import { covers } from "../kit/place_containment.js";
import { Files } from "../services/files.js";
import { Git, GitRefused } from "../services/git.js";
import { at, LOCAL, PLACES } from "./workspace.js";
/** The message of the commit that holds what the user left uncommitted in the folder, the user's change by hand, and nothing else; an evaluating packet finds those commits by it (REQ-FLOW-003 step 1, REQ-ALG-007, D244). */
export const BY_HAND = "what the user changed by hand";
/**
 * Commits the folder on its line with `message`, the whole of it or only
 * `paths`. Gives the new commit, none where nothing changed, or the files git
 * could not merge, and then commits nothing. Below the top of a larger
 * repository, a merge in progress is completed only where it takes in what
 * the line `taken` holds: main, taken into the ticket's branch (D240); any
 * other is the user's, and is left as it is (D201).
 */
export const commitOf = (on, message, paths, taken) => using(Files, (files) => using(Git, (git) => sequence(files.makeFolder(at(on.folder, LOCAL)), git.commit(on.folder, at(on.folder, PLACES.commitIndex), on.line, message, paths, taken))));
/** Files git names from the repository's top, each by its path in the workspace where it lies in the folder at `within`; else from the repository's top, and said so (D49, D240). */
export const namedFrom = (within, files) => files.map((f) => (within === "" ? f : covers(within, f) ? f.slice(within.length + 1) : `${f} (from the repository's top, outside the workspace's folder)`));
/** Commits on the folder's line the file at `path` as `text` gives it, and nothing else the folder holds (REQ-FLOW-006 step 3, D227). Gives the new commit, none where the line holds that text there already. */
export const committedText = (on, message, path, text) => using(Files, (files) => using(Git, (git) => sequence(files.makeFolder(at(on.folder, LOCAL)), git.commitText(on.folder, at(on.folder, PLACES.commitIndex), on.line, message, path, text))));
/** As `commitOf`, where git leaving a merge it could not make is no ending of the flow's own: it is refused. */
export const committed = (on, message, paths) => decide(commitOf(on, message, paths), (c) => "unresolved" in c
    ? fault(new GitRefused(on.folder, `git could not merge ${namedFrom(c.within, c.unresolved).join(", ")}, and the merge is not resolved`))
    : end(c.commit));
