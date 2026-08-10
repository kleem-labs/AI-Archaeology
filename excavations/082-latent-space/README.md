# Excavation 082 — Latent Space — Coordinates for Hidden Causes

[Previous: Excavation 081](../081-autoencoders/README.md)

The bottleneck contains numbers, but do nearby codes vary meaningfully?

Without knowing the inherited method, we might try this: Assume any compressed coordinates form a smooth useful space.

Its hidden assumption appears in the following case: Tiny code changes can cause abrupt unrelated outputs.

Remove that assumption and the needed repair becomes clear: Shape the latent distribution and train nearby codes to decode coherently.

## Now work a case you can see

Moving one latent coordinate gradually changes image brightness while another changes pose.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

Latent directions need not be independent or human-readable.

This is not an unrelated warning. The construction can shape the latent distribution and train nearby codes to decode coherently. It cannot infer or control information that never enters that construction.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 083](../083-autoregressive-generation/README.md)
