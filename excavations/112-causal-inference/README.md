# Excavation 112 — Causal Inference

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Continual learning, reasoning, and research

A world model predicts future observations. Prediction from recorded correlations cannot answer what would happen if the agent deliberately intervened and changed one cause.

At the Hall of Possible Worlds, the keeper of unfinished questions returns to the table of mirrored maps. Yesterday's instrument still lies open, so the first move asks for no new magic: treat every correlation as a controllable cause.

The keeper of unfinished questions repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: the trouble appears immediately: hot weather raises both; changing one does not necessarily change the other. The failure is stable enough to become evidence.

*The keeper of unfinished questions sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   treat every correlation as a… the trouble appears immediately: hot…
            \        /
             \      /
              represent plausible causal structure…
```

Across the table of mirrored maps, the old path and the repaired path run side by side. One carries “treat every correlation as a controllable cause”; the other knows how to represent plausible causal structure and distinguish observing a variable from intervening on it. When the failure—the trouble appears immediately: hot weather raises both; changing one does not necessarily change the other—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to causal inference. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: represent plausible causal structure and distinguish observing a variable from intervening on it. This problem and its repair will travel under the name **Causal Inference**, but the name carries no knowledge the scene has not earned.

What changed on the table of mirrored maps can be said without symbols. Before, the method could only treat every correlation as a controllable cause; now it can also represent plausible causal structure and distinguish observing a variable from intervening on it. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

## Understanding causal inference

Observing umbrellas predicts rain; forcing umbrellas open does not cause rain.

## Where causal inference runs out

Causal conclusions require assumptions not recoverable from correlations alone.

The causal inference repair holds, but the world asks for something it was never given. At the Hall of Possible Worlds, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the table of mirrored maps

Rebuild the causal inference scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 113](../113-counterfactuals/README.md)
