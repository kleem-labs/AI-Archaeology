# Excavation 028 — Momentum — Remembering Which Way Downhill Persists

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

The learning rate controls the size of each step. Mini-batches nevertheless disagree sideways from one update to the next, hiding the direction that persists across their noise.

Inside the Lantern Observatory, every old tool is given one honest chance. The keeper of uncertain stories sets the ring of glass lanterns between the evidence and the desired answer, then tries to obey only the newest gradient.

The keeper of uncertain stories repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: sideways noise repeatedly cancels progress. Average every past gradient equally; ancient advice remains influential after the landscape changes. The failure is stable enough to become evidence.

*The keeper of uncertain stories sketches the break before changing it:*

```text
observation
    │
    ▼
[obey only the newest gradient]
    │
    ╳  sideways noise repeatedly cancels…
    │
    ▼
[keep a fading memory of past…]
```

Across the ring of glass lanterns, the old path and the repaired path run side by side. One carries “obey only the newest gradient”; the other knows how to keep a fading memory of past gradients and combine it with the new one. When the failure—sideways noise repeatedly cancels progress. Average every past gradient equally; ancient advice remains influential after the landscape changes—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to momentum. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: keep a fading memory of past gradients and combine it with the new one. This problem and its repair will travel under the name **Momentum**, but the name carries no knowledge the scene has not earned.

What changed on the ring of glass lanterns can be said without symbols. Before, the method could only obey only the newest gradient; now it can also keep a fading memory of past gradients and combine it with the new one. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

## The calculation hidden inside momentum

The keeper of uncertain stories carries the momentum scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but momentum can overshoot, and its extra memory introduces another setting. It does not repair a fundamentally bad loss or dataset.

Three small groups inspect tiger tracks. Each recommends changing two detector dials: stripes and movement. Their advice is `[3,1]`, `[3,-1]`, and `[3,1]`. Now the coordinates are not anonymous: every group agrees that stripe trust should rise by 3, while movement advice flips with noisy tracks. Remembering recent directions reinforces the persistent stripe evidence and lets the contradictory movement evidence partly cancel.

### Naming what is already on the table

**g_t** is the newest noisy gradient.
**v_{t−1}** stores direction accumulated previously.
**β** between zero and one controls how much old motion survives; repeated multiplication makes old advice fade.
Addition combines memory with new evidence into velocity v_t.
**η** scales that velocity before it changes θ.

### Why the melody needs these exact notes

[Multiplying old velocity by β](../../MATHEMATICAL_MOVES.md#multiplication) fades memory instead of remembering every ancient gradient equally. β near zero forgets quickly; β near one preserves direction longer.
[Adding the new gradient](../../MATHEMATICAL_MOVES.md#addition) lets current evidence join the surviving past direction. Multiplying them would erase memory wherever either vector contains zero.
The final [η scaling](../../MATHEMATICAL_MOVES.md#multiplication) chooses travel distance and [the minus sign](../../MATHEMATICAL_MOVES.md#negative-sign) turns remembered uphill direction into a downhill update.

Inside momentum, familiar operations return with stricter duties: **the lock and key**—one influence matters through another, and either missing factor can close the path; **the joining river**—separate contributions meet without losing where they came from; and **the turning wind**—an uphill quantity is made to point downhill, or surprise is made to count as cost. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Cover the prose about momentum and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
v_t=\beta v_{t-1}+g_t
$$

$$
\theta_{t+1}=\theta_t-\eta v_t
$$

## Momentum beyond this one case

A heavy ball rattles less across a narrow ravine and keeps moving along the valley.

## Return to the ring of glass lanterns

Rebuild the momentum scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Excavation 029](../029-initialization/README.md)
