# Excavation 217 — Conditional Probability and Bayes’ Rule — Let Evidence Rearrange Belief

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->



Random variables turn possible worlds into measurable quantities. A fresh paw print should change the tiger probability, but merely retaining yesterday's distribution ignores the reason observation matters.

Far below the Transformer, Conditional Probability and Bayes’ Rule begins with an ordinary situation and a tool that almost—but not quite—solves it.

Before seeing tracks, the valley expects tiger on one day in ten and deer on nine. Deep clawed tracks are likely under tiger and rare under deer. The print has arrived; the old shares can no longer remain untouched.

The chamber has reduced the abstraction to one physical thing: **a ring of lanterns and one fresh track beneath a lens**. The question carved beside it asks: *How should one paw print rearrange the brightness of competing hidden stories?*

With no standard method to recite, the most economical proposal is to compare only how well each animal explains the print and choose the largest likelihood.

A useful wrong idea is one that leaves a clean fossil of its missing responsibility. Likelihood ignores how common each animal was before the evidence. A moderately diagnostic clue could make an extremely rare story look certain if prior plausibility is discarded.

```text
what we kept       what disappeared
     │                     │
     └──── first attempt ──┘
               │
          failure mark
               │
       one necessary repair
               │
             Conditional Probability and Bayes’ Rule
```

The next idea is forced only because the evidence asks us to multiply each prior belief by that story's support for the evidence, then divide by the total support across all stories so the surviving weights again form one distribution.

The failure and repair now form one continuous argument for Conditional Probability and Bayes’ Rule: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside conditional probability and bayes’ rule

The symbols for conditional probability and bayes’ rule will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Conditional Probability and Bayes’ Rule against the named case

Out of 100 imagined days, expect 10 tiger days and 90 deer days. Suppose deep tracks appear on 8 of 10 tiger days but only 9 of 90 deer days. Among the 17 deep-track days, 8 involve tiger. After observing deep tracks, tiger probability becomes `8/17`, not 0.8 and not the old 0.1.

### Naming what is already on the table

**H** is one hidden story and **E** the observed evidence. **P(H)** is prior plausibility. **P(E|H)** is likelihood. Their product is the joint share where H and E occur. **P(E)** totals all routes to the evidence. Division asks what fraction of evidence-compatible worlds contain H.

### Why the melody needs these exact notes

[Conditional probability](../../MATHEMATICAL_MOVES.md#conditional-bar) states which fact is held as known. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) requires both prior story and compatible evidence, while [division](../../MATHEMATICAL_MOVES.md#division) restricts attention to worlds where E occurred. Adding prior and likelihood would mix quantities that do not form a joint share.

Every operation required by conditional probability and bayes’ rule now has a visible job in the named case, so the complete construction can be written compactly:

$$
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}
$$

## A real-world echo

Evidence is a gate, not paint. It does not colour every old belief equally; it admits worlds in proportion to how naturally they could have produced what was seen.

## What this unlocks elsewhere

Likelihood, calibration, Bayesian updating, filtering, and uncertainty-aware planning all reuse this rearrangement. Excavation 102 used it; here we expose the counting skeleton underneath.

## Where the promise of conditional probability and bayes’ rule breaks

A posterior distribution can still be too rich to carry everywhere. One mean alone, however, hides whether beliefs are tightly gathered, widely spread, or moving together.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Conditional Probability and Bayes’ Rule tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 218: Expectation, Variance, and Covariance — Centre, Spread, and Shared Motion](../218-expectation-variance-covariance/README.md)
