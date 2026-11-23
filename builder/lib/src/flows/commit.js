/**
 * A commit (REQ-FLOW-001, "Commit"). Every commit the framework makes, a
 * step's result, an answer, what the user left on main, a move on the board
 * and set-up, is made here: git commits what the folder holds, files git
 * ignores left out, or only the paths named, on the folder's line by its name
 * (C13). Where git stages in an index of the commit's own, it keeps that index
 * in the folder's local place, beside C1's index of identities, so nothing is
 * kept outside the workspace (REQ-FLOW-001, D201).
 *
 * @uses C13 C17
 * @is REQ-FLOW-001 REQ-FLOW-005
 */
import { decide, end, fault, sequence, using } from "../kit/calculus.js";
import { Files } from "../services/files.js";
import { Git, GitRefused } from "../services/git.js";
import { at, LOCAL, PLACES } from "./workspace.js";
/** Commits the folder on its line with `message`, the whole of it or only `paths`. Gives the new commit, none where nothing changed, or the files git could not merge, and then commits nothing. */
export const commitOf = (on, message, paths) => using(Files, (files) => using(Git, (git) => sequence(files.makeFolder(at(on.folder, LOCAL)), git.commit(on.folder, at(on.folder, PLACES.commitIndex), on.line, message, paths))));
/** As `commitOf`, where git leaving a merge it could not make is no ending of the flow's own: it is refused. */
export const committed = (on, message, paths) => decide(commitOf(on, message, paths), (c) => "unresolved" in c
    ? fault(new GitRefused(on.folder, `git could not merge ${c.unresolved.join(", ")}, and the merge is not resolved`))
    : end(c.commit));
