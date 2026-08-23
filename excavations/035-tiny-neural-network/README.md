# Excavation 035 — A Tiny Neural Network — Assemble the Entire Learning Loop

<!-- book-prose-v2 -->

Generalization is the property we actually wanted: useful structure that survives new cases. We have derived its pieces separately; now they must become one visible machine whose prediction, loss, blame, and update form a complete loop.

The previous discovery seems almost sufficient: we could hide everything behind a framework call.

The shortcut appears to retain everything a tiny neural network needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

Then a case arrives in which convenience and truth separate: the code runs, but the causal chain disappears. Hand-tune outputs without gradients; every new example breaks the tuning.

The counterexample teaches a tiny neural network. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: we need to build a two-layer network, cache its intermediate values, backpropagate every derivative, update on batches, and evaluate on unseen data.

Now—and not earlier—we may introduce **A Tiny Neural Network**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to hide everything behind a framework call., and the case answers that the code runs, but the causal chain disappears. Hand-tune outputs without gradients; every new example breaks the tuning. With the narrow repair—to we need to build a two-layer network, cache its intermediate values, backpropagate every derivative, update on batches, and evaluate on unseen data—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. A Tiny Neural Network returns to the same counterexample, replaces the attempt to hide everything behind a framework call. with the responsibility to we need to build a two-layer network, cache its intermediate values, backpropagate every derivative, update on batches, and evaluate on unseen data, and must succeed where the shortcut failed.

## The calculation hidden inside a tiny neural network

Before A Tiny Neural Network receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

The repair solves the immediate failure, but a tiny network exposes mechanics but is not yet a language model. The next arc must turn sequences into a trained generative system.

Input 2 is mixed into a hidden signal, gated, and produces prediction 0.7. If the target is 1, loss sends correction backward through the same steps, changes weights, and the next forward pass may produce 0.8. The arrows are one loop.

### Names for pieces we have already used

**x** is observed input.
**Wx+b** mixes features and supplies offsets.
**φ** bends the mapping so depth adds new behavior.
**ŷ** is the prediction and **L** measures its failure.
**∇_θL** assigns local correction directions to all parameters θ.
**θ′** is the updated state; the arrows show the forward path continuing into feedback rather than separate facts.

### Why no cheaper operation does the same job

[Arrows](../../MATHEMATICAL_MOVES.md#arrows) preserve process order: data is transformed, activated, predicted, priced, blamed, and only then used to update parameters. Equality would wrongly claim those stages are the same object.
[The gradient stage](../../MATHEMATICAL_MOVES.md#gradient) changes a single loss into parameter-by-parameter advice; the final primed θ names the resulting new state.

The notation is finally shorter than the story that created it:

$$
x\to Wx+b\to\phi(\cdot)\to\hat y\to L\to\nabla_\theta L\to\theta^\prime
$$

## A Tiny Neural Network beyond this one case

An engine is understood when fuel, ignition, motion, exhaust, and feedback operate together—not when its parts lie labeled on a table.

## Take a tiny neural network to the workbench

Move a tiny neural network from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running a tiny neural network, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the a tiny neural network result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Tokenization](../036-tokenization/README.md)
