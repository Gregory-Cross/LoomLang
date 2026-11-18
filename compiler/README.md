# OCaml compiler build bootstrap

This milestone piece builds a trivial greeting module and a standard-library
test runner. It does not implement the evaluator or read Loom programs.

OCaml 5.5.2 is the existing private installation at
`C:\LoomBuild\toolchains\ocaml-check-20261117-1500`. No package manager or
download is needed. Run these commands with the installed Python:

```powershell
C:\Python314\python.exe -B C:\LoomLang\compiler\build.py build --kind clean --directory C:\LoomBuild\codex\loom-compiler\b01
C:\Python314\python.exe -B C:\LoomLang\compiler\build.py build --kind rebuild --directory C:\LoomBuild\codex\loom-compiler\b01
C:\Python314\python.exe -B C:\LoomLang\compiler\build.py test --directory C:\LoomBuild\codex\loom-compiler\b01 --suite pass.tests
C:\Python314\python.exe -B C:\LoomLang\compiler\build.py test --directory C:\LoomBuild\codex\loom-compiler\b01 --suite intentional-failure.tests
C:\Python314\python.exe -B C:\LoomLang\compiler\build.py test --directory C:\LoomBuild\codex\loom-compiler\b01 --suite empty.tests
```

The clean command requires a new directory, an immediate child of the build
root. Use another name if `b01` already exists; no deletion is performed.
Rebuild compiles the same ordered set again in that directory. All copied
sources, compiler products, private home/cache/temp folders and logs go there.
The sources under `compiler/src` are never compiled in place.

The command invokes `ocamlopt.exe` by absolute path. Its children receive the
successful contained check's explicit private environment, with writable home,
cache and temporary directories relocated into the build directory. The private
PATH is the exact successful check's value. The command does not mutate its own,
the user's or the system's environment. Tools invoked inside OCaml may use that
private search path, as in the contained check.

Each build holds the shared build slot and run slot, in that order. Each test
run holds the run slot. A busy slot refuses immediately; owned slots are
released in reverse order on success or failure. An unreadable acquisition
response also triggers a holder-checked cleanup attempt; an unconfirmed release
is reported as an error. Forced termination can still require coordinator
recovery of a stale slot. Tokens stay in memory. The
JSON logs record commands, source hashes, exit codes, output, times, slot events
and sampled physical-memory and commit-headroom minima. The ordered module set
uses one compiler driver at a time.

Test manifests are UTF-8 plain text with three tab-separated fields per row:
test name, input fixture file name, expected fixture file name. Blank lines and
`#` comments are ignored. Fixture bytes and expected results are independent of
the OCaml code. The runner reports names and selected/passed/failed counts.
`pass.tests` must exit 0; `intentional-failure.tests` must name one failed test
and exit 1; `empty.tests` must report zero selected and exit 2. Those latter two
non-zero outcomes are expected verification controls, not a green test suite.
