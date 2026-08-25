# Excavation 048 — Hallucination — When Fluent Prediction Outruns Evidence

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Information Theory](../../MATHEMATICS_ATLAS.md#information)
>
> **Applied territory:** Language models and useful answers

Evaluation therefore begins with the job the system is supposed to perform. On that job, a disturbing failure remains: the model can produce a beautifully fluent answer even when no evidence supports it.

At the Hall of Voices, the public archivist meets the next case beside the listening table. The nearest idea is also the most reasonable one: trust fluent language because uncertainty should sound hesitant.

The attraction of this attempt is easy to see. To trust fluent language because uncertainty should sound hesitant reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: training rewards plausible continuations. A fabricated citation can match the shape of real citations and therefore sound more natural than “I do not know.”.

The contradiction matters because it identifies a structural loss in the instruction to trust fluent language because uncertainty should sound hesitant, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The listening table will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Hallucination**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## When Fluent Prediction Outruns Evidence

The prompt asks for the 2018 paper “Tiger Attention Networks.” Search returns no matching source. A supported system must say no source was found instead of completing the familiar citation pattern.

## Where hallucination runs out

Evidence reduces unsupported claims but sources can be wrong, stale, conflicting, or misread.

At the Hall of Voices, the public archivist leaves a blank beneath the new mark. Hallucination has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the listening table

Rebuild the hallucination scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 049](../049-calibration/README.md)
