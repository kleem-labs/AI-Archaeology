# Excavation 191 — Data Parallelism — Let Several Workers Observe Different Evidence

<!-- book-prose-v2 -->

Gradient noise measurements choose a useful global batch. One device cannot process that batch quickly enough, even though the modern model and optimizer state now fit through sharding.

The previous discovery seems almost sufficient: we could send the same mini-batch to every worker and average their gradients.

The shortcut appears to retain everything data parallelism needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

One counterexample is enough to expose the missing job: all workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully.

The counterexample teaches data parallelism. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update.

Now—and not earlier—we may introduce **Data Parallelism**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to send the same mini-batch to every worker and average their gradients, and the case answers that all workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully. With the narrow repair—to replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Data Parallelism returns to the same counterexample, replaces the attempt to send the same mini-batch to every worker and average their gradients with the responsibility to replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update, and must succeed where the shortcut failed.

## Let Several Workers Observe Different Evidence

Four workers each read eight different sequences. Their four average gradients become one average over thirty-two sequences before any worker advances the parameters.

A formula for data parallelism is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

## The calculation hidden inside data parallelism

Before Data Parallelism receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

P is the number of data-parallel workers, g_p is worker p's average gradient from different examples, and g is the single gradient used by the shared optimizer step.

### Why no cheaper operation does the same job

[Summation](../../MATHEMATICAL_MOVES.md#summation) lets every worker's independent evidence contribute. [Division](../../MATHEMATICAL_MOVES.md#division) returns advice per worker so adding hardware does not enlarge the update by itself. Multiplication would let a zero coordinate from one worker erase all others.

Every symbol in Data Parallelism can now be read back into an action already performed. The whole procedure fits in one line:

$$
g=\frac1P\sum_{p=1}^{P}g_p
$$

## Where data parallelism runs out

Because one shared update cannot proceed until every worker's evidence has joined the average, synchronous data parallelism waits for the slowest worker and communicates a full update's worth of gradient information.

The boundary can be predicted from the construction itself. Data Parallelism performs the repair to replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

## Take data parallelism to the workbench

Move data parallelism from imagination to evidence by making the shortcut fail under controlled inputs. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running data parallelism, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the data parallelism result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Pipeline Parallelism — Stop Waiting for the Whole Model to Cross One Device at a Time](../192-pipeline-parallelism/README.md)
