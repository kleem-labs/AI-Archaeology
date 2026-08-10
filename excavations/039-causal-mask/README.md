# Excavation 039 — Causal Masking — Preventing the Future from Leaking Backward

[Previous: Excavation 038](../038-position/README.md)

During next-token training the whole sentence is available. Without a barrier, the representation at cat can inspect the answer sitting to its right.

Our first construction is deliberately modest: Train each prefix in a separate forward pass. It prevents cheating but repeats nearly identical work.

The cost of that attempt points to the missing operation: Process all positions together while blocking attention from position i to every later position j.

## From procedure to notation

A mask prevents direct attention leakage; shifted targets and data pipelines must also align correctly.



## Build each piece from what just happened

While learning from “the tiger sleeps,” the model sees the complete training sentence. At the position after *the*, the correct next token *tiger* is already sitting to the right. Place an impassable barrier on every connection pointing into the future. In score language, those forbidden paths receive a value whose exponential contribution becomes zero, while present and earlier words remain available.

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
