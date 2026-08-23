# Excavation 185 — Mixture Sampling — Turn Planned Shares into a Reproducible Stream

<!-- book-prose-v2 -->

The mixture weights state which domains should be heard. They do not yet produce a finite ordered token stream that every resumed worker can reconstruct.

A careful builder would first avoid adding machinery and round each domain's desired share independently and concatenate the resulting blocks.

The shortcut appears to retain everything mixture sampling needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

The world supplies the one comparison the shortcut hoped never to face: independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero.

The counterexample teaches mixture sampling. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source.

Now—and not earlier—we may introduce **Mixture Sampling**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to round each domain's desired share independently and concatenate the resulting blocks, and the case answers that independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero. With the narrow repair—to use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Mixture Sampling returns to the same counterexample, replaces the attempt to round each domain's desired share independently and concatenate the resulting blocks with the responsibility to use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source, and must succeed where the shortcut failed.

## Turn Planned Shares into a Reproducible Stream

For 1,000 document draws, a 0.05 field-report weight expects about 50 selections. The seeded schedule interleaves those reports with other domains and records the actual count rather than promising exact equality by chance.

A formula for mixture sampling is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

## The calculation hidden inside mixture sampling

Before Mixture Sampling receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

N is the total number of scheduled training draws, w_d is domain d's share, n_d is its realized count, and E[n_d] is the average count expected across many schedules.

### Why no cheaper operation does the same job

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced because each of N draws independently offers domain d the same share w_d. Addition would grant a fixed number unrelated to run length. [Expectation](../../MATHEMATICAL_MOVES.md#expectation) describes a long-run average, not a guarantee that one finite schedule equals Nw_d exactly.

Every symbol in Mixture Sampling can now be read back into an action already performed. The whole procedure fits in one line:

$$
E[n_d]=Nw_d
$$

## Where mixture sampling runs out

Sampling realizes probabilities only approximately in a finite run, and replacement can repeat scarce documents enough to increase memorization.

The boundary can be predicted from the construction itself. Mixture Sampling performs the repair to use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

## Take mixture sampling to the workbench

Move mixture sampling from imagination to evidence by making the shortcut fail under controlled inputs. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running mixture sampling, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the mixture sampling result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: The Token Budget — Convert a Training Plan into a Count of Lessons](../186-token-budget/README.md)
