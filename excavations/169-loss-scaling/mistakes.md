# Mistakes — Excavation 169

## Tempting idea

Increase the learning rate so small updates become visible.

## Evidence that breaks it

The learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update.

## Requirement carried forward

Multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
