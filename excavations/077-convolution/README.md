# Excavation 077 — Convolution — Reusing the Same Local Detector

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

Pixels preserve local color and position without yet revealing edges, stripes, or animals. The same small visual pattern may appear anywhere in the image, so relearning a detector at every location wastes both data and parameters.

The previous discovery reaches the Glass Menagerie carrying one unfinished problem. Beside the wall of illuminated tiles, the maker of seeing-machines first tries to learn a separate edge detector for every location.

There is good reason to begin this way. If we learn a separate edge detector for every location, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: the trouble appears immediately: the model relearns the same pattern thousands of times and fails when it moves.

This failure cannot be repaired by performing the instruction to learn a separate edge detector for every location more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the wall of illuminated tiles; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to slide one small learned filter across all positions and reuse its weights. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Convolution**. The name is simply a handle for the distinction already reconstructed.

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
