# Excavation 132 — Knowledge Distillation — Teaching a Smaller Student

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Scientific self-improvement and oversight

Synthetic data can expand training only when errors are verified instead of multiplied. The capable teacher generating or checking those lessons may be too large and costly for deployment.

At the Academy of Trials, the experimentalist meets the next case beside the sealed evidence ledger. The nearest idea is also the most reasonable one: train a small model only on the original hard labels.

The attraction of this attempt is easy to see. To train a small model only on the original hard labels reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: the trouble appears immediately: the labels reveal the winner but discard how the teacher distributed doubt among alternatives.

The contradiction matters because it identifies a structural loss in the instruction to train a small model only on the original hard labels, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The sealed evidence ledger will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must let the student imitate the teacher's probability pattern as well as the observed answer. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Knowledge Distillation**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## Teaching a Smaller Student

For an animal image, 0.55 tiger, 0.40 leopard, 0.05 car teaches similarity that the label tiger hides.

## Where knowledge distillation runs out

The student also inherits the teacher's blind spots.

At the Academy of Trials, the experimentalist leaves a blank beneath the new mark. Knowledge Distillation has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the sealed evidence ledger

Rebuild the knowledge distillation scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [The wrong ideas worth preserving](mistakes.md); [Diagram and dependency path](diagram.md); [Invention exercises](exercises.md); [References and reading trail](references.md); and [Visual asset brief](images/README.md).

[Next: Mixture of Experts — Spending Computation Where It Helps](../133-mixture-of-experts/README.md)
