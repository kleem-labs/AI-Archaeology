# Excavation 173 — Tensor Parallelism — Split One Matrix That No Device Can Hold

Sharded parameters can be gathered for computation, but the largest matrix itself becomes too large to materialize or multiply on one worker.

Perhaps we assign whole layers to different devices and pass every activation through them sequentially.

It survives until the measured run answers back. One oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work.

Now the missing requirement is concrete. Split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output.

## Let one run decide

Divide one vocabulary projection into four column blocks. Each device scores one quarter of the vocabulary from the same hidden state; concatenation restores the full logits.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

Split the vocabulary-scoring matrix into four column blocks. Every device receives the same hidden state X but multiplies it by only its own block W_p, producing scores Y_p for its quarter of the vocabulary. Those scores must remain distinct, so place the four blocks beside one another in vocabulary order. Adding them would collapse different tokens into the same slots. Y names the restored full score row after concatenation.

W is partitioned into P column blocks; every worker receives X and produces the corresponding block of output columns.

### Why these operations are forced

[Concatenation](../../MATHEMATICAL_MOVES.md#concatenation) preserves distinct output columns side by side; addition would collapse vocabulary scores that must remain separate. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) applies the same input X to each learned block, and equality states that partitioned execution matches the unsplit matrix operation.

Only now can we compress the procedure:

$$
Y_p=XW_p,\quad Y=[Y_1,Y_2,\ldots,Y_P]
$$

## What this repair cannot do

Tensor parallelism introduces communication inside every layer, so a slow interconnect can erase its benefit.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Speculative Decoding — Let a Small Model Propose, Never Decide](../174-speculative-decoding/README.md)
