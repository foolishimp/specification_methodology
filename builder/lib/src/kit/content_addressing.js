/**
 * Content addressing: the identity of a file is a hash of its content, and the
 * identity of a folder a hash of the names and identities in it. Git computes
 * both; this is the one module that asks git for identities. It starts git
 * through the supervised child (C12).
 *
 * Git keeps the identities in an index of their own, which the caller names,
 * apart from the folder's own index. Each time, git is told the files that
 * changed since it last looked (`ls-files --modified --deleted --others`) and
 * records their identities alone (`update-index --info-only`), so the work
 * follows the files that changed and no content is kept. A new index starts
 * from what the folder's own index knows of the last commit (`read-tree -m`),
 * so it too follows what changed. The folders' identities are written as
 * trees, which hold names and identities and no content of a file. Files git
 * ignores are no part of them. A file git holds is read back by its identity.
 *
 * Git is started in the folder, so the files are those under it, by their
 * paths from it. Where the folder lies below the top of its repository, its
 * identity is that of the folder within git's tree of the whole, and the
 * places are read in it, so a file outside the folder is part of no identity
 * (REQ-ALG-001, D201).
 *
 * A release of this product names its manifest by the sha256 of the
 * manifest's bytes, which git does not give: that identity is computed here
 * too, by Effect's digest module on the platform's WebCrypto (D197).
 *
 * @carries C1
 */
import { Digest } from "effect/crypto";
import * as Effect from "effect/Effect";
import { covers } from "./place_containment.js";
import { supervise } from "./supervised_child.js";
/** Git could not give the identities, and why. */
export class IdentityRefused {
    folder;
    why;
    _tag = "IdentityRefused";
    constructor(folder, why) {
        this.folder = folder;
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
const asks = (folder, args, extra) => supervise({
    command: "git",
    args,
    cwd: folder,
    deadline: 10 * MINUTE,
    ...(extra?.input === undefined ? {} : { input: extra.input }),
    env: extra?.index === undefined ? clean : { ...clean, GIT_INDEX_FILE: extra.index }
}).pipe(Effect.flatMap((o) => o.outcome === "returned" && o.code === 0
    ? Effect.succeed(o.output)
    : Effect.fail(new IdentityRefused(folder, o.outcome === "returned" ? o.errors.trim() : o.outcome === "ran over" ? "git ran over" : o.why))));
const parts = (output) => output.split("\0").filter((p) => p !== "");
/**
 * The identities of the folder as it is now: of the whole folder, of each
 * file and folder at `places`, and of the folder beside the places `apart`.
 * `index` is where git keeps them, in a place git ignores; `fresh` says there
 * is none there yet. An index git cannot read is started again.
 */
export const identitiesOf = (folder, index, places, fresh, apart = []) => Effect.gen(function* () {
    // From the folder's own index, where git can read it against the last commit; otherwise empty.
    const start = asks(folder, ["read-tree", "-m", "HEAD", `--index-output=${index}`]).pipe(Effect.catch(() => asks(folder, ["read-tree", "--empty"], { index })));
    const update = Effect.gen(function* () {
        // A path that ends in "/" is a repository of its own inside the folder; it is no file of this one.
        const changed = [...new Set(parts(yield* asks(folder, ["ls-files", "-z", "--modified", "--deleted", "--others", "--exclude-standard"], { index })))].filter((p) => !p.endsWith("/"));
        if (changed.length > 0)
            yield* asks(folder, ["update-index", "-z", "--add", "--remove", "--info-only", "--stdin"], { input: changed.map((p) => `${p}\0`).join(""), index });
        const whole = (yield* asks(folder, ["write-tree", "--missing-ok"], { index })).trim();
        const prefix = (yield* asks(folder, ["rev-parse", "--show-prefix"])).trim().replace(/\/$/, "");
        if (prefix === "")
            return whole;
        // The folder within the whole; a folder that holds no file git keeps is the empty one.
        const found = yield* asks(folder, ["ls-tree", "-z", "--full-tree", whole, "--", prefix]).pipe(Effect.map(parts));
        const entry = found.find((line) => line.slice(line.indexOf("\t") + 1) === prefix);
        return entry === undefined ? (yield* asks(folder, ["hash-object", "-t", "tree", "--stdin"], { input: "" })).trim() : (entry.split(" ")[2]?.split("\t")[0] ?? "");
    });
    if (fresh)
        yield* start;
    const root = yield* update.pipe(Effect.catch(() => start.pipe(Effect.andThen(update))));
    const identities = new Map();
    const files = [];
    const listed = places.length === 0 ? [] : parts(yield* asks(folder, ["ls-tree", "-r", "-t", "-z", "--full-tree", root, "--", ...places]));
    for (const line of listed) {
        const tab = line.indexOf("\t");
        const [, type, identity] = line.slice(0, tab).split(" ");
        const path = line.slice(tab + 1);
        if (identity === undefined)
            continue;
        identities.set(path, identity);
        if (type === "blob")
            files.push(path);
    }
    if (apart.length === 0)
        return { root, identities, files };
    // Git lists the entries at the top and in each folder that holds a place apart, and not the folders it passes through on the way.
    const holding = [...new Set(apart.flatMap((p) => (p.includes("/") ? [`${p.slice(0, p.lastIndexOf("/"))}/`] : [])))];
    const beside = parts(yield* asks(folder, ["ls-tree", "-z", "--full-tree", root, "--", ".", ...holding])).filter((line) => !apart.some((p) => covers(p, line.slice(line.indexOf("\t") + 1))));
    return { root, identities, files, beside: beside.join("\n") };
});
/** The files git holds in the folder or does not ignore there, by path relative to it. */
export const filesOf = (folder) => asks(folder, ["ls-files", "-z", "--cached", "--others", "--exclude-standard"]).pipe(Effect.map((out) => parts(out).filter((p) => !p.endsWith("/"))));
/** The text of the file git holds under an identity, in the repository the folder lies in. */
export const textOf = (folder, identity) => asks(folder, ["cat-file", "blob", identity]);
/**
 * The identity of each of `places` that is there under `commit`, from the
 * folder, as git holds it in that commit's tree: the same identity the index of
 * identities gives the same content. None where git does not hold the commit
 * (REQ-ALG-004). It reads no index.
 */
export const underCommit = (folder, commit, places) => asks(folder, ["cat-file", "-e", `${commit}^{commit}`]).pipe(Effect.matchEffect({
    onFailure: () => Effect.succeed(undefined),
    onSuccess: () => places.length === 0
        ? Effect.succeed(new Map())
        : asks(folder, ["ls-tree", "-z", commit, "--", ...places]).pipe(Effect.map((out) => new Map(out.split("\0").filter((l) => l !== "").flatMap((l) => {
            const [meta = "", path = ""] = l.split("\t");
            const id = meta.split(" ")[2];
            return id === undefined ? [] : [[path, id]];
        }))))
}));
/** The text of the file at `path`, from the folder, under `commit`; none where git holds no such file there. */
export const textAt = (folder, commit, path) => asks(folder, ["cat-file", "blob", `${commit}:./${path}`]).pipe(Effect.orElseSucceed(() => undefined));
/** The identity git gives to a text, as it would to a file holding it. Nothing is stored. */
export const identityOfText = (folder, text) => asks(folder, ["hash-object", "--stdin"], { input: text }).pipe(Effect.map((out) => out.trim()));
/** The sha256 of a file's bytes, in lowercase hex, as a release's manifest is named by it (D197). */
export const sha256Of = (bytes) => Effect.gen(function* () {
    const digest = yield* Digest.Digest;
    return yield* digest.digestHex(Digest.sha256, bytes);
}).pipe(Effect.provide(Digest.layerWebCrypto));
