# Mistakes — 023

## Wrong Idea #1

Measure only the first effect or only the final effect. Either breaks the causal path. Recompute the whole network separately for every weight; that repeats enormous amounts of work.

**Problem:** Branches require sensitivities from every downstream path to be added, not merely one chain followed.

## Correct Idea

Multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward.
