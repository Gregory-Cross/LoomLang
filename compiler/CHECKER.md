# Milestone B resolver and checker

**SOURCE** — FORMS.md B-F03 through B-F07 define this first-order, unary profile. The checker receives all definitions from a successful piece 12a read and the entry word supplied by the invocation. OUTCOMES.md B-O07 assigns argument validation and source reading to earlier passes. The owner selected this milestone and its provisional vocabulary, then renamed the fixed-position value to `tuple` and approved the definition spelling in E-40. The five reserved words are `def`, `add`, `sub`, `mul` and `tuple`. The spelling `row` follows the ordinary name rules.

**PROPOSED** — `Checker.check ~entry` accepts a `Reader.program` and an already validated entry word. It returns the admitted program or the first diagnostic. A refusal exposes its cause, its location and the B-O05 facts. Host failures use the separate B-O06 tool-fault channel with the active phase.

## Check order

**SOURCE** — Apply OUTCOMES.md B-O07 passes 3 through 6 in the following order, using the roles and arities in FORMS.md B-F05 through B-F07.

1. Collect every global name in declaration order and give it its zero-based definition index. At each name check first for a reserved word, then for a duplicate. The first occurrence supplies the original index.
2. Check the parameter count of every declaration in order. Each must have exactly one. After all counts pass, check every binder in declaration order. At each binder check for a reserved word, then for collision with any global, including a later declaration. Each parameter binds only its own body.
3. Resolve every body in declaration order and each expression in preorder. A bare word must name the local parameter. An absent bare word is unbound. A known word of another role is a wrong-role refusal. For an application, check the head's existence and role, then its arity, then its children from left to right. The three arithmetic primitives each take two arguments, `tuple` takes any number, and a named definition takes one. A parameter and `def` have the wrong role at a call head. Forward, self and mutual calls are admitted. Operand kinds are determined at execution.
4. Select the entry after all bodies pass. A reserved entry has the wrong role. A different absent entry is missing. An entry declaration of the wrong arity has already failed pass 2, including when some other definition would have been selected.

**SOURCE** — M-30 and RD-C1 assign the never-matching-rule control to 12b. B-F03 and B-F07 have no pattern rule or case alternative that can never match. B-F06 requires every unused definition to be checked and permits a valid definition unreachable from the selected entry.

## Refusals and positions

**SOURCE** — OUTCOMES.md B-O05 specifies the following cause names and facts. B-O03 and B-O07 locate body nodes by definition index and a zero-based child-index path from the root. B-O07 measures source offsets in raw UTF-8 bytes from zero. Numeric report facts use canonical decimal strings. The `actual_role` spellings are `local`, `definition`, `primitive`, `constructor` and `keyword`. For `resolve.wrong_role`, `required_role` is `local` for a bare reference and `callable` for a call head. In the table, the last column gives the PROPOSED anchors used by the OCaml interface.

| B-O05 cause | Facts | PROPOSED location |
| --- | --- | --- |
| `check.reserved_global` | `name`, `declaration_index` | Reserved definition name |
| `check.duplicate_global` | `name`, `first_index`, `second_index` | Second definition name |
| `check.unsupported_definition_arity` | `name`, `actual` parameter count | Name of the non-unary definition |
| `check.reserved_binder` | `name`, `definition_index` | Reserved parameter |
| `check.binder_global_collision` | `name`, `definition_index`, `global_index` | Colliding parameter |
| `resolve.unbound_variable` | `name` and node location | Bare word |
| `resolve.unknown_call` | `name` and node location | Call head |
| `resolve.wrong_role` | `name`, `actual_role`, `required_role` and node location | Bare word requiring `local` or head requiring `callable` |
| `resolve.primitive_arity` | `name`, `expected`, `actual` and node location | Primitive head |
| `resolve.named_arity` | `name`, `expected`, `actual` and node location | Named call head |
| `invoke.entry_missing` | `name` | Invocation entry word |
| `invoke.entry_wrong_role` | `name`, `actual_role` | Invocation entry word |

**PROPOSED** — A source diagnostic carries the owning definition index and the start position of the indicated word in the reader. Its line and column follow READER.md. Declaration and binder diagnostics have no expression path. At a body root the path is the empty list. On entry lookup failure the location is `Entry_argument`. The supplied word comes from the invocation and has no source offset, line, column, definition index or expression path.

## Admitted program and charges

**SOURCE** — B-F05 and B-F06 require fixed local slots and definition indices, written declaration and child order, literals, tuple construction, binary arithmetic and unary named calls. All bodies must resolve before entry. B-F06 and the piece 12 plan allow the meter and frames to consume resolved forms without looking up display names during execution.

**PROPOSED** — The admitted program provides the original bytes, an indexed definition table and its selected entry index. Each definition keeps its name, parameter and reader spans as metadata. Each expression carries its source span and one of five forms. These are an existing piece 11 literal value, local slot zero, an ordered list of tuple children, a tagged binary primitive with two children, or a fixed definition index with one call argument. Consumers can reconstruct a node path from the definition index and ordered children. The table is exposed through read-only accessors.

**SOURCE** — CHARGES.md B-C03 places resolution and checking outside execution fuel and gives B no checking budget. B-O02 and B-O07 require a semantic refusal before execution even with zero fuel. Pieces 13 and 14 receive the admitted forms for metering and frames. Piece 12b performs no evaluation.
