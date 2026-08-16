# Excavation 185 — Mixture Sampling — Turn Planned Shares into a Reproducible Stream

The mixture weights state which domains should be heard. They do not yet produce a finite ordered token stream that every resumed worker can reconstruct.

At first we round each domain's desired share independently and concatenate the resulting blocks.

Reality objects. Independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero.

That evidence forces a repair. Use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source.

## Let one run decide

For 1,000 document draws, a 0.05 field-report weight expects about 50 selections. The seeded schedule interleaves those reports with other domains and records the actual count rather than promising exact equality by chance.

## The arithmetic we have earned

N is the total number of scheduled training draws, w_d is domain d's share, n_d is its realized count, and E[n_d] is the average count expected across many schedules.

### Why these operations are forced

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced because each of N draws independently offers domain d the same share w_d. Addition would grant a fixed number unrelated to run length. [Expectation](../../MATHEMATICAL_MOVES.md#expectation) describes a long-run average, not a guarantee that one finite schedule equals Nw_d exactly.

Only now can we compress the procedure:

$$
E[n_d]=Nw_d
$$

## What this repair cannot do

Sampling realizes probabilities only approximately in a finite run, and replacement can repeat scarce documents enough to increase memorization.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: The Token Budget — Convert a Training Plan into a Count of Lessons](../186-token-budget/README.md)
