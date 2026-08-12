# Excavation 028 — Momentum — Remembering Which Way Downhill Persists

The learning rate controls the size of each step. Mini-batches nevertheless disagree sideways from one update to the next, hiding the direction that persists across their noise.

Using what we have, we obey only the newest gradient. Sideways noise repeatedly cancels progress. Average every past gradient equally; ancient advice remains influential after the landscape changes.

Now we can see what is missing: we must keep a fading memory of past gradients and combine it with the new one.

## From procedure to notation

The repair solves the immediate failure, but momentum can overshoot, and its extra memory introduces another setting. It does not repair a fundamentally bad loss or dataset.

## The arithmetic we have earned

Three small groups inspect tiger tracks. Each recommends changing two detector dials: stripes and movement. Their advice is `[3,1]`, `[3,-1]`, and `[3,1]`. Now the coordinates are not anonymous: every group agrees that stripe trust should rise by 3, while movement advice flips with noisy tracks. Remembering recent directions reinforces the persistent stripe evidence and lets the contradictory movement evidence partly cancel.

### Only now do the symbols earn names

- **g_t** is the newest noisy gradient.
- **v_{t−1}** stores direction accumulated previously.
- **β** between zero and one controls how much old motion survives; repeated multiplication makes old advice fade.
- Addition combines memory with new evidence into velocity v_t.
- **η** scales that velocity before it changes θ.

Only now can we compress that reasoning:

$$
v_t=\beta v_{t-1}+g_t
$$

$$
\theta_{t+1}=\theta_t-\eta v_t
$$

## Carry the idea back into the world

A heavy ball rattles less across a narrow ravine and keeps moving along the valley.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Test what you believe

Use the [invention challenges](exercises.md).

## What this discovery now makes possible

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 029](../029-initialization/README.md)
