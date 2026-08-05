# Mistakes — 042

## Naive idea

Divide each logit by their sum. Negative values break probability and shifting all scores changes the result.

## Failure

A probability distribution expresses model confidence, not truth. Poor calibration and biased data remain possible.

## Discovery

Exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token.
