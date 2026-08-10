# Excavation 023 — The Chain Rule — Following One Change Through Many Machines

[Previous excavation](../022-derivatives/README.md)

A weight changes a hidden signal, which changes a score, which changes a probability, which changes the loss. The weight never touches the loss directly.

At first, the simplest answer is tempting: Measure only the first effect or only the final effect. Either breaks the causal path. Recompute the whole network separately for every weight; that repeats enormous amounts of work.

But the simplicity has discarded something important: Branches require sensitivities from every downstream path to be added, not merely one chain followed.

The missing information determines the next move: Multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## Compress your discovery into mathematics


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
