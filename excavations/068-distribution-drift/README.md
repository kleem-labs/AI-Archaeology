# Excavation 068 — Distribution Drift

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Learning in the world and interpretability

Online learning adapts quickly and can also absorb noise or attack just as quickly. The system must first distinguish ordinary variation from a genuine change in the source producing its inputs.

At the Living Watchgarden, the field naturalist meets the next case beside the weathered observation slate. The nearest idea is also the most reasonable one: assume training accuracy remains valid forever.

The attraction of this attempt is easy to see. To assume training accuracy remains valid forever reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: a winter-trained demand model meets summer behavior and keeps reporting confident old patterns.

The contradiction matters because it identifies a structural loss in the instruction to assume training accuracy remains valid forever, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The weathered observation slate will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Distribution Drift**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## Understanding distribution drift

Average order size moves from $40 to $75 while error doubles. The shift is evidence to inspect, not automatic permission to update.

## Where distribution drift runs out

Not every statistical shift changes the decision that matters.

A final test reaches beyond the new instrument. It does not refute Distribution Drift; it reveals the edge of what was constructed. The field naturalist carries that edge into the following room.

## Return to the weathered observation slate

Rebuild the distribution drift scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 069](../069-controlled-experiments/README.md)
