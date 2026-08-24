# Excavation 221 — Hypothesis Tests and Confidence Intervals — When Is an Improvement Convincing?

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Mathematical roots beneath the machine

The central limit theorem gives the shape and scale of repeated sample averages. It still does not decide whether a measured model improvement is evidence of a real change or an ordinary tremor of sampling.

The corridor bends beneath every model we have built. Here **Hypothesis Tests and Confidence Intervals** is not presented as inherited knowledge. Its symbol is still buried, and the only lantern we carry is the failure left by the preceding excavation.

Two assistants answer the same 100 field questions. The new assistant scores, on average, 0.4 points higher. The room wants to celebrate, but daily paired differences wobble with a standard deviation of 2 points.

If we were the first people in this chamber, we would probably declare every positive sample difference a discovery.

We let the idea touch the evidence. The fracture appears exactly where information was lost. Another sample from unchanged systems can land above zero by chance. A positive sign says which side won this sample; it does not say how surprising that victory would be if the true average difference were zero.

```text
             what the world shows
                      │
         ┌────────────┴────────────┐
         │                         │
   old explanation           counterexample
         │                         │
         └──────── breaks ─────────┘
                      │
               repair the promise
                      │
                    Hypothesis Tests and Confidence Intervals
```

The broken attempt has done its work. It tells us, in ordinary language, to state the no-improvement claim, measure the observed mean difference in units of its standard error, and report both a test statistic and the range of effects compatible with the sampling noise.

This is the hinge of the Hypothesis Tests and Confidence Intervals excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

## Hypothesis Tests and Confidence Intervals on the stone workbench

For the 100 paired questions, the mean difference is 0.4 and the standard deviation of differences is 2. The standard error is `2/√100 = 0.2`, so the improvement sits `0.4/0.2 = 2` standard errors above zero. A rough 95% interval is `0.4 ± 1.96×0.2`, or about `[0.008, 0.792]`. Zero lies just outside, yet the interval also warns that the practical gain may be tiny.

The point of keeping the objects named while rebuilding Hypothesis Tests and Confidence Intervals is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

## The calculation hidden inside hypothesis tests and confidence intervals

Return to the named Hypothesis Tests and Confidence Intervals scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

### Naming what is already on the table

**dᵢ** is the score difference on paired question i. **d̄** is their observed mean. Zero is the null claim of no average improvement. **s/√n** estimates how much the sample mean would wobble. **z** tells how many such wobble-units separate the observation from the null.

### Why the melody needs these exact notes

[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) makes each question compare like with like. [The mean](../../MATHEMATICAL_MOVES.md#mean) lets all paired questions contribute. [The square root](../../MATHEMATICAL_MOVES.md#square-root) converts sample count into the scale of average noise, and [division](../../MATHEMATICAL_MOVES.md#division) asks how large the effect is relative to that noise. Dividing only by s would ignore that one hundred witnesses stabilize a mean more than one witness.

The operations inside Hypothesis Tests and Confidence Intervals form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
z=\frac{\overline d-0}{s/\sqrt n}
$$

Read the Hypothesis Tests and Confidence Intervals line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

## A real-world echo

A distant bell may be real or merely wind in the tower. Evidence asks not only whether you heard a sound, but how loud it was compared with the night's ordinary noise.

That echo helps Hypothesis Tests and Confidence Intervals remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

## What this chamber was connected to

Benchmark uncertainty, A/B tests, ablations, model comparisons, and safety evaluations need this separation between observed effect, sampling uncertainty, and practical importance.

The older excavation and this Hypothesis Tests and Confidence Intervals chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

## Where the promise of hypothesis tests and confidence intervals breaks

A test depends on sampling assumptions, a chosen error rate, and a claim selected before inspection. It cannot rescue biased data, repeated unreported testing, or a meaningless metric. Nor does statistical significance guarantee useful significance.

The boundary belongs beside the discovery of Hypothesis Tests and Confidence Intervals because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Hypothesis Tests and Confidence Intervals tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 222: Markov Chains — When the Present Carries the Relevant Past](../222-markov-chains/README.md)
