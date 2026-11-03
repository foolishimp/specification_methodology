"""Observable projection/refusal tests for the packaged source-reader CLI.

The manager fixture supplies its public JSON interface. Native manager use is
qualified separately; these cases exercise the helper's real subprocess path.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest


READER = Path(__file__).resolve().parent.parent / "common/plugins/spec/scripts/read_basis.py"
GATE = READER.with_name("claude_tool_gate.py")


class ClaudeToolGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="stdo-tool-gate-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.control = self.root / "control.json"
        self.control.write_text('{"role":"issuer"}\n')
        self.policy = self.root / "policy.json"
        self.audit = self.root / "audit.jsonl"
        self.policy.write_text(json.dumps({"kind": "stdo.claude-tool-policy", "schema_version": 1,
            "policy_id": "urn:fixture:issuer-policy", "authority_ref": "urn:fixture:admitted-grant",
            "cwd": str(self.root), "read_paths": [str(self.control)],
            "bash_commands": ["python3 /approved/admission.py issuer"], "skills": ["spec:stdo-work"]}))
        self.pin = hashlib.sha256(self.policy.read_bytes()).hexdigest()

    def event(self, tool="Read", value=None):
        return {"hook_event_name": "PreToolUse", "cwd": str(self.root),
                "tool_name": tool, "tool_input": value or {"file_path": str(self.control)},
                "tool_use_id": "test-tool-1"}

    def invoke(self, event=None, *, cwd=None, audit=True):
        args = [sys.executable, "-B", str(GATE), "--policy", str(self.policy), "--policy-sha256", self.pin]
        if audit:
            args += ["--audit", str(self.audit)]
        p = subprocess.run(args, input=json.dumps(event or self.event()), capture_output=True,
                           text=True, cwd=cwd or self.root)
        self.assertEqual((p.returncode, p.stderr), (0, ""))
        return json.loads(p.stdout)["hookSpecificOutput"]

    def test_exact_supported_calls_allow_and_audit(self):
        for event in [self.event(), self.event("Skill", {"skill": "spec:stdo-work"}),
                      self.event("Bash", {"command": "python3 /approved/admission.py issuer"})]:
            self.assertEqual(self.invoke(event)["permissionDecision"], "allow")
        records = [json.loads(line) for line in self.audit.read_text().splitlines()]
        self.assertEqual(len(records), 3)
        self.assertEqual({r["policy_sha256"] for r in records}, {self.pin})
        self.assertNotIn("tool_input", records[0])

    def test_extra_shell_text_and_unlisted_command_deny(self):
        for command in ["ls ..", "python3 /approved/admission.py issuer; cat private.txt",
                        "python3 /approved/admission.py issuer\nls"]:
            with self.subTest(command=command):
                result = self.invoke(self.event("Bash", {"command": command}))
                self.assertEqual(result["permissionDecision"], "deny")
                self.assertEqual(result["permissionDecisionReason"], "command_not_listed")

    def test_changed_event_or_process_cwd_deny(self):
        event = self.event()
        event["cwd"] = str(self.root.parent)
        self.assertEqual(self.invoke(event)["permissionDecisionReason"], "cwd_mismatch")
        self.assertEqual(self.invoke(cwd=self.root.parent)["permissionDecisionReason"], "hook_cwd_mismatch")

    def test_unlisted_escape_and_redirected_read_deny(self):
        for name in [str(self.root / "other.txt"), str(self.root / ".." / self.root.name / "control.json")]:
            self.assertEqual(self.invoke(self.event(value={"file_path": name}))["permissionDecision"], "deny")
        target = self.root / "target.txt"
        target.write_text("other content")
        self.control.unlink()
        self.control.symlink_to(target)
        self.assertEqual(self.invoke()["permissionDecisionReason"], "noncanonical_path")

    def test_unknown_event_tool_and_skill_arguments_deny(self):
        event = self.event()
        event["hook_event_name"] = "PostToolUse"
        self.assertEqual(self.invoke(event)["permissionDecisionReason"], "wrong_hook_event")
        self.assertEqual(self.invoke(self.event("Glob", {"pattern": "**/*"}))["permissionDecisionReason"], "tool_not_supported")
        self.assertEqual(self.invoke(self.event("Skill", {"skill": "spec:stdo-work", "args": "new grant"}))["permissionDecisionReason"], "skill_not_listed")

    def test_policy_tamper_and_unsupported_parameters_deny(self):
        result = self.invoke(self.event("Bash", {"command": "python3 /approved/admission.py issuer", "dangerouslyDisableSandbox": True}))
        self.assertEqual(result["permissionDecisionReason"], "unsupported_bash_input")
        result = self.invoke(self.event("Bash", {"command": "python3 /approved/admission.py issuer", "run_in_background": True}))
        self.assertEqual(result["permissionDecisionReason"], "background_not_supported")
        self.policy.write_text(self.policy.read_text() + " ")
        self.assertEqual(self.invoke()["permissionDecisionReason"], "policy_digest_mismatch")

    def test_selected_unavailable_audit_denies(self):
        self.audit.mkdir()
        self.assertEqual(self.invoke()["permissionDecisionReason"], "audit_unavailable")

    def test_host_without_no_bytecode_flag_keeps_plugin_pristine(self):
        plugin = self.root / "plugin"
        plugin.mkdir()
        for source in (GATE, READER):
            (plugin / source.name).write_bytes(source.read_bytes())
        p = subprocess.run([sys.executable, str(plugin / GATE.name), "--policy", str(self.policy),
                            "--policy-sha256", self.pin], input=json.dumps(self.event()),
                           capture_output=True, text=True, cwd=self.root)
        self.assertEqual(p.returncode, 0)
        self.assertEqual(json.loads(p.stdout)["hookSpecificOutput"]["permissionDecision"], "allow")
        self.assertEqual({p.name for p in plugin.iterdir()}, {GATE.name, READER.name})


class SourceReaderTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="stdo-source-reader-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.release = self.root / "release"
        self.member = self.release / "standards/OWNER.md"
        self.member.parent.mkdir(parents=True)
        self.definition = self.root / "stdo_fixture.json"
        self.state_path = self.root / "state.json"
        self.manager = self.root / "manager"
        self.manager.write_text("#!" + sys.executable + "\n" + '''import json,sys,time
from pathlib import Path
state=json.loads((Path(__file__).parent/'state.json').read_text())
args=sys.argv[1:]
if args[:1]==['--store']:
    if args[1]!=state['store']:sys.exit(9)
    args=args[2:]
if state.get('fail')==args[0]:sys.exit(7)
if state.get('timeout'):time.sleep(1)
if args[0]=='status':print(json.dumps(state['status']))
elif args[0]=='resolve':
    print(json.dumps({'uri':state.get('uri_override',args[1]),'path':state['routes'][args[1]]}))
else:sys.exit(8)
''')
        self.manager.chmod(0o755)
        self.subject("# Owner\n\n## One\nkeep me\n\n### Nested\nkeep this too\n\n## Two\nexclude this\n")

    def subject(self, text):
        self.member.write_bytes(text.encode("utf-8"))
        manifest = {"standards": {"installed_root": "standards", "members": [
            {"path": "OWNER.md", "sha256": hashlib.sha256(self.member.read_bytes()).hexdigest()}]}}
        raw = (json.dumps(manifest) + "\n").encode()
        (self.release / "manifest.json").write_bytes(raw)
        basis = {"uri": "stdo://releases/v3.0.3/", "manifest_sha256": hashlib.sha256(raw).hexdigest()}
        self.definition.write_text(json.dumps({"product": {"definition_id": "urn:fixture"},
            "constitution": {"stdo": {"basis": basis}}}))
        self.state = {"store": str(self.root / "store"), "status": {
            "definition": str(self.definition), "definition_id": "urn:fixture", "basis": basis["uri"],
            "manifest_sha256": basis["manifest_sha256"], "path": str(self.release),
            "installed": True, "valid": True, "failures": []}, "routes": {
            basis["uri"] + "manifest.json": str(self.release / "manifest.json"),
            basis["uri"] + "standards/OWNER.md": str(self.member)}}
        self.save()

    def save(self):
        self.state_path.write_text(json.dumps(self.state))

    def invoke(self, command="read", *extra, catalog=False, heading="One"):
        args = [sys.executable, "-B", str(READER), command, "--stdo", str(self.manager),
                "--store", self.state["store"], "--definition", str(self.definition)]
        if command == "read":
            args += ["--member", "standards/OWNER.md"]
            args += ["--list-headings"] if catalog else ["--heading", heading]
        p = subprocess.run(args + list(extra), capture_output=True, text=True)
        self.assertEqual(p.stderr, "")
        return p.returncode, json.loads(p.stdout)

    def test_check_returns_compact_verified_identity(self):
        code, result = self.invoke("check")
        self.assertEqual((code, result["status"]), (0, "checked"))
        self.assertEqual(result["definition_id"], "urn:fixture")
        self.assertEqual(result["manifest_sha256"], self.state["status"]["manifest_sha256"])
        self.assertNotIn("members", result)
        self.assertNotIn("sections", result)

    def test_projection_preserves_nested_text_and_excludes_next_section(self):
        code, result = self.invoke()
        self.assertEqual(code, 0)
        section = result["sections"][0]
        self.assertEqual(section["text"], "## One\nkeep me\n\n### Nested\nkeep this too\n\n")
        self.assertEqual((section["first_line"], section["last_line"]), (3, 8))
        self.assertEqual(section["sha256"], hashlib.sha256(section["text"].encode()).hexdigest())

    def test_catalog_returns_verified_selectors_without_source_bodies(self):
        code, result = self.invoke(catalog=True)
        self.assertEqual(code, 0)
        self.assertEqual([h["heading"] for h in result["headings"]], ["Owner", "One", "Nested", "Two"])
        self.assertEqual(result["headings"][1], {"heading": "One", "level": 2, "first_line": 3, "unique": True})
        self.assertNotIn("sections", result)
        self.assertNotIn("exclude this", json.dumps(result))
        self.subject("## One\na\n## One\nb\n")
        self.assertEqual([h["unique"] for h in self.invoke(catalog=True)[1]["headings"]], [False, False])

    def test_digest_mismatch_refuses_without_returning_source(self):
        self.member.write_text("# changed\n## One\nnot admitted\n")
        code, result = self.invoke()
        self.assertEqual((code, result["reason"]), (1, "member_digest_mismatch"))
        self.assertNotIn("sections", result)

    def test_manifest_digest_mismatch(self):
        (self.release / "manifest.json").write_text("{}")
        self.assertEqual(self.invoke()[1]["reason"], "manifest_digest_mismatch")

    def test_exact_definition_and_basis_must_match(self):
        for key, value in [("definition_id", "urn:other"), ("basis", "stdo://releases/v3.0.2/"),
                           ("definition", str(self.root / "other.json")), ("valid", False)]:
            with self.subTest(key=key):
                original = self.state["status"][key]
                self.state["status"][key] = value
                self.save()
                self.assertEqual(self.invoke()[1]["reason"], "basis_verification_mismatch")
                self.state["status"][key] = original
        self.save()

    def test_manager_failure_and_timeout_keep_distinct_results(self):
        self.state["fail"] = "status"
        self.save()
        self.assertEqual(self.invoke()[1]["reason"], "manager_failed:status:exit=7")
        del self.state["fail"]
        self.state["timeout"] = True
        self.save()
        code, result = self.invoke("check", "--timeout", "0.05")
        self.assertEqual((code, result["status"], result["reason"]), (2, "incomplete", "manager_timeout"))

    def test_resolver_uri_and_path_must_match(self):
        self.state["uri_override"] = "stdo://releases/v3.0.2/manifest.json"
        self.save()
        self.assertEqual(self.invoke()[1]["reason"], "manifest_route_mismatch")
        del self.state["uri_override"]
        other = self.root / "other.md"
        other.write_bytes(self.member.read_bytes())
        self.state["routes"]["stdo://releases/v3.0.3/standards/OWNER.md"] = str(other)
        self.save()
        self.assertEqual(self.invoke()[1]["reason"], "member_route_mismatch")

    def test_missing_and_duplicate_real_headings_refuse(self):
        for text in ["# Owner\n## Elsewhere\n", "## One\na\n## One\nb\n"]:
            with self.subTest(text=text):
                self.subject(text)
                self.assertEqual(self.invoke()[1]["reason"], "section_missing_or_ambiguous:One")

    def test_examples_and_comments_do_not_invent_or_end_sections(self):
        self.subject("## One\n```md\n## Two\n```\n<!--\n## Two\n-->\nkept\n## Two\nnot kept\n")
        code, result = self.invoke()
        self.assertEqual(code, 0)
        self.assertIn("kept\n", result["sections"][0]["text"])
        self.assertNotIn("not kept", result["sections"][0]["text"])
        self.subject("# Owner\n```md\n## One\n```\n<!--\n## One\n-->\n")
        self.assertEqual(self.invoke()[1]["reason"], "section_missing_or_ambiguous:One")

    def test_op02_container_end_cannot_expose_unselected_section(self):
        # Exact independent-review specimen, formerly checked with lines 1–7.
        self.subject("## One\n> ```\n> quoted example\n## Two\nUNSELECTED TWO\n> ```\n> another quote\n## Three\nUNSELECTED THREE\n")
        for catalog in (False, True):
            code, result = self.invoke(catalog=catalog)
            self.assertEqual((code, result["status"], result["reason"]),
                             (1, "refused", "unsupported_container_fence"))
            self.assertNotIn("sections", result)
            self.assertNotIn("headings", result)

    def test_op02_comment_container_end_cannot_expose_unselected_section(self):
        # Exact residual review specimen through the real CLI, not parser-only.
        self.subject("## One\n> <!--\n> quoted comment\n## Two\nUNSELECTED TWO\n> -->\n## Three\nUNSELECTED THREE\n")
        for catalog in (False, True):
            code, result = self.invoke(catalog=catalog)
            self.assertEqual((code, result["status"], result["reason"]),
                             (1, "refused", "unsupported_comment_placement"))
            self.assertNotIn("sections", result)
            self.assertNotIn("headings", result)

    def test_adjacent_comment_placements_refuse_before_projection(self):
        for opener in ["  <!--", "\t<!--", "- <!--", "1. <!--", "> > <!--",
                       "> - <!--", "- > <!--", "paragraph <!--",
                       "<!-- closed --> <!--", "<!--\n--> <!--"]:
            with self.subTest(opener=opener):
                self.subject("## One\n" + opener + "\n## Two\nUNSELECTED TWO\n-->\n## Three\n")
                for catalog in (False, True):
                    code, result = self.invoke(catalog=catalog)
                    self.assertEqual((code, result["reason"]), (1, "unsupported_comment_placement"))
                    self.assertNotIn("sections", result)
                    self.assertNotIn("headings", result)

    def test_unsupported_html_states_and_comment_exposed_fences_refuse(self):
        for opener in ["<![CDATA[", "<!FOO", "<?instruction", "> <div>", "- <div>"]:
            with self.subTest(opener=opener):
                self.subject("## One\n" + opener + "\n## Two\nUNSELECTED TWO\n>\n## Three\n")
                for catalog in (False, True):
                    code, result = self.invoke(catalog=catalog)
                    self.assertEqual((code, result["reason"]), (1, "unsupported_markdown_html_block"))
                    self.assertNotIn("sections", result)
                    self.assertNotIn("headings", result)
        for prefix in ["<!-- closed -->", "<!--\n-->"]:
            with self.subTest(prefix=prefix):
                self.subject("## One\n" + prefix + "```\n## Two\nUNSELECTED TWO\n```\n## Three\n")
                self.assertEqual(self.invoke()[1]["reason"], "unsupported_fence_comment")

    def test_op02_self_closing_html_cannot_invent_named_section(self):
        # Exact review specimen: Two is raw HTML content, not an ATX section.
        self.subject("## One\n<div/>\n## Two\nNOT AN ATX SECTION\n\n## Three\nend\n")
        for catalog in (False, True):
            code, result = self.invoke(catalog=catalog, heading="Two")
            self.assertEqual((code, result["status"], result["reason"]),
                             (1, "refused", "unsupported_markdown_html_block"))
            self.assertNotIn("sections", result)
            self.assertNotIn("headings", result)

    def test_leading_angle_domain_refuses_without_html_tag_recognition(self):
        openers = ["<", "<div", "<script", "</div", "<x-custom/>", "<!", "<?",
                   "<https://example.invalid>", "<reader@example.invalid>"]
        openers += [prefix + "<div/>" for prefix in
                    [" ", "   ", "\t", "> ", ">>", "- ", "1. ", "- > ", "> - > 2. "]]
        for opener in openers:
            with self.subTest(opener=opener):
                self.subject("## One\n" + opener + "\n## Two\nRAW OR AMBIGUOUS\n\n## Three\nend\n")
                code, result = self.invoke(heading="Two")
                self.assertEqual((code, result["reason"]), (1, "unsupported_markdown_html_block"))
                self.assertNotIn("sections", result)
                self.assertNotIn("headings", result)

    def test_literal_and_fenced_angle_forms_preserve_real_sections(self):
        self.subject("## One\nA < B; inline <span/> remains inline.\n\\<div/>\n```html\n<div/>\n## Two\n```\n## Two\nreal section\n")
        code, result = self.invoke(heading="Two")
        self.assertEqual(code, 0)
        self.assertEqual(result["sections"][0]["text"], "## Two\nreal section\n")

    def test_unicode_separators_cannot_invent_lines_or_sections(self):
        for separator in ["\v", "\f", "\x1c", "\x1d", "\x1e", "\x85", "\u2028", "\u2029"]:
            with self.subTest(codepoint=f"U+{ord(separator):04X}"):
                self.subject("## One\nordinary" + separator + "## False\n## Two\nreal section\n")
                code, result = self.invoke(heading="False")
                self.assertEqual((code, result["status"], result["reason"]),
                                 (1, "refused", "section_missing_or_ambiguous:False"))
                self.assertNotIn("sections", result)
                code, catalog = self.invoke(catalog=True)
                self.assertEqual(code, 0)
                self.assertEqual([(h["heading"], h["first_line"]) for h in catalog["headings"]],
                                 [("One", 1), ("Two", 3)])
                code, result = self.invoke(heading="One")
                self.assertEqual(code, 0)
                expected = "## One\nordinary" + separator + "## False\n"
                self.assertEqual(result["sections"][0]["text"], expected)
                self.assertEqual(result["sections"][0]["sha256"], hashlib.sha256(expected.encode()).hexdigest())

    def test_non_ascii_whitespace_cannot_close_fences(self):
        for fence in ["```", "~~~"]:
            for whitespace in ["\u00a0", "\u1680", "\u2000", "\u2028", "\u2029", "\v", "\f", "\x85"]:
                with self.subTest(fence=fence, codepoint=f"U+{ord(whitespace):04X}"):
                    self.subject("## One\n" + fence + "text\ncode\n" + fence + whitespace + "\n## False\nstill code\n")
                    code, result = self.invoke(heading="False")
                    self.assertEqual((code, result["status"], result["reason"]),
                                     (1, "refused", "unterminated_markdown_structure"))
                    self.assertNotIn("sections", result)

    def test_physical_endings_preserve_section_bytes_and_coordinates(self):
        bodies = ["# Owner", "", "## One", "body\u2028continuation", "### Nested", "caf\u00e9\u00a0", "## Two", "end"]
        for endings in [["\n"] * 8, ["\r\n"] * 8, ["\r"] * 8,
                        ["\r\n", "\r", "\n", "\r\n", "\n", "\r", "\r\n", "\n"]]:
            for final_ending in (True, False):
                with self.subTest(endings=repr(endings), final_ending=final_ending):
                    lines = [body + ending for body, ending in zip(bodies, endings)]
                    if not final_ending:
                        lines[-1] = bodies[-1]
                    self.subject("".join(lines))
                    code, result = self.invoke()
                    self.assertEqual(code, 0)
                    section = result["sections"][0]
                    expected = "".join(lines[2:6]).encode("utf-8")
                    self.assertEqual(section["text"].encode("utf-8"), expected)
                    self.assertEqual(section["sha256"], hashlib.sha256(expected).hexdigest())
                    self.assertEqual((section["first_line"], section["last_line"]), (3, 6))
                    code, catalog = self.invoke(catalog=True)
                    self.assertEqual(code, 0)
                    self.assertEqual([(h["heading"], h["first_line"]) for h in catalog["headings"]],
                                     [("Owner", 1), ("One", 3), ("Nested", 5), ("Two", 7)])

    def test_spaces_and_tabs_close_fences_after_literal_unicode(self):
        for fence in ["```", "~~~"]:
            for ending in ["\n", "\r\n", "\r"]:
                with self.subTest(fence=fence, ending=repr(ending)):
                    self.subject(ending.join(["## One", fence, fence + "\u00a0", "## False",
                                              "   " + fence + " \t", "## Two", "body", ""]))
                    code, result = self.invoke(heading="Two")
                    self.assertEqual(code, 0)
                    self.assertEqual(result["sections"][0]["text"], "## Two" + ending + "body" + ending)
                    self.assertEqual((result["sections"][0]["first_line"], result["sections"][0]["last_line"]), (6, 7))

    def test_atx_and_blank_line_whitespace_is_space_or_tab(self):
        self.subject("## One\n##\u00a0\n##\u2028\n## \u00a0\nkept\n## \t\n## Two\nend\n")
        code, result = self.invoke(catalog=True)
        self.assertEqual(code, 0)
        self.assertEqual([(h["heading"], h["first_line"]) for h in result["headings"]],
                         [("One", 1), ("\u00a0", 4), ("", 6), ("Two", 7)])
        self.subject("## One\n\u00a0\n---\n## Two\nend\n")
        self.assertEqual(self.invoke()[1]["reason"], "unsupported_setext_heading")
        for middle in [" \t\n---", "paragraph\n---\u00a0"]:
            self.subject("## One\n" + middle + "\n## Two\nend\n")
            code, result = self.invoke(catalog=True)
            self.assertEqual(code, 0)
            self.assertEqual([h["heading"] for h in result["headings"]], ["One", "Two"])

    def test_adjacent_nested_fence_and_heading_containers_refuse(self):
        for opener in ["  ```", "- ```", "1. ```", "> > ```"]:
            with self.subTest(opener=opener):
                self.subject("## One\n" + opener + "\nexample\n## Two\nother\n```\n")
                self.assertEqual(self.invoke()[1]["reason"], "unsupported_container_fence")
        for heading in ["  ## Two", "- ## Two", "> ## Two"]:
            with self.subTest(heading=heading):
                self.subject("## One\n" + heading + "\nother\n")
                self.assertEqual(self.invoke()[1]["reason"], "unsupported_container_heading")

    def test_unterminated_or_unsupported_blocks_refuse(self):
        for text, reason in [
            ("## One\na\n<!--\n## Fake\n", "unterminated_markdown_structure"),
            ("## One\na\n```\n## Fake\n", "unterminated_markdown_structure"),
            ("## One\na\n<div>\n## Fake\n</div>\n", "unsupported_markdown_html_block"),
            ("## One\na\n\nHeading\n===\n", "unsupported_setext_heading"),
            ("## One\na\n<!-- x -->## Two\n", "unsupported_heading_comment")]:
            with self.subTest(reason=reason):
                self.subject(text)
                self.assertEqual(self.invoke()[1]["reason"], reason)

    def test_invalid_routes_and_missing_member_do_not_fallback(self):
        for route in ["standards/../outside.md", "standards/OWNER.md?x=1", "standards/OWNER.md#one"]:
            with self.subTest(route=route):
                self.assertEqual(self.invoke("read", "--member", route)[1]["reason"], "invalid_member_route")
        self.assertEqual(self.invoke("read", "--member", "standards/ABSENT.md")[1]["reason"], "member_missing_or_ambiguous")


if __name__ == "__main__":
    unittest.main()
