# Excavation 035 — A Tiny Neural Network — Assemble the Entire Learning Loop

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Learning from uncertainty and error

Generalization is the property we actually wanted: useful structure that survives new cases. We have derived its pieces separately; now they must become one visible machine whose prediction, loss, blame, and update form a complete loop.

Inside the Lantern Observatory, the old method is given an honest chance. The keeper of uncertain stories places the evidence on the ring of glass lanterns and tries to hide everything behind a framework call.

Nothing about this first move is careless. To hide everything behind a framework call is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: the code runs, but the causal chain disappears. Hand-tune outputs without gradients; every new example breaks the tuning.

The important discovery is not merely that trying to hide everything behind a framework call failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the ring of glass lanterns, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to build a two-layer network, cache its intermediate values, backpropagate every derivative, update on batches, and evaluate on unseen data. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **A Tiny Neural Network**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

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
