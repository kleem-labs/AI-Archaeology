# Excavation 028 — Momentum — Remembering Which Way Downhill Persists

<!-- book-prose-v2 -->

The learning rate controls the size of each step. Mini-batches nevertheless disagree sideways from one update to the next, hiding the direction that persists across their noise.

If the old idea can be stretched one step farther, we should obey only the newest gradient.

If the proposal works on every relevant case, momentum is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The proposal breaks for a specific reason, not by authority: sideways noise repeatedly cancels progress. Average every past gradient equally; ancient advice remains influential after the landscape changes.

Nothing magical creates momentum. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: keep a fading memory of past gradients and combine it with the new one.

This boundary between the failed rule and its repair is the subject later work calls **Momentum**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize momentum; try to break it by subtraction. Remove the part that knows how to keep a fading memory of past gradients and combine it with the new one, leaving only the attempt to obey only the newest gradient.. What returns is not a vague weakness but the original contradiction: sideways noise repeatedly cancels progress. Average every past gradient equally; ancient advice remains influential after the landscape changes. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to obey only the newest gradient. receives the same test as the rule to keep a fading memory of past gradients and combine it with the new one. Their different outcomes reveal what momentum contributes without asking the reader to trust historical convention.

## The calculation hidden inside momentum

Do not read the coming Momentum line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

The repair solves the immediate failure, but momentum can overshoot, and its extra memory introduces another setting. It does not repair a fundamentally bad loss or dataset.

Three small groups inspect tiger tracks. Each recommends changing two detector dials: stripes and movement. Their advice is `[3,1]`, `[3,-1]`, and `[3,1]`. Now the coordinates are not anonymous: every group agrees that stripe trust should rise by 3, while movement advice flips with noisy tracks. Remembering recent directions reinforces the persistent stripe evidence and lets the contradictory movement evidence partly cancel.

### Names for pieces we have already used

**g_t** is the newest noisy gradient.
**v_{t−1}** stores direction accumulated previously.
**β** between zero and one controls how much old motion survives; repeated multiplication makes old advice fade.
Addition combines memory with new evidence into velocity v_t.
**η** scales that velocity before it changes θ.

### Why no cheaper operation does the same job

[Multiplying old velocity by β](../../MATHEMATICAL_MOVES.md#multiplication) fades memory instead of remembering every ancient gradient equally. β near zero forgets quickly; β near one preserves direction longer.
[Adding the new gradient](../../MATHEMATICAL_MOVES.md#addition) lets current evidence join the surviving past direction. Multiplying them would erase memory wherever either vector contains zero.
The final [η scaling](../../MATHEMATICAL_MOVES.md#multiplication) chooses travel distance and [the minus sign](../../MATHEMATICAL_MOVES.md#negative-sign) turns remembered uphill direction into a downhill update.

The notation is finally shorter than the story that created it:

$$
v_t=\beta v_{t-1}+g_t
$$

$$
\theta_{t+1}=\theta_t-\eta v_t
$$

## Momentum beyond this one case

A heavy ball rattles less across a narrow ravine and keeps moving along the valley.

## Take momentum to the workbench

A mathematical story about momentum earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running momentum, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the momentum result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Excavation 029](../029-initialization/README.md)
