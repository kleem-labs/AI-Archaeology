# Excavation 102 — Bayesian Updating

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Continual learning, reasoning, and research

Separating uncertainty in the observation from uncertainty in the model's knowledge tells us what kind of ignorance we face. New evidence must then revise several plausible stories without erasing what was believed before it arrived.

The doors of the Hall of Possible Worlds close against the wind. On the table of mirrored maps, the keeper of unfinished questions writes the cheapest rule that might still be true: discard the old belief and use only the newest clue.

For a moment the mark looks complete. Then the evidence refuses to fit: the trouble appears immediately: one noisy footprint can overpower years of evidence. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The keeper of unfinished questions sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ discard the old belief and use only… ──▶ blurred: the trouble appears immediately: one…
      │
      └── new lens ──▶ combine prior plausibility with how… ──▶ distinction survives
```

The keeper of unfinished questions lays two translucent sheets over the table of mirrored maps. The first is inscribed, “discard the old belief and use only the newest clue.” Its path ends where the trouble appears immediately: one noisy footprint can overpower years of evidence. The second receives the same evidence but is allowed to combine prior plausibility with how expected the clue is under each story, then normalize across stories. Held to the light, the sheets separate at exactly one decision.

No one reaches for a bayesian updating formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The keeper of unfinished questions changes only that one responsibility: combine prior plausibility with how expected the clue is under each story, then normalize across stories. When the ink dries, the name **Bayesian Updating** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because the trouble appears immediately: one noisy footprint can overpower years of evidence, while the other can combine prior plausibility with how expected the clue is under each story, then normalize across stories. That fork—not the vocabulary—is where bayesian updating lives.

<!-- memory-film-v1:start -->
> **Memory realm 10 of 18 — [Hall of Possible Worlds](../../MEMORY_PALACE.md#realm-10)**
>
> **The question carried into this chamber:** What fails if we discard the old belief and use only the newest clue?

## When the chamber changes

The Bayesian Updating chamber leaves one scene behind so the idea can be recovered after its symbols fade.

First hold the failed picture still: The thread follows the tempting path—discard the old belief and use only the newest clue. Then the evidence answers: the trouble appears immediately: one noisy footprint can overpower years of evidence.

Now let the chamber move: The keeper of unfinished questions changes one moving part. The thread can now combine prior plausibility with how expected the clue is under each story, then normalize across stories.

The object that should remain after the terminology disappears is **the bayesian updating thread mounted on the table of mirrored maps**.

> **Memory seal — Bayesian Updating**
>
> Bayesian Updating keeps the missing power: combine prior plausibility with how expected the clue is under each story, then normalize across stories.

Give the idea a bodily path: Touch the bayesian updating thread in imagination: make a narrow gate with both hands, block the old path, then open only the route the evidence permits.
<!-- memory-film-v1:end -->

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
