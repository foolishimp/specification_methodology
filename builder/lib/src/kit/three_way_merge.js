/**
 * Three-way merge from a common ancestor: git's merge of two lines of work.
 * This is the one module that asks git to keep lines of work: to say git's
 * version, to make a
 * repository and to say the top of the one a folder lies in and git's own
 * directory for it, to make a branch
 * and put the folder on it, to commit on the line the folder is on, to take
 * one line into another and merge one into another, and to say what a line
 * changed. It makes no second folder: no working tree is made or pruned
 * (REQ-FLOW-001, D238). It decides nothing about which side of a merge is
 * right. It starts git through the supervised child (C12).
 *
 * A commit is made the way git makes one, from the files of the folder, and
 * goes on the line the folder is on.
 *
 * The folder may lie below the top of the repository (REQ-FLOW-001, D201).
 * Git is then started in the folder, so each path it is given or gives is
 * from the folder, and every commit but one that takes main in or merges, and
 * every change it reads, concerns only files under it; taking main in and the
 * merge take the whole tree, since the repository's folder has one branch
 * checked out, and a file git could not merge is given from the repository's
 * top (D240). A merge of the user's own under way there is left as it is
 * (D201).
 *
 * @carries C13
 */
import * as Effect from "effect/Effect";
import { byName } from "./order_by_name.js";
import { covers } from "./place_containment.js";
import { supervise } from "./supervised_child.js";
/** Git could not do what it was asked, and why. */
export class LineRefused {
    folder;
    asked;
    why;
    _tag = "LineRefused";
    constructor(folder, asked, why) {
        this.folder = folder;
        this.asked = asked;
        this.why = why;
    }
}
const MINUTE = 60_000;
/** Git's own variables that would point it at another repository, index or object store; a child is started without them. */
const clean = {
    GIT_DIR: undefined,
    GIT_WORK_TREE: undefined,
    GIT_INDEX_FILE: undefined,
    GIT_COMMON_DIR: undefined,
    GIT_OBJECT_DIRECTORY: undefined,
    GIT_ALTERNATE_OBJECT_DIRECTORIES: undefined,
    GIT_NAMESPACE: undefined
};
/** The commits are the framework's: made under its name, with no hook or signing of the user's in the way. */
const env = {
    ...clean,
    GIT_AUTHOR_NAME: "STDO Builder",
    GIT_AUTHOR_EMAIL: "stdo-builder@localhost",
    GIT_COMMITTER_NAME: "STDO Builder",
    GIT_COMMITTER_EMAIL: "stdo-builder@localhost",
    GIT_TERMINAL_PROMPT: "0",
    GIT_EDITOR: "true"
};
/**
 * Git starts no upkeep of its own after a merge, either: that runs detached,
 * past the child's return and its deadline (C12), and at 100,000 files
 * (REQ-PARAM-001) it is still writing in the workspace when the command has
 * ended. The user's own git commands keep the repository as its settings say.
 */
const settings = ["-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null", "-c", "gc.auto=0", "-c", "maintenance.auto=false"];
const git = (folder, args, extra = {}, input) => supervise({ command: "git", args: [...settings, ...args], cwd: folder, deadline: 10 * MINUTE, env: { ...env, ...extra }, ...(input === undefined ? {} : { input }) }).pipe(Effect.flatMap((o) => o.outcome === "returned"
    ? Effect.succeed(o)
    : Effect.fail(new LineRefused(folder, args.join(" "), o.outcome === "ran over" ? "git ran over" : o.why))));
/** Git, which must exit with zero; its output. */
const must = (folder, args, extra = {}, input) => git(folder, args, extra, input).pipe(Effect.flatMap((o) => (o.code === 0 ? Effect.succeed(o.output) : Effect.fail(new LineRefused(folder, args.join(" "), o.errors.trim() || o.output.trim())))));
const parts = (output) => output.split("\0").filter((p) => p !== "");
/** The most bytes of paths one call of git is given, well within what a system lets one command line hold. */
const PATH_BYTES = 64 * 1024;
/** The paths in groups, each within PATH_BYTES, in their order: a commit may change every file of a workspace of 100,000 (REQ-PARAM-001). */
const inGroups = (paths) => {
    const groups = [];
    let bytes = PATH_BYTES;
    for (const path of paths) {
        // A UTF-16 unit of a path is at most three bytes on the command line.
        const size = 3 * path.length + 1;
        if (bytes + size > PATH_BYTES) {
            groups.push([]);
            bytes = 0;
        }
        groups[groups.length - 1]?.push(path);
        bytes += size;
    }
    return groups;
};
/**
 * Git's version, as `git --version` gives it, from its first line: the
 * numbers after `git version`, such as `2.50.1`; none where git gives no such
 * line. Git is asked that and nothing else, with no setting before it, in the
 * system's top folder, so the folder named need not be there (D248).
 */
export const versionOf = () => supervise({ command: "git", args: ["--version"], cwd: "/", deadline: MINUTE, env: { ...clean, LC_ALL: "C" } }).pipe(Effect.flatMap((o) => o.outcome === "returned"
    ? Effect.succeed(o.code === 0 ? /^git version ([0-9]+(?:\.[0-9]+)+)/.exec(o.output.trim())?.[1] : undefined)
    : Effect.fail(new LineRefused("/", "--version", o.outcome === "ran over" ? "git ran over" : o.why))));
/**
 * The top folder of the repository the folder lies in, as git gives it; none
 * only where git says the folder is in no repository. Git's words are read in
 * English, so this one call sets `LC_ALL=C`. Any other refusal is refused.
 */
export const topOf = (folder) => git(folder, ["rev-parse", "--show-toplevel"], { LC_ALL: "C" }).pipe(Effect.flatMap((o) => o.code === 0
    ? Effect.succeed(o.output.trim())
    : o.errors.includes("not a git repository")
        ? Effect.succeed(undefined)
        : Effect.fail(new LineRefused(folder, "rev-parse --show-toplevel", o.errors.trim() || o.output.trim()))));
/**
 * Git's own directory for the folder, by its absolute path, as git gives it
 * (`rev-parse --absolute-git-dir`): in a linked working tree, that tree's own.
 * Git's commands that clean the folder or stash what it holds do not reach it
 * (REQ-FLOW-001, D245).
 */
export const gitDirOf = (folder) => must(folder, ["rev-parse", "--absolute-git-dir"]).pipe(Effect.map((out) => out.trim()));
/** The folder's place from the top of its repository, as git gives it: empty at the top. */
const prefixOf = (folder) => must(folder, ["rev-parse", "--show-prefix"]).pipe(Effect.map((out) => out.trim().replace(/\/$/, "")));
/** Whether the repository whose top folder is `top` ignores the folder at `path`, from that top; a folder not yet there is judged as a folder (D201). */
export const ignores = (top, path) => git(top, ["check-ignore", "-q", "--", `${path}/`]).pipe(Effect.flatMap((o) => o.code === 0 ? Effect.succeed(true) : o.code === 1 ? Effect.succeed(false) : Effect.fail(new LineRefused(top, "check-ignore", o.errors.trim() || o.output.trim()))));
/** Makes the folder a repository whose first line of work is `line`. */
export const makeRepository = (folder, line) => must(folder, ["init", "-q", "-b", line]).pipe(Effect.asVoid);
/** Where git keeps the tips of the lines of work. A line is named to git in full, so a tag of the same name does not stand for it. */
const HEADS = "refs/heads";
const refOf = (line) => `${HEADS}/${line}`;
/** The line a full name of git's names, or none where it names no line. */
const lineNamed = (ref) => (ref !== HEADS && covers(HEADS, ref) ? ref.slice(HEADS.length + 1) : undefined);
/** The line of work the folder has checked out, by its name; none where its HEAD names a commit alone or anything but a line. */
export const currentLine = (folder) => git(folder, ["symbolic-ref", "-q", "HEAD"]).pipe(Effect.map((o) => (o.code === 0 ? lineNamed(o.output.trim()) : undefined)));
/** The commit a line or other name stands for, or undefined. */
export const tipOf = (folder, name) => git(folder, ["rev-parse", "--verify", "--quiet", `${name}^{commit}`]).pipe(Effect.map((o) => (o.code === 0 ? o.output.trim() : undefined)));
/** A line git writes to mark where it could not merge, at the start of a line: `<<<<<<<` or `>>>>>>>`. */
const MARKER = "^(<<<<<<<|>>>>>>>)( |$)";
/**
 * Commits what the folder holds, or what it holds at `paths`, on the line
 * named `line`, with `message`: its parent is that line's tip and that line is
 * moved. The folder must be on that line, or nothing is committed and git's
 * refusal is given (REQ-FLOW-001, "Commit"). Git is started in the folder, so
 * the paths are from it, and what it holds is its files alone, files git
 * ignores left out (REQ-FLOW-001). At the top of a repository, git stages the
 * whole folder in the folder's own index (`add -A -- .`). For `paths`, or
 * below the top, it stages them in an index of the commit's own, at `index`,
 * which the caller names in a place git ignores within the folder, as C1's
 * index of identities is named. It is read from the line's tip with what the
 * folder's own index knows of it (`read-tree -m`), so the commit differs from
 * the tip at the paths or under the folder alone, and holds nothing the user
 * staged outside it; then they are staged in the folder's own index, where
 * git holds them or finds them there. Gives the new commit, or none when
 * nothing changed.
 *
 * A merge git could not make is never committed. Where git left a file of the
 * commit unmerged, or a file the commit changes holds a line marking a
 * conflict, nothing is committed and the files are given, each by its path
 * from the repository's top. A merge in progress whose files are resolved is
 * committed with both its parents, even where they were resolved to what the
 * line already held, from the folder's own index, which holds what the merge
 * took in. That is done where the folder is the top of its repository, and,
 * below the top, only where the merge takes in a commit that the line `taken`
 * holds: git's own merge of main into the ticket's branch, which the user
 * resolved in the folder (D240). That commit takes the whole tree, outside the
 * folder too, so while it is in progress a file git left unmerged, or one the
 * merge changes that holds a line marking a conflict, is looked for in the
 * whole repository. Below the top, any other merge in progress is the user's
 * (D201): it is left in progress, and the commit is of the folder's files
 * alone, with one parent, as where no merge is in progress. The files are
 * then looked for under the folder, or at `paths`.
 */
export const commit = (folder, index, line, message, paths, taken) => Effect.gen(function* () {
    const only = ["--", ...(paths ?? ["."])];
    const on = yield* currentLine(folder);
    if (on !== line)
        return yield* Effect.fail(new LineRefused(folder, "commit", `the folder is ${on === undefined ? "on no branch" : `on ${on}`}, not on ${line}`));
    const head = yield* tipOf(folder, refOf(line));
    const within = (path) => paths === undefined || paths.some((p) => covers(p, path));
    const prefix = yield* prefixOf(folder);
    const inProgress = paths === undefined ? yield* tipOf(folder, "MERGE_HEAD") : undefined;
    // Below the top, the merge in progress is the take-in's only where the line taken in holds what it takes in; any other is the user's, and is left as it is (D201, D240).
    const takenIn = inProgress === undefined || prefix === "" || taken === undefined ? false : (yield* git(folder, ["merge-base", "--is-ancestor", inProgress, refOf(taken)])).code === 0;
    const merging = prefix === "" || takenIn ? inProgress : undefined;
    // While a merge is in progress git is asked from the repository's top, so it names each file from there; otherwise from the folder, and each file is named from the top by the folder's place.
    const seen = merging === undefined ? folder : (yield* must(folder, ["rev-parse", "--show-toplevel"])).trim();
    const fromTop = (path) => (merging !== undefined || prefix === "" ? path : `${prefix}/${path}`);
    // Staging would take a file git left unmerged as resolved, so those are found first.
    const unmerged = parts(yield* must(seen, ["ls-files", "-u", "-z"])).map((e) => e.slice(e.indexOf("\t") + 1)).filter(within);
    if (unmerged.length > 0)
        return { unresolved: byName(new Set(unmerged.map(fromTop))), within: prefix };
    const named = merging !== undefined || (paths === undefined && prefix === "") ? undefined : index;
    const staging = named === undefined ? {} : { GIT_INDEX_FILE: named };
    if (named !== undefined) {
        const fromOwn = head === undefined ? undefined : yield* git(folder, ["read-tree", "-m", head, `--index-output=${named}`]);
        if (fromOwn === undefined || fromOwn.code !== 0)
            yield* must(folder, head === undefined ? ["read-tree", "--empty"] : ["read-tree", head], staging);
    }
    yield* must(folder, ["add", "-A", ...only], staging);
    const tree = (yield* must(folder, ["write-tree"], staging)).trim();
    const changed = parts(yield* must(seen, head === undefined ? ["ls-tree", "-r", "-z", "--name-only", tree] : ["diff-tree", "-r", "-z", "--name-only", "--no-renames", ...(merging === undefined ? ["--relative"] : []), head, tree]));
    const found = yield* Effect.forEach(inGroups(changed), (group) => git(seen, ["grep", "-l", "-z", "-I", "-E", MARKER, tree, "--", ...group]));
    const marked = found.flatMap((o) => parts(o.output)).map((p) => p.slice(tree.length + 1));
    if (marked.length > 0)
        return { unresolved: byName(new Set(marked.map(fromTop))), within: prefix };
    if (changed.length === 0 && merging === undefined)
        return { commit: undefined };
    const parents = [...(head === undefined ? [] : ["-p", head]), ...(merging === undefined ? [] : ["-p", merging])];
    const made = (yield* must(folder, ["commit-tree", tree, ...parents, "-m", message])).trim();
    yield* must(folder, ["update-ref", "-m", `commit: ${message}`, refOf(line), made, head ?? ""]);
    if (merging !== undefined)
        yield* must(folder, ["merge", "--quit"]);
    if (named !== undefined) {
        // A path neither on disk nor in the folder's own index is as the commit has it there already.
        const held = paths === undefined ? ["."] : parts(yield* must(folder, ["ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", ...paths]));
        yield* Effect.forEach(inGroups(held), (group) => must(folder, ["add", "-A", "--", ...group]));
    }
    return { commit: made };
});
/**
 * Commits on `line` the file at `path`, from the folder, as `text` gives it,
 * and nothing else: what the folder holds of that file or of any other is not
 * staged (REQ-FLOW-006 step 3, D227). The commit's own index at `index` is
 * read from the line's tip; the folder's own index then holds the file as the
 * commit does. None where the text is what the tip holds.
 */
export const commitText = (folder, index, line, message, path, text) => Effect.gen(function* () {
    const on = yield* currentLine(folder);
    if (on !== line)
        return yield* Effect.fail(new LineRefused(folder, "commit", `the folder is ${on === undefined ? "on no branch" : `on ${on}`}, not on ${line}`));
    const head = yield* tipOf(folder, refOf(line));
    if (head === undefined)
        return undefined;
    const staging = { GIT_INDEX_FILE: index };
    // The path from the top of the folder's tree, where git reads it whatever folder it is started in.
    const top = (yield* must(folder, ["rev-parse", "--show-toplevel"])).trim();
    const prefix = yield* prefixOf(folder);
    const full = prefix === "" ? path : `${prefix}/${path}`;
    yield* must(top, ["read-tree", head], staging);
    const blob = (yield* must(top, ["hash-object", "-w", "--stdin"], {}, text)).trim();
    yield* must(top, ["update-index", "--add", "--cacheinfo", `100644,${blob},${full}`], staging);
    const tree = (yield* must(top, ["write-tree"], staging)).trim();
    if (tree === (yield* must(top, ["rev-parse", `${head}^{tree}`])).trim())
        return undefined;
    const made = (yield* must(top, ["commit-tree", tree, "-p", head, "-m", message])).trim();
    yield* must(top, ["update-ref", "-m", `commit: ${message}`, refOf(line), made, head]);
    yield* must(top, ["update-index", "--add", "--cacheinfo", `100644,${blob},${full}`]);
    return made;
});
/**
 * The lines of work the repository has as remote branches, by the name each
 * has below its remote (`refs/remotes/<remote>/<name>`), named one of `names`
 * or below one, each with the full name of the first remote that has it: what
 * a clone holds of the lines its origin had (REQ-FLOW-003 step 1).
 */
export const remoteLines = (folder, names) => must(folder, ["for-each-ref", "--format=%(refname)", "refs/remotes"]).pipe(Effect.map((out) => {
    const found = new Map();
    for (const ref of out.split("\n").filter((r) => r !== "")) {
        const name = ref.split("/").slice(3).join("/");
        if (name !== "" && names.some((n) => name === n || covers(n, name)) && !found.has(name))
            found.set(name, ref);
    }
    return found;
}));
/**
 * Of the files asked for, each a name of git's, such as a line, and a path
 * from the folder, the ones git holds there, by their place in the list: one
 * `cat-file --batch-check` for all, which reads no content (D239).
 */
export const presentAt = (folder, asked) => Effect.gen(function* () {
    if (asked.length === 0)
        return new Set();
    const prefix = yield* prefixOf(folder);
    const input = asked.map(([rev, path]) => `${rev}:${prefix === "" ? path : `${prefix}/${path}`}\n`).join("");
    const lines = (yield* must(folder, ["cat-file", "--batch-check=%(objecttype)"], {}, input)).split("\n");
    return new Set(asked.flatMap((_, i) => (lines[i] === "blob" ? [i] : [])));
});
/** The names of the files in the folder at `path`, from the workspace's folder, under the name `rev` of git's; none where there is no such folder there. It reads no content. */
export const namesAt = (folder, rev, path) => git(folder, ["ls-tree", "-z", "--full-tree", "--name-only", `${rev}:./${path}`]).pipe(Effect.map((o) => (o.code === 0 ? parts(o.output) : [])));
/** Makes the line `line` at `commit`, where there is none of that name; git refuses where there is (`update-ref` with no old value). */
export const makeLine = (folder, line, commit) => must(folder, ["update-ref", "-m", `branch: ${line}`, refOf(line), commit, ""]).pipe(Effect.asVoid);
/** Each working tree of the repository, by its folder, with the line it has checked out, where it has one (`worktree list --porcelain`). It writes nothing: it neither makes nor prunes one. */
const workingTrees = (folder) => must(folder, ["worktree", "list", "--porcelain", "-z"]).pipe(Effect.map((out) => {
    const trees = [];
    for (const field of out.split("\0")) {
        if (field.startsWith("worktree "))
            trees.push({ folder: field.slice("worktree ".length) });
        const last = trees[trees.length - 1];
        const named = field.startsWith("branch ") ? lineNamed(field.slice("branch ".length)) : undefined;
        if (last !== undefined && named !== undefined)
            last.line = named;
    }
    return trees;
}));
/** The working tree, other than the one the folder lies in, that has the line `line` checked out; none where no other has it (D239). */
export const heldElsewhere = (folder, line) => Effect.gen(function* () {
    const own = (yield* must(folder, ["rev-parse", "--show-toplevel"])).trim();
    const trees = yield* workingTrees(folder);
    return trees.find((t) => t.line === line && t.folder !== own)?.folder;
});
/**
 * Puts the folder on the line `line` (REQ-FLOW-001, "Open a branch"). Where
 * another working tree has it checked out, git would refuse, and so does
 * this, naming that tree. Where the line is on the commit the folder is on,
 * only HEAD is moved (`symbolic-ref`), so no file is written. Otherwise git
 * puts it there (`switch`), and its refusal is given as git words it.
 */
export const switchTo = (folder, line) => Effect.gen(function* () {
    const elsewhere = yield* heldElsewhere(folder, line);
    if (elsewhere !== undefined)
        return { refused: `'${line}' is already used by worktree at '${elsewhere}'`, elsewhere };
    const tip = yield* tipOf(folder, refOf(line));
    if (tip === undefined)
        return { refused: `there is no branch ${line}` };
    if (tip === (yield* tipOf(folder, "HEAD"))) {
        yield* must(folder, ["symbolic-ref", "-m", `switch: ${line}`, "HEAD", refOf(line)]);
        return { switched: true };
    }
    const o = yield* git(folder, ["switch", "--quiet", line], { LC_ALL: "C" });
    return o.code === 0 ? { switched: true } : { refused: (o.errors || o.output).trim() };
});
/** The files git names where it refuses to write over what the user has not committed or has not added, by path from the repository's top. */
const refusedFiles = (words) => byName(new Set(words.split("\n").flatMap((l) => {
    const m = /(?:Entry|Untracked working tree file) '([^']+)' (?:not uptodate|would be overwritten)/.exec(l);
    return m?.[1] === undefined ? [] : [m[1]];
})));
/**
 * Of the paths the take-in adds, from the commit `from` to the tree or commit
 * `to`, each that is there already in the repository's folder, inside the
 * workspace's folder or outside it, and that git does not hold: the path
 * itself, as a file, or as a folder that holds a file git does not hold; or a
 * folder on the way to it, there as a file. Each by its path from the
 * repository's top, in the order of the names. Git ignores some of them, and
 * its own take-in would write over those with no word (REQ-FLOW-008, D250).
 * Git lists them, with every file it does not hold, ignored or not, and each
 * folder that holds no file it holds as one entry ending in `/`; each path is
 * given to it literally, from the repository's top.
 */
const inTheWay = (folder, from, to) => Effect.gen(function* () {
    const top = yield* topOf(folder);
    if (top === undefined)
        return [];
    const added = parts(yield* must(top, ["diff-tree", "-r", "-z", "--name-only", "--diff-filter=A", from, to]));
    if (added.length === 0)
        return [];
    const ways = [...new Set(added.flatMap((p) => p.split("/").slice(0, -1).map((_, i, all) => all.slice(0, i + 1).join("/"))))];
    const listed = (paths) => Effect.map(Effect.forEach(inGroups(paths), (group) => must(top, ["--literal-pathspecs", "ls-files", "--others", "--directory", "-z", "--", ...group])), (outs) => outs.flatMap(parts));
    const adds = new Set(added);
    const found = new Set();
    // A path the take-in adds is in the way where git lists it, or a file below it.
    for (const entry of yield* listed(added)) {
        const path = entry.replace(/\/$/, "");
        const named = adds.has(path) ? path : added.find((p) => covers(p, path));
        if (named !== undefined)
            found.add(named);
    }
    // A folder on the way is in the way where git lists it as a file, with no `/`.
    const onTheWay = new Set(ways);
    for (const entry of ways.length === 0 ? [] : yield* listed(ways))
        if (onTheWay.has(entry))
            found.add(entry);
    return byName(found);
});
/**
 * Takes the line `from` into the line `line`, which the folder has checked
 * out, in the folder (REQ-FLOW-008 step 1). Where `from` is held already,
 * nothing is done. Git makes the merge apart from the index first
 * (`merge-tree --write-tree`), so a file the user staged anywhere in the
 * repository is no refusal; where `line` holds nothing `from` lacks, the
 * merge is `from` itself. Git puts what it changed in the index and the files
 * (`read-tree -m -u`), which refuses where that would write over what the user
 * has not committed or has not added: the files are then named and nothing is
 * taken in. Only then is the line moved (`update-ref`). Where git cannot merge
 * a file by itself, git's own merge is run in the folder so the user resolves
 * it there, and each file it could not merge is named by its path from the
 * repository's top, as git names it; a merge git left unmerged is that, and no
 * refusal. Where that merge refuses, nothing is taken in. Before any of it,
 * where a path the take-in adds, or a folder on the way to it, is there
 * already and git does not hold it, nothing is taken in and each is named
 * (D250).
 */
export const takeInto = (folder, line, from, message) => Effect.gen(function* () {
    const on = yield* currentLine(folder);
    if (on !== line)
        return { merged: "refused", why: `${folder} is ${on === undefined ? "on no branch" : `on ${on}`}, not on ${line}` };
    const before = yield* tipOf(folder, refOf(line));
    const theirs = yield* tipOf(folder, refOf(from));
    if (before === undefined || theirs === undefined)
        return { merged: "refused", why: `${line} or ${from} has no commit` };
    if ((yield* git(folder, ["merge-base", "--is-ancestor", theirs, before])).code === 0)
        return { merged: "yes", changed: false };
    const forward = (yield* git(folder, ["merge-base", "--is-ancestor", before, theirs])).code === 0;
    const o = forward ? undefined : yield* git(folder, ["merge-tree", "--write-tree", "-z", "--name-only", refOf(line), refOf(from)]);
    if (o !== undefined && o.code !== 0 && o.code !== 1)
        return { merged: "refused", why: (o.errors || o.output).trim() };
    // The tree the take-in gives, whether or not git could merge every file: what it adds is looked at before anything is written (D250).
    const tree = o === undefined ? theirs : (o.output.split("\0")[0] ?? "").trim();
    const way = yield* inTheWay(folder, before, tree);
    if (way.length > 0)
        return { merged: "refused", why: `${from} adds ${way.join(", ")}, where a file or a folder that git does not hold is there already`, inTheWay: way };
    if (o !== undefined && o.code === 1) {
        const m = yield* git(folder, ["merge", "--no-edit", "--no-ff", "-m", message, refOf(from)], { LC_ALL: "C" });
        // Each file git left unmerged, by its path from the repository's top.
        const files = parts(yield* must(folder, ["diff", "--name-only", "--diff-filter=U", "-z"]));
        if (files.length > 0)
            return { merged: "conflict", files };
        const why = (m.errors || m.output).trim();
        return { merged: "refused", why, files: refusedFiles(why) };
    }
    const made = o === undefined ? theirs : (yield* must(folder, ["commit-tree", (o.output.split("\0")[0] ?? "").trim(), "-p", before, "-p", theirs, "-m", message])).trim();
    const put = yield* git(folder, ["read-tree", "-m", "-u", before, made], { LC_ALL: "C" });
    if (put.code !== 0) {
        const why = (put.errors || put.output).trim();
        return { merged: "refused", why, files: refusedFiles(why) };
    }
    yield* must(folder, ["update-ref", "-m", `merge: ${message}`, refOf(line), made, before]);
    return { merged: "yes", changed: true };
});
/**
 * Merges the line `from` into the line `line` (REQ-FLOW-008 step 2): `line`
 * is an ancestor of `from`, so the merge's content is `from`'s own. Git makes
 * the merge commit from `from`'s whole tree with both lines as its parents
 * (`commit-tree`), moves `line` to it (`update-ref`, from the tip it read) and
 * puts the folder on `line` (`symbolic-ref`). No file is written and the index
 * is not touched, so what the user has uncommitted, staged or untracked is as
 * it was. Where another working tree has `line` checked out, or `line` is not
 * an ancestor of `from`, nothing is done. No file is merged, so git meets no
 * conflict here.
 */
export const mergeInto = (folder, line, from, message) => Effect.gen(function* () {
    const elsewhere = yield* heldElsewhere(folder, line);
    if (elsewhere !== undefined)
        return { merged: "refused", why: `${line} is checked out in the working tree at ${elsewhere}`, elsewhere };
    const before = yield* tipOf(folder, refOf(line));
    const theirs = yield* tipOf(folder, refOf(from));
    if (before === undefined || theirs === undefined)
        return { merged: "refused", why: `${line} or ${from} has no commit` };
    if ((yield* git(folder, ["merge-base", "--is-ancestor", before, theirs])).code !== 0)
        return { merged: "refused", why: `${from} does not hold all of ${line}` };
    const tree = (yield* must(folder, ["rev-parse", "--verify", `${theirs}^{tree}`])).trim();
    const made = (yield* must(folder, ["commit-tree", tree, "-p", before, "-p", theirs, "-m", message])).trim();
    yield* must(folder, ["update-ref", "-m", `merge: ${message}`, refOf(line), made, before]);
    yield* must(folder, ["symbolic-ref", "-m", `merge: ${message}`, "HEAD", refOf(line)]);
    return { merged: "yes", changed: true };
});
/** The file at `path` as the line `from` has it, put in the folder and in git's index by git. */
export const takeFrom = (folder, from, path) => must(folder, ["checkout", refOf(from), "--", path]).pipe(Effect.asVoid);
/** The line checked out in `folder` holds all of the line `name`: every commit of it, wherever in the repository it changed a file (REQ-FLOW-008, D240). */
export const holdsAll = (folder, name) => git(folder, ["merge-base", "--is-ancestor", refOf(name), "HEAD"]).pipe(Effect.map((o) => o.code === 0));
/** The files under the folder that differ between two commits, or over a range such as `a...b`, by their paths from the folder, with how many lines of each were added or taken out (D201). */
export const changedLines = (folder, from, to) => must(folder, ["diff", "--numstat", "--no-renames", "--relative", "-z", from, ...(to === undefined ? [] : [to])]).pipe(Effect.map((out) => parts(out).map((entry) => {
    const [added = "0", removed = "0", ...path] = entry.split("\t");
    const count = (n) => (n === "-" ? 0 : Number(n));
    return { path: path.join("\t"), lines: count(added) + count(removed), added: count(added), removed: count(removed) };
})));
/** The commit where `from` and the line `name` last met, git's merge base; none where they share none (REQ-FLOW-006, D211). */
export const mergeBase = (folder, from, name) => git(folder, ["merge-base", from, refOf(name)]).pipe(Effect.map((r) => (r.code === 0 && r.output.trim() !== "" ? r.output.trim() : undefined)));
/**
 * The commits the line `line` holds and `from` does not, merges left out, whose
 * message is `message` and nothing else and which change a file at one of
 * `paths`, from the folder; oldest first (REQ-ALG-007, D244).
 */
export const commitsWith = (folder, from, line, message, paths) => paths.length === 0
    ? Effect.succeed([])
    : must(folder, ["rev-list", "--reverse", "--no-merges", "--fixed-strings", `--grep=${message}`, "--format=%H%x00%B", `${from}..${refOf(line)}`, "--", ...paths]).pipe(Effect.map((out) => 
    // rev-list prints a line `commit <id>` before each format; only a message that is `message` alone counts.
    out.split(/^commit [0-9a-f]+\n/m).filter((e) => e !== "").flatMap((e) => {
        const [id = "", body = ""] = e.split("\0");
        return body.trim() === message ? [id.trim()] : [];
    })));
/** Each branch, tag and the stash, by its full name, with the commit it is on (D228). */
export const refs = (folder) => must(folder, ["for-each-ref", "--format=%(refname) %(objectname)", "refs/heads", "refs/tags", "refs/stash"]).pipe(Effect.map((out) => new Map(out.split("\n").filter((l) => l.includes(" ")).map((l) => [l.slice(0, l.lastIndexOf(" ")), l.slice(l.lastIndexOf(" ") + 1)]))));
/**
 * What git lists as changed, staged or untracked under the repository's top,
 * outside the folder `within`, by path from the top, each with whether git
 * tracks it; it reads no file's content beyond what git's own listing does
 * (D228, D243).
 */
export const outside = (top, within) => Effect.gen(function* () {
    const out = (p) => p !== "" && !p.endsWith("/") && !(within !== "" && covers(within, p));
    const untracked = parts(yield* must(top, ["ls-files", "-z", "--others", "--exclude-standard"])).filter(out);
    const tracked = parts(yield* must(top, ["ls-files", "-z", "--modified", "--deleted"])).filter(out);
    const head = yield* tipOf(top, "HEAD");
    const staged = head === undefined ? [] : parts(yield* must(top, ["diff-index", "--cached", "--name-only", "--no-renames", "-z", head])).filter(out);
    return new Map([...untracked.map((p) => [p, "untracked"]), ...[...tracked, ...staged].map((p) => [p, "tracked"])]);
});
/**
 * Each file outside the folder `within` that differs between the commits
 * `from` and `to`, by path from the repository's top, with what happened to
 * it: one `diff-tree` of the whole tree, which compares the identities git
 * holds and reads no file's content; with no renames found, since finding one
 * reads content (D256).
 */
export const committedOutside = (top, within, from, to) => must(top, ["diff-tree", "-r", "-z", "--no-renames", "--name-status", from, to]).pipe(Effect.map((out) => {
    const fields = parts(out);
    const found = new Map();
    for (let i = 0; i + 1 < fields.length; i += 2) {
        const status = fields[i] ?? "";
        const path = fields[i + 1] ?? "";
        if (within !== "" && covers(within, path))
            continue;
        found.set(path, status.startsWith("A") ? "added" : status.startsWith("D") ? "removed" : "changed");
    }
    return byName(found.keys()).map((p) => [p, found.get(p) ?? "changed"]);
}));
/** The identity git gives a file a commit does not hold. */
const NO_FILE = /^0+$/;
/**
 * Each file that differs between the commits `from` and `to`, anywhere in the
 * repository, by path from its top, with what happened to it and the identity
 * each commit gives it: one `diff-tree` of the whole tree, which compares the
 * identities git holds and reads no file's content; with no renames found,
 * and each identity whole (D257).
 */
export const differsBetween = (top, from, to) => must(top, ["diff-tree", "-r", "-z", "--no-renames", "--no-abbrev", from, to]).pipe(Effect.map((out) => {
    const fields = parts(out);
    const found = new Map();
    for (let i = 0; i + 1 < fields.length; i += 2) {
        // `:<mode> <mode> <identity> <identity> <status>`, then the path.
        const [, , a = "", b = "", status = ""] = (fields[i] ?? "").split(" ");
        const path = fields[i + 1] ?? "";
        found.set(path, { path, how: status.startsWith("A") ? "added" : status.startsWith("D") ? "removed" : "changed", from: NO_FILE.test(a) ? "" : a, to: NO_FILE.test(b) ? "" : b });
    }
    return byName(found.keys()).flatMap((p) => found.get(p) ?? []);
}));
/** Of the paths given, by path from the repository's top, those the commit holds: one `ls-tree` for each group of paths, which reads no file. */
export const heldBy = (top, commit, paths) => Effect.forEach(inGroups(paths), (group) => must(top, ["ls-tree", "-r", "-z", "--full-tree", "--name-only", commit, "--", ...group])).pipe(Effect.map((outs) => new Set(outs.flatMap(parts))));
/** The lines of work named one of `names`, or below one of them as `stdo/x` is below `stdo`, by name. */
export const linesNamed = (folder, names) => must(folder, ["for-each-ref", "--format=%(refname)", ...names.map(refOf)]).pipe(Effect.map((out) => out.split("\n").flatMap((ref) => {
    const line = lineNamed(ref);
    return line === undefined ? [] : [line];
})));
/** The merge commits on `line`, newest first, each with its parents. */
/** The subject of each merge the line holds, newest first. */
export const mergeSubjects = (folder, line) => must(folder, ["log", "--merges", "--format=%s", refOf(line)]).pipe(Effect.map((out) => out.split("\n").filter((l) => l !== "")));
export const mergesOn = (folder, line) => must(folder, ["rev-list", "--merges", "--parents", refOf(line)]).pipe(Effect.map((out) => out.split("\n").filter((l) => l !== "").map((l) => {
    const [commit = "", ...parents] = l.split(" ");
    return { commit, parents };
})));
