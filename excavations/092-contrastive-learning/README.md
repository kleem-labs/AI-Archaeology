# Excavation 092 — Contrastive Learning

Multimodal alignment places an image near its matching caption. Pulling pairs together alone permits every pair to collapse to the same point; meaning appears only when the correct match wins against plausible alternatives.

One tempting answer is to pull every observed pair together without negatives.

The trouble appears immediately: all representations can collapse to one point.

Now we can see what is missing: we must compare each true pair against mismatched alternatives in the same batch.

## Let the case decide

One tiger image chooses its caption among 31 wrong captions; success requires relative alignment.

## The arithmetic we have earned

Place four wildlife photographs beside four captions. The tiger photograph should prefer “a striped predator” over “a river,” “a truck,” and “a sleeping dog.” Pulling only the correct pair together is insufficient: every photograph and caption could collapse to the same location. Making the tiger compete against all candidate captions forces its correct caption to be closer *relative to the alternatives*.

- zi and ti are the matched image and text vectors.
- Their dot product is the named alignment score.
- Temperature T controls how sharply alternatives compete.
- The denominator includes every candidate caption, preventing all examples from collapsing to one point.
- The negative log penalizes the true pair when mismatches receive comparable scores.

### Why these operations are forced

- [Each dot product](../../MATHEMATICAL_MOVES.md#dot-product) measures aligned agreement between one image representation and one candidate text representation.
- [Dividing by temperature](../../MATHEMATICAL_MOVES.md#division) controls how strongly score gaps matter before [exponentiation](../../MATHEMATICAL_MOVES.md#exponential) converts them into positive relative weights.
- [The denominator sum](../../MATHEMATICAL_MOVES.md#summation) makes the correct pair compete against all candidates, preventing every representation from winning by collapsing to one point.
- [Negative log](../../MATHEMATICAL_MOVES.md#logarithm) turns the correct pair's probability share into additive cost and punishes confident preference for the wrong match.

Only now can we compress the procedure:

$$
L_i=-\log\frac{\exp(z_i\cdot t_i/T)}{\sum_j\exp(z_i\cdot t_j/T)}
$$

## The boundary of the discovery

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
