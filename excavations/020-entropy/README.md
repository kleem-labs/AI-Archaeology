# Excavation 020 — Entropy — Measuring the Uncertainty of a Whole Situation

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Learning from uncertainty and error

Information gives one surprising observation a numerical weight. Before opening the next envelope, however, the community needs to compare the uncertainty of entire situations, not only the surprise of one event after it happens.

Inside the Lantern Observatory, every old tool is given one honest chance. The keeper of uncertain stories sets the ring of glass lanterns between the evidence and the desired answer, then tries to count the number of outcomes.

Reality answers without terminology: both bags contain stones, and both have two named colors if we list an absent possibility. Or inspect only the most likely outcome, losing the rest of the distribution. The ring of glass lanterns now holds two situations the old rule cannot keep apart.

*The keeper of uncertain stories sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: count the number of outcomes
possible road B ─┘              └── loses: both bags contain stones, and both…

same roads ──▶ repaired map ──▶ average the information of every…
```

The ring of glass lanterns is divided down the middle. Left side: “count the number of outcomes.” Its final mark records both bags contain stones, and both have two named colors if we list an absent possibility. Or inspect only the most likely outcome, losing the rest of the distribution. Right side: the same starting evidence, now allowed to average the information of every possible outcome, weighted by how often that outcome occurs. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given entropy a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: average the information of every possible outcome, weighted by how often that outcome occurs. The name **Entropy** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to count the number of outcomes; on the other lies the observed fact that both bags contain stones, and both have two named colors if we list an absent possibility. Or inspect only the most likely outcome, losing the rest of the distribution. The bridge called entropy has exactly the planks needed to average the information of every possible outcome, weighted by how often that outcome occurs.

<!-- memory-film-v1:start -->
> **Memory realm 3 of 18 — [Lantern Observatory](../../MEMORY_PALACE.md#realm-3)**
>
> **The question carried into this chamber:** What fails if we count the number of outcomes?

## When the chamber changes

The Entropy room does not ask you to memorize its name. It asks you to watch one object change.

First hold the failed picture still: The compass follows the tempting path—count the number of outcomes. Then the evidence answers: both bags contain stones, and both have two named colors if we list an absent possibility. Or inspect only the most likely outcome, losing the rest of the distribution.

Now let the chamber move: The keeper of uncertain stories changes one moving part. The compass can now average the information of every possible outcome, weighted by how often that outcome occurs.

The object that should remain after the terminology disappears is **the entropy compass mounted on the ring of glass lanterns**.

> **Memory seal — Entropy**
>
> Entropy keeps the missing power: average the information of every possible outcome, weighted by how often that outcome occurs.

Give the idea a bodily path: Touch the entropy compass in imagination: point backward to the failed attempt, touch the present object, then point forward through the repair.
<!-- memory-film-v1:end -->

## The calculation hidden inside entropy

The keeper of uncertain stories carries the entropy scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

For a fair coin, each outcome has probability 1/2 and information 1 bit. Weighting gives 0.5×1+0.5×1=1 expected bit. A coin guaranteed heads gives -log₂(1)=0, so its entropy is zero.

### Naming what is already on the table

**pᵢ** is the probability of possible outcome i.
**−log pᵢ** is the information received if i occurs.
Multiplying by pᵢ weights that surprise by how often it is expected to occur.
Summing over every i computes average surprise before the outcome is known.
**H(P)** names uncertainty of the whole distribution P.

### Why the melody needs these exact notes

[Multiplying each surprise by pᵢ](../../MATHEMATICAL_MOVES.md#multiplication) lets common outcomes speak more often than rare ones when measuring the uncertainty of the whole situation.
[Summing](../../MATHEMATICAL_MOVES.md#summation) combines those mutually exclusive outcome contributions into one expected uncertainty; multiplying them would make any certain zero-surprise outcome erase all others.
[The log](../../MATHEMATICAL_MOVES.md#logarithm) still converts probability products into additive information, and [the minus sign](../../MATHEMATICAL_MOVES.md#negative-sign) keeps that information nonnegative.

Inside entropy, familiar operations return with stricter duties: **the lock and key**—one influence matters through another, and either missing factor can close the path; **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the spiral stair**—compounded chances become steps that can be accumulated. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Nothing remains unnamed in the entropy case on the ring of glass lanterns. We can finally trade the long route for its compact map:

$$
H(P)=-\sum_i p_i\log p_i
$$

## Entropy beyond this one case

Entropy is the expected surprise before opening a sealed envelope. A guaranteed message brings none; evenly balanced alternatives bring more.

## Where entropy runs out

Entropy measures uncertainty in a stated distribution, not disorder in every everyday sense.

A final test reaches beyond the new instrument. It does not refute Entropy; it reveals the edge of what was constructed. The keeper of uncertain stories carries that edge into the following room.

## Return to the ring of glass lanterns

Rebuild the entropy scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
