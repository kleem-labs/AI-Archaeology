# Excavation 128 — Reproducibility — Can the Discovery Survive Another Run?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Scientific self-improvement and oversight

Experimental design isolates one suspected cause and provides a control. A single successful run can still be a favorable random seed rather than a discovery that will survive repetition.

At the Academy of Trials, the experimentalist meets the next case beside the sealed evidence ledger. The nearest idea is also the most reasonable one: keep the best checkpoint and report its score.

The attraction of this attempt is easy to see. To keep the best checkpoint and report its score reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: changing only the random seed makes the gain disappear.

The contradiction matters because it identifies a structural loss in the instruction to keep the best checkpoint and report its score, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The sealed evidence ledger will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must record code, data, configuration, environment, seeds, and variation across repeated runs. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Reproducibility**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## Can the Discovery Survive Another Run

Run five seeds; compare the distribution of gains rather than celebrating the luckiest one.

## Where reproducibility runs out

Repeated agreement does not remove a shared bias in all runs.

A final test reaches beyond the new instrument. It does not refute Reproducibility; it reveals the edge of what was constructed. The experimentalist carries that edge into the following room.

## Return to the sealed evidence ledger

Rebuild the reproducibility scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [The wrong ideas worth preserving](mistakes.md); [Diagram and dependency path](diagram.md); [Invention exercises](exercises.md); [References and reading trail](references.md); and [Visual asset brief](images/README.md).

[Next: Benchmarks — Building a Ruler Before Measuring Progress](../129-benchmarks/README.md)
