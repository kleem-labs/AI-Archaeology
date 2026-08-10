# Excavation 120 — Program Synthesis

[Previous: Excavation 119](../119-graph-neural-networks/README.md)

Can examples specify a reusable procedure rather than one output?

The first solution that suggests itself is this: Memorize the provided input-output pairs.

The idea survives only until we test it against reality: A new input exposes the absence of an underlying algorithm.

The failure gives us a precise requirement: Search or generate candidate programs, execute them, and keep those satisfying examples and constraints.

## Now work a case you can see

Examples 2→4 and 3→6 suggest multiply by two; testing 5 distinguishes it from memorized lookup.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Finite examples rarely identify one unique intended program.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 121](../121-formal-verification/README.md)
