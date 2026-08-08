# Excavation 092 — Contrastive Learning

[Previous: Excavation 091](../091-multimodal-alignment/README.md)

Paired examples should be close, but close relative to what?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Pull every observed pair together without negatives.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* All representations can collapse to one point.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Compare each true pair against mismatched alternatives in the same batch.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

One tiger image chooses its caption among 31 wrong captions; success requires relative alignment.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build each piece from what just happened

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

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 093](../093-speech-audio/README.md)
