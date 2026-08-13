# Mistakes — Excavation 165

## Tempting idea

Use the same raw gradient step scale for every parameter.

## Evidence that breaks it

A rate safe for frequent large gradients barely moves sparse coordinates; a rate large enough for sparse coordinates makes noisy ones unstable.

## Requirement carried forward

Keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
