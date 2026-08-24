# Mistakes Worth Preserving — Excavation 223

## The tempting idea

We tried to enumerate every possible full action sequence and total its reward independently.

## The evidence that refused it

the number of paths grows exponentially with horizon, and shared suffixes are recomputed. A ten-step tree may contain many copies of the same state with the same remaining problem.

## What the wreckage taught us

The next construction had to give each state one stored value equal to the best immediate reward plus the discounted expected value of its possible next states, then reuse that value wherever the state reappears.

Keep this wrong idea. It is the negative space around Dynamic Programming: it records why the accepted method has exactly the responsibilities it does.
