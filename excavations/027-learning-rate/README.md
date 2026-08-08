# Excavation 027 — Learning Rate — How Large Should the Next Step Be?

[Previous: Excavation 026](../026-mini-batches/README.md)

The gradient points downhill, but it does not say how far to walk. A correct direction can still produce a disastrous step.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Always take a huge step: leap across the valley and oscillate. Always take a microscopic step: improve so slowly that the expedition ends first.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Always take a huge step: leap across the valley and oscillate. Always take a microscopic step: improve so slowly that the expedition ends first.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time.

Only after that reasoning may we give your discovery its inherited name.

## Why It Still Fails

The repair solves the immediate failure, but no single learning rate is best throughout training. Scale, curvature, batch noise, and parameter units all matter.

## Compress your discovery into mathematics


## Build each piece from what just happened

At weight 8 the gradient is 10. Rate 1 moves to -2 and overshoots; rate 0.1 moves to 7; rate 0.01 moves to 7.9. The rate controls travel distance, not downhill direction.

### Give Short Names Only After We Know the Pieces

- **g_t** is the downhill evidence measured at step t.
- **η_t** converts direction into a chosen travel distance and may change with time.
- The minus sign moves against increasing loss.
- **θ_t** and **θ_{t+1}** distinguish the old and updated parameter states.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
\theta_{t+1}=\theta_t-\eta_t g_t
$$

## Carry the idea back into the world

A mountain guide chooses shorter steps on steep or uncertain ground and can walk farther on a smooth open slope.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Test what you believe

Use the [invention challenges](exercises.md).

## What this discovery now makes possible

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 028](../028-momentum/README.md)
