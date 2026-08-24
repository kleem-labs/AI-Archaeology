# Excavation 024 — Backpropagation — Reusing Blame Instead of Recomputing It

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Calculus & Differential Change](../../MATHEMATICS_ATLAS.md#calculus) · [Graphs & Relational Structures](../../MATHEMATICS_ATLAS.md#graphs) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Learning from uncertainty and error

The chain rule follows responsibility through one sequence of machines. A real network is a branching graph with shared intermediate results, so tracing every route independently repeats the same downstream work.

At the Lantern Observatory, the keeper of uncertain stories returns to the ring of glass lanterns. Yesterday's instrument still lies open, so the first move asks for no new magic: perturb each weight and rerun the model.

For a moment the mark looks complete. Then the evidence refuses to fit: this needs at least one extra forward pass per weight. Or trace paths independently and calculate the same suffix again and again. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The keeper of uncertain stories sketches the break before changing it:*

```text
OLD PATH:  request ──▶ perturb each weight and rerun the… ──▶ this needs at least one extra forward…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ compute the prediction once, remember… ──▶ accountable result
```

The keeper of uncertain stories lays two translucent sheets over the ring of glass lanterns. The first is inscribed, “perturb each weight and rerun the model.” Its path ends where this needs at least one extra forward pass per weight. Or trace paths independently and calculate the same suffix again and again. The second receives the same evidence but is allowed to compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream. Held to the light, the sheets separate at exactly one decision.

No one reaches for a backpropagation formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The keeper of uncertain stories changes only that one responsibility: compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream. When the ink dries, the name **Backpropagation** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The ring of glass lanterns keeps both histories. Its older mark still says, ‘perturb each weight and rerun the model’; beside it, the newer mark says, ‘compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream.’ The distance between those sentences is the exact shape of backpropagation: no larger than the failure required, and no smaller than reality permits.

<!-- memory-film-v1:start -->
> **Memory realm 3 of 18 — [Lantern Observatory](../../MEMORY_PALACE.md#realm-3)**
>
> **The question carried into this chamber:** What fails if we perturb each weight and rerun the model?

## When the chamber changes

The mathematical name Backpropagation can now rest. What matters is whether its transformation remains visible.

First hold the failed picture still: The bell follows the tempting path—perturb each weight and rerun the model. Then the evidence answers: this needs at least one extra forward pass per weight. Or trace paths independently and calculate the same suffix again and again.

Now let the chamber move: The keeper of uncertain stories changes one moving part. The bell can now compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream.

The object that should remain after the terminology disappears is **the backpropagation bell mounted on the ring of glass lanterns**.

> **Memory seal — Backpropagation**
>
> Backpropagation keeps the missing power: compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream.

Give the idea a bodily path: Touch the backpropagation bell in imagination: trace its outline with one finger, cover it with your palm, then uncover only the repaired path.
<!-- memory-film-v1:end -->

## The calculation hidden inside backpropagation

The keeper of uncertain stories carries the backpropagation scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

One shared dough temperature affects two outcomes: crust and centre. The crust branch sends blame 3 through local sensitivity 2, contributing 6. The centre branch sends blame 4 through sensitivity 5, contributing 20. Because both outcomes depended on the same temperature, the baker must return total blame 26 to that shared decision. Computing either downstream suffix twice would add work without adding evidence.

### Naming what is already on the table

**x̄** means accumulated sensitivity of final loss to intermediate x.
A node can influence several child results y, so every downstream path must contribute.
**ȳ** is blame already accumulated at child y.
**∂y/∂x** says how strongly x affected that child locally.
Multiplication passes blame through one edge; summation combines all outgoing paths.

### Why the melody needs these exact notes

[The partial derivative](../../MATHEMATICAL_MOVES.md#partial-derivative) measures one local edge while other inputs are held fixed.
[Multiplying child blame by edge sensitivity](../../MATHEMATICAL_MOVES.md#multiplication) passes downstream responsibility through that edge; either factor being zero should block that path.
[Summing over children](../../MATHEMATICAL_MOVES.md#summation) reunites separate downstream routes that all depended on x. Multiplication would incorrectly make one zero-blame route erase every other route.

Listen beneath backpropagation: **the whispered question**—one decision is asked what would change if only it moved; **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Every mark needed for backpropagation is now visible on the ring of glass lanterns. The symbols do not add an idea; they bind the discovered moves into one line:

$$
\bar{x}=\sum_{y\in children(x)}\bar{y}\frac{\partial y}{\partial x}
$$

## Backpropagation beyond this one case

A company traces one final loss through departments. Each department receives accumulated responsibility, then distributes it to the decisions that produced its output.

## Where backpropagation runs out

Backpropagation returns a local sensitivity for each weight: which infinitesimal direction would raise the loss, and how strongly. That information contains no instruction saying whether to take the whole suggested movement, one tenth of it, or one thousandth; choosing that fraction is a separate optimization decision. Nor does a local slope reveal the entire loss landscape. A downward direction from the present point cannot prove that a deeper valley does not exist elsewhere, so backpropagation alone cannot guarantee the best minimum.

At the Lantern Observatory, the keeper of uncertain stories leaves a blank beneath the new mark. Backpropagation has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the ring of glass lanterns

Rebuild the backpropagation scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
