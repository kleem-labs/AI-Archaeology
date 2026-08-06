# Excavation 112 — Causal Inference

[Previous: Excavation 111](../111-world-models/README.md)

## Take the First Step Yourself

> **Your problem:** Ice-cream sales and drownings rise together. Would banning ice cream reduce drownings?

> **Try your first idea:** Treat every correlation as a controllable cause.

> **Now try to break your idea:** Hot weather raises both; changing one does not necessarily change the other.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Ice-cream sales and drownings rise together. Would banning ice cream reduce drownings?

## Your First Attempt

Treat every correlation as a controllable cause.

## Break Your First Attempt

Hot weather raises both; changing one does not necessarily change the other.

## Repair Your Attempt

Represent plausible causal structure and distinguish observing a variable from intervening on it.

## What You Have Just Invented

**Represent plausible causal structure and distinguish observing a variable from intervening on it.**

## Rebuild the Discovery with a Concrete Case

Observing umbrellas predicts rain; forcing umbrellas open does not cause rain.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

Causal conclusions require assumptions not recoverable from correlations alone.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 113](../113-counterfactuals/README.md)
