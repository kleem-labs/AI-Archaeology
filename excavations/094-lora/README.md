# Excavation 094 — Low-Rank Adaptation

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Audio models extend the assistant's senses and enlarge the already expensive system. Adapting the whole model for each ranger station, language, or task would duplicate billions of parameters.

The doors of the Road of Consequences close against the wind. On the map of branching journeys, the expedition leader writes the cheapest rule that might still be true: copy and fine-tune all parameters for every task.

The expedition leader repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: storage and training cost multiply, and the base model is harder to preserve. The failure is stable enough to become evidence.

*The expedition leader sketches the break before changing it:*

```text
observation
    │
    ▼
[copy and fine-tune all parameters for…]
    │
    ╳  storage and training cost multiply,…
    │
    ▼
[freeze the base and learn a small…]
```

Across the map of branching journeys, the old path and the repaired path run side by side. One carries “copy and fine-tune all parameters for every task”; the other knows how to freeze the base and learn a small low-rank correction to selected matrices. When the failure—storage and training cost multiply, and the base model is harder to preserve—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to low-rank adaptation. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: freeze the base and learn a small low-rank correction to selected matrices. This problem and its repair will travel under the name **Low-Rank Adaptation**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—copy and fine-tune all parameters for every task? The answer remains storage and training cost multiply, and the base model is harder to preserve. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

<!-- memory-film-v1:start -->
> **Memory realm 9 of 18 — [Road of Consequences](../../MEMORY_PALACE.md#realm-9)**
>
> **The question carried into this chamber:** What fails if we copy and fine-tune all parameters for every task?

## When the chamber changes

The mathematical name Low-Rank Adaptation can now rest. What matters is whether its transformation remains visible.

First hold the failed picture still: The gear follows the tempting path—copy and fine-tune all parameters for every task. Then the evidence answers: storage and training cost multiply, and the base model is harder to preserve.

Now let the chamber move: The expedition leader changes one moving part. The gear can now freeze the base and learn a small low-rank correction to selected matrices.

The object that should remain after the terminology disappears is **the low-rank adaptation gear mounted on the map of branching journeys**.

> **Memory seal — Low-Rank Adaptation**
>
> Low-Rank Adaptation keeps the missing power: freeze the base and learn a small low-rank correction to selected matrices.

Give the idea a bodily path: Touch the low-rank adaptation gear in imagination: make a narrow gate with both hands, block the old path, then open only the route the evidence permits.
<!-- memory-film-v1:end -->

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

Cover the prose about low-rank adaptation and each mark can still be recovered from the case. Only now is the compressed form safe to write:

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
