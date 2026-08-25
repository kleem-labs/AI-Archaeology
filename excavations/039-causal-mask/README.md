# Excavation 039 — Causal Masking — Preventing the Future from Leaking Backward

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Language models and useful answers

Position marks make order visible. During next-token training, however, the correct answer is sitting to the right inside the same sentence, where an unrestricted attention mechanism can simply look at it.

Inside the Clockwork Scriptorium, the old method is given an honest chance. The mechanist places the evidence on the sentence-wheel and tries to train each prefix in a separate forward pass.

Nothing about this first move is careless. To train each prefix in a separate forward pass is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: it prevents cheating but repeats nearly identical work.

The important discovery is not merely that trying to train each prefix in a separate forward pass failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the sentence-wheel, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to process all positions together while blocking attention from position i to every later position j. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Causal Masking**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## The calculation hidden inside causal masking

The mechanist carries the causal masking scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A mask prevents direct attention leakage; shifted targets and data pipelines must also align correctly.

While learning from “the tiger sleeps,” the model sees the complete training sentence. At the position after *the*, the correct next token *tiger* is already sitting to the right. Place an impassable barrier on every connection pointing into the future. In score language, those forbidden paths receive a value whose exponential contribution becomes zero, while present and earlier words remain available.

### Naming what is already on the table

**i** is the receiving position and **j** a possible source position.
When j≤i, the source is present or past, so adding zero leaves its attention score unchanged.
When j>i, the source is future; adding −∞ makes its later softmax weight zero.
**M_ij** stores that allowed-or-forbidden correction for every pair.

### Why the melody needs these exact notes

[Cases](../../MATHEMATICAL_MOVES.md#cases) are forced because visible and forbidden positions obey genuinely different rules.
[j ≤ i and j > i](../../MATHEMATICAL_MOVES.md#inequalities) divide earlier-or-current keys from future keys for query position i.
Zero leaves an allowed attention score unchanged. [Negative infinity](../../MATHEMATICAL_MOVES.md#negative-sign) makes a forbidden score's exponential weight zero after softmax; a large positive value would do the opposite.

The calculation reuses familiar motions: **the turning wind**—an uphill quantity is made to point downhill, or surprise is made to count as cost. Together they keep the path from the concrete case to notation intact.

The story of causal masking has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
M_{ij}=\begin{cases}0&j\le i\\-\infty&j>i\end{cases}
$$

The equation arrives after every operation has a job.

## Causal Masking beyond this one case

An exam sheet can contain later questions, but an opaque cover hides everything beyond the current line.

## Return to the sentence-wheel

Rebuild the causal masking scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 040](../040-next-token-examples/README.md)
