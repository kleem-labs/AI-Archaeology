# Excavation 035 — A Tiny Neural Network — Assemble the Entire Learning Loop

Generalization is the property we actually wanted: useful structure that survives new cases. We have derived its pieces separately; now they must become one visible machine whose prediction, loss, blame, and update form a complete loop.

An obvious shortcut is to hide everything behind a framework call. The code runs, but the causal chain disappears. Hand-tune outputs without gradients; every new example breaks the tuning.

We need to build a two-layer network, cache its intermediate values, backpropagate every derivative, update on batches, and evaluate on unseen data.

## From procedure to notation

The repair solves the immediate failure, but a tiny network exposes mechanics but is not yet a language model. The next arc must turn sequences into a trained generative system.

## The arithmetic we have earned

Input 2 is mixed into a hidden signal, gated, and produces prediction 0.7. If the target is 1, loss sends correction backward through the same steps, changes weights, and the next forward pass may produce 0.8. The arrows are one loop.

### Only now do the symbols earn names

- **x** is observed input.
- **Wx+b** mixes features and supplies offsets.
- **φ** bends the mapping so depth adds new behavior.
- **ŷ** is the prediction and **L** measures its failure.
- **∇_θL** assigns local correction directions to all parameters θ.
- **θ′** is the updated state; the arrows show the forward path continuing into feedback rather than separate facts.

Only now can we compress that reasoning:

$$
x\to Wx+b\to\phi(\cdot)\to\hat y\to L\to\nabla_\theta L\to\theta^\prime
$$

## Carry the idea back into the world

An engine is understood when fuel, ignition, motion, exhaust, and feedback operate together—not when its parts lie labeled on a table.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Test what you believe

Use the [invention challenges](exercises.md).

## What this discovery now makes possible

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Tokenization](../036-tokenization/README.md)
