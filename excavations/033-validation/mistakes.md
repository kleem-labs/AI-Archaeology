# Mistakes — 033

## Wrong Idea #1

Use training loss for every choice; it rewards memorization. Check the test set repeatedly; every decision leaks test information back into development.

## Why it fails

One unseen set must guide choices, while another remains untouched for the final estimate.

## Correct idea

Split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end.
