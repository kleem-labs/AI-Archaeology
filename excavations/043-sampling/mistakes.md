# Mistakes — 043

## Naive idea

Always use argmax. The same prompt follows the same narrow path. Sample raw probabilities blindly. Low-quality tail tokens eventually derail the text.

## Failure

Sampling changes expression, not knowledge. No decoding rule can repair a model that assigned poor probabilities.

## Discovery

Control the distribution with temperature and optionally restrict it to a credible top set before sampling.
