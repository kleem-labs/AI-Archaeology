# Excavation 080 — Vision Transformers

[Previous: Excavation 079](../079-cnn-hierarchy/README.md)

Convolutions bake in locality, but distant image regions may need direct comparison.

The first solution that suggests itself is this: Treat every pixel as a token.

The idea survives only until we test it against reality: The sequence becomes enormous and individual pixels carry little stable structure.

The failure gives us a precise requirement: Group pixels into patches, embed them as tokens, add position, and apply attention.

## Now work a case you can see

A 224×224 image with 16×16 patches becomes 196 tokens instead of 50,176 pixel tokens.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

Patch size trades detail for cost and needs substantial data.

The boundary follows from the mechanism itself. We designed it to Group pixels into patches, embed them as tokens, add position, and apply attention. That operation solves the failure we had reached, but it contains no step that answers the additional problem above.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 081](../081-autoencoders/README.md)
