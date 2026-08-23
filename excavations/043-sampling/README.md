# Excavation 043 — Sampling — Choosing Without Always Taking the Maximum

<!-- book-prose-v2 -->

Softmax turns vocabulary scores into a distribution. Generation now faces a choice that training did not settle: should the machine always take the winner or sometimes follow another plausible continuation?

Before naming anything new, try to always use argmax.

Its appeal is not ignorance but economy. Sampling should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Then a case arrives in which convenience and truth separate: the same prompt follows the same narrow path. Sample raw probabilities blindly. Low-quality tail tokens eventually derail the text.

Notice what the counterexample has accomplished for sampling. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: we need to control the distribution with temperature and optionally restrict it to a credible top set before sampling.

Humanity eventually gathered this problem and its repairs under the name **Sampling**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace sampling with the old instruction to always use argmax.. The result is again that the same prompt follows the same narrow path. Sample raw probabilities blindly. Low-quality tail tokens eventually derail the text. Put back only the requirement to we need to control the distribution with temperature and optionally restrict it to a credible top set before sampling. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when sampling is introduced. The same evidence that defeated the attempt to always use argmax. is presented again. Only the ability to we need to control the distribution with temperature and optionally restrict it to a credible top set before sampling changes, so the repaired conclusion cannot be credited to a conveniently different example.

## The calculation hidden inside sampling

Before Sampling receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Sampling changes expression, not knowledge. No decoding rule can repair a model that assigned poor probabilities.

After “the tiger,” suppose *sleeps* is more likely than *runs*, but both make sense. Always choosing the winner makes every story follow the same path. Imagine a temperature dial on indecision: cooling enlarges the evidence gap and makes *sleeps* dominate; heating shrinks the gap and lets *runs* remain plausible. Dividing every logit by the same temperature implements that dial before sampling.

### Names for pieces we have already used

**ℓ_i** is candidate i's raw logit.
**T** is temperature: dividing by T changes score gaps before exponentiation.
T<1 enlarges gaps and sharpens choices; T>1 shrinks gaps and spreads probability.
Exponentiation preserves ranking while making evidence positive.
Summing over every j and dividing normalizes the adjusted evidence into p_i(T).

### Why no cheaper operation does the same job

[Dividing every logit by T](../../MATHEMATICAL_MOVES.md#division) changes score gaps before probabilities are formed. T below one enlarges gaps; T above one shrinks them. Adding T would shift every score equally and softmax would not change at all.
[Exponentiation](../../MATHEMATICAL_MOVES.md#exponential) then turns the adjusted gaps into positive ratios, while [summing](../../MATHEMATICAL_MOVES.md#summation) and dividing make one probability distribution.

The notation is finally shorter than the story that created it:

$$
p_i(T)=\frac{e^{\ell_i/T}}{\sum_j e^{\ell_j/T}}
$$

The equation arrives after every operation has a job.

## Sampling beyond this one case

A musician follows likely notes but sometimes chooses another harmonious option; neither rigid repetition nor random keys make music.

## Take sampling to the workbench

The argument for sampling is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running sampling, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the sampling result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 044](../044-context-window/README.md)
