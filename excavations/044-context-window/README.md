# Excavation 044 — Context Windows — How Much Past Can the Model Carry?

[Previous: Excavation 043](../043-sampling/README.md)

Generation repeats one token at a time, and every new token may attend to the past. The stored conversation keeps growing.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Attend to the entire history forever. Computation and memory grow, and the model eventually exceeds positions it was trained to handle.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Attend to the entire history forever. Computation and memory grow, and the model eventually exceeds positions it was trained to handle.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past.

Only after that reasoning may we give your discovery its inherited name.

## Why It Still Fails

A larger window is not perfect memory. Retrieval, compression, recurrence, and careful data are separate inventions.

## Compress your discovery into mathematics


## Build each piece from what just happened

With 4 tokens, attention forms 4×4=16 query-key comparisons. With 8 tokens it forms 8×8=64—not merely twice as many. This repeated pairing creates square growth.

### Give Short Names Only After We Know the Pieces

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
