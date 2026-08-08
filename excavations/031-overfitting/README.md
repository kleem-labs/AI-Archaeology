# Excavation 031 — Overfitting — When Perfect Memory Pretends to Be Intelligence

[Previous: Excavation 030](../030-activation-functions/README.md)

A model scores perfectly on every training example, then fails on a new animal seen from a different angle.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Celebrate zero training error. The model may have memorized scratches and shadows. Make the model infinitely flexible; it can store even more irrelevant detail.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Celebrate zero training error. The model may have memorized scratches and shadows. Make the model infinitely flexible; it can store even more irrelevant detail.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Reserve unseen cases and compare training success with performance outside the training memory.

Only after that reasoning may we give your discovery its inherited name.

## Why It Still Fails

The repair solves the immediate failure, but a gap diagnoses overfitting but does not identify its cause. Leakage, distribution shift, and noisy evaluation can mislead us.

## Compress your discovery into mathematics


## Build each piece from what just happened

A model has training loss 0.02 and unseen loss 0.17. Subtracting gives a gap of 0.15. The low training number shows memory; the gap measures how much success disappeared outside it.

### Give Short Names Only After We Know the Pieces

- **L_train** measures error on examples allowed to shape the model.
- **L_unseen** measures error on held-out observations.
- Subtraction isolates deterioration outside memory instead of confusing it with absolute task difficulty.
- A positive generalization gap is evidence that training success did not fully survive.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
\text{generalization gap}=L_{\text{unseen}}-L_{\text{train}}
$$

## Carry the idea back into the world

A student who memorizes answer positions can ace the practice sheet and fail when the same ideas are rearranged.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Test what you believe

Use the [invention challenges](exercises.md).

## What this discovery now makes possible

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 032](../032-regularization/README.md)
