# Mistakes — Excavation 189

## Tempting idea

Drop the rate abruptly near the end of training.

## Evidence that breaks it

A sudden cliff changes update scale in one step and makes the chosen drop date an arbitrary discontinuity; dropping too early freezes useful learning.

## Requirement carried forward

Decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state.

The wrong idea remains because its failure exposes information the successful design must preserve.
