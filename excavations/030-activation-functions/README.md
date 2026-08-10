# Excavation 030 — Activation Functions — Why a Network Must Bend

[Previous: Excavation 029](../029-initialization/README.md)

We stack many learned transformations, expecting deeper reasoning. If every layer is linear, the entire tower is equivalent to one matrix.

The first solution that suggests itself is this: Add more linear layers. Depth increases, but expressive power does not. Use a hard yes-or-no threshold; it creates decisions but supplies almost no useful gradient.

The failure gives us a precise requirement: Place an activation after a linear transformation. ReLU opens positive paths; smoother gates such as GELU vary them gradually.

## From procedure to notation

The repair solves the immediate failure, but every activation has tradeoffs: dead ReLUs, saturation, computational cost, or assumptions about input scale.



## Build each piece from what just happened

A gatekeeper receives a danger signal. Two ordinary scaling rules—double it, then triple it—always behave like one rule that multiplies by six. Adding more such rules has created no new decision. Put a gate between them: negative evidence is closed to zero while positive evidence continues. Now the same machinery treats warning evidence and reassuring evidence differently, something one multiplication cannot reproduce.

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
