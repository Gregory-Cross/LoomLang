# Milestone B reader

Piece 12a reads a binary source file and accounts for every definition in source order (M-30 and RD-C1). An empty or whitespace-only file has zero definitions. A malformed declaration anywhere refuses the whole file, including when a valid definition precedes it.

**PROPOSED** — The OCaml module returned by `Reader.Make` exposes `read_file` for a file and `read_bytes` for an in-memory source. Its success record holds the original bytes, the ordered definitions and the end position.

## Source text

**SOURCE** — FORMS.md B-F04 specifies strict UTF-8, case-sensitive ASCII words and ASCII digits. It admits space, tab, CR, LF and CRLF as whitespace. The four punctuation characters are `[`, `]`, `,` and `=`. Scan each word and each decimal digit run to its maximal length (B-F03). A BOM, comments, parentheses, quoting and signs have no spelling in this grammar.

```text
program    ::= definition* EOF
definition ::= "def" word "[" names? "]" "=" expr
names      ::= word ("," word)*
expr       ::= natural | word | word "[" arguments? "]"
arguments  ::= expr ("," expr)*
word       ::= [A-Za-z_][A-Za-z0-9_]*
natural    ::= "0" | [1-9][0-9]*
```

The owner's E-40 answer fixes the provisional definition spelling, with one body and no terminator. The milestone vocabulary is `def`, `add`, `sub`, `mul` and `tuple`. The provisional fixed-position value spelling is `tuple`. The word `row` follows the ordinary identifier grammar. Words remain intact at declaration names, binders, references and application heads, including words whose reserved roles 12b will check.

## Forms and positions

**PROPOSED** — The OCaml definition record carries its written name, ordered parameter list, one body and its span from `def` through the body. Each name has its own span. The interface represents the three B-F03 expression forms with `Literal`, `Reference` and `Apply`. Empty parameter and argument lists are represented explicitly. `Apply` preserves the raw head and ordered children of arithmetic, tuple construction and named calls. A literal pairs its canonical source digits with the exact piece 11 value interned by the caller's value store. Source occurrences retain their own spans even when their value is shared.

**SOURCE** — OUTCOMES.md B-O07 measures offsets from zero in the original UTF-8 bytes and places EOF at the file's byte length.

**PROPOSED** — Spans are half-open. Lines and columns start at one. A tab advances one column, as does each other decoded Unicode scalar within a line. LF, CR and the pair CRLF each produce one displayed line break and reset the column to one. A refusal points to the start of its offending token, scalar or ill-formed sequence, or to EOF. The syntax diagnostic carries `Token` with the original spelling or `End_of_source` for EOF.

## Refusals and tool faults

Apply the ordering in OUTCOMES.md B-O05 through B-O07. Check the byte limit, validate UTF-8 across the whole file, scan all tokens left to right, then parse left to right. At the first failure in the selected pass, return its location and facts.

| Source refusal | Cause and facts |
| --- | --- |
| `read.encoding` | Ill-formed UTF-8 sequence at its starting byte. |
| `read.character` | Unsupported scalar, its Unicode code point and its starting byte. This includes U+FEFF. |
| `read.noncanonical_natural` | Digit run of length greater than one beginning with zero, its complete token and start. |
| `read.syntax` | Expected token or token class, actual token or EOF, and its start. A comma in a list requires a further parameter or expression. |

**SOURCE** — OUTCOMES.md B-O05 places the byte offset in `at.source_offset` and uses canonical decimal spellings for reported numeric facts. B-O06 specifies the tool faults and their facts. `tool.source_io` supplies the failed file operation and system error. `tool.source_limit` supplies `limit` and `observed_at_least`. Host allocation and stack failures carry the reader phase as `tool.host_memory` and `tool.host_stack`. An unexpected internal failure carries the phase and reason as `tool.internal_error`.

**PROPOSED** — The OCaml error variant `Refused` pairs a cause with a `position` record containing `source_offset`, `line` and `column`. `Tool_error` carries a separate fault value. For `tool.source_limit`, the reader sets `observed_at_least` to the first disallowed byte count, `limit + 1`.

**SOURCE** — OUTCOMES.md B-O01 gives a default source limit of 1,048,576 bytes and allows the caller to supply any exact natural, including zero.

**PROPOSED** — The parser keeps open applications on an explicit stack.

**INFERENCE** — The smallest complete program with application depth `d >= 1` has `8 + 3*d` bytes, using `def f[]=` and nested single-letter heads around an empty application. Thus the default limit accommodates at most 349,522 nested applications. One more needs 1,048,577 bytes and can be read with that larger source limit.

## Charges and subsequent checks

CHARGES.md B-C03 places reading, decoding, parsing and interning source literals outside execution fuel. The reader takes no fuel and there is no checking budget. A tool byte limit applies to the input itself.

Piece 12b owns global collection, duplicate and reserved-name checks, binding, arities, entry lookup and resolution of every body, including unused declarations. RD-C1 assigns the rule-that-can-never-match control to 12b. Execution, charging operations and rendering the invocation report belong to later pieces.
