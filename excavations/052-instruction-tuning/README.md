# Excavation 052 — Instruction Tuning — From Continuation to Cooperation

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Information Theory](../../MATHEMATICS_ATLAS.md#information)
>
> **Applied territory:** Language models and useful answers

Scaling laws reveal regular trends as resources grow. A larger next-token predictor is still a predictor; nothing in scale alone tells it that a user's instruction should govern the continuation.

At the Hall of Voices, the public archivist meets the next case beside the listening table. The nearest idea is also the most reasonable one: prompt more forcefully and hope next-token prediction infers the desired interaction.

The attraction of this attempt is easy to see. To prompt more forcefully and hope next-token prediction infers the desired interaction reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: the trouble appears immediately: given “Translate cat to French,” raw continuation may produce more translation examples, commentary, or unrelated web text. Pretraining learned many formats, not one cooperative policy.

The contradiction matters because it identifies a structural loss in the instruction to prompt more forcefully and hope next-token prediction infers the desired interaction, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The listening table will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Instruction Tuning**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## From Continuation to Cooperation

Training examples pair “Summarize: [paragraph]” with a concise summary and “Classify sentiment: [review]” with a label. A new instruction can reuse the demonstrated relation between request and response.

## Where instruction tuning runs out

Instruction tuning teaches behavioral patterns from its examples; it does not guarantee truth, safety, or correct obedience to every request.

The instruction tuning repair holds, but the world asks for something it was never given. At the Hall of Voices, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the listening table

Rebuild the instruction tuning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 053](../053-preference-learning/README.md)
