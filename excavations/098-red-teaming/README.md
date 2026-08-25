# Excavation 098 — Red Teaming

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Inference serving turns a trained artifact into a live service. Ordinary validation rarely includes adversarial prompts, unusual tool sequences, resource exhaustion, or users deliberately searching for failure.

A new case arrives at the Road of Consequences. Nothing yet demands a new invention, so the expedition leader uses the map of branching journeys to evaluate only expected well-formed requests.

This is precisely the kind of shortcut a careful builder should try first. The instruction to evaluate only expected well-formed requests preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: real users, attackers, and accidents find paths designers never listed.

The counterexample separates two questions that the attempt to evaluate only expected well-formed requests had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the map of branching journeys fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now actively search for failures, record reproducible cases, and turn discoveries into regression tests and mitigations. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Red Teaming**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Understanding red teaming

A hidden instruction in a retrieved page bypasses a normal demo; the case becomes a permanent injection test.

## Where red teaming runs out

No finite red team proves universal safety.

A final test reaches beyond the new instrument. It does not refute Red Teaming; it reveals the edge of what was constructed. The expedition leader carries that edge into the following room.

## Return to the map of branching journeys

Rebuild the red teaming scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 099](../099-governance/README.md)
