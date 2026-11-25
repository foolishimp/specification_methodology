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
import * as Context from "effect/Context"
import * as Effect from "effect/Effect"
import * as Layer from "effect/Layer"
import type * as ChildProcessSpawner from "effect/process/ChildProcessSpawner"
import { differenceNow, filesOf, folderTreeAt, identitiesOf, identityOfText, textAt, textOf, treeDifference, underCommit, type Identities, type IdentityMap } from "../kit/content_addressing.js"
import * as Lines from "../kit/three_way_merge.js"

/** Git could not do what the framework asked, and why. */
export class GitRefused {
  readonly _tag = "GitRefused"
  constructor(readonly folder: string, readonly why: string) {}
}

export type { Identities, IdentityMap }
export type Merged = Lines.Merged
export type Committed = Lines.Committed
export type Switched = Lines.Switched
export type Happened = Lines.Happened
export type Differs = Lines.Differs

export class Git extends Context.Service<Git, {
  /** The identity of a whole folder, of each file and folder at `places` and of the folder beside the places `apart`, from git's index of identities at `index`, which follows what changed; `fresh` where there is none there yet (C1). */
  readonly identities: (folder: string, index: string, places: readonly string[], fresh: boolean, apart?: readonly string[]) => Effect.Effect<Identities, GitRefused>
  /** The identity at `from` and at `to` of each path whose identity differs between two identities of the folder; none where git no longer holds `from` (C1, D226). */
  readonly treeDifference: (folder: string, from: string, to: string) => Effect.Effect<{ readonly start: IdentityMap; readonly end: IdentityMap } | undefined, GitRefused>
  /** The same, between the tree `from` and the folder now, read through the index of identities at `index` and writing nothing (C1, D242). */
  readonly differenceNow: (folder: string, index: string, from: string) => Effect.Effect<{ readonly start: IdentityMap; readonly end: IdentityMap } | undefined, GitRefused>
  /** The tree of the folder in a commit (C1, D241). */
  readonly folderTreeAt: (folder: string, commit: string) => Effect.Effect<string, GitRefused>
  /** Each branch, tag and the stash, by its full name, with the commit it is on (C13, D228). */
  readonly refs: (folder: string) => Effect.Effect<ReadonlyMap<string, string>, GitRefused>
  /** What git lists as changed, staged or untracked under the repository's top, outside `within`, by path from the top, with whether git tracks it (C13, D228, D243). */
  readonly outside: (top: string, within: string) => Effect.Effect<ReadonlyMap<string, "tracked" | "untracked">, GitRefused>
  /** Of the paths given, from the repository's top, those a commit holds (C13, D243). */
  readonly heldBy: (top: string, commit: string, paths: readonly string[]) => Effect.Effect<ReadonlySet<string>, GitRefused>
  /** Each file outside `within` that differs between two commits, by path from the repository's top, with what happened to it; no content read (C13, D256). */
  readonly committedOutside: (top: string, within: string, from: string, to: string) => Effect.Effect<readonly (readonly [string, Lines.Happened])[], GitRefused>
  /** Each file anywhere in the repository that differs between two commits, by path from its top, with what happened to it and the identity each commit gives it; no content read (C13, D257). */
  readonly differsBetween: (top: string, from: string, to: string) => Effect.Effect<readonly Lines.Differs[], GitRefused>
  /** The files git holds in the folder or does not ignore there. */
  readonly files: (folder: string) => Effect.Effect<readonly string[], GitRefused>
  readonly identityOfText: (folder: string, text: string) => Effect.Effect<string, GitRefused>
  /** The text of the file git holds under an identity (C1). */
  readonly textOf: (folder: string, identity: string) => Effect.Effect<string, GitRefused>
  /** The identity of each place that is there under a commit, from the folder; none where git does not hold the commit (REQ-ALG-004). */
  readonly underCommit: (folder: string, commit: string, places: readonly string[]) => Effect.Effect<ReadonlyMap<string, string> | undefined, GitRefused>
  /** The text of a file under a commit, from the folder; none where there is none. */
  readonly textAt: (folder: string, commit: string, path: string) => Effect.Effect<string | undefined>
  /** The subject of each merge a line holds, newest first. */
  readonly mergeSubjects: (folder: string, line: string) => Effect.Effect<readonly string[], GitRefused>
  /** Git's version, as `git --version` gives it, such as `2.50.1`; none where it gives no version (D248). */
  readonly version: () => Effect.Effect<string | undefined, GitRefused>
  /** The top folder of the repository the folder lies in; none where git says it is in no repository. */
  readonly topOf: (folder: string) => Effect.Effect<string | undefined, GitRefused>
  /** Git's own directory for the folder, by its absolute path: in a linked working tree, that tree's own (REQ-FLOW-001, D245). */
  readonly gitDirOf: (folder: string) => Effect.Effect<string, GitRefused>
  /** Whether the repository whose top folder is `top` ignores the folder at `path`, from that top. */
  readonly ignores: (top: string, path: string) => Effect.Effect<boolean, GitRefused>
  readonly makeRepository: (folder: string, line: string) => Effect.Effect<void, GitRefused>
  /** The line the folder has checked out; none where its HEAD names no line. */
  readonly currentLine: (folder: string) => Effect.Effect<string | undefined, GitRefused>
  readonly tipOf: (folder: string, name: string) => Effect.Effect<string | undefined, GitRefused>
  /** Commits what the folder holds, or only `paths`, on the line named `line`, staging where it must in an index of the commit's own at `index`, in a place git ignores within the folder; none where nothing changed, and the files where git could not merge them. Below the top of a repository, a merge in progress is completed only where it takes in what the line `taken` holds (D240). */
  readonly commit: (folder: string, index: string, line: string, message: string, paths?: readonly string[], taken?: string) => Effect.Effect<Committed, GitRefused>
  /** Commits on `line` the file at `path` as `text` gives it, and nothing else the folder holds; none where the line's tip holds that text there (REQ-FLOW-006 step 3, D227). */
  readonly commitText: (folder: string, index: string, line: string, message: string, path: string, text: string) => Effect.Effect<string | undefined, GitRefused>
  /** Puts the file at `path` as the line `from` has it in the folder, by git. */
  readonly takeFrom: (folder: string, from: string, path: string) => Effect.Effect<void, GitRefused>
  /** Makes the line `line` at `commit`, where there is none (D239). */
  readonly makeLine: (folder: string, line: string, commit: string) => Effect.Effect<void, GitRefused>
  /** Puts the folder on the line `line`; git's refusal, with the working tree that has it checked out where that is why (D239). */
  readonly switchTo: (folder: string, line: string) => Effect.Effect<Lines.Switched, GitRefused>
  /** The working tree, other than the folder's own, that has the line `line` checked out; none where no other has it (D239). */
  readonly heldElsewhere: (folder: string, line: string) => Effect.Effect<string | undefined, GitRefused>
  /** The lines the repository has as remote branches, named one of `names` or below one, each with the full name of a remote branch (D239). */
  readonly remoteLines: (folder: string, names: readonly string[]) => Effect.Effect<ReadonlyMap<string, string>, GitRefused>
  /** Of the files asked for, by a name of git's and a path from the folder, those git holds, by their place in the list (D239). */
  readonly presentAt: (folder: string, asked: readonly (readonly [string, string])[]) => Effect.Effect<ReadonlySet<number>, GitRefused>
  /** The names of the files at a folder's path under a name of git's (D239). */
  readonly namesAt: (folder: string, rev: string, path: string) => Effect.Effect<readonly string[], GitRefused>
  /** Takes the line `from` into `line`, which the folder is on, in the folder (D240). */
  readonly takeInto: (folder: string, line: string, from: string, message: string) => Effect.Effect<Merged, GitRefused>
  /** Merges `from` into `line`, an ancestor of it, by `commit-tree`, `update-ref` and `symbolic-ref`, writing no file (D240). */
  readonly mergeInto: (folder: string, line: string, from: string, message: string) => Effect.Effect<Lines.MergedInto, GitRefused>
  readonly holdsAll: (folder: string, name: string) => Effect.Effect<boolean, GitRefused>
  readonly changedLines: (folder: string, from: string, to?: string) => Effect.Effect<readonly Lines.Changed[], GitRefused>
  /** The commit where `from` and the line `name` last met; none where they share none. */
  readonly mergeBase: (folder: string, from: string, name: string) => Effect.Effect<string | undefined, GitRefused>
  /** The commits the line `line` holds and `from` does not, but merges, whose message is `message` alone and which change a file at `paths`; oldest first (D244). */
  readonly commitsWith: (folder: string, from: string, line: string, message: string, paths: readonly string[]) => Effect.Effect<readonly string[], GitRefused>
  /** The lines named one of `names`, or below one. */
  readonly linesNamed: (folder: string, names: readonly string[]) => Effect.Effect<readonly string[], GitRefused>
  readonly mergesOn: (folder: string, line: string) => Effect.Effect<readonly { readonly commit: string; readonly parents: readonly string[] }[], GitRefused>
}>()("stdo-builder/Git") {}

export const gitLive: Layer.Layer<Git, never, ChildProcessSpawner.ChildProcessSpawner> = Layer.effect(
  Git,
  Effect.gen(function*() {
    const context = yield* Effect.context<ChildProcessSpawner.ChildProcessSpawner>()
    const lift = <A>(e: Effect.Effect<A, { readonly folder: string; readonly why: string }, ChildProcessSpawner.ChildProcessSpawner>) =>
      e.pipe(Effect.mapError((r) => new GitRefused(r.folder, r.why)), Effect.provideContext(context))
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
    })
  })
)
