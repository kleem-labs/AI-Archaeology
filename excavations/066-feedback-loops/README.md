# Excavation 066 — Feedback Loops

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Learning in the world and interpretability

> **PART VII — LEARNING AFTER DEPLOYMENT**
>
> The laboratory door opens onto a changing world. Now the system influences the very evidence from which it learns.

The field assistant is now bounded, observable, and deployed. Its recommendations change what people see and choose, so today's behavior alters the data that will be treated as evidence tomorrow.

A new case arrives at the Living Watchgarden. Nothing yet demands a new invention, so the field naturalist uses the weathered observation slate to treat every click as independent evidence of natural preference.

This is precisely the kind of shortcut a careful builder should try first. The instruction to treat every click as independent evidence of natural preference preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: show one song repeatedly; its extra clicks now appear to prove it deserved repetition.

The counterexample separates two questions that the attempt to treat every click as independent evidence of natural preference had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the weathered observation slate fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now record how the system influenced each observation and evaluate outcomes against a control or exploration policy. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Feedback Loops**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Understanding feedback loops

Two equal songs begin with ten listeners each. The agent promotes A to ninety more people; A receives more clicks because it received more chances, not necessarily because it was better.

## Where feedback loops runs out

Feedback can create self-fulfilling popularity and erase unexposed alternatives.

At the Living Watchgarden, the field naturalist leaves a blank beneath the new mark. Feedback Loops has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the weathered observation slate

Rebuild the feedback loops scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 067](../067-online-learning/README.md)
