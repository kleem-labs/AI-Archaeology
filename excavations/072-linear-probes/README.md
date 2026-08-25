# Excavation 072 — Linear Probes

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Learning in the world and interpretability

Internal-feature analysis asks what distinctions a hidden layer already makes. A simple probe may decode “tiger” from that layer, but decodability does not prove the original model uses that information.

At the Living Watchgarden, the field naturalist meets the next case beside the weathered observation slate. The nearest idea is also the most reasonable one: train a powerful classifier on hidden states and call any success evidence.

The attraction of this attempt is easy to see. To train a powerful classifier on hidden states and call any success evidence reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: the trouble appears immediately: the probe learns the task itself even if the representation did not make it simple.

The contradiction matters because it identifies a structural loss in the instruction to train a powerful classifier on hidden states and call any success evidence, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The weathered observation slate will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must use a deliberately limited probe and compare layers, controls, and baselines. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Linear Probes**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## Understanding linear probes

A linear probe succeeds at layer 8 but random-label controls fail, suggesting species became linearly accessible there.

## Where linear probes runs out

Decodable information is not proof the model uses it.

At the Living Watchgarden, the field naturalist leaves a blank beneath the new mark. Linear Probes has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the weathered observation slate

Rebuild the linear probes scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 073](../073-attribution/README.md)
