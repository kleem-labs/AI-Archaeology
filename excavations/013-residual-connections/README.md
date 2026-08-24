# Excavation 013 — Residual Connections

Imagine rewriting an important message fifty times. If every editor replaces the entire document, one poor edit can erase something later editors need.

A deep network faces the same danger. Attention and feed-forward blocks transform a representation repeatedly. Requiring each block to reproduce everything worth keeping while also improving it is an unnecessarily hard job.

## Failed attempt: trust replacement

Let each layer output a completely new representation. To do nothing useful, the layer must learn a perfect copy operation. Errors compound, and the learning signal must pass through every transformation on its way backward.

## Let each layer propose a correction

Keep the original stream and ask the block only for a change:

```text
original representation ─────────────┐
        └→ transformation → proposal ├→ add → new representation
```

If the proposal is useful, add it. If no change is needed, a proposal near zero leaves the original intact.

This reconnects directly with Excavation 004: a vector can describe a state, and another vector can describe how that state should change.

Only now do we need the compact rule:

## The calculation hidden inside residual connections

A cartographer already has a useful map of the forest. A new survey reports that one trail bends half a kilometre east and one kilometre south. Replacing the whole map with that small report would destroy everything known; adding it as a correction preserves the map and changes only the trail. If the survey discovers nothing useful, adding a zero correction leaves the original untouched.

### Naming what is already on the table

- **x** is the representation worth preserving.
- **F(x)** is only the transformation's proposed correction, not a complete replacement.
- Addition keeps a direct route for x and makes “do nothing” possible when F(x)=0.
- **y** is the corrected state passed onward.

The block learns the **residual**—the difference between what exists and what should be added.

This direct route also gives learning signals a path that does not depend entirely on every learned transformation. Residual connections do not guarantee that a very deep model will train, but they make preservation and correction far easier.

Addition requires the input and proposal to have the same shape. That is why attention and feed-forward sublayers return to the model's shared width before joining the residual stream.

### Why the melody needs these exact notes

[Addition](../../MATHEMATICAL_MOVES.md#addition) preserves the old message **x** and treats the block as a proposed change **F(x)**. Replacing x would force every block to reconstruct all useful old information.
[F(x)](../../MATHEMATICAL_MOVES.md#function-application) says the proposed change depends on this exact incoming representation rather than being one fixed correction for every token.

Trace each operation by touch rather than by name: **the joining river**—separate contributions meet without losing where they came from. Together they form the smallest mechanism that survives the counterexample.

The keeper of words reads the journey of residual connections once more across the long cedar table, then lets the words contract without losing their order:

$$
\mathbf{y}=\mathbf{x}+F(\mathbf{x})
$$

<!-- memory-film-v1:start -->
> **Memory realm 2 of 18 — [Scriptorium of Echoes](../../MEMORY_PALACE.md#realm-2)**
>
> **The question carried into this chamber:** How can a deep stack learn a change without erasing the useful state it already has?

## When the chamber changes

Before leaving Residual Connections, replay the discovery as motion rather than as a definition.

First hold the failed picture still: Every new layer replaces the whole state, so a poor transformation can destroy information and gradients struggle to return.

Now let the chamber move: The old road remains open while the new branch contributes only its proposed change.

The object that should remain after the terminology disappears is **a stone bridge with an old road running beneath a newly built arch**.

> **Memory seal — Residual Connections**
>
> A residual connection preserves the old state while allowing a layer to add a correction.

Give the idea a bodily path: Hold one hand steady while the other makes a small motion and joins it.
<!-- memory-film-v1:end -->

## Challenge

If the best transformation for one layer is “leave this representation alone,” compare what a replacement block must learn with what a residual block must output.

## What the next excavation needs

Repeated transformations and additions can make some representations numerically huge and others tiny. The next block needs a more stable working scale.

[Next: Layer Normalization](../014-layer-normalization/README.md)

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Foundations and representation
