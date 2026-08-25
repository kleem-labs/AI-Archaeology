# Excavation 112 — Causal Inference

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Continual learning, reasoning, and research

A world model predicts future observations. Prediction from recorded correlations cannot answer what would happen if the agent deliberately intervened and changed one cause.

At the Hall of Possible Worlds, the keeper of unfinished questions meets the next case beside the table of mirrored maps. The nearest idea is also the most reasonable one: treat every correlation as a controllable cause.

The attraction of this attempt is easy to see. To treat every correlation as a controllable cause reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: the trouble appears immediately: hot weather raises both; changing one does not necessarily change the other.

The contradiction matters because it identifies a structural loss in the instruction to treat every correlation as a controllable cause, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The table of mirrored maps will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must represent plausible causal structure and distinguish observing a variable from intervening on it. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Causal Inference**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## Understanding causal inference

Observing umbrellas predicts rain; forcing umbrellas open does not cause rain.

## Where causal inference runs out

Causal conclusions require assumptions not recoverable from correlations alone.

The causal inference repair holds, but the world asks for something it was never given. At the Hall of Possible Worlds, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the table of mirrored maps

Rebuild the causal inference scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 113](../113-counterfactuals/README.md)
