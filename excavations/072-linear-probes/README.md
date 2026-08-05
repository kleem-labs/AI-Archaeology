# Excavation 072 — Linear Probes

[Previous: Excavation 071](../071-features-inside-networks/README.md)

## Take the First Step Yourself

> **Your problem:** Can a hidden layer already separate animal species?

> **Try your first idea:** Train a powerful classifier on hidden states and call any success evidence.

> **Now try to break your idea:** The probe learns the task itself even if the representation did not make it simple.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Can a hidden layer already separate animal species?

## Your First Attempt

Train a powerful classifier on hidden states and call any success evidence.

## Break Your First Attempt

The probe learns the task itself even if the representation did not make it simple.

## Repair Your Attempt

Use a deliberately limited probe and compare layers, controls, and baselines.

## What You Have Just Invented

**Use a deliberately limited probe and compare layers, controls, and baselines.**

## Rebuild the Discovery with a Concrete Case

A linear probe succeeds at layer 8 but random-label controls fail, suggesting species became linearly accessible there.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

Decodable information is not proof the model uses it.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 073](../073-attribution/README.md)
