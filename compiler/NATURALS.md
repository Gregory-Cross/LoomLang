# Naturals: milestone B pieces 2 and 3

`Natural` is an abstract immutable natural number, stored in little-endian
30-bit limbs. It has decimal reading/printing, comparison, addition, subtraction
that stops at zero, multiplication and exact mathematical bit length.
`sub(2, 5)` is zero and `mul(7, 7)` is 49. There is no selected maximum number; allocation,
array and string capacity remain finite host resources. Host failures are not
fuel exhaustion or semantic refusals. Metering itself belongs to a later piece.

The source comment proves each arithmetic intermediate fits OCaml's 63-bit
native integer, including the product-plus-carries bound. Subtraction's signed
intermediate is between `-B` and `B-1`; multiplication's is at most `B^2-1`,
where `B=2^30`. The sum of product array lengths is checked before addition.
Inputs remain immutable, including when both arguments refer to the same value.
`bit_length`
returns a natural rather than computing an overflowing native `30 * length`.
It returns zero for zero. The future meter can use this exact component without
this module deciding its full tariff or the charge for a zero-valued argument.

Use the existing Python installation. The command calls piece 1's process,
memory, private environment and shared-slot helpers; it adds its own ordered
module list and link step. It pins the exact helper bytes, including their
interruption cleanup repairs. Pieces 1 and 2 supply the committed baseline;
any helper change requires an explicit pin update and fresh verification.

```powershell
C:\Python314\python.exe -B C:\LoomLang\compiler\naturals_build.py build --kind clean --directory C:\LoomBuild\codex\loom-compiler\b03
C:\Python314\python.exe -B C:\LoomLang\compiler\naturals_build.py build --kind rebuild --directory C:\LoomBuild\codex\loom-compiler\b03
C:\Python314\python.exe -B C:\LoomLang\compiler\naturals_build.py check --directory C:\LoomBuild\codex\loom-compiler\b03
C:\Python314\python.exe -B C:\LoomLang\compiler\naturals_build.py check --directory C:\LoomBuild\codex\loom-compiler\b03 --control wrong-sum
C:\Python314\python.exe -B C:\LoomLang\compiler\naturals_build.py check --directory C:\LoomBuild\codex\loom-compiler\b03 --control wrong-product
C:\Python314\python.exe -B C:\LoomLang\compiler\naturals_build.py check --directory C:\LoomBuild\codex\loom-compiler\b03 --control zero
```

Choose a new directory for the clean build. Builds hold the build and run slots;
oracle and native checks hold the run slot and execute serially. Busy slots are
retried for up to 600 seconds by default, with visible waiting messages. All
code generation, private writable directories, requests, expected/actual text
and logs are under that build directory. The helper's private PATH is reused
unchanged. No user/system environment, installation or toolchain write is needed.
After acquiring the run slot, a check reads the build ledger, validates the
executable and records its matched SHA-256. It holds that slot through comparison
so a cooperating rebuild cannot replace the validated artifact during the check.

The oracle is a separate Python process using only built-in integers and the
standard library. It imports no OCaml implementation or corpus code. The
native probe imports no Python. Their interface is UTF-8 tab-separated text:
`name`, `operation`, `left decimal`, `right decimal or -`; replies are `name`
and `decimal result` (or `INVALID` for rejected parse input). Leading zeroes
are accepted; signs, separators and whitespace are rejected by decimal input.
The smoke requests and literal expected answers are in separate fixture files.
Request files may use LF or CRLF line endings. Line framing is removed without
trimming operand whitespace; tabs and newlines delimit the transport fields
and rows and cannot be embedded in a decimal operand.
A final row may omit its line ending; all its operand bytes are preserved.
Only a CR immediately followed by the terminating LF is removed as framing.

The generated finite corpus covers each radix boundary `2^(30*k)` for every
`k=1..113` and its two neighbours, carry chains, equal-prefix comparisons,
native word boundaries, decimal group boundaries and 128 fixed-seed random
pairs up to 1,024 decimal digits. Boundary 113 is 1,021 decimal digits and enters
114 limbs. This is finite evidence, not exhaustive arithmetic verification.
Additional named cases cover zero in either operand position, equal-length
comparisons whose decisive middle limb opposes the low limbs, multi-limb
carry-to-zero chains and uneven-length overflow, and inputs of 115, 128 and
256 limbs. Every operation also receives leading-zero input. Parse cases
reject empty text, signs, spaces, separators, non-digits and non-ASCII input.
A constructed decimal-printing case reaches the maximum division numerator
`10^9 * 2^30 - 1`. No enormous allocation is made merely to force a multi-limb
bit-length result; that general case still relies on the implementation's
natural-valued construction and its reviewed bound.
Piece 3 adds 128 random pairs with seed `0x4C4F4F4D0301`, again up to 1,024
decimal digits, with subtraction and multiplication in both operand orders.
Its named cases cover borrow chains at every `B^k`, `k=1..113`, the minimum
subtraction intermediate `-B`, underflow, equality, multiplication by zero and
one, dense and alternating limbs, asymmetric products, and squares through
256 limbs (up to 512 result limbs). Equal operand text makes the probe reuse
one value, so these cases also check aliasing without input mutation.
The full corpus has 5,997 named cases, including the previous 4,245 cases and
28 literal smoke answers. Each operation's count and both seeds are in the
command's corpus metadata. The earlier random seed is `0x4C4F4F4D0201`.
Every operation has a unique name; a missing/duplicate result or zero compared
count fails. Full generated text and named outcomes stay in the build log tree
for a second implementation to reuse unchanged. The Python version is recorded.

The normal check must return 0. The development-only wrong-sum switch changes
the selected `7+8` result from 15 to 16; comparison must fail and return 1.
The wrong-product switch changes the selected `7*7` result from 49 to 50;
its single comparison must also fail and return 1. The
empty comparison control returns 2 and reports `zero compared count`. These
non-zero controls are expected failures, not passing test suites.
