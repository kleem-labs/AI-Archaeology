# Excavation 013 — Residual Connections

[Previous: Feed-Forward Networks](../012-feed-forward-networks/README.md)


## Take the First Step Yourself

> **Your problem:** How can fifty layers improve a message without repeatedly erasing it?

> **Try your first idea:** Ask a replacement layer to do nothing. What perfect copying must it learn?

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

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

## Build Every Piece from the Concrete Example

A layer receives [5,2]. If it discovers only a correction [0.5,-1], addition gives [5.5,1]. If no correction is needed, [0,0] preserves [5,2] exactly instead of relearning how to copy it.

### Give Short Names Only After We Know the Pieces

- **x** is the representation worth preserving.
- **F(x)** is only the transformation's proposed correction, not a complete replacement.
- Addition keeps a direct route for x and makes “do nothing” possible when F(x)=0.
- **y** is the corrected state passed onward.


The block learns the **residual**—the difference between what exists and what should be added.

This direct route also gives learning signals a path that does not depend entirely on every learned transformation. Residual connections do not guarantee that a very deep model will train, but they make preservation and correction far easier.

Addition requires the input and proposal to have the same shape. That is why attention and feed-forward sublayers return to the model's shared width before joining the residual stream.

Only now can we compress that reasoning:

$$
\mathbf{y}=\mathbf{x}+F(\mathbf{x})
$$


## Challenge

If the best transformation for one layer is “leave this representation alone,” compare what a replacement block must learn with what a residual block must output.

## What the next excavation needs

Repeated transformations and additions can make some representations numerically huge and others tiny. The next block needs a more stable working scale.

[Next: Layer Normalization](../014-layer-normalization/README.md)
