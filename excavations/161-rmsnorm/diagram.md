# Diagram — RMSNorm — Do We Need to Subtract the Centre?

```mermaid
flowchart LR
    X["features: 3, 4"] --> S["squares: 9, 16"]
    S --> A["mean square: 12.5"]
    A --> R["root: 3.54"]
    R --> N["divide features by 3.54"]
```

```text
[3,4] and [30,40] -> same normalized direction
```

<!-- memory-film-v1:start -->
## Five-frame memory film

```text
QUESTION       What fails if we delete normalization because each individual operation appears cheap?
     ↓
OBJECT         the rmsnorm lens mounted on the brass reference machine
     ↓
VISIBLE BREAK  The lens follows the tempting path—delete normalization because each individual operation appears cheap. Then the evidence answers: deep residual streams drift in scale and training destabilizes; the repeated control was doing essential work.
     ↓
TRANSFORMATION The enginewright changes one moving part. The lens can now keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable.
     ↓
MEMORY SEAL    RMSNorm keeps the missing power: keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable.
```
<!-- memory-film-v1:end -->
