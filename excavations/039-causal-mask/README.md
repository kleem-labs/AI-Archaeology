# Excavation 039 — Causal Masking — Preventing the Future from Leaking Backward

Position marks make order visible. During next-token training, however, the correct answer is sitting to the right inside the same sentence, where an unrestricted attention mechanism can simply look at it.

At first we train each prefix in a separate forward pass. It prevents cheating but repeats nearly identical work.

We need to process all positions together while blocking attention from position i to every later position j.

## From procedure to notation

A mask prevents direct attention leakage; shifted targets and data pipelines must also align correctly.

## The arithmetic we have earned

While learning from “the tiger sleeps,” the model sees the complete training sentence. At the position after *the*, the correct next token *tiger* is already sitting to the right. Place an impassable barrier on every connection pointing into the future. In score language, those forbidden paths receive a value whose exponential contribution becomes zero, while present and earlier words remain available.

### Only now do the symbols earn names

- **i** is the receiving position and **j** a possible source position.
- When j≤i, the source is present or past, so adding zero leaves its attention score unchanged.
- When j>i, the source is future; adding −∞ makes its later softmax weight zero.
- **M_ij** stores that allowed-or-forbidden correction for every pair.

### Why these operations are forced

- [Cases](../../MATHEMATICAL_MOVES.md#cases) are forced because visible and forbidden positions obey genuinely different rules.
- [j ≤ i and j > i](../../MATHEMATICAL_MOVES.md#inequalities) divide earlier-or-current keys from future keys for query position i.
- Zero leaves an allowed attention score unchanged. [Negative infinity](../../MATHEMATICAL_MOVES.md#negative-sign) makes a forbidden score's exponential weight zero after softmax; a large positive value would do the opposite.

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
