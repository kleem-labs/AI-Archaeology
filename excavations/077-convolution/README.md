# Excavation 077 — Convolution — Reusing the Same Local Detector

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Pixels preserve local color and position without yet revealing edges, stripes, or animals. The same small visual pattern may appear anywhere in the image, so relearning a detector at every location wastes both data and parameters.

A new case arrives at the Glass Menagerie, but the maker of seeing-machines first reaches for the familiar wall of illuminated tiles. Its promise is simple: learn a separate edge detector for every location.

At the edge of the wall of illuminated tiles, the shortcut produces its consequence: the trouble appears immediately: the model relearns the same pattern thousands of times and fails when it moves. That consequence, not a textbook, earns the next move.

*The maker of seeing-machines sketches the break before changing it:*

```text
observation
    │
    ▼
[learn a separate edge detector for…]
    │
    ╳  the trouble appears immediately: the…
    │
    ▼
[slide one small learned filter across…]
```

The maker of seeing-machines covers the new mark and the old contradiction returns: the trouble appears immediately: the model relearns the same pattern thousands of times and fails when it moves. The cover is lifted, restoring the ability to slide one small learned filter across all positions and reuse its weights, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason convolution exists.

What must change for convolution is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: slide one small learned filter across all positions and reuse its weights. That threshold is where **Convolution** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In convolution, that memory takes a precise form: whenever the trouble appears immediately: the model relearns the same pattern thousands of times and fails when it moves, preserve enough structure to slide one small learned filter across all positions and reuse its weights.

## Reusing the Same Local Detector

The filter [-1,1] produces a large response wherever neighboring brightness jumps from dark to light.

## The calculation hidden inside convolution

The maker of seeing-machines carries the convolution scene to the wall of illuminated tiles. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A ranger photographs a tiger behind tall grass. Along one row, neighboring brightness values change from dark grass to bright stripe and back to dark fur. She builds one three-slot stripe detector and slides that same detector across the row. At every location she multiplies each observed brightness by the matching detector slot and adds the agreements. A large total says the local patch resembles the stripe pattern. Reusing the detector matters because a stripe should remain a stripe whether it appears on the left or right of the photograph.

The signal values are neighboring brightness measurements.
The kernel values are the same small detector reused at every location.
Multiplication measures how each local measurement agrees with its detector weight.
Summation combines the local evidence; shifting i moves the same detector instead of learning a new one.

### Why the melody needs these exact notes

[Each multiplication](../../MATHEMATICAL_MOVES.md#multiplication) asks how strongly one local pixel agrees with the corresponding filter weight. A zero weight ignores that location; a negative one looks for contrast.
[The sum](../../MATHEMATICAL_MOVES.md#summation) combines those aligned local contributions into one detector response. Multiplying all responses would let one zero pixel erase the entire pattern.
[i+j](../../MATHEMATICAL_MOVES.md#indices) slides the same relative filter position j to a new image location i, which is how one detector is reused rather than relearned everywhere.

Trace each operation by touch rather than by name: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. Together they form the smallest mechanism that survives the counterexample.

The wall of illuminated tiles already contains the complete convolution mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
y_i=\sum_{j=0}^{k-1}x_{i+j}w_j
$$

## Where convolution runs out

Convolution assumes useful locality and translation reuse.

Here the new path ends honestly. Convolution can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the wall of illuminated tiles

Rebuild the convolution scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 078](../078-pooling/README.md)
