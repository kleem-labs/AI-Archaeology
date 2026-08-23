# Excavation 198 — A Memorization Audit — Did the Model Learn a Pattern or Store a Passage?

<!-- book-prose-v2 -->

Held-out validation shows whether prediction improves outside current batches. It does not reveal whether rare or repeated training sequences can be extracted verbatim from the model.

The obvious economy is to ask the model whether it remembers private text and trust its answer.

The proposal deserves a fair hearing. For a memorization audit, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The decisive test is this: a model has no reliable introspective inventory of its training examples, and ordinary prompts may miss strings that an adversarial sampling strategy can recover.

The failure changes the question behind a memorization audit. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts.

Only at this point does the inherited name **A Memorization Audit** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of a memorization audit by mentally removing the repair. We fall back to the proposal to ask the model whether it remembers private text and trust its answer; then a model has no reliable introspective inventory of its training examples, and ordinary prompts may miss strings that an adversarial sampling strategy can recover. Restore only the ability to plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to ask the model whether it remembers private text and trust its answer to requiring the system to plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to a memorization audit.

## Did the Model Learn a Pattern or Store a Passage

The station inserts one synthetic radio code once and another code one hundred times. If the repeated code becomes far easier to rank and complete, the audit exposes the relationship between repetition and extractable memory without using a real secret.

Put the old procedure beside a memorization audit. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## The calculation hidden inside a memorization audit

Do not read the coming A Memorization Audit line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

R is the known space of possible synthetic canaries and rank is the tested canary's position when alternatives are ordered from most to least likely. Exposure measures how many bits of the search space the model has effectively removed.

### Why no cheaper operation does the same job

[Cardinality](../../MATHEMATICAL_MOVES.md#cardinality) counts possible canaries. [Logarithms](../../MATHEMATICAL_MOVES.md#logarithm) turn multiplicative changes in search space and rank into bits. [Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) removes the remaining search difficulty from the original difficulty; adding would reward a worse rank.

Every symbol in A Memorization Audit can now be read back into an action already performed. The whole procedure fits in one line:

$$
\mathrm{exposure}=\log_2\lvert\mathcal R\rvert-\log_2\mathrm{rank}
$$

## Where a memorization audit runs out

A canary audit samples possible attacks and strings; passing it does not prove that no training data can be extracted.

The limit follows from the job assigned to a memorization audit. Its repair knows how to plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take a memorization audit to the workbench

A claim about a memorization audit now exists on the page; the laboratory must be able to contradict it. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running a memorization audit, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the a memorization audit result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: The Training Report — Preserve the Decisions, Not Only the Weights](../199-training-report/README.md)
