# OCaml reference evaluator · increment 1

This is the R2 reference evaluator for Loom’s resolved, unary natural-number programs. It runs top entry, local and literal reads, Add and truncated Sub under one serial root with separate work and construction grants. The production compiler is a separate implementation.

The installed evaluator specifications cover batches 1, 2, 9 and 10 as well as Add and Sub. This increment exercises entry and reads from batch 2 and the Add and Sub rules. Multiplication, wrong-kind handling, shifts and bitwise operations are outside its executable receipt. [Evaluator specification index](../../docs/spec/README.md) · [Add](../../docs/spec/evaluator/ADD.md) · [Sub](../../docs/spec/evaluator/SUB.md)

A resolved graph identifies operands and local bindings by position. A fixture fixes the graph or obtained operands, grant, schedule and observer. The ordinary observer sees the return or stop. The linked exact observer also sees the readings purchased for the selected occurrence. [Graph and fixture format](GRAPH-INPUT.md)

## Build and run

Use Python 3.9 or later and the recorded Windows x64 OCaml 5.5.2 / MinGW-w64 GCC 16.2.0 distribution. Set `LOOM_OCAML_TOOLCHAIN` to the distribution directory containing `ocaml/bin` and `msys64/mingw64/bin`. From this directory, choose fresh output directories outside the checkout. On the shared Loom host, hold the build and run slots for native compilation and the run slot for fixture execution.

~~~powershell
$work = Join-Path ([System.IO.Path]::GetTempPath()) ('loom-ocaml-' + [guid]::NewGuid().ToString('N'))
$bin = Join-Path $work 'build'
$capture = Join-Path $work 'capture'
New-Item -ItemType Directory -Path $work | Out-Null
python -B run.py build --toolchain $env:LOOM_OCAML_TOOLCHAIN --out $bin
python -B run.py run --build $bin --out $capture
~~~

The default run writes both observers’ canonical records to `records.jsonl` in the capture directory. Use `--observer ordinary` or `--observer trial-exact` to select one observer. Use `--probe` at build time for the instrumented image. The runner records the probe-switch setting and links nat, json, probe_switch, core, resolved_graph, arithmetic and driver in that order.

## Receipt and standing

**PARTIAL.** Independent source and account review, native rebuild, trace comparison and witness decoding cover the named R2 edition and 47 starts under both observers. The 94 runs produced 150 witnesses, 92 projections and two pre-entry refusals. On the recorded toolchain, the regular executable SHA-256 is `c6f7411dd411962cd7d46e43d32293518a5fe78a2eb84a887167cfb735255120` and the 188,182-byte full capture SHA-256 is `7134001b89cdfa34838427d224f06ea224096e6227d7d3bdb4d22a3c74360b50`. These identities support a byte-for-byte comparison on the recorded configuration.

The receipt is limited to these graphs, operations, observers and grants. Whole-slice conformance, production-compiler acceptance, resource qualification on real workloads, an official demonstration and stage advancement remain open.
