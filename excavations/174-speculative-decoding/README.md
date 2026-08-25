# Excavation 174 — Speculative Decoding — Let a Small Model Propose, Never Decide

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Model systems and engine optimization

Tensor parallelism makes one target-model step possible, but autoregressive dependence still serializes token generation.

A new case arrives at the Engine Cavern. Nothing yet demands a new invention, so the enginewright uses the brass reference machine to let a cheap draft model emit several tokens and return them directly.

This is precisely the kind of shortcut a careful builder should try first. The instruction to let a cheap draft model emit several tokens and return them directly preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: speed improves by silently replacing the trusted target distribution with a weaker model's distribution.

The counterexample separates two questions that the attempt to let a cheap draft model emit several tokens and return them directly had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the brass reference machine fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Speculative Decoding**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Let a Small Model Propose, Never Decide

The draft proposes “the tiger sleeps.” One target call verifies all three positions; an unsupported token is rejected and sampling resumes from the corrected target distribution.

## The calculation hidden inside speculative decoding

The enginewright carries the speculative decoding scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

If the draft assigns tiger probability 0.8 but the target assigns 0.4, only half of those proposals have target support: 0.4/0.8=0.5. If the draft assigns 0.4 and the target 0.8, the ratio is 2, but acceptance cannot be 200 percent, so it stops at 1. The function a(x) names this capped acceptance chance for proposed token x.

q(x) is draft probability, p(x) is target probability, and a(x) is the probability of accepting the draft token under the correction step.

### Why the melody needs these exact notes

[Division](../../MATHEMATICAL_MOVES.md#division) compares target support per unit of draft support. [Minimum](../../MATHEMATICAL_MOVES.md#minimum) caps acceptance at one because probabilities cannot exceed certainty. Simply taking max or always accepting would change the target distribution; the ratio corrects proposals that the draft overproduces.

The mandala has curved back upon itself. In this chamber we meet **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; and **the narrow gate**—the smaller allowance prevents a promise from exceeding its boundary. What seemed like a new formula is older mathematical instinct arranged around a new need.

Every mark needed for speculative decoding is now visible on the brass reference machine. The symbols do not add an idea; they bind the discovered moves into one line:

$$
a(x)=\min\left(1,\frac{p(x)}{q(x)}\right)
$$

## Where speculative decoding runs out

Speed depends on draft agreement and hardware utilization; poor proposals add work instead of removing it.

At the Engine Cavern, the enginewright leaves a blank beneath the new mark. Speculative Decoding has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the brass reference machine

Rebuild the speculative decoding scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: A Modern Tiny Language Model — Assemble the Measured Engine](../175-modern-tiny-llm/README.md)
