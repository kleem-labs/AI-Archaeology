# Excavation 044 — Context Windows — How Much Past Can the Model Carry?

[Previous: Excavation 043](../043-sampling/README.md)

## Problem

Generation repeats one token at a time, and every new token may attend to the past. The stored conversation keeps growing.

## Naive Attempt

Attend to the entire history forever. Computation and memory grow, and the model eventually exceeds positions it was trained to handle.

## Why It Fails

The attempt either gives the model forbidden information, discards useful structure, or performs repeated work without solving the actual representation problem.

## Better Attempt

Choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past.

## Why It Still Fails

A larger window is not perfect memory. Retrieval, compression, recurrence, and careful data are separate inventions.

## Key Insight

**Choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past.**

## Mathematics Emerges

## Why Every Term Must Exist Before the Equation

- **n** is the number of tokens inside the active context.
- Each of n queries can compare with n keys, creating roughly n×n score pairs.
- That repeated pairwise work is why cost grows proportionally to n² rather than n.
- The proportional sign is used because heads, width, batching, and implementation add constants omitted from this scaling argument.

Only now can we compress that reasoning:

$$
\text{attention cost}\propto n^2
$$


The equation arrives after every operation has a job.

## Real-World Analogy

A desk holds only a finite number of open pages. Notes and indexes can preserve selected information after pages leave the desk.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 045](../045-tiny-gpt/README.md)
