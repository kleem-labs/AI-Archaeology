# Excavation 033 — Validation — Testing Without Peeking at the Final Exam

Regularization changes which fitted explanation the learner prefers. Choosing its strength by repeatedly checking the final exam would quietly turn that exam into more training data.

At first we use training loss for every choice; it rewards memorization. Check the test set repeatedly; every decision leaks test information back into development.

That failure tells us to split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end.

## From procedure to notation

The repair solves the immediate failure, but random splits fail when future, users, families, or duplicated records leak across boundaries. The split must match the real deployment question.

## The arithmetic we have earned

With 100 examples, use 60 to change weights, 20 to choose learning rate, and keep 20 sealed. If the sealed 20 guide choices, they stop being an honest final test.

### Only now do the symbols earn names

- **D** is all available data.
- The three named subsets exist because weight learning, design choices, and final measurement must not share feedback.
- Union means they reconstruct the available collection.
- The intended split also requires no example to leak between sets, even though the compact union symbol alone does not state disjointness.

Only now can we compress that reasoning:

$$
D=D_{\text{train}}\cup D_{\text{validation}}\cup D_{\text{test}}
$$

## Carry the idea back into the world

A practice exam guides study. A sealed final exam measures what survived without feedback.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Test what you believe

Use the [invention challenges](exercises.md).

## What this discovery now makes possible

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 034](../034-generalization/README.md)
