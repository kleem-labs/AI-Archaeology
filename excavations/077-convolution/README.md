# Excavation 077 — Convolution — Reusing the Same Local Detector

Pixels preserve local color and position without yet revealing edges, stripes, or animals. The same small visual pattern may appear anywhere in the image, so relearning a detector at every location wastes both data and parameters.

An obvious shortcut is to learn a separate edge detector for every location.

The trouble appears immediately: the model relearns the same pattern thousands of times and fails when it moves.

That failure tells us to slide one small learned filter across all positions and reuse its weights.

## Let the case decide

The filter [-1,1] produces a large response wherever neighboring brightness jumps from dark to light.

## The arithmetic we have earned

A ranger photographs a tiger behind tall grass. Along one row, neighboring brightness values change from dark grass to bright stripe and back to dark fur. She builds one three-slot stripe detector and slides that same detector across the row. At every location she multiplies each observed brightness by the matching detector slot and adds the agreements. A large total says the local patch resembles the stripe pattern. Reusing the detector matters because a stripe should remain a stripe whether it appears on the left or right of the photograph.

- The signal values are neighboring brightness measurements.
- The kernel values are the same small detector reused at every location.
- Multiplication measures how each local measurement agrees with its detector weight.
- Summation combines the local evidence; shifting i moves the same detector instead of learning a new one.

Only now can we compress the procedure:

$$
y_i=\sum_{j=0}^{k-1}x_{i+j}w_j
$$

## The boundary of the discovery

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
