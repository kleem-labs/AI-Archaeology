# Excavation 156 — Relative Position Bias — What Should Happen Beyond the Seen Window?

Rotary position makes displacement visible inside the attention match. When the station tests much longer sequences, the model must rank relationships at separations absent from training.

Perhaps we trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there.

It survives until the measured run answers back. A mathematically defined position is not necessarily a learned behavior; attention can become erratic at unfamiliar separations.

Now the missing requirement is concrete. Add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation.

## Let one run decide

For one head with slope 0.1, a key 2 places back receives −0.2 while a key 20 places back receives −2.0 before softmax. Content can overcome the penalty, but distance has a predictable cost.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

Suppose tiger matches one key with content score 3.0. The key is two places away, and we decide that each place should cost 0.1, so distance contributes 2×0.1=0.2. Removing that cost leaves 2.8. A key twenty places away pays 20×0.1=2.0 and keeps 1.0. We now name the original content score s_ij, the price per place m, and the adjusted result s-prime.

s_ij is the content match, |i−j| is token separation, m is this head's nonnegative distance slope, and s-prime is the adjusted score.

### Why these operations are forced

[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) lowers rather than raises distant matches. [Absolute value](../../MATHEMATICAL_MOVES.md#absolute-value) keeps separation size while discarding left-versus-right direction in this bias. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) lets slope m control the price per position; adding a fixed m would not make farther tokens cost more.

Only now can we compress the procedure:

$$
s_{ij}^{\prime}=s_{ij}-m\lvert i-j\rvert
$$

## What this repair cannot do

A fixed distance preference can suppress a decisive remote clue and is an architectural bias, not universal truth.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: The KV Cache — Stop Re-reading the Entire Past](../157-kv-cache/README.md)
