# Excavation 081 — Autoencoders — Compressing and Rebuilding

[Previous: Excavation 080](../080-vision-transformers/README.md)

Can a model preserve what matters using fewer numbers?

A reasonable place to begin is: Copy the input through an unrestricted hidden layer.

Now place that proposal under pressure: A wide hidden layer learns identity without compression.

What broke tells us what the replacement must preserve: Force information through a bottleneck and train reconstruction.

## Now work a case you can see

Four correlated measurements compress to two codes that still rebuild the originals approximately.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

Good reconstruction may preserve details irrelevant to downstream meaning.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 082](../082-latent-space/README.md)
