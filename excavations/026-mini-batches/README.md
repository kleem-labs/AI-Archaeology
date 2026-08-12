# Excavation 026 — Mini-Batches — Learning from More Than One Example

Gradient descent can update the network after one example. One muddy footprint can now steer every weight, and the next unusual footprint can pull the whole machine back again.

One tempting answer is to use one example per update. It is fast, but noisy accidents dominate. Use every observation before each update. It is stable, but painfully slow and cannot react until the whole archive is read.

So we average the evidence from a small group. Each batch is large enough to soften accidents and small enough to update frequently.

## From procedure to notation

The repair solves the immediate failure, but batch gradients are still estimates. Batch size changes noise, memory use, and sometimes what kind of solution training finds.

## The arithmetic we have earned

A tiger detector has two adjustable dials: how much to trust stripes and how much to trust movement. A clear morning photograph recommends raising those dials by 2 and 4. A muddy side view recommends 4 and 2. A night photograph recommends 3 and 3. For the stripe dial, the three witnesses propose 2+4+3=9, so their average advice is 3. The movement dial also averages to 3. If we merely added their advice, inviting three witnesses instead of one would triple the step even when their average opinion had not changed.

### Only now do the symbols earn names

- **B** is the selected mini-batch and **|B|** its number of examples.
- **Lᵢ** is loss for example i; **∇_θLᵢ** is that example's proposed parameter direction.
- Summing combines the witnesses.
- Dividing by batch size prevents merely using more examples from making the step proportionally larger.
- **g_B** is the batch's less noisy gradient estimate.

Only now can we compress that reasoning:

$$
g_B=\frac{1}{|B|}\sum_{i\in B}\nabla_\theta L_i
$$

## Carry the idea back into the world

A council does not ask one witness or the entire nation. It hears a manageable panel, makes a decision, then hears another.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Test what you believe

Use the [invention challenges](exercises.md).

## What this discovery now makes possible

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 027](../027-learning-rate/README.md)
