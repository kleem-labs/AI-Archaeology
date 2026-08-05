# Excavation 095 — Quantization

[Previous: Excavation 094](../094-lora/README.md)

## Take the First Step Yourself

> **Your problem:** How can a model use less memory and faster arithmetic at inference?

> **Try your first idea:** Round every weight aggressively without measuring effect.

> **Now try to break your idea:** Small but important distinctions disappear and outputs degrade.

> Stop here. State the missing requirement without naming the repair.

## The Observation

How can a model use less memory and faster arithmetic at inference?

## Your First Attempt

Round every weight aggressively without measuring effect.

## Break Your First Attempt

Small but important distinctions disappear and outputs degrade.

## Repair Your Attempt

Map values to a limited set of levels using calibrated scale and test sensitive layers.

## What You Have Just Invented

**Map values to a limited set of levels using calibrated scale and test sensitive layers.**

## Rebuild the Discovery with a Concrete Case

Weights from -1 to 1 become 256 integer levels; a stored integer plus scale approximately reconstructs each value.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build Every Piece from the Concrete Example

- Real weight w is divided by scale s to express it in integer-sized steps.
- Rounding chooses the nearest allowed integer q.
- Multiplying q by s reconstructs the approximate weight used in computation.
- The scale is calibrated so important values fit the available integer range.

Only now can we compress the procedure:

$$
q=\operatorname{round}(w/s),\qquad \widehat w=sq
$$

## Real-World Limit

Lower precision trades accuracy for efficiency and hardware support varies.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 096](../096-distributed-training/README.md)
