# Excavation 118 — Knowledge Graphs

A neuro-symbolic system gives learned perception and exact rules distinct jobs. Those rules need facts stored with explicit entities and relationships rather than buried inside one paragraph or vector.

Using what we have, we store every fact as an isolated sentence.

That confidence lasts only until repeated entities, reverse links, and multi-hop questions become difficult to traverse.

So we represent entities as nodes and named relations as edges.

## Let the case decide

Tiger —is_a→ cat and cat —is_a→ mammal support a two-hop ancestry query.

## The boundary of the discovery

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
