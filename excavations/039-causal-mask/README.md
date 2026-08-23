# Excavation 039 — Causal Masking — Preventing the Future from Leaking Backward

<!-- book-prose-v2 -->

Position marks make order visible. During next-token training, however, the correct answer is sitting to the right inside the same sentence, where an unrestricted attention mechanism can simply look at it.

The machinery already in our hands suggests that we train each prefix in a separate forward pass.

This is how causal masking ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

One counterexample is enough to expose the missing job: it prevents cheating but repeats nearly identical work.

The wrong answer makes the need for causal masking inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: we need to process all positions together while blocking attention from position i to every later position j.

The usual name, **Causal Masking**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to train each prefix in a separate forward pass. produces the observed failure: it prevents cheating but repeats nearly identical work. Starting with the repaired demand to we need to process all positions together while blocking attention from position i to every later position j preserves the information the shortcut lost. The subject of causal masking lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to we need to process all positions together while blocking attention from position i to every later position j instead of merely trying to train each prefix in a separate forward pass.. That controlled contrast is what turns a plausible explanation of causal masking into an understandable derivation.

## The calculation hidden inside causal masking

Before Causal Masking receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

A mask prevents direct attention leakage; shifted targets and data pipelines must also align correctly.

While learning from “the tiger sleeps,” the model sees the complete training sentence. At the position after *the*, the correct next token *tiger* is already sitting to the right. Place an impassable barrier on every connection pointing into the future. In score language, those forbidden paths receive a value whose exponential contribution becomes zero, while present and earlier words remain available.

### Names for pieces we have already used

**i** is the receiving position and **j** a possible source position.
When j≤i, the source is present or past, so adding zero leaves its attention score unchanged.
When j>i, the source is future; adding −∞ makes its later softmax weight zero.
**M_ij** stores that allowed-or-forbidden correction for every pair.

### Why no cheaper operation does the same job

[Cases](../../MATHEMATICAL_MOVES.md#cases) are forced because visible and forbidden positions obey genuinely different rules.
[j ≤ i and j > i](../../MATHEMATICAL_MOVES.md#inequalities) divide earlier-or-current keys from future keys for query position i.
Zero leaves an allowed attention score unchanged. [Negative infinity](../../MATHEMATICAL_MOVES.md#negative-sign) makes a forbidden score's exponential weight zero after softmax; a large positive value would do the opposite.

The notation is finally shorter than the story that created it:

$$
M_{ij}=\begin{cases}0&j\le i\\-\infty&j>i\end{cases}
$$

The equation arrives after every operation has a job.

## Causal Masking beyond this one case

An exam sheet can contain later questions, but an opaque cover hides everything beyond the current line.

## Take causal masking to the workbench

The reader has reconstructed causal masking in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running causal masking, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the causal masking result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 040](../040-next-token-examples/README.md)
