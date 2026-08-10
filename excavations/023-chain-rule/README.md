# Excavation 023 — The Chain Rule — Following One Change Through Many Machines

[Previous excavation](../022-derivatives/README.md)

A weight changes a hidden signal, which changes a score, which changes a probability, which changes the loss. The weight never touches the loss directly.

At first, the simplest answer is tempting: Measure only the first effect or only the final effect. Either breaks the causal path. Recompute the whole network separately for every weight; that repeats enormous amounts of work.

The missing information determines the next move: Multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward.

## From procedure to notation

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

## Build each piece from what just happened

A weight change is doubled by the first machine, tripled by the second, and quadrupled by the loss. One unit at the start becomes 2, then 6, then 24. Multiplying 2×3×4 captures the complete path.

### Give Short Names Only After We Know the Pieces

- **w→x→y→L** is the causal path through successive machines.
- Each fraction is one local sensitivity: how its output changes when its input changes.
- Multiplication is forced because a change is scaled at every link it traverses.
- The product gives the effect of w on L without pretending they touch directly.

Only now can we compress that reasoning:

$$
\frac{dL}{dw}=\frac{dL}{dy}\frac{dy}{dx}\frac{dx}{dw}
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

## Carry the idea back into the world

A line of gears passes motion onward. To know the final turn from the first gear, combine the ratio contributed by every contact.

## Limits

Branches require sensitivities from every downstream path to be added, not merely one chain followed.

The reason is visible in the procedure. It knows how to multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward. The limitation above asks for another judgment, and no part of the procedure makes that judgment.

## Enter the laboratory

Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md).

## Test what you believe

Use the [invention exercises](exercises.md), not as a quiz but as a request to rediscover the idea.

## What this discovery now makes possible

- [Mistakes and failed ideas](mistakes.md)
- [Mermaid and ASCII diagram](diagram.md)
- [References](references.md)
- [Visual asset brief](images/README.md)

The limitation in this excavation creates the need for the next one.
