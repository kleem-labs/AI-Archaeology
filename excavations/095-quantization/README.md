# Excavation 095 — Quantization

[Previous: Excavation 094](../094-lora/README.md)

How can a model use less memory and faster arithmetic at inference?

The first solution that suggests itself is this: Round every weight aggressively without measuring effect.

The idea survives only until we test it against reality: Small but important distinctions disappear and outputs degrade.

The failure gives us a precise requirement: Map values to a limited set of levels using calibrated scale and test sensitive layers.

## Now work a case you can see

Weights from -1 to 1 become 256 integer levels; a stored integer plus scale approximately reconstructs each value.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build each piece from what just happened


Suppose one learned weight is `0.73`, but the device can store only integer steps of size `0.10`. Dividing by the step size says the weight is 7.3 steps; rounding stores integer 7. During computation, multiplying 7 by `0.10` reconstructs `0.70`. The device has traded an error of `0.03` for cheaper storage and arithmetic. The scale decides which real differences survive.

- Real weight w is divided by scale s to express it in integer-sized steps.
- Rounding chooses the nearest allowed integer q.
- Multiplying q by s reconstructs the approximate weight used in computation.
- The scale is calibrated so important values fit the available integer range.

Only now can we compress the procedure:

$$
q=\mathrm{round}(w/s),\qquad \widehat w=sq
$$

## Where your new idea still breaks

Lower precision trades accuracy for efficiency and hardware support varies.

The boundary follows from the mechanism itself. We designed it to map values to a limited set of levels using calibrated scale and test sensitive layers. That operation solves the failure we had reached, but it contains no step that answers the additional problem above.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 096](../096-distributed-training/README.md)
