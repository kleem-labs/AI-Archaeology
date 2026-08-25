# Excavation 044 — Context Windows — How Much Past Can the Model Carry?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Language models and useful answers

Sampling allows several plausible futures instead of one repetitive path. Every chosen token is appended to the past, so the amount of history available to attention grows until computation or memory reaches a boundary.

At the Clockwork Scriptorium, the mechanist meets the next case beside the sentence-wheel. The nearest idea is also the most reasonable one: attend to the entire history forever.

The attraction of this attempt is easy to see. To attend to the entire history forever reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: computation and memory grow, and the model eventually exceeds positions it was trained to handle.

The contradiction matters because it identifies a structural loss in the instruction to attend to the entire history forever, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The sentence-wheel will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Context Windows**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## The calculation hidden inside context windows

The mechanist carries the context windows scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A larger window is not perfect memory. Retrieval, compression, recurrence, and careful data are separate inventions.

Four words create sixteen possible question–source comparisons: each of four positions may inspect four positions. Eight words create sixty-four. The growth becomes visible when we draw the square table: doubling each side multiplies the number of cells by four. The cost comes from pairwise looking, not from storing eight words alone.

### Naming what is already on the table

**n** is the number of tokens inside the active context.
Each of n queries can compare with n keys, creating roughly n×n score pairs.
That repeated pairwise work is why cost grows proportionally to n² rather than n.
The proportional sign is used because heads, width, batching, and implementation add constants omitted from this scaling argument.

### Why the melody needs these exact notes

[Proportionality](../../MATHEMATICAL_MOVES.md#proportionality) states the growth pattern without pretending every implementation has the same fixed cost.
[The square](../../MATHEMATICAL_MOVES.md#powers) appears because each of n query positions can compare with n key positions, creating n×n pairs. A linear n would count only one comparison per token.

Inside context windows, familiar operations return with stricter duties: **the echoing chamber**—large departures return with greater force while opposite signs stop cancelling. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Nothing remains unnamed in the context windows case on the sentence-wheel. We can finally trade the long route for its compact map:

$$
\text{attention cost}\propto n^2
$$

The equation arrives after every operation has a job.

## Context Windows beyond this one case

A desk holds only a finite number of open pages. Notes and indexes can preserve selected information after pages leave the desk.

## Return to the sentence-wheel

Rebuild the context windows scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 045](../045-tiny-gpt/README.md)
