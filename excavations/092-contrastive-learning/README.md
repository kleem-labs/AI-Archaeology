# Excavation 092 — Contrastive Learning

[Previous: Excavation 091](../091-multimodal-alignment/README.md)

## Take the First Step Yourself

> **Your problem:** Paired examples should be close, but close relative to what?

> **Try your first idea:** Pull every observed pair together without negatives.

> **Now try to break your idea:** All representations can collapse to one point.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Paired examples should be close, but close relative to what?

## Your First Attempt

Pull every observed pair together without negatives.

## Break Your First Attempt

All representations can collapse to one point.

## Repair Your Attempt

Compare each true pair against mismatched alternatives in the same batch.

## What You Have Just Invented

**Compare each true pair against mismatched alternatives in the same batch.**

## Rebuild the Discovery with a Concrete Case

One tiger image chooses its caption among 31 wrong captions; success requires relative alignment.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build Every Piece from the Concrete Example

- zi and ti are the matched image and text vectors.
- Their dot product is the named alignment score.
- Temperature T controls how sharply alternatives compete.
- The denominator includes every candidate caption, preventing all examples from collapsing to one point.
- The negative log penalizes the true pair when mismatches receive comparable scores.

Only now can we compress the procedure:

$$
L_i=-\log\frac{\exp(z_i\cdot t_i/T)}{\sum_j\exp(z_i\cdot t_j/T)}
$$

## Real-World Limit

False negatives may actually describe the same concept.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 093](../093-speech-audio/README.md)
