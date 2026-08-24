# Excavation 035 — A Tiny Neural Network — Assemble the Entire Learning Loop

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Learning from uncertainty and error

Generalization is the property we actually wanted: useful structure that survives new cases. We have derived its pieces separately; now they must become one visible machine whose prediction, loss, blame, and update form a complete loop.

Night gathers around the Lantern Observatory. Under the light of the ring of glass lanterns, the keeper of uncertain stories refuses to invent prematurely and begins with the plain rule: hide everything behind a framework call.

At the edge of the ring of glass lanterns, the shortcut produces its consequence: the code runs, but the causal chain disappears. Hand-tune outputs without gradients; every new example breaks the tuning. That consequence, not a textbook, earns the next move.

*The keeper of uncertain stories sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   hide everything behind a framework… the code runs, but the causal chain…
            \        /
             \      /
              we need to build a two-layer network,…
```

The keeper of uncertain stories covers the new mark and the old contradiction returns: the code runs, but the causal chain disappears. Hand-tune outputs without gradients; every new example breaks the tuning. The cover is lifted, restoring the ability to build a two-layer network, cache its intermediate values, backpropagate every derivative, update on batches, and evaluate on unseen data, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason tiny neural network exists.

What must change for tiny neural network is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: we need to build a two-layer network, cache its intermediate values, backpropagate every derivative, update on batches, and evaluate on unseen data. That threshold is where **A Tiny Neural Network** enters the story.

The marks on the ring of glass lanterns form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. tiny neural network is not any single point. It is the path connecting them in the only order that makes the last point necessary.

## The calculation hidden inside a tiny neural network

The keeper of uncertain stories carries the tiny neural network scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but a tiny network exposes mechanics but is not yet a language model. The next arc must turn sequences into a trained generative system.

Input 2 is mixed into a hidden signal, gated, and produces prediction 0.7. If the target is 1, loss sends correction backward through the same steps, changes weights, and the next forward pass may produce 0.8. The arrows are one loop.

### Naming what is already on the table

**x** is observed input.
**Wx+b** mixes features and supplies offsets.
**φ** bends the mapping so depth adds new behavior.
**ŷ** is the prediction and **L** measures its failure.
**∇_θL** assigns local correction directions to all parameters θ.
**θ′** is the updated state; the arrows show the forward path continuing into feedback rather than separate facts.

### Why the melody needs these exact notes

[Arrows](../../MATHEMATICAL_MOVES.md#arrows) preserve process order: data is transformed, activated, predicted, priced, blamed, and only then used to update parameters. Equality would wrongly claim those stages are the same object.
[The gradient stage](../../MATHEMATICAL_MOVES.md#gradient) changes a single loss into parameter-by-parameter advice; the final primed θ names the resulting new state.

The ring of glass lanterns already contains the complete tiny neural network mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
x\to Wx+b\to\phi(\cdot)\to\hat y\to L\to\nabla_\theta L\to\theta^\prime
$$

## A Tiny Neural Network beyond this one case

An engine is understood when fuel, ignition, motion, exhaust, and feedback operate together—not when its parts lie labeled on a table.

## The circle that teaches itself

Uncertainty became information; information became loss; loss became local sensitivity; sensitivities flowed backward; and a chosen step changed the machine. The circle is closed only because every arrow can be walked in ordinary language.

```text
prediction → surprise → loss → blame → update → new prediction
```

The trail called *the circle that teaches itself* is what remains when one necessity becomes another.

## Return to the ring of glass lanterns

Rebuild the tiny neural network scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Tokenization](../036-tokenization/README.md)
