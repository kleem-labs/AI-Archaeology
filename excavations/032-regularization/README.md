# Excavation 032 — Regularization — Making Memorization More Expensive

[Previous: Excavation 031](../031-overfitting/README.md)


## Take the First Step Yourself

> **Your problem:** The model can reduce training loss by building fragile rules around tiny accidental details.

> **Try your first idea:** Forbid complexity by making the model too small; it may lose real structure too. Stop training at an arbitrary time without observing unseen performance.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

## Problem

The model can reduce training loss by building fragile rules around tiny accidental details.

## Your First Attempt

Forbid complexity by making the model too small; it may lose real structure too. Stop training at an arbitrary time without observing unseen performance.

## Break Your First Attempt

Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Forbid complexity by making the model too small; it may lose real structure too. Stop training at an arbitrary time without observing unseen performance.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

## Repair Your Attempt

Add a cost for large weights, remove random paths during training, or stop when validation performance stops improving.

## Why It Still Fails

The repair solves the immediate failure, but regularization expresses a preference, not a universal truth. Too much causes underfitting and different tasks need different biases.

## What You Have Just Invented

**Add a cost for large weights, remove random paths during training, or stop when validation performance stops improving.**

## Only Now Give the Discovery a Mathematical Name

## Build Every Piece from the Concrete Example

Two models have data loss 2. Model A has squared-weight sum 100; B has 4. With lambda 0.1, totals are 12 and 2.4. The penalty makes the equally fitting but less extreme model preferable.

### Give Short Names Only After We Know the Pieces

- **L_data** rewards fitting observations.
- **θ** contains the weights; squaring and summing them creates ||θ||² without signed cancellation.
- **λ** expresses how strongly we prefer smaller machinery relative to data fit.
- Addition forces training to negotiate prediction accuracy and complexity in one objective.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
L_{\text{total}}=L_{\text{data}}+\lambda\lVert\theta\rVert^2
$$


## Real-World Analogy

A map that explains every pebble with a separate rule is less trustworthy than one road system that explains many journeys.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Exercises

Use the [invention challenges](exercises.md).

## Connections

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 033](../033-validation/README.md)
