# OP-02 adjacent unsupported HTML discriminator

Same revision-3 source, same CS-09 closed-section property and same existing S2 finding. `ADJACENT_HTML_DISCRIMINATORS.json` SHA256 `a4fbe895f041f3059b587072aae52c6796859e54e6cfb947f606d31caa691424` records direct calls of the exact frozen `headings()` and `sections()` implementations. This is function-level source behavior, distinct from the already retained full quoted-comment CLI reproduction.

The CDATA and declaration specimens place `## Two` inside `<![CDATA[ ... ]]>` and `<!FOO ... >` respectively. The reader invents and returns Two as a named section. The [CommonMark HTML-block definition](https://spec.commonmark.org/0.31.2/#html-blocks) treats these as HTML blocks until their terminators; Two is not an ATX section. The reader's HTML-refusal check recognizes DOCTYPE and other tag forms but misses these declaration/CDATA openers. The shipped source explicitly claims refusal of unsupported HTML rather than general HTML support. Positive projection is therefore wrong; conservative refusal is sufficient.

The record also exposes how a comment opener following ordinary paragraph text can carry the same global comment state across an ATX heading. Block structure is determined before inline structure; a column-zero ATX heading interrupts the paragraph. This is a further comment-placement discriminator, not a request for a general parser. The original quoted-comment case remains the primary full-CLI evidence.

No actual released source occurrence, native-session leak, candidate repair or stronger whole-method claim is inferred from these specimens. They help distinguish the selected closed selector from a superficially narrower token-only repair.
