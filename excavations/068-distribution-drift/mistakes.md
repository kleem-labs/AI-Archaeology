# Mistakes — 068

## First idea

Assume training accuracy remains valid forever.

## Counterexample

A winter-trained demand model meets summer behavior and keeps reporting confident old patterns.

## Repair

Monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining.
