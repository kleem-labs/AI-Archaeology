# Excavation 102 — Bayesian Updating

<!-- book-prose-v2 -->

Separating uncertainty in the observation from uncertainty in the model's knowledge tells us what kind of ignorance we face. New evidence must then revise several plausible stories without erasing what was believed before it arrived.

The obvious economy is to discard the old belief and use only the newest clue.

The proposal deserves a fair hearing. For bayesian updating, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The decisive test is this: the trouble appears immediately: one noisy footprint can overpower years of evidence.

The failure changes the question behind bayesian updating. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: combine prior plausibility with how expected the clue is under each story, then normalize across stories.

Only at this point does the inherited name **Bayesian Updating** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of bayesian updating by mentally removing the repair. We fall back to the proposal to discard the old belief and use only the newest clue; then the trouble appears immediately: one noisy footprint can overpower years of evidence. Restore only the ability to combine prior plausibility with how expected the clue is under each story, then normalize across stories, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to discard the old belief and use only the newest clue to requiring the system to combine prior plausibility with how expected the clue is under each story, then normalize across stories. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to bayesian updating.

## Understanding bayesian updating

Tiger starts at 10%, but a deep paw print is far more likely under tiger than wind; the belief rises without becoming certainty.

Put the old procedure beside bayesian updating. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## The calculation hidden inside bayesian updating

Do not read the coming Bayesian Updating line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Before seeing tracks, a ranger considers tiger less common than deer: perhaps tiger receives prior share 1 and deer share 4. A deep round print is far more expected under tiger—say likelihood 8—than deer—say likelihood 1. Multiplying gives supports 8 for tiger and 4 for deer. Dividing each by total support 12 turns them into revised shares: two thirds tiger, one third deer. The print overcame the prior, but did not erase it.

Tiger’s prior belief is its share before the footprint.
The footprint likelihood says how expected this exact clue is if tiger is true.
Multiplying gives tiger’s unnormalized support.
The denominator repeats that multiplication for every story and adds them so final beliefs total one.

### Why no cheaper operation does the same job

[Likelihood times prior](../../MATHEMATICAL_MOVES.md#multiplication) requires a story to have both earlier plausibility and support from the new footprint. Addition would let overwhelming prior belief compensate linearly for evidence impossible under that story.
[The denominator sums support](../../MATHEMATICAL_MOVES.md#summation) over every competing story to find the whole amount of belief available.
[Division by that total](../../MATHEMATICAL_MOVES.md#division) turns each story's support into a share summing to one, while [the conditional bars](../../MATHEMATICAL_MOVES.md#conditional-bar) keep “evidence given story” distinct from “story after evidence.”

Every symbol in Bayesian Updating can now be read back into an action already performed. The whole procedure fits in one line:

$$
P(H\mid E)=\frac{P(E\mid H)P(H)}{\sum_j P(E\mid H_j)P(H_j)}
$$

## Where bayesian updating runs out

Results depend on priors and likelihood assumptions.

The limit follows from the job assigned to bayesian updating. Its repair knows how to combine prior plausibility with how expected the clue is under each story, then normalize across stories. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take bayesian updating to the workbench

A claim about bayesian updating now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running bayesian updating, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the bayesian updating result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 103](../103-ensembles/README.md)
