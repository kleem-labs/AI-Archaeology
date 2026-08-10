# Excavation 112 — Causal Inference

[Previous: Excavation 111](../111-world-models/README.md)

Ice-cream sales and drownings rise together. Would banning ice cream reduce drownings?

Without knowing the inherited method, we might try this: Treat every correlation as a controllable cause.

Its hidden assumption appears in the following case: Hot weather raises both; changing one does not necessarily change the other.

Remove that assumption and the needed repair becomes clear: Represent plausible causal structure and distinguish observing a variable from intervening on it.

## Now work a case you can see

Observing umbrellas predicts rain; forcing umbrellas open does not cause rain.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Causal conclusions require assumptions not recoverable from correlations alone.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 113](../113-counterfactuals/README.md)
