# Excavation 083 — Autoregressive Generation Beyond Text

[Previous: Excavation 082](../082-latent-space/README.md)

How can a model generate an image one piece at a time?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Predict all pixels independently.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Independent pixels produce noise because neighboring colors and shapes constrain one another.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Choose an order and predict each piece from previously generated pieces.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

After generating sky pixels, the model gives blue neighbors higher probability.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

Sequential generation can be slow and ordering introduces bias.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 084](../084-diffusion/README.md)
