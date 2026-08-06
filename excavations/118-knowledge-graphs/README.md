# Excavation 118 — Knowledge Graphs

[Previous: Excavation 117](../117-neuro-symbolic-systems/README.md)

## Take the First Step Yourself

> **Your problem:** How can facts preserve who relates to whom instead of becoming one text paragraph?

> **Try your first idea:** Store every fact as an isolated sentence.

> **Now try to break your idea:** Repeated entities, reverse links, and multi-hop questions become difficult to traverse.

> Stop here. State the missing requirement without naming the repair.

## The Observation

How can facts preserve who relates to whom instead of becoming one text paragraph?

## Your First Attempt

Store every fact as an isolated sentence.

## Break Your First Attempt

Repeated entities, reverse links, and multi-hop questions become difficult to traverse.

## Repair Your Attempt

Represent entities as nodes and named relations as edges.

## What You Have Just Invented

**Represent entities as nodes and named relations as edges.**

## Rebuild the Discovery with a Concrete Case

Tiger —is_a→ cat and cat —is_a→ mammal support a two-hop ancestry query.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

Graphs can be incomplete, stale, and uncertain.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 119](../119-graph-neural-networks/README.md)
