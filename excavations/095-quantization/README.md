# Excavation 095 — Quantization

[Previous: Excavation 094](../094-lora/README.md)

How can a model use less memory and faster arithmetic at inference?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Round every weight aggressively without measuring effect.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Small but important distinctions disappear and outputs degrade.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Map values to a limited set of levels using calibrated scale and test sensitive layers.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

Weights from -1 to 1 become 256 integer levels; a stored integer plus scale approximately reconstructs each value.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build each piece from what just happened

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

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 096](../096-distributed-training/README.md)
