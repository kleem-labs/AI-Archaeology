# Mistakes — Excavation 162

## Tempting idea

Keep post-normalization because each block's output then looks standardized before the next block.

## Evidence that breaks it

The supposedly clean output places normalization directly on the identity route every gradient must cross, making the long residual path harder to preserve.

## Requirement carried forward

Normalize only the input to the changing branch and let the identity stream pass around it unchanged.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
