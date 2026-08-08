# Excavation 039 — Causal Masking — Preventing the Future from Leaking Backward

[Previous: Excavation 038](../038-position/README.md)

During next-token training the whole sentence is available. Without a barrier, the representation at cat can inspect the answer sitting to its right.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Train each prefix in a separate forward pass. It prevents cheating but repeats nearly identical work.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Train each prefix in a separate forward pass. It prevents cheating but repeats nearly identical work.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Process all positions together while blocking attention from position i to every later position j.

Only after that reasoning may we give your discovery its inherited name.

## Why It Still Fails

A mask prevents direct attention leakage; shifted targets and data pipelines must also align correctly.

## Compress your discovery into mathematics


## Build each piece from what just happened

For position i=2, sources j=0,1,2 receive mask value 0 and remain visible. Sources j=3,4 receive negative infinity; exponentiation turns those scores into zero weight.

### Give Short Names Only After We Know the Pieces

- **i** is the receiving position and **j** a possible source position.
- When j≤i, the source is present or past, so adding zero leaves its attention score unchanged.
- When j>i, the source is future; adding −∞ makes its later softmax weight zero.
- **M_ij** stores that allowed-or-forbidden correction for every pair.

Only now can we compress that reasoning:

$$
M_{ij}=\begin{cases}0&j\le i\\-\infty&j>i\end{cases}
$$


The equation arrives after every operation has a job.

## Carry the idea back into the world

An exam sheet can contain later questions, but an opaque cover hides everything beyond the current line.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 040](../040-next-token-examples/README.md)
