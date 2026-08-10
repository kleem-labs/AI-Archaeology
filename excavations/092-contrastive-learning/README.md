# Excavation 092 — Contrastive Learning

[Previous: Excavation 091](../091-multimodal-alignment/README.md)

Paired examples should be close, but close relative to what?

Without knowing the inherited method, we might try this: Pull every observed pair together without negatives.

Its hidden assumption appears in the following case: All representations can collapse to one point.

Remove that assumption and the needed repair becomes clear: Compare each true pair against mismatched alternatives in the same batch.

## Now work a case you can see

One tiger image chooses its caption among 31 wrong captions; success requires relative alignment.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build each piece from what just happened


Place four wildlife photographs beside four captions. The tiger photograph should prefer “a striped predator” over “a river,” “a truck,” and “a sleeping dog.” Pulling only the correct pair together is insufficient: every photograph and caption could collapse to the same location. Making the tiger compete against all candidate captions forces its correct caption to be closer *relative to the alternatives*.

- zi and ti are the matched image and text vectors.
- Their dot product is the named alignment score.
- Temperature T controls how sharply alternatives compete.
- The denominator includes every candidate caption, preventing all examples from collapsing to one point.
- The negative log penalizes the true pair when mismatches receive comparable scores.

Only now can we compress the procedure:

$$
L_i=-\log\frac{\exp(z_i\cdot t_i/T)}{\sum_j\exp(z_i\cdot t_j/T)}
$$

## Where your new idea still breaks

False negatives may actually describe the same concept.

This is not an unrelated warning. The construction can compare each true pair against mismatched alternatives in the same batch. It cannot infer or control information that never enters that construction.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 093](../093-speech-audio/README.md)
