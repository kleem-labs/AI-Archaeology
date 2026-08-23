# Excavation 173 — Tensor Parallelism — Split One Matrix That No Device Can Hold

<!-- book-prose-v2 -->

Sharded parameters can be gathered for computation, but the largest matrix itself becomes too large to materialize or multiply on one worker.

A careful builder would first avoid adding machinery and assign whole layers to different devices and pass every activation through them sequentially.

The shortcut appears to retain everything tensor parallelism needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

Reality now asks a question the retained information cannot answer: one oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work.

The counterexample teaches tensor parallelism. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output.

Now—and not earlier—we may introduce **Tensor Parallelism**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to assign whole layers to different devices and pass every activation through them sequentially, and the case answers that one oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work. With the narrow repair—to split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Tensor Parallelism returns to the same counterexample, replaces the attempt to assign whole layers to different devices and pass every activation through them sequentially with the responsibility to split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output, and must succeed where the shortcut failed.

## Split One Matrix That No Device Can Hold

Divide one vocabulary projection into four column blocks. Each device scores one quarter of the vocabulary from the same hidden state; concatenation restores the full logits.

A formula for tensor parallelism is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

## The calculation hidden inside tensor parallelism

Before Tensor Parallelism receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Split the vocabulary-scoring matrix into four column blocks. Every device receives the same hidden state X but multiplies it by only its own block W_p, producing scores Y_p for its quarter of the vocabulary. Those scores must remain distinct, so place the four blocks beside one another in vocabulary order. Adding them would collapse different tokens into the same slots. Y names the restored full score row after concatenation.

W is partitioned into P column blocks; every worker receives X and produces the corresponding block of output columns.

### Why no cheaper operation does the same job

[Concatenation](../../MATHEMATICAL_MOVES.md#concatenation) preserves distinct output columns side by side; addition would collapse vocabulary scores that must remain separate. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) applies the same input X to each learned block, and equality states that partitioned execution matches the unsplit matrix operation.

Every symbol in Tensor Parallelism can now be read back into an action already performed. The whole procedure fits in one line:

$$
Y_p=XW_p,\quad Y=[Y_1,Y_2,\ldots,Y_P]
$$

## Where tensor parallelism runs out

Tensor parallelism introduces communication inside every layer, so a slow interconnect can erase its benefit.

The boundary can be predicted from the construction itself. Tensor Parallelism performs the repair to split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

## Take tensor parallelism to the workbench

Move tensor parallelism from imagination to evidence by making the shortcut fail under controlled inputs. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running tensor parallelism, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the tensor parallelism result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Speculative Decoding — Let a Small Model Propose, Never Decide](../174-speculative-decoding/README.md)
