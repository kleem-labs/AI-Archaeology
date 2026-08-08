# Excavation 077 — Convolution — Reusing the Same Local Detector

[Previous: Excavation 076](../076-pixels/README.md)

An edge can appear anywhere in an image.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Learn a separate edge detector for every location.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* The model relearns the same pattern thousands of times and fails when it moves.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Slide one small learned filter across all positions and reuse its weights.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

The filter [-1,1] produces a large response wherever neighboring brightness jumps from dark to light.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build each piece from what just happened

- The signal values are neighboring brightness measurements.
- The kernel values are the same small detector reused at every location.
- Multiplication measures how each local measurement agrees with its detector weight.
- Summation combines the local evidence; shifting i moves the same detector instead of learning a new one.

Only now can we compress the procedure:

$$
y_i=\sum_{j=0}^{k-1}x_{i+j}w_j
$$

## Where your new idea still breaks

Convolution assumes useful locality and translation reuse.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 078](../078-pooling/README.md)
