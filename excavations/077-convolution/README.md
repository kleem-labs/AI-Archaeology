# Excavation 077 — Convolution — Reusing the Same Local Detector

[Previous: Excavation 076](../076-pixels/README.md)

An edge can appear anywhere in an image.

Without knowing the inherited method, we might try this: Learn a separate edge detector for every location.

Its hidden assumption appears in the following case: The model relearns the same pattern thousands of times and fails when it moves.

Remove that assumption and the needed repair becomes clear: Slide one small learned filter across all positions and reuse its weights.

## Now work a case you can see

The filter [-1,1] produces a large response wherever neighboring brightness jumps from dark to light.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build each piece from what just happened


A ranger photographs a tiger behind tall grass. Along one row, neighboring brightness values change from dark grass to bright stripe and back to dark fur. She builds one three-slot stripe detector and slides that same detector across the row. At every location she multiplies each observed brightness by the matching detector slot and adds the agreements. A large total says the local patch resembles the stripe pattern. Reusing the detector matters because a stripe should remain a stripe whether it appears on the left or right of the photograph.

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

This is not an unrelated warning. The construction can slide one small learned filter across all positions and reuse its weights. It cannot infer or control information that never enters that construction.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 078](../078-pooling/README.md)
