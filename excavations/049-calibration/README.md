# Excavation 049 — Calibration — Does 80% Confidence Mean Eight Out of Ten?

[Previous: Excavation 048](../048-hallucination/README.md)

## Take the First Step Yourself

> **Your problem:** A model labels many answers “80% confident.” Can a user interpret that number?

> **Try your first idea:** Treat the largest softmax probability as honest confidence.

> **Now try to break your idea:** Collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability.

> Stop here. State what the repair must accomplish in ordinary language. Do not name a standard technique.

## The Observation

A model labels many answers “80% confident.” Can a user interpret that number?

## Your First Attempt

Treat the largest softmax probability as honest confidence.

## Break Your First Attempt

Collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability.

What information did the attempt lose? Write that requirement before continuing.

## Repair Your Attempt

Group predictions with similar confidence and compare their average stated confidence with the fraction actually correct.

## What You Have Just Invented

**Group predictions with similar confidence and compare their average stated confidence with the fraction actually correct.**

## Build Every Piece from the Concrete Example

Five predictions report 0.8 confidence. Exactly four are correct. Accuracy is 4/5=0.8, so this group is calibrated. If only two are correct, accuracy is 0.4 and the confidence gap is 0.4.

### Give Short Names Only After We Know the Pieces

Each group contains predictions with similar confidence. Accuracy counts how many were correct. The absolute difference measures the reliability gap; weighting by group size prevents tiny groups dominating.

Only now can we compress the exact procedure:

$$
\operatorname{ECE}=\sum_b\frac{|B_b|}{n}\left|\operatorname{accuracy}(B_b)-\operatorname{confidence}(B_b)\right|
$$

## Real-World Limit

Calibration depends on task and population. A model calibrated overall can be unreliable for an important subgroup.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 050](../050-data-quality/README.md)
