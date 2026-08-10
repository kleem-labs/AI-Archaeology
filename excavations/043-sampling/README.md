# Excavation 043 — Sampling — Choosing Without Always Taking the Maximum

[Previous: Excavation 042](../042-vocabulary-probabilities/README.md)

The model predicts several plausible next tokens. Taking only the highest probability makes generation repetitive and brittle.

At first, the simplest answer is tempting: Always use argmax. The same prompt follows the same narrow path. Sample raw probabilities blindly. Low-quality tail tokens eventually derail the text.

The missing information determines the next move: Control the distribution with temperature and optionally restrict it to a credible top set before sampling.

## From procedure to notation

Sampling changes expression, not knowledge. No decoding rule can repair a model that assigned poor probabilities.



## Build each piece from what just happened

After “the tiger,” suppose *sleeps* is more likely than *runs*, but both make sense. Always choosing the winner makes every story follow the same path. Imagine a temperature dial on indecision: cooling enlarges the evidence gap and makes *sleeps* dominate; heating shrinks the gap and lets *runs* remain plausible. Dividing every logit by the same temperature implements that dial before sampling.

### Give Short Names Only After We Know the Pieces

- **ℓ_i** is candidate i's raw logit.
- **T** is temperature: dividing by T changes score gaps before exponentiation.
- T<1 enlarges gaps and sharpens choices; T>1 shrinks gaps and spreads probability.
- Exponentiation preserves ranking while making evidence positive.
- Summing over every j and dividing normalizes the adjusted evidence into p_i(T).

Only now can we compress that reasoning:

$$
p_i(T)=\frac{e^{\ell_i/T}}{\sum_j e^{\ell_j/T}}
$$


The equation arrives after every operation has a job.

## Carry the idea back into the world

A musician follows likely notes but sometimes chooses another harmonious option; neither rigid repetition nor random keys make music.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 044](../044-context-window/README.md)
