# Excavation 173 — Tensor Parallelism — Split One Matrix That No Device Can Hold

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Sharded parameters can be gathered for computation, but the largest matrix itself becomes too large to materialize or multiply on one worker.

A new case arrives at the Engine Cavern, but the enginewright first reaches for the familiar brass reference machine. Its promise is simple: assign whole layers to different devices and pass every activation through them sequentially.

At the edge of the brass reference machine, the shortcut produces its consequence: one oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work. That consequence, not a textbook, earns the next move.

*The enginewright sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: assign whole layers to different…
possible road B ─┘              └── loses: one oversized layer still cannot fit,…

same roads ──▶ repaired map ──▶ split a matrix across its columns or…
```

The enginewright covers the new mark and the old contradiction returns: one oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work. The cover is lifted, restoring the ability to split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason tensor parallelism exists.

What must change for tensor parallelism is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output. That threshold is where **Tensor Parallelism** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In tensor parallelism, that memory takes a precise form: whenever one oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work, preserve enough structure to split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output.

## Split One Matrix That No Device Can Hold

Divide one vocabulary projection into four column blocks. Each device scores one quarter of the vocabulary from the same hidden state; concatenation restores the full logits.

## The calculation hidden inside tensor parallelism

The enginewright carries the tensor parallelism scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Split the vocabulary-scoring matrix into four column blocks. Every device receives the same hidden state X but multiplies it by only its own block W_p, producing scores Y_p for its quarter of the vocabulary. Those scores must remain distinct, so place the four blocks beside one another in vocabulary order. Adding them would collapse different tokens into the same slots. Y names the restored full score row after concatenation.

W is partitioned into P column blocks; every worker receives X and produces the corresponding block of output columns.

### Why the melody needs these exact notes

[Concatenation](../../MATHEMATICAL_MOVES.md#concatenation) preserves distinct output columns side by side; addition would collapse vocabulary scores that must remain separate. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) applies the same input X to each learned block, and equality states that partitioned execution matches the unsplit matrix operation.

Trace each operation by touch rather than by name: **the binding loom**—distinct pieces remain side by side instead of being blended away; and **the lock and key**—one influence matters through another, and either missing factor can close the path. Together they form the smallest mechanism that survives the counterexample.

The brass reference machine already contains the complete tensor parallelism mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
Y_p=XW_p,\quad Y=[Y_1,Y_2,\ldots,Y_P]
$$

## Where tensor parallelism runs out

Tensor parallelism introduces communication inside every layer, so a slow interconnect can erase its benefit.

Here the new path ends honestly. Tensor Parallelism can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the brass reference machine

Rebuild the tensor parallelism scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Speculative Decoding — Let a Small Model Propose, Never Decide](../174-speculative-decoding/README.md)
