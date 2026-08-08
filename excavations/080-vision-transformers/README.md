# Excavation 080 — Vision Transformers

[Previous: Excavation 079](../079-cnn-hierarchy/README.md)

Convolutions bake in locality, but distant image regions may need direct comparison.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Treat every pixel as a token.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* The sequence becomes enormous and individual pixels carry little stable structure.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Group pixels into patches, embed them as tokens, add position, and apply attention.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

A 224×224 image with 16×16 patches becomes 196 tokens instead of 50,176 pixel tokens.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

Patch size trades detail for cost and needs substantial data.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 081](../081-autoencoders/README.md)
