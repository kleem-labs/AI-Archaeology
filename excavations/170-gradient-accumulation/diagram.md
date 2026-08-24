# Diagram — Gradient Accumulation — Build a Large Batch That Does Not Fit

```mermaid
sequenceDiagram
    participant M as Gradient memory
    participant O as Optimizer
    loop four micro-batches
        M->>M: add unscaled gradient; do not update
    end
    M->>O: divide accumulated advice by 4
    O->>O: take one optimizer step
```

```text
8 + 8 + 8 + 8 examples -> one effective batch of 32
```

<!-- memory-film-v1:start -->
## Five-frame memory film

```text
QUESTION       What fails if we reduce the batch until it fits and change nothing else?
     ↓
OBJECT         the gradient accumulation gate mounted on the brass reference machine
     ↓
VISIBLE BREAK  The gate follows the tempting path—reduce the batch until it fits and change nothing else. Then the evidence answers: the gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together.
     ↓
TRANSFORMATION The enginewright changes one moving part. The gate can now run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step.
     ↓
MEMORY SEAL    Gradient Accumulation keeps the missing power: run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step.
```
<!-- memory-film-v1:end -->
