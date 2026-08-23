# Excavation 156 — Relative Position Bias — What Should Happen Beyond the Seen Window?

<!-- book-prose-v2 -->

Rotary position makes displacement visible inside the attention match. When the station tests much longer sequences, the model must rank relationships at separations absent from training.

The least expensive next move is to trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there.

The proposal deserves a fair hearing. For relative position bias, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The proposal breaks for a specific reason, not by authority: a mathematically defined position is not necessarily a learned behavior; attention can become erratic at unfamiliar separations.

The failure changes the question behind relative position bias. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation.

Only at this point does the inherited name **Relative Position Bias** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of relative position bias by mentally removing the repair. We fall back to the proposal to trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there; then a mathematically defined position is not necessarily a learned behavior; attention can become erratic at unfamiliar separations. Restore only the ability to add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there to requiring the system to add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to relative position bias.

## What Should Happen Beyond the Seen Window

For one head with slope 0.1, a key 2 places back receives −0.2 while a key 20 places back receives −2.0 before softmax. Content can overcome the penalty, but distance has a predictable cost.

Put the old procedure beside relative position bias. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## The calculation hidden inside relative position bias

Do not read the coming Relative Position Bias line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Suppose tiger matches one key with content score 3.0. The key is two places away, and we decide that each place should cost 0.1, so distance contributes 2×0.1=0.2. Removing that cost leaves 2.8. A key twenty places away pays 20×0.1=2.0 and keeps 1.0. We now name the original content score s_ij, the price per place m, and the adjusted result s-prime.

s_ij is the content match, |i−j| is token separation, m is this head's nonnegative distance slope, and s-prime is the adjusted score.

### Why no cheaper operation does the same job

[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) lowers rather than raises distant matches. [Absolute value](../../MATHEMATICAL_MOVES.md#absolute-value) keeps separation size while discarding left-versus-right direction in this bias. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) lets slope m control the price per position; adding a fixed m would not make farther tokens cost more.

Every symbol in Relative Position Bias can now be read back into an action already performed. The whole procedure fits in one line:

$$
s_{ij}^{\prime}=s_{ij}-m\lvert i-j\rvert
$$

## Where relative position bias runs out

A fixed distance preference can suppress a decisive remote clue and is an architectural bias, not universal truth.

The limit follows from the job assigned to relative position bias. Its repair knows how to add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take relative position bias to the workbench

A claim about relative position bias now exists on the page; the laboratory must be able to contradict it. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running relative position bias, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the relative position bias result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: The KV Cache — Stop Re-reading the Entire Past](../157-kv-cache/README.md)
