# Excavation 094 — Low-Rank Adaptation

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Audio models extend the assistant's senses and enlarge the already expensive system. Adapting the whole model for each ranger station, language, or task would duplicate billions of parameters.

A new case arrives at the Road of Consequences. Nothing yet demands a new invention, so the expedition leader uses the map of branching journeys to copy and fine-tune all parameters for every task.

This is precisely the kind of shortcut a careful builder should try first. The instruction to copy and fine-tune all parameters for every task preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: storage and training cost multiply, and the base model is harder to preserve.

The counterexample separates two questions that the attempt to copy and fine-tune all parameters for every task had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the map of branching journeys fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now freeze the base and learn a small low-rank correction to selected matrices. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Low-Rank Adaptation**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Understanding low-rank adaptation

Instead of a million-value update, two narrow matrices produce a constrained correction with far fewer trainable values.

## The calculation hidden inside low-rank adaptation

The expedition leader carries the low-rank adaptation scene to the map of branching journeys. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A large language model already knows general English, but a park service needs it to understand a small set of ranger report conventions. Copying and changing its entire transformation matrix would be expensive. Instead, freeze the original map and learn two narrow maps: one compresses a report into a few adaptation directions, and the other expands those directions back into a correction with the original shape. Adding that correction preserves the base map while bending it toward ranger language.

W is the frozen large matrix we refuse to duplicate.
A and B are the two narrow trainable matrices.
Their product BA creates a full-shaped correction while using far fewer values.
Addition preserves the base behavior and applies only the learned adaptation.

### Why the melody needs these exact notes

[BA](../../MATHEMATICAL_MOVES.md#multiplication) composes two narrow learned transformations, forcing the correction through a low-dimensional bottleneck instead of learning every entry of a full matrix.
[Adding that correction to W](../../MATHEMATICAL_MOVES.md#addition) preserves the pretrained base and treats adaptation as a change. [The prime on W](../../MATHEMATICAL_MOVES.md#symbol-decorations) marks the adapted version; replacing W would discard the knowledge we intended to keep.

The mandala has curved back upon itself. In this chamber we meet **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the joining river**—separate contributions meet without losing where they came from. What seemed like a new formula is older mathematical instinct arranged around a new need.

Every mark in the coming low-rank adaptation equation now belongs to a visible part of the case. The compressed form is:

$$
W^\prime=W+BA
$$

## Where low-rank adaptation runs out

Low rank may be insufficient for large behavioral changes.

The low-rank adaptation repair holds, but the world asks for something it was never given. At the Road of Consequences, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the map of branching journeys

Rebuild the low-rank adaptation scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 095](../095-quantization/README.md)
