# Excavation 077 — Convolution — Reusing the Same Local Detector

<!-- book-prose-v2 -->

Pixels preserve local color and position without yet revealing edges, stripes, or animals. The same small visual pattern may appear anywhere in the image, so relearning a detector at every location wastes both data and parameters.

A careful builder would first avoid adding machinery and learn a separate edge detector for every location.

The shortcut appears to retain everything convolution needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

Reality now asks a question the retained information cannot answer: the trouble appears immediately: the model relearns the same pattern thousands of times and fails when it moves.

The counterexample teaches convolution. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: slide one small learned filter across all positions and reuse its weights.

Now—and not earlier—we may introduce **Convolution**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to learn a separate edge detector for every location, and the case answers that the trouble appears immediately: the model relearns the same pattern thousands of times and fails when it moves. With the narrow repair—to slide one small learned filter across all positions and reuse its weights—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Convolution returns to the same counterexample, replaces the attempt to learn a separate edge detector for every location with the responsibility to slide one small learned filter across all positions and reuse its weights, and must succeed where the shortcut failed.

## Reusing the Same Local Detector

The filter [-1,1] produces a large response wherever neighboring brightness jumps from dark to light.

A formula for convolution is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

## The calculation hidden inside convolution

Before Convolution receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

A ranger photographs a tiger behind tall grass. Along one row, neighboring brightness values change from dark grass to bright stripe and back to dark fur. She builds one three-slot stripe detector and slides that same detector across the row. At every location she multiplies each observed brightness by the matching detector slot and adds the agreements. A large total says the local patch resembles the stripe pattern. Reusing the detector matters because a stripe should remain a stripe whether it appears on the left or right of the photograph.

The signal values are neighboring brightness measurements.
The kernel values are the same small detector reused at every location.
Multiplication measures how each local measurement agrees with its detector weight.
Summation combines the local evidence; shifting i moves the same detector instead of learning a new one.

### Why no cheaper operation does the same job

[Each multiplication](../../MATHEMATICAL_MOVES.md#multiplication) asks how strongly one local pixel agrees with the corresponding filter weight. A zero weight ignores that location; a negative one looks for contrast.
[The sum](../../MATHEMATICAL_MOVES.md#summation) combines those aligned local contributions into one detector response. Multiplying all responses would let one zero pixel erase the entire pattern.
[i+j](../../MATHEMATICAL_MOVES.md#indices) slides the same relative filter position j to a new image location i, which is how one detector is reused rather than relearned everywhere.

Every symbol in Convolution can now be read back into an action already performed. The whole procedure fits in one line:

$$
y_i=\sum_{j=0}^{k-1}x_{i+j}w_j
$$

## Where convolution runs out

Convolution assumes useful locality and translation reuse.

The boundary can be predicted from the construction itself. Convolution performs the repair to slide one small learned filter across all positions and reuse its weights; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

## Take convolution to the workbench

Move convolution from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running convolution, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the convolution result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 078](../078-pooling/README.md)
