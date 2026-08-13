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
