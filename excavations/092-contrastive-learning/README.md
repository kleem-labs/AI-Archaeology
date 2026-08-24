# Excavation 092 — Contrastive Learning

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Multimodal alignment places an image near its matching caption. Pulling pairs together alone permits every pair to collapse to the same point; meaning appears only when the correct match wins against plausible alternatives.

Inside the Road of Consequences, every old tool is given one honest chance. The expedition leader sets the map of branching journeys between the evidence and the desired answer, then tries to pull every observed pair together without negatives.

Reality answers without terminology: the trouble appears immediately: all representations can collapse to one point. The map of branching journeys now holds two situations the old rule cannot keep apart.

*The expedition leader sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: pull every observed pair together…
possible road B ─┘              └── loses: the trouble appears immediately: all…

same roads ──▶ repaired map ──▶ compare each true pair against…
```

The map of branching journeys is divided down the middle. Left side: “pull every observed pair together without negatives.” Its final mark records the trouble appears immediately: all representations can collapse to one point. Right side: the same starting evidence, now allowed to compare each true pair against mismatched alternatives in the same batch. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given contrastive learning a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: compare each true pair against mismatched alternatives in the same batch. The name **Contrastive Learning** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to pull every observed pair together without negatives; on the other lies the observed fact that the trouble appears immediately: all representations can collapse to one point. The bridge called contrastive learning has exactly the planks needed to compare each true pair against mismatched alternatives in the same batch.

<!-- memory-film-v1:start -->
> **Memory realm 9 of 18 — [Road of Consequences](../../MEMORY_PALACE.md#realm-9)**
>
> **The question carried into this chamber:** What fails if we pull every observed pair together without negatives?

## When the chamber changes

The Contrastive Learning chamber leaves one scene behind so the idea can be recovered after its symbols fade.

First hold the failed picture still: The map follows the tempting path—pull every observed pair together without negatives. Then the evidence answers: the trouble appears immediately: all representations can collapse to one point.

Now let the chamber move: The expedition leader changes one moving part. The map can now compare each true pair against mismatched alternatives in the same batch.

The object that should remain after the terminology disappears is **the contrastive learning map mounted on the map of branching journeys**.

> **Memory seal — Contrastive Learning**
>
> Contrastive Learning keeps the missing power: compare each true pair against mismatched alternatives in the same batch.

Give the idea a bodily path: Touch the contrastive learning map in imagination: point backward to the failed attempt, touch the present object, then point forward through the repair.
<!-- memory-film-v1:end -->

## Understanding contrastive learning

One tiger image chooses its caption among 31 wrong captions; success requires relative alignment.

## The calculation hidden inside contrastive learning

The expedition leader carries the contrastive learning scene to the map of branching journeys. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Place four wildlife photographs beside four captions. The tiger photograph should prefer “a striped predator” over “a river,” “a truck,” and “a sleeping dog.” Pulling only the correct pair together is insufficient: every photograph and caption could collapse to the same location. Making the tiger compete against all candidate captions forces its correct caption to be closer *relative to the alternatives*.

zi and ti are the matched image and text vectors.
Their dot product is the named alignment score.
Temperature T controls how sharply alternatives compete.
The denominator includes every candidate caption, preventing all examples from collapsing to one point.
The negative log penalizes the true pair when mismatches receive comparable scores.

### Why the melody needs these exact notes

[Each dot product](../../MATHEMATICAL_MOVES.md#dot-product) measures aligned agreement between one image representation and one candidate text representation.
[Dividing by temperature](../../MATHEMATICAL_MOVES.md#division) controls how strongly score gaps matter before [exponentiation](../../MATHEMATICAL_MOVES.md#exponential) converts them into positive relative weights.
[The denominator sum](../../MATHEMATICAL_MOVES.md#summation) makes the correct pair compete against all candidates, preventing every representation from winning by collapsing to one point.
[Negative log](../../MATHEMATICAL_MOVES.md#logarithm) turns the correct pair's probability share into additive cost and punishes confident preference for the wrong match.

Inside contrastive learning, familiar operations return with stricter duties: **the meeting of arrows**—matching directions reinforce while opposing directions resist; **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; and **the rising flame**—a small score difference becomes positive relative evidence. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Nothing remains unnamed in the contrastive learning case on the map of branching journeys. We can finally trade the long route for its compact map:

$$
L_i=-\log\frac{\exp(z_i\cdot t_i/T)}{\sum_j\exp(z_i\cdot t_j/T)}
$$

## Where contrastive learning runs out

False negatives may actually describe the same concept.

A final test reaches beyond the new instrument. It does not refute Contrastive Learning; it reveals the edge of what was constructed. The expedition leader carries that edge into the following room.

## Return to the map of branching journeys

Rebuild the contrastive learning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 093](../093-speech-audio/README.md)
