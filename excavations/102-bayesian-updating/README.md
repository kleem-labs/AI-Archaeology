# Excavation 102 — Bayesian Updating

[Previous: Excavation 101](../101-two-kinds-uncertainty/README.md)

## Take the First Step Yourself

> **Your problem:** A tracker begins with prior beliefs about tiger, deer, and wind, then observes a deep paw print.

> **Try your first idea:** Discard the old belief and use only the newest clue.

> **Now try to break your idea:** One noisy footprint can overpower years of evidence.

> Stop here. State the missing requirement without naming the repair.

## The Observation

A tracker begins with prior beliefs about tiger, deer, and wind, then observes a deep paw print.

## Your First Attempt

Discard the old belief and use only the newest clue.

## Break Your First Attempt

One noisy footprint can overpower years of evidence.

## Repair Your Attempt

Combine prior plausibility with how expected the clue is under each story, then normalize across stories.

## What You Have Just Invented

**Combine prior plausibility with how expected the clue is under each story, then normalize across stories.**

## Rebuild the Discovery with a Concrete Case

Tiger starts at 10%, but a deep paw print is far more likely under tiger than wind; the belief rises without becoming certainty.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Build Every Piece from the Concrete Example

- Tiger’s prior belief is its share before the footprint.
- The footprint likelihood says how expected this exact clue is if tiger is true.
- Multiplying gives tiger’s unnormalized support.
- The denominator repeats that multiplication for every story and adds them so final beliefs total one.

Only now can we compress the procedure:

$$
P(H\mid E)=\frac{P(E\mid H)P(H)}{\sum_j P(E\mid H_j)P(H_j)}
$$

## Real-World Limit

Results depend on priors and likelihood assumptions.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 103](../103-ensembles/README.md)
