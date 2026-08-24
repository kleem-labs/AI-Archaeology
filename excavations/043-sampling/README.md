# Excavation 043 — Sampling — Choosing Without Always Taking the Maximum

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Softmax turns vocabulary scores into a distribution. Generation now faces a choice that training did not settle: should the machine always take the winner or sometimes follow another plausible continuation?

Night gathers around the Clockwork Scriptorium. Under the light of the sentence-wheel, the mechanist refuses to invent prematurely and begins with the plain rule: always use argmax.

The rule survives the easy cases. The next case leaves a crack through the middle of it: the same prompt follows the same narrow path. Sample raw probabilities blindly. Low-quality tail tokens eventually derail the text. More confidence cannot repair information that never entered the rule.

*The mechanist sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: always use argmax
possible road B ─┘              └── loses: the same prompt follows the same…

same roads ──▶ repaired map ──▶ we need to control the distribution…
```

Two trails now cross the sentence-wheel. The pale trail bears the instruction “always use argmax.” It disappears into the observed failure: the same prompt follows the same narrow path. Sample raw probabilities blindly. Low-quality tail tokens eventually derail the text. The darker trail carries one additional capacity—to control the distribution with temperature and optionally restrict it to a credible top set before sampling. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed sampling mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the sentence-wheel is altered in exactly one way: we need to control the distribution with temperature and optionally restrict it to a credible top set before sampling. Much later, people will call this territory **Sampling**. Here the name is only a memory of the failure it can survive.

The sentence-wheel has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and sampling looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

## The calculation hidden inside sampling

The mechanist carries the sampling scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Sampling changes expression, not knowledge. No decoding rule can repair a model that assigned poor probabilities.

After “the tiger,” suppose *sleeps* is more likely than *runs*, but both make sense. Always choosing the winner makes every story follow the same path. Imagine a temperature dial on indecision: cooling enlarges the evidence gap and makes *sleeps* dominate; heating shrinks the gap and lets *runs* remain plausible. Dividing every logit by the same temperature implements that dial before sampling.

### Naming what is already on the table

**ℓ_i** is candidate i's raw logit.
**T** is temperature: dividing by T changes score gaps before exponentiation.
T<1 enlarges gaps and sharpens choices; T>1 shrinks gaps and spreads probability.
Exponentiation preserves ranking while making evidence positive.
Summing over every j and dividing normalizes the adjusted evidence into p_i(T).

### Why the melody needs these exact notes

[Dividing every logit by T](../../MATHEMATICAL_MOVES.md#division) changes score gaps before probabilities are formed. T below one enlarges gaps; T above one shrinks them. Adding T would shift every score equally and softmax would not change at all.
[Exponentiation](../../MATHEMATICAL_MOVES.md#exponential) then turns the adjusted gaps into positive ratios, while [summing](../../MATHEMATICAL_MOVES.md#summation) and dividing make one probability distribution.

The symbols are about to change costume, but their work has appeared before: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; **the rising flame**—a small score difference becomes positive relative evidence; and **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. This is how distant excavations begin to sound like variations of one melody.

The mechanist reads the journey of sampling once more across the sentence-wheel, then lets the words contract without losing their order:

$$
p_i(T)=\frac{e^{\ell_i/T}}{\sum_j e^{\ell_j/T}}
$$

The equation arrives after every operation has a job.

## Sampling beyond this one case

A musician follows likely notes but sometimes chooses another harmonious option; neither rigid repetition nor random keys make music.

## Return to the sentence-wheel

Rebuild the sampling scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 044](../044-context-window/README.md)
