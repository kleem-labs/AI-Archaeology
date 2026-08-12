# Excavation 024 — Backpropagation — Reusing Blame Instead of Recomputing It

The chain rule follows responsibility through one sequence of machines. A real network is a branching graph with shared intermediate results, so tracing every route independently repeats the same downstream work.

Perhaps we perturb each weight and rerun the model. This needs at least one extra forward pass per weight. Or trace paths independently and calculate the same suffix again and again.

Now we can see what is missing: we must compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream.

## From procedure to notation

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

## The arithmetic we have earned

One shared dough temperature affects two outcomes: crust and centre. The crust branch sends blame 3 through local sensitivity 2, contributing 6. The centre branch sends blame 4 through sensitivity 5, contributing 20. Because both outcomes depended on the same temperature, the baker must return total blame 26 to that shared decision. Computing either downstream suffix twice would add work without adding evidence.

### Only now do the symbols earn names

- **x̄** means accumulated sensitivity of final loss to intermediate x.
- A node can influence several child results y, so every downstream path must contribute.
- **ȳ** is blame already accumulated at child y.
- **∂y/∂x** says how strongly x affected that child locally.
- Multiplication passes blame through one edge; summation combines all outgoing paths.

Only now can we compress that reasoning:

$$
\bar{x}=\sum_{y\in children(x)}\bar{y}\frac{\partial y}{\partial x}
$$

## Carry the idea back into the world

A company traces one final loss through departments. Each department receives accumulated responsibility, then distributes it to the decisions that produced its output.

## Limits

Backpropagation returns a local sensitivity for each weight: which infinitesimal direction would raise the loss, and how strongly. That information contains no instruction saying whether to take the whole suggested movement, one tenth of it, or one thousandth; choosing that fraction is a separate optimization decision. Nor does a local slope reveal the entire loss landscape. A downward direction from the present point cannot prove that a deeper valley does not exist elsewhere, so backpropagation alone cannot guarantee the best minimum.

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
