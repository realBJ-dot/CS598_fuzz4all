V8 is a JavaScript and WebAssembly engine developed by Google for its Chrome browser.[1][4] V8 is free and open-source software that is part of the Chromium project and also used separately in non-browser contexts, notably the Node.js runtime system.

Google created V8 for its Chrome browser, and both were first released in 2008.[4] The lead developer of V8 was Lars Bak, and it was named for the powerful car engine.[5] For several years, Chrome was faster than other browsers at executing JavaScript.[6][7][8]

The V8 assembler is based on the Strongtalk assembler.[9] On 7 December 2010, a new compiling infrastructure named Crankshaft was released, with speed improvements.[10] In version 41 of Chrome in 2015, project TurboFan was added to provide more performance improvements with previously challenging workloads such as asm.js.[11] Much of V8's development is strongly inspired by the Java HotSpot Virtual Machine developed by Sun Microsystems, with the newer execution pipelines being very similar to those of HotSpot's.

Support for the new WebAssembly language began in 2015.[12]

In 2016, the Ignition interpreter was added to V8 with the design goal of reducing the memory usage on small memory Android phones in comparison with TurboFan and Crankshaft.[13] Ignition is a register based machine and shares a similar (albeit not the exact same) design to the templating interpreter utilized by HotSpot.

In 2017, V8 shipped a brand-new compiler pipeline, consisting of Ignition (the interpreter) and TurboFan (the optimizing compiler). Starting with V8 version 5.9, Full-codegen (the early baseline compiler) and Crankshaft are no longer used in V8 for JavaScript execution, since the team believed they were no longer able to keep pace with new JavaScript language features and the optimizations those features required.[14]

In 2021, a new tiered compilation pipeline was introduced with the release of the SparkPlug compiler, which supplements the existing TurboFan compiler within V8, in a direct parallel to the profiling C1 Compiler used by HotSpot.

In 2023, the Maglev SSA-based compiler was added, which is 10 times slower than Sparkplug but 10 times faster than TurboFan, bridging the gap between Sparkplug and TurboFan for less frequently run loops that do not get "hot" enough to be optimised by TurboFan, as is the case for most web applications that spend more time interacting with the browser than in JavaScript execution.

V8 first generates an abstract syntax tree with its own parser.[16] Then, Ignition generates bytecode from this syntax tree using the internal V8 bytecode format.[17] TurboFan compiles this bytecode into machine code. In other words, V8 compiles ECMAScript directly to native machine code using just-in-time compilation before executing it.[18] The compiled code is additionally optimized (and re-optimized) dynamically at runtime, based on heuristics of the code's execution profile. Optimization techniques used include inlining, elision of expensive runtime properties, and inline caching. The garbage collector is a generational incremental collector.
V8 can compile to x86, ARM or MIPS instruction set architectures in both their 32-bit and 64-bit editions; it has additionally been ported to PowerPC[20] and IBM ESA/390[21][22] for use in servers.[23]

V8 can be used in a browser or integrated into independent projects. V8 is used in the following software:

Chromium-based web browsers - Google Chrome, Brave, Opera, Vivaldi and Microsoft Edge.
Firefox - parts of V8 ported to the browser for regular expressions parsing
Couchbase database server
Deno runtime environment[24]
Electron desktop application framework, used by the Atom and Visual Studio Code text editors
MarkLogic database server
NativeScript mobile application framework[25]
Node.js runtime environment[26]
Qt Quick runtime environment[27]

