# Excavation 082 — Latent Space — Coordinates for Hidden Causes

[Previous: Excavation 081](../081-autoencoders/README.md)

The bottleneck contains numbers, but do nearby codes vary meaningfully?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Assume any compressed coordinates form a smooth useful space.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Tiny code changes can cause abrupt unrelated outputs.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Shape the latent distribution and train nearby codes to decode coherently.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

Moving one latent coordinate gradually changes image brightness while another changes pose.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

Latent directions need not be independent or human-readable.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 083](../083-autoregressive-generation/README.md)
