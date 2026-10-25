# Install, update and remove the Claude STDO Skills bundle

The install unit is the complete set of five `skills/` directories, including all
resources below them. The entry and delegation flows use sibling skills; an
individual directory is not a supported independent installation. Claude Code
discovers them at `<workspace>/.claude/skills/<name>/SKILL.md`.

The release skill carries its installation helper and maintenance reference. The
package's development `design/`, `tests/`, README and inventory need not be copied
into host discovery directories. The pinned STDO installation, the governed
Product's deciding sources and the a_c public tool are explicit external inputs,
not resources supplied by this skill bundle.

## Verify

Run `python3 -I -B <package>/tests/check_package.py`. It checks the complete roster,
frontmatter, no symbolic links/special files, exact file inventory and hashes. Recognized
local Markdown links in skill resources must resolve to existing regular files
inside the five-directory bundle. Simple inline destinations are supported;
heading fragments, code/prose citations and remote/method availability are not
validated. Required delivered resources use checked Markdown links. A passing
check is bounded integrity evidence, not host qualification.

## Install

Choose an existing disposable workspace and an exact verified source package.
Run:

```
python3 -I -B <package>/skills/stdo-release-install/scripts/manage_install.py install --package <package> --workspace <workspace>
```

Any existing selected skill directory or package ownership receipt causes a
refusal before mutation. Unrelated skill siblings remain unchanged. On success,
retain the returned SHA256 of `.claude/stdo-skills-claude.receipt.json`; that
receipt identifies the source inventory and every installed file/directory.
Confirm real host discovery and an explicit invocation separately.

## Update and remove

Select the exact previously retained receipt SHA256. Do not compute a replacement
hash merely to bypass an unexpected mismatch.

```
python3 -I -B <new-package>/skills/stdo-release-install/scripts/manage_install.py update --package <new-package> --workspace <workspace> --receipt-sha256 <previous-receipt-sha256>
python3 -I -B <installed-release-skill>/scripts/manage_install.py remove --workspace <workspace> --receipt-sha256 <current-receipt-sha256>
```

Both operations require the ownership receipt and an exact match of the current
owned file and directory set and contents. Changed/missing files, local additions
(including hidden files and empty directories), same-name foreign installations
and symlinks are preserved by refusal. An update validates the complete new
five-skill package before touching the existing bundle and returns a new receipt
hash. Removal touches only that selected bundle and its receipt, leaving unrelated
siblings and configuration intact. No force or individual-skill update exists.

Use exclusive workspace access. This local helper is not a concurrent transaction
or an OS confinement boundary. A filesystem failure after mutation reports
`effect_uncertain`: retain the receipt and actual tree, reconcile partial effects
before another attempt, and never replace a mismatched tree by blind deletion.
Actual-host installation and invocation evidence remains distinct from focused
lifecycle fixture proof.
