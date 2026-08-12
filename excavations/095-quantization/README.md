# Excavation 095 — Quantization

Low-rank adaptation learns a small correction while preserving the base model. The unchanged base weights still consume memory and arithmetic every time the adapted model answers.

An obvious shortcut is to round every weight aggressively without measuring effect.

But small but important distinctions disappear and outputs degrade.

We need to map values to a limited set of levels using calibrated scale and test sensitive layers.

## Let the case decide

Weights from -1 to 1 become 256 integer levels; a stored integer plus scale approximately reconstructs each value.

## The arithmetic we have earned

Suppose one learned weight is `0.73`, but the device can store only integer steps of size `0.10`. Dividing by the step size says the weight is 7.3 steps; rounding stores integer 7. During computation, multiplying 7 by `0.10` reconstructs `0.70`. The device has traded an error of `0.03` for cheaper storage and arithmetic. The scale decides which real differences survive.

- Real weight w is divided by scale s to express it in integer-sized steps.
- Rounding chooses the nearest allowed integer q.
- Multiplying q by s reconstructs the approximate weight used in computation.
- The scale is calibrated so important values fit the available integer range.

### Why these operations are forced

- [Dividing by scale s](../../MATHEMATICAL_MOVES.md#division) expresses a real weight in units of one quantization step.
- [Rounding](../../MATHEMATICAL_MOVES.md#rounding) chooses the nearest integer level because storage permits only discrete codes; this is the deliberate lossy step.
- [Multiplying q by s](../../MATHEMATICAL_MOVES.md#multiplication) converts the stored step count back to the weight's approximate real scale. [The hat on w](../../MATHEMATICAL_MOVES.md#symbol-decorations) marks this reconstructed approximation; addition would shift levels rather than restore their unit size.

Only now can we compress the procedure:

$$
q=\mathrm{round}(w/s)
$$

$$
\widehat w=sq
$$

## The boundary of the discovery

Lower precision trades accuracy for efficiency and hardware support varies.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 096](../096-distributed-training/README.md)
