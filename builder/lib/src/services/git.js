/**
 * The git service: content identities (C1), and the lines of work: a
 * repository, a ticket's branch and the folder put on it, commits, taking main
 * in, merges and what a line changed (C13). REQ-FLOW-001: "Open a branch",
 * "Commit", "Merge". A branch is made by git and by nothing else; nothing here
 * makes or prunes a working tree, copies the workspace, reverts, resets or
 * deletes a branch (D238). Each is asked of the workspace's folder, by paths
 * from it, also where it lies below the top of a larger repository (D201).
 *
 * @uses C1 C13 C12
 * @is REQ-FLOW-001 REQ-FLOW-008 REQ-ALG-001 REQ-INTERFACE-001
 */
import * as Context from "effect/Context";
import * as Effect from "effect/Effect";
import * as Layer from "effect/Layer";
import { differenceNow, filesOf, folderTreeAt, identitiesOf, identityOfText, textAt, textOf, treeDifference, underCommit } from "../kit/content_addressing.js";
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
        treeDifference: (folder, from, to) => lift(treeDifference(folder, from, to)),
        differenceNow: (folder, index, from) => lift(differenceNow(folder, index, from)),
        folderTreeAt: (folder, commit) => lift(folderTreeAt(folder, commit)),
        heldBy: (top, commit, paths) => lift(Lines.heldBy(top, commit, paths)),
        committedOutside: (top, within, from, to) => lift(Lines.committedOutside(top, within, from, to)),
        differsBetween: (top, from, to) => lift(Lines.differsBetween(top, from, to)),
        refs: (folder) => lift(Lines.refs(folder)),
        outside: (top, within) => lift(Lines.outside(top, within)),
        identityOfText: (folder, text) => lift(identityOfText(folder, text)),
        textOf: (folder, identity) => lift(textOf(folder, identity)),
        underCommit: (folder, commit, places) => lift(underCommit(folder, commit, places)),
        textAt: (folder, commit, path) => textAt(folder, commit, path).pipe(Effect.provideContext(context)),
        mergeSubjects: (folder, line) => lift(Lines.mergeSubjects(folder, line)),
        version: () => lift(Lines.versionOf()),
        topOf: (folder) => lift(Lines.topOf(folder)),
        gitDirOf: (folder) => lift(Lines.gitDirOf(folder)),
        ignores: (top, path) => lift(Lines.ignores(top, path)),
        makeRepository: (folder, line) => lift(Lines.makeRepository(folder, line)),
        currentLine: (folder) => lift(Lines.currentLine(folder)),
        tipOf: (folder, name) => lift(Lines.tipOf(folder, name)),
        commit: (folder, index, line, message, paths, taken) => lift(Lines.commit(folder, index, line, message, paths, taken)),
        commitText: (folder, index, line, message, path, text) => lift(Lines.commitText(folder, index, line, message, path, text)),
        takeFrom: (folder, from, path) => lift(Lines.takeFrom(folder, from, path)),
        makeLine: (folder, line, commit) => lift(Lines.makeLine(folder, line, commit)),
        switchTo: (folder, line) => lift(Lines.switchTo(folder, line)),
        heldElsewhere: (folder, line) => lift(Lines.heldElsewhere(folder, line)),
        remoteLines: (folder, names) => lift(Lines.remoteLines(folder, names)),
        presentAt: (folder, asked) => lift(Lines.presentAt(folder, asked)),
        namesAt: (folder, rev, path) => lift(Lines.namesAt(folder, rev, path)),
        takeInto: (folder, line, from, message) => lift(Lines.takeInto(folder, line, from, message)),
        mergeInto: (folder, line, from, message) => lift(Lines.mergeInto(folder, line, from, message)),
        holdsAll: (folder, name) => lift(Lines.holdsAll(folder, name)),
        changedLines: (folder, from, to) => lift(Lines.changedLines(folder, from, to)),
        mergeBase: (folder, from, name) => lift(Lines.mergeBase(folder, from, name)),
        commitsWith: (folder, from, line, message, paths) => lift(Lines.commitsWith(folder, from, line, message, paths)),
        linesNamed: (folder, names) => lift(Lines.linesNamed(folder, names)),
        mergesOn: (folder, line) => lift(Lines.mergesOn(folder, line))
    });
}));
