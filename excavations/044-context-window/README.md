# Excavation 044 — Context Windows — How Much Past Can the Model Carry?

Sampling allows several plausible futures instead of one repetitive path. Every chosen token is appended to the past, so the amount of history available to attention grows until computation or memory reaches a boundary.

One tempting answer is to attend to the entire history forever. Computation and memory grow, and the model eventually exceeds positions it was trained to handle.

Now we can see what is missing: we must choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past.

## From procedure to notation

A larger window is not perfect memory. Retrieval, compression, recurrence, and careful data are separate inventions.

## The arithmetic we have earned

Four words create sixteen possible question–source comparisons: each of four positions may inspect four positions. Eight words create sixty-four. The reader can see the growth by drawing the square table: doubling each side multiplies the number of cells by four. The cost comes from pairwise looking, not from storing eight words alone.

### Only now do the symbols earn names

- **n** is the number of tokens inside the active context.
- Each of n queries can compare with n keys, creating roughly n×n score pairs.
- That repeated pairwise work is why cost grows proportionally to n² rather than n.
- The proportional sign is used because heads, width, batching, and implementation add constants omitted from this scaling argument.

Only now can we compress that reasoning:

$$
\text{attention cost}\propto n^2
$$

The equation arrives after every operation has a job.

## Carry the idea back into the world

A desk holds only a finite number of open pages. Notes and indexes can preserve selected information after pages leave the desk.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 045](../045-tiny-gpt/README.md)
