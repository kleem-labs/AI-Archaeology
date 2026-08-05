# Mistakes — 029

## Wrong Idea #1

Set every weight to zero. Neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate.

## Why it fails

Useful learners must begin different from one another without making signals vanish or explode.

## Correct idea

Draw small random weights whose scale depends on how many inputs feed the neuron.
