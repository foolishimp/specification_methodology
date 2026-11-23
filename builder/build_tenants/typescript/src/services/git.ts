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
import * as Context from "effect/Context"
import * as Effect from "effect/Effect"
import * as Layer from "effect/Layer"
import type * as ChildProcessSpawner from "effect/process/ChildProcessSpawner"
import { filesOf, identitiesOf, identityOfText, textAt, textOf, underCommit, type Identities, type IdentityMap } from "../kit/content_addressing.js"
import * as Lines from "../kit/three_way_merge.js"

/** Git could not do what the framework asked, and why. */
export class GitRefused {
  readonly _tag = "GitRefused"
  constructor(readonly folder: string, readonly why: string) {}
}

export type { Identities, IdentityMap }
export type Merged = Lines.Merged
export type Committed = Lines.Committed

export class Git extends Context.Service<Git, {
  /** The identity of a whole folder, of each file and folder at `places` and of the folder beside the places `apart`, from git's index of identities at `index`, which follows what changed; `fresh` where there is none there yet (C1). */
  readonly identities: (folder: string, index: string, places: readonly string[], fresh: boolean, apart?: readonly string[]) => Effect.Effect<Identities, GitRefused>
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
  /** The top folder of the repository the folder lies in; none where git says it is in no repository. */
  readonly topOf: (folder: string) => Effect.Effect<string | undefined, GitRefused>
  /** Whether the repository whose top folder is `top` ignores the folder at `path`, from that top. */
  readonly ignores: (top: string, path: string) => Effect.Effect<boolean, GitRefused>
  readonly makeRepository: (folder: string, line: string) => Effect.Effect<void, GitRefused>
  /** The line the folder has checked out; none where its HEAD names no line. */
  readonly currentLine: (folder: string) => Effect.Effect<string | undefined, GitRefused>
  readonly tipOf: (folder: string, name: string) => Effect.Effect<string | undefined, GitRefused>
  /** Commits what the folder holds, or only `paths`, on the line named `line`, staging where it must in an index of the commit's own at `index`, in a place git ignores within the folder; none where nothing changed, and the files where git could not merge them. */
  readonly commit: (folder: string, index: string, line: string, message: string, paths?: readonly string[]) => Effect.Effect<Committed, GitRefused>
  /** Puts the file at `path` as the line `from` has it in the checkout, by git. */
  readonly takeFrom: (folder: string, from: string, path: string) => Effect.Effect<void, GitRefused>
  readonly checkoutOf: (repository: string, line: string, from: string, checkout: string) => Effect.Effect<void, GitRefused>
  /** Merges the line `from` into `line`; refused where the folder is not on `line`. */
  readonly merge: (folder: string, line: string, from: string, message: string, fastForward: boolean) => Effect.Effect<Merged, GitRefused>
  /** Merges the line `from` into `line` with a commit of the merge, in the repository's own folder, leaving what the user has not committed outside what the merge changed as it is. */
  readonly mergeInto: (folder: string, line: string, from: string, message: string) => Effect.Effect<Merged, GitRefused>
  readonly holdsAll: (folder: string, name: string) => Effect.Effect<boolean, GitRefused>
  readonly changedLines: (folder: string, from: string, to?: string) => Effect.Effect<readonly Lines.Changed[], GitRefused>
  /** The commit where `from` and the line `name` last met; none where they share none. */
  readonly mergeBase: (folder: string, from: string, name: string) => Effect.Effect<string | undefined, GitRefused>
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
    })
  })
)
