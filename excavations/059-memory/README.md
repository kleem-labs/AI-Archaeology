# Excavation 059 — Memory — What Should Survive After the Context Ends?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Agents and reliable action

Planning turns a goal into steps the agent can inspect and revise. A plan that outlives the current context needs selected facts and decisions to survive without preserving every irrelevant token forever.

Inside the Gatehouse of Consequences, the old method is given an honest chance. The gatekeeper places the evidence on the iron threshold and tries to store every message forever and paste all history into every new prompt.

Nothing about this first move is careless. To store every message forever and paste all history into every new prompt is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: cost grows, irrelevant details drown current evidence, contradictions accumulate, and sensitive information persists without purpose.

The important discovery is not merely that trying to store every message forever and paste all history into every new prompt failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the iron threshold, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to separate short-term working context from durable memory. Store only useful facts with source, time, scope, and a way to update or forget them. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Memory**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## What Should Survive After the Context Ends

Save “prefers concise status reports” with its source and date. Do not save a temporary hotel door code. Retrieve the preference only for relevant writing tasks.

Memory earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

## Where memory runs out

Remembered facts can become stale or wrong. Memory needs consent, provenance, expiration, correction, and deletion.

Here the new path ends honestly. Memory can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the iron threshold

Rebuild the memory scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 060](../060-state-machines/README.md)
