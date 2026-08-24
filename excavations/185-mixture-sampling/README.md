# Excavation 185 — Mixture Sampling — Turn Planned Shares into a Reproducible Stream

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Data and pretraining operations

The mixture weights state which domains should be heard. They do not yet produce a finite ordered token stream that every resumed worker can reconstruct.

Morning reaches the Archive Foundry before anyone has a name for today's difficulty. Beside the chain-of-custody ledger, the archivist-engineer tries the smallest continuation of what already works: round each domain's desired share independently and concatenate the resulting blocks.

At the edge of the chain-of-custody ledger, the shortcut produces its consequence: independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero. That consequence, not a textbook, earns the next move.

*The archivist-engineer sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: round each domain's desired share…
                         │
                         └── mismatch: independent rounding can exceed the…

reference evidence ──▶ measured repair: use a seeded categorical schedule,…
```

The archivist-engineer covers the new mark and the old contradiction returns: independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero. The cover is lifted, restoring the ability to use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason mixture sampling exists.

What must change for mixture sampling is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source. That threshold is where **Mixture Sampling** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In mixture sampling, that memory takes a precise form: whenever independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero, preserve enough structure to use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source.

<!-- memory-film-v1:start -->
> **Memory realm 13 of 18 — [Archive Foundry](../../MEMORY_PALACE.md#realm-13)**
>
> **The question carried into this chamber:** What fails if we round each domain's desired share independently and concatenate the resulting blocks?

## When the chamber changes

The Mixture Sampling room does not ask you to memorize its name. It asks you to watch one object change.

First hold the failed picture still: The vessel follows the tempting path—round each domain's desired share independently and concatenate the resulting blocks. Then the evidence answers: independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero.

Now let the chamber move: The archivist-engineer changes one moving part. The vessel can now use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source.

The object that should remain after the terminology disappears is **the mixture sampling vessel mounted on the chain-of-custody ledger**.

> **Memory seal — Mixture Sampling**
>
> Mixture Sampling keeps the missing power: use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source.

Give the idea a bodily path: Touch the mixture sampling vessel in imagination: hold both hands as the two failed alternatives, then move one hand through the repaired route.
<!-- memory-film-v1:end -->

## Turn Planned Shares into a Reproducible Stream

For 1,000 document draws, a 0.05 field-report weight expects about 50 selections. The seeded schedule interleaves those reports with other domains and records the actual count rather than promising exact equality by chance.

## The calculation hidden inside mixture sampling

The archivist-engineer carries the mixture sampling scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

N is the total number of scheduled training draws, w_d is domain d's share, n_d is its realized count, and E[n_d] is the average count expected across many schedules.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced because each of N draws independently offers domain d the same share w_d. Addition would grant a fixed number unrelated to run length. [Expectation](../../MATHEMATICAL_MOVES.md#expectation) describes a long-run average, not a guarantee that one finite schedule equals Nw_d exactly.

The calculation borrows several gestures already encountered elsewhere: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the council of possible worlds**—each future speaks in proportion to how often it may arrive. mixture sampling feels new because the objects are new; the gestures remain recognizably human.

The chain-of-custody ledger already contains the complete mixture sampling mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
E[n_d]=Nw_d
$$

## Where mixture sampling runs out

Sampling realizes probabilities only approximately in a finite run, and replacement can repeat scarce documents enough to increase memorization.

Here the new path ends honestly. Mixture Sampling can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the chain-of-custody ledger

Rebuild the mixture sampling scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: The Token Budget — Convert a Training Plan into a Count of Lessons](../186-token-budget/README.md)
