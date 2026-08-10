# Excavation 118 — Knowledge Graphs

[Previous: Excavation 117](../117-neuro-symbolic-systems/README.md)

How can facts preserve who relates to whom instead of becoming one text paragraph?

At first, the simplest answer is tempting: Store every fact as an isolated sentence.

But the simplicity has discarded something important: Repeated entities, reverse links, and multi-hop questions become difficult to traverse.

The missing information determines the next move: Represent entities as nodes and named relations as edges.

## Now work a case you can see

Tiger —is_a→ cat and cat —is_a→ mammal support a two-hop ancestry query.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Graphs can be incomplete, stale, and uncertain.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 119](../119-graph-neural-networks/README.md)
