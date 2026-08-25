# Excavation 185 — Mixture Sampling — Turn Planned Shares into a Reproducible Stream

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Data and pretraining operations

The mixture weights state which domains should be heard. They do not yet produce a finite ordered token stream that every resumed worker can reconstruct.

The previous discovery reaches the Archive Foundry carrying one unfinished problem. Beside the chain-of-custody ledger, the archivist-engineer first tries to round each domain's desired share independently and concatenate the resulting blocks.

There is good reason to begin this way. If we round each domain's desired share independently and concatenate the resulting blocks, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero.

This failure cannot be repaired by performing the instruction to round each domain's desired share independently and concatenate the resulting blocks more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the chain-of-custody ledger; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Mixture Sampling**. The name is simply a handle for the distinction already reconstructed.

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
