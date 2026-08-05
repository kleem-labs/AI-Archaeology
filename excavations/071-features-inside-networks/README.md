# Excavation 071 — Features Inside Networks

[Previous: Excavation 070](../070-bandits/README.md)

## Take the First Step Yourself

> **Your problem:** A trained network works, but where is “striped animal” represented?

> **Try your first idea:** Search for one neuron dedicated to each human concept.

> **Now try to break your idea:** The concept disappears when one neuron is removed yet can still be decoded from a pattern across many neurons.

> Stop here. State the missing requirement without naming the repair.

## The Observation

A trained network works, but where is “striped animal” represented?

## Your First Attempt

Search for one neuron dedicated to each human concept.

## Break Your First Attempt

The concept disappears when one neuron is removed yet can still be decoded from a pattern across many neurons.

## Repair Your Attempt

Treat representations as distributed directions and test them across varied examples.

## What You Have Just Invented

**Treat representations as distributed directions and test them across varied examples.**

## Rebuild the Discovery with a Concrete Case

Tiger and zebra activate overlapping patterns; subtracting ordinary cats isolates a stripe-related direction better than one cell.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

Human labels may not match the model’s internal abstractions.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 072](../072-linear-probes/README.md)
