# Excavation 030 — Activation Functions — Why a Network Must Bend

[Previous: Excavation 029](../029-initialization/README.md)

We stack many learned transformations, expecting deeper reasoning. If every layer is linear, the entire tower is equivalent to one matrix.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Add more linear layers. Depth increases, but expressive power does not. Use a hard yes-or-no threshold; it creates decisions but supplies almost no useful gradient.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Add more linear layers. Depth increases, but expressive power does not. Use a hard yes-or-no threshold; it creates decisions but supplies almost no useful gradient.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Place an activation after a linear transformation. ReLU opens positive paths; smoother gates such as GELU vary them gradually.

Only after that reasoning may we give your discovery its inherited name.

## Why It Still Fails

The repair solves the immediate failure, but every activation has tradeoffs: dead ReLUs, saturation, computational cost, or assumptions about input scale.

## Compress your discovery into mathematics


## Build each piece from what just happened

Without a gate, multiplying by 2 and then 3 always equals multiplying once by 6. With ReLU between them, input -1 becomes -2, then 0, then 0—behavior no single multiply-by-6 rule reproduces for both signs.

### Give Short Names Only After We Know the Pieces

- **x** is the incoming representation.
- **W** mixes its features; **b** permits learned thresholds and offsets.
- **φ** is the necessary nonlinear gate; without it, stacked layers collapse into one linear map.
- **h** is the hidden representation after both mixing and gating.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
h=\phi(Wx+b)
$$

## Carry the idea back into the world

A railway switch changes which route a signal can take. Without switches, many track segments still form only one fixed route.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Test what you believe

Use the [invention challenges](exercises.md).

## What this discovery now makes possible

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 031](../031-overfitting/README.md)
