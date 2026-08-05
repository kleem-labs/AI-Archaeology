# Excavation 033 — Validation — Testing Without Peeking at the Final Exam

[Previous: Excavation 032](../032-regularization/README.md)


## Take the First Step Yourself

> **Your problem:** We need to choose model size, learning rate, and stopping time. Choosing them using the final test set quietly trains us on the test.

> **Try your first idea:** Use training loss for every choice; it rewards memorization. Check the test set repeatedly; every decision leaks test information back into development.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

## Problem

We need to choose model size, learning rate, and stopping time. Choosing them using the final test set quietly trains us on the test.

## Your First Attempt

Use training loss for every choice; it rewards memorization. Check the test set repeatedly; every decision leaks test information back into development.

## Break Your First Attempt

Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Use training loss for every choice; it rewards memorization. Check the test set repeatedly; every decision leaks test information back into development.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

## Repair Your Attempt

Split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end.

## Why It Still Fails

The repair solves the immediate failure, but random splits fail when future, users, families, or duplicated records leak across boundaries. The split must match the real deployment question.

## What You Have Just Invented

**Split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end.**

## Only Now Give the Discovery a Mathematical Name

## Build Every Piece from the Concrete Example

With 100 examples, use 60 to change weights, 20 to choose learning rate, and keep 20 sealed. If the sealed 20 guide choices, they stop being an honest final test.

### Give Short Names Only After We Know the Pieces

- **D** is all available data.
- The three named subsets exist because weight learning, design choices, and final measurement must not share feedback.
- Union means they reconstruct the available collection.
- The intended split also requires no example to leak between sets, even though the compact union symbol alone does not state disjointness.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
D=D_{\text{train}}\cup D_{\text{validation}}\cup D_{\text{test}}
$$


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
