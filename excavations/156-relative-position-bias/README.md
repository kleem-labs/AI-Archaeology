# Excavation 156 — Relative Position Bias — What Should Happen Beyond the Seen Window?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

Rotary position makes displacement visible inside the attention match. When the station tests much longer sequences, the model must rank relationships at separations absent from training.

At the Engine Cavern, the enginewright meets the next case beside the brass reference machine. The nearest idea is also the most reasonable one: trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there.

The attraction of this attempt is easy to see. To trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: a mathematically defined position is not necessarily a learned behavior; attention can become erratic at unfamiliar separations.

The contradiction matters because it identifies a structural loss in the instruction to trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The brass reference machine will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Relative Position Bias**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

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
