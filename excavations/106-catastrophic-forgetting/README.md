# Excavation 106 — Catastrophic Forgetting

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Continual learning, reasoning, and research

Selective prediction gives the system permission to abstain. When an approved new task finally supplies more training data, learning it can overwrite skills that were reliable yesterday.

The table of mirrored maps at the Hall of Possible Worlds still carries the marks of the previous discovery. The keeper of unfinished questions follows them as far as they seem willing to go: fine-tune only on the newest data.

The keeper of unfinished questions repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: updates useful for B overwrite weights carrying A. The failure is stable enough to become evidence.

*The keeper of unfinished questions sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   fine-tune only on the newest data updates useful for B overwrite…
            \        /
             \      /
              rehearse old evidence, protect…
```

Across the table of mirrored maps, the old path and the repaired path run side by side. One carries “fine-tune only on the newest data”; the other knows how to rehearse old evidence, protect important parameters, or allocate new capacity. When the failure—updates useful for B overwrite weights carrying A—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to catastrophic forgetting. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: rehearse old evidence, protect important parameters, or allocate new capacity. This problem and its repair will travel under the name **Catastrophic Forgetting**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—fine-tune only on the newest data? The answer remains updates useful for B overwrite weights carrying A. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.


Before leaving the table of mirrored maps, the keeper of unfinished questions tests the new idea backward. Remove the ability to rehearse old evidence, protect important parameters, or allocate new capacity, and the method falls back to this tempting instruction: fine-tune only on the newest data. The old consequence returns—updates useful for B overwrite weights carrying A. Restore the missing ability and that particular contradiction disappears. This reversible test is why catastrophic forgetting belongs to the growing structure rather than to a list of facts to memorize.

## Understanding catastrophic forgetting

Learning birds after mammals drops mammal accuracy; mixing a small mammal replay set preserves both.

## Where catastrophic forgetting runs out

Memory, privacy, and capacity limit rehearsal.

The catastrophic forgetting repair holds, but the world asks for something it was never given. At the Hall of Possible Worlds, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the table of mirrored maps

Rebuild the catastrophic forgetting scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 107](../107-continual-learning/README.md)
