# Mistakes — 053

## First idea

Write one perfect target response for every prompt and train only to imitate it.

## Counterexample

Many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer.

## Repair

Collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy.
