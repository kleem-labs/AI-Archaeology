# Excavation 052 — Instruction Tuning — From Continuation to Cooperation

<!-- book-prose-v2 -->

Scaling laws reveal regular trends as resources grow. A larger next-token predictor is still a predictor; nothing in scale alone tells it that a user's instruction should govern the continuation.

If the old idea can be stretched one step farther, we should prompt more forcefully and hope next-token prediction infers the desired interaction.

If the proposal works on every relevant case, instruction tuning is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The proposal breaks for a specific reason, not by authority: the trouble appears immediately: given “Translate cat to French,” raw continuation may produce more translation examples, commentary, or unrelated web text. Pretraining learned many formats, not one cooperative policy.

Nothing magical creates instruction tuning. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern.

This boundary between the failed rule and its repair is the subject later work calls **Instruction Tuning**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize instruction tuning; try to break it by subtraction. Remove the part that knows how to show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern, leaving only the attempt to prompt more forcefully and hope next-token prediction infers the desired interaction. What returns is not a vague weakness but the original contradiction: the trouble appears immediately: given “Translate cat to French,” raw continuation may produce more translation examples, commentary, or unrelated web text. Pretraining learned many formats, not one cooperative policy. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to prompt more forcefully and hope next-token prediction infers the desired interaction receives the same test as the rule to show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern. Their different outcomes reveal what instruction tuning contributes without asking the reader to trust historical convention.

## From Continuation to Cooperation

Training examples pair “Summarize: [paragraph]” with a concise summary and “Classify sentiment: [review]” with a label. A new instruction can reuse the demonstrated relation between request and response.

Hold the setting, evidence, and desired outcome fixed while testing instruction tuning. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

## Where instruction tuning runs out

Instruction tuning teaches behavioral patterns from its examples; it does not guarantee truth, safety, or correct obedience to every request.

This is where instruction tuning runs out for a causal reason. We gave it enough structure to show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

## Take instruction tuning to the workbench

A mathematical story about instruction tuning earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running instruction tuning, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the instruction tuning result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 053](../053-preference-learning/README.md)
