# Excavation 052 — Instruction Tuning — From Continuation to Cooperation

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Information Theory](../../MATHEMATICS_ATLAS.md#information)
>
> **Applied territory:** Language models and useful answers

Scaling laws reveal regular trends as resources grow. A larger next-token predictor is still a predictor; nothing in scale alone tells it that a user's instruction should govern the continuation.

Inside the Hall of Voices, every old tool is given one honest chance. The public archivist sets the listening table between the evidence and the desired answer, then tries to prompt more forcefully and hope next-token prediction infers the desired interaction.

The public archivist repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: the trouble appears immediately: given “Translate cat to French,” raw continuation may produce more translation examples, commentary, or unrelated web text. Pretraining learned many formats, not one cooperative policy. The failure is stable enough to become evidence.

*The public archivist sketches the break before changing it:*

```text
OLD PATH:  request ──▶ prompt more forcefully and hope… ──▶ the trouble appears immediately:…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ show many instruction-input-response… ──▶ accountable result
```

Across the listening table, the old path and the repaired path run side by side. One carries “prompt more forcefully and hope next-token prediction infers the desired interaction”; the other knows how to show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern. When the failure—the trouble appears immediately: given “Translate cat to French,” raw continuation may produce more translation examples, commentary, or unrelated web text. Pretraining learned many formats, not one cooperative policy—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to instruction tuning. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern. This problem and its repair will travel under the name **Instruction Tuning**, but the name carries no knowledge the scene has not earned.

What changed on the listening table can be said without symbols. Before, the method could only prompt more forcefully and hope next-token prediction infers the desired interaction; now it can also show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

## From Continuation to Cooperation

Training examples pair “Summarize: [paragraph]” with a concise summary and “Classify sentiment: [review]” with a label. A new instruction can reuse the demonstrated relation between request and response.

## Where instruction tuning runs out

Instruction tuning teaches behavioral patterns from its examples; it does not guarantee truth, safety, or correct obedience to every request.

The instruction tuning repair holds, but the world asks for something it was never given. At the Hall of Voices, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the listening table

Rebuild the instruction tuning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 053](../053-preference-learning/README.md)
