# Excavation 102 — Bayesian Updating

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Continual learning, reasoning, and research

Separating uncertainty in the observation from uncertainty in the model's knowledge tells us what kind of ignorance we face. New evidence must then revise several plausible stories without erasing what was believed before it arrived.

A new case arrives at the Hall of Possible Worlds. Nothing yet demands a new invention, so the keeper of unfinished questions uses the table of mirrored maps to discard the old belief and use only the newest clue.

This is precisely the kind of shortcut a careful builder should try first. The instruction to discard the old belief and use only the newest clue preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: the trouble appears immediately: one noisy footprint can overpower years of evidence.

The counterexample separates two questions that the attempt to discard the old belief and use only the newest clue had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the table of mirrored maps fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now combine prior plausibility with how expected the clue is under each story, then normalize across stories. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Bayesian Updating**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Understanding bayesian updating

Tiger starts at 10%, but a deep paw print is far more likely under tiger than wind; the belief rises without becoming certainty.

## The calculation hidden inside bayesian updating

The keeper of unfinished questions carries the bayesian updating scene to the table of mirrored maps. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Before seeing tracks, a ranger considers tiger less common than deer: perhaps tiger receives prior share 1 and deer share 4. A deep round print is far more expected under tiger—say likelihood 8—than deer—say likelihood 1. Multiplying gives supports 8 for tiger and 4 for deer. Dividing each by total support 12 turns them into revised shares: two thirds tiger, one third deer. The print overcame the prior, but did not erase it.

Tiger’s prior belief is its share before the footprint.
The footprint likelihood says how expected this exact clue is if tiger is true.
Multiplying gives tiger’s unnormalized support.
The denominator repeats that multiplication for every story and adds them so final beliefs total one.

### Why the melody needs these exact notes

[Likelihood times prior](../../MATHEMATICAL_MOVES.md#multiplication) requires a story to have both earlier plausibility and support from the new footprint. Addition would let overwhelming prior belief compensate linearly for evidence impossible under that story.
[The denominator sums support](../../MATHEMATICAL_MOVES.md#summation) over every competing story to find the whole amount of belief available.
[Division by that total](../../MATHEMATICAL_MOVES.md#division) turns each story's support into a share summing to one, while [the conditional bars](../../MATHEMATICAL_MOVES.md#conditional-bar) keep “evidence given story” distinct from “story after evidence.”

The mandala has curved back upon itself. In this chamber we meet **the lock and key**—one influence matters through another, and either missing factor can close the path; **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. What seemed like a new formula is older mathematical instinct arranged around a new need.

Every mark needed for bayesian updating is now visible on the table of mirrored maps. The symbols do not add an idea; they bind the discovered moves into one line:

$$
P(H\mid E)=\frac{P(E\mid H)P(H)}{\sum_j P(E\mid H_j)P(H_j)}
$$

## Where bayesian updating runs out

Results depend on priors and likelihood assumptions.

At the Hall of Possible Worlds, the keeper of unfinished questions leaves a blank beneath the new mark. Bayesian Updating has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the table of mirrored maps

Rebuild the bayesian updating scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 103](../103-ensembles/README.md)
