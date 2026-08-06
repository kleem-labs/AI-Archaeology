# Excavation 120 — Program Synthesis

[Previous: Excavation 119](../119-graph-neural-networks/README.md)

## Take the First Step Yourself

> **Your problem:** Can examples specify a reusable procedure rather than one output?

> **Try your first idea:** Memorize the provided input-output pairs.

> **Now try to break your idea:** A new input exposes the absence of an underlying algorithm.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Can examples specify a reusable procedure rather than one output?

## Your First Attempt

Memorize the provided input-output pairs.

## Break Your First Attempt

A new input exposes the absence of an underlying algorithm.

## Repair Your Attempt

Search or generate candidate programs, execute them, and keep those satisfying examples and constraints.

## What You Have Just Invented

**Search or generate candidate programs, execute them, and keep those satisfying examples and constraints.**

## Rebuild the Discovery with a Concrete Case

Examples 2→4 and 3→6 suggest multiply by two; testing 5 distinguishes it from memorized lookup.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

Finite examples rarely identify one unique intended program.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 121](../121-formal-verification/README.md)
