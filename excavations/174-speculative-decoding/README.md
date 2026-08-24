# Excavation 174 — Speculative Decoding — Let a Small Model Propose, Never Decide

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Tensor parallelism makes one target-model step possible, but autoregressive dependence still serializes token generation.

The doors of the Engine Cavern close against the wind. On the brass reference machine, the enginewright writes the cheapest rule that might still be true: let a cheap draft model emit several tokens and return them directly.

For a moment the mark looks complete. Then the evidence refuses to fit: speed improves by silently replacing the trusted target distribution with a weaker model's distribution. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The enginewright sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: let a cheap draft model emit several…
                         │
                         └── mismatch: speed improves by silently replacing…

reference evidence ──▶ measured repair: let the draft propose a short…
```

The enginewright lays two translucent sheets over the brass reference machine. The first is inscribed, “let a cheap draft model emit several tokens and return them directly.” Its path ends where speed improves by silently replacing the trusted target distribution with a weaker model's distribution. The second receives the same evidence but is allowed to let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling. Held to the light, the sheets separate at exactly one decision.

No one reaches for a speculative decoding formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The enginewright changes only that one responsibility: let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling. When the ink dries, the name **Speculative Decoding** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because speed improves by silently replacing the trusted target distribution with a weaker model's distribution, while the other can let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling. That fork—not the vocabulary—is where speculative decoding lives.

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
