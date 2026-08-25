# Excavation 221 — Hypothesis Tests and Confidence Intervals — When Is an Improvement Convincing?

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->



The central limit theorem gives the shape and scale of repeated sample averages. It still does not decide whether a measured model improvement is evidence of a real change or an ordinary tremor of sampling.

The corridor toward Hypothesis Tests and Confidence Intervals carries the unresolved consequence of the preceding excavation into a new physical scene.

Two assistants answer the same 100 field questions. The new assistant scores, on average, 0.4 points higher. The room wants to celebrate, but daily paired differences wobble with a standard deviation of 2 points.

The chamber has reduced the abstraction to one physical thing: **a distant tower bell beside a brass wind-and-noise meter**. The question carved beside it asks: *Is the new model's small victory a signal or an ordinary tremor of chance?*

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

The failure and repair now form one continuous argument for Hypothesis Tests and Confidence Intervals: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside hypothesis tests and confidence intervals

The symbols for hypothesis tests and confidence intervals will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Hypothesis Tests and Confidence Intervals against the named case

For the 100 paired questions, the mean difference is 0.4 and the standard deviation of differences is 2. The standard error is `2/√100 = 0.2`, so the improvement sits `0.4/0.2 = 2` standard errors above zero. A rough 95% interval is `0.4 ± 1.96×0.2`, or about `[0.008, 0.792]`. Zero lies just outside, yet the interval also warns that the practical gain may be tiny.

### Naming what is already on the table

**dᵢ** is the score difference on paired question i. **d̄** is their observed mean. Zero is the null claim of no average improvement. **s/√n** estimates how much the sample mean would wobble. **z** tells how many such wobble-units separate the observation from the null.

### Why the melody needs these exact notes

[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) makes each question compare like with like. [The mean](../../MATHEMATICAL_MOVES.md#mean) lets all paired questions contribute. [The square root](../../MATHEMATICAL_MOVES.md#square-root) converts sample count into the scale of average noise, and [division](../../MATHEMATICAL_MOVES.md#division) asks how large the effect is relative to that noise. Dividing only by s would ignore that one hundred witnesses stabilize a mean more than one witness.

Every operation required by hypothesis tests and confidence intervals now has a visible job in the named case, so the complete construction can be written compactly:

$$
z=\frac{\overline d-0}{s/\sqrt n}
$$

## A real-world echo

A distant bell may be real or merely wind in the tower. Evidence asks not only whether you heard a sound, but how loud it was compared with the night's ordinary noise.

## What this unlocks elsewhere

Benchmark uncertainty, A/B tests, ablations, model comparisons, and safety evaluations need this separation between observed effect, sampling uncertainty, and practical importance.

## Where the promise of hypothesis tests and confidence intervals breaks

A test depends on sampling assumptions, a chosen error rate, and a claim selected before inspection. It cannot rescue biased data, repeated unreported testing, or a meaningless metric. Nor does statistical significance guarantee useful significance.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Hypothesis Tests and Confidence Intervals tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 222: Markov Chains — When the Present Carries the Relevant Past](../222-markov-chains/README.md)
