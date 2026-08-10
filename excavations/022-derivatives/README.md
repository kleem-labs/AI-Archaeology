# Excavation 022 — Derivatives — Asking One Weight What It Changed

[Previous excavation](../021-cross-entropy/README.md)

The loss is high. The model has thousands of adjustable numbers. For one weight, should we increase it or decrease it?

Without knowing the inherited method, we might try this: Try a large jump and keep it if loss falls. Large jumps can leap over improvements. Try every possible value; there are infinitely many.

Its hidden assumption appears in the following case: A derivative is local advice. Curved landscapes can change direction, flatten, or hide better valleys elsewhere.

Remove that assumption and the needed repair becomes clear: Nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## Compress your discovery into mathematics


## Build each piece from what just happened

Use L(w)=w² at w=3. Nudge to 3.001: loss changes from 9 to about 9.006001. Dividing the loss change by 0.001 gives about 6; smaller nudges approach the local sensitivity 6.

### Give Short Names Only After We Know the Pieces

- **w** is the one weight whose responsibility we are probing.
- **ε** is a small experimental nudge.
- **L(w+ε)−L(w)** measures the loss change caused by that nudge.
- Dividing by ε turns total change into change per unit of weight.
- The limit shrinks the nudge so the answer becomes local rather than dependent on an arbitrary test step.
- **dL/dw** names that local sensitivity.

Only now can we compress that reasoning:

$$
\frac{dL}{dw}=\lim_{\epsilon\to0}\frac{L(w+\epsilon)-L(w)}{\epsilon}
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

## Carry the idea back into the world

A derivative is a local slope on a mountain trail: it says which direction rises and how sharply, only near the current step.

## Limits

A derivative is local advice. Curved landscapes can change direction, flatten, or hide better valleys elsewhere.

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
