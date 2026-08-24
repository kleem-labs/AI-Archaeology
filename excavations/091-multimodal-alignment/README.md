# Excavation 091 — Multimodal Alignment

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Policy gradients let consequences reshape action probabilities. The field system's words, images, and actions still live in separate representational worlds unless paired observations can teach them to meet.

Night gathers around the Road of Consequences. Under the light of the map of branching journeys, the expedition leader refuses to invent prematurely and begins with the plain rule: compare raw pixels directly with token IDs.

The rule survives the easy cases. The next case leaves a crack through the middle of it: their coordinates have unrelated meanings and shapes. More confidence cannot repair information that never entered the rule.

*The expedition leader sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ compare raw pixels directly with… ──▶ blurred: their coordinates have unrelated…
      │
      └── new lens ──▶ we need to use separate encoders and… ──▶ distinction survives
```

Two trails now cross the map of branching journeys. The pale trail bears the instruction “compare raw pixels directly with token IDs.” It disappears into the observed failure: their coordinates have unrelated meanings and shapes. The darker trail carries one additional capacity—to use separate encoders and train paired image-text examples to become nearby. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed multimodal alignment mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the map of branching journeys is altered in exactly one way: we need to use separate encoders and train paired image-text examples to become nearby. Much later, people will call this territory **Multimodal Alignment**. Here the name is only a memory of the failure it can survive.

The map of branching journeys has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and multimodal alignment looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.


Before leaving the map of branching journeys, the expedition leader tests the new idea backward. Remove the ability to use separate encoders and train paired image-text examples to become nearby, and the method falls back to this tempting instruction: compare raw pixels directly with token IDs. The old consequence returns—their coordinates have unrelated meanings and shapes. Restore the missing ability and that particular contradiction disappears. This reversible test is why multimodal alignment belongs to the growing structure rather than to a list of facts to memorize.

## Understanding multimodal alignment

A tiger photo and “striped big cat” move together; mismatched captions move apart.

## Where multimodal alignment runs out

Pairs can contain weak, biased, or incomplete descriptions.

The map of branching journeys answers today's question and falls silent at the next. That silence is precise: Multimodal Alignment was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the map of branching journeys

Rebuild the multimodal alignment scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 092](../092-contrastive-learning/README.md)
