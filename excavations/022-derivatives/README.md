# Excavation 022 — Derivatives — Asking One Weight What It Changed

Cross-entropy turns the model's misplaced confidence into one loss. One number can announce that the whole machine is wrong, but it cannot yet tell any particular weight whether moving up or down would help.

Using what we have, we try a large jump and keep it if loss falls. Large jumps can leap over improvements. Try every possible value; there are infinitely many.

So we nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero.

## From procedure to notation

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

## The arithmetic we have earned

A village adjusts one alarm dial controlling how much smoke is needed before ringing a bell. At setting 3 the false-alarm cost is 9. Raising the dial by only 0.001 changes the cost to about 9.006001. The extra cost divided by the tiny dial movement is about 6. Repeating with ever smaller movements reveals the local sensitivity at the current setting rather than the effect of one arbitrary jump.

### Only now do the symbols earn names

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
