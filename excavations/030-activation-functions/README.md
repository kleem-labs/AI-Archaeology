# Excavation 030 — Activation Functions — Why a Network Must Bend

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Calculus & Differential Change](../../MATHEMATICS_ATLAS.md#calculus) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Learning from uncertainty and error

Careful initialization keeps early signals alive and breaks symmetry. But a tower made only from linear transformations still collapses algebraically into one linear transformation, no matter how many layers we stack.

The doors of the Lantern Observatory close against the wind. On the ring of glass lanterns, the keeper of uncertain stories writes the cheapest rule that might still be true: add more linear layers.

For a moment the mark looks complete. Then the evidence refuses to fit: depth increases, but expressive power does not. Use a hard yes-or-no threshold; it creates decisions but supplies almost no useful gradient. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The keeper of uncertain stories sketches the break before changing it:*

```text
OLD PATH:  request ──▶ add more linear layers ──▶ depth increases, but expressive power…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ place an activation after a linear… ──▶ accountable result
```

The keeper of uncertain stories lays two translucent sheets over the ring of glass lanterns. The first is inscribed, “add more linear layers.” Its path ends where depth increases, but expressive power does not. Use a hard yes-or-no threshold; it creates decisions but supplies almost no useful gradient. The second receives the same evidence but is allowed to place an activation after a linear transformation. ReLU opens positive paths; smoother gates such as GELU vary them gradually. Held to the light, the sheets separate at exactly one decision.

No one reaches for a activation functions formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The keeper of uncertain stories changes only that one responsibility: place an activation after a linear transformation. ReLU opens positive paths; smoother gates such as GELU vary them gradually. When the ink dries, the name **Activation Functions** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because depth increases, but expressive power does not. Use a hard yes-or-no threshold; it creates decisions but supplies almost no useful gradient, while the other can place an activation after a linear transformation. ReLU opens positive paths; smoother gates such as GELU vary them gradually. That fork—not the vocabulary—is where activation functions lives.

<!-- memory-film-v1:start -->
> **Memory realm 3 of 18 — [Lantern Observatory](../../MEMORY_PALACE.md#realm-3)**
>
> **The question carried into this chamber:** Why a Network Must Bend?

## When the chamber changes

The Activation Functions room does not ask you to memorize its name. It asks you to watch one object change.

First hold the failed picture still: The gear follows the tempting path—add more linear layers. Then the evidence answers: depth increases, but expressive power does not. Use a hard yes-or-no threshold; it creates decisions but supplies almost no useful gradient.

Now let the chamber move: The keeper of uncertain stories changes one moving part. The gear can now place an activation after a linear transformation. ReLU opens positive paths; smoother gates such as GELU vary them gradually.

The object that should remain after the terminology disappears is **the activation functions gear mounted on the ring of glass lanterns**.

> **Memory seal — Activation Functions**
>
> Activation Functions keeps the missing power: place an activation after a linear transformation. ReLU opens positive paths; smoother gates such as GELU vary them gradually.

Give the idea a bodily path: Touch the activation functions gear in imagination: make a narrow gate with both hands, block the old path, then open only the route the evidence permits.
<!-- memory-film-v1:end -->

## The calculation hidden inside activation functions

The keeper of uncertain stories carries the activation functions scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but every activation has tradeoffs: dead ReLUs, saturation, computational cost, or assumptions about input scale.

A gatekeeper receives a danger signal. Two ordinary scaling rules—double it, then triple it—always behave like one rule that multiplies by six. Adding more such rules has created no new decision. Put a gate between them: negative evidence is closed to zero while positive evidence continues. Now the same machinery treats warning evidence and reassuring evidence differently, something one multiplication cannot reproduce.

### Naming what is already on the table

**x** is the incoming representation.
**W** mixes its features; **b** permits learned thresholds and offsets.
**φ** is the necessary nonlinear gate; without it, stacked layers collapse into one linear map.
**h** is the hidden representation after both mixing and gating.

### Why the melody needs these exact notes

[Wx](../../MATHEMATICAL_MOVES.md#multiplication) lets every learned input weight scale and mix its matching feature; [adding b](../../MATHEMATICAL_MOVES.md#addition) supplies a learnable baseline.
[Applying φ](../../MATHEMATICAL_MOVES.md#function-application) bends the result. Without φ, repeated multiply-and-add stages remain one linear map, no matter how many layers are stacked.

The mandala has curved back upon itself. In this chamber we meet **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the joining river**—separate contributions meet without losing where they came from. What seemed like a new formula is older mathematical instinct arranged around a new need.

Every mark needed for activation functions is now visible on the ring of glass lanterns. The symbols do not add an idea; they bind the discovered moves into one line:

$$
h=\phi(Wx+b)
$$

## Activation Functions beyond this one case

A railway switch changes which route a signal can take. Without switches, many track segments still form only one fixed route.

## Return to the ring of glass lanterns

Rebuild the activation functions scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Excavation 031](../031-overfitting/README.md)
