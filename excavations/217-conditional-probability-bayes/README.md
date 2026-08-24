# Excavation 217 — Conditional Probability and Bayes’ Rule — Let Evidence Rearrange Belief

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

Random variables turn possible worlds into measurable quantities. A fresh paw print should change the tiger probability, but merely retaining yesterday's distribution ignores the reason observation matters.

Far below the Transformer, the Undercroft stores no formula sheet. For **Conditional Probability and Bayes’ Rule**, it preserves a scene, a tempting tool, and the mark left where that tool broke.

Before seeing tracks, the valley expects tiger on one day in ten and deer on nine. Deep clawed tracks are likely under tiger and rare under deer. The print has arrived; the old shares can no longer remain untouched.

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

This is the hinge of the Conditional Probability and Bayes’ Rule excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

## Conditional Probability and Bayes’ Rule on the stone workbench

Out of 100 imagined days, expect 10 tiger days and 90 deer days. Suppose deep tracks appear on 8 of 10 tiger days but only 9 of 90 deer days. Among the 17 deep-track days, 8 involve tiger. After observing deep tracks, tiger probability becomes `8/17`, not 0.8 and not the old 0.1.

The point of keeping the objects named while rebuilding Conditional Probability and Bayes’ Rule is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

## The calculation hidden inside conditional probability and bayes’ rule

Return to the named Conditional Probability and Bayes’ Rule scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

### Naming what is already on the table

**H** is one hidden story and **E** the observed evidence. **P(H)** is prior plausibility. **P(E|H)** is likelihood. Their product is the joint share where H and E occur. **P(E)** totals all routes to the evidence. Division asks what fraction of evidence-compatible worlds contain H.

### Why the melody needs these exact notes

[Conditional probability](../../MATHEMATICAL_MOVES.md#conditional-bar) states which fact is held as known. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) requires both prior story and compatible evidence, while [division](../../MATHEMATICAL_MOVES.md#division) restricts attention to worlds where E occurred. Adding prior and likelihood would mix quantities that do not form a joint share.

The operations inside Conditional Probability and Bayes’ Rule form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}
$$

Read the Conditional Probability and Bayes’ Rule line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

## A real-world echo

Evidence is a gate, not paint. It does not colour every old belief equally; it admits worlds in proportion to how naturally they could have produced what was seen.

That echo helps Conditional Probability and Bayes’ Rule remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

## What this chamber was connected to

Likelihood, calibration, Bayesian updating, filtering, and uncertainty-aware planning all reuse this rearrangement. Excavation 102 used it; here we expose the counting skeleton underneath.

The older excavation and this Conditional Probability and Bayes’ Rule chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

## Where the promise of conditional probability and bayes’ rule breaks

A posterior distribution can still be too rich to carry everywhere. One mean alone, however, hides whether beliefs are tightly gathered, widely spread, or moving together.

The boundary belongs beside the discovery of Conditional Probability and Bayes’ Rule because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Conditional Probability and Bayes’ Rule tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 218: Expectation, Variance, and Covariance — Centre, Spread, and Shared Motion](../218-expectation-variance-covariance/README.md)
