# Excavation 095 — Quantization

<!-- book-prose-v2 -->

Low-rank adaptation learns a small correction while preserving the base model. The unchanged base weights still consume memory and arithmetic every time the adapted model answers.

The previous discovery seems almost sufficient: we could round every weight aggressively without measuring effect.

The shortcut appears to retain everything quantization needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

One counterexample is enough to expose the missing job: small but important distinctions disappear and outputs degrade.

The counterexample teaches quantization. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: we need to map values to a limited set of levels using calibrated scale and test sensitive layers.

Now—and not earlier—we may introduce **Quantization**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to round every weight aggressively without measuring effect, and the case answers that small but important distinctions disappear and outputs degrade. With the narrow repair—to we need to map values to a limited set of levels using calibrated scale and test sensitive layers—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Quantization returns to the same counterexample, replaces the attempt to round every weight aggressively without measuring effect with the responsibility to we need to map values to a limited set of levels using calibrated scale and test sensitive layers, and must succeed where the shortcut failed.

## Understanding quantization

Weights from -1 to 1 become 256 integer levels; a stored integer plus scale approximately reconstructs each value.

A formula for quantization is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

## The calculation hidden inside quantization

Before Quantization receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Suppose one learned weight is `0.73`, but the device can store only integer steps of size `0.10`. Dividing by the step size says the weight is 7.3 steps; rounding stores integer 7. During computation, multiplying 7 by `0.10` reconstructs `0.70`. The device has traded an error of `0.03` for cheaper storage and arithmetic. The scale decides which real differences survive.

Real weight w is divided by scale s to express it in integer-sized steps.
Rounding chooses the nearest allowed integer q.
Multiplying q by s reconstructs the approximate weight used in computation.
The scale is calibrated so important values fit the available integer range.

### Why no cheaper operation does the same job

[Dividing by scale s](../../MATHEMATICAL_MOVES.md#division) expresses a real weight in units of one quantization step.
[Rounding](../../MATHEMATICAL_MOVES.md#rounding) chooses the nearest integer level because storage permits only discrete codes; this is the deliberate lossy step.
[Multiplying q by s](../../MATHEMATICAL_MOVES.md#multiplication) converts the stored step count back to the weight's approximate real scale. [The hat on w](../../MATHEMATICAL_MOVES.md#symbol-decorations) marks this reconstructed approximation; addition would shift levels rather than restore their unit size.

Every symbol in Quantization can now be read back into an action already performed. The whole procedure fits in one line:

$$
q=\mathrm{round}(w/s)
$$

$$
\widehat w=sq
$$

## Where quantization runs out

Lower precision trades accuracy for efficiency and hardware support varies.

The boundary can be predicted from the construction itself. Quantization performs the repair to we need to map values to a limited set of levels using calibrated scale and test sensitive layers; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

## Take quantization to the workbench

Move quantization from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running quantization, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the quantization result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 096](../096-distributed-training/README.md)
