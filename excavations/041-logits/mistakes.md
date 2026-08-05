# Mistakes — 041

## Naive idea

Choose the nearest input embedding directly. That restricts the scoring rule and hides how every vocabulary candidate should compete.

## Failure

Logits have no standalone probability meaning and can shift together without changing the final distribution.

## Discovery

Use a learned linear map to produce one raw score for every vocabulary item.
