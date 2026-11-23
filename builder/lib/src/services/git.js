/**
 * The git service: content identities (C1), and the lines of work: a
 * repository, a ticket's branch and its checkout, commits, merges and what a
 * line changed (C13). REQ-FLOW-001: "Open a branch", "Commit", "Merge". A
 * branch and its checkout are made by git and by nothing else; nothing here
 * copies the workspace, reverts, resets or deletes a branch. Each is asked of
 * a folder, and concerns only files under it, by their paths from it, also
 * where it lies below the top of a larger repository (D201).
 *
 * @uses C1 C13 C12
 * @is REQ-FLOW-001 REQ-FLOW-008 REQ-ALG-001
 */
import * as Context from "effect/Context";
import * as Effect from "effect/Effect";
import * as Layer from "effect/Layer";
import { filesOf, identitiesOf, identityOfText, textAt, textOf, underCommit } from "../kit/content_addressing.js";
import * as Lines from "../kit/three_way_merge.js";
/** Git could not do what the framework asked, and why. */
export class GitRefused {
    folder;
    why;
    _tag = "GitRefused";
    constructor(folder, why) {
        this.folder = folder;
        this.why = why;
    }
}
export class Git extends Context.Service()("stdo-builder/Git") {
}
export const gitLive = Layer.effect(Git, Effect.gen(function* () {
    const context = yield* Effect.context();
    const lift = (e) => e.pipe(Effect.mapError((r) => new GitRefused(r.folder, r.why)), Effect.provideContext(context));
    return Git.of({
        identities: (folder, index, places, fresh, apart) => lift(identitiesOf(folder, index, places, fresh, apart)),
        files: (folder) => lift(filesOf(folder)),
        identityOfText: (folder, text) => lift(identityOfText(folder, text)),
        textOf: (folder, identity) => lift(textOf(folder, identity)),
        underCommit: (folder, commit, places) => lift(underCommit(folder, commit, places)),
        textAt: (folder, commit, path) => textAt(folder, commit, path).pipe(Effect.provideContext(context)),
        mergeSubjects: (folder, line) => lift(Lines.mergeSubjects(folder, line)),
        topOf: (folder) => lift(Lines.topOf(folder)),
        ignores: (top, path) => lift(Lines.ignores(top, path)),
        makeRepository: (folder, line) => lift(Lines.makeRepository(folder, line)),
        currentLine: (folder) => lift(Lines.currentLine(folder)),
        tipOf: (folder, name) => lift(Lines.tipOf(folder, name)),
        commit: (folder, index, line, message, paths) => lift(Lines.commit(folder, index, line, message, paths)),
        takeFrom: (folder, from, path) => lift(Lines.takeFrom(folder, from, path)),
        checkoutOf: (repository, line, from, checkout) => lift(Lines.checkoutOf(repository, line, from, checkout)),
        merge: (folder, line, from, message, fastForward) => lift(Lines.merge(folder, line, from, message, fastForward)),
        mergeInto: (folder, line, from, message) => lift(Lines.mergeInto(folder, line, from, message)),
        holdsAll: (folder, name) => lift(Lines.holdsAll(folder, name)),
        changedLines: (folder, from, to) => lift(Lines.changedLines(folder, from, to)),
        mergeBase: (folder, from, name) => lift(Lines.mergeBase(folder, from, name)),
        linesNamed: (folder, names) => lift(Lines.linesNamed(folder, names)),
        mergesOn: (folder, line) => lift(Lines.mergesOn(folder, line))
    });
}));
