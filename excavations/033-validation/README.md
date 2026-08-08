# Excavation 033 — Validation — Testing Without Peeking at the Final Exam

[Previous: Excavation 032](../032-regularization/README.md)

We need to choose model size, learning rate, and stopping time. Choosing them using the final test set quietly trains us on the test.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Use training loss for every choice; it rewards memorization. Check the test set repeatedly; every decision leaks test information back into development.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Use training loss for every choice; it rewards memorization. Check the test set repeatedly; every decision leaks test information back into development.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end.

Only after that reasoning may we give your discovery its inherited name.

## Why It Still Fails

The repair solves the immediate failure, but random splits fail when future, users, families, or duplicated records leak across boundaries. The split must match the real deployment question.

## Compress your discovery into mathematics


## Build each piece from what just happened

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
