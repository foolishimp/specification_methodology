# OP-02 remains open on revision 3: HTML comment container

Exact freeze `66a099d5550b3ae25d84d62fb77e296c80269fed9b30826fb876d023337c4522`; exact reader SHA256 `2cc68c45c4e98c7f92e456e3be30cae71c60880a8524a7270c4c779af117c0c3`. Scope and severity remain the existing OP-02 S2 bounded-section property (CS-09 and frozen E03/E12). This is a residual of the same container-state defect, not a new Markdown feature requirement or new qualification scope.

The original quoted-fence reproduction now refuses, and 22 mechanical tests pass from the frozen review copy. That supports the selected fence correction. However, `read_basis.py:104–121` still treats a comment opener inside a quote as globally active across the quote's end. The valid specimen below positively returns unselected section Two as part of requested One:

~~~~markdown
## One
> <!--
> quoted comment
## Two
UNSELECTED TWO
> -->
## Three
UNSELECTED THREE
~~~~

The exact frozen CLI exits 0, `status: checked`, `first_line: 1`, `last_line: 6`, and includes `UNSELECTED TWO`. A sound closed selector may refuse this structure; otherwise One ends at line 3. The [CommonMark 0.31.2 HTML-block rule](https://spec.commonmark.org/0.31.2/#html-blocks) ends an HTML block at its containing block's end when its normal terminator is not encountered. Quote termination makes Two a real same-level heading. Merely checking quote/list fences and headings does not cover comment state spanning the same boundary.

Reproduction: `REPRO_COMMENT_CONTAINER.py` SHA256 `c6b2f728e299b00809c96ba5c5899ca2834b414439908d36b8d97c1c4f4bc434`. Exact full CLI evidence: `COMMENT_CONTAINER_REPRO.json` SHA256 `6b1788a46f71a35ddfc496ee02016e6c6403fb54331342d07804159f44737472`. It uses the same isolated review-owned mock manager/manifest approach as the original OP-02 and does not change candidate sources or the installed release. Original discriminator replay is separately retained in `SECTION_CONTAINER_REPRO.json` and returns refusal.

Correction must either conserve comment-container boundaries or reject unsupported comment placements before returning a positive source projection/catalog. No specific implementation is authored by this reviewer. No occurrence in the actual released 3.0.3 owner files or live traces is claimed; a bounded successful ordinary-source read remains evidence for its own input. Product priority and disposition remain Executive decisions. Same-family nonauthor review remains bounded working evidence.
