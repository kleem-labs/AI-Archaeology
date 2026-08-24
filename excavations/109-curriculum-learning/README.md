# Excavation 109 — Curriculum Learning

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Meta-learning shapes that adaptation procedure. Its success depends on which tasks and difficulties the learner encounters first; a hostile order can make useful structure unnecessarily hard to discover.

A new case arrives at the Hall of Possible Worlds, but the keeper of unfinished questions first reaches for the familiar table of mirrored maps. Its promise is simple: shuffle all examples uniformly from the beginning.

The rule survives the easy cases. The next case leaves a crack through the middle of it: early gradients from unsolved complex cases are noisy and provide little structure. More confidence cannot repair information that never entered the rule.

*The keeper of unfinished questions sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: shuffle all examples uniformly from…
possible road B ─┘              └── loses: early gradients from unsolved complex…

same roads ──▶ repaired map ──▶ order or weight examples so mastered…
```

Two trails now cross the table of mirrored maps. The pale trail bears the instruction “shuffle all examples uniformly from the beginning.” It disappears into the observed failure: early gradients from unsolved complex cases are noisy and provide little structure. The darker trail carries one additional capacity—to order or weight examples so mastered foundations support harder cases, while revisiting earlier skills. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed curriculum learning mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the table of mirrored maps is altered in exactly one way: order or weight examples so mastered foundations support harder cases, while revisiting earlier skills. Much later, people will call this territory **Curriculum Learning**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the table of mirrored maps. The failed path remains visible beneath the repair, because curriculum learning is easier to remember when its scar remains attached to it. The scar reads, ‘early gradients from unsolved complex cases are noisy and provide little structure’; the new line exists only to keep that loss from happening again.

## Understanding curriculum learning

Learn clear single-animal images before crowded camouflage scenes.

## Where curriculum learning runs out

A poor curriculum can delay useful diversity or teach shortcuts.

The table of mirrored maps answers today's question and falls silent at the next. That silence is precise: Curriculum Learning was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the table of mirrored maps

Rebuild the curriculum learning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 110](../110-self-supervised-learning/README.md)
