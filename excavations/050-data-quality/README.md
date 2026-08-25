# Excavation 050 — Data Quality — What Lessons Did the Model Actually Receive?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Language models and useful answers

Calibration compares stated confidence with observed reliability. When those diverge, the cause often lies upstream in the lessons the model received—duplication, errors, missing groups, or misleading correlations.

A new case arrives at the Hall of Voices. Nothing yet demands a new invention, so the public archivist uses the listening table to collect as much text as possible and assume scale washes out bad examples.

This is precisely the kind of shortcut a careful builder should try first. The instruction to collect as much text as possible and assume scale washes out bad examples preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: duplicated false claims become louder, rare high-quality explanations become quieter, and sensitive records remain memorized. More observations amplify whatever process produced them.

The counterexample separates two questions that the attempt to collect as much text as possible and assume scale washes out bad examples had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the listening table fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now treat data construction as part of the model: trace provenance, remove harmful duplication, filter carefully, preserve valuable diversity, and document choices. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Data Quality**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## What Lessons Did the Model Actually Receive

A corpus contains one careful correction and 1,000 copied versions of the same false tiger fact. Counting pages makes the falsehood appear overwhelmingly supported; deduplication changes the lesson before training begins.

## Where data quality runs out

Filtering encodes human judgments and can erase minority language or useful unusual examples. Quality is task-dependent.

A final test reaches beyond the new instrument. It does not refute Data Quality; it reveals the edge of what was constructed. The public archivist carries that edge into the following room.

## Return to the listening table

Rebuild the data quality scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 051](../051-scaling-laws/README.md)
