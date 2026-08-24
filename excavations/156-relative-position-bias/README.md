# Excavation 156 — Relative Position Bias — What Should Happen Beyond the Seen Window?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

Rotary position makes displacement visible inside the attention match. When the station tests much longer sequences, the model must rank relationships at separations absent from training.

Inside the Engine Cavern, every old tool is given one honest chance. The enginewright sets the brass reference machine between the evidence and the desired answer, then tries to trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there.

For a moment the mark looks complete. Then the evidence refuses to fit: a mathematically defined position is not necessarily a learned behavior; attention can become erratic at unfamiliar separations. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The enginewright sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: trust every unseen distance to behave…
                         │
                         └── mismatch: a mathematically defined position is…

reference evidence ──▶ measured repair: add an explicit distance-dependent…
```

The enginewright lays two translucent sheets over the brass reference machine. The first is inscribed, “trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there.” Its path ends where a mathematically defined position is not necessarily a learned behavior; attention can become erratic at unfamiliar separations. The second receives the same evidence but is allowed to add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation. Held to the light, the sheets separate at exactly one decision.

No one reaches for a relative position bias formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The enginewright changes only that one responsibility: add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation. When the ink dries, the name **Relative Position Bias** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The brass reference machine keeps both histories. Its older mark still says, ‘trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there’; beside it, the newer mark says, ‘add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation.’ The distance between those sentences is the exact shape of relative position bias: no larger than the failure required, and no smaller than reality permits.

<!-- memory-film-v1:start -->
> **Memory realm 12 of 18 — [Engine Cavern](../../MEMORY_PALACE.md#realm-12)**
>
> **The question carried into this chamber:** What Should Happen Beyond the Seen Window?

## When the chamber changes

Keep the formal name Relative Position Bias covered for another moment. The surviving image is enough to rebuild it.

First hold the failed picture still: The map follows the tempting path—trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there. Then the evidence answers: a mathematically defined position is not necessarily a learned behavior; attention can become erratic at unfamiliar separations.

Now let the chamber move: The enginewright changes one moving part. The map can now add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation.

The object that should remain after the terminology disappears is **the relative position bias map mounted on the brass reference machine**.

> **Memory seal — Relative Position Bias**
>
> Relative Position Bias keeps the missing power: add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation.

Give the idea a bodily path: Touch the relative position bias map in imagination: point backward to the failed attempt, touch the present object, then point forward through the repair.
<!-- memory-film-v1:end -->

## What Should Happen Beyond the Seen Window

For one head with slope 0.1, a key 2 places back receives −0.2 while a key 20 places back receives −2.0 before softmax. Content can overcome the penalty, but distance has a predictable cost.

## The calculation hidden inside relative position bias

The enginewright carries the relative position bias scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Suppose tiger matches one key with content score 3.0. The key is two places away, and we decide that each place should cost 0.1, so distance contributes 2×0.1=0.2. Removing that cost leaves 2.8. A key twenty places away pays 20×0.1=2.0 and keeps 1.0. We now name the original content score s_ij, the price per place m, and the adjusted result s-prime.

s_ij is the content match, |i−j| is token separation, m is this head's nonnegative distance slope, and s-prime is the adjusted score.

### Why the melody needs these exact notes

[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) lowers rather than raises distant matches. [Absolute value](../../MATHEMATICAL_MOVES.md#absolute-value) keeps separation size while discarding left-versus-right direction in this bias. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) lets slope m control the price per position; adding a fixed m would not make farther tokens cost more.

Inside relative position bias, familiar operations return with stricter duties: **the chisel**—what is shared is removed so the remaining change can be seen; and **the lock and key**—one influence matters through another, and either missing factor can close the path. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Every mark needed for relative position bias is now visible on the brass reference machine. The symbols do not add an idea; they bind the discovered moves into one line:

$$
s_{ij}^{\prime}=s_{ij}-m\lvert i-j\rvert
$$

## Where relative position bias runs out

A fixed distance preference can suppress a decisive remote clue and is an architectural bias, not universal truth.

At the Engine Cavern, the enginewright leaves a blank beneath the new mark. Relative Position Bias has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the brass reference machine

Rebuild the relative position bias scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: The KV Cache — Stop Re-reading the Entire Past](../157-kv-cache/README.md)
