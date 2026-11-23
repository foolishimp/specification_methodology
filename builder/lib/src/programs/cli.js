#!/usr/bin/env node
/**
 * The command-line program (REQ-INTERFACE-001): it reads a command and its
 * inputs, passes them to the library, prints the words the library gives back
 * and exits with its exit code. It holds no check, no decision and no step of
 * a run. Its commands: set up, write a ticket, run, answer, show, list the
 * registry, and record the release that builds the product (REQ-FLOW-010).
 *
 * @uses C14
 * @is REQ-INTERFACE-001 REQ-FLOW-010
 */
import * as NodeRuntime from "@effect/platform-node/NodeRuntime";
import * as NodeServices from "@effect/platform-node/NodeServices";
import * as Effect from "effect/Effect";
import { Argument, Command, Flag } from "effect/cli";
import * as Library from "../library/library.js";
const workspace = Argument.String("workspace").pipe(Argument.withDescription("The workspace, by its path or file: URI"), Argument.withDefault("."));
const given = (value) => (value === "" ? undefined : value);
const say = (said) => Effect.promise(said).pipe(Effect.flatMap((s) => Effect.sync(() => {
    console.log(s.words);
    process.exitCode = s.exitCode;
})));
const setup = Command.make("setup", {
    workspace,
    name: Flag.String("name").pipe(Flag.withDescription("A name for the product")),
    release: Flag.String("release").pipe(Flag.withDescription("The method release, by its URI"), Flag.withDefault(Library.RELEASE.uri)),
    manifest: Flag.String("manifest").pipe(Flag.withDescription("The sha256 of the release's manifest"), Flag.withDefault(Library.RELEASE.manifest))
}, (c) => say(() => Library.setup(c.workspace, { name: c.name, release: { uri: c.release, manifest: c.manifest } })));
const ticket = Command.make("ticket", {
    workspace,
    words: Argument.String("words").pipe(Argument.withDescription("What you want, in your words"))
}, (c) => say(() => Library.ticket(c.workspace, c.words)));
const run = Command.make("run", {
    workspace,
    ticket: Flag.String("ticket").pipe(Flag.withDescription("The ticket to work on"), Flag.withDefault("")),
    standIn: Flag.String("stand-in").pipe(Flag.withDescription("A folder of the stand-in agent's fixtures"), Flag.withDefault(""))
}, (c) => {
    const ticket = given(c.ticket);
    const standIn = given(c.standIn);
    return say(() => Library.run(c.workspace, { ...(ticket === undefined ? {} : { ticket }), ...(standIn === undefined ? {} : { standIn }) }));
});
const answer = Command.make("answer", {
    workspace,
    says: Argument.Literals("answer", ["yes", "no"]),
    reason: Flag.String("reason").pipe(Flag.withDescription("Why, for an answer of no"), Flag.withDefault("")),
    ticket: Flag.String("ticket").pipe(Flag.withDescription("The ticket the answer is for"), Flag.withDefault("")),
    ruling: Flag.String("ruling").pipe(Flag.withDescription("A ruling that binds every later session of the ticket"), Flag.withDefault(""))
}, (c) => {
    const reason = given(c.reason);
    const ticket = given(c.ticket);
    const ruling = given(c.ruling);
    return say(() => Library.answer(c.workspace, c.says, { ...(reason === undefined ? {} : { reason }), ...(ticket === undefined ? {} : { ticket }), ...(ruling === undefined ? {} : { ruling }) }));
});
const show = Command.make("show", { workspace }, (c) => say(() => Library.show(c.workspace)));
const registry = Command.make("registry", { workspace }, (c) => say(() => Library.registry(c.workspace)));
const recordRelease = Command.make("record-release", { workspace }, (c) => say(() => Library.recordRelease(c.workspace)));
const program = Command.make("stdo-builder").pipe(Command.withSubcommands([setup, ticket, run, answer, show, registry, recordRelease]));
Command.run(program, { version: "3.2.0" }).pipe(Effect.provide(NodeServices.layer), NodeRuntime.runMain);
