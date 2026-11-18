# Milestone B file driver and development report

**SOURCE.** R20 lines 1000, 1018–1019, 1024 and 1044 require the evaluator outcomes, the ordinary wrong-kind result, fuel and the program/input/output/build record. Line 1046 reserves room for a later sequence kind’s starting state and makes and writes. The reviewed milestone forms supply the following development format. The meter prices are provisional.

## Invocation

**PROPOSED in B-O01 and B-F03–B-F07.**

```text
loom-b --program FILE --entry WORD --input NAT --fuel NAT [--max-source-bytes NAT] [--max-value-bytes NAT]
```

Each required flag appears once, in any order. Each optional flag appears at most once. A flag needs a following token that does not begin with two hyphens. A single-hyphen token is a value. No positional token or implicit entry is accepted. FILE is one literal path. WORD is an ASCII letter or underscore followed by zero or more ASCII letters, underscores or digits. NAT is 0 or a nonzero ASCII digit followed by zero or more ASCII digits. Input, fuel and both limits use NAT. The two effective limits each start at 1048576 bytes. A valid override, including zero, supplies the corresponding limit. An invalid spelling cannot supply an override.

**PROPOSED in B-O03/B-O05/B-O07.** Choose the first unknown, duplicate or valueless flag in argv order. The first flag has index zero. Then check missing program, entry, input and fuel in that order. Validate entry, input, fuel, source limit and value limit in order. Diagnostics retain the offending token or flag and all required facts. For reporting, retain the first recognized value of each flag obtained up to a structural error. A valid supplied word, input or budget can be recorded even if another argument fails. Unavailable or invalid entry/input/budget fields are null.

## One source and one evaluation

**SOURCE and PROPOSED in G1-C1, B-O01/B-O03/B-O06/B-O07 and B-C03.** Open one binary stream. Accumulate through EOF up to the accepted source limit, testing the first disallowed byte before decoding. Immediately after EOF, record the complete byte length. Then compute SHA-256 over that immutable string and give the same string to the reader’s byte entry. If hashing fails, the tool-fault report retains the byte length and gives null for the unavailable digest. Retain that binding on every subsequent outcome, including reader refusal. An open or read fault gives null source identity. A source limit stop reports the limit and the first disallowed count. The complete-source fields are null when the bounded read ended before EOF. No report uses a prefix digest.

**PROPOSED in B-F03–B-F07, B-O02/B-O05/B-O07 and B-C03/C08.** Strict UTF-8 decoding, whole-file lexing, then parsing precede global collection, declaration arity, binder checks, resolution of every body in order and selection of the entry. The driver uses the committed reader and checker and preserves their causes and positions. Checking, source/input interning and reporting are unmetered. An admitted program uses the same value store, a fresh meter and the metered primitive evaluator. Invalid input at fuel zero still refuses. A valid program at zero stops at its entry attempt.

## Development record

**PROPOSED in B-O02–B-O06.** Write one compact UTF-8 JSON object and a single LF to binary stdout. Use the B-O03 field order and the following structure; decimal quantities and indices are canonical strings. Unknown metadata uses JSON null.

| Field | Value |
| --- | --- |
| schema, status, code | `loom-b-report/1-candidate`, outcome and exact cause |
| profile, meter | `milestone-b-forms/1-candidate`, `milestone-b-ARTW/1-candidate` |
| contract_manifest_sha256, build_snapshot_sha256 | SHA-256 of the verified R1 paper manifest and exact build-input snapshot compiled into this executable |
| source_sha256, source_bytes | SHA-256 and byte length of the complete binary source |
| entry, input | Object with name and admitted definition_index, then the supplied input decimal |
| checking, reporting | Object with reading, resolving and checking each set to `unmetered`, then `unmetered` |
| limits | Effective source_bytes and value_bytes |
| execution | started, budget, used, remaining |
| at | definition_index, expr_path, source_offset; a definition body root has an empty path |
| invoice | A, R, T, W, total for a known failed bill, otherwise null |
| value, facts | Returned graph or null, then the cause-specific object |

**PROPOSED in B-O02/B-O03/B-O05/B-O06.** A return uses `returned/value.returned` and exit 0. Builtin none is an ordinary return. A fuel stop uses `out_of_fuel` and exit 2, the exact meter code, the first stopped site, event and zero failed_operation_debit. Wrong-kind includes the primitive operation. A bound-unavailable stop carries its reason and a null invoice. A refusal uses `refused` and exit 3. A tool fault uses `tool_error` and exit 4. Before entry, used is zero and remaining equals the parsed budget or is null. After the entry attempt, started is true and used plus remaining equals the budget. A value-limit fault keeps the completed accounting, null value and evaluation_status `returned`. Report I/O failures preserve the OS error and process exit on stderr if stdout is unusable. After a first encoding failure, attempt one detailed tool-fault report. If recovery also fails during construction, encoding or writing, make one best-effort static stderr diagnostic and terminate with exit 4. That final path performs no report encoding and requires no writable stream. Host memory, stack and internal faults retain the phase and available accounting. Only an actual meter stop reports fuel exhaustion.

**PROPOSED in B-O04/B-O08 with the owner’s tuple spelling.** The graph has root `"0"` and a nodes array. Assign IDs in depth-first preorder, visiting fields left to right. Emit each equal value once, list nodes in ID order and retain every field reference in position order. Natural, tuple and none nodes carry respectively decimal, fields, or only id and kind. Apply the value limit to the exact UTF-8 payload from the graph’s opening to closing brace, excluding the report envelope and LF. In historical fixtures the builtin constructor, value tag and fuel event spelled `row` map to `tuple`. Identifiers and diagnostic tokens retain their actual spelling. Per R20 line 1046, future sequence history can occupy a new optional member and node kind. B emits only its current members.

**PROPOSED implementation of B-O03/B-O05/B-O08.** Reader offsets use `at.source_offset`. EOF uses the reader probe’s unambiguous `<EOF>` spelling; an actual word keeps its spelling. Checker facts come from its named cause interface. I/O facts carry operation and system_error. The build ledger binds the native executable, its generated identity module, the source snapshot and the reviewed paper manifest. Verification compares the real exit and raw report bytes, including final LF, with fixture evidence and independently computed source and build identities.
