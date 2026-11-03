# S2 — Adjacent empty ATX closing delimiter becomes a false named selector

Exact subject: successor `SOURCE_DELTA.json` SHA256 `6cd82322ac23d4dfe8ce7d8bf0df73fd2d3ffcbe06f3f70be8925d27e22dc523`; reader `4c180df846327bf6a1eac337d5bc584f067f55bc044848d5f332e0f52bcd8ac5`. Source locator: `specification_methodology/v3/build_tenants/common/plugins/spec/scripts/read_basis.py:159–163`.

The original Unicode repair passes the independently frozen 42 cases /126 actual CLI calls. A separate concrete ATX selector discriminator remains: `## ###` is an empty heading under CommonMark0.31.2 §4.2, Example79. The column-zero form is admitted by the helper's supported ATX subset; no refusal or narrower exclusion applies. The nonempty title match treats its optional closing hashes as the heading name `###`.

The actual helper CLI with exact fixture member/manifest checks returns exit0/status checked for both the catalog and `--heading '###'`. It catalogs that invented name at line3 and projects `## ###\nselected\n` (lines3–4, digest `f530dab8d88aa060d14b1fb6cf44a71427ba6389d50c7c5553ad10b575e2e7e3`). Requesting the actual empty name is refused. The tab variant `## \t### \t` has the same failure. Adjacent NBSP-before/after-hashes cases correctly keep those characters as title content and refuse `###`; those controls prevent a Unicode-whitespace normalization fix from becoming the next mistake.

This violates CS-09 and frozen U-01/U-05: a verified exact source member cannot justify a false named section or catalog selector. Severity S2 reflects the positive source-projection claim and wrong selector, not merely a rejected optional syntax. The defect is pre-existing, not introduced by the Unicode fix. It is inside the already selected ATX boundary question; no general Markdown parser qualification is requested.

Required outcome: treat the delimiter-only form as an empty heading consistently in catalog and selection, or explicitly refuse the unsupported form without a positive catalog/section. Preserve the NBSP discriminators and exact source bytes/line coordinates. Writer owns any implementation/test repair and Executive owns disposition.

Evidence: ADJACENT_ATX.json pins all12 actual helper CLI calls, inputs, complete responses and exact reader. A controlled mock manager supplied exact control responses; this does not claim real-install or native-actor coverage. CommonMark source: https://spec.commonmark.org/0.31.2/#atx-headings. All116 composite source pins still match after inspection in SOURCE_CHECK_AFTER_001.json. Earlier native qualification limits remain unchanged.
