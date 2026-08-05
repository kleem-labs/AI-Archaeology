# Excavation 033 — Validation — Testing Without Peeking at the Final Exam

[Previous: Excavation 032](../032-regularization/README.md)

## Problem

We need to choose model size, learning rate, and stopping time. Choosing them using the final test set quietly trains us on the test.

## Naive Attempt

Use training loss for every choice; it rewards memorization. Check the test set repeatedly; every decision leaks test information back into development.

## Why It Fails

One unseen set must guide choices, while another remains untouched for the final estimate.

## Better Attempt

Split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end.

## Why It Still Fails

The repair solves the immediate failure, but random splits fail when future, users, families, or duplicated records leak across boundaries. The split must match the real deployment question.

## Key Insight

**Split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end.**

## Mathematics Emerges

$$
D=D_{\text{train}}\cup D_{\text{validation}}\cup D_{\text{test}}
$$

Every operation records a need established above; the equation is the fossil, not the living discovery.

## Real-World Analogy

A practice exam guides study. A sealed final exam measures what survived without feedback.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Exercises

Use the [invention challenges](exercises.md).

## Connections

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 034](../034-generalization/README.md)
